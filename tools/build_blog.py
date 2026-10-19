#!/usr/bin/env python3
"""Static blog generator for mealsaid.app. Stdlib + `markdown`.

blog/src/*.md  ->  blog/<slug>/index.html, blog/index.html,
                   sitemap.xml, feed.xml, robots.txt, llms.txt
Re-runnable, deterministic (no timestamps other than front matter dates).
"""
import html
import json
import re
import struct
import subprocess
import sys
from email.utils import format_datetime
from datetime import datetime, timezone
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "blog" / "src"
SITE = "https://mealsaid.app"
AUTHOR = "Om Divyatej"
APP_STORE = "https://apps.apple.com/app/id6818596412"
TESTFLIGHT = "https://testflight.apple.com/join/s6U7TMe1"
DEFAULT_IMAGE = "assets/og.png"
STATIC_PAGES = ["index.html", "privacy.html", "support.html", "creators.html"]

# ---------------------------------------------------------------- front matter
def parse_front_matter(text):
    """YAML-ish: `key: value`, `key: [a, b]`, and a `faq:` list of `- q:` / `  a:` pairs."""
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise ValueError("missing front matter")
    meta, body = {}, m.group(2)
    faq, cur = [], None
    for line in m.group(1).splitlines():
        if not line.strip():
            continue
        if cur is not None and line.startswith(" "):
            s = line.strip()
            if s.startswith("- q:"):
                cur.append({"q": s[4:].strip().strip('"')})
            elif s.startswith("a:"):
                cur[-1]["a"] = s[2:].strip().strip('"')
            else:
                raise ValueError(f"bad faq line: {line}")
            continue
        cur = None
        key, _, val = line.partition(":")
        key, val = key.strip(), val.strip()
        if key == "faq":
            cur = faq
        elif val.startswith("["):
            meta[key] = [v.strip().strip('"') for v in val.strip("[]").split(",") if v.strip()]
        else:
            meta[key] = val.strip('"')
    meta["faq"] = faq
    for k in ("title", "slug", "description", "date"):
        if k not in meta:
            raise ValueError(f"front matter missing {k}")
    meta.setdefault("updated", meta["date"])
    meta.setdefault("author", AUTHOR)
    meta.setdefault("tags", [])
    meta.setdefault("image", DEFAULT_IMAGE)
    meta["draft"] = meta.get("draft", "false").lower() == "true"
    return meta, body


# ---------------------------------------------------------------- helpers
def image_size(path):
    """(w, h) for PNG / WebP, else None."""
    with open(path, "rb") as f:
        head = f.read(30)
    if head[:8] == b"\x89PNG\r\n\x1a\n":
        return struct.unpack(">II", head[16:24])
    if head[:4] == b"RIFF" and head[8:12] == b"WEBP":
        chunk = head[12:16]
        if chunk == b"VP8X":
            w = int.from_bytes(head[24:27], "little") + 1
            h = int.from_bytes(head[27:30], "little") + 1
            return w, h
        if chunk == b"VP8 ":
            w, h = struct.unpack("<HH", head[26:30])
            return w & 0x3FFF, h & 0x3FFF
        if chunk == b"VP8L":
            b = head[21:25]
            w = 1 + (((b[1] & 0x3F) << 8) | b[0])
            h = 1 + (((b[3] & 0xF) << 10) | (b[2] << 2) | ((b[1] & 0xC0) >> 6))
            return w, h
    return None


def add_img_dims(html_body):
    def fix(m):
        tag = m.group(0)
        if "width=" in tag:
            return tag
        src = re.search(r'src="([^"]+)"', tag)
        p = ROOT / src.group(1).lstrip("/") if src else None
        if p and p.is_file() and (dims := image_size(p)):
            return tag[:-1].rstrip("/") + f' width="{dims[0]}" height="{dims[1]}" loading="lazy">'
        return tag
    return re.sub(r"<img [^>]*>", fix, html_body)


def iso(d):
    return datetime.strptime(d, "%Y-%m-%d").replace(tzinfo=timezone.utc)


def human(d):
    return iso(d).strftime("%B %-d, %Y")


