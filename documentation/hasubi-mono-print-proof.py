# RENDER THIS DOCUMENT WITH DRAWBOT: http://www.drawbot.com
# Unit Space: 72dpi (dots per inch)
from drawBot import *
from datetime import date
import math


# CONSTANTS
WIDTH = 792    # Width
HEIGHT = 612   # Height
MARGIN = 36    # Margin
UNIT = 9       # Unit
TODAY = str(date.today())
HASUBI_MONO_VF = "specimen-fonts/Hasubi-Mono[wght].ttf"
GRID_VIEW = False # Change this to "True" for a grid overlay


# Draws a grid
def grid():
    stroke(1, 0, 0, 0.5)
    strokeWidth(0.5)
    STEP_X, STEP_Y = 0, 0
    INCREMENT_X, INCREMENT_Y = MARGIN / 2, MARGIN / 2
    rect(MARGIN, MARGIN, WIDTH - (MARGIN * 2), HEIGHT - (MARGIN * 2))
    for x in range(41):
        polygon((MARGIN + STEP_X, MARGIN), (MARGIN + STEP_X, HEIGHT - MARGIN))
        STEP_X += INCREMENT_X
    for y in range(31):
        polygon((MARGIN, MARGIN + STEP_Y), (WIDTH - MARGIN, MARGIN + STEP_Y))
        STEP_Y += INCREMENT_Y
    polygon((WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
    polygon((0, HEIGHT / 2), (WIDTH, HEIGHT / 2))


# Draw page info
def draw_page_info(page_number, section):
    fill(0)
    stroke(0)
    strokeWidth(1)
    line((MARGIN, HEIGHT - MARGIN - UNIT*2), (WIDTH - MARGIN, HEIGHT - MARGIN - UNIT*2))
    line((MARGIN, MARGIN + UNIT*2), (WIDTH - MARGIN, MARGIN + UNIT*2))
    font(HASUBI_MONO_VF)
    stroke(None)
    fontSize(13)
    text("Page: "+str(int(page_number)), (MARGIN, MARGIN+(UNIT*0)))
    text(TODAY, (WIDTH-MARGIN-(UNIT*7.4), MARGIN+(UNIT*0)))
    if section == 0:
        text("Section 0: Cover Page", (MARGIN, HEIGHT-MARGIN-(UNIT*1)))
    if section == 1:
        text("Section 1: Cover Letter", (MARGIN, HEIGHT-MARGIN-(UNIT*1)))
    if section == 2:
        text("Section 2: Hasubi Mono Specimen", (MARGIN, HEIGHT-MARGIN-(UNIT*1)))
    text("حاسوبي مونو", (WIDTH-MARGIN-(UNIT*8), HEIGHT-MARGIN-(UNIT*1)))


# New Page
def new_page():
    newPage(WIDTH, HEIGHT)
    fill(0.9)
    rect(-2, -2, WIDTH+2, HEIGHT+2)
    if GRID_VIEW:
        grid()
    else:
        pass


# TEST FONTS
font(HASUBI_MONO_VF)
for axis, data in listFontVariations().items():
    print((axis, data))
# for eachFontName in installedFonts():
#    print(eachFontName)


newDrawing()
page_number = 0
new_page() #--------------------------------------------------#
draw_page_info(page_number, 0)
font(HASUBI_MONO_VF)
fontVariations(wght = 400)
fontSize(26)
stroke(None)
fill(0)
text("Hasubi Mono",  (MARGIN+UNIT*0, MARGIN+UNIT*52))
text("Print Proof",  (MARGIN+UNIT*0, MARGIN+UNIT*49))
page_number += 1


new_page() #--------------------------------------------------#
draw_page_info(page_number, 1)
LOREM_IPSUM = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
font(HASUBI_MONO_VF)
fontVariations(wght = 400)
fontSize(26)
stroke(None)
fill(0)

text("Contact Info",  (MARGIN+UNIT*0, MARGIN+UNIT*52))
fontSize(13)
text("Email: elih@protonmail.com",  (MARGIN+UNIT*0, MARGIN+UNIT*44))
text("GitHub: https://github.com/eliheuer",  (MARGIN+UNIT*0, MARGIN+UNIT*42))
text("Twitter: @eliheuer",  (MARGIN+UNIT*0, MARGIN+UNIT*40))
text("Mastodon: @elih@typo.social",  (MARGIN+UNIT*0, MARGIN+UNIT*38))
text("Ethereum ENS: elih.eth",  (MARGIN+UNIT*0, MARGIN+UNIT*36))

fontSize(26)
text("Sample Text",  (MARGIN+UNIT*42, MARGIN+UNIT*52))

fontSize(13)
lineHeight(18)
textBox(LOREM_IPSUM*4, (MARGIN+(UNIT*42), MARGIN+(UNIT*4), UNIT*38, UNIT*43.5))
#fill(1,0,0)
#rect(MARGIN+(UNIT*42), MARGIN+(UNIT*4), UNIT*38, UNIT*44)
page_number += 1


new_page() #--------------------------------------------------#
draw_page_info(page_number, 1)
font(HASUBI_MONO_VF)
fontVariations(wght = 400)
fontSize(26)
stroke(None)
fill(0)

fontSize(13)
lineHeight(18)
textBox(LOREM_IPSUM*4, (MARGIN+(UNIT*0),  MARGIN+(UNIT*4), UNIT*38, UNIT*49.5))
textBox(LOREM_IPSUM*4, (MARGIN+(UNIT*42), MARGIN+(UNIT*4), UNIT*38, UNIT*49.5))
#fill(1,0,0)
#rect(MARGIN+(UNIT*42), MARGIN+(UNIT*4), UNIT*38, UNIT*44)
page_number += 1


new_page() #--------------------------------------------------#
draw_page_info(page_number, 2)
HASUBI_MONO_INFO = "Hasubi Mono (حاسوبي مونو) is a horizontal contrast monospace font designed by Eli Heuer."
font(HASUBI_MONO_VF)
fontVariations(wght = 400)
fontSize(26)
stroke(None)
fill(0)

text("Hasubi Mono Specimen",  (MARGIN+UNIT*0, MARGIN+UNIT*52))


fontSize(169)
text("Aب",  (MARGIN+UNIT*51, MARGIN+UNIT*18))


fontSize(13)
lineHeight(18)
textBox(HASUBI_MONO_INFO*9, (MARGIN+(UNIT*0), MARGIN+(UNIT*4), UNIT*38, UNIT*43.5))
text("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z",  (MARGIN+UNIT*42, MARGIN+UNIT*46))
text("a b c d e f g h i j k l m n o p q r s t u v w x y z",  (MARGIN+UNIT*42, MARGIN+UNIT*44))
text("1 2 3 4 5 6 7 8 9 0 ! @ # % ^ & * ( ) - _ + = , . :",  (MARGIN+UNIT*42, MARGIN+UNIT*42))
text("اأإ ب ببب ت تتت ث ثثث ج ججج ح ححح خ خخخ د ـد ذ ـذ ر",  (MARGIN+UNIT*42, MARGIN+UNIT*40))
text("ــر ز ــز س سسس ش ششش ص صصص ض ضضض ع ععع غ غغغ ف ففف",  (MARGIN+UNIT*42, MARGIN+UNIT*38))
text("ق ققق ك ككك ل للل م ممم ن ننن ه ههه و ــــو ي ييي ء",  (MARGIN+UNIT*42, MARGIN+UNIT*36))

#fill(1,0,0)
#rect(MARGIN+(UNIT*42), MARGIN+(UNIT*4), UNIT*38, UNIT*44)
page_number += 1


new_page() #--------------------------------------------------#
draw_page_info(page_number, 2)
font(HASUBI_MONO_VF)
fontVariations(wght = 400)
fontSize(26)
stroke(None)
fill(0)

fontSize(26)
text("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z",  (MARGIN+UNIT*2, MARGIN+UNIT*52))
text("a b c d e f g h i j k l m n o p q r s t u v w x y z",  (MARGIN+UNIT*2, MARGIN+UNIT*48))
text("1 2 3 4 5 6 7 8 9 0 ! @ # % ^ & * ( ) - _ + = , . :",  (MARGIN+UNIT*2, MARGIN+UNIT*44))
text("اأإ ب ببب ت تتت ث ثثث ج ججج ح ححح خ خخخ د ـد ذ ـذ ر",  (MARGIN+UNIT*2, MARGIN+UNIT*40))
text("ــر ز ــز س سسس ش ششش ص صصص ض ضضض ع ععع غ غغغ ف ففف",  (MARGIN+UNIT*2, MARGIN+UNIT*36))
text("ق ققق ك ككك ل للل م ممم ن ننن ه ههه و ــــو ي ييي ء",  (MARGIN+UNIT*2, MARGIN+UNIT*32))

text("Ashadu ya ilahi be anaka",  (MARGIN+UNIT*42, MARGIN+UNIT*22))
text("khalaqtani lee erfanekah",  (MARGIN+UNIT*42, MARGIN+UNIT*18))
text("wa ebadatek. Ashhadu fee",  (MARGIN+UNIT*42, MARGIN+UNIT*14))
text("hadal heen be ajzee waaa",  (MARGIN+UNIT*42, MARGIN+UNIT*10))
text("quatekah wa daafi wa iqt",  (MARGIN+UNIT*42, MARGIN+UNIT*6))

text("أشهد يا إلهي بأنك خلقتني",  (MARGIN+UNIT*2, MARGIN+UNIT*22))
text("لعرفانك وعبادتك. أشهد في",  (MARGIN+UNIT*2, MARGIN+UNIT*18))
text("هذا الـحين بـعجزي وقـوتك",  (MARGIN+UNIT*2, MARGIN+UNIT*14))
text("وضــــعفي واقتدارك وفقري",  (MARGIN+UNIT*2, MARGIN+UNIT*10))
text("وغــــــــــــــــــنائك",  (MARGIN+UNIT*2, MARGIN+UNIT*6))

#fill(1,0,0)
#rect(MARGIN+(UNIT*42), MARGIN+(UNIT*4), UNIT*38, UNIT*44)
page_number += 1


new_page() #--------------------------------------------------#
draw_page_info(page_number, 2)
font(HASUBI_MONO_VF)
fontVariations(wght = 400)
fontSize(26)
stroke(None)
fill(0)

text("# Python demo: draws a grid",  (MARGIN+UNIT*0, MARGIN+UNIT*52))
text("def grid():",  (MARGIN+UNIT*0, MARGIN+UNIT*48))
text("    STEP_X, STEP_Y, INC_X, INC_Y = 0, 0, M / 2, M / 2",  (MARGIN+UNIT*0, MARGIN+UNIT*44))
text("    rect(M, M, W - (M * 2), H - (M * 2))",  (MARGIN+UNIT*0, MARGIN+UNIT*40))
text("    for x in range(41):",  (MARGIN+UNIT*0, MARGIN+UNIT*36))
text("        polygon((M + STEP_X, M), (M + STEP_X, H - M))",  (MARGIN+UNIT*0, MARGIN+UNIT*32))
text("        STEP_X += INC_X",  (MARGIN+UNIT*0, MARGIN+UNIT*28))
text("    for y in range(31):",  (MARGIN+UNIT*0, MARGIN+UNIT*24))
text("        polygon((M, M + STEP_Y), (W - M, M + STEP_Y))",  (MARGIN+UNIT*0, MARGIN+UNIT*20))
text("        STEP_Y += INC_Y",  (MARGIN+UNIT*0, MARGIN+UNIT*16))
text("    polygon((W / 2, 0), (W / 2, H))",  (MARGIN+UNIT*0, MARGIN+UNIT*12))
text("    polygon((0, H / 2), (W, H / 2))",  (MARGIN+UNIT*0, MARGIN+UNIT*8))

page_number += 1


new_page() #--------------------------------------------------#
draw_page_info(page_number, 2)
font(HASUBI_MONO_VF)
fontVariations(wght = 400)
fontSize(13)
stroke(None)
fill(0)

text("# Python demo: draws a grid",  (MARGIN+UNIT*0, MARGIN+UNIT*52))
text("def grid():",  (MARGIN+UNIT*0, MARGIN+UNIT*50))
text("    STEP_X, STEP_Y, INC_X, INC_Y = 0, 0, M / 2, M / 2",  (MARGIN+UNIT*0, MARGIN+UNIT*48))
text("    rect(M, M, W - (M * 2), H - (M * 2))",  (MARGIN+UNIT*0, MARGIN+UNIT*46))
text("    for x in range(41):",  (MARGIN+UNIT*0, MARGIN+UNIT*44))
text("        polygon((M + STEP_X, M), (M + STEP_X, H - M))",  (MARGIN+UNIT*0, MARGIN+UNIT*42))
text("        STEP_X += INC_X",  (MARGIN+UNIT*0, MARGIN+UNIT*40))
text("    for y in range(31):",  (MARGIN+UNIT*0, MARGIN+UNIT*38))
text("        polygon((M, M + STEP_Y), (W - M, M + STEP_Y))",  (MARGIN+UNIT*0, MARGIN+UNIT*36))
text("        STEP_Y += INC_Y",  (MARGIN+UNIT*0, MARGIN+UNIT*34))
text("    polygon((W / 2, 0), (W / 2, H))",  (MARGIN+UNIT*0, MARGIN+UNIT*32))
text("    polygon((0, H / 2), (W, H / 2))",  (MARGIN+UNIT*0, MARGIN+UNIT*30))

text('# Print "كن فيكون" six times',  (MARGIN+UNIT*0, MARGIN+UNIT*22))
text("if PRINT_DEMO == True:",  (MARGIN+UNIT*0, MARGIN+UNIT*20))
text("    for i in range(6):",  (MARGIN+UNIT*0, MARGIN+UNIT*18))
text('        text("كــــن فيكون", (MARGIN, MARGIN+UNIT*i))',  (MARGIN+UNIT*0, MARGIN+UNIT*16))
text("    else:",  (MARGIN+UNIT*0, MARGIN+UNIT*14))
text("        pass",  (MARGIN+UNIT*0, MARGIN+UNIT*12))

fontSize(26*2)
text("كــــن فيكون",  (MARGIN+UNIT*44, MARGIN+UNIT*50))
text("كــــن فيكون",  (MARGIN+UNIT*44, MARGIN+UNIT*42))
text("كــــن فيكون",  (MARGIN+UNIT*44, MARGIN+UNIT*34))
text("كــــن فيكون",  (MARGIN+UNIT*44, MARGIN+UNIT*26))
text("كــــن فيكون",  (MARGIN+UNIT*44, MARGIN+UNIT*18))
text("كــــن فيكون",  (MARGIN+UNIT*44, MARGIN+UNIT*10))

page_number += 1


new_page() #--------------------------------------------------#
draw_page_info(page_number, 2)
LATIN_TEXT_ONE = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
ARABIC_TEXT_ONE = "هل من مفرج غير الله قل سبحان الله هو الله كل عباد له وكل بأمره قائمون.  "

font(HASUBI_MONO_VF)
fontVariations(wght = 400)
stroke(None)
fill(0)

fontSize(13)
lineHeight(18)
textBox(LATIN_TEXT_ONE*1, (MARGIN+(UNIT*0),  MARGIN+(UNIT*4), UNIT*38, UNIT*49.5), align="left")
textBox(ARABIC_TEXT_ONE*8, (MARGIN+(UNIT*42), MARGIN+(UNIT*4), UNIT*38, UNIT*49.5), align="right")

fontSize(11)
textBox(LATIN_TEXT_ONE*1, (MARGIN+(UNIT*0),  MARGIN+(UNIT*4), UNIT*38, UNIT*21.4), align="left")
textBox(ARABIC_TEXT_ONE*10, (MARGIN+(UNIT*42), MARGIN+(UNIT*4), UNIT*38, UNIT*21.4), align="right")

#fill(1,0,0)
#rect(MARGIN+(UNIT*42), MARGIN+(UNIT*4), UNIT*38, UNIT*44)
page_number += 1


new_page() #--------------------------------------------------#
draw_page_info(page_number, 2)
MIXED_TEXT_ONE = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. هل من مفرج غير الله. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. قل سبحان الله هو الله. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. كل عباد له وكل بأمره قائمون. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

font(HASUBI_MONO_VF)
fontVariations(wght = 400)
stroke(None)
fill(0)

fontSize(13)
lineHeight(18)
textBox(MIXED_TEXT_ONE*2, (MARGIN+(UNIT*0),  MARGIN+(UNIT*4), UNIT*38, UNIT*49.5), align="left")
fontSize(11)
textBox(MIXED_TEXT_ONE*3, (MARGIN+(UNIT*42), MARGIN+(UNIT*4), UNIT*38, UNIT*49.4), align="left")

#fill(1,0,0)
#rect(MARGIN+(UNIT*42), MARGIN+(UNIT*4), UNIT*38, UNIT*44)
page_number += 1
#saveImage("test-01.png")







# Saving and post-processing #--------------------------------#
saveImage("hasubi-mono-print-proof.pdf")
print("DrawBot: Done :-)")



