#!/bin/sh
# Build the blog, commit, push, ping IndexNow.   usage: tools/publish.sh "commit message"
set -e
cd "$(dirname "$0")/.."
[ -x tools/.venv/bin/python ] || { python3 -m venv tools/.venv && tools/.venv/bin/pip -q install markdown; }
tools/.venv/bin/python tools/build_blog.py
git add -A
git diff --cached --quiet && { echo "nothing to publish"; exit 0; }
git commit -q -m "${1:-Publish blog}"
git push -q
python3 tools/indexnow.py --sitemap
