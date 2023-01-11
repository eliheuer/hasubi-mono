# This script is meant to be run from the documentation directory
# of your font's git repository. For example, from a Unix terminal:
# $ git clone my-font
# $ cd my-font/documentation
# $ python3 image1.py --output image1.png

#Note: fonts are sourced from the documentation/specimen-fonts directory 

# Import moduels from external python packages: https://pypi.org/
from drawbot_skia.drawbot import *
#from drawBot import * # Use this if you want to use the Mac-only regular drawbot
from fontTools.ttLib import TTFont
from fontTools.misc.fixedTools import floatToFixedToStr

# Import moduels from the Python Standard Library: https://docs.python.org/3/library/
import subprocess
import sys
import argparse

# Constants, these are the main "settings" for the image
WIDTH, HEIGHT, MARGIN, FRAMES = 2048, 1024, 128, 1
FONT_PATH = "fonts/variable/Hasubi-Mono[wght].ttf"
INPUT_FONT = "documentation/drawbot/specimen-fonts/InputMonoCompressed-Regular.ttf"
FONT_LICENSE = "OFL v1.1"
AUXILIARY_FONT = "fonts/variable/Hasubi-Mono[wght].ttf"
AUXILIARY_FONT_SIZE = 48
BIG_TEXT_A = "miب"
BIG_TEXT_B = "m"
BIG_TEXT_C = "i"
BIG_TEXT_FONT_SIZE = 1024/5.85
BIG_TEXT_SIDE_MARGIN = MARGIN * 1
BIG_TEXT_BOTTOM_MARGIN = MARGIN * 5.05
GRID_VIEW = False # Change this to "True" for a grid overlay
#GRID_VIEW = True # Change this to "True" for a grid overlay

# Handel the "--output" flag
# For example: $ python3 documentation/image1.py --output documentation/image1.png
parser = argparse.ArgumentParser()
parser.add_argument("--output", metavar="PNG", help="where to write the PNG file")
args = parser.parse_args()

# Load the font with the parts of fonttools that are imported with the line:
# from fontTools.ttLib import TTFont
# Docs Link: https://fonttools.readthedocs.io/en/latest/ttLib/ttFont.html
ttFont = TTFont(FONT_PATH)

# Constants that are worked out dynamically
MY_URL = subprocess.check_output("git remote get-url origin", shell=True).decode()
MY_URL = "https://github.com/eliheuer/hasubi-mono "
MY_HASH = subprocess.check_output("git rev-parse --short HEAD", shell=True).decode()
FONT_NAME = ttFont["name"].getDebugName(4)
FONT_VERSION = "v%s" % floatToFixedToStr(ttFont["head"].fontRevision, 16)
FONT_VERSION = "Alpha"
FONT_NAME = FONT_NAME+" "+FONT_VERSION
ENS_NAME = "elih.eth"
GIT_COMMIT = "Git Commit: "+MY_HASH
print("MY_HASH:", MY_HASH)
GIT_COMMIT = GIT_COMMIT[:-1]

# Draws a grid
def grid():
    stroke(1, 0, 0, 0.75)
    strokeWidth(0.5)
    STEP_X, STEP_Y = 0, 0
    INCREMENT_X, INCREMENT_Y = MARGIN / 8, MARGIN / 8
    rect(MARGIN, MARGIN, WIDTH - (MARGIN * 2), HEIGHT - (MARGIN * 2))
    for x in range(113):
        polygon((MARGIN + STEP_X, MARGIN), (MARGIN + STEP_X, HEIGHT - MARGIN))
        STEP_X += INCREMENT_X
    for y in range(49):
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
def draw_main_text():
    fill(1)
    stroke(None)
    font(FONT_PATH)
    fontVariations(wght = 400)

    fontSize(512+128+60)
    text(BIG_TEXT_A, (MARGIN, 256+64+32))

    font(INPUT_FONT)
    fontSize(512+128+60)
    text(BIG_TEXT_B, (MARGIN+512+256+310, 256+64+32))
    text(BIG_TEXT_C, (MARGIN+512+256+670, 256+64+32))


