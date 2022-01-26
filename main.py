#!/usr/bin/env python3

DIM_4K = (3840, 2160)
DIM_STANDARD_1 = (1920, 1080)
DIM_STANDARD_2 = (1280, 720)

from generator import draw_card
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}

if __name__ == "__main__":
    # Get user inputs
    width = int(input("Image width: "))
    height = int(input("Image height: "))
    text = input("Image text: ").upper()

    img = draw_card(width, height, text)
    img.save("test.png", "PNG")

