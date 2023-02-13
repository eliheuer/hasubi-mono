# This script is meant to be run from the root level
# of your font's git repository. For example, from a Unix terminal:
# $ git clone my-font
# $ cd my-font
# $ python3 documentation/drawbot/image1.py --output documentation/drawbot/image1.png
# Compress with image with imagemagik:
# 

# Import moduels from external python packages: https://pypi.org/
#from drawbot_skia.drawbot import *
from drawBot import *
from fontTools.ttLib import TTFont
from fontTools.misc.fixedTools import floatToFixedToStr

# Import moduels from the Python Standard Library: https://docs.python.org/3/library/
import subprocess
import sys
import argparse

# Constants, these are the main "settings" for the image
WIDTH, HEIGHT, MARGIN, FRAMES = 2048*2, 1024*2, 128*2, 1
FONT_PATH = "fonts/variable/Hasubi-Mono[wght].ttf"
AUXILIARY_FONT_PATH = "fonts/variable/Hasubi-Mono[wght].ttf"
UNIT = MARGIN/4
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
    stroke(0)
    strokeWidth(2)
    STEP_X, STEP_Y = 0, 0
    INCREMENT_X, INCREMENT_Y = MARGIN / 4, MARGIN / 4
    for x in range(56):
        polygon((MARGIN + STEP_X, MARGIN), (MARGIN + STEP_X, HEIGHT - MARGIN))
        STEP_X += INCREMENT_X
    for y in range(24):
        polygon((MARGIN, MARGIN + STEP_Y), (WIDTH - MARGIN, MARGIN + STEP_Y))
        STEP_Y += INCREMENT_Y
    strokeWidth(4)
    fill(None)
    rect(MARGIN, MARGIN, WIDTH - (MARGIN * 2), HEIGHT - (MARGIN * 2))
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

# Draws a rounded rectangle
def rectRounded(x,y,w,h,radius):
    path = BezierPath()
    sR=0.5*radius
    w=w-radius
    h=h-radius
    path.rect(x,y+sR,w+radius,h)
    path.rect(x+sR,y,w,h+radius)
    path.oval(x,y,radius,radius)
    path.oval(x+w,y,radius,radius)
    path.oval(x,y+h,radius,radius)
    path.oval(x+w,y+h,radius,radius)
    path.removeOverlap()
    drawPath(path)

# Draw the page/frame and a grid if "GRID_VIEW" is set to "True"
def draw_background():
    newPage(WIDTH, HEIGHT)
    fill(0.3)
    #rect(-2, -2, WIDTH + 2, HEIGHT + 2)
    if GRID_VIEW:
        grid()
    else:
        pass


