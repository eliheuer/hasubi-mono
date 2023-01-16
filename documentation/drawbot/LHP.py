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
fontSize(77.5)
fontVariations(wght = 400)
TOP_TEXT = MARGIN*14.05
LEADING = MARGIN-16
SIDE = 13.55
text("هـــــو الشافي الكافي المعين الغفور الرحيم", ((MARGIN-4)+MARGIN*SIDE, TOP_TEXT))
text("بـــــــــــــك يا علي بك يا وفي بك يا بهي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*1)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*2)))
text("بــــــــك يا سلطان بك يا رفعان بك يا ديان", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*3)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*4)))
text("بـــــــــــــك يا أحد بك يا صمد بك يا فرد", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*5)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*6)))
text("بــــــك يا سبحان بك يا قدسان بك يا مستعان", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*7)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*8)))
text("بــــــــــك يا عليم بك يا حكيم بك يا عظيم", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*9)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*10)))
text("بــــــــك يا رحمن بك يا عظمان بك يا قدران", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*11)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*12)))
text("بـــــــك يا معشوق بك يا محبوب بك يا مجذوب", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*13)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*14)))
#text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*5)))


# Page 2
#GRID_VIEW = True
draw_background()
fill(1)
stroke(None)
font(FONT_PATH)
fontSize(77.5)
fontVariations(wght = 400)
TOP_TEXT = MARGIN*14.05
LEADING = MARGIN-16
SIDE = 13.55
text("بــــــــــك يا عزيز بك يا نصير بك يا قدير", ((MARGIN-4)+MARGIN*SIDE, TOP_TEXT))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*1)))
text("بــــــــــك يا حاكم بك يا قائم بك يا عالم", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*2)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*3)))
text("بــــــــــــك يا روح بك يا نور بك يا ظهور", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*4)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*5)))
text("بـــــــك يا معمور بك يا مشهور بك يا مستور", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*6)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*7)))
text("بــــــــــك يا غائب بك يا غالب بك يا واهب", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*8)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*9)))
text("بــــــــــك يا قادر بك يا ناصر بك يا ساتر", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*10)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*11)))
text("بــــــــــك يا صانع بك يا قانع بك يا قالع", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*12)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*13)))
text("بــــــــــك يا طالع بك يا جامع بك يا رافع", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*14)))
#text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*5)))



# Page 3
#GRID_VIEW = True
draw_background()
fill(1)
stroke(None)
font(FONT_PATH)
fontSize(77.5)
fontVariations(wght = 400)
TOP_TEXT = MARGIN*14.05
LEADING = MARGIN-16
SIDE = 13.55
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, TOP_TEXT))
text("بــــــــــك يا بالغ بك يا فارغ بك يا سابغ", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*1)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*2)))
text("بـــــــــــــك يا نافع بك يا مانع يا صانع", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*3)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*4)))
text("بــــــــــك يا جليل بك يا جميل بك يا فضيل", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*5)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*6)))
text("بــــــــــك يا عادل بك يا فاضل بك يا باذل", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*7)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*8)))
text("بـــــــــك يا قيوم بك يا ديموم بك يا علوم", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*9)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*10)))
text("بــــــــــك يا عظوم بك يا قدوم بك يا كروم", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*11)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*12)))
text("بـــــــك يا محفوظ بك يا محظوظ بك يا ملحوظ", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*13)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*14)))

# text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, TOP_TEXT))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*1)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*2)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*3)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*4)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*5)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*6)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*7)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*8)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*9)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*10)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*11)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*12)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*13)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*14)))


