---
title: Which calorie apps remind you to log food, and do they work
slug: calorie-apps-that-remind-you-to-log
description: Four of six iPhone trackers send a logging reminder, checked 21 October 2026. In a 30 person trial, 19.05% of reminders were tapped at best.
date: 2026-10-21
updated: 2026-10-21
author: Om Divyatej
tags: [reminders, notifications, adherence, calorie tracking, mealsaid]
image: blog/img/calorie-apps-that-remind-you-to-log-1.webp
draft: false
takeaways:
  - Four of the six iPhone trackers I checked send a logging reminder, and three of those send a push notification you can swipe away.
  - In the best condition of a 30 person trial, 19.05% of reminders were tapped and 21.77% were followed by a log within an hour.
  - Moving reminders from a fixed time to the moment your activity changes lifted daily logging from 55.54% to 58.87%, a gap that was not statistically significant.
  - Across 1,255 users of a wellbeing app, a tailored push made someone 3.9% more likely to self-monitor in the next 24 hours.
  - MyFitnessPal and Cronometer both only fire the reminder if you have not already logged, which is the one design detail worth checking.
faq:
  - q: Which calorie app reminds you to log food?
    a: MyFitnessPal, Cronometer and MyNetDiary all send push reminders, and MealSaid places a phone call instead. I could not find a logging reminder in Lose It's or MacroFactor's documentation on 21 October 2026.
  - q: Do calorie tracking reminders actually work?
    a: Weakly. In a four week trial with 30 people, between 13.96% and 19.05% of reminders were tapped, and the gap in days logged between well timed and fixed time reminders was not statistically significant.
  - q: Does MyFitnessPal send reminders if I already logged?
    a: No. The setting is phrased "Remind me if I haven't logged", so a meal you logged before the chosen time does not produce a notification. Cronometer works the same way.
  - q: What happens if I ignore a logging reminder?
    a: Nothing. None of the six escalates, the notification just sits on your Lock Screen, and in the trial I read most prompts were never tapped.
  - q: Is MealSaid's call the same as a reminder?
    a: It is a different channel. Your iPhone rings with a normal incoming call, a voice asks what you ate, and the call is skipped if you logged recently. I have no adherence data of my own yet.
---

