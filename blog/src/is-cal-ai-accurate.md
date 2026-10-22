---
title: Is Cal AI accurate? It missed 345 calories a meal
slug: is-cal-ai-accurate
description: Cal AI says it is about 80% accurate. In an NIH test of 102 weighed meals it came in 345 calories low, the biggest miss of the four photo apps tested.
date: 2026-10-22
updated: 2026-10-22
author: Om Divyatej
tags: [cal ai, accuracy, photo logging, research, mealsaid]
image: blog/img/is-cal-ai-accurate-1.webp
draft: false
takeaways:
  - In an NIH test of 102 meals weighed to 0.1 g, Cal AI underestimated energy by 345 calories a meal, the largest miss of the four apps tested.
  - Appediet was the closest at 252 calories low, so the spread between best and worst photo app was 93 calories a meal.
  - Cal AI's own FAQ says the app is about 80% accurate. For a 345 calorie miss to be a 20% error, the meal would have to contain 1,725 calories.
  - All four apps underestimated fat by about 30 g a meal, which is where cooking oil and butter hide.
  - Cal AI publishes no price page. Its listing shows five different prices for a purchase called Unlimited, from $2.99 to $29.99.
faq:
  - q: How accurate is Cal AI?
    a: In the only controlled test I can find, Cal AI underestimated meal energy by 345 calories on average across 102 weighed meals. That was the worst of four photo apps, and the finding is a conference abstract, not a peer-reviewed paper.
  - q: Is Cal AI worth $29.99?
    a: Not for accuracy. $29.99 is the highest of five prices Apple lists for its Unlimited purchase, and Cal AI never publishes what period that buys, so you learn the terms after starting a 3 day trial.
  - q: Why do photo calorie apps underestimate meals?
    a: Fat is the main reason. The NIH group found all four apps missed about 30 g of fat per meal, and oil absorbed into food or butter stirred into a sauce does not show up in a photograph.
  - q: Does a high App Store rating mean an app is accurate?
    a: No. Across the four apps tested, ratings ran from 4.71 to 4.80 stars while the calorie error ran from 252 to 345 a meal. The best rated app had the largest error.
  - q: What is more accurate than a photo?
    a: Weighing food and logging it by weight. Everything else, a photo or a spoken description, is an estimate of portion size, and portion size is where most of the error comes from.
---

Cal AI's own FAQ says the app is "about 80% accurate". When researchers at the NIH photographed 102 meals weighed to the nearest 0.1 gram and ran them through it, Cal AI came in 345 calories low per meal, the biggest miss of the four apps they tested ([Healio](https://www.healio.com/news/primary-care/20260804/ai-photobased-calorietracking-tools-underestimate-them-by-33)).

Those two numbers only agree if the average meal contains 1,725 calories. The meals in that study were ordinary plated meals from a metabolic kitchen.

I read the NIH press release, the trade coverage carrying the per-app figures, and Cal AI's own site and App Store listing on 22 October 2026. I build a calorie tracker myself, so the last section says where mine is no better.

## How accurate is Cal AI?

**It underestimated meals by 345 calories on average, with a 95% confidence interval of 296 to 392, across 102 controlled meals.**

Olivia Charles and Aaron Hengist of the NIH's NIDDK intramural programme worked from 102 standardised meals made in the metabolic kitchen at the NIH Clinical Center, every ingredient weighed to 0.1 g. They photographed each meal, ran the photos through four apps, and compared the output with food composition tables ([American Society for Nutrition](https://www.eurekalert.org/news-releases/1136415)).

Every app came in low. The headline was an underestimate of roughly a third of the energy on the plate.

![Bar chart of calories each app missed per meal in the NIH test: Cal AI 345, Lose It 333, MyFitnessPal 327 and Appediet 252, with 95 percent confidence intervals](/blog/img/is-cal-ai-accurate-1.webp)

