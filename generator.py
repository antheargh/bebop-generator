#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
import textwrap

DIM_4K = (3840, 2160)
DIM_STANDARD_1 = (1920, 1080)
DIM_STANDARD_2 = (1280, 720)


def draw_card(w, h, line):
    # Load base (black) image
    img = Image.new("RGB", (w, h), 0)
    draw = ImageDraw.Draw(img)

    # Load font
    font_size = int(h/15)
    font = ImageFont.truetype(font="./Cheltenham Condensed Bold Italic.ttf", size=font_size)

    char_w, char_h = font.getsize('A')
    line_w, line_h = font.getsize(line)

    # Draw text
    y = h - 1.5*line_h
    x = w - line_w - char_w
    draw.text((x, y), line, fill='white', font=font)

    img.show()
    return img


