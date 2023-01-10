## Fontbakery report

Fontbakery version: 0.8.10

<details><summary><b>[10] HasubiMono-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 976, but got 960 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 464, but got 360 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** Font is monospaced but 22 glyphs (3.53%) have a different width. You should check the widths of: ['AE', 'Lcaron', 'uni0145', 'Eng', 'dcaron', 'dcroat', 'uni0123', 'lcaron', 'uni013C', 'lslash', 'uni0146', 'eng', 'uogonek', 'uniFEF8', 'uniFEFA', 'uniFEF6', 'lam_alefWaslaar.fina', 'uni066B', 'uni066C', 'uni2074', 'trademark', 'logicalnot'] [code: mono-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- doublestrokear

	- gafsarkashabovear

	- gafsarkashcenterar

	- miniKehehar

	- threedotsdownabovear

	- threedotsdowncenterar

	- threedotsupbelowar

	- twodotsverticalabovear 

	- And twodotsverticalbelowar
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: onequarter	Contours detected: 1	Expected: 3 or 4

	- Glyph name: onehalf	Contours detected: 1	Expected: 3

	- Glyph name: threequarters	Contours detected: 1	Expected: 3 or 4

	- Glyph name: Ccedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: aogonek	Contours detected: 0	Expected: 2

	- Glyph name: dcaron	Contours detected: 0	Expected: 3

	- Glyph name: dcroat	Contours detected: 0	Expected: 2

	- Glyph name: eogonek	Contours detected: 0	Expected: 2

	- Glyph name: uni0122	Contours detected: 1	Expected: 2

	- Glyph name: uni0123	Contours detected: 0	Expected: 3 or 4

	- Glyph name: hbar	Contours detected: 0	Expected: 1

	- Glyph name: Iogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: iogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: IJ	Contours detected: 0	Expected: 1 or 2

	- Glyph name: ij	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni0136	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni0137	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni013B	Contours detected: 0	Expected: 2

	- Glyph name: uni013C	Contours detected: 0	Expected: 2

	- Glyph name: Lcaron	Contours detected: 0	Expected: 2

	- Glyph name: lcaron	Contours detected: 0	Expected: 2

	- Glyph name: Lslash	Contours detected: 0	Expected: 1

	- Glyph name: lslash	Contours detected: 0	Expected: 1

	- Glyph name: uni0145	Contours detected: 0	Expected: 2

	- Glyph name: uni0146	Contours detected: 0	Expected: 2

	- Glyph name: Eng	Contours detected: 0	Expected: 1

	- Glyph name: eng	Contours detected: 0	Expected: 1

	- Glyph name: uni0156	Contours detected: 0	Expected: 3

	- Glyph name: uni0157	Contours detected: 0	Expected: 2

	- Glyph name: Scedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: scedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: tcaron	Contours detected: 0	Expected: 2

	- Glyph name: Uogonek	Contours detected: 0	Expected: 1

	- Glyph name: uogonek	Contours detected: 0	Expected: 1

	- Glyph name: uni0218	Contours detected: 0	Expected: 2

	- Glyph name: uni0219	Contours detected: 0	Expected: 2

	- Glyph name: uni021A	Contours detected: 0	Expected: 2

	- Glyph name: uni021B	Contours detected: 0	Expected: 2

	- Glyph name: ogonek	Contours detected: 0	Expected: 1

	- Glyph name: uni0312	Contours detected: 0	Expected: 1

	- Glyph name: uni0326	Contours detected: 0	Expected: 1

	- Glyph name: uni0327	Contours detected: 0	Expected: 1

	- Glyph name: uni0328	Contours detected: 0	Expected: 1

	- Glyph name: uni1E9E	Contours detected: 0	Expected: 1

	- Glyph name: trademark	Contours detected: 0	Expected: 2

	- Glyph name: Ccedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Eng	Contours detected: 0	Expected: 1

	- Glyph name: IJ	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Iogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Lcaron	Contours detected: 0	Expected: 2

	- Glyph name: Lslash	Contours detected: 0	Expected: 1

	- Glyph name: Uogonek	Contours detected: 0	Expected: 1

	- Glyph name: aogonek	Contours detected: 0	Expected: 2

	- Glyph name: dcaron	Contours detected: 0	Expected: 3

	- Glyph name: dcroat	Contours detected: 0	Expected: 2

	- Glyph name: eng	Contours detected: 0	Expected: 1

	- Glyph name: eogonek	Contours detected: 0	Expected: 2

	- Glyph name: hbar	Contours detected: 0	Expected: 1

	- Glyph name: ij	Contours detected: 0	Expected: 3 or 4

	- Glyph name: iogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: lcaron	Contours detected: 0	Expected: 2

	- Glyph name: lslash	Contours detected: 0	Expected: 1

	- Glyph name: ogonek	Contours detected: 0	Expected: 1

	- Glyph name: onehalf	Contours detected: 1	Expected: 3

	- Glyph name: onequarter	Contours detected: 1	Expected: 3 or 4

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: tcaron	Contours detected: 0	Expected: 2

	- Glyph name: threequarters	Contours detected: 1	Expected: 3 or 4

	- Glyph name: trademark	Contours detected: 0	Expected: 2

	- Glyph name: uni0122	Contours detected: 1	Expected: 2

	- Glyph name: uni0123	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni0136	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni0137	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni013B	Contours detected: 0	Expected: 2

	- Glyph name: uni013C	Contours detected: 0	Expected: 2

	- Glyph name: uni0145	Contours detected: 0	Expected: 2

	- Glyph name: uni0146	Contours detected: 0	Expected: 2

	- Glyph name: uni0156	Contours detected: 0	Expected: 3

	- Glyph name: uni0157	Contours detected: 0	Expected: 2

	- Glyph name: uni0218	Contours detected: 0	Expected: 2

	- Glyph name: uni0219	Contours detected: 0	Expected: 2

	- Glyph name: uni021A	Contours detected: 0	Expected: 2

	- Glyph name: uni021B	Contours detected: 0	Expected: 2

	- Glyph name: uni0312	Contours detected: 0	Expected: 1

	- Glyph name: uni0326	Contours detected: 0	Expected: 1

	- Glyph name: uni0327	Contours detected: 0	Expected: 1

	- Glyph name: uni0328	Contours detected: 0	Expected: 1

	- Glyph name: uni1E9E	Contours detected: 0	Expected: 1 

	- And Glyph name: uogonek	Contours detected: 0	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* a (U+0061): X=135.0,Y=0.5 (should be at baseline 0?)

	* a (U+0061): X=340.0,Y=510.0 (should be at x-height 512?)

	* b (U+0062): X=212.5,Y=511.5 (should be at x-height 512?)

	* b (U+0062): X=212.5,Y=1.0 (should be at baseline 0?)

	* d (U+0064): X=303.5,Y=1.0 (should be at baseline 0?)

	* d (U+0064): X=308.5,Y=510.0 (should be at x-height 512?)

	* n (U+006E): X=215.0,Y=510.5 (should be at x-height 512?)

	* p (U+0070): X=195.0,Y=510.0 (should be at x-height 512?)

	* q (U+0071): X=317.5,Y=510.0 (should be at x-height 512?)

	* r (U+0072): X=282.5,Y=513.0 (should be at x-height 512?)

	* s (U+0073): X=352.0,Y=-2.0 (should be at baseline 0?)

	* copyright (U+00A9): X=370.0,Y=-0.5 (should be at baseline 0?)

	* copyright (U+00A9): X=142.5,Y=-0.5 (should be at baseline 0?)

	* newGlyph (U+00B5): X=184.0,Y=-1.5 (should be at baseline 0?)

	* agrave (U+00E0): X=135.0,Y=0.5 (should be at baseline 0?)

	* aacute (U+00E1): X=135.0,Y=0.5 (should be at baseline 0?)

	* acircumflex (U+00E2): X=135.0,Y=0.5 (should be at baseline 0?)

	* atilde (U+00E3): X=135.0,Y=0.5 (should be at baseline 0?)

	* adieresis (U+00E4): X=135.0,Y=0.5 (should be at baseline 0?)

	* aring (U+00E5): X=135.0,Y=0.5 (should be at baseline 0?)

	* ae (U+00E6): X=461.5,Y=1.5 (should be at baseline 0?)

	* ae (U+00E6): X=38.5,Y=0.5 (should be at baseline 0?)

	* eth (U+00F0): X=299.5,Y=1.0 (should be at baseline 0?)

	* thorn (U+00FE): X=212.5,Y=1.0 (should be at baseline 0?)

	* amacron (U+0101): X=135.0,Y=0.5 (should be at baseline 0?)

	* abreve (U+0103): X=135.0,Y=0.5 (should be at baseline 0?)

	* oe (U+0153): X=455.5,Y=1.5 (should be at baseline 0?)

	* oe (U+0153): X=221.0,Y=-2.0 (should be at baseline 0?)

	* sacute (U+015B): X=352.0,Y=-2.0 (should be at baseline 0?)

	* scaron (U+0161): X=352.0,Y=-2.0 (should be at baseline 0?)

	* uni0631 (U+0631): X=290.0,Y=-258.0 (should be at descender -260?)

	* uni0632 (U+0632): X=290.0,Y=-258.0 (should be at descender -260?)

	* uni0635 (U+0635): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0635 (U+0635): X=-32.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=-32.0,Y=-261.0 (should be at descender -260?)

	* uni0698 (U+0698): X=290.0,Y=-258.0 (should be at descender -260?)

	* uni06A4 (U+06A4): X=312.5,Y=737.5 (should be at cap-height 736?) 

	* And uni06A4 (U+06A4): X=391.5,Y=737.5 (should be at cap-height 736?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* W (U+0057): L<<488.0,728.0>--<488.0,720.0>> -> L<<488.0,720.0>--<437.0,8.0>>

	* W (U+0057): L<<75.0,8.0>--<24.0,720.0>> -> L<<24.0,720.0>--<24.0,728.0>>

	* Wacute (U+1E82): L<<488.0,728.0>--<488.0,720.0>> -> L<<488.0,720.0>--<437.0,8.0>>

	* Wacute (U+1E82): L<<75.0,8.0>--<24.0,720.0>> -> L<<24.0,720.0>--<24.0,728.0>>

	* Wcircumflex (U+0174): L<<488.0,728.0>--<488.0,720.0>> -> L<<488.0,720.0>--<437.0,8.0>>

	* Wcircumflex (U+0174): L<<75.0,8.0>--<24.0,720.0>> -> L<<24.0,720.0>--<24.0,728.0>>

	* Wdieresis (U+1E84): L<<488.0,728.0>--<488.0,720.0>> -> L<<488.0,720.0>--<437.0,8.0>>

	* Wdieresis (U+1E84): L<<75.0,8.0>--<24.0,720.0>> -> L<<24.0,720.0>--<24.0,728.0>>

	* Wgrave (U+1E80): L<<488.0,728.0>--<488.0,720.0>> -> L<<488.0,720.0>--<437.0,8.0>> 

	* And Wgrave (U+1E80): L<<75.0,8.0>--<24.0,720.0>> -> L<<24.0,720.0>--<24.0,728.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* newGlyph (U+00B5): L<<59.0,-208.0>--<58.0,513.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[10] HasubiMono-Bold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 976, but got 960 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 464, but got 360 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** Font is monospaced but 34 glyphs (5.46%) have a different width. You should check the widths of: ['AE', 'uni0136', 'Lcaron', 'uni0145', 'Eng', 'uni0156', 'aogonek', 'dcaron', 'dcroat', 'eogonek', 'uni0123', 'hbar', 'ij', 'lcaron', 'uni013C', 'lslash', 'uni0146', 'eng', 'uni0157', 'scedilla', 'uni0219', 'tcaron', 'uni021B', 'uogonek', 'uniFEF8', 'uniFEFA', 'uniFEF6', 'lam_alefWaslaar.fina', 'uni066B', 'uni066C', 'uni2074', 'guillemotleft', 'trademark', 'logicalnot'] [code: mono-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- doublestrokear

	- gafsarkashabovear

	- gafsarkashcenterar

	- miniKehehar

	- threedotsdownabovear

	- threedotsdowncenterar

	- threedotsupbelowar

	- twodotsverticalabovear 

	- And twodotsverticalbelowar
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: colon	Contours detected: 1	Expected: 2

	- Glyph name: onequarter	Contours detected: 1	Expected: 3 or 4

	- Glyph name: onehalf	Contours detected: 1	Expected: 3

	- Glyph name: threequarters	Contours detected: 1	Expected: 3 or 4

	- Glyph name: Ccedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: aogonek	Contours detected: 0	Expected: 2

	- Glyph name: dcaron	Contours detected: 0	Expected: 3

	- Glyph name: dcroat	Contours detected: 0	Expected: 2

	- Glyph name: eogonek	Contours detected: 0	Expected: 2

	- Glyph name: uni0122	Contours detected: 1	Expected: 2

	- Glyph name: uni0123	Contours detected: 0	Expected: 3 or 4

	- Glyph name: hbar	Contours detected: 0	Expected: 1

	- Glyph name: Iogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: iogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: IJ	Contours detected: 0	Expected: 1 or 2

	- Glyph name: ij	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni0136	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni0137	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni013B	Contours detected: 0	Expected: 2

	- Glyph name: uni013C	Contours detected: 0	Expected: 2

	- Glyph name: Lcaron	Contours detected: 0	Expected: 2

	- Glyph name: lcaron	Contours detected: 0	Expected: 2

	- Glyph name: Lslash	Contours detected: 0	Expected: 1

	- Glyph name: lslash	Contours detected: 0	Expected: 1

	- Glyph name: uni0145	Contours detected: 0	Expected: 2

	- Glyph name: uni0146	Contours detected: 0	Expected: 2

	- Glyph name: Eng	Contours detected: 0	Expected: 1

	- Glyph name: eng	Contours detected: 0	Expected: 1

	- Glyph name: uni0156	Contours detected: 0	Expected: 3

	- Glyph name: uni0157	Contours detected: 0	Expected: 2

	- Glyph name: Scedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: scedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: tcaron	Contours detected: 0	Expected: 2

	- Glyph name: Uogonek	Contours detected: 0	Expected: 1

	- Glyph name: uogonek	Contours detected: 0	Expected: 1

	- Glyph name: uni0218	Contours detected: 0	Expected: 2

	- Glyph name: uni0219	Contours detected: 0	Expected: 2

	- Glyph name: uni021A	Contours detected: 0	Expected: 2

	- Glyph name: uni021B	Contours detected: 0	Expected: 2

	- Glyph name: ogonek	Contours detected: 0	Expected: 1

	- Glyph name: uni0312	Contours detected: 0	Expected: 1

	- Glyph name: uni0326	Contours detected: 0	Expected: 1

	- Glyph name: uni0327	Contours detected: 0	Expected: 1

	- Glyph name: uni0328	Contours detected: 0	Expected: 1

	- Glyph name: uni1E9E	Contours detected: 0	Expected: 1

	- Glyph name: trademark	Contours detected: 0	Expected: 2

	- Glyph name: Ccedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Eng	Contours detected: 0	Expected: 1

	- Glyph name: IJ	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Iogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Lcaron	Contours detected: 0	Expected: 2

	- Glyph name: Lslash	Contours detected: 0	Expected: 1

	- Glyph name: Uogonek	Contours detected: 0	Expected: 1

	- Glyph name: aogonek	Contours detected: 0	Expected: 2

	- Glyph name: colon	Contours detected: 1	Expected: 2

	- Glyph name: dcaron	Contours detected: 0	Expected: 3

	- Glyph name: dcroat	Contours detected: 0	Expected: 2

	- Glyph name: eng	Contours detected: 0	Expected: 1

	- Glyph name: eogonek	Contours detected: 0	Expected: 2

	- Glyph name: hbar	Contours detected: 0	Expected: 1

	- Glyph name: ij	Contours detected: 0	Expected: 3 or 4

	- Glyph name: iogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: lcaron	Contours detected: 0	Expected: 2

	- Glyph name: lslash	Contours detected: 0	Expected: 1

	- Glyph name: ogonek	Contours detected: 0	Expected: 1

	- Glyph name: onehalf	Contours detected: 1	Expected: 3

	- Glyph name: onequarter	Contours detected: 1	Expected: 3 or 4

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: tcaron	Contours detected: 0	Expected: 2

	- Glyph name: threequarters	Contours detected: 1	Expected: 3 or 4

	- Glyph name: trademark	Contours detected: 0	Expected: 2

	- Glyph name: uni0122	Contours detected: 1	Expected: 2

	- Glyph name: uni0123	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni0136	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni0137	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni013B	Contours detected: 0	Expected: 2

	- Glyph name: uni013C	Contours detected: 0	Expected: 2

	- Glyph name: uni0145	Contours detected: 0	Expected: 2

	- Glyph name: uni0146	Contours detected: 0	Expected: 2

	- Glyph name: uni0156	Contours detected: 0	Expected: 3

	- Glyph name: uni0157	Contours detected: 0	Expected: 2

	- Glyph name: uni0218	Contours detected: 0	Expected: 2

	- Glyph name: uni0219	Contours detected: 0	Expected: 2

	- Glyph name: uni021A	Contours detected: 0	Expected: 2

	- Glyph name: uni021B	Contours detected: 0	Expected: 2

	- Glyph name: uni0312	Contours detected: 0	Expected: 1

	- Glyph name: uni0326	Contours detected: 0	Expected: 1

	- Glyph name: uni0327	Contours detected: 0	Expected: 1

	- Glyph name: uni0328	Contours detected: 0	Expected: 1

	- Glyph name: uni1E9E	Contours detected: 0	Expected: 1 

	- And Glyph name: uogonek	Contours detected: 0	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* W (U+0057): L<<143.0,92.0>--<169.0,289.0>> -> L<<169.0,289.0>--<210.0,508.0>>

	* W (U+0057): L<<301.0,508.0>--<323.0,307.0>> -> L<<323.0,307.0>--<368.0,92.0>>

	* W (U+0057): L<<368.0,92.0>--<397.0,393.0>> -> L<<397.0,393.0>--<420.0,715.0>>

	* W (U+0057): L<<75.0,8.0>--<20.0,703.0>> -> L<<20.0,703.0>--<20.0,711.0>>

	* W (U+0057): L<<95.0,711.0>--<116.0,406.0>> -> L<<116.0,406.0>--<143.0,92.0>>

	* Wacute (U+1E82): L<<143.0,92.0>--<169.0,289.0>> -> L<<169.0,289.0>--<210.0,508.0>>

	* Wacute (U+1E82): L<<301.0,508.0>--<323.0,307.0>> -> L<<323.0,307.0>--<368.0,92.0>>

	* Wacute (U+1E82): L<<368.0,92.0>--<397.0,393.0>> -> L<<397.0,393.0>--<420.0,715.0>>

	* Wacute (U+1E82): L<<75.0,8.0>--<20.0,703.0>> -> L<<20.0,703.0>--<20.0,711.0>>

	* Wacute (U+1E82): L<<95.0,711.0>--<116.0,406.0>> -> L<<116.0,406.0>--<143.0,92.0>>

	* Wcircumflex (U+0174): L<<143.0,92.0>--<169.0,289.0>> -> L<<169.0,289.0>--<210.0,508.0>>

	* Wcircumflex (U+0174): L<<301.0,508.0>--<323.0,307.0>> -> L<<323.0,307.0>--<368.0,92.0>>

	* Wcircumflex (U+0174): L<<368.0,92.0>--<397.0,393.0>> -> L<<397.0,393.0>--<420.0,715.0>>

	* Wcircumflex (U+0174): L<<75.0,8.0>--<20.0,703.0>> -> L<<20.0,703.0>--<20.0,711.0>>

	* Wcircumflex (U+0174): L<<95.0,711.0>--<116.0,406.0>> -> L<<116.0,406.0>--<143.0,92.0>>

	* Wdieresis (U+1E84): L<<143.0,92.0>--<169.0,289.0>> -> L<<169.0,289.0>--<210.0,508.0>>

	* Wdieresis (U+1E84): L<<301.0,508.0>--<323.0,307.0>> -> L<<323.0,307.0>--<368.0,92.0>>

	* Wdieresis (U+1E84): L<<368.0,92.0>--<397.0,393.0>> -> L<<397.0,393.0>--<420.0,715.0>>

	* Wdieresis (U+1E84): L<<75.0,8.0>--<20.0,703.0>> -> L<<20.0,703.0>--<20.0,711.0>>

	* Wdieresis (U+1E84): L<<95.0,711.0>--<116.0,406.0>> -> L<<116.0,406.0>--<143.0,92.0>>

	* Wgrave (U+1E80): L<<143.0,92.0>--<169.0,289.0>> -> L<<169.0,289.0>--<210.0,508.0>>

	* Wgrave (U+1E80): L<<301.0,508.0>--<323.0,307.0>> -> L<<323.0,307.0>--<368.0,92.0>>

	* Wgrave (U+1E80): L<<368.0,92.0>--<397.0,393.0>> -> L<<397.0,393.0>--<420.0,715.0>>

	* Wgrave (U+1E80): L<<75.0,8.0>--<20.0,703.0>> -> L<<20.0,703.0>--<20.0,711.0>>

	* Wgrave (U+1E80): L<<95.0,711.0>--<116.0,406.0>> -> L<<116.0,406.0>--<143.0,92.0>>

	* backslash (U+005C): L<<145.0,700.0>--<288.0,280.0>> -> L<<288.0,280.0>--<444.0,-204.0>>

	* backslash (U+005C): L<<367.0,-204.0>--<224.0,216.0>> -> L<<224.0,216.0>--<68.0,700.0>>

	* w (U+0077): L<<145.0,99.0>--<179.0,229.0>> -> L<<179.0,229.0>--<220.0,345.0>>

	* w (U+0077): L<<365.0,99.0>--<394.0,289.0>> -> L<<394.0,289.0>--<417.0,508.0>>

	* w (U+0077): L<<99.0,504.0>--<119.0,310.0>> -> L<<119.0,310.0>--<145.0,99.0>>

	* wacute (U+1E83): L<<145.0,99.0>--<179.0,229.0>> -> L<<179.0,229.0>--<220.0,345.0>>

	* wacute (U+1E83): L<<365.0,99.0>--<394.0,289.0>> -> L<<394.0,289.0>--<417.0,508.0>>

	* wacute (U+1E83): L<<99.0,504.0>--<119.0,310.0>> -> L<<119.0,310.0>--<145.0,99.0>>

	* wcircumflex (U+0175): L<<145.0,99.0>--<179.0,229.0>> -> L<<179.0,229.0>--<220.0,345.0>>

	* wcircumflex (U+0175): L<<365.0,99.0>--<394.0,289.0>> -> L<<394.0,289.0>--<417.0,508.0>>

	* wcircumflex (U+0175): L<<99.0,504.0>--<119.0,310.0>> -> L<<119.0,310.0>--<145.0,99.0>>

	* wdieresis (U+1E85): L<<145.0,99.0>--<179.0,229.0>> -> L<<179.0,229.0>--<220.0,345.0>>

	* wdieresis (U+1E85): L<<365.0,99.0>--<394.0,289.0>> -> L<<394.0,289.0>--<417.0,508.0>>

	* wdieresis (U+1E85): L<<99.0,504.0>--<119.0,310.0>> -> L<<119.0,310.0>--<145.0,99.0>>

	* wgrave (U+1E81): L<<145.0,99.0>--<179.0,229.0>> -> L<<179.0,229.0>--<220.0,345.0>>

	* wgrave (U+1E81): L<<365.0,99.0>--<394.0,289.0>> -> L<<394.0,289.0>--<417.0,508.0>> 

	* And wgrave (U+1E81): L<<99.0,504.0>--<119.0,310.0>> -> L<<119.0,310.0>--<145.0,99.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* W (U+0057): L<<116.0,406.0>--<143.0,92.0>>/L<<143.0,92.0>--<169.0,289.0>> = 12.43304524184989

	* Wacute (U+1E82): L<<116.0,406.0>--<143.0,92.0>>/L<<143.0,92.0>--<169.0,289.0>> = 12.43304524184989

	* Wcircumflex (U+0174): L<<116.0,406.0>--<143.0,92.0>>/L<<143.0,92.0>--<169.0,289.0>> = 12.43304524184989

	* Wdieresis (U+1E84): L<<116.0,406.0>--<143.0,92.0>>/L<<143.0,92.0>--<169.0,289.0>> = 12.43304524184989 

	* And Wgrave (U+1E80): L<<116.0,406.0>--<143.0,92.0>>/L<<143.0,92.0>--<169.0,289.0>> = 12.43304524184989 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* newGlyph (U+00B5): L<<59.0,-208.0>--<58.0,513.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[11] HasubiMono-SemiBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 976, but got 960 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 464, but got 360 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** Font is monospaced but 34 glyphs (5.46%) have a different width. You should check the widths of: ['AE', 'uni0136', 'Lcaron', 'uni0145', 'Eng', 'uni0156', 'aogonek', 'dcaron', 'dcroat', 'eogonek', 'uni0123', 'hbar', 'ij', 'lcaron', 'uni013C', 'lslash', 'uni0146', 'eng', 'uni0157', 'scedilla', 'uni0219', 'tcaron', 'uni021B', 'uogonek', 'uniFEF8', 'uniFEFA', 'uniFEF6', 'lam_alefWaslaar.fina', 'uni066B', 'uni066C', 'uni2074', 'guillemotleft', 'trademark', 'logicalnot'] [code: mono-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- doublestrokear

	- gafsarkashabovear

	- gafsarkashcenterar

	- miniKehehar

	- threedotsdownabovear

	- threedotsdowncenterar

	- threedotsupbelowar

	- twodotsverticalabovear 

	- And twodotsverticalbelowar
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: colon	Contours detected: 1	Expected: 2

	- Glyph name: onequarter	Contours detected: 1	Expected: 3 or 4

	- Glyph name: onehalf	Contours detected: 1	Expected: 3

	- Glyph name: threequarters	Contours detected: 1	Expected: 3 or 4

	- Glyph name: Ccedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: aogonek	Contours detected: 0	Expected: 2

	- Glyph name: dcaron	Contours detected: 0	Expected: 3

	- Glyph name: dcroat	Contours detected: 0	Expected: 2

	- Glyph name: eogonek	Contours detected: 0	Expected: 2

	- Glyph name: uni0122	Contours detected: 1	Expected: 2

	- Glyph name: uni0123	Contours detected: 0	Expected: 3 or 4

	- Glyph name: hbar	Contours detected: 0	Expected: 1

	- Glyph name: Iogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: iogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: IJ	Contours detected: 0	Expected: 1 or 2

	- Glyph name: ij	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni0136	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni0137	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni013B	Contours detected: 0	Expected: 2

	- Glyph name: uni013C	Contours detected: 0	Expected: 2

	- Glyph name: Lcaron	Contours detected: 0	Expected: 2

	- Glyph name: lcaron	Contours detected: 0	Expected: 2

	- Glyph name: Lslash	Contours detected: 0	Expected: 1

	- Glyph name: lslash	Contours detected: 0	Expected: 1

	- Glyph name: uni0145	Contours detected: 0	Expected: 2

	- Glyph name: uni0146	Contours detected: 0	Expected: 2

	- Glyph name: Eng	Contours detected: 0	Expected: 1

	- Glyph name: eng	Contours detected: 0	Expected: 1

	- Glyph name: uni0156	Contours detected: 0	Expected: 3

	- Glyph name: uni0157	Contours detected: 0	Expected: 2

	- Glyph name: Scedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: scedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: tcaron	Contours detected: 0	Expected: 2

	- Glyph name: Uogonek	Contours detected: 0	Expected: 1

	- Glyph name: uogonek	Contours detected: 0	Expected: 1

	- Glyph name: uni0218	Contours detected: 0	Expected: 2

	- Glyph name: uni0219	Contours detected: 0	Expected: 2

	- Glyph name: uni021A	Contours detected: 0	Expected: 2

	- Glyph name: uni021B	Contours detected: 0	Expected: 2

	- Glyph name: ogonek	Contours detected: 0	Expected: 1

	- Glyph name: uni0312	Contours detected: 0	Expected: 1

	- Glyph name: uni0326	Contours detected: 0	Expected: 1

	- Glyph name: uni0327	Contours detected: 0	Expected: 1

	- Glyph name: uni0328	Contours detected: 0	Expected: 1

	- Glyph name: uni1E9E	Contours detected: 0	Expected: 1

	- Glyph name: trademark	Contours detected: 0	Expected: 2

	- Glyph name: Ccedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Eng	Contours detected: 0	Expected: 1

	- Glyph name: IJ	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Iogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Lcaron	Contours detected: 0	Expected: 2

	- Glyph name: Lslash	Contours detected: 0	Expected: 1

	- Glyph name: Uogonek	Contours detected: 0	Expected: 1

	- Glyph name: aogonek	Contours detected: 0	Expected: 2

	- Glyph name: colon	Contours detected: 1	Expected: 2

	- Glyph name: dcaron	Contours detected: 0	Expected: 3

	- Glyph name: dcroat	Contours detected: 0	Expected: 2

	- Glyph name: eng	Contours detected: 0	Expected: 1

	- Glyph name: eogonek	Contours detected: 0	Expected: 2

	- Glyph name: hbar	Contours detected: 0	Expected: 1

	- Glyph name: ij	Contours detected: 0	Expected: 3 or 4

	- Glyph name: iogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: lcaron	Contours detected: 0	Expected: 2

	- Glyph name: lslash	Contours detected: 0	Expected: 1

	- Glyph name: ogonek	Contours detected: 0	Expected: 1

	- Glyph name: onehalf	Contours detected: 1	Expected: 3

	- Glyph name: onequarter	Contours detected: 1	Expected: 3 or 4

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: tcaron	Contours detected: 0	Expected: 2

	- Glyph name: threequarters	Contours detected: 1	Expected: 3 or 4

	- Glyph name: trademark	Contours detected: 0	Expected: 2

	- Glyph name: uni0122	Contours detected: 1	Expected: 2

	- Glyph name: uni0123	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni0136	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni0137	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni013B	Contours detected: 0	Expected: 2

	- Glyph name: uni013C	Contours detected: 0	Expected: 2

	- Glyph name: uni0145	Contours detected: 0	Expected: 2

	- Glyph name: uni0146	Contours detected: 0	Expected: 2

	- Glyph name: uni0156	Contours detected: 0	Expected: 3

	- Glyph name: uni0157	Contours detected: 0	Expected: 2

	- Glyph name: uni0218	Contours detected: 0	Expected: 2

	- Glyph name: uni0219	Contours detected: 0	Expected: 2

	- Glyph name: uni021A	Contours detected: 0	Expected: 2

	- Glyph name: uni021B	Contours detected: 0	Expected: 2

	- Glyph name: uni0312	Contours detected: 0	Expected: 1

	- Glyph name: uni0326	Contours detected: 0	Expected: 1

	- Glyph name: uni0327	Contours detected: 0	Expected: 1

	- Glyph name: uni0328	Contours detected: 0	Expected: 1

	- Glyph name: uni1E9E	Contours detected: 0	Expected: 1 

	- And Glyph name: uogonek	Contours detected: 0	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* a (U+0061): X=135.0,Y=0.5 (should be at baseline 0?)

	* a (U+0061): X=340.0,Y=510.0 (should be at x-height 512?)

	* b (U+0062): X=212.5,Y=512.5 (should be at x-height 512?)

	* d (U+0064): X=303.5,Y=1.0 (should be at baseline 0?)

	* d (U+0064): X=308.5,Y=510.0 (should be at x-height 512?)

	* f (U+0066): X=330.0,Y=727.0 (should be at cap-height 725?)

	* f (U+0066): X=478.0,Y=727.0 (should be at cap-height 725?)

	* p (U+0070): X=195.0,Y=510.0 (should be at x-height 512?)

	* q (U+0071): X=317.5,Y=510.0 (should be at x-height 512?)

	* r (U+0072): X=282.5,Y=513.0 (should be at x-height 512?)

	* s (U+0073): X=351.5,Y=-2.0 (should be at baseline 0?)

	* dieresis (U+00A8): X=128.0,Y=725.5 (should be at cap-height 725?)

	* dieresis (U+00A8): X=206.0,Y=725.5 (should be at cap-height 725?)

	* dieresis (U+00A8): X=305.5,Y=725.5 (should be at cap-height 725?)

	* dieresis (U+00A8): X=383.5,Y=725.5 (should be at cap-height 725?)

	* copyright (U+00A9): X=370.0,Y=-0.5 (should be at baseline 0?)

	* copyright (U+00A9): X=142.5,Y=-0.5 (should be at baseline 0?)

	* degree (U+00B0): X=143.5,Y=724.5 (should be at cap-height 725?)

	* degree (U+00B0): X=369.0,Y=724.5 (should be at cap-height 725?)

	* newGlyph (U+00B5): X=184.0,Y=-1.5 (should be at baseline 0?)

	* agrave (U+00E0): X=135.0,Y=0.5 (should be at baseline 0?)

	* aacute (U+00E1): X=135.0,Y=0.5 (should be at baseline 0?)

	* acircumflex (U+00E2): X=135.0,Y=0.5 (should be at baseline 0?)

	* atilde (U+00E3): X=135.0,Y=0.5 (should be at baseline 0?)

	* adieresis (U+00E4): X=135.0,Y=0.5 (should be at baseline 0?)

	* aring (U+00E5): X=135.0,Y=0.5 (should be at baseline 0?)

	* aring (U+00E5): X=250.0,Y=726.0 (should be at cap-height 725?)

	* ae (U+00E6): X=461.5,Y=1.5 (should be at baseline 0?)

	* ae (U+00E6): X=38.5,Y=0.5 (should be at baseline 0?)

	* eth (U+00F0): X=299.5,Y=1.0 (should be at baseline 0?)

	* thorn (U+00FE): X=212.5,Y=1.0 (should be at baseline 0?)

	* amacron (U+0101): X=135.0,Y=0.5 (should be at baseline 0?)

	* abreve (U+0103): X=135.0,Y=0.5 (should be at baseline 0?)

	* ccaron (U+010D): X=173.5,Y=723.0 (should be at cap-height 725?)

	* ccaron (U+010D): X=356.5,Y=723.0 (should be at cap-height 725?)

	* ecaron (U+011B): X=164.5,Y=723.0 (should be at cap-height 725?)

	* ecaron (U+011B): X=347.5,Y=723.0 (should be at cap-height 725?)

	* lacute (U+013A): X=268.0,Y=941.0 (should be at ascender 940?)

	* lacute (U+013A): X=344.0,Y=941.0 (should be at ascender 940?)

	* ncaron (U+0148): X=170.5,Y=723.0 (should be at cap-height 725?)

	* ncaron (U+0148): X=353.5,Y=723.0 (should be at cap-height 725?)

	* oe (U+0153): X=455.5,Y=1.5 (should be at baseline 0?)

	* oe (U+0153): X=221.0,Y=-2.0 (should be at baseline 0?)

	* rcaron (U+0159): X=179.5,Y=723.0 (should be at cap-height 725?)

	* rcaron (U+0159): X=362.5,Y=723.0 (should be at cap-height 725?)

	* sacute (U+015B): X=351.5,Y=-2.0 (should be at baseline 0?)

	* scaron (U+0161): X=351.5,Y=-2.0 (should be at baseline 0?)

	* scaron (U+0161): X=160.5,Y=723.0 (should be at cap-height 725?)

	* scaron (U+0161): X=343.5,Y=723.0 (should be at cap-height 725?)

	* uring (U+016F): X=256.0,Y=726.0 (should be at cap-height 725?)

	* Wcircumflex (U+0174): X=216.0,Y=941.0 (should be at ascender 940?)

	* Wcircumflex (U+0174): X=296.0,Y=941.0 (should be at ascender 940?)

	* zcaron (U+017E): X=169.5,Y=723.0 (should be at cap-height 725?)

	* zcaron (U+017E): X=352.5,Y=723.0 (should be at cap-height 725?)

	* caron (U+02C7): X=164.5,Y=723.0 (should be at cap-height 725?)

	* caron (U+02C7): X=347.5,Y=723.0 (should be at cap-height 725?)

	* ring (U+02DA): X=256.0,Y=726.0 (should be at cap-height 725?)

	* uni030A (U+030A): X=256.0,Y=726.0 (should be at cap-height 725?)

	* uni030C (U+030C): X=164.5,Y=723.0 (should be at cap-height 725?)

	* uni030C (U+030C): X=347.5,Y=723.0 (should be at cap-height 725?)

	* uni0635 (U+0635): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0635 (U+0635): X=-32.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=-32.0,Y=-261.0 (should be at descender -260?)

	* uni0654 (U+0654): X=177.0,Y=726.0 (should be at cap-height 725?)

	* uni0654 (U+0654): X=335.0,Y=726.0 (should be at cap-height 725?)

	* uni06A4 (U+06A4): X=312.0,Y=723.5 (should be at cap-height 725?)

	* uni06A4 (U+06A4): X=393.0,Y=723.5 (should be at cap-height 725?)

	* Wgrave (U+1E80): X=159.0,Y=941.0 (should be at ascender 940?)

	* Wgrave (U+1E80): X=235.0,Y=941.0 (should be at ascender 940?)

	* Wacute (U+1E82): X=285.0,Y=941.0 (should be at ascender 940?) 

	* And Wacute (U+1E82): X=361.0,Y=941.0 (should be at ascender 940?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* W (U+0057): L<<148.0,88.0>--<178.0,360.0>> -> L<<178.0,360.0>--<208.0,509.0>>

	* W (U+0057): L<<369.0,88.0>--<403.0,504.0>> -> L<<403.0,504.0>--<421.0,722.0>>

	* W (U+0057): L<<75.0,8.0>--<22.0,709.0>> -> L<<22.0,709.0>--<22.0,717.0>>

	* W (U+0057): L<<96.0,717.0>--<125.0,297.0>> -> L<<125.0,297.0>--<148.0,88.0>>

	* Wacute (U+1E82): L<<148.0,88.0>--<178.0,360.0>> -> L<<178.0,360.0>--<208.0,509.0>>

	* Wacute (U+1E82): L<<369.0,88.0>--<403.0,504.0>> -> L<<403.0,504.0>--<421.0,722.0>>

	* Wacute (U+1E82): L<<75.0,8.0>--<22.0,709.0>> -> L<<22.0,709.0>--<22.0,717.0>>

	* Wacute (U+1E82): L<<96.0,717.0>--<125.0,297.0>> -> L<<125.0,297.0>--<148.0,88.0>>

	* Wcircumflex (U+0174): L<<148.0,88.0>--<178.0,360.0>> -> L<<178.0,360.0>--<208.0,509.0>>

	* Wcircumflex (U+0174): L<<369.0,88.0>--<403.0,504.0>> -> L<<403.0,504.0>--<421.0,722.0>>

	* Wcircumflex (U+0174): L<<75.0,8.0>--<22.0,709.0>> -> L<<22.0,709.0>--<22.0,717.0>>

	* Wcircumflex (U+0174): L<<96.0,717.0>--<125.0,297.0>> -> L<<125.0,297.0>--<148.0,88.0>>

	* Wdieresis (U+1E84): L<<148.0,88.0>--<178.0,360.0>> -> L<<178.0,360.0>--<208.0,509.0>>

	* Wdieresis (U+1E84): L<<369.0,88.0>--<403.0,504.0>> -> L<<403.0,504.0>--<421.0,722.0>>

	* Wdieresis (U+1E84): L<<75.0,8.0>--<22.0,709.0>> -> L<<22.0,709.0>--<22.0,717.0>>

	* Wdieresis (U+1E84): L<<96.0,717.0>--<125.0,297.0>> -> L<<125.0,297.0>--<148.0,88.0>>

	* Wgrave (U+1E80): L<<148.0,88.0>--<178.0,360.0>> -> L<<178.0,360.0>--<208.0,509.0>>

	* Wgrave (U+1E80): L<<369.0,88.0>--<403.0,504.0>> -> L<<403.0,504.0>--<421.0,722.0>>

	* Wgrave (U+1E80): L<<75.0,8.0>--<22.0,709.0>> -> L<<22.0,709.0>--<22.0,717.0>>

	* Wgrave (U+1E80): L<<96.0,717.0>--<125.0,297.0>> -> L<<125.0,297.0>--<148.0,88.0>>

	* backslash (U+005C): L<<146.0,699.0>--<341.0,120.0>> -> L<<341.0,120.0>--<443.0,-205.0>>

	* backslash (U+005C): L<<366.0,-203.0>--<171.0,376.0>> -> L<<171.0,376.0>--<69.0,701.0>>

	* w (U+0077): L<<101.0,504.0>--<128.0,239.0>> -> L<<128.0,239.0>--<151.0,98.0>>

	* w (U+0077): L<<365.0,98.0>--<398.0,360.0>> -> L<<398.0,360.0>--<416.0,509.0>>

	* wacute (U+1E83): L<<101.0,504.0>--<128.0,239.0>> -> L<<128.0,239.0>--<151.0,98.0>>

	* wacute (U+1E83): L<<365.0,98.0>--<398.0,360.0>> -> L<<398.0,360.0>--<416.0,509.0>>

	* wcircumflex (U+0175): L<<101.0,504.0>--<128.0,239.0>> -> L<<128.0,239.0>--<151.0,98.0>>

	* wcircumflex (U+0175): L<<365.0,98.0>--<398.0,360.0>> -> L<<398.0,360.0>--<416.0,509.0>>

	* wdieresis (U+1E85): L<<101.0,504.0>--<128.0,239.0>> -> L<<128.0,239.0>--<151.0,98.0>>

	* wdieresis (U+1E85): L<<365.0,98.0>--<398.0,360.0>> -> L<<398.0,360.0>--<416.0,509.0>>

	* wgrave (U+1E81): L<<101.0,504.0>--<128.0,239.0>> -> L<<128.0,239.0>--<151.0,98.0>> 

	* And wgrave (U+1E81): L<<365.0,98.0>--<398.0,360.0>> -> L<<398.0,360.0>--<416.0,509.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* W (U+0057): L<<125.0,297.0>--<148.0,88.0>>/L<<148.0,88.0>--<178.0,360.0>> = 12.573955314650881

	* Wacute (U+1E82): L<<125.0,297.0>--<148.0,88.0>>/L<<148.0,88.0>--<178.0,360.0>> = 12.573955314650881

	* Wcircumflex (U+0174): L<<125.0,297.0>--<148.0,88.0>>/L<<148.0,88.0>--<178.0,360.0>> = 12.573955314650881

	* Wdieresis (U+1E84): L<<125.0,297.0>--<148.0,88.0>>/L<<148.0,88.0>--<178.0,360.0>> = 12.573955314650881 

	* And Wgrave (U+1E80): L<<125.0,297.0>--<148.0,88.0>>/L<<148.0,88.0>--<178.0,360.0>> = 12.573955314650881 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* newGlyph (U+00B5): L<<59.0,-208.0>--<58.0,513.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[11] HasubiMono-ExtraBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 976, but got 960 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 464, but got 360 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** Font is monospaced but 34 glyphs (5.46%) have a different width. You should check the widths of: ['AE', 'uni0136', 'Lcaron', 'uni0145', 'Eng', 'uni0156', 'aogonek', 'dcaron', 'dcroat', 'eogonek', 'uni0123', 'hbar', 'ij', 'lcaron', 'uni013C', 'lslash', 'uni0146', 'eng', 'uni0157', 'scedilla', 'uni0219', 'tcaron', 'uni021B', 'uogonek', 'uniFEF8', 'uniFEFA', 'uniFEF6', 'lam_alefWaslaar.fina', 'uni066B', 'uni066C', 'uni2074', 'guillemotleft', 'trademark', 'logicalnot'] [code: mono-outliers]
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

	- doublestrokear

	- gafsarkashabovear

	- gafsarkashcenterar

	- miniKehehar

	- threedotsdownabovear

	- threedotsdowncenterar

	- threedotsupbelowar

	- twodotsverticalabovear 

	- And twodotsverticalbelowar
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: colon	Contours detected: 1	Expected: 2

	- Glyph name: onequarter	Contours detected: 1	Expected: 3 or 4

	- Glyph name: onehalf	Contours detected: 1	Expected: 3

	- Glyph name: threequarters	Contours detected: 1	Expected: 3 or 4

	- Glyph name: Ccedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: aogonek	Contours detected: 0	Expected: 2

	- Glyph name: dcaron	Contours detected: 0	Expected: 3

	- Glyph name: dcroat	Contours detected: 0	Expected: 2

	- Glyph name: eogonek	Contours detected: 0	Expected: 2

	- Glyph name: uni0122	Contours detected: 1	Expected: 2

	- Glyph name: uni0123	Contours detected: 0	Expected: 3 or 4

	- Glyph name: hbar	Contours detected: 0	Expected: 1

	- Glyph name: Iogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: iogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: IJ	Contours detected: 0	Expected: 1 or 2

	- Glyph name: ij	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni0136	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni0137	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni013B	Contours detected: 0	Expected: 2

	- Glyph name: uni013C	Contours detected: 0	Expected: 2

	- Glyph name: Lcaron	Contours detected: 0	Expected: 2

	- Glyph name: lcaron	Contours detected: 0	Expected: 2

	- Glyph name: Lslash	Contours detected: 0	Expected: 1

	- Glyph name: lslash	Contours detected: 0	Expected: 1

	- Glyph name: uni0145	Contours detected: 0	Expected: 2

	- Glyph name: uni0146	Contours detected: 0	Expected: 2

	- Glyph name: Eng	Contours detected: 0	Expected: 1

	- Glyph name: eng	Contours detected: 0	Expected: 1

	- Glyph name: uni0156	Contours detected: 0	Expected: 3

	- Glyph name: uni0157	Contours detected: 0	Expected: 2

	- Glyph name: Scedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: scedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: tcaron	Contours detected: 0	Expected: 2

	- Glyph name: Uogonek	Contours detected: 0	Expected: 1

	- Glyph name: uogonek	Contours detected: 0	Expected: 1

	- Glyph name: uni0218	Contours detected: 0	Expected: 2

	- Glyph name: uni0219	Contours detected: 0	Expected: 2

	- Glyph name: uni021A	Contours detected: 0	Expected: 2

	- Glyph name: uni021B	Contours detected: 0	Expected: 2

	- Glyph name: ogonek	Contours detected: 0	Expected: 1

	- Glyph name: uni0312	Contours detected: 0	Expected: 1

	- Glyph name: uni0326	Contours detected: 0	Expected: 1

	- Glyph name: uni0327	Contours detected: 0	Expected: 1

	- Glyph name: uni0328	Contours detected: 0	Expected: 1

	- Glyph name: uni1E9E	Contours detected: 0	Expected: 1

	- Glyph name: trademark	Contours detected: 0	Expected: 2

	- Glyph name: Ccedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Eng	Contours detected: 0	Expected: 1

	- Glyph name: IJ	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Iogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Lcaron	Contours detected: 0	Expected: 2

	- Glyph name: Lslash	Contours detected: 0	Expected: 1

	- Glyph name: Uogonek	Contours detected: 0	Expected: 1

	- Glyph name: aogonek	Contours detected: 0	Expected: 2

	- Glyph name: colon	Contours detected: 1	Expected: 2

	- Glyph name: dcaron	Contours detected: 0	Expected: 3

	- Glyph name: dcroat	Contours detected: 0	Expected: 2

	- Glyph name: eng	Contours detected: 0	Expected: 1

	- Glyph name: eogonek	Contours detected: 0	Expected: 2

	- Glyph name: hbar	Contours detected: 0	Expected: 1

	- Glyph name: ij	Contours detected: 0	Expected: 3 or 4

	- Glyph name: iogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: lcaron	Contours detected: 0	Expected: 2

	- Glyph name: lslash	Contours detected: 0	Expected: 1

	- Glyph name: ogonek	Contours detected: 0	Expected: 1

	- Glyph name: onehalf	Contours detected: 1	Expected: 3

	- Glyph name: onequarter	Contours detected: 1	Expected: 3 or 4

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: tcaron	Contours detected: 0	Expected: 2

	- Glyph name: threequarters	Contours detected: 1	Expected: 3 or 4

	- Glyph name: trademark	Contours detected: 0	Expected: 2

	- Glyph name: uni0122	Contours detected: 1	Expected: 2

	- Glyph name: uni0123	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni0136	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni0137	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni013B	Contours detected: 0	Expected: 2

	- Glyph name: uni013C	Contours detected: 0	Expected: 2

	- Glyph name: uni0145	Contours detected: 0	Expected: 2

	- Glyph name: uni0146	Contours detected: 0	Expected: 2

	- Glyph name: uni0156	Contours detected: 0	Expected: 3

	- Glyph name: uni0157	Contours detected: 0	Expected: 2

	- Glyph name: uni0218	Contours detected: 0	Expected: 2

	- Glyph name: uni0219	Contours detected: 0	Expected: 2

	- Glyph name: uni021A	Contours detected: 0	Expected: 2

	- Glyph name: uni021B	Contours detected: 0	Expected: 2

	- Glyph name: uni0312	Contours detected: 0	Expected: 1

	- Glyph name: uni0326	Contours detected: 0	Expected: 1

	- Glyph name: uni0327	Contours detected: 0	Expected: 1

	- Glyph name: uni0328	Contours detected: 0	Expected: 1

	- Glyph name: uni1E9E	Contours detected: 0	Expected: 1 

	- And Glyph name: uogonek	Contours detected: 0	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* percent (U+0025): X=151.0,Y=714.0 (should be at cap-height 713?)

	* W (U+0057): X=487.0,Y=711.0 (should be at cap-height 713?)

	* a (U+0061): X=135.0,Y=0.5 (should be at baseline 0?)

	* a (U+0061): X=340.0,Y=510.0 (should be at x-height 512?)

	* b (U+0062): X=212.0,Y=514.0 (should be at x-height 512?)

	* b (U+0062): X=215.5,Y=-1.0 (should be at baseline 0?)

	* c (U+0063): X=354.5,Y=510.5 (should be at x-height 512?)

	* d (U+0064): X=303.5,Y=1.0 (should be at baseline 0?)

	* d (U+0064): X=308.5,Y=510.0 (should be at x-height 512?)

	* i (U+0069): X=190.5,Y=711.0 (should be at cap-height 713?)

	* i (U+0069): X=281.5,Y=711.0 (should be at cap-height 713?)

	* p (U+0070): X=195.0,Y=510.0 (should be at x-height 512?)

	* q (U+0071): X=317.5,Y=510.0 (should be at x-height 512?)

	* r (U+0072): X=282.5,Y=513.0 (should be at x-height 512?)

	* s (U+0073): X=172.5,Y=-1.5 (should be at baseline 0?)

	* s (U+0073): X=350.5,Y=-2.0 (should be at baseline 0?)

	* w (U+0077): X=483.0,Y=510.0 (should be at x-height 512?)

	* sterling (U+00A3): X=429.5,Y=712.0 (should be at cap-height 713?)

	* copyright (U+00A9): X=370.0,Y=-0.5 (should be at baseline 0?)

	* copyright (U+00A9): X=142.5,Y=-0.5 (should be at baseline 0?)

	* newGlyph (U+00B5): X=184.0,Y=-1.5 (should be at baseline 0?)

	* paragraph (U+00B6): X=86.0,Y=711.5 (should be at cap-height 713?)

	* agrave (U+00E0): X=135.0,Y=0.5 (should be at baseline 0?)

	* aacute (U+00E1): X=135.0,Y=0.5 (should be at baseline 0?)

	* acircumflex (U+00E2): X=135.0,Y=0.5 (should be at baseline 0?)

	* atilde (U+00E3): X=135.0,Y=0.5 (should be at baseline 0?)

	* adieresis (U+00E4): X=135.0,Y=0.5 (should be at baseline 0?)

	* aring (U+00E5): X=135.0,Y=0.5 (should be at baseline 0?)

	* ae (U+00E6): X=461.5,Y=1.5 (should be at baseline 0?)

	* ae (U+00E6): X=38.5,Y=0.5 (should be at baseline 0?)

	* eth (U+00F0): X=299.5,Y=1.0 (should be at baseline 0?)

	* thorn (U+00FE): X=212.5,Y=1.0 (should be at baseline 0?)

	* amacron (U+0101): X=135.0,Y=0.5 (should be at baseline 0?)

	* abreve (U+0103): X=135.0,Y=0.5 (should be at baseline 0?)

	* ccaron (U+010D): X=129.0,Y=714.0 (should be at cap-height 713?)

	* ccaron (U+010D): X=401.0,Y=714.0 (should be at cap-height 713?)

	* ecaron (U+011B): X=120.0,Y=714.0 (should be at cap-height 713?)

	* ecaron (U+011B): X=392.0,Y=714.0 (should be at cap-height 713?)

	* ncaron (U+0148): X=126.0,Y=714.0 (should be at cap-height 713?)

	* ncaron (U+0148): X=398.0,Y=714.0 (should be at cap-height 713?)

	* oe (U+0153): X=455.5,Y=1.5 (should be at baseline 0?)

	* oe (U+0153): X=221.0,Y=-2.0 (should be at baseline 0?)

	* rcaron (U+0159): X=135.0,Y=714.0 (should be at cap-height 713?)

	* rcaron (U+0159): X=407.0,Y=714.0 (should be at cap-height 713?)

	* sacute (U+015B): X=172.5,Y=-1.5 (should be at baseline 0?)

	* sacute (U+015B): X=350.5,Y=-2.0 (should be at baseline 0?)

	* scaron (U+0161): X=172.5,Y=-1.5 (should be at baseline 0?)

	* scaron (U+0161): X=350.5,Y=-2.0 (should be at baseline 0?)

	* scaron (U+0161): X=119.0,Y=714.0 (should be at cap-height 713?)

	* scaron (U+0161): X=391.0,Y=714.0 (should be at cap-height 713?)

	* Wcircumflex (U+0174): X=487.0,Y=711.0 (should be at cap-height 713?)

	* zcaron (U+017E): X=125.0,Y=714.0 (should be at cap-height 713?)

	* zcaron (U+017E): X=397.0,Y=714.0 (should be at cap-height 713?)

	* caron (U+02C7): X=120.0,Y=714.0 (should be at cap-height 713?)

	* caron (U+02C7): X=392.0,Y=714.0 (should be at cap-height 713?)

	* uni030C (U+030C): X=120.0,Y=714.0 (should be at cap-height 713?)

	* uni030C (U+030C): X=392.0,Y=714.0 (should be at cap-height 713?)

	* uni0635 (U+0635): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0635 (U+0635): X=-32.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=-32.0,Y=-261.0 (should be at descender -260?)

	* Wgrave (U+1E80): X=487.0,Y=711.0 (should be at cap-height 713?)

	* Wacute (U+1E82): X=487.0,Y=711.0 (should be at cap-height 713?)

	* Wdieresis (U+1E84): X=487.0,Y=711.0 (should be at cap-height 713?) 

	* And Euro (U+20AC): X=429.5,Y=712.0 (should be at cap-height 713?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* W (U+0057): L<<138.0,96.0>--<160.0,217.0>> -> L<<160.0,217.0>--<213.0,506.0>>

	* W (U+0057): L<<296.0,510.0>--<313.0,383.0>> -> L<<313.0,383.0>--<367.0,96.0>>

	* W (U+0057): L<<367.0,96.0>--<391.0,281.0>> -> L<<391.0,281.0>--<420.0,707.0>>

	* W (U+0057): L<<75.0,8.0>--<19.0,697.0>> -> L<<19.0,697.0>--<19.0,705.0>>

	* W (U+0057): L<<94.0,705.0>--<107.0,514.0>> -> L<<107.0,514.0>--<138.0,96.0>>

	* Wacute (U+1E82): L<<138.0,96.0>--<160.0,217.0>> -> L<<160.0,217.0>--<213.0,506.0>>

	* Wacute (U+1E82): L<<296.0,510.0>--<313.0,383.0>> -> L<<313.0,383.0>--<367.0,96.0>>

	* Wacute (U+1E82): L<<367.0,96.0>--<391.0,281.0>> -> L<<391.0,281.0>--<420.0,707.0>>

	* Wacute (U+1E82): L<<75.0,8.0>--<19.0,697.0>> -> L<<19.0,697.0>--<19.0,705.0>>

	* Wacute (U+1E82): L<<94.0,705.0>--<107.0,514.0>> -> L<<107.0,514.0>--<138.0,96.0>>

	* Wcircumflex (U+0174): L<<138.0,96.0>--<160.0,217.0>> -> L<<160.0,217.0>--<213.0,506.0>>

	* Wcircumflex (U+0174): L<<296.0,510.0>--<313.0,383.0>> -> L<<313.0,383.0>--<367.0,96.0>>

	* Wcircumflex (U+0174): L<<367.0,96.0>--<391.0,281.0>> -> L<<391.0,281.0>--<420.0,707.0>>

	* Wcircumflex (U+0174): L<<75.0,8.0>--<19.0,697.0>> -> L<<19.0,697.0>--<19.0,705.0>>

	* Wcircumflex (U+0174): L<<94.0,705.0>--<107.0,514.0>> -> L<<107.0,514.0>--<138.0,96.0>>

	* Wdieresis (U+1E84): L<<138.0,96.0>--<160.0,217.0>> -> L<<160.0,217.0>--<213.0,506.0>>

	* Wdieresis (U+1E84): L<<296.0,510.0>--<313.0,383.0>> -> L<<313.0,383.0>--<367.0,96.0>>

	* Wdieresis (U+1E84): L<<367.0,96.0>--<391.0,281.0>> -> L<<391.0,281.0>--<420.0,707.0>>

	* Wdieresis (U+1E84): L<<75.0,8.0>--<19.0,697.0>> -> L<<19.0,697.0>--<19.0,705.0>>

	* Wdieresis (U+1E84): L<<94.0,705.0>--<107.0,514.0>> -> L<<107.0,514.0>--<138.0,96.0>>

	* Wgrave (U+1E80): L<<138.0,96.0>--<160.0,217.0>> -> L<<160.0,217.0>--<213.0,506.0>>

	* Wgrave (U+1E80): L<<296.0,510.0>--<313.0,383.0>> -> L<<313.0,383.0>--<367.0,96.0>>

	* Wgrave (U+1E80): L<<367.0,96.0>--<391.0,281.0>> -> L<<391.0,281.0>--<420.0,707.0>>

	* Wgrave (U+1E80): L<<75.0,8.0>--<19.0,697.0>> -> L<<19.0,697.0>--<19.0,705.0>>

	* Wgrave (U+1E80): L<<94.0,705.0>--<107.0,514.0>> -> L<<107.0,514.0>--<138.0,96.0>>

	* backslash (U+005C): L<<143.0,702.0>--<234.0,440.0>> -> L<<234.0,440.0>--<446.0,-202.0>>

	* backslash (U+005C): L<<369.0,-206.0>--<278.0,56.0>> -> L<<278.0,56.0>--<66.0,698.0>>

	* w (U+0077): L<<139.0,100.0>--<166.0,180.0>> -> L<<166.0,180.0>--<218.0,333.0>>

	* w (U+0077): L<<96.0,504.0>--<109.0,382.0>> -> L<<109.0,382.0>--<139.0,100.0>>

	* wacute (U+1E83): L<<139.0,100.0>--<166.0,180.0>> -> L<<166.0,180.0>--<218.0,333.0>>

	* wacute (U+1E83): L<<96.0,504.0>--<109.0,382.0>> -> L<<109.0,382.0>--<139.0,100.0>>

	* wcircumflex (U+0175): L<<139.0,100.0>--<166.0,180.0>> -> L<<166.0,180.0>--<218.0,333.0>>

	* wcircumflex (U+0175): L<<96.0,504.0>--<109.0,382.0>> -> L<<109.0,382.0>--<139.0,100.0>>

	* wdieresis (U+1E85): L<<139.0,100.0>--<166.0,180.0>> -> L<<166.0,180.0>--<218.0,333.0>>

	* wdieresis (U+1E85): L<<96.0,504.0>--<109.0,382.0>> -> L<<109.0,382.0>--<139.0,100.0>>

	* wgrave (U+1E81): L<<139.0,100.0>--<166.0,180.0>> -> L<<166.0,180.0>--<218.0,333.0>> 

	* And wgrave (U+1E81): L<<96.0,504.0>--<109.0,382.0>> -> L<<109.0,382.0>--<139.0,100.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* newGlyph (U+00B5): L<<59.0,-208.0>--<58.0,513.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[10] HasubiMono-Black.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 976, but got 960 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 464, but got 360 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** Font is monospaced but 20 glyphs (3.21%) have a different width. You should check the widths of: ['AE', 'uni0136', 'uni0156', 'aogonek', 'eogonek', 'hbar', 'ij', 'uni0157', 'scedilla', 'uni0219', 'tcaron', 'uni021B', 'uniFEF8', 'uniFEFA', 'uniFEF6', 'lam_alefWaslaar.fina', 'uni066B', 'uni066C', 'guillemotleft', 'logicalnot'] [code: mono-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- doublestrokear

	- gafsarkashabovear

	- gafsarkashcenterar

	- miniKehehar

	- threedotsdownabovear

	- threedotsdowncenterar

	- threedotsupbelowar

	- twodotsverticalabovear 

	- And twodotsverticalbelowar
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: onequarter	Contours detected: 1	Expected: 3 or 4

	- Glyph name: onehalf	Contours detected: 1	Expected: 3

	- Glyph name: threequarters	Contours detected: 1	Expected: 3 or 4

	- Glyph name: Ccedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: aogonek	Contours detected: 0	Expected: 2

	- Glyph name: dcaron	Contours detected: 0	Expected: 3

	- Glyph name: dcroat	Contours detected: 0	Expected: 2

	- Glyph name: eogonek	Contours detected: 0	Expected: 2

	- Glyph name: uni0122	Contours detected: 1	Expected: 2

	- Glyph name: uni0123	Contours detected: 0	Expected: 3 or 4

	- Glyph name: hbar	Contours detected: 0	Expected: 1

	- Glyph name: Iogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: iogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: IJ	Contours detected: 0	Expected: 1 or 2

	- Glyph name: ij	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni0136	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni0137	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni013B	Contours detected: 0	Expected: 2

	- Glyph name: uni013C	Contours detected: 0	Expected: 2

	- Glyph name: Lcaron	Contours detected: 0	Expected: 2

	- Glyph name: lcaron	Contours detected: 0	Expected: 2

	- Glyph name: Lslash	Contours detected: 0	Expected: 1

	- Glyph name: lslash	Contours detected: 0	Expected: 1

	- Glyph name: uni0145	Contours detected: 0	Expected: 2

	- Glyph name: uni0146	Contours detected: 0	Expected: 2

	- Glyph name: Eng	Contours detected: 0	Expected: 1

	- Glyph name: eng	Contours detected: 0	Expected: 1

	- Glyph name: uni0156	Contours detected: 0	Expected: 3

	- Glyph name: uni0157	Contours detected: 0	Expected: 2

	- Glyph name: Scedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: scedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: tcaron	Contours detected: 0	Expected: 2

	- Glyph name: Uogonek	Contours detected: 0	Expected: 1

	- Glyph name: uogonek	Contours detected: 0	Expected: 1

	- Glyph name: uni0218	Contours detected: 0	Expected: 2

	- Glyph name: uni0219	Contours detected: 0	Expected: 2

	- Glyph name: uni021A	Contours detected: 0	Expected: 2

	- Glyph name: uni021B	Contours detected: 0	Expected: 2

	- Glyph name: ogonek	Contours detected: 0	Expected: 1

	- Glyph name: uni0312	Contours detected: 0	Expected: 1

	- Glyph name: uni0326	Contours detected: 0	Expected: 1

	- Glyph name: uni0327	Contours detected: 0	Expected: 1

	- Glyph name: uni0328	Contours detected: 0	Expected: 1

	- Glyph name: uni1E9E	Contours detected: 0	Expected: 1

	- Glyph name: trademark	Contours detected: 0	Expected: 2

	- Glyph name: Ccedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Eng	Contours detected: 0	Expected: 1

	- Glyph name: IJ	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Iogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Lcaron	Contours detected: 0	Expected: 2

	- Glyph name: Lslash	Contours detected: 0	Expected: 1

	- Glyph name: Uogonek	Contours detected: 0	Expected: 1

	- Glyph name: aogonek	Contours detected: 0	Expected: 2

	- Glyph name: dcaron	Contours detected: 0	Expected: 3

	- Glyph name: dcroat	Contours detected: 0	Expected: 2

	- Glyph name: eng	Contours detected: 0	Expected: 1

	- Glyph name: eogonek	Contours detected: 0	Expected: 2

	- Glyph name: hbar	Contours detected: 0	Expected: 1

	- Glyph name: ij	Contours detected: 0	Expected: 3 or 4

	- Glyph name: iogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: lcaron	Contours detected: 0	Expected: 2

	- Glyph name: lslash	Contours detected: 0	Expected: 1

	- Glyph name: ogonek	Contours detected: 0	Expected: 1

	- Glyph name: onehalf	Contours detected: 1	Expected: 3

	- Glyph name: onequarter	Contours detected: 1	Expected: 3 or 4

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: tcaron	Contours detected: 0	Expected: 2

	- Glyph name: threequarters	Contours detected: 1	Expected: 3 or 4

	- Glyph name: trademark	Contours detected: 0	Expected: 2

	- Glyph name: uni0122	Contours detected: 1	Expected: 2

	- Glyph name: uni0123	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni0136	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni0137	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni013B	Contours detected: 0	Expected: 2

	- Glyph name: uni013C	Contours detected: 0	Expected: 2

	- Glyph name: uni0145	Contours detected: 0	Expected: 2

	- Glyph name: uni0146	Contours detected: 0	Expected: 2

	- Glyph name: uni0156	Contours detected: 0	Expected: 3

	- Glyph name: uni0157	Contours detected: 0	Expected: 2

	- Glyph name: uni0218	Contours detected: 0	Expected: 2

	- Glyph name: uni0219	Contours detected: 0	Expected: 2

	- Glyph name: uni021A	Contours detected: 0	Expected: 2

	- Glyph name: uni021B	Contours detected: 0	Expected: 2

	- Glyph name: uni0312	Contours detected: 0	Expected: 1

	- Glyph name: uni0326	Contours detected: 0	Expected: 1

	- Glyph name: uni0327	Contours detected: 0	Expected: 1

	- Glyph name: uni0328	Contours detected: 0	Expected: 1

	- Glyph name: uni1E9E	Contours detected: 0	Expected: 1 

	- And Glyph name: uogonek	Contours detected: 0	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* a (U+0061): X=135.0,Y=0.5 (should be at baseline 0?)

	* a (U+0061): X=340.5,Y=510.0 (should be at x-height 512?)

	* b (U+0062): X=216.5,Y=-2.0 (should be at baseline 0?)

	* c (U+0063): X=357.5,Y=510.5 (should be at x-height 512?)

	* d (U+0064): X=303.5,Y=1.0 (should be at baseline 0?)

	* d (U+0064): X=308.5,Y=510.0 (should be at x-height 512?)

	* j (U+006A): X=242.5,Y=702.0 (should be at cap-height 704?)

	* j (U+006A): X=333.5,Y=702.0 (should be at cap-height 704?)

	* m (U+006D): X=166.0,Y=510.5 (should be at x-height 512?)

	* m (U+006D): X=257.0,Y=510.5 (should be at x-height 512?)

	* m (U+006D): X=321.0,Y=510.5 (should be at x-height 512?)

	* p (U+0070): X=195.0,Y=510.0 (should be at x-height 512?)

	* q (U+0071): X=317.5,Y=510.0 (should be at x-height 512?)

	* r (U+0072): X=282.5,Y=513.0 (should be at x-height 512?)

	* s (U+0073): X=177.5,Y=-2.0 (should be at baseline 0?)

	* copyright (U+00A9): X=370.0,Y=-0.5 (should be at baseline 0?)

	* copyright (U+00A9): X=142.5,Y=-0.5 (should be at baseline 0?)

	* newGlyph (U+00B5): X=184.0,Y=-1.5 (should be at baseline 0?)

	* agrave (U+00E0): X=135.0,Y=0.5 (should be at baseline 0?)

	* aacute (U+00E1): X=135.0,Y=0.5 (should be at baseline 0?)

	* acircumflex (U+00E2): X=135.0,Y=0.5 (should be at baseline 0?)

	* atilde (U+00E3): X=135.0,Y=0.5 (should be at baseline 0?)

	* adieresis (U+00E4): X=135.0,Y=0.5 (should be at baseline 0?)

	* aring (U+00E5): X=135.0,Y=0.5 (should be at baseline 0?)

	* aring (U+00E5): X=193.5,Y=705.0 (should be at cap-height 704?)

	* aring (U+00E5): X=306.5,Y=705.0 (should be at cap-height 704?)

	* ae (U+00E6): X=461.5,Y=1.5 (should be at baseline 0?)

	* ae (U+00E6): X=38.5,Y=0.5 (should be at baseline 0?)

	* eth (U+00F0): X=299.5,Y=1.0 (should be at baseline 0?)

	* thorn (U+00FE): X=212.5,Y=1.0 (should be at baseline 0?)

	* amacron (U+0101): X=135.0,Y=0.5 (should be at baseline 0?)

	* abreve (U+0103): X=135.0,Y=0.5 (should be at baseline 0?)

	* abreve (U+0103): X=135.0,Y=706.0 (should be at cap-height 704?)

	* abreve (U+0103): X=188.0,Y=706.0 (should be at cap-height 704?)

	* abreve (U+0103): X=302.0,Y=706.0 (should be at cap-height 704?)

	* abreve (U+0103): X=355.0,Y=706.0 (should be at cap-height 704?)

	* cdotaccent (U+010B): X=223.0,Y=703.5 (should be at cap-height 704?)

	* cdotaccent (U+010B): X=302.5,Y=703.5 (should be at cap-height 704?)

	* edotaccent (U+0117): X=216.0,Y=703.5 (should be at cap-height 704?)

	* edotaccent (U+0117): X=295.5,Y=703.5 (should be at cap-height 704?)

	* gbreve (U+011F): X=151.0,Y=706.0 (should be at cap-height 704?)

	* gbreve (U+011F): X=204.0,Y=706.0 (should be at cap-height 704?)

	* gbreve (U+011F): X=318.0,Y=706.0 (should be at cap-height 704?)

	* gbreve (U+011F): X=371.0,Y=706.0 (should be at cap-height 704?)

	* gdotaccent (U+0121): X=226.0,Y=703.5 (should be at cap-height 704?)

	* gdotaccent (U+0121): X=305.5,Y=703.5 (should be at cap-height 704?)

	* ohungarumlaut (U+0151): X=302.0,Y=706.0 (should be at cap-height 704?)

	* ohungarumlaut (U+0151): X=394.0,Y=706.0 (should be at cap-height 704?)

	* ohungarumlaut (U+0151): X=159.0,Y=706.0 (should be at cap-height 704?)

	* ohungarumlaut (U+0151): X=251.0,Y=706.0 (should be at cap-height 704?)

	* oe (U+0153): X=455.5,Y=1.5 (should be at baseline 0?)

	* oe (U+0153): X=221.0,Y=-2.0 (should be at baseline 0?)

	* sacute (U+015B): X=177.5,Y=-2.0 (should be at baseline 0?)

	* scaron (U+0161): X=177.5,Y=-2.0 (should be at baseline 0?)

	* ubreve (U+016D): X=146.0,Y=706.0 (should be at cap-height 704?)

	* ubreve (U+016D): X=199.0,Y=706.0 (should be at cap-height 704?)

	* ubreve (U+016D): X=313.0,Y=706.0 (should be at cap-height 704?)

	* ubreve (U+016D): X=366.0,Y=706.0 (should be at cap-height 704?)

	* uring (U+016F): X=199.5,Y=705.0 (should be at cap-height 704?)

	* uring (U+016F): X=312.5,Y=705.0 (should be at cap-height 704?)

	* uhungarumlaut (U+0171): X=302.0,Y=706.0 (should be at cap-height 704?)

	* uhungarumlaut (U+0171): X=394.0,Y=706.0 (should be at cap-height 704?)

	* uhungarumlaut (U+0171): X=159.0,Y=706.0 (should be at cap-height 704?)

	* uhungarumlaut (U+0171): X=251.0,Y=706.0 (should be at cap-height 704?)

	* zdotaccent (U+017C): X=219.0,Y=703.5 (should be at cap-height 704?)

	* zdotaccent (U+017C): X=298.5,Y=703.5 (should be at cap-height 704?)

	* breve (U+02D8): X=146.0,Y=706.0 (should be at cap-height 704?)

	* breve (U+02D8): X=199.0,Y=706.0 (should be at cap-height 704?)

	* breve (U+02D8): X=313.0,Y=706.0 (should be at cap-height 704?)

	* breve (U+02D8): X=366.0,Y=706.0 (should be at cap-height 704?)

	* dotaccent (U+02D9): X=216.0,Y=703.5 (should be at cap-height 704?)

	* dotaccent (U+02D9): X=295.5,Y=703.5 (should be at cap-height 704?)

	* ring (U+02DA): X=199.5,Y=705.0 (should be at cap-height 704?)

	* ring (U+02DA): X=312.5,Y=705.0 (should be at cap-height 704?)

	* hungarumlaut (U+02DD): X=302.0,Y=706.0 (should be at cap-height 704?)

	* hungarumlaut (U+02DD): X=394.0,Y=706.0 (should be at cap-height 704?)

	* hungarumlaut (U+02DD): X=159.0,Y=706.0 (should be at cap-height 704?)

	* hungarumlaut (U+02DD): X=251.0,Y=706.0 (should be at cap-height 704?)

	* uni0306 (U+0306): X=146.0,Y=706.0 (should be at cap-height 704?)

	* uni0306 (U+0306): X=199.0,Y=706.0 (should be at cap-height 704?)

	* uni0306 (U+0306): X=313.0,Y=706.0 (should be at cap-height 704?)

	* uni0306 (U+0306): X=366.0,Y=706.0 (should be at cap-height 704?)

	* uni0307 (U+0307): X=216.0,Y=703.5 (should be at cap-height 704?)

	* uni0307 (U+0307): X=295.5,Y=703.5 (should be at cap-height 704?)

	* uni030A (U+030A): X=199.5,Y=705.0 (should be at cap-height 704?)

	* uni030A (U+030A): X=312.5,Y=705.0 (should be at cap-height 704?)

	* uni030B (U+030B): X=302.0,Y=706.0 (should be at cap-height 704?)

	* uni030B (U+030B): X=394.0,Y=706.0 (should be at cap-height 704?)

	* uni030B (U+030B): X=159.0,Y=706.0 (should be at cap-height 704?)

	* uni030B (U+030B): X=251.0,Y=706.0 (should be at cap-height 704?)

	* uni0635 (U+0635): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0635 (U+0635): X=-32.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=-32.0,Y=-261.0 (should be at descender -260?)

	* uni064A (U+064A): X=116.0,Y=-262.0 (should be at descender -260?)

	* uni064A (U+064A): X=260.0,Y=-262.0 (should be at descender -260?)

	* uni064A (U+064A): X=292.0,Y=-262.0 (should be at descender -260?) 

	* And uni064A (U+064A): X=436.0,Y=-262.0 (should be at descender -260?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* W (U+0057): L<<75.0,8.0>--<17.0,688.0>> -> L<<17.0,688.0>--<17.0,696.0>>

	* W (U+0057): L<<93.0,696.0>--<93.0,688.0>> -> L<<93.0,688.0>--<130.0,102.0>>

	* Wacute (U+1E82): L<<75.0,8.0>--<17.0,688.0>> -> L<<17.0,688.0>--<17.0,696.0>>

	* Wacute (U+1E82): L<<93.0,696.0>--<93.0,688.0>> -> L<<93.0,688.0>--<130.0,102.0>>

	* Wcircumflex (U+0174): L<<75.0,8.0>--<17.0,688.0>> -> L<<17.0,688.0>--<17.0,696.0>>

	* Wcircumflex (U+0174): L<<93.0,696.0>--<93.0,688.0>> -> L<<93.0,688.0>--<130.0,102.0>>

	* Wdieresis (U+1E84): L<<75.0,8.0>--<17.0,688.0>> -> L<<17.0,688.0>--<17.0,696.0>>

	* Wdieresis (U+1E84): L<<93.0,696.0>--<93.0,688.0>> -> L<<93.0,688.0>--<130.0,102.0>>

	* Wgrave (U+1E80): L<<75.0,8.0>--<17.0,688.0>> -> L<<17.0,688.0>--<17.0,696.0>>

	* Wgrave (U+1E80): L<<93.0,696.0>--<93.0,688.0>> -> L<<93.0,688.0>--<130.0,102.0>>

	* w (U+0077): L<<93.0,504.0>--<93.0,496.0>> -> L<<93.0,496.0>--<130.0,102.0>>

	* wacute (U+1E83): L<<93.0,504.0>--<93.0,496.0>> -> L<<93.0,496.0>--<130.0,102.0>>

	* wcircumflex (U+0175): L<<93.0,504.0>--<93.0,496.0>> -> L<<93.0,496.0>--<130.0,102.0>>

	* wdieresis (U+1E85): L<<93.0,504.0>--<93.0,496.0>> -> L<<93.0,496.0>--<130.0,102.0>> 

	* And wgrave (U+1E81): L<<93.0,504.0>--<93.0,496.0>> -> L<<93.0,496.0>--<130.0,102.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* newGlyph (U+00B5): L<<59.0,-208.0>--<58.0,513.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[10] HasubiMono-Medium.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 976, but got 960 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 464, but got 360 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** Font is monospaced but 34 glyphs (5.46%) have a different width. You should check the widths of: ['AE', 'uni0136', 'Lcaron', 'uni0145', 'Eng', 'uni0156', 'aogonek', 'dcaron', 'dcroat', 'eogonek', 'uni0123', 'hbar', 'ij', 'lcaron', 'uni013C', 'lslash', 'uni0146', 'eng', 'uni0157', 'scedilla', 'uni0219', 'tcaron', 'uni021B', 'uogonek', 'uniFEF8', 'uniFEFA', 'uniFEF6', 'lam_alefWaslaar.fina', 'uni066B', 'uni066C', 'uni2074', 'guillemotleft', 'trademark', 'logicalnot'] [code: mono-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- doublestrokear

	- gafsarkashabovear

	- gafsarkashcenterar

	- miniKehehar

	- threedotsdownabovear

	- threedotsdowncenterar

	- threedotsupbelowar

	- twodotsverticalabovear 

	- And twodotsverticalbelowar
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: onequarter	Contours detected: 1	Expected: 3 or 4

	- Glyph name: onehalf	Contours detected: 1	Expected: 3

	- Glyph name: threequarters	Contours detected: 1	Expected: 3 or 4

	- Glyph name: Ccedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: aogonek	Contours detected: 0	Expected: 2

	- Glyph name: dcaron	Contours detected: 0	Expected: 3

	- Glyph name: dcroat	Contours detected: 0	Expected: 2

	- Glyph name: eogonek	Contours detected: 0	Expected: 2

	- Glyph name: uni0122	Contours detected: 1	Expected: 2

	- Glyph name: uni0123	Contours detected: 0	Expected: 3 or 4

	- Glyph name: hbar	Contours detected: 0	Expected: 1

	- Glyph name: Iogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: iogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: IJ	Contours detected: 0	Expected: 1 or 2

	- Glyph name: ij	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni0136	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni0137	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni013B	Contours detected: 0	Expected: 2

	- Glyph name: uni013C	Contours detected: 0	Expected: 2

	- Glyph name: Lcaron	Contours detected: 0	Expected: 2

	- Glyph name: lcaron	Contours detected: 0	Expected: 2

	- Glyph name: Lslash	Contours detected: 0	Expected: 1

	- Glyph name: lslash	Contours detected: 0	Expected: 1

	- Glyph name: uni0145	Contours detected: 0	Expected: 2

	- Glyph name: uni0146	Contours detected: 0	Expected: 2

	- Glyph name: Eng	Contours detected: 0	Expected: 1

	- Glyph name: eng	Contours detected: 0	Expected: 1

	- Glyph name: uni0156	Contours detected: 0	Expected: 3

	- Glyph name: uni0157	Contours detected: 0	Expected: 2

	- Glyph name: Scedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: scedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: tcaron	Contours detected: 0	Expected: 2

	- Glyph name: Uogonek	Contours detected: 0	Expected: 1

	- Glyph name: uogonek	Contours detected: 0	Expected: 1

	- Glyph name: uni0218	Contours detected: 0	Expected: 2

	- Glyph name: uni0219	Contours detected: 0	Expected: 2

	- Glyph name: uni021A	Contours detected: 0	Expected: 2

	- Glyph name: uni021B	Contours detected: 0	Expected: 2

	- Glyph name: ogonek	Contours detected: 0	Expected: 1

	- Glyph name: uni0312	Contours detected: 0	Expected: 1

	- Glyph name: uni0326	Contours detected: 0	Expected: 1

	- Glyph name: uni0327	Contours detected: 0	Expected: 1

	- Glyph name: uni0328	Contours detected: 0	Expected: 1

	- Glyph name: uni1E9E	Contours detected: 0	Expected: 1

	- Glyph name: trademark	Contours detected: 0	Expected: 2

	- Glyph name: Ccedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Eng	Contours detected: 0	Expected: 1

	- Glyph name: IJ	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Iogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Lcaron	Contours detected: 0	Expected: 2

	- Glyph name: Lslash	Contours detected: 0	Expected: 1

	- Glyph name: Uogonek	Contours detected: 0	Expected: 1

	- Glyph name: aogonek	Contours detected: 0	Expected: 2

	- Glyph name: dcaron	Contours detected: 0	Expected: 3

	- Glyph name: dcroat	Contours detected: 0	Expected: 2

	- Glyph name: eng	Contours detected: 0	Expected: 1

	- Glyph name: eogonek	Contours detected: 0	Expected: 2

	- Glyph name: hbar	Contours detected: 0	Expected: 1

	- Glyph name: ij	Contours detected: 0	Expected: 3 or 4

	- Glyph name: iogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: lcaron	Contours detected: 0	Expected: 2

	- Glyph name: lslash	Contours detected: 0	Expected: 1

	- Glyph name: ogonek	Contours detected: 0	Expected: 1

	- Glyph name: onehalf	Contours detected: 1	Expected: 3

	- Glyph name: onequarter	Contours detected: 1	Expected: 3 or 4

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: tcaron	Contours detected: 0	Expected: 2

	- Glyph name: threequarters	Contours detected: 1	Expected: 3 or 4

	- Glyph name: trademark	Contours detected: 0	Expected: 2

	- Glyph name: uni0122	Contours detected: 1	Expected: 2

	- Glyph name: uni0123	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni0136	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni0137	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni013B	Contours detected: 0	Expected: 2

	- Glyph name: uni013C	Contours detected: 0	Expected: 2

	- Glyph name: uni0145	Contours detected: 0	Expected: 2

	- Glyph name: uni0146	Contours detected: 0	Expected: 2

	- Glyph name: uni0156	Contours detected: 0	Expected: 3

	- Glyph name: uni0157	Contours detected: 0	Expected: 2

	- Glyph name: uni0218	Contours detected: 0	Expected: 2

	- Glyph name: uni0219	Contours detected: 0	Expected: 2

	- Glyph name: uni021A	Contours detected: 0	Expected: 2

	- Glyph name: uni021B	Contours detected: 0	Expected: 2

	- Glyph name: uni0312	Contours detected: 0	Expected: 1

	- Glyph name: uni0326	Contours detected: 0	Expected: 1

	- Glyph name: uni0327	Contours detected: 0	Expected: 1

	- Glyph name: uni0328	Contours detected: 0	Expected: 1

	- Glyph name: uni1E9E	Contours detected: 0	Expected: 1 

	- And Glyph name: uogonek	Contours detected: 0	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* dollar (U+0024): X=381.5,Y=729.5 (should be at cap-height 730?)

	* W (U+0057): X=421.0,Y=729.0 (should be at cap-height 730?)

	* a (U+0061): X=135.0,Y=0.5 (should be at baseline 0?)

	* a (U+0061): X=340.0,Y=510.0 (should be at x-height 512?)

	* d (U+0064): X=303.5,Y=1.0 (should be at baseline 0?)

	* d (U+0064): X=308.5,Y=510.0 (should be at x-height 512?)

	* d (U+0064): X=360.0,Y=728.0 (should be at cap-height 730?)

	* d (U+0064): X=432.0,Y=728.0 (should be at cap-height 730?)

	* p (U+0070): X=195.0,Y=510.0 (should be at x-height 512?)

	* q (U+0071): X=317.5,Y=510.0 (should be at x-height 512?)

	* r (U+0072): X=282.5,Y=513.0 (should be at x-height 512?)

	* s (U+0073): X=351.5,Y=-2.0 (should be at baseline 0?)

	* w (U+0077): X=416.0,Y=511.0 (should be at x-height 512?)

	* braceleft (U+007B): X=187.5,Y=729.0 (should be at cap-height 730?)

	* braceright (U+007D): X=322.5,Y=729.0 (should be at cap-height 730?)

	* copyright (U+00A9): X=370.0,Y=-0.5 (should be at baseline 0?)

	* copyright (U+00A9): X=142.5,Y=-0.5 (should be at baseline 0?)

	* newGlyph (U+00B5): X=184.0,Y=-1.5 (should be at baseline 0?)

	* agrave (U+00E0): X=135.0,Y=0.5 (should be at baseline 0?)

	* aacute (U+00E1): X=135.0,Y=0.5 (should be at baseline 0?)

	* acircumflex (U+00E2): X=135.0,Y=0.5 (should be at baseline 0?)

	* atilde (U+00E3): X=135.0,Y=0.5 (should be at baseline 0?)

	* adieresis (U+00E4): X=135.0,Y=0.5 (should be at baseline 0?)

	* aring (U+00E5): X=135.0,Y=0.5 (should be at baseline 0?)

	* ae (U+00E6): X=461.5,Y=1.5 (should be at baseline 0?)

	* ae (U+00E6): X=38.5,Y=0.5 (should be at baseline 0?)

	* eth (U+00F0): X=299.5,Y=1.0 (should be at baseline 0?)

	* thorn (U+00FE): X=212.5,Y=1.0 (should be at baseline 0?)

	* amacron (U+0101): X=135.0,Y=0.5 (should be at baseline 0?)

	* abreve (U+0103): X=135.0,Y=0.5 (should be at baseline 0?)

	* lacute (U+013A): X=260.0,Y=938.0 (should be at ascender 940?)

	* lacute (U+013A): X=352.0,Y=938.0 (should be at ascender 940?)

	* oe (U+0153): X=455.5,Y=1.5 (should be at baseline 0?)

	* oe (U+0153): X=221.0,Y=-2.0 (should be at baseline 0?)

	* sacute (U+015B): X=351.5,Y=-2.0 (should be at baseline 0?)

	* scaron (U+0161): X=351.5,Y=-2.0 (should be at baseline 0?)

	* Wcircumflex (U+0174): X=421.0,Y=729.0 (should be at cap-height 730?)

	* Wcircumflex (U+0174): X=208.0,Y=938.0 (should be at ascender 940?)

	* Wcircumflex (U+0174): X=304.0,Y=938.0 (should be at ascender 940?)

	* uni0635 (U+0635): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0635 (U+0635): X=-32.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=-32.0,Y=-261.0 (should be at descender -260?)

	* uni064A (U+064A): X=149.5,Y=-259.5 (should be at descender -260?)

	* uni064A (U+064A): X=233.0,Y=-259.5 (should be at descender -260?)

	* uni064A (U+064A): X=319.0,Y=-259.5 (should be at descender -260?)

	* uni064A (U+064A): X=402.0,Y=-259.5 (should be at descender -260?)

	* uni06A4 (U+06A4): X=312.5,Y=730.5 (should be at cap-height 730?)

	* uni06A4 (U+06A4): X=392.5,Y=730.5 (should be at cap-height 730?)

	* Wgrave (U+1E80): X=421.0,Y=729.0 (should be at cap-height 730?)

	* Wgrave (U+1E80): X=151.0,Y=938.0 (should be at ascender 940?)

	* Wgrave (U+1E80): X=243.0,Y=938.0 (should be at ascender 940?)

	* Wacute (U+1E82): X=421.0,Y=729.0 (should be at cap-height 730?)

	* Wacute (U+1E82): X=277.0,Y=938.0 (should be at ascender 940?)

	* Wacute (U+1E82): X=369.0,Y=938.0 (should be at ascender 940?) 

	* And Wdieresis (U+1E84): X=421.0,Y=729.0 (should be at cap-height 730?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* W (U+0057): L<<369.0,84.0>--<408.0,616.0>> -> L<<408.0,616.0>--<421.0,729.0>>

	* W (U+0057): L<<75.0,8.0>--<23.0,714.0>> -> L<<23.0,714.0>--<23.0,722.0>>

	* Wacute (U+1E82): L<<369.0,84.0>--<408.0,616.0>> -> L<<408.0,616.0>--<421.0,729.0>>

	* Wacute (U+1E82): L<<75.0,8.0>--<23.0,714.0>> -> L<<23.0,714.0>--<23.0,722.0>>

	* Wcircumflex (U+0174): L<<369.0,84.0>--<408.0,616.0>> -> L<<408.0,616.0>--<421.0,729.0>>

	* Wcircumflex (U+0174): L<<75.0,8.0>--<23.0,714.0>> -> L<<23.0,714.0>--<23.0,722.0>>

	* Wdieresis (U+1E84): L<<369.0,84.0>--<408.0,616.0>> -> L<<408.0,616.0>--<421.0,729.0>>

	* Wdieresis (U+1E84): L<<75.0,8.0>--<23.0,714.0>> -> L<<23.0,714.0>--<23.0,722.0>>

	* Wgrave (U+1E80): L<<369.0,84.0>--<408.0,616.0>> -> L<<408.0,616.0>--<421.0,729.0>>

	* Wgrave (U+1E80): L<<75.0,8.0>--<23.0,714.0>> -> L<<23.0,714.0>--<23.0,722.0>>

	* backslash (U+005C): L<<148.0,697.0>--<395.0,-40.0>> -> L<<395.0,-40.0>--<441.0,-207.0>>

	* backslash (U+005C): L<<364.0,-201.0>--<117.0,536.0>> -> L<<117.0,536.0>--<71.0,703.0>>

	* w (U+0077): L<<364.0,97.0>--<403.0,432.0>> -> L<<403.0,432.0>--<416.0,511.0>>

	* wacute (U+1E83): L<<364.0,97.0>--<403.0,432.0>> -> L<<403.0,432.0>--<416.0,511.0>>

	* wcircumflex (U+0175): L<<364.0,97.0>--<403.0,432.0>> -> L<<403.0,432.0>--<416.0,511.0>>

	* wdieresis (U+1E85): L<<364.0,97.0>--<403.0,432.0>> -> L<<403.0,432.0>--<416.0,511.0>> 

	* And wgrave (U+1E81): L<<364.0,97.0>--<403.0,432.0>> -> L<<403.0,432.0>--<416.0,511.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* newGlyph (U+00B5): L<<59.0,-208.0>--<58.0,513.0>> [code: found-semi-vertical]
</div></details><br></div></details>
### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 12 | 50 | 668 | 37 | 520 | 0 |
| 0% | 1% | 4% | 52% | 3% | 40% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
