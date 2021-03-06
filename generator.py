#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont, ImageFilter


def draw_card(w, h, text):
    # Parse text
    lines = text.split("\r\n")
    # Get rid of blank trailing lines (if any)
    while lines[-1] == "":
        lines.pop()
    n = len(lines)

    # Load base (black) image
    img = Image.new("RGB", (w, h), 0)
    draw = ImageDraw.Draw(img)

    # Load font
    font_size = int(h/15)
    # In case some gronk puts a bajillion lines for no good reason
    if n*font_size > h:
        font_size = int(h/(1.2*n))

    font = ImageFont.truetype(font="./Cheltenham Condensed Bold Italic.ttf", size=font_size)
    char_w, char_h = font.getsize('A')
    # Start n lines up with slight padding at bottom
    y = h - n*char_h - 0.7*char_h

    # Draw text
    for n, line in enumerate(lines):
        line = line.upper()
        line_w, line_h = font.getsize(line)
        x = w - line_w - char_w
        draw.text((x, y), line, fill='white', font=font)
        # Next line
        y += line_h

    # Slight gaussian blur for ViNtAgE aesthetic
    img = img.filter(ImageFilter.GaussianBlur(radius=font_size/55))
    return img


