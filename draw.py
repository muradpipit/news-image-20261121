#!/usr/bin/env python3
"""Draw the front page of 'The World in One Day' for 21 November 2026.

A single 1024x1024 newspaper front page summarising the day's world news.
Written from scratch for the news-image-20261121 make.fun bounty.
Deterministic: same input always produces the same PNG bytes.
"""
import textwrap

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 40
PAPER = (247, 242, 231)
INK = (18, 18, 18)
RED = (158, 22, 22)
GREY = (90, 86, 78)
RULE = (60, 58, 52)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy wrap on pixel width; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_centered(draw, y, text, fnt, fill=INK, x0=0, x1=W):
    w = draw.textlength(text, font=fnt)
    draw.text(((x0 + x1 - w) / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- top rule + masthead ----
    d.line([(MARGIN, 30), (W - MARGIN, 30)], fill=RULE, width=2)
    y = 44
    y = draw_centered(d, y, "THE WORLD IN ONE DAY", font(SERIF_B, 62))
    y += 6
    y = draw_centered(
        d, y,
        "SATURDAY, 21 NOVEMBER 2026  \u2022  ONE IMAGE, THE WHOLE WORLD",
        font(SANS, 19), fill=GREY,
    )
    y += 14
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=INK, width=5)
    y += 8
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=INK, width=1)
    y += 18

    # ---- top story ----
    y = draw_centered(d, y, "TOP STORY", font(SANS_B, 18), fill=RED)
    y += 8
    headline = "RUSSIAN MISSILES FALL ON POLAND"
    for line in wrap(d, headline, font(SERIF_B, 54), W - 2 * MARGIN):
        y = draw_centered(d, y, line, font(SERIF_B, 54))
        y += 4
    y += 6
    sub = ("Two missiles and a suspected drone come down on Polish soil. "
           "Warsaw calls it a deliberate provocation; NATO condemns "
           "a grave violation of allied airspace.")
    for line in wrap(d, sub, font(SERIF, 23), W - 2 * MARGIN - 60):
        y = draw_centered(d, y, line, font(SERIF, 23))
        y += 2
    y += 12
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=RULE, width=2)
    y += 16

    # ---- story grid: 3 columns x 3 rows ----
    stories = [
        ("MARKETS", "S&P 500 and Dow slide into correction",
         "AI stocks plunge about 3.7% in Friday trading, dragging both indexes down."),
        ("TECH", "Trump threatens ban on US AI data centres abroad",
         "The president warns American firms against building AI data centres overseas."),
        ("MARKETS", "Nvidia hits 52-week low",
         "Shares fall after reports the SEC is investigating the company's accounting."),
        ("WEATHER", "Cyclone Akvan hits Odisha coast",
         "High winds and heavy rain lash India as thousands are evacuated to safety."),
        ("DIPLOMACY", "France seeks UN Security Council meeting",
         "Paris acts after a Russian strike kills eight and hits the Kyiv embassy."),
        ("MARKETS", "India's NSE now world's fifth-largest exchange",
         "The bourse overtakes Nasdaq and HKEX in a landmark for Indian markets."),
        ("EUROPE", "Estonia shuts all crossings to Russia",
         "Tallinn closes every border crossing after suspected arson sabotage."),
        ("EUROPE", "EU readies \u20ac45bn aid package for Ukraine",
         "Brussels prepares its biggest support package yet for Kyiv."),
        ("SPORT", "Firouzja wins Total Chess World Tour Pilot",
         "Alireza Firouzja takes the title in the championship tour pilot event."),
    ]
    col_w = (W - 2 * MARGIN - 2 * 24) // 3  # 296
    col_x = [MARGIN, MARGIN + col_w + 24, MARGIN + 2 * (col_w + 24)]
    row_h = 184
    for i, (kicker, head, body) in enumerate(stories):
        r, c = divmod(i, 3)
        x = col_x[c]
        yy = y + r * row_h
        d.text((x, yy), kicker, font=font(SANS_B, 15), fill=RED)
        yy += 22
        for line in wrap(d, head, font(SERIF_B, 22), col_w)[:3]:
            d.text((x, yy), line, font=font(SERIF_B, 22), fill=INK)
            yy += 27
        yy += 2
        for line in wrap(d, body, font(SERIF, 17), col_w)[:3]:
            d.text((x, yy), line, font=font(SERIF, 17), fill=(52, 50, 46))
            yy += 22
        # vertical rules between columns
        if c < 2:
            d.line([(x + col_w + 12, y + r * row_h + 4),
                    (x + col_w + 12, y + (r + 1) * row_h - 14)],
                   fill=(200, 192, 176), width=1)
    y = y + 3 * row_h + 4

    # ---- footer ----
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=INK, width=3)
    y += 10
    draw_centered(
        d, y,
        "THE WORLD IN ONE DAY \u2014 21 NOVEMBER 2026 \u2022 ALL STORIES FIRST REPORTED TODAY",
        font(SANS, 15), fill=GREY,
    )

    img.save("entry.png", format="PNG")
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
