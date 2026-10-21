---
title: Which calorie apps actually write to (and read from) Apple Health
slug: calorie-apps-apple-health
description: Nine calorie apps checked against their own docs on 20 October 2026: who writes nutrition to Apple Health, who reads it back, why calories get doubled.
date: 2026-10-20
updated: 2026-10-20
author: Om Divyatej
tags: [apple health, healthkit, myfitnesspal, lose it, macrofactor, cronometer, mealsaid]
image: blog/img/calorie-apps-apple-health-1.webp
draft: false
medium: https://om-divyatej.medium.com/which-calorie-apps-actually-write-to-and-read-from-apple-health-d972176c5a43
takeaways:
  - Of nine calorie apps checked on 20 October 2026, only Lose It and MacroFactor read nutrition back from Apple Health. The other seven only write.
  - Apple Health supports 39 nutrition fields, and every app asks for its own subset, so "syncs with Apple Health" can mean three different things.
  - Doubled calories in Health come from two sources writing the same meal. Fix it under Data Sources & Access by turning one source off.
  - MacroFactor is the only app whose doc explains its conflict rules. Lose It imports dietary energy only on the free tier.
  - MealSaid writes five nutrition fields plus workouts, reads workouts, steps, weight, heart rate and sleep, and does not import food from other apps.
faq:
  - q: Does MyFitnessPal read food from Apple Health?
    a: No. Its support doc lists Food as one direction only, MyFitnessPal to Apple Health. It reads exercise, weight and sleep from Health, not nutrition.
  - q: Which calorie apps read nutrition from Apple Health?
    a: Of the nine I checked, Lose It (dietary energy only on the free tier) and MacroFactor (calories, macros and micros). The other seven only write.
  - q: Does MealSaid read what other apps logged?
    a: No. MealSaid writes energy, protein, carbs, fat and fiber to Health and reads workouts, steps, weight, heart rate and sleep. It does not import food from other apps.
  - q: Why are my calories doubled in Apple Health?
    a: Two apps are writing food to Health, or one app logged the same meal twice. Health adds every source together unless you pick one under Data Sources and Access. MyNetDiary's own doc warns about this.
  - q: Does any of this work on Android?
    a: No. Apple Health is iPhone only. Android has Health Connect, which is a separate system with its own rules.
---

Most calorie apps write your food into Apple Health. Very few read it back. Of the nine apps I checked on 20 October 2026 against their own support pages, only two import nutrition from Health: Lose It (dietary energy only, free tier) and MacroFactor (calories, macros and micros).

MyFitnessPal, Cronometer, MyNetDiary, FatSecret, Lifesum, Carbon Diet Coach and MealSaid all write and do not read.

!stat 2 of 9 | calorie apps read nutrition back from Apple Health; the other seven only write

That one-way street is what makes "syncs with Apple Health" such a slippery phrase. Here is what each app actually does, with the doc it comes from.

## What does "syncs with Apple Health" really mean?

It can mean three different things and app listings rarely say which. Writing nutrition into Health, reading nutrition out of Health, or reading other data like steps and weight.