# Page 4
#GRID_VIEW = True
draw_background()
fill(1)
stroke(None)
font(FONT_PATH)
fontSize(77.5)
fontVariations(wght = 400)
TOP_TEXT = MARGIN*14.05
LEADING = MARGIN-16
SIDE = 13.55
text("بــــــــــك يا عطوف بك يا رؤوف بك يا لطوف", ((MARGIN-4)+MARGIN*SIDE, TOP_TEXT))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*1)))
text("بـــــــــك يا ملاذ بك يا معاذ بك يا مستعاذ", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*2)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*3)))
text("بــــــــك يا غياث بك يا مستغاث بك يا نفاث", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*4)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*5)))
text("بــــــــــك يا كاشف بك يا ناشف بك يا عاطف", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*6)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*7)))
text("بـــــــــك يا جان بك يا جانان بك يا إيمان", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*8)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*9)))
text("بــــــــــك يا ساقي بك يا عالي بك يا غالي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*10)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*11)))
text("بـــــــــــك يا ذكر الأعظم بك يا إسم الأقدم", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*12)))
text("بـــــــــــــــــــــــــــك يا رسم الأكرم", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*13)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*14)))

# text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, TOP_TEXT))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*1)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*2)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*3)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*4)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*5)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*6)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*7)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*8)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*9)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*10)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*11)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*12)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*13)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*14)))


# Page 5
#GRID_VIEW = True
draw_background()
fill(1)
stroke(None)
font(FONT_PATH)
fontSize(77.5)
fontVariations(wght = 400)
TOP_TEXT = MARGIN*14.05
LEADING = MARGIN-16
SIDE = 13.55
text("بــــــــــك يا سبوح بك يا قدوس بك يا نزوه", ((MARGIN-4)+MARGIN*SIDE, TOP_TEXT))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*1)))
text("بــــــــــك يا فتاح بك يا نصاح بك يا نجاح", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*2)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*3)))
text("بــــــــــك يا حبيب بك يا طبيب بك يا جذيب", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*4)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*5)))
text("بـــــــــــك يا جلال بك يا جمال بك يا فضال", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*6)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*7)))
text("بــــــــــك يا واثق بك يا عاشق بك يا فالق", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*8)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*9)))
text("بـــــــــــك يا وهاج بك يا بلاج بك يا بهاج", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*10)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*11)))
text("بـــــــــــك يا وهاب بك يا عطاف بك يا رآف", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*12)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*13)))
text("بــــــــــك يا تائب بك يا نائب بك يا ذاوب", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*14)))


# text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, TOP_TEXT))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*1)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*2)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*3)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*4)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*5)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*6)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*7)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*8)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*9)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*10)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*11)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*12)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*13)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*14)))


# Page 6
#GRID_VIEW = True
draw_background()
fill(1)
stroke(None)
font(FONT_PATH)
fontSize(77.5)
fontVariations(wght = 400)
TOP_TEXT = MARGIN*14.05
LEADING = MARGIN-16
SIDE = 13.55
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, TOP_TEXT))
text("بــــــــــك يا ثابت بك يا نابت بك يا ذاوت", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*1)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*2)))
text("بــــــــــــك يا حافظ بك يا لاحظ بك يا لافظ", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*3)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*4)))
text("يـــــــــــــــا ظاهر مستور يا غائب مشهور", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*5)))
text("يـــــــــــــــــــــــــا ناظر منظور أنت", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*6)))
text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*7)))
text("يـــــــــــــــــا قاتل عشاق يا واهب فساق", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*8)))
text("يــــــــــــــــــــــــا كافي بك يا كافي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*9)))
text("يــــــــــــــــــــــــا شافي بك يا شافي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*10)))
text("يـــــا باقي بك يا باقي أنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*11)))
text("سبــــــــــــــــــــــحانك اللهم يا إلهي", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*12)))
text("أســــــــــــألك بجودك الذي به فتحت أبواب", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*13)))
text("الـــــــــــــــــــــــــــــفضل والعطاء", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*14)))

# text("أنت الكافي وأنت الشافي وأنت الباقي يا باقي", ((MARGIN-4)+MARGIN*SIDE, TOP_TEXT))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*1)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*2)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*3)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*4)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*5)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*6)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*7)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*8)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*9)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*10)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*11)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*12)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*13)))
# text("", ((MARGIN-4)+MARGIN*SIDE, (TOP_TEXT)-(LEADING*14)))











saveImage("documentation/drawbot/LHP.png")
# Print done in the terminal
print("DrawBot: Done")
