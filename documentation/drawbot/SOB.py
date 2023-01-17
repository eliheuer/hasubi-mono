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


# Page 1
#GRID_VIEW = True
draw_background()
fill(1)
stroke(None)
font(FONT_PATH)
fontSize(128+4)
fontVariations(wght = 400)
TOP_TEXT = MARGIN*13
LEADING = MARGIN*1.5
SIDE = 13.1
text("أشــــــهد يا إلهي بأنك", ((MARGIN-4)+MARGIN*SIDE, TOP_TEXT))
text("خلقتني لعرفانك وعبادتـك", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*1)))
text("أشــــــهد في هذا الحين", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*2)))
text("بــعجزي وقـوتـك وضعفــي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*3)))
text("واقتدارك وفقـري وغنائـك", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*4)))
text("لا إلــــــه إلا أنـــــت", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*5)))
text("الــــــــــــــــمهيمن", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*6)))
text("الـــــــــــــــــقيوم", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*7)))


saveImage("documentation/drawbot/SOB.png")
# Print done in the terminal
print("DrawBot: Done")
