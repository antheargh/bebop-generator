#!/usr/bin/env python3

DIM_4K = (3840, 2160)
DIM_STANDARD_1 = (1920, 1080)
DIM_STANDARD_2 = (1280, 720)

from generator import draw_card
from flask import Flask, render_template, request, send_file
import requests
from io import BytesIO

app = Flask(__name__)

def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=80)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')


@app.route("/")
def hello():
    return render_template("home.html")


@app.route("/card", methods=["POST"])
def render_card():
    text = request.form["cardText"]
    w = int(request.form["cardWidth"])
    h = int(request.form["cardHeight"])
    card = draw_card(w, h, text)

    return serve_pil_image(card)


if __name__ == "__main__":
    app.run()


