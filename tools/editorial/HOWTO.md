# Daily drafting routine

1. Read `STYLE.md`, then take the top row in `BACKLOG.md` with status `todo` (never a "needs Om's phone test" row).
2. Research with web search, primary sources only: the app's own support page or App Store listing, the journal article, USDA FoodData Central. Note the date you read each page; it goes in the post.
3. Write `blog/src/<slug>.md` with `draft: true` and the full front matter from the STYLE schema. No em dashes anywhere.
4. Charts: add one function per post to `tools/blog_images.py` (pattern: `im, d = canvas()`, draw with `text()`, `d.line`, `d.rounded_rectangle`, end with `source(d, "Source: ...")` and `save(im, "<slug>-1.webp")`), call it from `__main__`, run `pip install pillow` then `BLOG_FONT=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf python tools/blog_images.py` on Linux (on Om's Mac the default font works). Commit the `.webp`.
5. Run `pip install markdown` then `python tools/qa_post.py blog/src/<slug>.md` and fix every FAIL; read every WARN and either add the source link or cut the number.
6. Preview if useful: `python tools/build_blog.py --include-drafts` (do not commit the generated HTML; CI builds it).
7. Flip the row in `BACKLOG.md` to `drafted`, in the same commit.
8. Commit to branch `draft/<slug>` and open a PR titled `Draft: <title>`. Body = the full `qa_post.py` report, then "Five claims I am least sure of" (each with the sentence and why), then the source list with the date read.
9. Publishing is human only: Om reviews, sets `draft: false`, sets `date` and `updated` to the publish day, merges to `main`. CI then builds the HTML, commits it back, and pings IndexNow. Nothing else to do.
10. The next day, if yesterday's PR is still open, do not touch it; take the next `todo` row.
