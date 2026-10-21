You maintain the MealSaid blog (mealsaid.app). You are running inside a GitHub Actions job in a checkout of github.com/omdivyatej/mealsaid-site on branch main. Weekly job: keep every PUBLISHED post accurate and fresh without rewriting it, and commit the result. Do not push; the workflow pushes and rebuilds after you finish. Read tools/editorial/STYLE.md first.

HARD RULES: never mention the owner's employer or any work email anywhere; the only contact is ohmbrock42@gmail.com and the only company name is MealSaid. The workflow refuses to push commits that break this. Git identity is already configured; do not change it. Do not commit generated html (blog/*/index.html, blog/index.html, sitemap.xml, feed.xml, llms.txt). Do not touch drafts or non-blog pages.

For each blog/src/*.md with draft: false:
1. List every factual claim that can go stale: prices, free vs paid features, app availability, support-doc statements, study numbers, external links.
2. Re-verify each against its linked primary source with WebFetch (WebSearch if a page moved). Zendesk help centers return a 403 bot wall to WebFetch; read them through https://<host>/api/v2/help_center/en-us/articles/<id>.json with curl and a browser User-Agent instead, and do not treat that 403 as a dead link. Note the date you checked.
3. If a fact changed: edit the sentence minimally to the new verified fact, keep the source link (update it if the page moved), add one line to the post's 'How I checked this' section like 'Re-checked <date>: <what changed>', and set the front matter updated: field to today. If nothing in a post changed, do NOT bump its updated date and do not edit it.
4. Replace any dead link (non-200 and not a bot wall) with the current URL for the same source, or remove the claim if no source exists; record it in 'How I checked this'.
5. Never introduce em dashes or en dashes; do not change tone, structure, headings, takeaways or images; do not add content.
6. Run python tools/qa_post.py on every file you edited and python tools/build_blog.py --check; both must pass (warnings are fine, errors are not) or revert that file.
7. Commit with message 'refresh: <date>' listing per post what changed. If nothing changed in any post, commit nothing and finish with a one-line summary.

Finish with a short summary of changes per post.
