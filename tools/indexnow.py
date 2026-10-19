#!/usr/bin/env python3
"""Submit URLs to IndexNow (Bing, Yandex, Naver, Seznam share the index).

usage: indexnow.py URL [URL ...]      or      indexnow.py --sitemap
Key = the 32-hex <key>.txt file at the site root.
"""
import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOST = "mealsaid.app"

key_file = next(p for p in ROOT.glob("*.txt") if re.fullmatch(r"[0-9a-f]{32}", p.stem))
urls = sys.argv[1:]
if urls == ["--sitemap"]:
    urls = re.findall(r"<loc>(.*?)</loc>", (ROOT / "sitemap.xml").read_text())
if not urls:
    sys.exit(__doc__)

body = json.dumps({"host": HOST, "key": key_file.stem, "keyLocation": f"https://{HOST}/{key_file.name}", "urlList": urls}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow", body, {"Content-Type": "application/json; charset=utf-8"})
try:
    with urllib.request.urlopen(req) as r:
        print(f"IndexNow {r.status} for {len(urls)} URL(s)")
except urllib.error.HTTPError as e:
    sys.exit(f"IndexNow {e.code}: {e.read().decode()}")
