#!/usr/bin/env python3
"""Render the blog figures into blog/img/<slug>-<n>.webp. PIL only, re-runnable.
usage: tools/.venv/bin/python tools/blog_images.py
"""
import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "blog" / "img"
RAW = Path("/Users/omdivyatej/Downloads/Code/voicefit/release/screenshots/raw")
BG, INK, INK2, INK3, LINE, ACC = "#0b0e13", "#f3f5f8", "#aeb6c4", "#6f7889", "#232935", "#d6ff3d"
FONT = os.environ.get("BLOG_FONT", "/System/Library/Fonts/HelveticaNeue.ttc")  # a .ttc with 4 weights; a plain .ttf renders one weight
W = {"r": 0, "b": 1, "l": 7, "m": 10}


def F(size, w="r"):
    return ImageFont.truetype(FONT, size, index=W[w] if FONT.endswith(".ttc") else 0)


def canvas(w=1600, h=900):
    im = Image.new("RGB", (w, h), BG)
    return im, ImageDraw.Draw(im)


def text(d, xy, s, size=28, w="r", fill=INK, anchor="la"):
    d.text(xy, s, font=F(size, w), fill=fill, anchor=anchor)


def source(d, s, h=900):
    text(d, (80, h - 56), s, 20, fill=INK3)


def save(im, name):
    p = OUT / name
    for q in (85, 78, 70, 60, 50):
        im.save(p, "WEBP", quality=q, method=6)
        if p.stat().st_size <= 150 * 1024:
            break
    print(f"{p.relative_to(ROOT)}  {im.size[0]}x{im.size[1]}  {p.stat().st_size // 1024} KB")


# ------------------------------------------------------------ why people quit
def quit_logins():
    im, d = canvas()
    text(d, (80, 70), "Share of the MyFitnessPal group who logged in, by month", 36, "m")
    text(d, (80, 124), "Six-month randomized trial of overweight primary-care patients", 24, fill=INK2)
    vals = [97, 55, 47, 43, 23, 35]
    x0, x1, y0, y1 = 180, 1460, 220, 740
    pts = [(x0 + i * (x1 - x0) / 5, y1 - v / 100 * (y1 - y0)) for i, v in enumerate(vals)]
    d.line([(x0 - 40, y1), (x1 + 40, y1)], fill=LINE, width=2)
    d.line(pts, fill=ACC, width=4, joint="curve")
    for i, ((x, y), v) in enumerate(zip(pts, vals)):
        d.ellipse([x - 9, y - 9, x + 9, y + 9], fill=BG, outline=ACC, width=4)
        text(d, (x, y - 26), f"{v}%", 30, "m", anchor="ms")
        text(d, (x, y1 + 24), f"Month {i + 1}", 24, fill=INK3, anchor="ma")
    source(d, "Source: Laing et al., Annals of Internal Medicine 2014, n = 212. Median logins fell from 8 a month to 0.")
    save(im, "why-people-quit-calorie-tracking-1.webp")


def quit_waffle():
    im, d = canvas()
    text(d, (80, 290), "2.58%", 150, "b")
    text(d, (84, 470), "of 189,770 people who downloaded", 30, fill=INK2)
    text(d, (84, 512), "a free food-journal app used it actively", 30, fill=INK2)
    text(d, (84, 554), "for more than a week.", 30, fill=INK2)
    text(d, (84, 620), "Each square is 1% of downloads.", 22, fill=INK3)
    gx, gy, cell, gap = 880, 130, 56, 10
    full = int(2.58)
    frac = 2.58 - full
    for i in range(100):
        r, c = divmod(i, 10)
        x, y = gx + c * (cell + gap), gy + r * (cell + gap)
        d.rounded_rectangle([x, y, x + cell, y + cell], 6, fill="#1a2029")
        if i < full:
            d.rounded_rectangle([x, y, x + cell, y + cell], 6, fill=ACC)
        elif i == full:
            d.rounded_rectangle([x, y, x + round(cell * frac), y + cell], 6, fill=ACC)
    source(d, "Source: Helander et al., Journal of Medical Internet Research 2014. Active = 10 or more photos over at least a week.")
    save(im, "why-people-quit-calorie-tracking-2.webp")


def quit_bars():
    im, d = canvas()
    text(d, (80, 70), "Median share of 84 days with a food log", 36, "m")
    text(d, (80, 124), "Same weight loss in both groups: 3.3 kg versus 3.4 kg", 24, fill=INK2)
    base, top = 740, 240
    for x, v, label, col in ((420, 97, "Daily checklist of red-zone foods", ACC), (960, 49, "Logging every food with calories", "#3a4252")):
        h = (base - top) * v / 100
        d.rounded_rectangle([x, base - h, x + 300, base], 10, fill=col)
        d.rectangle([x, base - 12, x + 300, base], fill=col)
        text(d, (x + 150, base - h - 20), f"{v}%", 54, "b", anchor="ms")
        text(d, (x + 150, base + 24), label, 24, fill=INK2, anchor="ma")
    d.line([(300, base), (1300, base)], fill=LINE, width=2)
    source(d, "Source: Patel et al., JMIR Formative Research 2022, n = 38 (18 detailed, 20 simplified), remote pilot.")
    save(im, "why-people-quit-calorie-tracking-3.webp")


# ------------------------------------------------------------ mfp alternatives
ROWS = [
    ("MyFitnessPal", "$79.99 / yr", "Premium", "Premium", "Yes", "Yes"),
    ("Lose It!", "$79.99 / yr", "Free", "Premium", "Yes", "Yes"),
    ("Cronometer", "$59.99 / yr", "Free", "Gold", "Yes", "Yes"),
    ("MacroFactor", "$71.99 / yr, no free tier", "Paid app", "Paid app", "Yes", "None"),
    ("MyNetDiary", "$59.99 / yr", "Free", "Free", "Yes", "No"),
    ("Cal AI", "$29.99 SKU, no price page", "Subscription", "Subscription", "Not confirmed", "Not stated"),
    ("FatSecret", "$59.99 / yr", "Free", "Premium", "Yes", "Not stated"),
    ("MealSaid", "Free, no purchases", "No barcode", "Free", "Yes", "No"),
]
COLS = [("App", 80), ("Paid price", 360), ("Barcode", 720), ("Voice logging", 920), ("Writes to Apple Health", 1150), ("Ads on free tier", 1420)]


def mfp_table():
    im, d = canvas(1600, 1000)
    text(d, (80, 60), "MyFitnessPal and seven alternatives, October 2026", 36, "m")
    y = 150
    for name, x in COLS:
        text(d, (x, y), name.upper(), 18, "m", fill=INK3)
    d.line([(80, y + 36), (1520, y + 36)], fill=LINE, width=2)
    y += 60
    for row in ROWS:
        for (name, x), val in zip(COLS, row):
            bold = name == "App"
            quiet = val in ("Premium", "Gold", "Subscription", "Not confirmed", "Not stated", "No barcode", "Paid app")
            text(d, (x, y), val, 26, "m" if bold else "r", fill=INK if bold or not quiet else INK3)
        y += 76
        d.line([(80, y - 22), (1520, y - 22)], fill=LINE, width=1)
    text(d, (80, y + 8), "Grey text means the feature costs extra or the company does not say.", 20, fill=INK3)
    source(d, "Sources: each company's pricing page or US App Store listing, checked 20 October 2026.", 1000)
    save(im, "myfitnesspal-alternatives-1.webp")


