## Fontbakery report

Fontbakery version: 0.8.10

<details><summary><b>[10] HasubiMono-Black.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1080, but got 1035 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** Font is monospaced but 73 glyphs (8.45%) have a different width. You should check the widths of: ['uni27E8', 'uni27E9', 'guillemotleft', 'brokenbar.001', 'uni20BF', 'uni20B5', 'colonmonetary', 'dong', 'uni20B2', 'uni20B4', 'uni20AD', 'uni20BE', 'uni20BA', 'uni20BC', 'uni20A6', 'uni20B1', 'uni20BD', 'uni20A8', 'uni20B9', 'uni20AA', 'uni20B8', 'uni20AE', 'uni20A9', 'approxequal', 'logicalnot', 'emptyset', 'infinity', 'integral', 'uni2126', 'uni2206', 'product', 'summation', 'radical', 'partialdiff', 'uni00B5', 'perthousand', 'arrowup', 'uni2197', 'arrowright', 'uni2198', 'arrowdown', 'uni2199', 'arrowleft', 'uni2196', 'arrowboth', 'arrowupdn', 'uni25CF', 'circle', 'openbullet', 'uni25C6', 'uni25C7', 'lozenge', 'filledbox', 'uni25A1', 'uni25AA', 'uni25AB', 'triagup', 'uni25B6', 'triagdn', 'uni25C0', 'uni25B3', 'uni25B7', 'uni25BD', 'uni25C1', 'uni25B4', 'uni25B8', 'uni25BE', 'uni25C2', 'uni25B5', 'uni25B9', 'uni25BF', 'uni25C3', 'newGlyph.001'] [code: mono-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- ar.test.001

	- brokenbar.001

	- doublestrokear

	- eight.numr

	- eight.tf

	- five.numr

	- five.tf

	- four.numr

	- four.tf

	- gafsarkashabovear

	- gafsarkashcenterar

	- miniKehehar

	- newGlyph.001

	- nine.numr

	- nine.tf

	- one.numr

	- one.tf

	- seven.numr

	- seven.tf

	- six.numr

	- six.tf

	- three.numr

	- three.tf

	- threedotsdownabovear

	- threedotsdowncenterar

	- threedotsupbelowar

	- two.numr

	- two.tf

	- twodotsverticalabovear

	- twodotsverticalbelowar

	- uni00B5

	- uni03020300

	- uni03020300.case

	- uni03020301

	- uni03020301.case

	- uni03020303

	- uni03020303.case

	- uni03020309

	- uni03020309.case

	- uni03060300

	- uni03060300.case

	- uni03060301

	- uni03060301.case

	- uni03060303

	- uni03060303.case

	- uni03060309

	- uni03060309.case

	- zero.numr 

	- And zero.tf
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: ogonek	Contours detected: 0	Expected: 1

	- Glyph name: uni0312	Contours detected: 0	Expected: 1

	- Glyph name: uni0327	Contours detected: 0	Expected: 1

	- Glyph name: uni0328	Contours detected: 0	Expected: 1

	- Glyph name: uni0E3F	Contours detected: 5	Expected: 3

	- Glyph name: perthousand	Contours detected: 0	Expected: 6 or 7

	- Glyph name: colonmonetary	Contours detected: 0	Expected: 1 or 3

	- Glyph name: uni20A6	Contours detected: 0	Expected: 1, 3 or 5

	- Glyph name: uni20A8	Contours detected: 0	Expected: 3

	- Glyph name: uni20A9	Contours detected: 0	Expected: 1, 3, 4 or 7

	- Glyph name: uni20AA	Contours detected: 0	Expected: 2

	- Glyph name: dong	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni20AD	Contours detected: 0	Expected: 1

	- Glyph name: uni20AE	Contours detected: 0	Expected: 1

	- Glyph name: uni20B1	Contours detected: 0	Expected: 1, 2 or 4

	- Glyph name: uni20B2	Contours detected: 0	Expected: 1, 2 or 3

	- Glyph name: uni20B4	Contours detected: 0	Expected: 1 or 2

	- Glyph name: uni20B5	Contours detected: 0	Expected: 1 or 2

	- Glyph name: uni20B8	Contours detected: 0	Expected: 2

	- Glyph name: uni20B9	Contours detected: 0	Expected: 1

	- Glyph name: uni20BA	Contours detected: 0	Expected: 1

	- Glyph name: uni20BC	Contours detected: 0	Expected: 1

	- Glyph name: uni20BD	Contours detected: 0	Expected: 2

	- Glyph name: uni20BF	Contours detected: 0	Expected: 3

	- Glyph name: uni2126	Contours detected: 0	Expected: 1

	- Glyph name: arrowleft	Contours detected: 0	Expected: 1

	- Glyph name: arrowup	Contours detected: 0	Expected: 1

	- Glyph name: arrowright	Contours detected: 0	Expected: 1

	- Glyph name: arrowdown	Contours detected: 0	Expected: 1

	- Glyph name: arrowboth	Contours detected: 0	Expected: 1

	- Glyph name: arrowupdn	Contours detected: 0	Expected: 1

	- Glyph name: uni2196	Contours detected: 0	Expected: 1

	- Glyph name: uni2197	Contours detected: 0	Expected: 1

	- Glyph name: uni2198	Contours detected: 0	Expected: 1

	- Glyph name: uni2199	Contours detected: 0	Expected: 1

	- Glyph name: partialdiff	Contours detected: 0	Expected: 2

	- Glyph name: emptyset	Contours detected: 0	Expected: 3

	- Glyph name: uni2206	Contours detected: 0	Expected: 2

	- Glyph name: product	Contours detected: 0	Expected: 1

	- Glyph name: summation	Contours detected: 0	Expected: 1

	- Glyph name: radical	Contours detected: 0	Expected: 1

	- Glyph name: infinity	Contours detected: 0	Expected: 3

	- Glyph name: integral	Contours detected: 0	Expected: 1

	- Glyph name: approxequal	Contours detected: 0	Expected: 2

	- Glyph name: filledbox	Contours detected: 0	Expected: 1

	- Glyph name: uni25A1	Contours detected: 0	Expected: 2

	- Glyph name: uni25AA	Contours detected: 0	Expected: 1

	- Glyph name: uni25AB	Contours detected: 0	Expected: 2

	- Glyph name: triagup	Contours detected: 0	Expected: 1

	- Glyph name: uni25B3	Contours detected: 0	Expected: 2

	- Glyph name: uni25B6	Contours detected: 0	Expected: 1

	- Glyph name: uni25B7	Contours detected: 0	Expected: 2

	- Glyph name: triagdn	Contours detected: 0	Expected: 1

	- Glyph name: uni25BD	Contours detected: 0	Expected: 2

	- Glyph name: uni25C0	Contours detected: 0	Expected: 1

	- Glyph name: uni25C1	Contours detected: 0	Expected: 2

	- Glyph name: uni25C6	Contours detected: 0	Expected: 1

	- Glyph name: uni25C7	Contours detected: 0	Expected: 2

	- Glyph name: lozenge	Contours detected: 0	Expected: 2

	- Glyph name: circle	Contours detected: 0	Expected: 2

	- Glyph name: uni25CF	Contours detected: 0	Expected: 1

	- Glyph name: uni27E8	Contours detected: 0	Expected: 1

	- Glyph name: uni27E9	Contours detected: 0	Expected: 1

	- Glyph name: approxequal	Contours detected: 0	Expected: 2

	- Glyph name: arrowboth	Contours detected: 0	Expected: 1

	- Glyph name: arrowdown	Contours detected: 0	Expected: 1

	- Glyph name: arrowup	Contours detected: 0	Expected: 1

	- Glyph name: arrowupdn	Contours detected: 0	Expected: 1

	- Glyph name: circle	Contours detected: 0	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 0	Expected: 1 or 3

	- Glyph name: dong	Contours detected: 0	Expected: 3 or 4

	- Glyph name: emptyset	Contours detected: 0	Expected: 3

	- Glyph name: infinity	Contours detected: 0	Expected: 3

	- Glyph name: integral	Contours detected: 0	Expected: 1

	- Glyph name: lozenge	Contours detected: 0	Expected: 2

	- Glyph name: ogonek	Contours detected: 0	Expected: 1

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: partialdiff	Contours detected: 0	Expected: 2

	- Glyph name: perthousand	Contours detected: 0	Expected: 6 or 7

	- Glyph name: product	Contours detected: 0	Expected: 1

	- Glyph name: radical	Contours detected: 0	Expected: 1

	- Glyph name: summation	Contours detected: 0	Expected: 1

	- Glyph name: triagdn	Contours detected: 0	Expected: 1

	- Glyph name: triagup	Contours detected: 0	Expected: 1

	- Glyph name: uni0312	Contours detected: 0	Expected: 1

	- Glyph name: uni0327	Contours detected: 0	Expected: 1

	- Glyph name: uni0328	Contours detected: 0	Expected: 1

	- Glyph name: uni0E3F	Contours detected: 5	Expected: 3

	- Glyph name: uni20A6	Contours detected: 0	Expected: 1, 3 or 5

	- Glyph name: uni20A9	Contours detected: 0	Expected: 1, 3, 4 or 7

	- Glyph name: uni20AA	Contours detected: 0	Expected: 2

	- Glyph name: uni20AD	Contours detected: 0	Expected: 1

	- Glyph name: uni20AE	Contours detected: 0	Expected: 1

	- Glyph name: uni20B1	Contours detected: 0	Expected: 1, 2 or 4

	- Glyph name: uni20B2	Contours detected: 0	Expected: 1, 2 or 3

	- Glyph name: uni20B4	Contours detected: 0	Expected: 1 or 2

	- Glyph name: uni20B5	Contours detected: 0	Expected: 1 or 2

	- Glyph name: uni20B8	Contours detected: 0	Expected: 2

	- Glyph name: uni20B9	Contours detected: 0	Expected: 1

	- Glyph name: uni20BA	Contours detected: 0	Expected: 1

	- Glyph name: uni20BC	Contours detected: 0	Expected: 1

	- Glyph name: uni20BD	Contours detected: 0	Expected: 2

	- Glyph name: uni20BF	Contours detected: 0	Expected: 3

	- Glyph name: uni2126	Contours detected: 0	Expected: 1

	- Glyph name: uni2196	Contours detected: 0	Expected: 1

	- Glyph name: uni2197	Contours detected: 0	Expected: 1

	- Glyph name: uni2198	Contours detected: 0	Expected: 1

	- Glyph name: uni2199	Contours detected: 0	Expected: 1

	- Glyph name: uni2206	Contours detected: 0	Expected: 2

	- Glyph name: uni25A1	Contours detected: 0	Expected: 2

	- Glyph name: uni25AA	Contours detected: 0	Expected: 1

	- Glyph name: uni25AB	Contours detected: 0	Expected: 2

	- Glyph name: uni25B3	Contours detected: 0	Expected: 2

	- Glyph name: uni25B6	Contours detected: 0	Expected: 1

	- Glyph name: uni25B7	Contours detected: 0	Expected: 2

	- Glyph name: uni25BD	Contours detected: 0	Expected: 2

	- Glyph name: uni25C0	Contours detected: 0	Expected: 1

	- Glyph name: uni25C1	Contours detected: 0	Expected: 2

	- Glyph name: uni25C6	Contours detected: 0	Expected: 1

	- Glyph name: uni25C7	Contours detected: 0	Expected: 2

	- Glyph name: uni25CF	Contours detected: 0	Expected: 1

	- Glyph name: uni27E8	Contours detected: 0	Expected: 1 

	- And Glyph name: uni27E9	Contours detected: 0	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* a (U+0061): X=146.0,Y=1.0 (should be at baseline 0?)

	* b (U+0062): X=209.0,Y=-1.0 (should be at baseline 0?)

	* d (U+0064): X=303.0,Y=-1.0 (should be at baseline 0?)

	* s (U+0073): X=329.5,Y=546.0 (should be at x-height 544?)

	* u (U+0075): X=294.5,Y=2.0 (should be at baseline 0?)

	* copyright (U+00A9): X=370.0,Y=-0.5 (should be at baseline 0?)

	* copyright (U+00A9): X=142.5,Y=-0.5 (should be at baseline 0?)

	* newGlyph (U+00B5): X=184.0,Y=-1.5 (should be at baseline 0?)

	* agrave (U+00E0): X=146.0,Y=1.0 (should be at baseline 0?)

	* aacute (U+00E1): X=146.0,Y=1.0 (should be at baseline 0?)

	* acircumflex (U+00E2): X=146.0,Y=1.0 (should be at baseline 0?)

	* atilde (U+00E3): X=146.0,Y=1.0 (should be at baseline 0?)

	* adieresis (U+00E4): X=146.0,Y=1.0 (should be at baseline 0?)

	* aring (U+00E5): X=146.0,Y=1.0 (should be at baseline 0?)

	* aring (U+00E5): X=199.5,Y=737.0 (should be at cap-height 736?)

	* aring (U+00E5): X=312.5,Y=737.0 (should be at cap-height 736?)

	* ae (U+00E6): X=461.5,Y=1.5 (should be at baseline 0?)

	* ae (U+00E6): X=38.5,Y=0.5 (should be at baseline 0?)

	* eth (U+00F0): X=299.5,Y=1.0 (should be at baseline 0?)

	* ugrave (U+00F9): X=294.5,Y=2.0 (should be at baseline 0?)

	* uacute (U+00FA): X=294.5,Y=2.0 (should be at baseline 0?)

	* ucircumflex (U+00FB): X=294.5,Y=2.0 (should be at baseline 0?)

	* udieresis (U+00FC): X=294.5,Y=2.0 (should be at baseline 0?)

	* thorn (U+00FE): X=212.5,Y=1.0 (should be at baseline 0?)

	* amacron (U+0101): X=146.0,Y=1.0 (should be at baseline 0?)

	* abreve (U+0103): X=146.0,Y=1.0 (should be at baseline 0?)

	* aogonek (U+0105): X=146.0,Y=1.0 (should be at baseline 0?)

	* dcaron (U+010F): X=255.0,Y=-1.0 (should be at baseline 0?)

	* dcroat (U+0111): X=299.5,Y=1.0 (should be at baseline 0?)

	* uni0123 (U+0123): X=171.0,Y=735.0 (should be at cap-height 736?)

	* iogonek (U+012F): X=202.5,Y=734.0 (should be at cap-height 736?)

	* iogonek (U+012F): X=293.5,Y=734.0 (should be at cap-height 736?)

	* ij (U+0133): X=354.5,Y=734.0 (should be at cap-height 736?)

	* ij (U+0133): X=445.5,Y=734.0 (should be at cap-height 736?)

	* ij (U+0133): X=122.5,Y=734.0 (should be at cap-height 736?)

	* ij (U+0133): X=213.5,Y=734.0 (should be at cap-height 736?)

	* ohungarumlaut (U+0151): X=319.0,Y=738.0 (should be at cap-height 736?)

	* ohungarumlaut (U+0151): X=411.0,Y=738.0 (should be at cap-height 736?)

	* ohungarumlaut (U+0151): X=176.0,Y=738.0 (should be at cap-height 736?)

	* ohungarumlaut (U+0151): X=268.0,Y=738.0 (should be at cap-height 736?)

	* oe (U+0153): X=455.5,Y=1.5 (should be at baseline 0?)

	* oe (U+0153): X=221.0,Y=-2.0 (should be at baseline 0?)

	* utilde (U+0169): X=294.5,Y=2.0 (should be at baseline 0?)

	* umacron (U+016B): X=294.5,Y=2.0 (should be at baseline 0?)

	* ubreve (U+016D): X=294.5,Y=2.0 (should be at baseline 0?)

	* uring (U+016F): X=294.5,Y=2.0 (should be at baseline 0?)

	* uring (U+016F): X=199.5,Y=737.0 (should be at cap-height 736?)

	* uring (U+016F): X=312.5,Y=737.0 (should be at cap-height 736?)

	* uhungarumlaut (U+0171): X=294.5,Y=2.0 (should be at baseline 0?)

	* uhungarumlaut (U+0171): X=319.0,Y=738.0 (should be at cap-height 736?)

	* uhungarumlaut (U+0171): X=411.0,Y=738.0 (should be at cap-height 736?)

	* uhungarumlaut (U+0171): X=176.0,Y=738.0 (should be at cap-height 736?)

	* uhungarumlaut (U+0171): X=268.0,Y=738.0 (should be at cap-height 736?)

	* uogonek (U+0173): X=294.5,Y=2.0 (should be at baseline 0?)

	* uhorn (U+01B0): X=294.5,Y=2.0 (should be at baseline 0?)

	* uni0635 (U+0635): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0635 (U+0635): X=-32.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=-32.0,Y=-261.0 (should be at descender -260?)

	* uni0654 (U+0654): X=300.0,Y=734.0 (should be at cap-height 736?)

	* uni0654 (U+0654): X=273.0,Y=734.0 (should be at cap-height 736?)

	* uni0E3F (U+0E3F): X=264.0,Y=735.0 (should be at cap-height 736?)

	* uni1EA1 (U+1EA1): X=146.0,Y=1.0 (should be at baseline 0?)

	* uni1EA3 (U+1EA3): X=146.0,Y=1.0 (should be at baseline 0?)

	* uni1EA5 (U+1EA5): X=146.0,Y=1.0 (should be at baseline 0?)

	* uni1EA5 (U+1EA5): X=478.0,Y=738.0 (should be at cap-height 736?)

	* uni1EA7 (U+1EA7): X=146.0,Y=1.0 (should be at baseline 0?)

	* uni1EA9 (U+1EA9): X=146.0,Y=1.0 (should be at baseline 0?)

	* uni1EA9 (U+1EA9): X=400.0,Y=734.0 (should be at cap-height 736?)

	* uni1EAB (U+1EAB): X=146.0,Y=1.0 (should be at baseline 0?)

	* uni1EAB (U+1EAB): X=306.0,Y=737.0 (should be at cap-height 736?)

	* uni1EAD (U+1EAD): X=146.0,Y=1.0 (should be at baseline 0?)

	* uni1EAF (U+1EAF): X=146.0,Y=1.0 (should be at baseline 0?)

	* uni1EB1 (U+1EB1): X=146.0,Y=1.0 (should be at baseline 0?)

	* uni1EB3 (U+1EB3): X=146.0,Y=1.0 (should be at baseline 0?)

	* uni1EB5 (U+1EB5): X=146.0,Y=1.0 (should be at baseline 0?)

	* uni1EB7 (U+1EB7): X=146.0,Y=1.0 (should be at baseline 0?)

	* uni1EBF (U+1EBF): X=478.0,Y=738.0 (should be at cap-height 736?)

	* uni1EC3 (U+1EC3): X=400.0,Y=734.0 (should be at cap-height 736?)

	* uni1EC5 (U+1EC5): X=306.0,Y=737.0 (should be at cap-height 736?)

	* uni1ED1 (U+1ED1): X=478.0,Y=738.0 (should be at cap-height 736?)

	* uni1ED5 (U+1ED5): X=400.0,Y=734.0 (should be at cap-height 736?)

	* uni1ED7 (U+1ED7): X=306.0,Y=737.0 (should be at cap-height 736?)

	* uni1EE5 (U+1EE5): X=294.5,Y=2.0 (should be at baseline 0?)

	* uni1EE7 (U+1EE7): X=294.5,Y=2.0 (should be at baseline 0?)

	* uni1EE9 (U+1EE9): X=294.5,Y=2.0 (should be at baseline 0?)

	* uni1EEB (U+1EEB): X=294.5,Y=2.0 (should be at baseline 0?)

	* uni1EED (U+1EED): X=294.5,Y=2.0 (should be at baseline 0?)

	* uni1EEF (U+1EEF): X=294.5,Y=2.0 (should be at baseline 0?) 

	* And uni1EF1 (U+1EF1): X=294.5,Y=2.0 (should be at baseline 0?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* W (U+0057): L<<488.0,712.0>--<449.0,24.0>> -> L<<449.0,24.0>--<449.0,8.0>>

	* W (U+0057): L<<488.0,728.0>--<488.0,712.0>> -> L<<488.0,712.0>--<449.0,24.0>>

	* W (U+0057): L<<63.0,24.0>--<24.0,712.0>> -> L<<24.0,712.0>--<24.0,728.0>>

	* W (U+0057): L<<63.0,8.0>--<63.0,24.0>> -> L<<63.0,24.0>--<24.0,712.0>>

	* Wacute (U+1E82): L<<488.0,712.0>--<449.0,24.0>> -> L<<449.0,24.0>--<449.0,8.0>>

	* Wacute (U+1E82): L<<488.0,728.0>--<488.0,712.0>> -> L<<488.0,712.0>--<449.0,24.0>>

	* Wacute (U+1E82): L<<63.0,24.0>--<24.0,712.0>> -> L<<24.0,712.0>--<24.0,728.0>>

	* Wacute (U+1E82): L<<63.0,8.0>--<63.0,24.0>> -> L<<63.0,24.0>--<24.0,712.0>>

	* Wcircumflex (U+0174): L<<488.0,712.0>--<449.0,24.0>> -> L<<449.0,24.0>--<449.0,8.0>>

	* Wcircumflex (U+0174): L<<488.0,728.0>--<488.0,712.0>> -> L<<488.0,712.0>--<449.0,24.0>>

	* Wcircumflex (U+0174): L<<63.0,24.0>--<24.0,712.0>> -> L<<24.0,712.0>--<24.0,728.0>>

	* Wcircumflex (U+0174): L<<63.0,8.0>--<63.0,24.0>> -> L<<63.0,24.0>--<24.0,712.0>>

	* Wdieresis (U+1E84): L<<488.0,712.0>--<449.0,24.0>> -> L<<449.0,24.0>--<449.0,8.0>>

	* Wdieresis (U+1E84): L<<488.0,728.0>--<488.0,712.0>> -> L<<488.0,712.0>--<449.0,24.0>>

	* Wdieresis (U+1E84): L<<63.0,24.0>--<24.0,712.0>> -> L<<24.0,712.0>--<24.0,728.0>>

	* Wdieresis (U+1E84): L<<63.0,8.0>--<63.0,24.0>> -> L<<63.0,24.0>--<24.0,712.0>>

	* Wgrave (U+1E80): L<<488.0,712.0>--<449.0,24.0>> -> L<<449.0,24.0>--<449.0,8.0>>

	* Wgrave (U+1E80): L<<488.0,728.0>--<488.0,712.0>> -> L<<488.0,712.0>--<449.0,24.0>>

	* Wgrave (U+1E80): L<<63.0,24.0>--<24.0,712.0>> -> L<<24.0,712.0>--<24.0,728.0>>

	* Wgrave (U+1E80): L<<63.0,8.0>--<63.0,24.0>> -> L<<63.0,24.0>--<24.0,712.0>>

	* Y (U+0059): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* Y (U+0059): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* Yacute (U+00DD): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* Yacute (U+00DD): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* Ycircumflex (U+0176): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* Ycircumflex (U+0176): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* Ydieresis (U+0178): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* Ydieresis (U+0178): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* Ygrave (U+1EF2): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* Ygrave (U+1EF2): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* uni1EF4 (U+1EF4): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* uni1EF4 (U+1EF4): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* uni1EF6 (U+1EF6): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* uni1EF6 (U+1EF6): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* uni1EF8 (U+1EF8): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* uni1EF8 (U+1EF8): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* uni2116 (U+2116): L<<207.0,88.0>--<207.0,96.0>> -> L<<207.0,96.0>--<183.0,392.0>>

	* uni2116 (U+2116): L<<207.0,96.0>--<183.0,392.0>> -> L<<183.0,392.0>--<183.0,728.0>>

	* uni2116 (U+2116): L<<65.0,640.0>--<89.0,336.0>> -> L<<89.0,336.0>--<89.0,8.0>>

	* uni2116 (U+2116): L<<65.0,648.0>--<65.0,640.0>> -> L<<65.0,640.0>--<89.0,336.0>>

	* w (U+0077): L<<93.0,504.0>--<93.0,496.0>> -> L<<93.0,496.0>--<130.0,102.0>>

	* wacute (U+1E83): L<<93.0,504.0>--<93.0,496.0>> -> L<<93.0,496.0>--<130.0,102.0>>

	* wcircumflex (U+0175): L<<93.0,504.0>--<93.0,496.0>> -> L<<93.0,496.0>--<130.0,102.0>>

	* wdieresis (U+1E85): L<<93.0,504.0>--<93.0,496.0>> -> L<<93.0,496.0>--<130.0,102.0>> 

	* And wgrave (U+1E81): L<<93.0,504.0>--<93.0,496.0>> -> L<<93.0,496.0>--<130.0,102.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* newGlyph (U+00B5): L<<59.0,-208.0>--<58.0,513.0>> 

	* And uniFEDC (U+FEDC): L<<481.0,148.0>--<480.0,8.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[9] HasubiMono-Medium.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1080, but got 1035 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** Font is monospaced but 73 glyphs (8.45%) have a different width. You should check the widths of: ['uni27E8', 'uni27E9', 'guillemotleft', 'brokenbar.001', 'uni20BF', 'uni20B5', 'colonmonetary', 'dong', 'uni20B2', 'uni20B4', 'uni20AD', 'uni20BE', 'uni20BA', 'uni20BC', 'uni20A6', 'uni20B1', 'uni20BD', 'uni20A8', 'uni20B9', 'uni20AA', 'uni20B8', 'uni20AE', 'uni20A9', 'approxequal', 'logicalnot', 'emptyset', 'infinity', 'integral', 'uni2126', 'uni2206', 'product', 'summation', 'radical', 'partialdiff', 'uni00B5', 'perthousand', 'arrowup', 'uni2197', 'arrowright', 'uni2198', 'arrowdown', 'uni2199', 'arrowleft', 'uni2196', 'arrowboth', 'arrowupdn', 'uni25CF', 'circle', 'openbullet', 'uni25C6', 'uni25C7', 'lozenge', 'filledbox', 'uni25A1', 'uni25AA', 'uni25AB', 'triagup', 'uni25B6', 'triagdn', 'uni25C0', 'uni25B3', 'uni25B7', 'uni25BD', 'uni25C1', 'uni25B4', 'uni25B8', 'uni25BE', 'uni25C2', 'uni25B5', 'uni25B9', 'uni25BF', 'uni25C3', 'newGlyph.001'] [code: mono-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- ar.test.001

	- brokenbar.001

	- doublestrokear

	- eight.numr

	- eight.tf

	- five.numr

	- five.tf

	- four.numr

	- four.tf

	- gafsarkashabovear

	- gafsarkashcenterar

	- miniKehehar

	- newGlyph.001

	- nine.numr

	- nine.tf

	- one.numr

	- one.tf

	- seven.numr

	- seven.tf

	- six.numr

	- six.tf

	- three.numr

	- three.tf

	- threedotsdownabovear

	- threedotsdowncenterar

	- threedotsupbelowar

	- two.numr

	- two.tf

	- twodotsverticalabovear

	- twodotsverticalbelowar

	- uni00B5

	- uni03020300

	- uni03020300.case

	- uni03020301

	- uni03020301.case

	- uni03020303

	- uni03020303.case

	- uni03020309

	- uni03020309.case

	- uni03060300

	- uni03060300.case

	- uni03060301

	- uni03060301.case

	- uni03060303

	- uni03060303.case

	- uni03060309

	- uni03060309.case

	- zero.numr 

	- And zero.tf
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: ogonek	Contours detected: 0	Expected: 1

	- Glyph name: uni0312	Contours detected: 0	Expected: 1

	- Glyph name: uni0327	Contours detected: 0	Expected: 1

	- Glyph name: uni0328	Contours detected: 0	Expected: 1

	- Glyph name: uni0E3F	Contours detected: 5	Expected: 3

	- Glyph name: perthousand	Contours detected: 0	Expected: 6 or 7

	- Glyph name: colonmonetary	Contours detected: 0	Expected: 1 or 3

	- Glyph name: uni20A6	Contours detected: 0	Expected: 1, 3 or 5

	- Glyph name: uni20A8	Contours detected: 0	Expected: 3

	- Glyph name: uni20A9	Contours detected: 0	Expected: 1, 3, 4 or 7

	- Glyph name: uni20AA	Contours detected: 0	Expected: 2

	- Glyph name: dong	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni20AD	Contours detected: 0	Expected: 1

	- Glyph name: uni20AE	Contours detected: 0	Expected: 1

	- Glyph name: uni20B1	Contours detected: 0	Expected: 1, 2 or 4

	- Glyph name: uni20B2	Contours detected: 0	Expected: 1, 2 or 3

	- Glyph name: uni20B4	Contours detected: 0	Expected: 1 or 2

	- Glyph name: uni20B5	Contours detected: 0	Expected: 1 or 2

	- Glyph name: uni20B8	Contours detected: 0	Expected: 2

	- Glyph name: uni20B9	Contours detected: 0	Expected: 1

	- Glyph name: uni20BA	Contours detected: 0	Expected: 1

	- Glyph name: uni20BC	Contours detected: 0	Expected: 1

	- Glyph name: uni20BD	Contours detected: 0	Expected: 2

	- Glyph name: uni20BF	Contours detected: 0	Expected: 3

	- Glyph name: uni2126	Contours detected: 0	Expected: 1

	- Glyph name: arrowleft	Contours detected: 0	Expected: 1

	- Glyph name: arrowup	Contours detected: 0	Expected: 1

	- Glyph name: arrowright	Contours detected: 0	Expected: 1

	- Glyph name: arrowdown	Contours detected: 0	Expected: 1

	- Glyph name: arrowboth	Contours detected: 0	Expected: 1

	- Glyph name: arrowupdn	Contours detected: 0	Expected: 1

	- Glyph name: uni2196	Contours detected: 0	Expected: 1

	- Glyph name: uni2197	Contours detected: 0	Expected: 1

	- Glyph name: uni2198	Contours detected: 0	Expected: 1

	- Glyph name: uni2199	Contours detected: 0	Expected: 1

	- Glyph name: partialdiff	Contours detected: 0	Expected: 2

	- Glyph name: emptyset	Contours detected: 0	Expected: 3

	- Glyph name: uni2206	Contours detected: 0	Expected: 2

	- Glyph name: product	Contours detected: 0	Expected: 1

	- Glyph name: summation	Contours detected: 0	Expected: 1

	- Glyph name: radical	Contours detected: 0	Expected: 1

	- Glyph name: infinity	Contours detected: 0	Expected: 3

	- Glyph name: integral	Contours detected: 0	Expected: 1

	- Glyph name: approxequal	Contours detected: 0	Expected: 2

	- Glyph name: filledbox	Contours detected: 0	Expected: 1

	- Glyph name: uni25A1	Contours detected: 0	Expected: 2

	- Glyph name: uni25AA	Contours detected: 0	Expected: 1

	- Glyph name: uni25AB	Contours detected: 0	Expected: 2

	- Glyph name: triagup	Contours detected: 0	Expected: 1

	- Glyph name: uni25B3	Contours detected: 0	Expected: 2

	- Glyph name: uni25B6	Contours detected: 0	Expected: 1

	- Glyph name: uni25B7	Contours detected: 0	Expected: 2

	- Glyph name: triagdn	Contours detected: 0	Expected: 1

	- Glyph name: uni25BD	Contours detected: 0	Expected: 2

	- Glyph name: uni25C0	Contours detected: 0	Expected: 1

	- Glyph name: uni25C1	Contours detected: 0	Expected: 2

	- Glyph name: uni25C6	Contours detected: 0	Expected: 1

	- Glyph name: uni25C7	Contours detected: 0	Expected: 2

	- Glyph name: lozenge	Contours detected: 0	Expected: 2

	- Glyph name: circle	Contours detected: 0	Expected: 2

	- Glyph name: uni25CF	Contours detected: 0	Expected: 1

	- Glyph name: uni27E8	Contours detected: 0	Expected: 1

	- Glyph name: uni27E9	Contours detected: 0	Expected: 1

	- Glyph name: approxequal	Contours detected: 0	Expected: 2

	- Glyph name: arrowboth	Contours detected: 0	Expected: 1

	- Glyph name: arrowdown	Contours detected: 0	Expected: 1

	- Glyph name: arrowup	Contours detected: 0	Expected: 1

	- Glyph name: arrowupdn	Contours detected: 0	Expected: 1

	- Glyph name: circle	Contours detected: 0	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 0	Expected: 1 or 3

	- Glyph name: dong	Contours detected: 0	Expected: 3 or 4

	- Glyph name: emptyset	Contours detected: 0	Expected: 3

	- Glyph name: infinity	Contours detected: 0	Expected: 3

	- Glyph name: integral	Contours detected: 0	Expected: 1

	- Glyph name: lozenge	Contours detected: 0	Expected: 2

	- Glyph name: ogonek	Contours detected: 0	Expected: 1

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: partialdiff	Contours detected: 0	Expected: 2

	- Glyph name: perthousand	Contours detected: 0	Expected: 6 or 7

	- Glyph name: product	Contours detected: 0	Expected: 1

	- Glyph name: radical	Contours detected: 0	Expected: 1

	- Glyph name: summation	Contours detected: 0	Expected: 1

	- Glyph name: triagdn	Contours detected: 0	Expected: 1

	- Glyph name: triagup	Contours detected: 0	Expected: 1

	- Glyph name: uni0312	Contours detected: 0	Expected: 1

	- Glyph name: uni0327	Contours detected: 0	Expected: 1

	- Glyph name: uni0328	Contours detected: 0	Expected: 1

	- Glyph name: uni0E3F	Contours detected: 5	Expected: 3

	- Glyph name: uni20A6	Contours detected: 0	Expected: 1, 3 or 5

	- Glyph name: uni20A9	Contours detected: 0	Expected: 1, 3, 4 or 7

	- Glyph name: uni20AA	Contours detected: 0	Expected: 2

	- Glyph name: uni20AD	Contours detected: 0	Expected: 1

	- Glyph name: uni20AE	Contours detected: 0	Expected: 1

	- Glyph name: uni20B1	Contours detected: 0	Expected: 1, 2 or 4

	- Glyph name: uni20B2	Contours detected: 0	Expected: 1, 2 or 3

	- Glyph name: uni20B4	Contours detected: 0	Expected: 1 or 2

	- Glyph name: uni20B5	Contours detected: 0	Expected: 1 or 2

	- Glyph name: uni20B8	Contours detected: 0	Expected: 2

	- Glyph name: uni20B9	Contours detected: 0	Expected: 1

	- Glyph name: uni20BA	Contours detected: 0	Expected: 1

	- Glyph name: uni20BC	Contours detected: 0	Expected: 1

	- Glyph name: uni20BD	Contours detected: 0	Expected: 2

	- Glyph name: uni20BF	Contours detected: 0	Expected: 3

	- Glyph name: uni2126	Contours detected: 0	Expected: 1

	- Glyph name: uni2196	Contours detected: 0	Expected: 1

	- Glyph name: uni2197	Contours detected: 0	Expected: 1

	- Glyph name: uni2198	Contours detected: 0	Expected: 1

	- Glyph name: uni2199	Contours detected: 0	Expected: 1

	- Glyph name: uni2206	Contours detected: 0	Expected: 2

	- Glyph name: uni25A1	Contours detected: 0	Expected: 2

	- Glyph name: uni25AA	Contours detected: 0	Expected: 1

	- Glyph name: uni25AB	Contours detected: 0	Expected: 2

	- Glyph name: uni25B3	Contours detected: 0	Expected: 2

	- Glyph name: uni25B6	Contours detected: 0	Expected: 1

	- Glyph name: uni25B7	Contours detected: 0	Expected: 2

	- Glyph name: uni25BD	Contours detected: 0	Expected: 2

	- Glyph name: uni25C0	Contours detected: 0	Expected: 1

	- Glyph name: uni25C1	Contours detected: 0	Expected: 2

	- Glyph name: uni25C6	Contours detected: 0	Expected: 1

	- Glyph name: uni25C7	Contours detected: 0	Expected: 2

	- Glyph name: uni25CF	Contours detected: 0	Expected: 1

	- Glyph name: uni27E8	Contours detected: 0	Expected: 1 

	- And Glyph name: uni27E9	Contours detected: 0	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* W (U+0057): L<<488.0,712.0>--<449.0,24.0>> -> L<<449.0,24.0>--<449.0,8.0>>

	* W (U+0057): L<<488.0,728.0>--<488.0,712.0>> -> L<<488.0,712.0>--<449.0,24.0>>

	* W (U+0057): L<<63.0,24.0>--<24.0,712.0>> -> L<<24.0,712.0>--<24.0,728.0>>

	* W (U+0057): L<<63.0,8.0>--<63.0,24.0>> -> L<<63.0,24.0>--<24.0,712.0>>

	* Wacute (U+1E82): L<<488.0,712.0>--<449.0,24.0>> -> L<<449.0,24.0>--<449.0,8.0>>

	* Wacute (U+1E82): L<<488.0,728.0>--<488.0,712.0>> -> L<<488.0,712.0>--<449.0,24.0>>

	* Wacute (U+1E82): L<<63.0,24.0>--<24.0,712.0>> -> L<<24.0,712.0>--<24.0,728.0>>

	* Wacute (U+1E82): L<<63.0,8.0>--<63.0,24.0>> -> L<<63.0,24.0>--<24.0,712.0>>

	* Wcircumflex (U+0174): L<<488.0,712.0>--<449.0,24.0>> -> L<<449.0,24.0>--<449.0,8.0>>

	* Wcircumflex (U+0174): L<<488.0,728.0>--<488.0,712.0>> -> L<<488.0,712.0>--<449.0,24.0>>

	* Wcircumflex (U+0174): L<<63.0,24.0>--<24.0,712.0>> -> L<<24.0,712.0>--<24.0,728.0>>

	* Wcircumflex (U+0174): L<<63.0,8.0>--<63.0,24.0>> -> L<<63.0,24.0>--<24.0,712.0>>

	* Wdieresis (U+1E84): L<<488.0,712.0>--<449.0,24.0>> -> L<<449.0,24.0>--<449.0,8.0>>

	* Wdieresis (U+1E84): L<<488.0,728.0>--<488.0,712.0>> -> L<<488.0,712.0>--<449.0,24.0>>

	* Wdieresis (U+1E84): L<<63.0,24.0>--<24.0,712.0>> -> L<<24.0,712.0>--<24.0,728.0>>

	* Wdieresis (U+1E84): L<<63.0,8.0>--<63.0,24.0>> -> L<<63.0,24.0>--<24.0,712.0>>

	* Wgrave (U+1E80): L<<488.0,712.0>--<449.0,24.0>> -> L<<449.0,24.0>--<449.0,8.0>>

	* Wgrave (U+1E80): L<<488.0,728.0>--<488.0,712.0>> -> L<<488.0,712.0>--<449.0,24.0>>

	* Wgrave (U+1E80): L<<63.0,24.0>--<24.0,712.0>> -> L<<24.0,712.0>--<24.0,728.0>>

	* Wgrave (U+1E80): L<<63.0,8.0>--<63.0,24.0>> -> L<<63.0,24.0>--<24.0,712.0>>

	* Y (U+0059): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* Y (U+0059): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* Yacute (U+00DD): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* Yacute (U+00DD): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* Ycircumflex (U+0176): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* Ycircumflex (U+0176): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* Ydieresis (U+0178): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* Ydieresis (U+0178): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* Ygrave (U+1EF2): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* Ygrave (U+1EF2): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* backslash (U+005C): L<<148.0,697.0>--<395.0,-40.0>> -> L<<395.0,-40.0>--<441.0,-207.0>>

	* backslash (U+005C): L<<364.0,-201.0>--<117.0,536.0>> -> L<<117.0,536.0>--<71.0,703.0>>

	* uni1EF4 (U+1EF4): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* uni1EF4 (U+1EF4): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* uni1EF6 (U+1EF6): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* uni1EF6 (U+1EF6): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* uni1EF8 (U+1EF8): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* uni1EF8 (U+1EF8): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* uni2116 (U+2116): L<<207.0,88.0>--<207.0,96.0>> -> L<<207.0,96.0>--<183.0,392.0>>

	* uni2116 (U+2116): L<<207.0,96.0>--<183.0,392.0>> -> L<<183.0,392.0>--<183.0,728.0>>

	* uni2116 (U+2116): L<<65.0,640.0>--<89.0,336.0>> -> L<<89.0,336.0>--<89.0,8.0>>

	* uni2116 (U+2116): L<<65.0,648.0>--<65.0,640.0>> -> L<<65.0,640.0>--<89.0,336.0>>

	* w (U+0077): L<<364.0,97.0>--<403.0,459.0>> -> L<<403.0,459.0>--<416.0,537.0>>

	* wacute (U+1E83): L<<364.0,97.0>--<403.0,459.0>> -> L<<403.0,459.0>--<416.0,537.0>>

	* wcircumflex (U+0175): L<<364.0,97.0>--<403.0,459.0>> -> L<<403.0,459.0>--<416.0,537.0>>

	* wdieresis (U+1E85): L<<364.0,97.0>--<403.0,459.0>> -> L<<403.0,459.0>--<416.0,537.0>> 

	* And wgrave (U+1E81): L<<364.0,97.0>--<403.0,459.0>> -> L<<403.0,459.0>--<416.0,537.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* newGlyph (U+00B5): L<<59.0,-208.0>--<58.0,513.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[9] HasubiMono-SemiBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1080, but got 1035 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** Font is monospaced but 73 glyphs (8.45%) have a different width. You should check the widths of: ['uni27E8', 'uni27E9', 'guillemotleft', 'brokenbar.001', 'uni20BF', 'uni20B5', 'colonmonetary', 'dong', 'uni20B2', 'uni20B4', 'uni20AD', 'uni20BE', 'uni20BA', 'uni20BC', 'uni20A6', 'uni20B1', 'uni20BD', 'uni20A8', 'uni20B9', 'uni20AA', 'uni20B8', 'uni20AE', 'uni20A9', 'approxequal', 'logicalnot', 'emptyset', 'infinity', 'integral', 'uni2126', 'uni2206', 'product', 'summation', 'radical', 'partialdiff', 'uni00B5', 'perthousand', 'arrowup', 'uni2197', 'arrowright', 'uni2198', 'arrowdown', 'uni2199', 'arrowleft', 'uni2196', 'arrowboth', 'arrowupdn', 'uni25CF', 'circle', 'openbullet', 'uni25C6', 'uni25C7', 'lozenge', 'filledbox', 'uni25A1', 'uni25AA', 'uni25AB', 'triagup', 'uni25B6', 'triagdn', 'uni25C0', 'uni25B3', 'uni25B7', 'uni25BD', 'uni25C1', 'uni25B4', 'uni25B8', 'uni25BE', 'uni25C2', 'uni25B5', 'uni25B9', 'uni25BF', 'uni25C3', 'newGlyph.001'] [code: mono-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- ar.test.001

	- brokenbar.001

	- doublestrokear

	- eight.numr

	- eight.tf

	- five.numr

	- five.tf

	- four.numr

	- four.tf

	- gafsarkashabovear

	- gafsarkashcenterar

	- miniKehehar

	- newGlyph.001

	- nine.numr

	- nine.tf

	- one.numr

	- one.tf

	- seven.numr

	- seven.tf

	- six.numr

	- six.tf

	- three.numr

	- three.tf

	- threedotsdownabovear

	- threedotsdowncenterar

	- threedotsupbelowar

	- two.numr

	- two.tf

	- twodotsverticalabovear

	- twodotsverticalbelowar

	- uni00B5

	- uni03020300

	- uni03020300.case

	- uni03020301

	- uni03020301.case

	- uni03020303

	- uni03020303.case

	- uni03020309

	- uni03020309.case

	- uni03060300

	- uni03060300.case

	- uni03060301

	- uni03060301.case

	- uni03060303

	- uni03060303.case

	- uni03060309

	- uni03060309.case

	- zero.numr 

	- And zero.tf
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: ogonek	Contours detected: 0	Expected: 1

	- Glyph name: uni0312	Contours detected: 0	Expected: 1

	- Glyph name: uni0327	Contours detected: 0	Expected: 1

	- Glyph name: uni0328	Contours detected: 0	Expected: 1

	- Glyph name: uni0E3F	Contours detected: 5	Expected: 3

	- Glyph name: perthousand	Contours detected: 0	Expected: 6 or 7

	- Glyph name: colonmonetary	Contours detected: 0	Expected: 1 or 3

	- Glyph name: uni20A6	Contours detected: 0	Expected: 1, 3 or 5

	- Glyph name: uni20A8	Contours detected: 0	Expected: 3

	- Glyph name: uni20A9	Contours detected: 0	Expected: 1, 3, 4 or 7

	- Glyph name: uni20AA	Contours detected: 0	Expected: 2

	- Glyph name: dong	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni20AD	Contours detected: 0	Expected: 1

	- Glyph name: uni20AE	Contours detected: 0	Expected: 1

	- Glyph name: uni20B1	Contours detected: 0	Expected: 1, 2 or 4

	- Glyph name: uni20B2	Contours detected: 0	Expected: 1, 2 or 3

	- Glyph name: uni20B4	Contours detected: 0	Expected: 1 or 2

	- Glyph name: uni20B5	Contours detected: 0	Expected: 1 or 2

	- Glyph name: uni20B8	Contours detected: 0	Expected: 2

	- Glyph name: uni20B9	Contours detected: 0	Expected: 1

	- Glyph name: uni20BA	Contours detected: 0	Expected: 1

	- Glyph name: uni20BC	Contours detected: 0	Expected: 1

	- Glyph name: uni20BD	Contours detected: 0	Expected: 2

	- Glyph name: uni20BF	Contours detected: 0	Expected: 3

	- Glyph name: uni2126	Contours detected: 0	Expected: 1

	- Glyph name: arrowleft	Contours detected: 0	Expected: 1

	- Glyph name: arrowup	Contours detected: 0	Expected: 1

	- Glyph name: arrowright	Contours detected: 0	Expected: 1

	- Glyph name: arrowdown	Contours detected: 0	Expected: 1

	- Glyph name: arrowboth	Contours detected: 0	Expected: 1

	- Glyph name: arrowupdn	Contours detected: 0	Expected: 1

	- Glyph name: uni2196	Contours detected: 0	Expected: 1

	- Glyph name: uni2197	Contours detected: 0	Expected: 1

	- Glyph name: uni2198	Contours detected: 0	Expected: 1

	- Glyph name: uni2199	Contours detected: 0	Expected: 1

	- Glyph name: partialdiff	Contours detected: 0	Expected: 2

	- Glyph name: emptyset	Contours detected: 0	Expected: 3

	- Glyph name: uni2206	Contours detected: 0	Expected: 2

	- Glyph name: product	Contours detected: 0	Expected: 1

	- Glyph name: summation	Contours detected: 0	Expected: 1

	- Glyph name: radical	Contours detected: 0	Expected: 1

	- Glyph name: infinity	Contours detected: 0	Expected: 3

	- Glyph name: integral	Contours detected: 0	Expected: 1

	- Glyph name: approxequal	Contours detected: 0	Expected: 2

	- Glyph name: filledbox	Contours detected: 0	Expected: 1

	- Glyph name: uni25A1	Contours detected: 0	Expected: 2

	- Glyph name: uni25AA	Contours detected: 0	Expected: 1

	- Glyph name: uni25AB	Contours detected: 0	Expected: 2

	- Glyph name: triagup	Contours detected: 0	Expected: 1

	- Glyph name: uni25B3	Contours detected: 0	Expected: 2

	- Glyph name: uni25B6	Contours detected: 0	Expected: 1

	- Glyph name: uni25B7	Contours detected: 0	Expected: 2

	- Glyph name: triagdn	Contours detected: 0	Expected: 1

	- Glyph name: uni25BD	Contours detected: 0	Expected: 2

	- Glyph name: uni25C0	Contours detected: 0	Expected: 1

	- Glyph name: uni25C1	Contours detected: 0	Expected: 2

	- Glyph name: uni25C6	Contours detected: 0	Expected: 1

	- Glyph name: uni25C7	Contours detected: 0	Expected: 2

	- Glyph name: lozenge	Contours detected: 0	Expected: 2

	- Glyph name: circle	Contours detected: 0	Expected: 2

	- Glyph name: uni25CF	Contours detected: 0	Expected: 1

	- Glyph name: uni27E8	Contours detected: 0	Expected: 1

	- Glyph name: uni27E9	Contours detected: 0	Expected: 1

	- Glyph name: approxequal	Contours detected: 0	Expected: 2

	- Glyph name: arrowboth	Contours detected: 0	Expected: 1

	- Glyph name: arrowdown	Contours detected: 0	Expected: 1

	- Glyph name: arrowup	Contours detected: 0	Expected: 1

	- Glyph name: arrowupdn	Contours detected: 0	Expected: 1

	- Glyph name: circle	Contours detected: 0	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 0	Expected: 1 or 3

	- Glyph name: dong	Contours detected: 0	Expected: 3 or 4

	- Glyph name: emptyset	Contours detected: 0	Expected: 3

	- Glyph name: infinity	Contours detected: 0	Expected: 3

	- Glyph name: integral	Contours detected: 0	Expected: 1

	- Glyph name: lozenge	Contours detected: 0	Expected: 2

	- Glyph name: ogonek	Contours detected: 0	Expected: 1

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: partialdiff	Contours detected: 0	Expected: 2

	- Glyph name: perthousand	Contours detected: 0	Expected: 6 or 7

	- Glyph name: product	Contours detected: 0	Expected: 1

	- Glyph name: radical	Contours detected: 0	Expected: 1

	- Glyph name: summation	Contours detected: 0	Expected: 1

	- Glyph name: triagdn	Contours detected: 0	Expected: 1

	- Glyph name: triagup	Contours detected: 0	Expected: 1

	- Glyph name: uni0312	Contours detected: 0	Expected: 1

	- Glyph name: uni0327	Contours detected: 0	Expected: 1

	- Glyph name: uni0328	Contours detected: 0	Expected: 1

	- Glyph name: uni0E3F	Contours detected: 5	Expected: 3

	- Glyph name: uni20A6	Contours detected: 0	Expected: 1, 3 or 5

	- Glyph name: uni20A9	Contours detected: 0	Expected: 1, 3, 4 or 7

	- Glyph name: uni20AA	Contours detected: 0	Expected: 2

	- Glyph name: uni20AD	Contours detected: 0	Expected: 1

	- Glyph name: uni20AE	Contours detected: 0	Expected: 1

	- Glyph name: uni20B1	Contours detected: 0	Expected: 1, 2 or 4

	- Glyph name: uni20B2	Contours detected: 0	Expected: 1, 2 or 3

	- Glyph name: uni20B4	Contours detected: 0	Expected: 1 or 2

	- Glyph name: uni20B5	Contours detected: 0	Expected: 1 or 2

	- Glyph name: uni20B8	Contours detected: 0	Expected: 2

	- Glyph name: uni20B9	Contours detected: 0	Expected: 1

	- Glyph name: uni20BA	Contours detected: 0	Expected: 1

	- Glyph name: uni20BC	Contours detected: 0	Expected: 1

	- Glyph name: uni20BD	Contours detected: 0	Expected: 2

	- Glyph name: uni20BF	Contours detected: 0	Expected: 3

	- Glyph name: uni2126	Contours detected: 0	Expected: 1

	- Glyph name: uni2196	Contours detected: 0	Expected: 1

	- Glyph name: uni2197	Contours detected: 0	Expected: 1

	- Glyph name: uni2198	Contours detected: 0	Expected: 1

	- Glyph name: uni2199	Contours detected: 0	Expected: 1

	- Glyph name: uni2206	Contours detected: 0	Expected: 2

	- Glyph name: uni25A1	Contours detected: 0	Expected: 2

	- Glyph name: uni25AA	Contours detected: 0	Expected: 1

	- Glyph name: uni25AB	Contours detected: 0	Expected: 2

	- Glyph name: uni25B3	Contours detected: 0	Expected: 2

	- Glyph name: uni25B6	Contours detected: 0	Expected: 1

	- Glyph name: uni25B7	Contours detected: 0	Expected: 2

	- Glyph name: uni25BD	Contours detected: 0	Expected: 2

	- Glyph name: uni25C0	Contours detected: 0	Expected: 1

	- Glyph name: uni25C1	Contours detected: 0	Expected: 2

	- Glyph name: uni25C6	Contours detected: 0	Expected: 1

	- Glyph name: uni25C7	Contours detected: 0	Expected: 2

	- Glyph name: uni25CF	Contours detected: 0	Expected: 1

	- Glyph name: uni27E8	Contours detected: 0	Expected: 1 

	- And Glyph name: uni27E9	Contours detected: 0	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* W (U+0057): L<<488.0,712.0>--<449.0,24.0>> -> L<<449.0,24.0>--<449.0,8.0>>

	* W (U+0057): L<<488.0,728.0>--<488.0,712.0>> -> L<<488.0,712.0>--<449.0,24.0>>

	* W (U+0057): L<<63.0,24.0>--<24.0,712.0>> -> L<<24.0,712.0>--<24.0,728.0>>

	* W (U+0057): L<<63.0,8.0>--<63.0,24.0>> -> L<<63.0,24.0>--<24.0,712.0>>

	* Wacute (U+1E82): L<<488.0,712.0>--<449.0,24.0>> -> L<<449.0,24.0>--<449.0,8.0>>

	* Wacute (U+1E82): L<<488.0,728.0>--<488.0,712.0>> -> L<<488.0,712.0>--<449.0,24.0>>

	* Wacute (U+1E82): L<<63.0,24.0>--<24.0,712.0>> -> L<<24.0,712.0>--<24.0,728.0>>

	* Wacute (U+1E82): L<<63.0,8.0>--<63.0,24.0>> -> L<<63.0,24.0>--<24.0,712.0>>

	* Wcircumflex (U+0174): L<<488.0,712.0>--<449.0,24.0>> -> L<<449.0,24.0>--<449.0,8.0>>

	* Wcircumflex (U+0174): L<<488.0,728.0>--<488.0,712.0>> -> L<<488.0,712.0>--<449.0,24.0>>

	* Wcircumflex (U+0174): L<<63.0,24.0>--<24.0,712.0>> -> L<<24.0,712.0>--<24.0,728.0>>

	* Wcircumflex (U+0174): L<<63.0,8.0>--<63.0,24.0>> -> L<<63.0,24.0>--<24.0,712.0>>

	* Wdieresis (U+1E84): L<<488.0,712.0>--<449.0,24.0>> -> L<<449.0,24.0>--<449.0,8.0>>

	* Wdieresis (U+1E84): L<<488.0,728.0>--<488.0,712.0>> -> L<<488.0,712.0>--<449.0,24.0>>

	* Wdieresis (U+1E84): L<<63.0,24.0>--<24.0,712.0>> -> L<<24.0,712.0>--<24.0,728.0>>

	* Wdieresis (U+1E84): L<<63.0,8.0>--<63.0,24.0>> -> L<<63.0,24.0>--<24.0,712.0>>

	* Wgrave (U+1E80): L<<488.0,712.0>--<449.0,24.0>> -> L<<449.0,24.0>--<449.0,8.0>>

	* Wgrave (U+1E80): L<<488.0,728.0>--<488.0,712.0>> -> L<<488.0,712.0>--<449.0,24.0>>

	* Wgrave (U+1E80): L<<63.0,24.0>--<24.0,712.0>> -> L<<24.0,712.0>--<24.0,728.0>>

	* Wgrave (U+1E80): L<<63.0,8.0>--<63.0,24.0>> -> L<<63.0,24.0>--<24.0,712.0>>

	* Y (U+0059): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* Y (U+0059): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* Yacute (U+00DD): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* Yacute (U+00DD): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* Ycircumflex (U+0176): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* Ycircumflex (U+0176): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* Ydieresis (U+0178): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* Ydieresis (U+0178): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* Ygrave (U+1EF2): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* Ygrave (U+1EF2): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* backslash (U+005C): L<<146.0,699.0>--<341.0,120.0>> -> L<<341.0,120.0>--<443.0,-205.0>>

	* backslash (U+005C): L<<366.0,-203.0>--<171.0,376.0>> -> L<<171.0,376.0>--<69.0,701.0>>

	* uni1EF4 (U+1EF4): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* uni1EF4 (U+1EF4): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* uni1EF6 (U+1EF6): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* uni1EF6 (U+1EF6): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* uni1EF8 (U+1EF8): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* uni1EF8 (U+1EF8): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* uni2116 (U+2116): L<<207.0,88.0>--<207.0,96.0>> -> L<<207.0,96.0>--<183.0,392.0>>

	* uni2116 (U+2116): L<<207.0,96.0>--<183.0,392.0>> -> L<<183.0,392.0>--<183.0,728.0>>

	* uni2116 (U+2116): L<<65.0,640.0>--<89.0,336.0>> -> L<<89.0,336.0>--<89.0,8.0>>

	* uni2116 (U+2116): L<<65.0,648.0>--<65.0,640.0>> -> L<<65.0,640.0>--<89.0,336.0>>

	* w (U+0077): L<<101.0,525.0>--<128.0,239.0>> -> L<<128.0,239.0>--<151.0,98.0>>

	* w (U+0077): L<<365.0,98.0>--<398.0,381.0>> -> L<<398.0,381.0>--<416.0,530.0>>

	* wacute (U+1E83): L<<101.0,525.0>--<128.0,239.0>> -> L<<128.0,239.0>--<151.0,98.0>>

	* wacute (U+1E83): L<<365.0,98.0>--<398.0,381.0>> -> L<<398.0,381.0>--<416.0,530.0>>

	* wcircumflex (U+0175): L<<101.0,525.0>--<128.0,239.0>> -> L<<128.0,239.0>--<151.0,98.0>>

	* wcircumflex (U+0175): L<<365.0,98.0>--<398.0,381.0>> -> L<<398.0,381.0>--<416.0,530.0>>

	* wdieresis (U+1E85): L<<101.0,525.0>--<128.0,239.0>> -> L<<128.0,239.0>--<151.0,98.0>>

	* wdieresis (U+1E85): L<<365.0,98.0>--<398.0,381.0>> -> L<<398.0,381.0>--<416.0,530.0>>

	* wgrave (U+1E81): L<<101.0,525.0>--<128.0,239.0>> -> L<<128.0,239.0>--<151.0,98.0>>

	* wgrave (U+1E81): L<<365.0,98.0>--<398.0,381.0>> -> L<<398.0,381.0>--<416.0,530.0>>

	* x (U+0078): L<<102.0,91.0>--<97.0,99.0>> -> L<<97.0,99.0>--<43.0,187.0>> 

	* And x (U+0078): L<<398.0,444.0>--<403.0,436.0>> -> L<<403.0,436.0>--<458.0,345.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* newGlyph (U+00B5): L<<59.0,-208.0>--<58.0,513.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[9] HasubiMono-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1080, but got 1035 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** Font is monospaced but 1 glyphs (0.12%) have a different width. You should check the widths of: ['logicalnot'] [code: mono-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- ar.test.001

	- brokenbar.001

	- doublestrokear

	- eight.numr

	- eight.tf

	- five.numr

	- five.tf

	- four.numr

	- four.tf

	- gafsarkashabovear

	- gafsarkashcenterar

	- miniKehehar

	- newGlyph.001

	- nine.numr

	- nine.tf

	- one.numr

	- one.tf

	- seven.numr

	- seven.tf

	- six.numr

	- six.tf

	- three.numr

	- three.tf

	- threedotsdownabovear

	- threedotsdowncenterar

	- threedotsupbelowar

	- two.numr

	- two.tf

	- twodotsverticalabovear

	- twodotsverticalbelowar

	- uni00B5

	- uni03020300

	- uni03020300.case

	- uni03020301

	- uni03020301.case

	- uni03020303

	- uni03020303.case

	- uni03020309

	- uni03020309.case

	- uni03060300

	- uni03060300.case

	- uni03060301

	- uni03060301.case

	- uni03060303

	- uni03060303.case

	- uni03060309

	- uni03060309.case

	- zero.numr 

	- And zero.tf
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: ogonek	Contours detected: 0	Expected: 1

	- Glyph name: uni0312	Contours detected: 0	Expected: 1

	- Glyph name: uni0327	Contours detected: 0	Expected: 1

	- Glyph name: uni0328	Contours detected: 0	Expected: 1

	- Glyph name: uni0E3F	Contours detected: 5	Expected: 3

	- Glyph name: perthousand	Contours detected: 0	Expected: 6 or 7

	- Glyph name: colonmonetary	Contours detected: 0	Expected: 1 or 3

	- Glyph name: uni20A6	Contours detected: 0	Expected: 1, 3 or 5

	- Glyph name: uni20A8	Contours detected: 0	Expected: 3

	- Glyph name: uni20A9	Contours detected: 0	Expected: 1, 3, 4 or 7

	- Glyph name: uni20AA	Contours detected: 0	Expected: 2

	- Glyph name: dong	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni20AD	Contours detected: 0	Expected: 1

	- Glyph name: uni20AE	Contours detected: 0	Expected: 1

	- Glyph name: uni20B1	Contours detected: 0	Expected: 1, 2 or 4

	- Glyph name: uni20B2	Contours detected: 0	Expected: 1, 2 or 3

	- Glyph name: uni20B4	Contours detected: 0	Expected: 1 or 2

	- Glyph name: uni20B5	Contours detected: 0	Expected: 1 or 2

	- Glyph name: uni20B8	Contours detected: 0	Expected: 2

	- Glyph name: uni20B9	Contours detected: 0	Expected: 1

	- Glyph name: uni20BA	Contours detected: 0	Expected: 1

	- Glyph name: uni20BC	Contours detected: 0	Expected: 1

	- Glyph name: uni20BD	Contours detected: 0	Expected: 2

	- Glyph name: uni20BF	Contours detected: 0	Expected: 3

	- Glyph name: uni2126	Contours detected: 0	Expected: 1

	- Glyph name: arrowleft	Contours detected: 0	Expected: 1

	- Glyph name: arrowup	Contours detected: 0	Expected: 1

	- Glyph name: arrowright	Contours detected: 0	Expected: 1

	- Glyph name: arrowdown	Contours detected: 0	Expected: 1

	- Glyph name: arrowboth	Contours detected: 0	Expected: 1

	- Glyph name: arrowupdn	Contours detected: 0	Expected: 1

	- Glyph name: uni2196	Contours detected: 0	Expected: 1

	- Glyph name: uni2197	Contours detected: 0	Expected: 1

	- Glyph name: uni2198	Contours detected: 0	Expected: 1

	- Glyph name: uni2199	Contours detected: 0	Expected: 1

	- Glyph name: partialdiff	Contours detected: 0	Expected: 2

	- Glyph name: emptyset	Contours detected: 0	Expected: 3

	- Glyph name: uni2206	Contours detected: 0	Expected: 2

	- Glyph name: product	Contours detected: 0	Expected: 1

	- Glyph name: summation	Contours detected: 0	Expected: 1

	- Glyph name: radical	Contours detected: 0	Expected: 1

	- Glyph name: infinity	Contours detected: 0	Expected: 3

	- Glyph name: integral	Contours detected: 0	Expected: 1

	- Glyph name: approxequal	Contours detected: 0	Expected: 2

	- Glyph name: filledbox	Contours detected: 0	Expected: 1

	- Glyph name: uni25A1	Contours detected: 0	Expected: 2

	- Glyph name: uni25AA	Contours detected: 0	Expected: 1

	- Glyph name: uni25AB	Contours detected: 0	Expected: 2

	- Glyph name: triagup	Contours detected: 0	Expected: 1

	- Glyph name: uni25B3	Contours detected: 0	Expected: 2

	- Glyph name: uni25B6	Contours detected: 0	Expected: 1

	- Glyph name: uni25B7	Contours detected: 0	Expected: 2

	- Glyph name: triagdn	Contours detected: 0	Expected: 1

	- Glyph name: uni25BD	Contours detected: 0	Expected: 2

	- Glyph name: uni25C0	Contours detected: 0	Expected: 1

	- Glyph name: uni25C1	Contours detected: 0	Expected: 2

	- Glyph name: uni25C6	Contours detected: 0	Expected: 1

	- Glyph name: uni25C7	Contours detected: 0	Expected: 2

	- Glyph name: lozenge	Contours detected: 0	Expected: 2

	- Glyph name: circle	Contours detected: 0	Expected: 2

	- Glyph name: uni25CF	Contours detected: 0	Expected: 1

	- Glyph name: uni27E8	Contours detected: 0	Expected: 1

	- Glyph name: uni27E9	Contours detected: 0	Expected: 1

	- Glyph name: approxequal	Contours detected: 0	Expected: 2

	- Glyph name: arrowboth	Contours detected: 0	Expected: 1

	- Glyph name: arrowdown	Contours detected: 0	Expected: 1

	- Glyph name: arrowup	Contours detected: 0	Expected: 1

	- Glyph name: arrowupdn	Contours detected: 0	Expected: 1

	- Glyph name: circle	Contours detected: 0	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 0	Expected: 1 or 3

	- Glyph name: dong	Contours detected: 0	Expected: 3 or 4

	- Glyph name: emptyset	Contours detected: 0	Expected: 3

	- Glyph name: infinity	Contours detected: 0	Expected: 3

	- Glyph name: integral	Contours detected: 0	Expected: 1

	- Glyph name: lozenge	Contours detected: 0	Expected: 2

	- Glyph name: ogonek	Contours detected: 0	Expected: 1

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: partialdiff	Contours detected: 0	Expected: 2

	- Glyph name: perthousand	Contours detected: 0	Expected: 6 or 7

	- Glyph name: product	Contours detected: 0	Expected: 1

	- Glyph name: radical	Contours detected: 0	Expected: 1

	- Glyph name: summation	Contours detected: 0	Expected: 1

	- Glyph name: triagdn	Contours detected: 0	Expected: 1

	- Glyph name: triagup	Contours detected: 0	Expected: 1

	- Glyph name: uni0312	Contours detected: 0	Expected: 1

	- Glyph name: uni0327	Contours detected: 0	Expected: 1

	- Glyph name: uni0328	Contours detected: 0	Expected: 1

	- Glyph name: uni0E3F	Contours detected: 5	Expected: 3

	- Glyph name: uni20A6	Contours detected: 0	Expected: 1, 3 or 5

	- Glyph name: uni20A9	Contours detected: 0	Expected: 1, 3, 4 or 7

	- Glyph name: uni20AA	Contours detected: 0	Expected: 2

	- Glyph name: uni20AD	Contours detected: 0	Expected: 1

	- Glyph name: uni20AE	Contours detected: 0	Expected: 1

	- Glyph name: uni20B1	Contours detected: 0	Expected: 1, 2 or 4

	- Glyph name: uni20B2	Contours detected: 0	Expected: 1, 2 or 3

	- Glyph name: uni20B4	Contours detected: 0	Expected: 1 or 2

	- Glyph name: uni20B5	Contours detected: 0	Expected: 1 or 2

	- Glyph name: uni20B8	Contours detected: 0	Expected: 2

	- Glyph name: uni20B9	Contours detected: 0	Expected: 1

	- Glyph name: uni20BA	Contours detected: 0	Expected: 1

	- Glyph name: uni20BC	Contours detected: 0	Expected: 1

	- Glyph name: uni20BD	Contours detected: 0	Expected: 2

	- Glyph name: uni20BF	Contours detected: 0	Expected: 3

	- Glyph name: uni2126	Contours detected: 0	Expected: 1

	- Glyph name: uni2196	Contours detected: 0	Expected: 1

	- Glyph name: uni2197	Contours detected: 0	Expected: 1

	- Glyph name: uni2198	Contours detected: 0	Expected: 1

	- Glyph name: uni2199	Contours detected: 0	Expected: 1

	- Glyph name: uni2206	Contours detected: 0	Expected: 2

	- Glyph name: uni25A1	Contours detected: 0	Expected: 2

	- Glyph name: uni25AA	Contours detected: 0	Expected: 1

	- Glyph name: uni25AB	Contours detected: 0	Expected: 2

	- Glyph name: uni25B3	Contours detected: 0	Expected: 2

	- Glyph name: uni25B6	Contours detected: 0	Expected: 1

	- Glyph name: uni25B7	Contours detected: 0	Expected: 2

	- Glyph name: uni25BD	Contours detected: 0	Expected: 2

	- Glyph name: uni25C0	Contours detected: 0	Expected: 1

	- Glyph name: uni25C1	Contours detected: 0	Expected: 2

	- Glyph name: uni25C6	Contours detected: 0	Expected: 1

	- Glyph name: uni25C7	Contours detected: 0	Expected: 2

	- Glyph name: uni25CF	Contours detected: 0	Expected: 1

	- Glyph name: uni27E8	Contours detected: 0	Expected: 1 

	- And Glyph name: uni27E9	Contours detected: 0	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* W (U+0057): L<<488.0,712.0>--<449.0,24.0>> -> L<<449.0,24.0>--<449.0,8.0>>

	* W (U+0057): L<<488.0,728.0>--<488.0,712.0>> -> L<<488.0,712.0>--<449.0,24.0>>

	* W (U+0057): L<<63.0,24.0>--<24.0,712.0>> -> L<<24.0,712.0>--<24.0,728.0>>

	* W (U+0057): L<<63.0,8.0>--<63.0,24.0>> -> L<<63.0,24.0>--<24.0,712.0>>

	* Wacute (U+1E82): L<<488.0,712.0>--<449.0,24.0>> -> L<<449.0,24.0>--<449.0,8.0>>

	* Wacute (U+1E82): L<<488.0,728.0>--<488.0,712.0>> -> L<<488.0,712.0>--<449.0,24.0>>

	* Wacute (U+1E82): L<<63.0,24.0>--<24.0,712.0>> -> L<<24.0,712.0>--<24.0,728.0>>

	* Wacute (U+1E82): L<<63.0,8.0>--<63.0,24.0>> -> L<<63.0,24.0>--<24.0,712.0>>

	* Wcircumflex (U+0174): L<<488.0,712.0>--<449.0,24.0>> -> L<<449.0,24.0>--<449.0,8.0>>

	* Wcircumflex (U+0174): L<<488.0,728.0>--<488.0,712.0>> -> L<<488.0,712.0>--<449.0,24.0>>

	* Wcircumflex (U+0174): L<<63.0,24.0>--<24.0,712.0>> -> L<<24.0,712.0>--<24.0,728.0>>

	* Wcircumflex (U+0174): L<<63.0,8.0>--<63.0,24.0>> -> L<<63.0,24.0>--<24.0,712.0>>

	* Wdieresis (U+1E84): L<<488.0,712.0>--<449.0,24.0>> -> L<<449.0,24.0>--<449.0,8.0>>

	* Wdieresis (U+1E84): L<<488.0,728.0>--<488.0,712.0>> -> L<<488.0,712.0>--<449.0,24.0>>

	* Wdieresis (U+1E84): L<<63.0,24.0>--<24.0,712.0>> -> L<<24.0,712.0>--<24.0,728.0>>

	* Wdieresis (U+1E84): L<<63.0,8.0>--<63.0,24.0>> -> L<<63.0,24.0>--<24.0,712.0>>

	* Wgrave (U+1E80): L<<488.0,712.0>--<449.0,24.0>> -> L<<449.0,24.0>--<449.0,8.0>>

	* Wgrave (U+1E80): L<<488.0,728.0>--<488.0,712.0>> -> L<<488.0,712.0>--<449.0,24.0>>

	* Wgrave (U+1E80): L<<63.0,24.0>--<24.0,712.0>> -> L<<24.0,712.0>--<24.0,728.0>>

	* Wgrave (U+1E80): L<<63.0,8.0>--<63.0,24.0>> -> L<<63.0,24.0>--<24.0,712.0>>

	* Y (U+0059): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* Y (U+0059): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* Yacute (U+00DD): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* Yacute (U+00DD): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* Ycircumflex (U+0176): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* Ycircumflex (U+0176): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* Ydieresis (U+0178): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* Ydieresis (U+0178): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* Ygrave (U+1EF2): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* Ygrave (U+1EF2): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* uni1EF4 (U+1EF4): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* uni1EF4 (U+1EF4): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* uni1EF6 (U+1EF6): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* uni1EF6 (U+1EF6): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* uni1EF8 (U+1EF8): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* uni1EF8 (U+1EF8): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* uni2116 (U+2116): L<<207.0,88.0>--<207.0,96.0>> -> L<<207.0,96.0>--<183.0,392.0>>

	* uni2116 (U+2116): L<<207.0,96.0>--<183.0,392.0>> -> L<<183.0,392.0>--<183.0,728.0>>

	* uni2116 (U+2116): L<<65.0,640.0>--<89.0,336.0>> -> L<<89.0,336.0>--<89.0,8.0>> 

	* And uni2116 (U+2116): L<<65.0,648.0>--<65.0,640.0>> -> L<<65.0,640.0>--<89.0,336.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* newGlyph (U+00B5): L<<59.0,-208.0>--<58.0,513.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[9] HasubiMono-Bold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1080, but got 1035 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** Font is monospaced but 73 glyphs (8.45%) have a different width. You should check the widths of: ['uni27E8', 'uni27E9', 'guillemotleft', 'brokenbar.001', 'uni20BF', 'uni20B5', 'colonmonetary', 'dong', 'uni20B2', 'uni20B4', 'uni20AD', 'uni20BE', 'uni20BA', 'uni20BC', 'uni20A6', 'uni20B1', 'uni20BD', 'uni20A8', 'uni20B9', 'uni20AA', 'uni20B8', 'uni20AE', 'uni20A9', 'approxequal', 'logicalnot', 'emptyset', 'infinity', 'integral', 'uni2126', 'uni2206', 'product', 'summation', 'radical', 'partialdiff', 'uni00B5', 'perthousand', 'arrowup', 'uni2197', 'arrowright', 'uni2198', 'arrowdown', 'uni2199', 'arrowleft', 'uni2196', 'arrowboth', 'arrowupdn', 'uni25CF', 'circle', 'openbullet', 'uni25C6', 'uni25C7', 'lozenge', 'filledbox', 'uni25A1', 'uni25AA', 'uni25AB', 'triagup', 'uni25B6', 'triagdn', 'uni25C0', 'uni25B3', 'uni25B7', 'uni25BD', 'uni25C1', 'uni25B4', 'uni25B8', 'uni25BE', 'uni25C2', 'uni25B5', 'uni25B9', 'uni25BF', 'uni25C3', 'newGlyph.001'] [code: mono-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- ar.test.001

	- brokenbar.001

	- doublestrokear

	- eight.numr

	- eight.tf

	- five.numr

	- five.tf

	- four.numr

	- four.tf

	- gafsarkashabovear

	- gafsarkashcenterar

	- miniKehehar

	- newGlyph.001

	- nine.numr

	- nine.tf

	- one.numr

	- one.tf

	- seven.numr

	- seven.tf

	- six.numr

	- six.tf

	- three.numr

	- three.tf

	- threedotsdownabovear

	- threedotsdowncenterar

	- threedotsupbelowar

	- two.numr

	- two.tf

	- twodotsverticalabovear

	- twodotsverticalbelowar

	- uni00B5

	- uni03020300

	- uni03020300.case

	- uni03020301

	- uni03020301.case

	- uni03020303

	- uni03020303.case

	- uni03020309

	- uni03020309.case

	- uni03060300

	- uni03060300.case

	- uni03060301

	- uni03060301.case

	- uni03060303

	- uni03060303.case

	- uni03060309

	- uni03060309.case

	- zero.numr 

	- And zero.tf
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: ogonek	Contours detected: 0	Expected: 1

	- Glyph name: uni0312	Contours detected: 0	Expected: 1

	- Glyph name: uni0327	Contours detected: 0	Expected: 1

	- Glyph name: uni0328	Contours detected: 0	Expected: 1

	- Glyph name: uni0E3F	Contours detected: 5	Expected: 3

	- Glyph name: perthousand	Contours detected: 0	Expected: 6 or 7

	- Glyph name: colonmonetary	Contours detected: 0	Expected: 1 or 3

	- Glyph name: uni20A6	Contours detected: 0	Expected: 1, 3 or 5

	- Glyph name: uni20A8	Contours detected: 0	Expected: 3

	- Glyph name: uni20A9	Contours detected: 0	Expected: 1, 3, 4 or 7

	- Glyph name: uni20AA	Contours detected: 0	Expected: 2

	- Glyph name: dong	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni20AD	Contours detected: 0	Expected: 1

	- Glyph name: uni20AE	Contours detected: 0	Expected: 1

	- Glyph name: uni20B1	Contours detected: 0	Expected: 1, 2 or 4

	- Glyph name: uni20B2	Contours detected: 0	Expected: 1, 2 or 3

	- Glyph name: uni20B4	Contours detected: 0	Expected: 1 or 2

	- Glyph name: uni20B5	Contours detected: 0	Expected: 1 or 2

	- Glyph name: uni20B8	Contours detected: 0	Expected: 2

	- Glyph name: uni20B9	Contours detected: 0	Expected: 1

	- Glyph name: uni20BA	Contours detected: 0	Expected: 1

	- Glyph name: uni20BC	Contours detected: 0	Expected: 1

	- Glyph name: uni20BD	Contours detected: 0	Expected: 2

	- Glyph name: uni20BF	Contours detected: 0	Expected: 3

	- Glyph name: uni2126	Contours detected: 0	Expected: 1

	- Glyph name: arrowleft	Contours detected: 0	Expected: 1

	- Glyph name: arrowup	Contours detected: 0	Expected: 1

	- Glyph name: arrowright	Contours detected: 0	Expected: 1

	- Glyph name: arrowdown	Contours detected: 0	Expected: 1

	- Glyph name: arrowboth	Contours detected: 0	Expected: 1

	- Glyph name: arrowupdn	Contours detected: 0	Expected: 1

	- Glyph name: uni2196	Contours detected: 0	Expected: 1

	- Glyph name: uni2197	Contours detected: 0	Expected: 1

	- Glyph name: uni2198	Contours detected: 0	Expected: 1

	- Glyph name: uni2199	Contours detected: 0	Expected: 1

	- Glyph name: partialdiff	Contours detected: 0	Expected: 2

	- Glyph name: emptyset	Contours detected: 0	Expected: 3

	- Glyph name: uni2206	Contours detected: 0	Expected: 2

	- Glyph name: product	Contours detected: 0	Expected: 1

	- Glyph name: summation	Contours detected: 0	Expected: 1

	- Glyph name: radical	Contours detected: 0	Expected: 1

	- Glyph name: infinity	Contours detected: 0	Expected: 3

	- Glyph name: integral	Contours detected: 0	Expected: 1

	- Glyph name: approxequal	Contours detected: 0	Expected: 2

	- Glyph name: filledbox	Contours detected: 0	Expected: 1

	- Glyph name: uni25A1	Contours detected: 0	Expected: 2

	- Glyph name: uni25AA	Contours detected: 0	Expected: 1

	- Glyph name: uni25AB	Contours detected: 0	Expected: 2

	- Glyph name: triagup	Contours detected: 0	Expected: 1

	- Glyph name: uni25B3	Contours detected: 0	Expected: 2

	- Glyph name: uni25B6	Contours detected: 0	Expected: 1

	- Glyph name: uni25B7	Contours detected: 0	Expected: 2

	- Glyph name: triagdn	Contours detected: 0	Expected: 1

	- Glyph name: uni25BD	Contours detected: 0	Expected: 2

	- Glyph name: uni25C0	Contours detected: 0	Expected: 1

	- Glyph name: uni25C1	Contours detected: 0	Expected: 2

	- Glyph name: uni25C6	Contours detected: 0	Expected: 1

	- Glyph name: uni25C7	Contours detected: 0	Expected: 2

	- Glyph name: lozenge	Contours detected: 0	Expected: 2

	- Glyph name: circle	Contours detected: 0	Expected: 2

	- Glyph name: uni25CF	Contours detected: 0	Expected: 1

	- Glyph name: uni27E8	Contours detected: 0	Expected: 1

	- Glyph name: uni27E9	Contours detected: 0	Expected: 1

	- Glyph name: approxequal	Contours detected: 0	Expected: 2

	- Glyph name: arrowboth	Contours detected: 0	Expected: 1

	- Glyph name: arrowdown	Contours detected: 0	Expected: 1

	- Glyph name: arrowup	Contours detected: 0	Expected: 1

	- Glyph name: arrowupdn	Contours detected: 0	Expected: 1

	- Glyph name: circle	Contours detected: 0	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 0	Expected: 1 or 3

	- Glyph name: dong	Contours detected: 0	Expected: 3 or 4

	- Glyph name: emptyset	Contours detected: 0	Expected: 3

	- Glyph name: infinity	Contours detected: 0	Expected: 3

	- Glyph name: integral	Contours detected: 0	Expected: 1

	- Glyph name: lozenge	Contours detected: 0	Expected: 2

	- Glyph name: ogonek	Contours detected: 0	Expected: 1

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: partialdiff	Contours detected: 0	Expected: 2

	- Glyph name: perthousand	Contours detected: 0	Expected: 6 or 7

	- Glyph name: product	Contours detected: 0	Expected: 1

	- Glyph name: radical	Contours detected: 0	Expected: 1

	- Glyph name: summation	Contours detected: 0	Expected: 1

	- Glyph name: triagdn	Contours detected: 0	Expected: 1

	- Glyph name: triagup	Contours detected: 0	Expected: 1

	- Glyph name: uni0312	Contours detected: 0	Expected: 1

	- Glyph name: uni0327	Contours detected: 0	Expected: 1

	- Glyph name: uni0328	Contours detected: 0	Expected: 1

	- Glyph name: uni0E3F	Contours detected: 5	Expected: 3

	- Glyph name: uni20A6	Contours detected: 0	Expected: 1, 3 or 5

	- Glyph name: uni20A9	Contours detected: 0	Expected: 1, 3, 4 or 7

	- Glyph name: uni20AA	Contours detected: 0	Expected: 2

	- Glyph name: uni20AD	Contours detected: 0	Expected: 1

	- Glyph name: uni20AE	Contours detected: 0	Expected: 1

	- Glyph name: uni20B1	Contours detected: 0	Expected: 1, 2 or 4

	- Glyph name: uni20B2	Contours detected: 0	Expected: 1, 2 or 3

	- Glyph name: uni20B4	Contours detected: 0	Expected: 1 or 2

	- Glyph name: uni20B5	Contours detected: 0	Expected: 1 or 2

	- Glyph name: uni20B8	Contours detected: 0	Expected: 2

	- Glyph name: uni20B9	Contours detected: 0	Expected: 1

	- Glyph name: uni20BA	Contours detected: 0	Expected: 1

	- Glyph name: uni20BC	Contours detected: 0	Expected: 1

	- Glyph name: uni20BD	Contours detected: 0	Expected: 2

	- Glyph name: uni20BF	Contours detected: 0	Expected: 3

	- Glyph name: uni2126	Contours detected: 0	Expected: 1

	- Glyph name: uni2196	Contours detected: 0	Expected: 1

	- Glyph name: uni2197	Contours detected: 0	Expected: 1

	- Glyph name: uni2198	Contours detected: 0	Expected: 1

	- Glyph name: uni2199	Contours detected: 0	Expected: 1

	- Glyph name: uni2206	Contours detected: 0	Expected: 2

	- Glyph name: uni25A1	Contours detected: 0	Expected: 2

	- Glyph name: uni25AA	Contours detected: 0	Expected: 1

	- Glyph name: uni25AB	Contours detected: 0	Expected: 2

	- Glyph name: uni25B3	Contours detected: 0	Expected: 2

	- Glyph name: uni25B6	Contours detected: 0	Expected: 1

	- Glyph name: uni25B7	Contours detected: 0	Expected: 2

	- Glyph name: uni25BD	Contours detected: 0	Expected: 2

	- Glyph name: uni25C0	Contours detected: 0	Expected: 1

	- Glyph name: uni25C1	Contours detected: 0	Expected: 2

	- Glyph name: uni25C6	Contours detected: 0	Expected: 1

	- Glyph name: uni25C7	Contours detected: 0	Expected: 2

	- Glyph name: uni25CF	Contours detected: 0	Expected: 1

	- Glyph name: uni27E8	Contours detected: 0	Expected: 1 

	- And Glyph name: uni27E9	Contours detected: 0	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* W (U+0057): L<<488.0,712.0>--<449.0,24.0>> -> L<<449.0,24.0>--<449.0,8.0>>

	* W (U+0057): L<<488.0,728.0>--<488.0,712.0>> -> L<<488.0,712.0>--<449.0,24.0>>

	* W (U+0057): L<<63.0,24.0>--<24.0,712.0>> -> L<<24.0,712.0>--<24.0,728.0>>

	* W (U+0057): L<<63.0,8.0>--<63.0,24.0>> -> L<<63.0,24.0>--<24.0,712.0>>

	* Wacute (U+1E82): L<<488.0,712.0>--<449.0,24.0>> -> L<<449.0,24.0>--<449.0,8.0>>

	* Wacute (U+1E82): L<<488.0,728.0>--<488.0,712.0>> -> L<<488.0,712.0>--<449.0,24.0>>

	* Wacute (U+1E82): L<<63.0,24.0>--<24.0,712.0>> -> L<<24.0,712.0>--<24.0,728.0>>

	* Wacute (U+1E82): L<<63.0,8.0>--<63.0,24.0>> -> L<<63.0,24.0>--<24.0,712.0>>

	* Wcircumflex (U+0174): L<<488.0,712.0>--<449.0,24.0>> -> L<<449.0,24.0>--<449.0,8.0>>

	* Wcircumflex (U+0174): L<<488.0,728.0>--<488.0,712.0>> -> L<<488.0,712.0>--<449.0,24.0>>

	* Wcircumflex (U+0174): L<<63.0,24.0>--<24.0,712.0>> -> L<<24.0,712.0>--<24.0,728.0>>

	* Wcircumflex (U+0174): L<<63.0,8.0>--<63.0,24.0>> -> L<<63.0,24.0>--<24.0,712.0>>

	* Wdieresis (U+1E84): L<<488.0,712.0>--<449.0,24.0>> -> L<<449.0,24.0>--<449.0,8.0>>

	* Wdieresis (U+1E84): L<<488.0,728.0>--<488.0,712.0>> -> L<<488.0,712.0>--<449.0,24.0>>

	* Wdieresis (U+1E84): L<<63.0,24.0>--<24.0,712.0>> -> L<<24.0,712.0>--<24.0,728.0>>

	* Wdieresis (U+1E84): L<<63.0,8.0>--<63.0,24.0>> -> L<<63.0,24.0>--<24.0,712.0>>

	* Wgrave (U+1E80): L<<488.0,712.0>--<449.0,24.0>> -> L<<449.0,24.0>--<449.0,8.0>>

	* Wgrave (U+1E80): L<<488.0,728.0>--<488.0,712.0>> -> L<<488.0,712.0>--<449.0,24.0>>

	* Wgrave (U+1E80): L<<63.0,24.0>--<24.0,712.0>> -> L<<24.0,712.0>--<24.0,728.0>>

	* Wgrave (U+1E80): L<<63.0,8.0>--<63.0,24.0>> -> L<<63.0,24.0>--<24.0,712.0>>

	* Y (U+0059): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* Y (U+0059): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* Yacute (U+00DD): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* Yacute (U+00DD): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* Ycircumflex (U+0176): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* Ycircumflex (U+0176): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* Ydieresis (U+0178): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* Ydieresis (U+0178): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* Ygrave (U+1EF2): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* Ygrave (U+1EF2): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* backslash (U+005C): L<<145.0,700.0>--<288.0,280.0>> -> L<<288.0,280.0>--<444.0,-204.0>>

	* backslash (U+005C): L<<367.0,-204.0>--<224.0,216.0>> -> L<<224.0,216.0>--<68.0,700.0>>

	* uni1EF4 (U+1EF4): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* uni1EF4 (U+1EF4): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* uni1EF6 (U+1EF6): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* uni1EF6 (U+1EF6): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* uni1EF8 (U+1EF8): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* uni1EF8 (U+1EF8): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* uni2116 (U+2116): L<<207.0,88.0>--<207.0,96.0>> -> L<<207.0,96.0>--<183.0,392.0>>

	* uni2116 (U+2116): L<<207.0,96.0>--<183.0,392.0>> -> L<<183.0,392.0>--<183.0,728.0>>

	* uni2116 (U+2116): L<<65.0,640.0>--<89.0,336.0>> -> L<<89.0,336.0>--<89.0,8.0>>

	* uni2116 (U+2116): L<<65.0,648.0>--<65.0,640.0>> -> L<<65.0,640.0>--<89.0,336.0>>

	* w (U+0077): L<<365.0,99.0>--<394.0,304.0>> -> L<<394.0,304.0>--<417.0,523.0>>

	* w (U+0077): L<<99.0,519.0>--<119.0,310.0>> -> L<<119.0,310.0>--<145.0,99.0>>

	* wacute (U+1E83): L<<365.0,99.0>--<394.0,304.0>> -> L<<394.0,304.0>--<417.0,523.0>>

	* wacute (U+1E83): L<<99.0,519.0>--<119.0,310.0>> -> L<<119.0,310.0>--<145.0,99.0>>

	* wcircumflex (U+0175): L<<365.0,99.0>--<394.0,304.0>> -> L<<394.0,304.0>--<417.0,523.0>>

	* wcircumflex (U+0175): L<<99.0,519.0>--<119.0,310.0>> -> L<<119.0,310.0>--<145.0,99.0>>

	* wdieresis (U+1E85): L<<365.0,99.0>--<394.0,304.0>> -> L<<394.0,304.0>--<417.0,523.0>>

	* wdieresis (U+1E85): L<<99.0,519.0>--<119.0,310.0>> -> L<<119.0,310.0>--<145.0,99.0>>

	* wgrave (U+1E81): L<<365.0,99.0>--<394.0,304.0>> -> L<<394.0,304.0>--<417.0,523.0>>

	* wgrave (U+1E81): L<<99.0,519.0>--<119.0,310.0>> -> L<<119.0,310.0>--<145.0,99.0>> 

	* And x (U+0078): L<<374.0,394.0>--<378.0,386.0>> -> L<<378.0,386.0>--<459.0,254.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* newGlyph (U+00B5): L<<59.0,-208.0>--<58.0,513.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[10] HasubiMono-ExtraBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1080, but got 1035 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** Font is monospaced but 73 glyphs (8.45%) have a different width. You should check the widths of: ['uni27E8', 'uni27E9', 'guillemotleft', 'brokenbar.001', 'uni20BF', 'uni20B5', 'colonmonetary', 'dong', 'uni20B2', 'uni20B4', 'uni20AD', 'uni20BE', 'uni20BA', 'uni20BC', 'uni20A6', 'uni20B1', 'uni20BD', 'uni20A8', 'uni20B9', 'uni20AA', 'uni20B8', 'uni20AE', 'uni20A9', 'approxequal', 'logicalnot', 'emptyset', 'infinity', 'integral', 'uni2126', 'uni2206', 'product', 'summation', 'radical', 'partialdiff', 'uni00B5', 'perthousand', 'arrowup', 'uni2197', 'arrowright', 'uni2198', 'arrowdown', 'uni2199', 'arrowleft', 'uni2196', 'arrowboth', 'arrowupdn', 'uni25CF', 'circle', 'openbullet', 'uni25C6', 'uni25C7', 'lozenge', 'filledbox', 'uni25A1', 'uni25AA', 'uni25AB', 'triagup', 'uni25B6', 'triagdn', 'uni25C0', 'uni25B3', 'uni25B7', 'uni25BD', 'uni25C1', 'uni25B4', 'uni25B8', 'uni25BE', 'uni25C2', 'uni25B5', 'uni25B9', 'uni25BF', 'uni25C3', 'newGlyph.001'] [code: mono-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Hasubi Mono ExtraBold' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- ar.test.001

	- brokenbar.001

	- doublestrokear

	- eight.numr

	- eight.tf

	- five.numr

	- five.tf

	- four.numr

	- four.tf

	- gafsarkashabovear

	- gafsarkashcenterar

	- miniKehehar

	- newGlyph.001

	- nine.numr

	- nine.tf

	- one.numr

	- one.tf

	- seven.numr

	- seven.tf

	- six.numr

	- six.tf

	- three.numr

	- three.tf

	- threedotsdownabovear

	- threedotsdowncenterar

	- threedotsupbelowar

	- two.numr

	- two.tf

	- twodotsverticalabovear

	- twodotsverticalbelowar

	- uni00B5

	- uni03020300

	- uni03020300.case

	- uni03020301

	- uni03020301.case

	- uni03020303

	- uni03020303.case

	- uni03020309

	- uni03020309.case

	- uni03060300

	- uni03060300.case

	- uni03060301

	- uni03060301.case

	- uni03060303

	- uni03060303.case

	- uni03060309

	- uni03060309.case

	- zero.numr 

	- And zero.tf
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: ogonek	Contours detected: 0	Expected: 1

	- Glyph name: uni0312	Contours detected: 0	Expected: 1

	- Glyph name: uni0327	Contours detected: 0	Expected: 1

	- Glyph name: uni0328	Contours detected: 0	Expected: 1

	- Glyph name: uni0E3F	Contours detected: 5	Expected: 3

	- Glyph name: perthousand	Contours detected: 0	Expected: 6 or 7

	- Glyph name: colonmonetary	Contours detected: 0	Expected: 1 or 3

	- Glyph name: uni20A6	Contours detected: 0	Expected: 1, 3 or 5

	- Glyph name: uni20A8	Contours detected: 0	Expected: 3

	- Glyph name: uni20A9	Contours detected: 0	Expected: 1, 3, 4 or 7

	- Glyph name: uni20AA	Contours detected: 0	Expected: 2

	- Glyph name: dong	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni20AD	Contours detected: 0	Expected: 1

	- Glyph name: uni20AE	Contours detected: 0	Expected: 1

	- Glyph name: uni20B1	Contours detected: 0	Expected: 1, 2 or 4

	- Glyph name: uni20B2	Contours detected: 0	Expected: 1, 2 or 3

	- Glyph name: uni20B4	Contours detected: 0	Expected: 1 or 2

	- Glyph name: uni20B5	Contours detected: 0	Expected: 1 or 2

	- Glyph name: uni20B8	Contours detected: 0	Expected: 2

	- Glyph name: uni20B9	Contours detected: 0	Expected: 1

	- Glyph name: uni20BA	Contours detected: 0	Expected: 1

	- Glyph name: uni20BC	Contours detected: 0	Expected: 1

	- Glyph name: uni20BD	Contours detected: 0	Expected: 2

	- Glyph name: uni20BF	Contours detected: 0	Expected: 3

	- Glyph name: uni2126	Contours detected: 0	Expected: 1

	- Glyph name: arrowleft	Contours detected: 0	Expected: 1

	- Glyph name: arrowup	Contours detected: 0	Expected: 1

	- Glyph name: arrowright	Contours detected: 0	Expected: 1

	- Glyph name: arrowdown	Contours detected: 0	Expected: 1

	- Glyph name: arrowboth	Contours detected: 0	Expected: 1

	- Glyph name: arrowupdn	Contours detected: 0	Expected: 1

	- Glyph name: uni2196	Contours detected: 0	Expected: 1

	- Glyph name: uni2197	Contours detected: 0	Expected: 1

	- Glyph name: uni2198	Contours detected: 0	Expected: 1

	- Glyph name: uni2199	Contours detected: 0	Expected: 1

	- Glyph name: partialdiff	Contours detected: 0	Expected: 2

	- Glyph name: emptyset	Contours detected: 0	Expected: 3

	- Glyph name: uni2206	Contours detected: 0	Expected: 2

	- Glyph name: product	Contours detected: 0	Expected: 1

	- Glyph name: summation	Contours detected: 0	Expected: 1

	- Glyph name: radical	Contours detected: 0	Expected: 1

	- Glyph name: infinity	Contours detected: 0	Expected: 3

	- Glyph name: integral	Contours detected: 0	Expected: 1

	- Glyph name: approxequal	Contours detected: 0	Expected: 2

	- Glyph name: filledbox	Contours detected: 0	Expected: 1

	- Glyph name: uni25A1	Contours detected: 0	Expected: 2

	- Glyph name: uni25AA	Contours detected: 0	Expected: 1

	- Glyph name: uni25AB	Contours detected: 0	Expected: 2

	- Glyph name: triagup	Contours detected: 0	Expected: 1

	- Glyph name: uni25B3	Contours detected: 0	Expected: 2

	- Glyph name: uni25B6	Contours detected: 0	Expected: 1

	- Glyph name: uni25B7	Contours detected: 0	Expected: 2

	- Glyph name: triagdn	Contours detected: 0	Expected: 1

	- Glyph name: uni25BD	Contours detected: 0	Expected: 2

	- Glyph name: uni25C0	Contours detected: 0	Expected: 1

	- Glyph name: uni25C1	Contours detected: 0	Expected: 2

	- Glyph name: uni25C6	Contours detected: 0	Expected: 1

	- Glyph name: uni25C7	Contours detected: 0	Expected: 2

	- Glyph name: lozenge	Contours detected: 0	Expected: 2

	- Glyph name: circle	Contours detected: 0	Expected: 2

	- Glyph name: uni25CF	Contours detected: 0	Expected: 1

	- Glyph name: uni27E8	Contours detected: 0	Expected: 1

	- Glyph name: uni27E9	Contours detected: 0	Expected: 1

	- Glyph name: approxequal	Contours detected: 0	Expected: 2

	- Glyph name: arrowboth	Contours detected: 0	Expected: 1

	- Glyph name: arrowdown	Contours detected: 0	Expected: 1

	- Glyph name: arrowup	Contours detected: 0	Expected: 1

	- Glyph name: arrowupdn	Contours detected: 0	Expected: 1

	- Glyph name: circle	Contours detected: 0	Expected: 2

	- Glyph name: colonmonetary	Contours detected: 0	Expected: 1 or 3

	- Glyph name: dong	Contours detected: 0	Expected: 3 or 4

	- Glyph name: emptyset	Contours detected: 0	Expected: 3

	- Glyph name: infinity	Contours detected: 0	Expected: 3

	- Glyph name: integral	Contours detected: 0	Expected: 1

	- Glyph name: lozenge	Contours detected: 0	Expected: 2

	- Glyph name: ogonek	Contours detected: 0	Expected: 1

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: partialdiff	Contours detected: 0	Expected: 2

	- Glyph name: perthousand	Contours detected: 0	Expected: 6 or 7

	- Glyph name: product	Contours detected: 0	Expected: 1

	- Glyph name: radical	Contours detected: 0	Expected: 1

	- Glyph name: summation	Contours detected: 0	Expected: 1

	- Glyph name: triagdn	Contours detected: 0	Expected: 1

	- Glyph name: triagup	Contours detected: 0	Expected: 1

	- Glyph name: uni0312	Contours detected: 0	Expected: 1

	- Glyph name: uni0327	Contours detected: 0	Expected: 1

	- Glyph name: uni0328	Contours detected: 0	Expected: 1

	- Glyph name: uni0E3F	Contours detected: 5	Expected: 3

	- Glyph name: uni20A6	Contours detected: 0	Expected: 1, 3 or 5

	- Glyph name: uni20A9	Contours detected: 0	Expected: 1, 3, 4 or 7

	- Glyph name: uni20AA	Contours detected: 0	Expected: 2

	- Glyph name: uni20AD	Contours detected: 0	Expected: 1

	- Glyph name: uni20AE	Contours detected: 0	Expected: 1

	- Glyph name: uni20B1	Contours detected: 0	Expected: 1, 2 or 4

	- Glyph name: uni20B2	Contours detected: 0	Expected: 1, 2 or 3

	- Glyph name: uni20B4	Contours detected: 0	Expected: 1 or 2

	- Glyph name: uni20B5	Contours detected: 0	Expected: 1 or 2

	- Glyph name: uni20B8	Contours detected: 0	Expected: 2

	- Glyph name: uni20B9	Contours detected: 0	Expected: 1

	- Glyph name: uni20BA	Contours detected: 0	Expected: 1

	- Glyph name: uni20BC	Contours detected: 0	Expected: 1

	- Glyph name: uni20BD	Contours detected: 0	Expected: 2

	- Glyph name: uni20BF	Contours detected: 0	Expected: 3

	- Glyph name: uni2126	Contours detected: 0	Expected: 1

	- Glyph name: uni2196	Contours detected: 0	Expected: 1

	- Glyph name: uni2197	Contours detected: 0	Expected: 1

	- Glyph name: uni2198	Contours detected: 0	Expected: 1

	- Glyph name: uni2199	Contours detected: 0	Expected: 1

	- Glyph name: uni2206	Contours detected: 0	Expected: 2

	- Glyph name: uni25A1	Contours detected: 0	Expected: 2

	- Glyph name: uni25AA	Contours detected: 0	Expected: 1

	- Glyph name: uni25AB	Contours detected: 0	Expected: 2

	- Glyph name: uni25B3	Contours detected: 0	Expected: 2

	- Glyph name: uni25B6	Contours detected: 0	Expected: 1

	- Glyph name: uni25B7	Contours detected: 0	Expected: 2

	- Glyph name: uni25BD	Contours detected: 0	Expected: 2

	- Glyph name: uni25C0	Contours detected: 0	Expected: 1

	- Glyph name: uni25C1	Contours detected: 0	Expected: 2

	- Glyph name: uni25C6	Contours detected: 0	Expected: 1

	- Glyph name: uni25C7	Contours detected: 0	Expected: 2

	- Glyph name: uni25CF	Contours detected: 0	Expected: 1

	- Glyph name: uni27E8	Contours detected: 0	Expected: 1 

	- And Glyph name: uni27E9	Contours detected: 0	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* W (U+0057): L<<488.0,712.0>--<449.0,24.0>> -> L<<449.0,24.0>--<449.0,8.0>>

	* W (U+0057): L<<488.0,728.0>--<488.0,712.0>> -> L<<488.0,712.0>--<449.0,24.0>>

	* W (U+0057): L<<63.0,24.0>--<24.0,712.0>> -> L<<24.0,712.0>--<24.0,728.0>>

	* W (U+0057): L<<63.0,8.0>--<63.0,24.0>> -> L<<63.0,24.0>--<24.0,712.0>>

	* Wacute (U+1E82): L<<488.0,712.0>--<449.0,24.0>> -> L<<449.0,24.0>--<449.0,8.0>>

	* Wacute (U+1E82): L<<488.0,728.0>--<488.0,712.0>> -> L<<488.0,712.0>--<449.0,24.0>>

	* Wacute (U+1E82): L<<63.0,24.0>--<24.0,712.0>> -> L<<24.0,712.0>--<24.0,728.0>>

	* Wacute (U+1E82): L<<63.0,8.0>--<63.0,24.0>> -> L<<63.0,24.0>--<24.0,712.0>>

	* Wcircumflex (U+0174): L<<488.0,712.0>--<449.0,24.0>> -> L<<449.0,24.0>--<449.0,8.0>>

	* Wcircumflex (U+0174): L<<488.0,728.0>--<488.0,712.0>> -> L<<488.0,712.0>--<449.0,24.0>>

	* Wcircumflex (U+0174): L<<63.0,24.0>--<24.0,712.0>> -> L<<24.0,712.0>--<24.0,728.0>>

	* Wcircumflex (U+0174): L<<63.0,8.0>--<63.0,24.0>> -> L<<63.0,24.0>--<24.0,712.0>>

	* Wdieresis (U+1E84): L<<488.0,712.0>--<449.0,24.0>> -> L<<449.0,24.0>--<449.0,8.0>>

	* Wdieresis (U+1E84): L<<488.0,728.0>--<488.0,712.0>> -> L<<488.0,712.0>--<449.0,24.0>>

	* Wdieresis (U+1E84): L<<63.0,24.0>--<24.0,712.0>> -> L<<24.0,712.0>--<24.0,728.0>>

	* Wdieresis (U+1E84): L<<63.0,8.0>--<63.0,24.0>> -> L<<63.0,24.0>--<24.0,712.0>>

	* Wgrave (U+1E80): L<<488.0,712.0>--<449.0,24.0>> -> L<<449.0,24.0>--<449.0,8.0>>

	* Wgrave (U+1E80): L<<488.0,728.0>--<488.0,712.0>> -> L<<488.0,712.0>--<449.0,24.0>>

	* Wgrave (U+1E80): L<<63.0,24.0>--<24.0,712.0>> -> L<<24.0,712.0>--<24.0,728.0>>

	* Wgrave (U+1E80): L<<63.0,8.0>--<63.0,24.0>> -> L<<63.0,24.0>--<24.0,712.0>>

	* Y (U+0059): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* Y (U+0059): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* Yacute (U+00DD): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* Yacute (U+00DD): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* Ycircumflex (U+0176): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* Ycircumflex (U+0176): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* Ydieresis (U+0178): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* Ydieresis (U+0178): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* Ygrave (U+1EF2): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* Ygrave (U+1EF2): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* backslash (U+005C): L<<143.0,702.0>--<234.0,440.0>> -> L<<234.0,440.0>--<446.0,-202.0>>

	* backslash (U+005C): L<<369.0,-206.0>--<278.0,56.0>> -> L<<278.0,56.0>--<66.0,698.0>>

	* uni1EF4 (U+1EF4): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* uni1EF4 (U+1EF4): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* uni1EF6 (U+1EF6): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* uni1EF6 (U+1EF6): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* uni1EF8 (U+1EF8): L<<108.0,728.0>--<199.0,512.0>> -> L<<199.0,512.0>--<232.0,416.0>>

	* uni1EF8 (U+1EF8): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>>

	* uni2116 (U+2116): L<<207.0,88.0>--<207.0,96.0>> -> L<<207.0,96.0>--<183.0,392.0>>

	* uni2116 (U+2116): L<<207.0,96.0>--<183.0,392.0>> -> L<<183.0,392.0>--<183.0,728.0>>

	* uni2116 (U+2116): L<<65.0,640.0>--<89.0,336.0>> -> L<<89.0,336.0>--<89.0,8.0>>

	* uni2116 (U+2116): L<<65.0,648.0>--<65.0,640.0>> -> L<<65.0,640.0>--<89.0,336.0>>

	* w (U+0077): L<<139.0,100.0>--<166.0,189.0>> -> L<<166.0,189.0>--<218.0,342.0>>

	* w (U+0077): L<<365.0,100.0>--<389.0,226.0>> -> L<<389.0,226.0>--<418.0,515.0>>

	* w (U+0077): L<<96.0,513.0>--<109.0,382.0>> -> L<<109.0,382.0>--<139.0,100.0>>

	* wacute (U+1E83): L<<139.0,100.0>--<166.0,189.0>> -> L<<166.0,189.0>--<218.0,342.0>>

	* wacute (U+1E83): L<<365.0,100.0>--<389.0,226.0>> -> L<<389.0,226.0>--<418.0,515.0>>

	* wacute (U+1E83): L<<96.0,513.0>--<109.0,382.0>> -> L<<109.0,382.0>--<139.0,100.0>>

	* wcircumflex (U+0175): L<<139.0,100.0>--<166.0,189.0>> -> L<<166.0,189.0>--<218.0,342.0>>

	* wcircumflex (U+0175): L<<365.0,100.0>--<389.0,226.0>> -> L<<389.0,226.0>--<418.0,515.0>>

	* wcircumflex (U+0175): L<<96.0,513.0>--<109.0,382.0>> -> L<<109.0,382.0>--<139.0,100.0>>

	* wdieresis (U+1E85): L<<139.0,100.0>--<166.0,189.0>> -> L<<166.0,189.0>--<218.0,342.0>>

	* wdieresis (U+1E85): L<<365.0,100.0>--<389.0,226.0>> -> L<<389.0,226.0>--<418.0,515.0>>

	* wdieresis (U+1E85): L<<96.0,513.0>--<109.0,382.0>> -> L<<109.0,382.0>--<139.0,100.0>>

	* wgrave (U+1E81): L<<139.0,100.0>--<166.0,189.0>> -> L<<166.0,189.0>--<218.0,342.0>>

	* wgrave (U+1E81): L<<365.0,100.0>--<389.0,226.0>> -> L<<389.0,226.0>--<418.0,515.0>> 

	* And wgrave (U+1E81): L<<96.0,513.0>--<109.0,382.0>> -> L<<109.0,382.0>--<139.0,100.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* newGlyph (U+00B5): L<<59.0,-208.0>--<58.0,513.0>> 

	* And uniFEDC (U+FEDC): L<<481.0,126.0>--<480.0,8.0>> [code: found-semi-vertical]
</div></details><br></div></details>
### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 12 | 44 | 668 | 37 | 526 | 0 |
| 0% | 1% | 3% | 52% | 3% | 41% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