Four of the six iPhone calorie apps I checked will remind you to log, and three of those four do it with a push notification you can swipe away. The number that should shape your expectations: in the best condition of a four week trial with 30 people, 19.05% of reminders were tapped and 21.77% were followed by a log within the hour ([Chen et al., CHI 2024](https://www.ruizlab.org/wp-content/uploads/2024/10/3613904.3641993.pdf)).

I read each app's own help centre, App Store listing or public feedback board on 21 October 2026. MealSaid is my app, and I have no adherence numbers of my own yet, so the last row is a description of the feature and not a claim that it works better.

## Which calorie apps actually send a logging reminder?

**MyFitnessPal, Cronometer and MyNetDiary send push notifications, MealSaid places a call, and I found nothing for Lose It or MacroFactor.** The more useful question is whether the reminder is skipped once you have logged.

| App | Reminder you can set | Costs extra? | Where you set it | Source |
|---|---|---|---|---|
| MyFitnessPal | A push per meal, only if you have not logged, as many as you want | No, the article does not mention Premium | Profile icon, then Reminders | [Help](https://support.myfitnesspal.com/hc/en-us/articles/360032622391-How-to-set-up-logging-reminders) |
| Lose It! | None I could find in the help centre; widgets are documented | Widgets are free | Home Screen widget picker | [Widgets](https://loseit.zendesk.com/hc/en-us/articles/51045533782548-How-to-Set-Up-Widgets) |
| Cronometer | A daily push plus one per diary group, only if you have not logged | No | More, then Account, then Notifications | [Help](https://support.cronometer.com/hc/en-us/articles/360051718511-Mobile-Notifications) |
| MyNetDiary | Meal reminders, listed among the free features | No | Not documented publicly | [App Store](https://apps.apple.com/us/app/calorie-counter-mynetdiary/id287529757) |
| MacroFactor | None; a weigh-in reminder is an open feature request | Not applicable | Not applicable | [Feedback board](https://feedback.macrofactorapp.com/) |
| MealSaid | A phone call at times you pick, skipped if you logged recently | No, the app is free | In the app | [How it works](/blog/how-mealsaid-works/) |

![Table of six calorie apps showing what each sends when you have not logged: push notifications for MyFitnessPal, Cronometer and MyNetDiary, nothing for Lose It and MacroFactor, and an incoming phone call for MealSaid](/blog/img/calorie-apps-that-remind-you-to-log-1.webp)

MyFitnessPal's setting is worded well. The row you tap reads "Remind me if I haven't logged", then you pick the meal and the time ([MyFitnessPal](https://support.myfitnesspal.com/hc/en-us/articles/360032622391-How-to-set-up-logging-reminders)).

Cronometer does the same thing and goes further, with a separate toggle per diary group so breakfast and dinner can nag independently ([Cronometer](https://support.cronometer.com/hc/en-us/articles/360051718511-Mobile-Notifications)).

MacroFactor is the surprise. Its public feedback board carries a Weigh-In Notification request at 52 votes, still marked Under Consideration ([MacroFactor](https://feedback.macrofactorapp.com/)), and I found no food logging reminder documented at all.

## What happens if you ignore a logging reminder?

**Nothing, in all six. None of them escalates, and the research says most prompts are ignored anyway.** The Lock Screen stacks them up and that is the end of it.

Chen and colleagues ran the cleanest test I could find. Thirty people used a weight maintenance app paired with FatSecret for four weeks, each person seeing both reminder styles, with reminders either at fixed times or timed to a change in their physical activity.

![Dumbbell chart of three outcomes under fixed time versus activity timed reminders in Chen 2024: reminders tapped 13.96 versus 19.05 percent, followed by a log within an hour 17.32 versus 21.77 percent, and days with a log 55.54 versus 58.87 percent](/blog/img/calorie-apps-that-remind-you-to-log-2.webp)

Read the left-hand dots first. Even the better style left four reminders in five untapped, and that is among people who had volunteered for a logging study and knew they were being watched.

Timing did help with speed. People clicked 12.33 minutes after a context-triggered reminder against 18.42 minutes for a fixed-time one ([Chen et al., CHI 2024](https://www.ruizlab.org/wp-content/uploads/2024/10/3613904.3641993.pdf)).

What it did not move was the thing you care about. Days with a log went from 55.54% to 58.87%, a difference of 3.33 percentage points with a 95% confidence interval of minus 3.07 to 9.73, which includes zero ([Chen et al., CHI 2024](https://www.ruizlab.org/wp-content/uploads/2024/10/3613904.3641993.pdf)).

!stat 3.9% | more likely to self-monitor in the next 24 hours when a push was sent, across 1,255 users | [Bidargaddi et al., 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC6293241/)

The bigger study points the same way. Bidargaddi and colleagues micro-randomized push notifications across 89 days for 1,255 users of a wellbeing app and found a risk ratio of 1.039, with a 95% confidence interval of 1.01 to 1.08 ([JMIR 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC6293241/)). Real, and tiny.

## Does a different kind of reminder work better?

**I could not find a published test of anything louder than a push notification for food logging, and that includes my own app.** What the literature does show is that the size of the push effect is small and that effort, not forgetting, is the bigger problem.

Bentley and Tollmar saw logging rise from 12% to 63% when notifications were added, but across two different studies rather than a controlled comparison ([CHI 2013](https://library.selfresearch.org/?p=26308)). I went through that and six other dropout studies in [why people quit calorie tracking](/blog/why-people-quit-calorie-tracking/).

MealSaid takes the loud route: at times you pick, your iPhone rings like a normal call, a voice asks what you ate, and it waits while you answer. The call is skipped if you logged recently, the same conditional logic MyFitnessPal and Cronometer use for their banners.

I believe a ringing phone is harder to dismiss without deciding than a banner is. I have not proved it. A 30 day test of calls against reminders against a widget, same person, is running, and the raw table goes up whichever way it lands.

## How do I turn reminders on?

**Both apps that document it hide the setting a few taps from the home screen, and neither charges for it.** Reminders are not in the main settings list, which is probably why people think the feature is missing.

In MyFitnessPal on iOS: tap the profile icon, scroll to Reminders, tap the plus, choose the meal, choose the time, tap the check mark. The help page adds the usual trap, that iOS notification permission has to be on or nothing arrives.

In Cronometer: More, then Account, then Notifications, then Allow Notifications, then Reminder to Log Food, then pick a time. Diary group reminders and a weight reminder after seven quiet days sit on the same screen.

If you use MyNetDiary, meal reminders are listed among its free features on its US App Store listing, though I could not find a support page with the steps ([App Store](https://apps.apple.com/us/app/calorie-counter-mynetdiary/id287529757)).

## What should you do if reminders are not working for you?

**Stop adding more of them.** Four reminders a day that you swipe away teach you to swipe, and the trial numbers above say the tap rate is low even when the timing is clever.

Two things are worth trying instead. Cut what a single entry costs you in taps, and put the log somewhere you already look, which is what Lose It's widgets are for.

MealSaid is my version of the first idea, and it is free with no in-app purchases. The gaps are real: no barcode scanner, no photo logging, no food database to browse, English only, and it needs iOS 26. If you log packaged food by barcode, MyFitnessPal or Cronometer will serve you better than I will.

## How I checked this

Checked 21 October 2026. I read the MyFitnessPal reminders article (updated 1 October 2026) and the Cronometer notifications article (updated 20 October 2026) through their help centres, and searched Lose It's help centre for reminders, notifications and push notifications without finding a logging reminder article.

The two studies were read in full text. Chen et al. is 30 participants over four weeks, within subjects, so treat every percentage as a small sample. Bidargaddi et al. is 1,255 users over 89 days, which is large but measures any app interaction rather than food logging specifically.

Two gaps I could not close. MyNetDiary publishes no support page for its reminder settings that I could find, so its row rests on the App Store listing. MacroFactor could have an undocumented reminder in the app; its own feedback board suggests not. Corrections to ohmbrock42@gmail.com.