def mfp_timeline():
    im, d = canvas()
    text(d, (80, 70), "What MyFitnessPal moved behind Premium", 36, "m")
    x0, x1, y = 160, 1440, 520
    d.line([(x0, y), (x1, y)], fill=LINE, width=3)
    years = list(range(2022, 2027))
    for yr in years:
        x = x0 + (yr - 2022) / 4 * (x1 - x0)
        d.line([(x, y - 10), (x, y + 10)], fill=INK3, width=2)
        text(d, (x, y + 28), str(yr), 22, fill=INK3, anchor="ma")
    events = [(2022 + 9 / 12, "Barcode scanning", "1 October 2022", -1), (2024 + 11 / 12, "Voice Log", "December 2024", 1)]
    for t, title, when, side in events:
        x = x0 + (t - 2022) / 4 * (x1 - x0)
        d.ellipse([x - 12, y - 12, x + 12, y + 12], fill=ACC)
        ty = y - 150 if side < 0 else y - 150
        d.line([(x, y - 14), (x, ty + 70)], fill=INK3, width=2)
        text(d, (x, ty), title, 34, "m", anchor="ma")
        text(d, (x, ty + 44), when, 24, fill=INK2, anchor="ma")
    text(d, (x0, 680), "Meal Scan (photo) is Premium too. MyFitnessPal's pages give no launch date, so it has no dot.", 24, fill=INK2)
    text(d, (x0, 720), "Still free: manual search logging, the food database and Apple Health sync, with ads.", 24, fill=INK2)
    source(d, "Sources: MyFitnessPal support articles on the barcode scanner, voice logging and the Free / Premium comparison, checked 20 October 2026.")
    save(im, "myfitnesspal-alternatives-2.webp")


# ------------------------------------------------------------ apple health
def health_matrix():
    im, d = canvas()
    text(d, (80, 70), "Who writes food to Apple Health, and who reads it back", 36, "m")
    apps = [("MyFitnessPal", "Yes", "No"), ("Lose It", "Yes", "Energy only, free tier"), ("Cronometer", "Yes", "No"),
            ("MacroFactor", "Yes", "Yes"), ("MealSaid", "Yes", "No")]
    cx1, cx2 = 760, 1140
    text(d, (cx1, 170), "WRITES NUTRITION", 18, "m", fill=INK3, anchor="ma")
    text(d, (cx2, 170), "READS NUTRITION BACK", 18, "m", fill=INK3, anchor="ma")
    d.line([(80, 212), (1520, 212)], fill=LINE, width=2)
    y = 262
    for name, w, r in apps:
        text(d, (80, y), name, 30, "m", anchor="lm")
        for cx, v in ((cx1, w), (cx2, r)):
            full = v == "Yes"
            col = INK if full else INK3
            if full:
                d.ellipse([cx - 13, y - 13, cx + 13, y + 13], fill=ACC if (cx == cx2) else INK)
            else:
                d.ellipse([cx - 13, y - 13, cx + 13, y + 13], outline="#39414f", width=3)
            if v not in ("Yes", "No"):
                text(d, (cx + 30, y), v, 22, fill=INK3, anchor="lm")
        y += 98
        d.line([(80, y - 49), (1520, y - 49)], fill=LINE, width=1)
    text(d, (80, 770), "Filled dot = yes, per the app's own support doc. Hollow = no.", 22, fill=INK3)
    source(d, "Sources: MyFitnessPal, Lose It, Cronometer and MacroFactor support articles, checked 20 October 2026; MealSaid is our own app.")
    save(im, "calorie-apps-apple-health-1.webp")


