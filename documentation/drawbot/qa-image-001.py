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
WIDTH, HEIGHT, MARGIN, FRAMES = 2048, 2048, 256, 1
FONT_PATH = "specimen-fonts/Hasubi-Mono[wght].ttf"
INPUT_FONT = "specimen-fonts/InputMonoCompressed-Regular.ttf"
FONT_LICENSE = "OFL v1.1"
AUXILIARY_FONT = "specimen-fonts/Hasubi-Mono[wght].ttf"
AUXILIARY_FONT_SIZE = 48
BIG_TEXT_FONT_SIZE = 1024/5.85
BIG_TEXT_SIDE_MARGIN = MARGIN * 1
BIG_TEXT_BOTTOM_MARGIN = MARGIN * 5.05
GRID_VIEW = False # Change this to "True" for a grid overlay

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
    stroke(1, 0, 0, 1)
    strokeWidth(1)
    STEP_X, STEP_Y = 0, 0
    INCREMENT_X, INCREMENT_Y = MARGIN / 4, MARGIN / 4
    rect(MARGIN, MARGIN, WIDTH - (MARGIN * 2), HEIGHT - (MARGIN * 2))
    for x in range(25):
        polygon((MARGIN + STEP_X, MARGIN), (MARGIN + STEP_X, HEIGHT - MARGIN))
        STEP_X += INCREMENT_X
    for y in range(25):
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
    fontSize(125)
    text("أشـــــــهد يا إلهي بأنك", (WIDTH-MARGIN, HEIGHT-(MARGIN*1.5)))
    text("خـلقتني لعرفانك وعبادتـك", (WIDTH-MARGIN, HEIGHT-(MARGIN*2.25)))
    text("أشـــــــهد في هذا الحين", (WIDTH-MARGIN, HEIGHT-(MARGIN*3.00)))
    text("بــــعجزي وقوتك وضعفـــي", (WIDTH-MARGIN, HEIGHT-(MARGIN*3.75)))
    text("واقـــــتدارك وفقـــــري", (WIDTH-MARGIN, HEIGHT-(MARGIN*4.50)))
    text("وغــــــــــــــــــنائك", (WIDTH-MARGIN, HEIGHT-(MARGIN*5.25)))
    text("لا إله إلا أنت الــــمهيمن", (WIDTH-MARGIN, HEIGHT-(MARGIN*6.00)))
    text("الــــــــــــــــــقيوم", (WIDTH-MARGIN, HEIGHT-(MARGIN*6.75)))


# Draw White lines
def draw_white_lines():
    stroke(1)
    strokeWidth(3)
    lineCap("round")
    line((MARGIN, MARGIN), (MARGIN, HEIGHT - MARGIN))
    line((WIDTH-MARGIN, MARGIN), (WIDTH-MARGIN, HEIGHT - MARGIN))
    stroke(None)

# Draw text describing the font and it's git status & repo URL
def draw_auxiliary_text():
    font(AUXILIARY_FONT)
    fontSize(28)
    fill(1)
    #text("Hasubi Mono: m U+006D", (MARGIN+12, HEIGHT-MARGIN-19), align="left")


# Build and save the image
if __name__ == "__main__":
    draw_background()
    draw_main_text()
    #draw_white_lines()
    draw_auxiliary_text()
    # Save output, using the "--output" flag location
    saveImage(args.output)
    # Print done in the terminal
    print("DrawBot: Done")