| App | Calories missed per meal | 95% confidence interval | App Store rating | Purchases Apple lists |
|---|---|---|---|---|
| [Cal AI](https://apps.apple.com/us/app/cal-ai-calorie-tracker/id6480417616) | 345 | 296 to 392 | 4.80 from 372k ratings | $0.99 to $29.99 |
| [Lose It!](https://apps.apple.com/us/app/lose-it-calorie-counter/id297368629) | 333 | 282 to 383 | 4.77 from 782k ratings | $9.99 to $79.99 |
| [MyFitnessPal](https://apps.apple.com/us/app/myfitnesspal-calorie-counter/id341232718) | 327 | 269 to 385 | 4.71 from 2.4M ratings | $9.99 to $79.99 |
| [Appediet](https://apps.apple.com/us/app/ai-calorie-counter-appediet/id6450329545) | 252 | 210 to 295 | 4.78 from 48k ratings | $6.99 to $79.99 |

Caveats before anyone quotes this at me. It is a conference abstract presented at NUTRITION 2026 and has not been through journal peer review ([Healio](https://www.healio.com/news/primary-care/20260804/ai-photobased-calorietracking-tools-underestimate-them-by-33)). And the apps were fed photographs with no correction, which is how most people use them but not the best case.

One more thing the chart will not tell you. The intervals for Cal AI, Lose It! and MyFitnessPal overlap heavily, so this test does not establish a ranking among those three. Only the gap to Appediet at 252 comes close to separating.

Still, 102 weighed meals is a better test than any of these companies has published about itself.

## Does Cal AI's own accuracy claim hold up?

**Not against this test. "About 80% accurate" and a 345 calorie miss only reconcile at meals of 1,725 calories.**

The claim sits in the FAQ on Cal AI's own site, unqualified ([Cal AI](https://www.calai.app/)). There is no sample size, no method and no link to data behind it.

Do the arithmetic the other way. If 345 calories is the mean error and the claim of a 20% error holds, the mean meal has to be 1,725 calories. A plated lunch is not that.

!stat 1,725 | calories a meal would need to contain for a 345 calorie miss to be a 20% error | [Cal AI FAQ](https://www.calai.app/)

The ratings do not help you either. Cal AI holds 4.80 stars from about 372,000 US ratings, the highest of the four apps tested, while posting the largest error ([App Store](https://apps.apple.com/us/app/cal-ai-calorie-tracker/id6480417616)).

![Scatter plot of App Store rating against calories missed per meal for four apps, showing Cal AI highest rated at 4.80 and furthest right at 345 calories missed](/blog/img/is-cal-ai-accurate-2.webp)

## Why do photo apps miss so much fat?

**Because fat is invisible in a photograph. All four apps were about 30 g of fat short per meal.**

Hengist put it plainly: "These apps tend to underestimate calories, especially from fats" ([American Society for Nutrition](https://www.eurekalert.org/news-releases/1136415)). Oil absorbed into a stir fry, butter melted into a sauce, ghee stirred through dal, dressing already tossed into a salad: none of it is visible once the plate is made.

Fat carries more energy per gram than protein or carbohydrate, so missing 30 g of it costs more than missing 30 g of anything else. Carbohydrates, the one macro you can mostly see on a plate, were estimated more consistently across all four apps ([American Society for Nutrition](https://www.eurekalert.org/news-releases/1136415)).

Cal AI's pitch leans on hardware, saying the phone's depth sensor calculates food volume ([Cal AI](https://www.calai.app/)). Depth solves volume. It does not tell you what was poured into the pan twenty minutes earlier.

## What does Cal AI cost?

**$29.99 is the highest of five prices Apple lists for its Unlimited purchase, and Cal AI publishes no price page at all.**

The In-App Purchases panel on the US listing shows "Unlimited" at $2.99, $5.99, $9.99, $19.99 and $29.99, plus a $0.99 Streak Restore, which buys back a logging streak you broke ([App Store](https://apps.apple.com/us/app/cal-ai-calorie-tracker/id6480417616)). Apple never prints the billing period, so none of those numbers tells you what you are committing to.

Cal AI's site offers a 3 day trial and states no price ([Cal AI](https://www.calai.app/)). Its terms mention auto-renewal without naming a period or an amount ([Cal AI terms](https://calai.app/tos)).

There is also no free tier. The App Store description carries one line in capitals at the end, that food scanning analysis results require a subscription. I went through the same panel for nine apps in [what is actually free in a free calorie counter](/blog/free-calorie-counter-without-subscription/), and Cal AI was the only one whose core function is gated outright.

## Is Cal AI worth it?

**Not if you are buying accuracy. If you want the lowest effort way to get a number, it works, as long as you treat the number as a floor.**

Here is the practical reading of the NIH result. If the pattern held across three meals a day, you would be short about 1,035 calories a day, which is more than most people's entire intended deficit.

That is a projection from a single-meal mean, not a measured daily figure, so treat it as the direction rather than the size. Even halved, it is enough to make a diary useless for the thing diaries are for.

If you want fewer calories missed, weigh your food and log it by weight. Cronometer does this better than anything I have built: lab-analysed nutrition data, a free barcode scanner and up to 95 nutrients on the free tier ([Cronometer](https://cronometer.com/features/free-nutrition-tracking-app.html)).

MealSaid, which I built, does not take photos at all. You say what you ate and it writes calories and macros to Apple Health ([how MealSaid works](/blog/how-mealsaid-works/)), which moves the guess from the camera to your own description of the portion. That is a different error, not an absent one.

I have not published accuracy numbers of my own, so nothing on this page says MealSaid beats Cal AI. That test is running: weighed meals against a kitchen scale and USDA reference values, and it will go up with the raw table whichever way it falls. The gaps I can state now are that there is no barcode scanner, no photo logging and no food database search, it needs iOS 26 on an iPhone, and it is English only.

## How I checked this

Checked 22 October 2026. The study facts come from the American Society for Nutrition release on the NIDDK work presented at NUTRITION 2026, and the per-app calorie figures and confidence intervals come from Healio's report of the same abstract, which is the only source I found carrying the breakdown by app. The abstract itself does not appear to be published anywhere I can link to.

The prices, the purchase names and the ratings were read directly off the US App Store listings on 22 October 2026 for all four apps. Cal AI's accuracy claim, the depth sensor line and the 3 day trial came from calai.app, and the auto-renewal line from its terms page.

What I could not verify: the average energy of the 102 meals, which no source states, so the "about a third" figure stays as reported rather than recomputed per app. Healio prints all four intervals with the larger number first, which fits differences expressed as negatives; I have shown them ascending. The 1,725 calorie and 1,035 calorie figures are my own arithmetic on the published means, with no new data behind them. Corrections to ohmbrock42@gmail.com.
