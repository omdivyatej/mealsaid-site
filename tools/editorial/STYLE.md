# MealSaid blog style

Every post is a first-person note from Om, the person who built the app. It reads like someone who measured something and is telling you the result, not like marketing. `tools/qa_post.py` enforces the mechanical parts of this file; the rest is judgement.

## Voice

- First person, "I". Om checked the pages, ran the test, got it wrong once and says so.
- Answer in the first two sentences of the post. The verdict and the key number come before any H2.
- Open with the result. "Lose It imports dietary energy, MyFitnessPal does not." Never "Calorie tracking has come a long way."
- Exact numbers with units, odd ones. 47 seconds, $79.99 a year, 2.58% of 189,770. Not "under a minute", not "most".
- Say how you know in one plain sentence. "I read each app's own support page on 20 October 2026."
- Include the loss. Where MealSaid is worse, say so in the same tone as everything else.
- Short paragraphs, three sentences at most. Vary sentence length. One-line paragraphs are fine.
- Sentence case headings. End when the information ends. No "Conclusion", no "Final thoughts", no summary section.

## Structure (what the build and the QA expect)

1. Front matter (schema below), then two or three opening paragraphs that answer the question.
2. Each H2 is either the question people type ("Why are my calories doubled in Apple Health?") or a short plain statement under 70 characters ("The app calls you").
3. The first line under every H2 is one bold sentence that answers it on its own. Then the detail.
4. Exactly one comparison table per post, when the topic is comparative. Columns are what people ask: price a year, free tier, ads, voice, Apple Health write, reminders.
5. One or two `!stat` callouts at most (`!stat 2.58% | stayed active past a week | [Helander 2014](url)`). A stat callout never repeats a number that a chart in the same post already shows.
6. 3 to 5 takeaways and 3 to 5 FAQ pairs in front matter. Each one is a complete sentence a reader could quote without the post.
7. A final `## How I checked this` section that starts with "Checked <day month year>." and says what was read or measured, on which device, and what could not be verified.
8. Body between 900 and 1,800 words. Fit the question; an answer page can be short.

## Sources and quotes

- Every number links to its source in the same paragraph, with the sample size when there is one ("n = 212", "189,770 downloads").
- Link to primary sources: the company's own support page or App Store listing, the journal article, USDA FoodData Central. Not a roundup that cites them.
- Quote at most once per source, under 15 words, in quotation marks, with the link.
- Credit competitors by name and link to them. If Cronometer does something better, say "Cronometer does this better" and link.
- State MealSaid's gaps plainly wherever they are relevant (see the facts block below).
- Dated claims carry the date in the sentence. Prices and paywalls change; the "Checked" date is part of the fact.

## Banned

- Em dashes and en dashes, anywhere, including front matter and alt text. Use a comma, a period or parentheses.
- "In today's", "whether you're", "it's important to note", "game changer", "delve", "seamless", "robust", "leverage", "elevate", "landscape", "journey", "let's dive in", "in conclusion".
- Triads ("fast, accurate and effortless"). Two items or four.
- "Not just X, but Y" and "It's not about X, it's about Y".
- Bold-label bullet lists where every bullet is "**Feature:** explanation".
- Title Case headings. Hedging every row; pick a winner per row.
- Identical section shapes (every section same length with the same sub-headings).
- Numbers you cannot link. If the only source is memory, cut the number.

## Images

- Only two kinds: charts we render ourselves with `tools/blog_images.py`, or real screenshots of the app (Om supplies those from his phone; the cloud routine does not invent them).
- Never stock photos, never AI-generated art, never decorative icons, no card chrome or borders around figures.
- Charts: 1600 x 900, background `#0b0e13`, text `#f3f5f8`, accent `#d6ff3d`, one idea per chart, title at top left in plain words, a one-line "Source: ..." at the bottom with sample size and date. Saved as WebP under 150 KB, named `blog/img/<slug>-<n>.webp`.
- The front matter `image` is the first chart. It doubles as the social preview.
- Alt text describes what the chart shows, including the key numbers, in one sentence. No dashes.

## Front matter schema

```
---
title: Which calorie apps actually write to (and read from) Apple Health
slug: calorie-apps-apple-health
description: One sentence with the key number, 160 characters or fewer.
date: 2026-10-20
updated: 2026-10-20
author: Om Divyatej
tags: [apple health, healthkit, mealsaid]
image: blog/img/calorie-apps-apple-health-1.webp
draft: true
takeaways:
  - Complete sentence a reader could quote on its own.
  - Three to five of these.
  - Each with its number.
faq:
  - q: A question people type into a search box?
    a: A two-sentence answer that stands alone.
  - q: Three to five pairs.
    a: Each answer is specific.
---
```

`draft: true` keeps the post out of the build. A human flips it to `false` to publish. `medium:` is optional and is added by Om after cross-posting.

## Facts you may state about MealSaid

- Free. No ads, no in-app purchases, no subscription.
- iPhone only, requires iOS 26. No Android, no iPad-specific version, no web app.
- English only.
- You say what you ate; it estimates calories, protein, carbs, fat and fiber and writes them to Apple Health as dietary energy, protein, carbohydrates, total fat and fiber. It also logs workouts to Apple Health.
- Speech to text runs on the phone. The text goes to our server and a language model turns it into entries. Nothing is recorded or stored on our side. Apple Health data stays on the phone.
- The app calls you: at times you pick, your iPhone rings with a normal incoming call from MealSaid, a voice asks what you ate, and it waits until you finish. Calls are skipped if you logged recently.
- You can also log from Siri ("Hey Siri, log in MealSaid, two eggs and toast"), a Lock Screen control and a Home Screen widget, without opening the app.
- Sign in with Apple is the only login.
- No barcode scanner, no photo logging, no food database search, no restaurant menus, no recipe builder.
- It does not import food logged by other apps from Apple Health.
- Contact: ohmbrock42@gmail.com
- Links: https://mealsaid.app, App Store https://apps.apple.com/app/id6818596412, TestFlight https://testflight.apple.com/join/s6U7TMe1

Anything about MealSaid not on this list (accuracy numbers, user counts, timings, roadmap) is not to be stated until Om has measured it and it is in a published post you can link to.
