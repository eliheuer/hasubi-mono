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
WIDTH, HEIGHT, MARGIN, FRAMES = 2048, 1024, 128, 1
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
    fontSize(64)
    fontVariations(wght = 400)
    # Adjust this line to center main text manually.
    # TODO: This should be done automatically when drawbot-skia
    # has support for textBox() and FormattedString

    TOP_TEXT = MARGIN*5.5
    LEADING = 80
    text("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z", ((MARGIN-4)+64, TOP_TEXT))
    text("a b c d e f g h i j k l m n o p q r s t u v w x y z", ((MARGIN-4)+64, (TOP_TEXT)-(LEADING*1)))
    text("1 2 3 4 5 6 7 8 9 0 Á Ă Â Ä À Ā Å Ã & ! ? + = , . :", ((MARGIN-4)+64, (TOP_TEXT)-(LEADING*2)))
    text("اأإ ب ببب ت تتت ث ثثث ج ججج ح ححح خ خخخ د ـد ذ ـذ ر", ((MARGIN-4)+MARGIN*13.55, (TOP_TEXT)-(LEADING*3)))
    text("ــر ز ــز س سسس ش ششش ص صصص ض ضضض ع ععع غ غغغ ف ففف", ((MARGIN-4)+MARGIN*13.55, (TOP_TEXT)-(LEADING*4)))
    text("ق ققق ك ككك ل للل م ممم ن ننن ه ههه و ــــو ي ييي ء", ((MARGIN-4)+MARGIN*13.55, (TOP_TEXT)-(LEADING*5)))


# Divider lines
def draw_divider_lines():
    stroke(1)
    strokeWidth(4)
    lineCap("round")
    line((MARGIN+64, HEIGHT - MARGIN*1.5), (WIDTH - MARGIN-64, HEIGHT - MARGIN*1.5))
    line((MARGIN+64, MARGIN + (MARGIN / 2)), (WIDTH - MARGIN-64, MARGIN + (MARGIN / 2)))
    stroke(None)


# Draw text describing the font and it's git status & repo URL
def draw_auxiliary_text():
    # Setup
    font(AUXILIARY_FONT_PATH)
    fontSize(48)
    POS_TOP_LEFT = (MARGIN+64, HEIGHT - MARGIN * 1.275)
    POS_TOP_RIGHT = (WIDTH - 64 -MARGIN, HEIGHT - MARGIN * 1.275)
    POS_BOTTOM_LEFT = (MARGIN+64, MARGIN)
    POS_BOTTOM_RIGHT = (WIDTH - 64 - MARGIN * 0.8, MARGIN)
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
