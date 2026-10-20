#!/usr/bin/env python3
"""Render the blog figures into blog/img/<slug>-<n>.webp. PIL only, re-runnable.
usage: tools/.venv/bin/python tools/blog_images.py
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "blog" / "img"
RAW = Path("/Users/omdivyatej/Downloads/Code/voicefit/release/screenshots/raw")
BG, INK, INK2, INK3, LINE, ACC = "#0b0e13", "#f3f5f8", "#aeb6c4", "#6f7889", "#232935", "#d6ff3d"
FONT = "/System/Library/Fonts/HelveticaNeue.ttc"
W = {"r": 0, "b": 1, "l": 7, "m": 10}


def F(size, w="r"):
    return ImageFont.truetype(FONT, size, index=W[w])


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


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    quit_logins(); quit_waffle(); quit_bars()
    mfp_table(); mfp_timeline()
    health_matrix(); health_macros_card()
    log_strip()
    screenshot("home.png", "how-mealsaid-works-1.webp"); screenshot("call.png", "how-mealsaid-works-2.webp"); how_flow()