# Draw Red lines
def draw_red_lines():
    stroke(1,0,0)
    strokeWidth(3)
    lineCap("round")
    font(AUXILIARY_FONT)
    fill(0)
    fontSize(28)

    #line((MARGIN+40, MARGIN+110), (MARGIN+90, MARGIN+110))
    stroke(None)
    text("72", (MARGIN+51,  MARGIN+145+96), align="left")
    text("64", (MARGIN+166, MARGIN+145+96), align="left")
    text("72", (MARGIN+278, MARGIN+145+96), align="left")
    text("80", (MARGIN+248, MARGIN+456+96), align="left")
    text("80", (MARGIN+128, MARGIN+456+96), align="left")

    text("80", (MARGIN+436, MARGIN+448+96), align="left")
    text("72", (MARGIN+528, MARGIN+300+96), align="left")
    text("80", (MARGIN+420, MARGIN+145+96), align="left")
    text("80", (MARGIN+630, MARGIN+145+96), align="left")

    text("72", (MARGIN+750,  MARGIN+332+96), align="left")
    text("80", (MARGIN+885,  MARGIN+145+96), align="left")
    text("72", (MARGIN+1013, MARGIN+332+96), align="left")

    text("80", (MARGIN+1133, MARGIN+145+96), align="left")
    text("79", (MARGIN+1249, MARGIN+145+96), align="left")
    text("70", (MARGIN+1225, MARGIN+480+96), align="left")
    text("70", (MARGIN+1340, MARGIN+480+96), align="left")
    text("80", (MARGIN+1365, MARGIN+145+96), align="left")


    text("82", (MARGIN+1520, MARGIN+145+96), align="left")
    text("82", (MARGIN+1520, MARGIN+475+96), align="left")
    text("91", (MARGIN+1608, MARGIN+300+96), align="left")
    text("82", (MARGIN+1700, MARGIN+145+96), align="left")

    fill(1,0,0)
    stroke(1,0,0)

    stroke(None)


# Draw White lines
def draw_white_lines():
    stroke(1)
    strokeWidth(3)
    lineCap("round")
    line((MARGIN, MARGIN+96), (MARGIN, HEIGHT - MARGIN))
    line((MARGIN+(359*1), MARGIN+96), (MARGIN+(359*1), HEIGHT - MARGIN))
    line((MARGIN+(359*2)-6, MARGIN+96), (MARGIN+(359*2)-6, HEIGHT - MARGIN))
    line((MARGIN+(359*3)+2, MARGIN+96), (MARGIN+(359*3)+2, HEIGHT - MARGIN))
    line((MARGIN+(359*4)+8, MARGIN+96), (MARGIN+(359*4)+8, HEIGHT - MARGIN))
    line((WIDTH-MARGIN, MARGIN+96), (WIDTH-MARGIN, HEIGHT - MARGIN))
    stroke(None)

# Draw text describing the font and it's git status & repo URL
def draw_auxiliary_text():
    font(AUXILIARY_FONT)
    fontSize(28)
    fill(1)
    text("Hasubi Mono: m U+006D", (MARGIN+12, HEIGHT-MARGIN-19), align="left")
    text("Hasubi Mono: i U+0069", (MARGIN+(359*1)+12, HEIGHT-MARGIN-19), align="left")
    text("Hasubi Mono: ب U+0628", (MARGIN+(359*2)-6+12, HEIGHT-MARGIN-19), align="left")
    text("Input Mono: m U+006D", (MARGIN+(359*3)+2+12, HEIGHT-MARGIN-19), align="left")
    text("Input Mono: i U+0069", (MARGIN+(359*4)+8+12, HEIGHT-MARGIN-19), align="left")


    text("Hasubi Mono-Line Length Test: the quick brown fox jumps over the lazy dog the quick brown fox jumps over the lazy dog", (MARGIN, MARGIN+32), align="left")
    text("Input Mono--Line Length Test: ", (MARGIN, MARGIN), align="left")
    font(INPUT_FONT)
    text("the quick brown fox jumps over the lazy dog the quick brown fox jumps over the lazy dog", (MARGIN+430, MARGIN), align="left")

# Build and save the image
if __name__ == "__main__":
    draw_background()
    draw_main_text()
    draw_red_lines()
    draw_white_lines()
    draw_auxiliary_text()
    # Save output, using the "--output" flag location
    saveImage(args.output)
    # Print done in the terminal
    print("DrawBot: Done")