def esc(s):
    return html.escape(s, quote=True)


def git_date(path):
    out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", path], cwd=ROOT,
                         capture_output=True, text=True, check=True).stdout.strip()
    if not out:
        raise RuntimeError(f"{path} is not committed; sitemap lastmod needs git history")
    return out


# ---------------------------------------------------------------- templates
HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="color-scheme" content="dark">
<meta name="theme-color" content="#080b12">
<link rel="canonical" href="{url}">
<link rel="alternate" type="application/rss+xml" title="MealSaid blog" href="{site}/feed.xml">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="MealSaid">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{image}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=optional">
<link rel="stylesheet" href="/blog/blog.css">
{jsonld}</head>
<body>
<header class="wrap">
  <div class="nav">
    <a class="brand" href="/" aria-label="MealSaid home"><img src="/assets/icon-192.png" width="30" height="30" alt="">MealSaid</a>
    <nav class="links"><a href="/blog/">Blog</a><a class="ghost" href="{testflight}">Join the beta</a></nav>
  </div>
</header>
<main class="wrap">
"""

FOOT = """</main>
<footer class="wrap">
  <span>© 2026 Turgon</span>
  <nav aria-label="Footer">
    <a href="/blog/">Blog</a>
    <a href="/privacy.html">Privacy</a>
    <a href="/support.html">Support</a>
    <a href="/feed.xml">RSS</a>
    <a href="mailto:om@turgon.ai">om@turgon.ai</a>
  </nav>
</footer>
</body>
</html>
"""

TRY_CARD = f"""<aside class="try">
  <h2>Try MealSaid</h2>
  <p>Say what you ate. It's logged into Apple Health with calories and macros. Forget? It calls you. Free, no ads, iPhone.</p>
  <div class="cta">
    <a class="btn primary" href="{APP_STORE}">Get it on the App Store</a>
    <a class="btn secondary" href="{TESTFLIGHT}">Join the TestFlight beta</a>
  </div>
