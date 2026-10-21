#!/usr/bin/env python3
"""QA gate for blog posts. Exit 1 on any FAIL.   usage: tools/qa_post.py [--skip-links] blog/src/*.md

FAIL: em/en dashes; a banned company name; missing front matter (title, slug, description <=160, date, updated,
author, tags, image on disk, 3-5 takeaways, 3-5 faq); paragraph over 90 words; body outside 900-1800 words;
http link not 200/301/302 (browser UA; 403/429 is a WARN); H2 that is neither a question nor a statement under 70 chars;
a published post (draft: false) with no internal link to another existing blog post.
WARN: sentence with a digit in a paragraph with no link (unsourced number); banned filler phrases.
Needs `markdown` installed only because the front matter parser lives in build_blog.py.
"""
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_blog import ROOT, SRC, parse_front_matter  # noqa: E402

REQUIRED = ("title", "slug", "description", "date", "updated", "author", "tags", "image", "takeaways", "faq")
BANNED = "tur" "gon"  # split so this file does not contain the word
FILLER = ("in today's", "whether you're", "it's important to note", "game changer", "delve")
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15"
OK_STATUS = {200, 301, 302, 303, 307, 308}
BOT_WALL = {403, 429}  # Zendesk/Cloudflare help centers refuse every scripted fetch; a 403 says nothing about the link
LINK = re.compile(r"\]\((https?://[^)\s]+)\)")
SENT = re.compile(r"(?<=[.!?])\s+")  # split on sentence end + space, so $19.99 stays whole


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


def check_link(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.9"})
    try:
        with urllib.request.build_opener(_NoRedirect).open(req, timeout=20) as r:
            return url, r.status
    except urllib.error.HTTPError as e:
        return url, e.code
    except Exception as e:  # DNS, timeout, TLS
        return url, type(e).__name__


def blocks(body):
    """Prose paragraphs only: skip tables, lists, callouts, headings, images, fences."""
    out, fence = [], False
    for block in re.split(r"\n\s*\n", body):
        b = block.strip()
        if not b:
            continue
        if b.startswith("```"):
            fence = not fence if b.count("```") % 2 else fence
            continue
        if fence or re.match(r"^(\||[-*] |\d+\. |!|#|>|<)", b):
            continue
        out.append(b)
    return out


def words(text):
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)  # images
    text = re.sub(r"\]\([^)]*\)", "]", text)  # link targets
    return len(text.split())


def qa(path, skip_links):
    fails, warns = [], []
    text = path.read_text(encoding="utf-8")
    for n, line in enumerate(text.splitlines(), 1):
        if "\u2014" in line or "\u2013" in line:
            fails.append(f"line {n}: em/en dash")
        if BANNED in line.lower():
            fails.append(f"line {n}: banned word")
        low = line.lower()
        for ph in FILLER:
            if ph in low:
                warns.append(f"line {n}: filler phrase '{ph}'")
    try:
        meta, body = parse_front_matter(text)
    except ValueError as e:
        return [f"front matter: {e}"], warns
    raw_keys = set(re.findall(r"^(\w+):", text.split("\n---\n", 1)[0], re.M))
    for k in REQUIRED:
        if k not in raw_keys:
            fails.append(f"front matter: missing {k}")
    if len(meta["description"]) > 160:
        fails.append(f"front matter: description is {len(meta['description'])} chars (max 160)")
    if not (ROOT / meta["image"]).is_file():
        fails.append(f"front matter: image {meta['image']} not on disk")
    if not 3 <= len(meta["takeaways"]) <= 5:
        fails.append(f"front matter: {len(meta['takeaways'])} takeaways (need 3-5)")
    if not 3 <= len(meta["faq"]) <= 5 or any("a" not in f for f in meta["faq"]):
        fails.append(f"front matter: {len(meta['faq'])} complete faq pairs (need 3-5)")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", meta["date"]) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", meta["updated"]):
        fails.append("front matter: date/updated must be YYYY-MM-DD")

    if not meta["draft"]:  # publish gate: a live post must point readers at another live post
        targets = set(re.findall(r"\]\((?:https://mealsaid\.app)?/blog/([a-z0-9-]+)/\)", body)) - {meta["slug"], "img"}
        live = {s for s in targets if (SRC / f"{s}.md").is_file()}
        if not live:
            fails.append("published post has no internal link to another blog post (link /blog/<slug>/)")
        for s in targets - live:
            fails.append(f"internal link to /blog/{s}/ but blog/src/{s}.md does not exist")

    n = words(body)
    if not 900 <= n <= 1800:
        fails.append(f"body is {n} words (need 900-1800)")
    for h in re.findall(r"^## (.+)$", body, re.M):
        if not h.rstrip().endswith("?") and len(h) >= 70:
            fails.append(f"H2 not a question and {len(h)} chars (max 69): {h!r}")
    for b in blocks(body):
        w = words(b)
        if w > 90:
            fails.append(f"paragraph of {w} words: {b[:60]!r}...")
        if "](" not in b:
            for s in SENT.split(b):
                if re.search(r"\d", s):
                    warns.append(f"unsourced number: {s.strip()[:90]!r}")
    if not skip_links:
        urls = sorted(set(LINK.findall(text)))
        with ThreadPoolExecutor(8) as ex:
            for url, status in ex.map(check_link, urls):
                if status in BOT_WALL:
                    warns.append(f"link {status} (bot wall, open it in a browser): {url}")
                elif status not in OK_STATUS:
                    fails.append(f"link {status}: {url}")
    return fails, warns


def main(argv):
    skip = "--skip-links" in argv
    paths = [Path(a) for a in argv if not a.startswith("--")]
    if not paths:
        sys.exit(__doc__)
    bad = 0
    for p in paths:
        fails, warns = qa(p, skip)
        bad += bool(fails)
        print(f"{'FAIL' if fails else 'PASS'} {p}  ({len(fails)} errors, {len(warns)} warnings)")
        for f in fails:
            print("  FAIL", f)
        for w in warns[:12]:
            print("  WARN", w)
        if len(warns) > 12:
            print(f"  WARN +{len(warns) - 12} more")
    print(f"\n{len(paths) - bad}/{len(paths)} passed")
    return 1 if bad else 0


def _selfcheck():
    assert words("see [a](https://x.y/) and ![img](/p.webp) b") == 4
    assert blocks("para one\n\n| t |\n|---|\n\n- li\n\n## H\n\n!stat 1 | x\n\npara two") == ["para one", "para two"]
    print("selfcheck ok")


if __name__ == "__main__":
    _selfcheck() if "--check" in sys.argv else sys.exit(main(sys.argv[1:]))
