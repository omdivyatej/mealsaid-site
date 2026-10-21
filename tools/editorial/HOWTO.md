# Daily routine: write, self-review, publish

1. Read `STYLE.md`, then take the top `todo` row in `BACKLOG.md` (or a `drafted (blocked: ...)` row you can now clear). Never a "needs Om's phone test" row.
2. Research with web search, primary sources only: the app's own support page or App Store listing, the journal article, USDA FoodData Central. Note the date you read each page; it goes in the post.
3. Write `blog/src/<slug>.md` with `draft: true` and the full front matter from the STYLE schema. Link at least one other post on the blog. No em dashes anywhere.
4. Charts: add one function per post to `tools/blog_images.py` (pattern: `im, d = canvas()`, draw with `text()`, `d.line`, `d.rounded_rectangle`, end with `source(d, "Source: ...")` and `save(im, "<slug>-1.webp")`), call it from `__main__`, then `pip install pillow` and on Linux `BLOG_FONT=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf python tools/blog_images.py` (Om's Mac uses the default font). Commit the `.webp`.
5. Self-review against the rubric below, up to 3 rounds. Score each of the 7 lines 1 to 5 and fix anything under 4 before the next round. Write the final scores in the commit message.
6. Gate, all three must pass: every rubric line is 4 or 5; `pip install markdown && python tools/qa_post.py blog/src/<slug>.md` prints PASS (read every WARN, then add the source link or cut the number); `python tools/build_blog.py --check` prints "selfcheck ok" and `python tools/build_blog.py --include-drafts` builds without error (do not commit the generated HTML; CI builds it).
7. Gate passed: set `draft: false`, set `date` and `updated` to today, flip the BACKLOG row to `published` with the link `https://mealsaid.app/blog/<slug>/`. Gate failed after 3 rounds: leave `draft: true`, flip the row to `drafted (blocked: <one line>)`.
8. Commit `blog/src/<slug>.md`, the `.webp` files, `tools/blog_images.py` and `BACKLOG.md` in one commit and push straight to `main`. Never put the text "[skip ci]" in the commit message; it stops the Action.
9. The Action builds the HTML, commits it back as "ci: build blog [skip ci]", and pings IndexNow. Check `gh run list -w publish -L 1` is green and `https://mealsaid.app/blog/<slug>/` returns 200 within about three minutes. If red, fix forward with another push.
10. Done for the day. One post a day is the ceiling; a second post is never a good use of the slot. If a published post's facts change (price, paywall), update that post, bump `updated`, and push; that is a real update, not a new post.

## Rubric (score 1 to 5; publish needs every line at 4 or above)

| Line | 5 looks like |
|---|---|
| Formatting | Front matter complete, H2s are questions or short statements, bold one-line answer under each, paragraphs of 3 sentences or fewer, no dashes |
| Images | First image is our own chart with title, source line and real numbers; every image has descriptive alt text; no stock, no AI art, no chrome |
| Tables | Exactly one table when the topic is comparative, columns are what people ask, every cell verified against a linked source on a stated date |
| Style | Reads as Om after a test: first person, result first, exact numbers, a loss admitted, no filler words, no triads, no summary section |
| SEO | Title is the question plus the hook, description under 160 characters with the key number, slug matches, internal link present, date and updated set |
| GEO | Answer in the first two sentences, each H2 answerable on its own, takeaways and FAQ quotable without the post, sources linked with sample sizes |
| Facts | Every number traces to a primary source read today; MealSaid claims come only from the STYLE facts block or a linked published post; competitors credited |