</aside>
"""


def jsonld_blocks(*objs):
    return "".join('<script type="application/ld+json">' + json.dumps(o, ensure_ascii=False, separators=(",", ":")) + "</script>\n" for o in objs)


def render_post(p, prev_p, next_p):
    url = f"{SITE}/blog/{p['slug']}/"
    image = f"{SITE}/{p['image']}"
    article = {
        "@context": "https://schema.org", "@type": "Article",
        "headline": p["title"], "description": p["description"], "image": image,
        "datePublished": iso(p["date"]).isoformat(), "dateModified": iso(p["updated"]).isoformat(),
        "author": {"@type": "Person", "name": p["author"], "url": f"{SITE}/"},
        "publisher": {"@type": "Organization", "name": "MealSaid", "url": f"{SITE}/",
                      "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/icon-192.png", "width": 192, "height": 192}},
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "keywords": ", ".join(p["tags"]),
    }
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "MealSaid", "item": f"{SITE}/"},
        {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{SITE}/blog/"},
        {"@type": "ListItem", "position": 3, "name": p["title"], "item": url}]}
    ld = [article, crumbs]
    faq_html = ""
    if p["faq"]:
        ld.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in p["faq"]]})
        faq_html = '<section class="faq" aria-labelledby="faq-h"><h2 id="faq-h">Questions</h2>' + "".join(
            f"<details><summary>{esc(f['q'])}</summary><p>{esc(f['a'])}</p></details>" for f in p["faq"]) + "</section>\n"

    dates = f"Published {human(p['date'])}"
    if p["updated"] != p["date"]:
        dates += f" · Updated {human(p['updated'])}"
    nav = ""
    if prev_p or next_p:
        nav = '<nav class="pn" aria-label="More posts">'
        nav += f'<a href="/blog/{prev_p["slug"]}/" rel="prev"><small>Older</small>{esc(prev_p["title"])}</a>' if prev_p else "<span></span>"
        nav += f'<a href="/blog/{next_p["slug"]}/" rel="next"><small>Newer</small>{esc(next_p["title"])}</a>' if next_p else "<span></span>"
        nav += "</nav>\n"

    head = HEAD.format(title=esc(p["title"]), description=esc(p["description"]), url=url, site=SITE, og_type="article",
                       image=image, testflight=TESTFLIGHT, jsonld=jsonld_blocks(*ld))
    body = (f'<article>\n<header class="post-head">\n<p class="crumbs"><a href="/blog/">Blog</a></p>\n'
            f'<h1>{esc(p["title"])}</h1>\n<p class="lede">{esc(p["description"])}</p>\n'
            f'<p class="meta"><time datetime="{p["date"]}">{dates}</time></p>\n'
            f'<p class="meta">{esc(p["author"])}, founder of MealSaid</p>\n</header>\n'
            f'<div class="prose">\n{p["html"]}\n</div>\n{faq_html}</article>\n{TRY_CARD}{nav}')
    return head + body + FOOT


def render_index(posts):
    url = f"{SITE}/blog/"
    items = "".join(
        f'<li><a href="/blog/{p["slug"]}/"><h2>{esc(p["title"])}</h2><p>{esc(p["description"])}</p>'
        f'<small><time datetime="{p["date"]}">{human(p["date"])}</time>'
        + (f' · Updated <time datetime="{p["updated"]}">{human(p["updated"])}</time>' if p["updated"] != p["date"] else "")
        + "</small></a></li>\n" for p in posts)
    ld = [{"@context": "https://schema.org", "@type": "Blog", "name": "MealSaid blog", "url": url,
           "publisher": {"@type": "Organization", "name": "MealSaid", "url": f"{SITE}/"}},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "MealSaid", "item": f"{SITE}/"},
              {"@type": "ListItem", "position": 2, "name": "Blog", "item": url}]}]
    head = HEAD.format(title="MealSaid blog", description="Notes from building MealSaid, the calorie tracker you talk to.",
                       url=url, site=SITE, og_type="website", image=f"{SITE}/{DEFAULT_IMAGE}", testflight=TESTFLIGHT,
                       jsonld=jsonld_blocks(*ld))
    body = ('<header class="post-head"><h1>Blog</h1><p class="lede">Notes from building MealSaid, the calorie tracker you talk to.</p></header>\n'
            f'<ul class="posts">\n{items}</ul>\n{TRY_CARD}')
    return head + body + FOOT


def render_sitemap(posts):
    rows = [(f"{SITE}/", git_date("index.html"))] + [(f"{SITE}/{p}", git_date(p)) for p in STATIC_PAGES[1:]]
    rows.append((f"{SITE}/blog/", max(p["updated"] for p in posts)))
    rows += [(f"{SITE}/blog/{p['slug']}/", p["updated"]) for p in posts]
    body = "".join(f"  <url><loc>{u}</loc><lastmod>{d}</lastmod></url>\n" for u, d in rows)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}</urlset>\n'


def render_feed(posts):
    items = "".join(
        f"  <item>\n    <title>{esc(p['title'])}</title>\n    <link>{SITE}/blog/{p['slug']}/</link>\n"
        f"    <guid isPermaLink=\"true\">{SITE}/blog/{p['slug']}/</guid>\n"
        f"    <pubDate>{format_datetime(iso(p['date']))}</pubDate>\n"
        f"    <description>{esc(p['description'])}</description>\n"
        f"    <content:encoded><![CDATA[{p['html']}]]></content:encoded>\n  </item>\n" for p in posts)
    last = format_datetime(iso(max(p["updated"] for p in posts)))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:content="http://purl.org/rss/1.0/modules/content/">\n<channel>\n'
            f"  <title>MealSaid blog</title>\n  <link>{SITE}/blog/</link>\n"
            "  <description>Notes from building MealSaid, the calorie tracker you talk to.</description>\n"
            f"  <language>en</language>\n  <lastBuildDate>{last}</lastBuildDate>\n"
            f'  <atom:link href="{SITE}/feed.xml" rel="self" type="application/rss+xml"/>\n{items}</channel>\n</rss>\n')


ROBOTS = """# mealsaid.app. Everyone welcome, including AI crawlers.
User-agent: *
Allow: /