Apple Health is a database on your phone. Apps ask permission to write to specific fields and to read specific fields, one by one. Apple publishes the nutrition fields it supports, 39 of them, from dietaryEnergyConsumed and dietaryProtein down to individual vitamins ([Apple developer docs: nutrition type identifiers](https://developer.apple.com/documentation/healthkit/nutrition-type-identifiers)).

!stat 39 | nutrition fields Apple Health supports, from dietaryEnergyConsumed down to individual vitamins | [Apple developer docs](https://developer.apple.com/documentation/healthkit/nutrition-type-identifiers)

You can see exactly what each app asked for under Settings > Health > Data Access & Devices ([Apple Support: share your Health data](https://support.apple.com/guide/iphone/share-your-health-data-iph5ede58c3d/ios)).

So when an app says it "syncs", ask three questions.

- Does it write my meals in?
- Does it read meals other apps wrote?
- Does it only read steps and weight and call that sync?

## Which apps write nutrition and which read it?

Seven of nine write only. Two read. Nobody is a complete two-way mirror.

![Matrix of MyFitnessPal, Lose It, Cronometer, MacroFactor and MealSaid showing all five write nutrition to Apple Health and only MacroFactor reads it back in full, Lose It energy only](/blog/img/calorie-apps-apple-health-1.webp)

| App | Writes food to Health | Fields written (per their doc) | Reads food from Health | Reads other Health data | Source, date seen |
|---|---|---|---|---|---|
| MyFitnessPal | Yes | "Meal summaries and most nutrients"; caffeine and vitamin A excluded; no per-meal timestamps | No | Exercise, weight, sleep | [MFP support](https://support.myfitnesspal.com/hc/en-us/articles/360032271092-Apple-Health-connection-and-syncing), updated 24 Sep 2026 |
| Lose It | Yes | Food (fields not itemised) | Yes, dietary energy only on free; macros and water with Premium custom goals | Weight, exercise | [Lose It help](https://help.loseit.com/hc/en-us/articles/47773580085140-Using-Apple-Health-With-Lose-It), updated 1 Apr 2026 |
| MacroFactor | Yes | Calories, macros, supported micros | Yes, calories, macros and micros for the day | Weight, both directions | [MacroFactor help](https://help.macrofactorapp.com/en/articles/102-integrations) |
| Cronometer | Yes | "13 Different Nutrients" plus dietary cholesterol | No | Activity, exercise, weight, sleep, biometrics | [Cronometer support](https://support.cronometer.com/hc/en-us/articles/360020734212-Apple-Health-Apple-Watch), updated 18 Oct 2026 |
| MyNetDiary | Yes | "up to 38 nutrients", water | No (reads water) | Workouts, steps, weight, blood pressure, glucose, sleep | [MyNetDiary support](https://www.mynetdiary.com/supportArticle.do?articleId=418) |
| FatSecret | Yes | Foods with "detailed nutritional information" | No | Calories burned, steps | [App Store listing](https://apps.apple.com/us/app/calorie-counter-by-fatsecret/id347184248) |
| Lifesum | Yes | "Food calories, Food nutrition, Weight, Water intake" | No | Exercise calories, steps, workouts, weight | [Lifesum help](https://help.lifesum.com/en/article/eagtau/), updated 26 Aug 2026 |
| Carbon Diet Coach | Yes | Energy, macros, available micros | No | Weight, body fat | [Carbon help](https://help.joincarbon.com/en/articles/9814262-apple-health-integration), updated 8 Sep 2025 |
| MealSaid | Yes | Dietary energy, protein, carbohydrates, total fat, fiber; workouts with active calories | No | Workouts, steps, weight, heart rate, sleep | Our own app, [how it works](/blog/how-mealsaid-works/) |

!note Cal AI is missing from the table on purpose. Its FAQ describes connecting Apple Health for steps, and its App Store listing does not mention Health at all. Third-party blogs say it writes calories and macros. I could not confirm that from anything Cal AI publishes, so I am not putting it in a row.

Two rows deserve a note. MacroFactor's import has a priority rule: manual entry beats its own food log, which beats Apple Health, and a MacroFactor food entry for a day blocks the Health import for that day ([MacroFactor help](https://help.macrofactorapp.com/en/articles/102-integrations)).

Lose It marks imported dietary energy with a heart icon in the log so you can tell it apart; its doc says "Food data from other 3rd party apps in Apple Health may appear in Lose It!"

## Why does it matter whether an app reads nutrition back?

Because reading is what lets you switch apps, or use two, without losing the day. A write-only app is a one-way door: its entries land in Health for everyone else to see, but it never looks at what anyone else logged.

In practice that means if you log breakfast with a Siri phrase in one app and lunch by barcode in another, only Apple Health itself has the whole day. MyFitnessPal will show you its own meals. Cronometer will show you its own.

Health > Browse > Nutrition > Dietary Energy shows both, which is why I tell people to treat the Health app as the ledger and the trackers as input devices.

MacroFactor is the one app here built for that two-app life, and it is the only one whose doc explains the conflict rules. Lose It gets you partway (energy only, and no macros unless you pay and set a custom goal).

## Why are my calories doubled in Apple Health?

Two sources wrote the same meal, and Health adds them up. Fix it under Health > Browse > Nutrition > Dietary Energy > Data Sources & Access by turning off the source you do not want counted.

This is the trap the "sync" word hides. Every write-only app above will happily add its entries next to another app's entries. MyNetDiary's own support page says it directly: if you log the same food in two apps, "you may see duplicate records in Apple Health".

It is not only two apps either; the Athlytic recovery app's help doc notes that "MyFitnessPal has been known to double-log calories in Apple Health" on its own ([Athlytic help](https://athlyticapp.helpscoutdocs.com/article/51-missing-or-incorrect-calories-from-your-nutrition-tracker-in-athlytic), updated 24 Feb 2025).

A reader-plus-writer is a different risk. If an app reads dietary energy from Health and also writes dietary energy to Health, a second tracker's entries can get imported and then re-exported as the first app's own.

MacroFactor handles this with the priority rule above. Lose It's doc does not say what happens if you also write from another app, and I could not test it for this post.

Carbon Diet Coach took the blunt route: "We do not import nutrition from other apps." It reads back only its own entries, to avoid writing them twice.

## Which fields does MealSaid write and what does it not do?

MealSaid writes five nutrition fields (dietary energy, protein, carbohydrates, total fat, fiber) and real workouts with active calories. It reads workouts, steps, weight, heart rate and sleep for context.

![MealSaid macros card for a chicken burrito bowl: 32 g protein, 52 g carbs, 14 g fat, 4 g fiber, each against its daily target, with Tap any value to edit](/blog/img/calorie-apps-apple-health-2.webp)

What it does not do:

- It does not read food from Health.
- It does not write water, caffeine, sugar, sodium or micronutrients.
- The Health data it reads never leaves your phone.

If you want 38 nutrients in Health, MyNetDiary or Cronometer will give you more than we do. If you want an app that imports what other trackers logged, that is MacroFactor. MealSaid's bet is narrower: get the meal into Health in one sentence, by voice or by Siri, with the app closed, and let Health be the ledger.

It also requires iOS 26, is English only, has no barcode scanner, and there is no Android version, so Health Connect users are out of luck.

## How I checked this

Checked 20 October 2026. For each app I read the current Apple Health page in its own help center or, where none exists, the developer's own App Store description, and recorded the write and read lists and the page's "updated" date where shown. MyFitnessPal, Lose It and Cronometer block scripted fetches of their help centers (they return 403 to anything that is not a browser), so those three were read through the help center's public API and confirmed in Safari.

Cal AI's FAQ and listing were read the same day and found silent on nutrition writes. MealSaid's row is from our own HealthKit permission list. I did not install every app and inspect Settings > Health > Data Access for this post; that is a follow-up, with screenshots, and if it contradicts a doc I will say so here. Corrections to ohmbrock42@gmail.com.
