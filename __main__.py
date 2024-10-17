#! /usr/bin/env python

import sys
from pathlib import Path

from PIL import Image
import pygame as pg
import yaml

MAIN_DIR = Path(__file__).parent
CONFIG_FILE = MAIN_DIR / "config.yaml"

with CONFIG_FILE.open() as f:
    config = yaml.safe_load(f)

DOT_MARGINS = (
    (),
    ((0, 0),),
    ((1, -1), (-1, 1)),
    ((1, -1), (0, 0), (-1, 1)),
    ((-1, -1), (1, -1), (-1, 1), (1, 1)),
    ((-1, -1), (1, -1), (-1, 1), (1, 1), (0, 0)),
    ((-1, -1), (1, -1), (-1, 1), (1, 1), (-1, 0), (1, 0))
)

DIE_WIDTH = config["DIE_WIDTH"]
DOT_RADIUS = config["DOT_RADIUS"]
RESOLUTION_FACTOR = config["RESOLUTION_FACTOR"]
DIE_MARGIN_FACTOR = DIE_WIDTH // config["DIE_MARGIN_DIVISOR"]

DIE_COLOR = pg.Color(config["DIE_COLOR"])
LINE_COLOR = pg.Color(config["LINE_COLOR"])

INPUT_PATH = MAIN_DIR / config["INPUT_PATH"] if not sys.argv[1:] else Path(sys.argv[1])
OUTPUT_PATH = INPUT_PATH.with_stem(config["OUTPUT_STEM"])

if __name__ == "__main__":
    img = Image.open(INPUT_PATH).convert("L")
    WIDTH = RESOLUTION_FACTOR * img.size[0]
    HEIGHT = RESOLUTION_FACTOR * img.size[1]
    GRID_WIDTH = WIDTH // DIE_WIDTH
    GRID_HEIGHT = HEIGHT // DIE_WIDTH

    pix = img.resize((GRID_WIDTH, GRID_HEIGHT)).load()
    surface = pg.Surface((GRID_WIDTH * DIE_WIDTH, GRID_HEIGHT * DIE_WIDTH))

    for pixel_x in range(GRID_WIDTH):
        for pixel_y in range(GRID_HEIGHT):
            brightness = pix[pixel_x, pixel_y]
            dieValue = round(brightness / 42.5)
            
            dieCenterX = round((pixel_x + 0.5) * DIE_WIDTH)
            dieCenterY = round((pixel_y + 0.5) * DIE_WIDTH)

            for marginX, marginY in DOT_MARGINS[dieValue]:
                coordX = dieCenterX + marginX * DIE_MARGIN_FACTOR
                coordY = dieCenterY + marginY * DIE_MARGIN_FACTOR
                pg.draw.circle(surface, DIE_COLOR, (coordX, coordY), DOT_RADIUS)
            
    for i in range(GRID_WIDTH):
        x = i * DIE_WIDTH
        pg.draw.line(surface, LINE_COLOR, (x, 0), (x, HEIGHT))

    for i in range(GRID_HEIGHT):
        y = i * DIE_WIDTH
        pg.draw.line(surface, LINE_COLOR, (0, y), (WIDTH, y))

    pg.image.save(surface, OUTPUT_PATH)