# AI / answer-engine crawlers, listed explicitly so the intent is clear.
User-agent: GPTBot
User-agent: OAI-SearchBot
User-agent: ChatGPT-User
User-agent: ClaudeBot
User-agent: Claude-SearchBot
User-agent: Claude-User
User-agent: anthropic-ai
User-agent: PerplexityBot
User-agent: Perplexity-User
User-agent: Google-Extended
User-agent: Googlebot
User-agent: Bingbot
User-agent: Applebot
User-agent: Applebot-Extended
User-agent: CCBot
User-agent: Amazonbot
User-agent: DuckDuckBot
Allow: /

Sitemap: https://mealsaid.app/sitemap.xml
"""


def render_llms(posts):
    links = "".join(f"- [{p['title']}]({SITE}/blog/{p['slug']}/): {p['description']}\n" for p in posts)
    return f"""# MealSaid

> MealSaid is a free iPhone app that logs what you ate by voice. You say "two eggs, toast and a coffee", and calories, protein, carbs, fat and fiber are estimated and written into Apple Health in about a second. If you forget to log, the app calls your phone at times you picked, asks what you ate, and waits until you finish. It also logs workouts. No ads, no in-app purchases, no tracking. Sign in with Apple is the only login. English only. Requires iOS 26. Built by Om Divyatej (Turgon). Voice is processed by our server, OpenAI and Anthropic and is not stored. Apple Health data never leaves the phone.

## Key pages

- [Home]({SITE}/): what the app does, screenshots, FAQ
- [App Store]({APP_STORE}): download
- [TestFlight beta]({TESTFLIGHT}): early builds
- [Privacy policy]({SITE}/privacy.html): what is sent off the phone and what is kept
- [Support]({SITE}/support.html): fixes for mic, Health, and call problems; account deletion
- [Blog]({SITE}/blog/): notes from building MealSaid
- [RSS]({SITE}/feed.xml)

## Blog posts

{links}"""


# ---------------------------------------------------------------- main
def load_posts():
    md = markdown.Markdown(extensions=["tables", "fenced_code", "attr_list", "toc"], extension_configs={"toc": {"toc_depth": "2-3"}})
    posts = []
    for f in sorted(SRC.glob("*.md")):
        meta, body = parse_front_matter(f.read_text(encoding="utf-8"))
        if meta["draft"]:
            continue
        md.reset()
        meta["html"] = add_img_dims(md.convert(body))
        posts.append(meta)
    posts.sort(key=lambda p: (p["date"], p["slug"]), reverse=True)
    return posts


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.read_text(encoding="utf-8") != text:
        path.write_text(text, encoding="utf-8")
        print("wrote", path.relative_to(ROOT))


def main():
    posts = load_posts()
    if not posts:
        sys.exit("no posts in blog/src")
    for i, p in enumerate(posts):  # newest first: prev = older = i+1
        write(ROOT / "blog" / p["slug"] / "index.html",
              render_post(p, posts[i + 1] if i + 1 < len(posts) else None, posts[i - 1] if i > 0 else None))
    write(ROOT / "blog" / "index.html", render_index(posts))
    write(ROOT / "sitemap.xml", render_sitemap(posts))
    write(ROOT / "feed.xml", render_feed(posts))
    write(ROOT / "robots.txt", ROBOTS)
    write(ROOT / "llms.txt", render_llms(posts))
    print(f"{len(posts)} post(s)")


def _selfcheck():
    meta, body = parse_front_matter('---\ntitle: T\nslug: t\ndescription: D\ndate: 2026-01-02\ntags: [a, b]\nfaq:\n  - q: Q1\n    a: A1\n---\n# hi\n')
    assert meta["tags"] == ["a", "b"] and meta["faq"] == [{"q": "Q1", "a": "A1"}] and meta["updated"] == "2026-01-02"
    assert body == "# hi\n" and meta["draft"] is False
    assert image_size(ROOT / "assets" / "og.png") == (1200, 630)
    assert image_size(ROOT / "assets" / "home.webp") == (780, 1695)
    print("selfcheck ok")


if __name__ == "__main__":
    _selfcheck() if "--check" in sys.argv else main()
