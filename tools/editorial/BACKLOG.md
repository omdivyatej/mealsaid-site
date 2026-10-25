# Blog backlog

Ordered by priority. Status: `todo` | `drafted` | `published` | `needs Om's phone test`. A draft that failed the publish gate stays `drafted` with the blocker in the same cell, for example `drafted (blocked: two prices unverifiable)`. The daily routine takes the top `todo`, or the top blocked `drafted` row if it can clear the blocker. Rows marked "needs Om's phone test" wait for raw CSVs from Om (see `blog/data/` once they exist); do not write them from desk research.

One rule above all: every post needs one original element that exists nowhere else, listed in the "Required original element" column. A post without it is not written.

| # | Title idea | Target query | Intent | Page type | Required original element | Status | Link |
|---|---|---|---|---|---|---|---|
| 1 | MyFitnessPal alternatives in 2026, checked this month | MyFitnessPal alternative free no ads | switching | table | verified price and paywall table, dated | published | https://mealsaid.app/blog/myfitnesspal-alternatives/ |
| 2 | Which calorie apps actually write to (and read from) Apple Health | calorie tracker that syncs with Apple Health | Apple Health | table | read vs write matrix from each app's own docs | published | https://mealsaid.app/blog/calorie-apps-apple-health/ |
| 3 | Why most people quit calorie tracking within two weeks | why do I keep forgetting to log my meals | adherence | research summary | seven dropout studies with sample sizes | published | https://mealsaid.app/blog/why-people-quit-calorie-tracking/ |
| 4 | How to log food on iPhone without opening an app | log calories with Siri | voice | guide | step-by-step on a real phone, Shortcuts limits per app | published | https://mealsaid.app/blog/log-food-without-opening-the-app/ |
| 5 | How MealSaid works | calorie tracker that calls you | product | explainer | the call flow and data path, from the builder | published | https://mealsaid.app/blog/how-mealsaid-works/ |
| 6 | I timed how long it takes to log the same 5 meals in 6 calorie apps | best calorie tracker that doesn't require typing | voice | our own test | 90 screen-recorded runs, median seconds and taps per app (Protocol A) | needs Om's phone test | |
| 7 | How accurate are AI calorie estimates? 30 weighed meals, 3 apps | how accurate are AI calorie estimates | accuracy | our own test | kitchen-scale and USDA reference values, error per app (Protocol B) | needs Om's phone test | |
| 8 | I stopped forgetting to log when the app started calling me: 30 days of data | app that reminds me to log food | adherence | our own test | days logged under reminders vs widget vs call, same person (Protocol C) | needs Om's phone test | |
| 9 | Calorie tracker with voice input: what "voice" means in each app | calorie tracker with voice input | voice | table | dictation vs understanding, per app, from each app's own docs, dated | published | https://mealsaid.app/blog/calorie-tracker-voice-input/ |
| 10 | Which calorie apps remind you to log, and what happens if you ignore them | app that reminds me to log food | adherence | table | reminder type per app (push, widget, call) from docs, dated | published | https://mealsaid.app/blog/calorie-apps-that-remind-you-to-log/ |
| 11 | Free calorie counter without a subscription: what is actually free | free calorie counter without subscription | switching | table | in-app purchase list from each US App Store listing, dated | published | https://mealsaid.app/blog/free-calorie-counter-without-subscription/ |
| 12 | Is Cal AI accurate, and is it worth $29.99? | is Cal AI accurate | accuracy | answer | verified price, what Cal AI's own pages claim, the NIH photo-app study | published | https://mealsaid.app/blog/is-cal-ai-accurate/ |
| 13 | How many calories off is a calorie tracker, on average? | how many calories off is a calorie tracker | accuracy | answer | every published error figure with sample size, one table | published | https://mealsaid.app/blog/how-many-calories-off-is-a-calorie-tracker/ |
| 14 | Lose It vs MyFitnessPal in 2026 | Lose It vs MyFitnessPal | switching | table | verified free-tier and Premium feature table, dated; MealSaid is a footnote | published | https://mealsaid.app/blog/lose-it-vs-myfitnesspal/ |
| 15 | MacroFactor vs Cronometer | MacroFactor vs Cronometer | switching | table | verified price, micronutrient count, Apple Health read/write; MealSaid is a footnote | published | https://mealsaid.app/blog/macrofactor-vs-cronometer/ |
| 16 | Cal AI alternatives that do not need a photo | Cal AI alternative | switching | table | verified price and input method per app, dated | published | https://mealsaid.app/blog/cal-ai-alternatives-no-photo/ |
| 17 | A simpler Cronometer alternative | Cronometer alternative simpler | switching | answer | taps-to-log count from each app's own flow description | published | https://mealsaid.app/blog/simpler-cronometer-alternative/ |
| 18 | Best free calorie tracker for iPhone only | best calorie tracker iPhone only free | Apple Health | table | iPhone-only features (Siri, widgets, Health write) verified per app | published | https://mealsaid.app/blog/best-free-calorie-tracker-iphone/ |
| 19 | Hands-free calorie tracking while cooking or driving | hands-free calorie tracking | voice | answer | which apps work with the screen off or via Siri, verified | todo | |
| 20 | Calorie tracking when you hate logging (ADHD and the rest of us) | calorie tracker for ADHD | adherence | answer | self-monitoring research with sample sizes, friction count per app | todo | |
| 21 | How to stay consistent with calorie tracking | how to stay consistent with calorie tracking | adherence | guide | research on habit cues, plus our adherence numbers once #8 exists | todo | |
| 22 | Can I log food by talking to an app? | can I log food by talking to an app | voice | answer | list of every iOS app with real voice logging, verified, dated | todo | |
| 23 | Is MyFitnessPal still free? What is paywalled, re-checked monthly | is MyFitnessPal still free in 2026 | switching | update to #1 | new dated row in the existing table each month | todo | |
| 24 | Does MacroFactor / Lose It / Cronometer write nutrition to Apple Health? | does MacroFactor write nutrition to Apple Health | Apple Health | update to #2 | one H2 per app with the exact fields, from docs | todo | |
| 25 | Cal AI vs MyFitnessPal vs MealSaid: same 10 meals, three input methods | Cal AI vs MyFitnessPal | accuracy | our own test | time and error per method, from #6 and #7 | needs Om's phone test | |
| 26 | Photo calorie counter vs voice calorie counter: accuracy | photo vs voice calorie counter accuracy | accuracy | our own test | per-meal error by input method, from #7 | needs Om's phone test | |