def health_macros_card():
    card = Image.open(RAW / "detail.png").convert("RGB").crop((48, 1020, 1272, 2040))
    im, d = canvas(1600, 1000)
    h = 900
    card = card.resize((round(card.width * h / card.height), h), Image.LANCZOS)
    im.paste(card, ((1600 - card.width) // 2, 50))
    save(im, "calorie-apps-apple-health-2.webp")


# ------------------------------------------------------------ log without opening
def log_strip():
    im, d = canvas()
    cols = [80, 580, 1080]
    pw = 440
    for x, n, title in zip(cols, "123", ("Siri", "Lock Screen control", "Home Screen widget")):
        text(d, (x, 90), n, 26, "m", fill=ACC if n == "1" else INK3)
        text(d, (x + 36, 90), title, 30, "m")
    # 1 Siri phrase
    text(d, (80, 200), "“Hey Siri, log in MealSaid,", 36, "m")
    text(d, (80, 250), "two eggs and toast”", 36, "m")
    text(d, (80, 330), "Siri shows a card confirming", 24, fill=INK2)
    text(d, (80, 364), "what was logged. The app", 24, fill=INK2)
    text(d, (80, 398), "never opens.", 24, fill=INK2)
    # 2 listening screen
    log = Image.open(RAW / "log.png").convert("RGB").crop((260, 1000, 1060, 1900))
    log = log.resize((pw, round(log.height * pw / log.width)), Image.LANCZOS)
    im.paste(log, (580, 200))
    text(d, (580, 200 + log.height + 30), "One press on the locked phone opens", 24, fill=INK2)
    text(d, (580, 234 + log.height + 30), "the app already listening.", 24, fill=INK2)
    # 3 widget
    wd = Image.open(RAW / "homescreen.png").convert("RGB").crop((80, 330, 1260, 790))
    wd = wd.resize((pw, round(wd.height * pw / wd.width)), Image.LANCZOS)
    im.paste(wd, (1080, 200))
    text(d, (1080, 200 + wd.height + 30), "Tap anywhere on the widget.", 24, fill=INK2)
    text(d, (1080, 234 + wd.height + 30), "It shows today's total too.", 24, fill=INK2)
    source(d, "MealSaid on iOS 26. Screenshots from the App Store build.")
    save(im, "log-food-without-opening-the-app-3.webp")


# ------------------------------------------------------------ how it works
def screenshot(name, out):
    im = Image.open(RAW / name).convert("RGB")
    im = im.resize((800, round(im.height * 800 / im.width)), Image.LANCZOS)
    save(im, out)


def how_flow():
    im, d = canvas()
    steps = [("You say it", "“two eggs, toast and a coffee”"),
             ("Calories and macros", "480 kcal, 32 g protein, 52 g carbs, 14 g fat"),
             ("Apple Health", "dietary energy, protein, carbs, fat, fiber")]
    xs = [80, 600, 1120]
    for x, (t, s) in zip(xs, steps):
        text(d, (x, 360), t, 40, "m")
        text(d, (x, 420), s, 24, fill=INK2)
    for x in (500, 1020):
        d.line([(x, 384), (x + 60, 384)], fill=INK3, width=4)
        d.line([(x + 44, 368), (x + 60, 384), (x + 44, 400)], fill=INK3, width=4, joint="curve")
    text(d, (80, 560), "About a second, end to end.", 30, "m", fill=ACC)
    text(d, (80, 610), "Speech to text happens on the phone. The text goes to our server, a language model turns it", 24, fill=INK2)
    text(d, (80, 644), "into entries, and the entries are written to Apple Health. Nothing is recorded.", 24, fill=INK2)
    source(d, "Values from a real MealSaid entry (chicken burrito bowl). Estimates are checked against USDA FoodData Central for common foods.")
    save(im, "how-mealsaid-works-3.webp")


# ------------------------------------------------------------ macrofactor vs cronometer
# (app, annual US price, nutrients documented, source of the nutrient count)
MVC_VALUE = [
    ("MacroFactor", 71.99, 56, "56 reference pages I counted in its help centre"),
    ("Cronometer Gold", 59.99, 95, "95 nutrients and compounds, on their own site"),
    ("Cronometer Basic", 0.00, 95, "the same 95 nutrients, with ads and two charts"),
]


def mvc_per_nutrient():
    im, d = canvas()
    text(d, (80, 58), "A year of each app, divided by the nutrients it documents", 38, "m")
    text(d, (80, 112), "Annual US price over the number of nutrients each company says it tracks", 24, fill=INK2)
    x0, xmax, span = 620, 1340, 1.40
    for g in (0, 0.25, 0.50, 0.75, 1.00, 1.25):
        gx = x0 + g / span * (xmax - x0)
        d.line([(gx, 200), (gx, 700)], fill="#1a2029", width=2)
        text(d, (gx, 716), f"${g:.2f}", 20, fill=INK3, anchor="ma")
    text(d, (x0 + 0.70 / span * (xmax - x0), 754), "cost per nutrient, per year", 22, fill=INK3, anchor="ma")
    y = 262
    for name, price, n, note in MVC_VALUE:
        free = price == 0
        per = price / n
        text(d, (80, y - 20), name, 31, fill=ACC if free else INK, anchor="lm")
        text(d, (80, y + 18), f"${price:.2f} a year over {n} nutrients", 24, fill=INK2, anchor="lm")
        text(d, (80, y + 54), note, 21, fill=INK3, anchor="lm")
        w = per / span * (xmax - x0)
        if free:
            d.rounded_rectangle([x0, y - 44, x0 + 10, y + 4], 4, fill=ACC)
            text(d, (x0 + 30, y - 20), "$0.00, nothing to pay", 30, "m", fill=ACC, anchor="lm")
        else:
            d.rounded_rectangle([x0, y - 44, x0 + w, y + 4], 8, fill="#3a4252")
            text(d, (x0 + w + 24, y - 20), f"${per:.2f}", 34, fill=INK, anchor="lm")
        y += 170
    d.line([(x0, 200), (x0, 700)], fill=LINE, width=2)
    text(d, (80, 792), "The two counts are not measured the same way, so read this as value, not as a nutrient audit.", 22, fill=INK3)
    source(d, "Sources: MacroFactor help centre, cronometer.com feature pages and both US App Store listings, read 24 October 2026.")
    save(im, "macrofactor-vs-cronometer-1.webp")


# (category, number of reference articles in MacroFactor's Nutrients collection, colour)
MVC_NUTRIENTS = [
    (9, "Calories and the macro breakdown", "#2b323e"),
    (11, "Amino acids", "#39414f"),
    (9, "Kinds of fat", "#4c5566"),
    (12, "Vitamins", "#6f7889"),
    (10, "Minerals", "#8b94a4"),
    (5, "Cholesterol, caffeine, alcohol, water, choline", "#aeb6c4"),
]


def mvc_nutrient_count():
    im, d = canvas()
    text(d, (80, 58), "What MacroFactor's 56 documented nutrients are", 38, "m")
    text(d, (80, 112), "One reference page per nutrient in its help centre, counted on 24 October 2026", 24, fill=INK2)
    x0, x1, top, bot = 80, 1380, 220, 324
    total = 95.0
    x = x0
    for n, _l, col in MVC_NUTRIENTS:
        w = n / total * (x1 - x0)
        d.rectangle([x, top, x + w, bot], fill=col)
        text(d, (x + w / 2, (top + bot) / 2), str(n), 30, "m", fill=INK if col != "#aeb6c4" else BG, anchor="mm")
        x += w
    d.line([(x1, top - 30), (x1, bot + 30)], fill=ACC, width=4)
    text(d, (x1 - 16, top - 44), "Cronometer says up to 95", 25, "m", fill=ACC, anchor="rs")
    text(d, (x + 22, (top + bot) / 2), "56", 30, "m", fill=INK, anchor="lm")
    y = 418
    for n, label, col in MVC_NUTRIENTS:
        d.rounded_rectangle([80, y - 14, 108, y + 14], 6, fill=col)
        text(d, (134, y), label, 27, fill=INK, anchor="lm")
        text(d, (1000, y), f"{n} pages", 27, "m", fill=INK, anchor="lm")
        y += 62
    text(d, (80, 792), "Cronometer publishes no list I could count the same way, so 95 is their number and 56 is mine.", 22, fill=INK3)
    source(d, "Sources: help.macrofactorapp.com Nutrients collection and cronometer.com/features/track-food.html, read 24 October 2026.")
    save(im, "macrofactor-vs-cronometer-2.webp")


# (label, foods with a full nutrient profile, note)
MVC_DEPTH = [
    ("MacroFactor standard database", 26500, "micronutrient complete common foods", "26,500"),
    ("Cronometer, NCC database", 17000, "lab analysed, 70 nutrients", "over 17,000"),
    ("Cronometer, USDA SR28", 8000, "lab analysed, over 70 nutrients", "over 8,000"),
]


def mvc_depth():
    im, d = canvas()
    text(d, (80, 58), "Foods that actually carry a full nutrient profile", 38, "m")
    text(d, (80, 112), "Counted from each company's own description of its database", 24, fill=INK2)
    x0, xmax, span = 620, 1360, 30000.0
    for g in (0, 10000, 20000, 30000):
        gx = x0 + g / span * (xmax - x0)
        d.line([(gx, 210), (gx, 620)], fill="#1a2029", width=2)
        text(d, (gx, 636), f"{g:,}", 20, fill=INK3, anchor="ma")
    y = 282
    for label, v, note, shown in MVC_DEPTH:
        mf = label.startswith("MacroFactor")
        text(d, (80, y - 18), label, 28, fill=ACC if mf else INK, anchor="lm")
        text(d, (80, y + 18), note, 21, fill=INK3, anchor="lm")
        w = v / span * (xmax - x0)
        d.rounded_rectangle([x0, y - 40, x0 + w, y + 2], 8, fill=ACC if mf else "#3a4252")
        text(d, (x0 + w + 24, y - 19), shown, 30, "m" if mf else "r", fill=INK, anchor="lm")
        y += 120
    d.line([(80, 690), (1520, 690)], fill=LINE, width=1)
    text(d, (80, 726), "MacroFactor's full search index holds about 1,360,000 items, so 26,500 is 1.9% of it.", 25, fill=INK2)
    text(d, (80, 764), "Cronometer's whole database runs to over a million entries; it does not break out the lab analysed share.", 23, fill=INK3)
    source(d, "Sources: MacroFactor Food Search Database article, Cronometer Data Sources article and cronometer.com free tier page, read 24 October 2026.")
    save(im, "macrofactor-vs-cronometer-3.webp")


# ------------------------------------------------------------ cal ai alternatives, no photo
# (app, typed search, one food by voice, a whole spoken or typed meal); "f" free, "p" paid, "-" not offered
CAN_ROWS = [
    ("MyNetDiary", "f", "f", ("p", "$99.99 a year")),
    ("MealSaid", "-", "-", "f"),
    ("Cronometer", "f", "-", ("p", "$59.99 a year")),
    ("MacroFactor", ("p", "$71.99 a year"), "-", ("p", "$71.99 a year")),
    ("MyFitnessPal", "f", "-", ("p", "$79.99 a year")),
    ("Lose It!", "f", ("p", "$79.99 a year"), "-"),
    ("Cal AI", "-", "-", ("p", "price not published")),
]
CAN_COLS = ("Type into a search box", "Say one food", "Say or type a whole meal")


def can_matrix():
    im, d = canvas()
    text(d, (80, 58), "Logging a meal with the camera off, and what it costs", 38, "m")
    text(d, (80, 112), "Every camera free route each app documents, and the tier it sits on", 24, fill=INK2)
    xs = (620, 960, 1270)
    for cx, label in zip(xs, CAN_COLS):
        text(d, (cx, 190), label.upper(), 18, fill=INK3, anchor="la")
    d.line([(80, 224), (1520, 224)], fill=LINE, width=2)
    y = 274

    def mark(cx, cy, cell):
        kind, note = cell if isinstance(cell, tuple) else (cell, "")
        if kind == "f":
            d.ellipse([cx - 13, cy - 13, cx + 13, cy + 13], fill=INK)
            text(d, (cx + 30, cy), note or "free", 22, fill=INK2, anchor="lm")
        elif kind == "p":
            d.ellipse([cx - 13, cy - 13, cx + 13, cy + 13], outline="#6f7889", width=3)
            text(d, (cx + 30, cy), note or "paid", 22, fill=INK3, anchor="lm")
        else:
            d.line([(cx - 13, cy), (cx + 13, cy)], fill="#39414f", width=4)

    for i, (name, a, b, c) in enumerate(CAN_ROWS):
        best = name == "MyNetDiary"
        text(d, (80, y), name, 29, fill=ACC if best else INK, anchor="lm")
        for cx, cell in zip(xs, (a, b, c)):
            mark(cx, y, cell)
        y += 76
        if i < len(CAN_ROWS) - 1:
            d.line([(80, y - 38), (1520, y - 38)], fill=LINE, width=1)
    d.ellipse([80, 778, 106, 804], fill=INK)
    text(d, (120, 791), "included free", 22, fill=INK2, anchor="lm")
    d.ellipse([340, 778, 366, 804], outline="#6f7889", width=3)
    text(d, (380, 791), "paid, cheapest yearly price shown", 22, fill=INK2, anchor="lm")
    d.line([(900, 791), (926, 791)], fill="#39414f", width=4)
    text(d, (942, 791), "not documented", 22, fill=INK2, anchor="lm")
    source(d, "Sources: each app's own help centre, feature page or US App Store listing, all read 24 October 2026.")
    save(im, "cal-ai-alternatives-no-photo-1.webp")


# every distinct in-app purchase price Apple lists for Cal AI, and the one name they share
CAN_UNLIMITED = [2.99, 5.99, 9.99, 19.99, 29.99]


def can_prices():
    im, d = canvas()
    text(d, (80, 70), "One product name, five prices, no price page", 38, "m")
    text(d, (80, 124), "Every distinct purchase named 'Unlimited' on Cal AI's US App Store listing", 24, fill=INK2)
    x0, xmax, span = 160, 1420, 33.0
    y = 470
    d.line([(x0, y), (xmax, y)], fill=LINE, width=3)
    for g in (0, 5, 10, 15, 20, 25, 30):
        gx = x0 + g / span * (xmax - x0)
        d.line([(gx, y - 10), (gx, y + 10)], fill=LINE, width=2)
        text(d, (gx, y + 34), f"${g}", 22, fill=INK3, anchor="ma")
    for i, v in enumerate(CAN_UNLIMITED):
        px = x0 + v / span * (xmax - x0)
        lift = 104 + (i % 2) * 74
        top = v == 29.99
        d.line([(px, y - 20), (px, y - lift + 10)], fill="#39414f", width=2)
        d.ellipse([px - 13, y - 13, px + 13, y + 13], fill=ACC if top else INK)
        text(d, (px, y - lift), f"${v:.2f}", 28, "m" if top else "r", fill=INK, anchor="ms")
    sx = x0 + 0.99 / span * (xmax - x0)
    d.ellipse([sx - 10, y - 10, sx + 10, y + 10], outline="#8b94a4", width=3)
    text(d, (sx - 8, y + 86), "$0.99 Streak Restore,", 21, fill=INK3, anchor="la")
    text(d, (sx - 8, y + 116), "the only purchase with a different name", 21, fill=INK3, anchor="la")
    text(d, (80, 630), "The dearest Unlimited is ten times the cheapest.", 32, fill=INK)
    text(d, (80, 684), "Cal AI's website has no pricing page, and Apple does not say what period any of these buys.", 26, fill=INK2)
    text(d, (80, 730), "You are shown one of them after starting the three day trial.", 24, fill=INK3)
    source(d, "Source: the In-App Purchases panel on Cal AI's US App Store listing and calai.app, both read 24 October 2026.")
    save(im, "cal-ai-alternatives-no-photo-2.webp")


# ------------------------------------------------------------ voice input
VOICE_LEVELS = [
    ("1", "Dictation", [
        "You tap the Dictate key on the iOS keyboard",
        "and your words land in the app's search box.",
        "One food, then you still pick the match.",
    ], ["Any app with a text field", "Free, it is an iOS keyboard feature"]),
    ("2", "Voice search", [
        "A microphone button inside the app searches",
        "the food database for what you just said.",
        "Still one food at a time.",
    ], ["Lose It! (Say It)", "Premium only"]),
    ("3", "Spoken meal", [
        "You say a whole sentence and the app returns",
        "several diary entries for you to review.",
        "The one that saves real time.",
    ], ["MyFitnessPal, Cronometer, MyNetDiary,", "MacroFactor, Lifesum, MealSaid"]),
]


def voice_levels():
    im, d = canvas()
    text(d, (80, 58), "Three different things calorie apps call voice input", 38)
    text(d, (80, 112), "What actually happens after you speak, from each app's own help pages", 24, fill=INK2)
    y = 196
    for num, name, lines, apps in VOICE_LEVELS:
        top = y
        acc = num == "3"
        text(d, (80, y + 14), num, 84, fill=ACC if acc else INK3)
        text(d, (190, y), name, 40, fill=INK)
        for i, ln in enumerate(lines):
            text(d, (190, y + 58 + i * 36), ln, 25, fill=INK2)
        text(d, (900, y + 4), "WHERE YOU FIND IT", 18, fill=INK3)
        for i, ap in enumerate(apps):
            text(d, (900, y + 40 + i * 36), ap, 25, fill=INK if i == 0 else INK2)
        y += 220
        if y < 760:
            d.line([(80, y - 40), (1520, y - 40)], fill=LINE, width=1)
        _ = top
    source(d, "Sources: MyFitnessPal, Cronometer, Lose It, MyNetDiary, MacroFactor and Lifesum help pages, read 21 October 2026.")
    save(im, "calorie-tracker-voice-input-1.webp")


VOICE_PRICES = [
    ("MyNetDiary Premium Plus", 99.99),
    ("Lifesum Premium", 99.99),
    ("MyFitnessPal Premium", 79.99),
    ("MacroFactor", 71.99),
    ("Cronometer Gold", 59.99),
    ("MealSaid", 0.0),
]


def voice_prices():
    im, d = canvas()
    text(d, (80, 58), "What a year of speaking your meals costs", 38)
    text(d, (80, 112), "Cheapest listed US plan that unlocks sentence level voice logging", 24, fill=INK2)
    x0, xmax, span = 560, 1340, 100.0
    y = 210
    med = 79.99
    mx = x0 + med / span * (xmax - x0)
    d.line([(mx, 186), (mx, 788)], fill="#39414f", width=2)
    text(d, (mx, 796), "Median of the five paid plans, $79.99", 20, fill=INK3, anchor="ma")
    for name, v in VOICE_PRICES:
        text(d, (80, y + 22), name, 27, fill=INK, anchor="lm")
        w = v / span * (xmax - x0)
        if v:
            d.rounded_rectangle([x0, y, x0 + w, y + 46], 8, fill="#3a4252")
            text(d, (x0 + w + 18, y + 22), f"${v:.2f}", 27, fill=INK, anchor="lm")
        else:
            d.rounded_rectangle([x0, y, x0 + 10, y + 46], 4, fill=ACC)
            text(d, (x0 + 28, y + 22), "$0, free, no in-app purchases", 27, fill=ACC, anchor="lm")
        y += 98
    d.line([(x0, 196), (x0, 788)], fill=LINE, width=2)
    text(d, (80, 796), "MealSaid is my app. It has no barcode scanner and no photo logging.", 20, fill=INK3)
    source(d, "Sources: each company's own pricing page or US App Store listing, checked 21 October 2026.")
    save(im, "calorie-tracker-voice-input-2.webp")


# ------------------------------------------------------------ logging reminders
REMIND_ROWS = [
    ("MyFitnessPal", "Push, one per meal, as many as you like", "Yes"),
    ("Lose It!", "None I could find in the help centre", "No reminder"),
    ("Cronometer", "Push, daily plus one per diary group", "Yes"),
    ("MyNetDiary", "Push meal reminders, listed as free", "Not stated"),
    ("MacroFactor", "None; a weigh-in reminder is requested", "No reminder"),
    ("MealSaid", "An incoming phone call at times you pick", "Yes"),
]


def remind_matrix():
    im, d = canvas()
    text(d, (80, 58), "What each calorie app does when you have not logged", 38)
    text(d, (80, 112), "Reminder type and whether it is skipped once you have logged, from each app's own docs", 24, fill=INK2)
    cx = 1210
    text(d, (80, 186), "APP", 18, fill=INK3)
    text(d, (560, 186), "WHAT IT SENDS", 18, fill=INK3)
    text(d, (cx, 186), "SKIPPED IF YOU LOGGED", 18, fill=INK3, anchor="ma")
    d.line([(80, 222), (1520, 222)], fill=LINE, width=2)
    y = 272
    for i, (name, what, skip) in enumerate(REMIND_ROWS):
        acc = name == "MealSaid"
        text(d, (80, y), name, 29, fill=ACC if acc else INK, anchor="lm")
        text(d, (560, y), what, 25, fill=INK2, anchor="lm")
        if skip == "Yes":
            d.ellipse([cx - 13, y - 13, cx + 13, y + 13], fill=INK)
        elif skip == "Not stated":
            d.ellipse([cx - 13, y - 13, cx + 13, y + 13], outline="#39414f", width=3)
            text(d, (cx + 30, y), "not stated", 22, fill=INK3, anchor="lm")
        else:
            d.line([(cx - 13, y), (cx + 13, y)], fill="#39414f", width=3)
            text(d, (cx + 30, y), "nothing to skip", 22, fill=INK3, anchor="lm")
        y += 88
        if i < len(REMIND_ROWS) - 1:
            d.line([(80, y - 44), (1520, y - 44)], fill=LINE, width=1)
    text(d, (80, 790), "Filled dot = the app says it only sends the reminder if you have not logged yet.", 22, fill=INK3)
    source(d, "Sources: MyFitnessPal, Cronometer and Lose It help centres, MyNetDiary App Store, MacroFactor feedback board, 21 October 2026.")
    save(im, "calorie-apps-that-remind-you-to-log-1.webp")


REMIND_METRICS = [
    ("Reminders tapped", 13.96, 19.05),
    ("Followed by a log within an hour", 17.32, 21.77),
    ("Days with a log, overall", 55.54, 58.87),
]


def remind_response():
    im, d = canvas()
    text(d, (80, 58), "How often a logging reminder actually works", 38)
    text(d, (80, 112), "Same 30 people, four weeks, reminders at fixed times versus reminders timed to activity", 24, fill=INK2)
    x0, xmax, span = 700, 1380, 70.0
    for g in (0, 20, 40, 60):
        gx = x0 + g / span * (xmax - x0)
        d.line([(gx, 230), (gx, 690)], fill="#1a2029", width=2)
        text(d, (gx, 706), f"{g}%", 20, fill=INK3, anchor="ma")
    y = 300
    for label, a, b in REMIND_METRICS:
        text(d, (80, y), label, 27, fill=INK, anchor="lm")
        ax = x0 + a / span * (xmax - x0)
        bx = x0 + b / span * (xmax - x0)
        d.line([(ax, y), (bx, y)], fill="#39414f", width=4)
        d.ellipse([ax - 12, y - 12, ax + 12, y + 12], fill="#6f7889")
        d.ellipse([bx - 12, y - 12, bx + 12, y + 12], fill=ACC)
        text(d, (ax - 26, y), f"{a:.2f}%", 24, fill=INK2, anchor="rm")
        text(d, (bx + 26, y), f"{b:.2f}%", 24, fill=INK, anchor="lm")
        y += 160
    d.ellipse([80, 762, 104, 786], fill="#6f7889")
    text(d, (118, 774), "fixed time", 22, fill=INK2, anchor="lm")
    d.ellipse([320, 762, 344, 786], fill=ACC)
    text(d, (358, 774), "timed to your activity", 22, fill=INK2, anchor="lm")
    text(d, (700, 774), "The first two gaps were significant. The daily log rate gap was not.", 22, fill=INK3, anchor="lm")
    source(d, "Source: Chen et al., CHI 2024, n = 30, within-subjects, 4 weeks, weight-maintenance app paired with FatSecret.")
    save(im, "calorie-apps-that-remind-you-to-log-2.webp")


# ------------------------------------------------------------ what is actually free
# (app, number of in-app purchase SKUs Apple lists, lowest, highest), US App Store, 22 October 2026
FREE_IAP = [
    ("Lifesum", 10, 21.99, 119.99),
    ("MacroFactor", 10, 9.99, 89.99),
    ("MyFitnessPal", 10, 9.99, 79.99),
    ("Lose It!", 10, 9.99, 79.99),
    ("Cronometer", 10, 10.99, 59.99),
    ("MyNetDiary", 10, 8.99, 59.99),
    ("FatSecret", 9, 10.49, 59.99),
    ("Yazio", 10, 11.90, 47.90),
    ("Cal AI", 10, 0.99, 29.99),
    ("MealSaid", 0, None, None),
]


def free_ranges():
    im, d = canvas()
    text(d, (80, 58), "What a free calorie counter can charge you", 38, "m")
    text(d, (80, 112), "Lowest and highest in-app purchase price on each app's US App Store page", 24, fill=INK2)
    x0, xmax, span = 600, 1430, 125.0
    for g in (0, 25, 50, 75, 100, 125):
        gx = x0 + g / span * (xmax - x0)
        d.line([(gx, 190), (gx, 742)], fill="#1a2029", width=2)
        text(d, (gx, 758), f"${g}", 20, fill=INK3, anchor="ma")
    y = 222
    for name, n, lo, hi in FREE_IAP:
        acc = name == "MealSaid"
        text(d, (80, y), name, 27, fill=ACC if acc else INK, anchor="lm")
        if lo is None:
            d.ellipse([x0 - 11, y - 11, x0 + 11, y + 11], fill=ACC)
            text(d, (x0 + 30, y), "no in-app purchases, nothing to buy", 23, fill=INK2, anchor="lm")
        else:
            ax = x0 + lo / span * (xmax - x0)
            bx = x0 + hi / span * (xmax - x0)
            d.line([(ax, y), (bx, y)], fill="#39414f", width=5)
            d.ellipse([ax - 10, y - 10, ax + 10, y + 10], fill="#8b94a4")
            d.ellipse([bx - 10, y - 10, bx + 10, y + 10], fill=INK)
            text(d, (ax - 24, y), f"${lo:,.2f}", 22, fill=INK2, anchor="rm")
            text(d, (bx + 24, y), f"${hi:,.2f}", 23, fill=INK, anchor="lm")
            text(d, (330, y), f"{n} listed", 22, fill=INK3, anchor="lm")
        y += 58
    text(d, (80, 806), "Apple shows at most ten purchases per listing, so these are floors, not full price lists.", 22, fill=INK3)
    source(d, "Source: the In-App Purchases panel on each US App Store listing, read 22 October 2026.")
    save(im, "free-calorie-counter-without-subscription-1.webp")


LOSEIT_PRICES = [(9.99, 0, -28), (11.99, 1, 0), (19.99, 0, 0), (23.99, 1, 0), (29.99, 0, 0), (39.99, 0, 0), (79.99, 0, 0)]


def free_loseit_ladder():
    im, d = canvas()
    text(d, (80, 70), "One product name, seven prices", 38, "m")
    text(d, (80, 124), "Every purchase named exactly 'Lose It! Premium' on the US App Store listing", 24, fill=INK2)
    x0, xmax, span = 140, 1420, 88.0
    y = 480
    d.line([(x0, y), (xmax, y)], fill=LINE, width=3)
    for g in (0, 20, 40, 60, 80):
        gx = x0 + g / span * (xmax - x0)
        d.line([(gx, y - 10), (gx, y + 10)], fill=LINE, width=2)
        text(d, (gx, y + 34), f"${g}", 22, fill=INK3, anchor="ma")
    for p, tier, dx in LOSEIT_PRICES:
        px = x0 + p / span * (xmax - x0)
        lift = 104 + tier * 74
        top = p == 79.99
        d.line([(px, y - 20), (px, y - lift + 10)], fill="#39414f", width=2)
        d.ellipse([px - 13, y - 13, px + 13, y + 13], fill=ACC if top else INK)
        text(d, (px + dx, y - lift), f"${p:,.2f}", 28, "m" if top else "r", fill=INK, anchor="ms")
    text(d, (80, 622), "The cheapest and the dearest differ by $70.00.", 32, fill=INK)
    text(d, (80, 676), "The Lose It! help centre quotes one price for Premium, $79.99 a year.", 26, fill=INK2)
    text(d, (80, 726), "Two more purchases on the same listing are named Premium Lifetime, at $49.99 and $59.99.", 24, fill=INK3)
    source(d, "Source: Lose It! US App Store listing and Lose It! help centre, both read 22 October 2026.")
    save(im, "free-calorie-counter-without-subscription-2.webp")


# ------------------------------------------------------------ is cal ai accurate
# (app, mean kcal underestimated, CI low, CI high, App Store rating, ratings count)
CALAI_APPS = [
    ("Cal AI", 345, 296, 392, 4.80, "372k"),
    ("Lose It!", 333, 282, 383, 4.77, "782k"),
    ("MyFitnessPal", 327, 269, 385, 4.71, "2.4M"),
    ("Appediet", 252, 210, 295, 4.78, "48k"),
]


def calai_error_bars():
    im, d = canvas()
    text(d, (80, 58), "Calories each app missed, per meal", 38, "m")
    text(d, (80, 112), "102 meals weighed to 0.1 g in an NIH metabolic kitchen, photographed and run through each app", 24, fill=INK2)
    x0, xmax, span = 420, 1400, 420.0
    for g in (0, 100, 200, 300, 400):
        gx = x0 + g / span * (xmax - x0)
        d.line([(gx, 210), (gx, 700)], fill="#1a2029", width=2)
        text(d, (gx, 716), f"{g}", 20, fill=INK3, anchor="ma")
    text(d, (x0 + 200 / span * (xmax - x0), 752), "calories under the measured value", 22, fill=INK3, anchor="ma")
    y = 272
    for name, mean, lo, hi, _r, _n in CALAI_APPS:
        worst = name == "Cal AI"
        text(d, (80, y - 17), name, 29, fill=ACC if worst else INK, anchor="lm")
        bx = x0 + mean / span * (xmax - x0)
        d.rounded_rectangle([x0, y - 36, bx, y + 2], 8, fill=ACC if worst else "#3a4252")
        lx = x0 + lo / span * (xmax - x0)
        hx = x0 + hi / span * (xmax - x0)
        d.line([(lx, y + 28), (hx, y + 28)], fill="#8b94a4", width=3)
        for wx in (lx, hx):
            d.line([(wx, y + 18), (wx, y + 38)], fill="#8b94a4", width=3)
        text(d, (bx + 26, y - 17), f"{mean} kcal", 28, "m" if worst else "r", fill=INK, anchor="lm")
        y += 112
    text(d, (80, 790), "Bars are the mean miss. The thin line under each bar is the 95% confidence interval.", 22, fill=INK3)
    source(d, "Source: Charles and Hengist, NIDDK, presented at NUTRITION 2026, n = 102 meals. Per-app figures via Healio, 4 August 2026.")
    save(im, "is-cal-ai-accurate-1.webp")


def calai_rating_vs_error():
    im, d = canvas()
    text(d, (80, 58), "Star ratings say nothing about accuracy", 38, "m")
    text(d, (80, 112), "US App Store rating against calories missed per meal, same four apps", 24, fill=INK2)
    x0, xmax, xlo, xhi = 320, 1420, 230.0, 370.0
    y0, y1, ylo, yhi = 660, 240, 4.68, 4.84
    px = lambda v: x0 + (v - xlo) / (xhi - xlo) * (xmax - x0)
    py = lambda v: y0 - (v - ylo) / (yhi - ylo) * (y0 - y1)
    for g in (250, 275, 300, 325, 350):
        d.line([(px(g), y1 - 20), (px(g), y0)], fill="#1a2029", width=2)
        text(d, (px(g), y0 + 20), str(g), 20, fill=INK3, anchor="ma")
    for g in (4.70, 4.75, 4.80):
        d.line([(x0 - 20, py(g)), (xmax, py(g))], fill="#1a2029", width=2)
        text(d, (x0 - 36, py(g)), f"{g:.2f}", 20, fill=INK3, anchor="rm")
    text(d, (px(300), y0 + 58), "calories missed per meal (further right is worse)", 22, fill=INK3, anchor="ma")
    text(d, (80, 180), "App Store rating", 22, fill=INK3)
    for name, mean, _lo, _hi, rating, n in CALAI_APPS:
        worst = name == "Cal AI"
        cx, cy = px(mean), py(rating)
        d.ellipse([cx - 14, cy - 14, cx + 14, cy + 14], fill=ACC if worst else INK)
        text(d, (cx, cy - 34), f"{name}  {rating:.2f} from {n}", 25, "m" if worst else "r", fill=INK, anchor="ms")
    text(d, (80, 782), "Ratings span 0.09 stars across a 93 calorie spread in error. The best rated app missed the most.", 24, fill=INK2)
    source(d, "Sources: US App Store listings read 22 October 2026; error figures from the NIDDK abstract via Healio, 4 August 2026.")
    save(im, "is-cal-ai-accurate-2.webp")


# ------------------------------------------------------------ how many calories off
# (label, calories a day of difference, sample size note, is the database row)
OFF_GAPS = [
    ("Photographed food record vs measured", 579, "Boushey 2017, n = 45", False),
    ("One 24 hour recall vs measured", 543, "Serra 2023, n = 30", False),
    ("Photo recognition app vs measured", 330, "Serra 2023, n = 30", False),
    ("App database vs reference database", 26, "Evenepoel 2020, n = 50", True),
]


def off_gaps():
    im, d = canvas()
    text(d, (80, 58), "Where a calorie tracker's error actually sits", 38, "m")
    text(d, (80, 112), "Calories a day of difference, four published comparisons", 24, fill=INK2)
    x0, xmax, span = 700, 1370, 620.0
    for g in (0, 200, 400, 600):
        gx = x0 + g / span * (xmax - x0)
        d.line([(gx, 200), (gx, 640)], fill="#1a2029", width=2)
        text(d, (gx, 656), str(g), 20, fill=INK3, anchor="ma")
    text(d, (x0 + 300 / span * (xmax - x0), 692), "calories a day", 22, fill=INK3, anchor="ma")
    y = 248
    for label, v, note, db in OFF_GAPS:
        text(d, (80, y - 14), label, 27, fill=ACC if db else INK, anchor="lm")
        text(d, (80, y + 22), note, 21, fill=INK3, anchor="lm")
        w = max(v / span * (xmax - x0), 4)
        d.rounded_rectangle([x0, y - 34, x0 + w, y + 6], 8, fill=ACC if db else "#3a4252")
        text(d, (x0 + w + 24, y - 14), f"{v}", 30, "m" if db else "r", fill=INK, anchor="lm")
        y += 112
    text(d, (80, 744), "The top three compare what people logged with energy expenditure measured by doubly labeled water.", 22, fill=INK3)
    text(d, (80, 780), "The bottom one compares the app's own food values with a national food composition database.", 22, fill=INK3)
    source(d, "Sources: Boushey, Nutrients 2017; Serra, Frontiers in Nutrition 2023; Evenepoel, JMIR 2020. Read 23 October 2026.")
    save(im, "how-many-calories-off-is-a-calorie-tracker-1.webp")


# (method, bias, lower limit of agreement, upper limit of agreement) in kcal/day
OFF_LOA = [("Photo recognition app", -330, -1504, 845), ("One 24 hour recall", -543, -1803, 717)]


def off_loa():
    im, d = canvas()
    text(d, (80, 58), "The average is not the error you get on a day", 38, "m")
    text(d, (80, 112), "Mean gap and 95% limits of agreement against doubly labeled water, 30 women, 7 days", 24, fill=INK2)
    x0, xmax, lo, hi = 300, 1460, -2000.0, 1000.0
    px = lambda v: x0 + (v - lo) / (hi - lo) * (xmax - x0)
    for g in (-2000, -1500, -1000, -500, 0, 500, 1000):
        d.line([(px(g), 230), (px(g), 660)], fill="#1a2029", width=2)
        text(d, (px(g), 678), f"{g:+,}".replace("+0", "0"), 20, fill=INK3, anchor="ma")
    d.line([(px(0), 210), (px(0), 660)], fill=ACC, width=3)
    text(d, (px(0) + 18, 196), "what they actually burned", 22, fill=ACC, anchor="la")
    y = 330
    for name, bias, llo, lhi in OFF_LOA:
        text(d, (80, y - 54), name, 28, fill=INK, anchor="lm")
        d.line([(px(llo), y), (px(lhi), y)], fill="#39414f", width=5)
        for wx in (px(llo), px(lhi)):
            d.line([(wx, y - 18), (wx, y + 18)], fill="#39414f", width=5)
        d.ellipse([px(bias) - 15, y - 15, px(bias) + 15, y + 15], fill=INK)
        text(d, (px(bias), y - 34), f"{bias:,}", 26, "m", fill=INK, anchor="ms")
        text(d, (px(llo), y + 46), f"{llo:,}", 22, fill=INK3, anchor="ma")
        text(d, (px(lhi), y + 46), f"+{lhi:,}", 22, fill=INK3, anchor="ma")
        y += 190
    text(d, (80, 730), "Calories a day. The bar is where 95% of individual days fall, so a 330 calorie average", 22, fill=INK3)
    text(d, (80, 764), "covers days that are 1,504 low and days that are 845 high.", 22, fill=INK3)
    source(d, "Source: Serra et al., Frontiers in Nutrition 2023, n = 30 women, Bland-Altman analysis, Table 3.")
    save(im, "how-many-calories-off-is-a-calorie-tracker-2.webp")


# (count, label, colour) for 269 restaurant items measured by bomb calorimetry
OFF_MENU = [
    (141, "At least 10 calories under the menu", "#2b323e"),
    (20, "Within 10 calories either way", "#4c5566"),
    (58, "10 to 99 calories over the menu", "#8b94a4"),
    (50, "At least 100 calories over the menu", ACC),
]


def off_menu():
    im, d = canvas()
    text(d, (80, 58), "What 269 restaurant dishes really contained", 38, "m")
    text(d, (80, 112), "Menu calories against bomb calorimetry, 42 randomly selected US restaurants", 24, fill=INK2)
    x0, x1, top, bot = 80, 1520, 220, 340
    total = sum(c for c, _l, _col in OFF_MENU)
    x = x0
    for c, _l, col in OFF_MENU:
        w = c / total * (x1 - x0)
        d.rectangle([x, top, x + w, bot], fill=col)
        text(d, (x + w / 2, (top + bot) / 2), str(c), 34, "m", fill=BG if col == ACC else INK, anchor="mm")
        x += w
    y = 440
    for c, label, col in OFF_MENU:
        d.rounded_rectangle([80, y - 14, 108, y + 14], 6, fill=col)
        text(d, (134, y), label, 28, fill=INK, anchor="lm")
        text(d, (900, y), f"{c} items", 28, "m", fill=INK, anchor="lm")
        text(d, (1120, y), f"{c / total * 100:.0f}% of 269", 26, fill=INK3, anchor="lm")
        y += 76
    text(d, (80, 756), "The overall mean gap was 10 calories a portion and was not statistically significant.", 23, fill=INK2)
    text(d, (80, 792), "One side dish held 1,000 calories more than the menu said.", 23, fill=INK3)
    source(d, "Source: Urban et al., JAMA 2011, 269 items (242 unique) bought January to June 2010 in Massachusetts, Arkansas and Indiana.")
    save(im, "how-many-calories-off-is-a-calorie-tracker-3.webp")


# ------------------------------------------------------------ lose it vs myfitnesspal
# (way of logging, Lose It tier, MyFitnessPal tier)
LVM_WAYS = [
    ("Search the food database", "Free", "Free"),
    ("Barcode scanner", "Premium, mid transition", "Premium since Oct 2022"),
    ("Photo logging", "Premium", "Premium"),
    ("Voice logging", "Premium", "Premium"),
    ("Logging a future day", "Premium", "Premium"),
]


def lvm_ways():
    im, d = canvas()
    text(d, (80, 58), "Five ways to log, and what each one costs", 38, "m")
    text(d, (80, 112), "From each company's own help centre, read 23 October 2026", 24, fill=INK2)
    c1, c2 = 740, 1130
    text(d, (80, 196), "WAY OF LOGGING", 18, "m", fill=INK3)
    text(d, (c1, 196), "LOSE IT!", 18, "m", fill=INK3)
    text(d, (c2, 196), "MYFITNESSPAL", 18, "m", fill=INK3)
    d.line([(80, 232), (1520, 232)], fill=LINE, width=2)
    y = 292
    for i, (way, a, b) in enumerate(LVM_WAYS):
        free = a == "Free"
        text(d, (80, y), way, 29, fill=ACC if free else INK, anchor="lm")
        for cx, v in ((c1, a), (c2, b)):
            head, _, tail = v.partition(", ")
            if "since" in v:
                head, tail = "Premium", v.split("Premium ")[1]
            text(d, (cx, y - (10 if tail else 0)), head, 27, "m" if head == "Free" else "r",
                 fill=ACC if head == "Free" else INK2, anchor="lm")
            if tail:
                text(d, (cx, y + 20), tail, 21, fill=INK3, anchor="lm")
        y += 96
        if i < len(LVM_WAYS) - 1:
            d.line([(80, y - 48), (1520, y - 48)], fill=LINE, width=1)
    text(d, (80, 760), "Green marks the only row a free account keeps in both apps.", 22, fill=INK3)
    source(d, "Sources: Lose It! and MyFitnessPal help centre articles on Scan It, Snap It, Say It, Meal Scan, Voice Log and meal planning, read 23 October 2026.")
    save(im, "lose-it-vs-myfitnesspal-1.webp")


# (tier, number of rows in MyFitnessPal's own comparison grid, colour)
LVM_TIERS = [(8, "Free", ACC), (21, "Premium", "#4c5566"), (4, "Premium+ only", "#2b323e")]


def lvm_free_count():
    im, d = canvas()
    text(d, (80, 58), "What a free MyFitnessPal account gets", 38, "m")
    text(d, (80, 112), "Every row in MyFitnessPal's own Free, Premium and Premium+ grid, counted", 24, fill=INK2)
    x0, x1, top, bot = 80, 1520, 230, 360
    total = sum(n for n, _t, _c in LVM_TIERS)
    x = x0
    for n, _t, col in LVM_TIERS:
        w = n / total * (x1 - x0)
        d.rectangle([x, top, x + w, bot], fill=col)
        text(d, (x + w / 2, (top + bot) / 2), str(n), 40, "m", fill=BG if col == ACC else INK, anchor="mm")
        x += w
    y = 470
    for n, tier, col in LVM_TIERS:
        d.rounded_rectangle([80, y - 14, 108, y + 14], 6, fill=col)
        text(d, (134, y), tier, 29, fill=INK, anchor="lm")
        text(d, (700, y), f"{n} of 33 features", 29, "m", fill=INK, anchor="lm")
        text(d, (1050, y), f"{n / total * 100:.0f}%", 27, fill=INK3, anchor="lm")
        y += 78
    text(d, (80, 740), "Free keeps logging, your own recipes, macro views and a printable report.", 23, fill=INK2)
    text(d, (80, 776), "Premium takes the barcode scanner, photo logging, voice logging and the ad-free view.", 23, fill=INK3)
    source(d, "Source: MyFitnessPal help centre, The difference between Free, Premium, and Premium +, updated 15 October 2026. Row count is mine.")
    save(im, "lose-it-vs-myfitnesspal-2.webp")


LVM_MFP = [9.99, 19.99, 49.99, 79.99]
LVM_LI = [9.99, 11.99, 19.99, 23.99, 29.99, 39.99, 79.99]
LVM_LI_LIFE = [49.99, 59.99]


def lvm_prices():
    im, d = canvas()
    text(d, (80, 58), "Ten purchases each, and the same price at the top", 38, "m")
    text(d, (80, 112), "Distinct in-app purchase prices on each US App Store listing, read 23 October 2026", 24, fill=INK2)
    y0, y1, top = 690, 230, 85.0
    py = lambda v: y0 - v / top * (y0 - y1)
    for g in (0, 20, 40, 60, 80):
        d.line([(260, py(g)), (1500, py(g))], fill="#1a2029", width=2)
        text(d, (230, py(g)), f"${g}", 21, fill=INK3, anchor="rm")

    def spread(vals, gap=36):
        """Label positions, top price first, pushed apart so nothing overlaps."""
        out = []
        for v in sorted(vals, reverse=True):
            ly = py(v)
            if out and ly < out[-1][1] + gap:
                ly = out[-1][1] + gap
            out.append((v, ly))
        return out

    for cx, name, vals, note in ((640, "MyFitnessPal", LVM_MFP, "4 distinct prices"),
                                 (1160, "Lose It!", LVM_LI, "7 distinct prices")):
        text(d, (cx, 160), name, 30, "m", fill=INK, anchor="ma")
        text(d, (cx, 198), note, 22, fill=INK3, anchor="ma")
        d.line([(cx, py(min(vals))), (cx, py(max(vals)))], fill="#39414f", width=4)
        for v, ly in spread(vals):
            best = v == 79.99
            d.ellipse([cx - 13, py(v) - 13, cx + 13, py(v) + 13], fill=ACC if best else INK)
            if abs(ly - py(v)) > 2:
                d.line([(cx + 16, py(v)), (cx + 34, ly)], fill="#39414f", width=2)
            text(d, (cx + 42, ly), f"${v:.2f}", 24, "m" if best else "r", fill=INK, anchor="lm")
    for v in LVM_LI_LIFE:
        d.ellipse([1160 - 11, py(v) - 11, 1160 + 11, py(v) + 11], outline="#8b94a4", width=3)
        text(d, (1160 - 28, py(v)), f"${v:.2f} lifetime", 22, fill=INK3, anchor="rm")
    text(d, (80, 744), "Both listings stop at $79.99, the price each help centre quotes for a year.", 23, fill=INK2)
    text(d, (80, 782), "Hollow rings are the two purchases named Premium Lifetime. Lose It's help centre prices Lifetime at $299.99.", 23, fill=INK3)
    source(d, "Source: the In-App Purchases panel on each US App Store listing, read 23 October 2026. Apple shows at most ten purchases.")
    save(im, "lose-it-vs-myfitnesspal-3.webp")

# ------------------------------------------------------------ simpler cronometer alternative
# (app, route, steps the app's own help article lists, numbered in the doc)
SCA_STEPS = [
    ("Lose It!", "Search, in the app", 9, ""),
    ("MyFitnessPal", "Search, iOS", 6, ""),
    ("MacroFactor", "Describe", 6, "steps written as prose"),
    ("MyNetDiary", "Describe", 5, ""),
    ("Cronometer", "Search, Add a Food", 4, ""),
    ("Cronometer", "Voice Logging, Gold only", 4, "steps written as prose"),
    ("MealSaid", "Say the whole meal", 1, "my own app"),
]


def sca_steps():
    im, d = canvas()
    text(d, (80, 58), "Steps to log one food, counted in each app's own help page", 38, "m")
    text(d, (80, 112), "The in-app route each company documents, read 25 October 2026", 24, fill=INK2)
    x0, unit, y = 640, 78, 210
    for app, route, n, note in SCA_STEPS:
        mine = app == "MealSaid"
        text(d, (80, y), app, 30, "m" if mine else "r", fill=ACC if mine else INK, anchor="lm")
        text(d, (80, y + 30), route, 21, fill=INK3, anchor="lm")
        for i in range(n):
            bx = x0 + i * unit
            d.rounded_rectangle([bx, y - 20, bx + unit - 12, y + 20], 8, fill=ACC if mine else "#3a4252")
            text(d, (bx + (unit - 12) / 2, y + 1), str(i + 1), 22, fill=BG if mine else INK2, anchor="mm")
        text(d, (x0 + n * unit + 16, y), f"{n} step" + ("s" if n > 1 else ""), 24, fill=INK2, anchor="lm")
        if note:
            text(d, (x0 + n * unit + 16, y + 28), note, 19, fill=INK3, anchor="lm")
        y += 80
    text(d, (80, 772), "Counted from the numbered instructions, or the actions in order where the page is prose.", 22, fill=INK2)
    text(d, (80, 806), "Favourites, recents and saved meals cut every count, in every app.", 22, fill=INK3)
    source(d, "Sources: Cronometer, MyFitnessPal, Lose It!, MyNetDiary and MacroFactor help pages, read 25 October 2026.")
    save(im, "simpler-cronometer-alternative-1.webp")


SCA_TABS = ["All", "Favorites", "Common", "Supplements", "Brands", "Custom", "Restaurants"]
SCA_MORE = [
    ("Sort By menu", "sets the order of the list before you type"),
    ("Database filter", "one source such as NCCDB, or a combination"),
    ("Better Alternative", "a swap offered on some brand name foods"),
    ("Multi-Add toggle", "tick boxes, Review Items, then Add to Diary"),
]


def sca_choices():
    im, d = canvas()
    text(d, (80, 58), "What Cronometer's food search offers before you pick", 38, "m")
    text(d, (80, 112), "Everything the Mobile Add a Food page describes inside one entry", 24, fill=INK2)
    text(d, (80, 206), "7", 92, "b", fill=ACC)
    text(d, (152, 242), "category tabs above the results", 30, fill=INK, anchor="lm")
    x, y = 80, 336
    for tab in SCA_TABS:
        w = d.textlength(tab, font=F(26)) + 52
        if x + w > 1520:
            x, y = 80, y + 72
        d.rounded_rectangle([x, y, x + w, y + 54], 27, outline="#39414f", width=2)
        text(d, (x + w / 2, y + 28), tab, 26, fill=INK2, anchor="mm")
        x += w + 18
    y += 146
    for name, note in SCA_MORE:
        d.line([(80, y), (120, y)], fill="#39414f", width=4)
        text(d, (144, y), name, 29, fill=INK, anchor="lm")
        text(d, (520, y), note, 24, fill=INK3, anchor="lm")
        y += 70
    text(d, (80, 790), "Then the food page itself: serving size, diary group and the full nutrient profile.", 23, fill=INK2)
    source(d, "Source: Cronometer help centre, Mobile Add a Food, updated 24 October 2026.")
    save(im, "simpler-cronometer-alternative-2.webp")


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    quit_logins(); quit_waffle(); quit_bars()
    mfp_table(); mfp_timeline()
    health_matrix(); health_macros_card()
    log_strip()
    screenshot("home.png", "how-mealsaid-works-1.webp"); screenshot("call.png", "how-mealsaid-works-2.webp"); how_flow()
    voice_levels(); voice_prices()
    remind_matrix(); remind_response()
    free_ranges(); free_loseit_ladder()
    calai_error_bars(); calai_rating_vs_error()
    off_gaps(); off_loa(); off_menu()
    lvm_ways(); lvm_free_count(); lvm_prices()
    mvc_per_nutrient(); mvc_nutrient_count(); mvc_depth()
    can_matrix(); can_prices()
    sca_steps(); sca_choices()
