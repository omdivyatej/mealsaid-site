---
title: How MealSaid works
slug: how-mealsaid-works
description: What happens when you say "two eggs and toast" to MealSaid, how the call works, where your data goes, and what the app does not do.
date: 2026-10-20
updated: 2026-10-20
author: Om Divyatej
tags: [mealsaid, calorie tracking, apple health, voice]
image: assets/og.png
draft: false
faq:
  - q: Is MealSaid free?
    a: Yes. There are no in-app purchases and no ads in version 1.0.
  - q: Does MealSaid work offline?
    a: Viewing your log, totals and progress works offline. Logging by voice and the call need an internet connection, because the transcript is understood on our server.
  - q: Is my voice recorded?
    a: No. Your voice is streamed to our server, turned into text and entries, and discarded. Audio is not stored by us. The text of what you said is saved to your account so you can read it under each entry.
  - q: Which phones does MealSaid support?
    a: Any iPhone running iOS 26 or later with a microphone. There is no Android version and none planned, because the app is built around Apple Health and iPhone calls.
---

I built MealSaid because every calorie tracker I tried asked me to do the same thing: open the app, search a database, pick a portion, repeat for every ingredient. I stopped after a week, every time. MealSaid is my attempt at the opposite. You say what you ate. It is logged. That is the whole app.

This post explains what actually happens when you use it, so you can decide if it is for you.

## What happens when you log a meal

You hold the mic button and say something like "two eggs, toast and a coffee" or "did chest for 45 minutes". Then you let go.

1. Your iPhone turns your speech into text. For the mic button this happens on the device, using Apple's speech recognition.
2. The text goes to our server, which asks a language model (Anthropic's Claude) to turn it into entries: a food or a workout, an amount, and an estimate for calories, protein, carbs, fat and fiber. For common foods it checks against USDA FoodData Central values.
3. The entries come back to your phone and are written to Apple Health as dietary energy, protein, carbohydrates, total fat and fiber. Workouts are written as real workouts with active calories.

Start to finish, this takes about a second. If you said when it happened ("this morning at 8"), it is logged at that time. Tap any entry and you see the exact words it was estimated from, and you can fix a number if the estimate is off.

There is no search box, no barcode scanner and no portion slider. There is a keyboard fallback for when the gym is too loud, but I do not expect you to use it.

## You do not have to open the app

Three shortcuts cover most of my own logging:

| Where | What you do |
|---|---|
| Siri | "Hey Siri, log in MealSaid, two eggs and toast." Logged with the app closed. |
| Lock Screen | Tap the MealSaid control. The app opens already listening. |
| Home Screen | Tap the widget. Same thing. |

## The app calls you

This is the part that is unusual, so let me be precise about it.

In the Profile tab you pick the times you usually forget to log, say 9 pm. At that time our server sends a push to your phone and your iPhone rings with a normal incoming call screen from "MealSaid". You can answer it from the Lock Screen like any call.

When you answer, a voice asks what you ate today and whether you worked out. Then it waits. It does not cut you off after three seconds the way a voice assistant does. You can pause, think, list everything from breakfast to the snack you are not proud of, and it only replies when you are actually finished. If you correct yourself ("actually that was two slices, not one") it fixes the entry. When you say "that's all", it hangs up and the entries appear on your Home screen and in Apple Health.

Some details, because they matter:

- Calls only ring at the times you picked, or when you ask. You can say "call me" into the mic at any time and it rings you back in about five seconds.
- If you already logged recently, the scheduled call is skipped.
- It never dials a phone number or another person. It is a two-way voice conversation between you and the app, carried over your internet connection.
- The voice on the call is OpenAI's Realtime model, streamed through our server. Nothing on the call is recorded.

## Seeing your day

The Home screen shows today's calories and macros against your targets, with a week strip you can scrub. The Progress tab shows calorie bars per day for the last 7, 30 or 90 days, plus protein per day and your streak. There is a Home Screen widget with today's numbers.

Your targets come from onboarding, which is also a conversation: you say your weight, height, goal and how you train, and the app sets daily calorie and macro targets. Change your mind later and just say so.

## Where your data lives

I want to be plain about this because "voice" and "AI" make people nervous, reasonably.

- **Your log** is stored on your iPhone, in Apple Health, and in your MealSaid account on our server (hosted on Fly.io), so a new phone keeps your history. You sign in once with Sign in with Apple. "Hide My Email" works fine.
- **Apple Health data never leaves your phone.** The app reads your workouts, steps, weight, heart rate and sleep on the device to give the call context, and writes meals and workouts there. None of that is uploaded.
- **Your voice is processed, not kept.** Speech is streamed to our server and on to OpenAI (the voice on the call) and Anthropic (understanding what you said), then discarded. Audio is not stored. The text of what you said is saved so you can read it under each entry.
- **No ads, no tracking, no analytics SDKs.** We count which features are used, with no food names attached, and that is it.
- **Delete account** in the Profile tab removes your account and every row about you from our server and wipes the app on your phone. Entries already written to Apple Health stay there until you delete them in Health.

The full detail is in the [privacy policy](/privacy.html).

## What it is not

MealSaid gives you calorie and macro estimates from what you said. They are estimates, made by a language model from your description and public nutrition data, and they can be off. It is a logging convenience, not medical advice and not a medical device. If you need gram-level precision, you still need a scale.

It also needs an internet connection to log. Reading your log and your progress works offline, but understanding what you said does not happen on the phone.

## Requirements

An iPhone running iOS 26 or later, a microphone and an internet connection. Apple Health is optional, but it is the point. English only for now. Free, with no in-app purchases.

If you want to try it, the links are below. If something does not work, email me at ohmbrock42@gmail.com and I will answer within two working days.