# Draw main text
#GRID_VIEW = True
def draw_main_text():
    fill(0,0,0,0.8)
    stroke(None)
    font(FONT_PATH)
    fontSize(UNIT*1.5)
    fontVariations(wght = 400)

    # main window
    # x, y, w, h, radius
    fill(0.05,0.05,0.07,0.1)
    rectRounded( MARGIN+(UNIT*1.5), MARGIN+(UNIT*1.5), UNIT*37, UNIT*20, UNIT*2.75)
    rectRounded( MARGIN+(UNIT*1.75), MARGIN+(UNIT*1.75), UNIT*37.5, UNIT*20.5, UNIT*2.4)
    fill(0, 0, 0, 1)
    #fill(0)
    rectRounded( MARGIN+(UNIT*2), MARGIN+(UNIT*2), UNIT*37, UNIT*20, UNIT*2)


    fill(0.05,0.05,0.07,0.1)
    rectRounded( MARGIN+(UNIT*40.5), MARGIN+(UNIT*1.5), UNIT*13, UNIT*20, UNIT*2.75)
    rectRounded( MARGIN+(UNIT*40.75), MARGIN+(UNIT*1.75), UNIT*13.5, UNIT*20.5, UNIT*2.4)
    fill(0, 0, 0, 1)
    #fill(0)
    rectRounded( MARGIN+(UNIT*41), MARGIN+(UNIT*2), UNIT*13, UNIT*20, UNIT*2)

    # Buttons
    # Red
    fill(0.03, 0.03, 0.03, 0.3)
    oval( MARGIN+(UNIT*2.75), MARGIN+(UNIT*19.75), UNIT*1.5, UNIT*1.5)
    fill(1, 0.2, 0, 0.5) 
    oval( MARGIN+(UNIT*3), MARGIN+(UNIT*20), UNIT, UNIT)
    fill(1, 0.25, 0) 
    oval( MARGIN+(UNIT*3.1), MARGIN+(UNIT*20.1), UNIT/1.25, UNIT/1.25)
    fill(1, 0.6, 0.0, 0.6) 
    oval( MARGIN+(UNIT*3.375), MARGIN+(UNIT*20.375), UNIT/4, UNIT/4)

    # YELLOW
    fill(0.03, 0.03, 0.03, 0.3)
    oval( MARGIN+(UNIT*4.75), MARGIN+(UNIT*19.75), UNIT*1.5, UNIT*1.5)
    fill(1, 0.3, 0, 0.9) 
    oval( MARGIN+(UNIT*5), MARGIN+(UNIT*20), UNIT, UNIT)
    fill(1, 0.55, 0) 
    oval( MARGIN+(UNIT*5.1), MARGIN+(UNIT*20.1), UNIT/1.25, UNIT/1.25)
    fill(1, 0.9, 0.3, 0.5) 
    oval( MARGIN+(UNIT*5.375), MARGIN+(UNIT*20.375), UNIT/4, UNIT/4)
    
   # GREEN 
    fill(0.03, 0.03, 0.03, 0.3)
    oval( MARGIN+(UNIT*6.75), MARGIN+(UNIT*19.75), UNIT*1.5, UNIT*1.5)
    fill(0, 0.8, 0.4, 0.5)
    oval( MARGIN+(UNIT*7), MARGIN+(UNIT*20), UNIT, UNIT)
    fill(0, 0.8, 0.4)
    oval( MARGIN+(UNIT*7.1), MARGIN+(UNIT*20.1), UNIT/1.25, UNIT/1.25)
    fill(0.2, 1, 1, 0.8)
    oval( MARGIN+(UNIT*7.375), MARGIN+(UNIT*20.375), UNIT/4, UNIT/4)

    # GRAY
    fill(0.03, 0.03, 0.03, 0.3)
    oval( MARGIN+(UNIT*41.75), MARGIN+(UNIT*19.75), UNIT*1.5, UNIT*1.5)
    fill(0.5, 0.5, 0.5, 0.4)
    oval( MARGIN+(UNIT*42), MARGIN+(UNIT*20), UNIT, UNIT)
    fill(0.4, 0.4, 0.4)
    oval( MARGIN+(UNIT*42.1), MARGIN+(UNIT*20.1), UNIT/1.25, UNIT/1.25)
    fill(0.5, 0.5, 0.5)
    oval( MARGIN+(UNIT*42.375), MARGIN+(UNIT*20.375), UNIT/4, UNIT/4)

    fill(0.03, 0.03, 0.03, 0.3)
    oval( MARGIN+(UNIT*43.75), MARGIN+(UNIT*19.75), UNIT*1.5, UNIT*1.5)
    fill(0.5, 0.5, 0.5, 0.4)
    oval( MARGIN+(UNIT*44), MARGIN+(UNIT*20), UNIT, UNIT)
    fill(0.4, 0.4, 0.4)
    oval( MARGIN+(UNIT*44.1), MARGIN+(UNIT*20.1), UNIT/1.25, UNIT/1.25)
    fill(0.5, 0.5, 0.5)
    oval( MARGIN+(UNIT*44.375), MARGIN+(UNIT*20.375), UNIT/4, UNIT/4)

    fill(0.03, 0.03, 0.03, 0.3)
    oval( MARGIN+(UNIT*45.75), MARGIN+(UNIT*19.75), UNIT*1.5, UNIT*1.5)
    fill(0.5, 0.5, 0.5, 0.4)
    oval( MARGIN+(UNIT*46), MARGIN+(UNIT*20), UNIT, UNIT)
    fill(0.4, 0.4, 0.4)
    oval( MARGIN+(UNIT*46.1), MARGIN+(UNIT*20.1), UNIT/1.25, UNIT/1.25)
    fill(0.5, 0.5, 0.5)
    oval( MARGIN+(UNIT*46.375), MARGIN+(UNIT*20.375), UNIT/4, UNIT/4)

    # Line Numbers
    fill(0.25, 0.25, 0.25)
    text("01", ( MARGIN+(UNIT*3), MARGIN+(UNIT*17.5)))
    text("02", ( MARGIN+(UNIT*3), MARGIN+(UNIT*15.5)))
    text("03", ( MARGIN+(UNIT*3), MARGIN+(UNIT*13.5)))
    text("04", ( MARGIN+(UNIT*3), MARGIN+(UNIT*11.5)))
    text("05", ( MARGIN+(UNIT*3), MARGIN+(UNIT*9.5)))
    fill(0, 1, 0.5, 0.05)
    rectRounded( MARGIN+(UNIT*5), MARGIN+(UNIT*7), UNIT*33, UNIT*2, UNIT/1.5)
    fill(None)
    stroke(0,1,0.4)
    strokeWidth(6)
    rectRounded( MARGIN+(UNIT*14.75), MARGIN+(UNIT*7), UNIT*1, UNIT*2, UNIT/1.5)
    stroke(None)
    fill(0, 1, 0.4)
    text("06", ( MARGIN+(UNIT*3), MARGIN+(UNIT*7.5)))
    fill(0.25, 0.25, 0.25)
    text("07", ( MARGIN+(UNIT*3), MARGIN+(UNIT*5.5)))


    fill(0.45, 0.45, 0.45)
    text('   # Print "كــن فيكون" six times', ( MARGIN+(UNIT*3), MARGIN+(UNIT*17.5)))
    
   #text("   if PRINT_DEMO == True:", ( MARGIN+(UNIT*3), MARGIN+(UNIT*15.5)))
    fill(0, 0.6, 1)
    text("   if", ( MARGIN+(UNIT*3), MARGIN+(UNIT*15.5)))
    fill(1)
    text("      PRINT_DEMO", ( MARGIN+(UNIT*3), MARGIN+(UNIT*15.5)))
    #fill(1)
    #text("      PRINT_DEMO == True:", ( MARGIN+(UNIT*3), MARGIN+(UNIT*15.5)))
    fill(0, 0.6, 1)
    text("                 ==", ( MARGIN+(UNIT*3), MARGIN+(UNIT*15.5)))
    fill(1, 0.6, 0) 
    text("                    True", ( MARGIN+(UNIT*3), MARGIN+(UNIT*15.5)))
    fill(1)
    text("                        :", ( MARGIN+(UNIT*3), MARGIN+(UNIT*15.5)))
    #text("   if PRINT_DEMO == True:", ( MARGIN+(UNIT*3), MARGIN+(UNIT*15.5)))
    
    
    #text("       for i in range(6):", ( MARGIN+(UNIT*3), MARGIN+(UNIT*13.5)))
    fill(0, 0.6, 1)
    text("       for", ( MARGIN+(UNIT*3), MARGIN+(UNIT*13.5)))
    fill(1)
    text("           i", ( MARGIN+(UNIT*3), MARGIN+(UNIT*13.5)))
    fill(0, 0.6, 1)
    text("             in", ( MARGIN+(UNIT*3), MARGIN+(UNIT*13.5)))
    fill(1, 0.6, 0) 
    text("                range", ( MARGIN+(UNIT*3), MARGIN+(UNIT*13.5)))
    fill(1)
    text("                     (", ( MARGIN+(UNIT*3), MARGIN+(UNIT*13.5)))
    fill(1, 0.1, 0) 
    text("                      6", ( MARGIN+(UNIT*3), MARGIN+(UNIT*13.5)))
    fill(1)
    text("                       ):", ( MARGIN+(UNIT*3), MARGIN+(UNIT*13.5)))
    #text("       for i in range(6):", ( MARGIN+(UNIT*3), MARGIN+(UNIT*13.5)))
    #text("       for i in range(6):", ( MARGIN+(UNIT*3), MARGIN+(UNIT*13.5)))



    #text('                              , (M+U, M+U))', ( MARGIN+(UNIT*3), MARGIN+(UNIT*11.5)))
    fill(1)
    text('           text(', ( MARGIN+(UNIT*3), MARGIN+(UNIT*11.5)))
    fill(1, 0.1, 0)
    text('               (', ( MARGIN+(UNIT*3), MARGIN+(UNIT*11.5)))
    fill(0, 1, 0.4)
    text('"كــن فيكون"', ( MARGIN+(UNIT*15.4), MARGIN+(UNIT*11.5)))
    fill(1)
    text('                            ,', ( MARGIN+(UNIT*3), MARGIN+(UNIT*11.5)))
    fill(1, 0.6, 0)
    text('                              ( ', ( MARGIN+(UNIT*3), MARGIN+(UNIT*11.5)))
    fill(1, 0.1, 0)
    text('                               32', ( MARGIN+(UNIT*3), MARGIN+(UNIT*11.5)))
    fill(0, 0.6, 1)
    text('                                 +', ( MARGIN+(UNIT*3), MARGIN+(UNIT*11.5)))
    fill(1)
    text('                                  U,', ( MARGIN+(UNIT*3), MARGIN+(UNIT*11.5)))
    fill(1, 0.1, 0)
    text('                                     8', ( MARGIN+(UNIT*3), MARGIN+(UNIT*11.5)))
    fill(0, 0.6, 1)
    text('                                      *', ( MARGIN+(UNIT*3), MARGIN+(UNIT*11.5)))
    fill(1)
    text('                                       i', ( MARGIN+(UNIT*3), MARGIN+(UNIT*11.5)))
    fill(1, 0.6, 0)
    text('                                        )', ( MARGIN+(UNIT*3), MARGIN+(UNIT*11.5)))
    fill(1, 0.1, 0)
    text('                                         )', ( MARGIN+(UNIT*3), MARGIN+(UNIT*11.5)))
    #text('                              , (M+U, M))', ( MARGIN+(UNIT*3), MARGIN+(UNIT*11.5)))
    #text('                              , (M+U, M))', ( MARGIN+(UNIT*3), MARGIN+(UNIT*11.5)))
    #text('                              , (M+U, M))', ( MARGIN+(UNIT*3), MARGIN+(UNIT*11.5)))

    # Output
    fill(0, 1, 0.4)
    text("كــن فيكون", ( MARGIN+(UNIT*45), MARGIN+(UNIT*17.5)))
    text("كــن فيكون", ( MARGIN+(UNIT*45), MARGIN+(UNIT*15.5)))
    text("كــن فيكون", ( MARGIN+(UNIT*45), MARGIN+(UNIT*13.5)))
    text("كــن فيكون", ( MARGIN+(UNIT*45), MARGIN+(UNIT*11.5)))
    text("كــن فيكون", ( MARGIN+(UNIT*45), MARGIN+(UNIT*9.5)))
    text("كــن فيكون", ( MARGIN+(UNIT*45), MARGIN+(UNIT*7.5)))
    fill(1)
    text("حاسوبي", ( MARGIN+(UNIT*48), MARGIN+(UNIT*5.5)))
    fill(0, 1, 0.5)
    #rectRounded( MARGIN+(UNIT*47), MARGIN+(UNIT*5), UNIT*0.25, UNIT*2, UNIT/4)

    #text("       else:", ( MARGIN+(UNIT*3), MARGIN+(UNIT*9.5)))
    fill(0, 0.6, 1)
    text("       else", ( MARGIN+(UNIT*3), MARGIN+(UNIT*9.5)))
    fill(1)
    text("           :", ( MARGIN+(UNIT*3), MARGIN+(UNIT*9.5)))
    #text("       else:", ( MARGIN+(UNIT*3), MARGIN+(UNIT*9.5)))
    #text("       else:", ( MARGIN+(UNIT*3), MARGIN+(UNIT*9.5)))

    fill(0, 0.6, 1)
    text("           pass", ( MARGIN+(UNIT*3), MARGIN+(UNIT*7.5)))
    #text(, ( MARGIN+(UNIT*3), MARGIN+(UNIT*19)))

    # Status Bar
    fill(0.3, 0.3, 0.3, 0.4)
    rectRounded( MARGIN+(UNIT*3), MARGIN+(UNIT*3), UNIT*35, UNIT*2, UNIT/1.5)
    fill(0.4, 0.4, 0.4)
    fill(0, 1, 0.4)
    text(" hasubi-mono-specimen.py", ( MARGIN+(UNIT*3), MARGIN+(UNIT*3.5)))



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
    #draw_divider_lines()
    #draw_auxiliary_text()
    # Save output, using the "--output" flag location
    saveImage(args.output)
    # Print done in the terminal
    print("DrawBot: Done")
