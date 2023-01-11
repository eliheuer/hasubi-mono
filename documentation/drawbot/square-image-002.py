# This script is meant to be run from the root level
# of your font's git repository. For example, from a Unix terminal:
# $ git clone my-font
# $ cd my-font
# $ python3 documentation/drawbot/image1.py --output documentation/drawbot/image1.png

# Import moduels from external python packages: https://pypi.org/
from drawbot_skia.drawbot import *
from fontTools.ttLib import TTFont
from fontTools.misc.fixedTools import floatToFixedToStr

# Import moduels from the Python Standard Library: https://docs.python.org/3/library/
import subprocess
import sys
import argparse

# Constants, these are the main "settings" for the image
WIDTH, HEIGHT, MARGIN, FRAMES = 2048, 2048, 128, 1
FONT_PATH = "fonts/variable/Hasubi-Mono[wght].ttf"
AUXILIARY_FONT_PATH = "fonts/variable/Hasubi-Mono[wght].ttf"
GRID_VIEW = False


# Handel the "--output" flag
# For example: $ python3 documentation/image1.py --output documentation/image1.png
parser = argparse.ArgumentParser()
parser.add_argument("--output", metavar="PNG", help="where to write the PNG file")
args = parser.parse_args()

# Load the font with the parts of fonttools that are imported with the line:
# from fontTools.ttLib import TTFont
# Docs Link: https://fonttools.readthedocs.io/en/latest/ttLib/ttFont.html
ttFont = TTFont(FONT_PATH)

# Font Info Constants
MY_URL = subprocess.check_output("git remote get-url origin", shell=True).decode()
MY_URL = "https://github.com/eliheuer/hasubi-mono "
MY_HASH = subprocess.check_output("git rev-parse --short HEAD", shell=True).decode()
FONT_NAME = ttFont["name"].getDebugName(4)
FONT_VERSION = "v%s" % floatToFixedToStr(ttFont["head"].fontRevision, 16)
FONT_LICENSE = "License: OFL v1.1"


# Draws a grid
def grid():
    stroke(1, 0, 0, 0.75)
    strokeWidth(2)
    STEP_X, STEP_Y = 0, 0
    INCREMENT_X, INCREMENT_Y = MARGIN / 2, MARGIN / 2
    rect(MARGIN, MARGIN, WIDTH - (MARGIN * 2), HEIGHT - (MARGIN * 2))
    for x in range(29):
        polygon((MARGIN + STEP_X, MARGIN), (MARGIN + STEP_X, HEIGHT - MARGIN))
        STEP_X += INCREMENT_X
    for y in range(29):
        polygon((MARGIN, MARGIN + STEP_Y), (WIDTH - MARGIN, MARGIN + STEP_Y))
        STEP_Y += INCREMENT_Y
    polygon((WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
    polygon((0, HEIGHT / 2), (WIDTH, HEIGHT / 2))


# Remap input range to VF axis range
# This is useful for animation
# (E.g. sinewave(-1,1) to wght(100,900))
def remap(value, inputMin, inputMax, outputMin, outputMax):
    inputSpan = inputMax - inputMin  # FIND INPUT RANGE SPAN
    outputSpan = outputMax - outputMin  # FIND OUTPUT RANGE SPAN
    valueScaled = float(value - inputMin) / float(inputSpan)
    return outputMin + (valueScaled * outputSpan)


# Draw the page/frame and a grid if "GRID_VIEW" is set to "True"
def draw_background():
    newPage(WIDTH, HEIGHT)
    fill(0)
    rect(-2, -2, WIDTH + 2, HEIGHT + 2)
    if GRID_VIEW:
        grid()
    else:
        pass


# Draw main text
#GRID_VIEW = True
def draw_main_text():
    fill(1)
    stroke(None)
    font(FONT_PATH)
    fontSize(128)
    fontVariations(wght = 400)

    #TOP_TEXT = MARGIN*6.55
    #LEADING = MARGIN-16
    #text("هـــــو الشافي الكافي المعين الغفور الرحيم", ((MARGIN-4)+MARGIN*13.55, TOP_TEXT))

    font_var = 400
    TRACKING = 132
    track = 128
    for i in range(11):
        fontVariations(wght = font_var)
        text("Hello World", (MARGIN * 9, (MARGIN*13)-(i*TRACKING)))
        print("font_var = ", font_var)
        font_var += 50
    font_var = 400
    for i in range(11):
        fontVariations(wght = font_var)
        text("كـــن فيكون", (MARGIN*7, (MARGIN*13)-(i*TRACKING)))
        font_var += 50

    fontVariations(wght = 400)
    fontSize(77.5/2)
    font_weights = ["400","450","500","550","600","650","700","750","800","850","900","950"]
    for i in range(11):
        text(font_weights[i], (MARGIN*7.75, (MARGIN*13)-(i*TRACKING)))


# Divider lines
def draw_divider_lines():
    stroke(1)
    strokeWidth(4)
    lineCap("round")
    line((MARGIN+64, HEIGHT - MARGIN*2), (WIDTH - MARGIN-64, HEIGHT - MARGIN*2))
    line((MARGIN+64, MARGIN + 128), (WIDTH - MARGIN-64, MARGIN + 128))
    stroke(None)


# Draw text describing the font and it's git status & repo URL
def draw_auxiliary_text():
    # Setup
    font(AUXILIARY_FONT_PATH)
    fontSize(48)
    POS_TOP_LEFT = (MARGIN+64, HEIGHT - MARGIN * 1.8)
    POS_TOP_RIGHT = (WIDTH - 64 -MARGIN, HEIGHT - MARGIN * 1.8)
    POS_BOTTOM_LEFT = (MARGIN+64, MARGIN *1.5)
    POS_BOTTOM_RIGHT = (WIDTH - 64 - MARGIN * 0.8, MARGIN*1.5)
    AT_HASH = "Git Commit: " + MY_HASH
    AT_HASH = AT_HASH.replace("\n", " ")
    # Draw Text
    text("Hasubi Mono Regular: Latin+Arabic Basic Character Set", POS_TOP_LEFT, align="left")
    text("v0.1-Alpha", POS_TOP_RIGHT, align="right")
    text(MY_URL, POS_BOTTOM_LEFT, align="left")
    text(AT_HASH, POS_BOTTOM_RIGHT, align="right")

    font("documentation/drawbot/specimen-fonts/InputMonoCompressed-Regular.ttf")
    fontSize(48)
    #text("Hasubi Mono Regular v0.1-Alpha", (MARGIN+64, HEIGHT - ((MARGIN * 1.275/2))), align="left")
    #text(FONT_LICENSE, (WIDTH - 64 -MARGIN, HEIGHT - ((MARGIN * 1.275)/2)), align="right")
    #text(MY_URL, (MARGIN+64, MARGIN/2), align="left")
    #text(AT_HASH, (WIDTH - 64 - MARGIN * 0.8, MARGIN/2), align="right")


# Build and save the image
if __name__ == "__main__":
    draw_background()
    draw_main_text()
    draw_divider_lines()
    draw_auxiliary_text()
    # Save output, using the "--output" flag location
    saveImage(args.output)
    # Print done in the terminal
    print("DrawBot: Done")
