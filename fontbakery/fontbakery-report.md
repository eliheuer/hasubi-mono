## Fontbakery report

Fontbakery version: 0.8.10

<details><summary><b>[10] HasubiMono-ExtraBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 432, but got 360 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** Font is monospaced but 42 glyphs (7.06%) have a different width. You should check the widths of: ['AE', 'IJ', 'uni0136', 'Lcaron', 'uni0145', 'Eng', 'uni0156', 'aogonek', 'dcaron', 'dcroat', 'eogonek', 'uni0123', 'hbar', 'ij', 'lcaron', 'uni013C', 'lslash', 'uni0146', 'eng', 'uni0157', 'scedilla', 'uni0219', 'tcaron', 'uni021B', 'uogonek', 'uniFED2', 'uniFB6B', 'uni06A1.fina', 'uni066F', 'uni066F.fina', 'uni0642', 'uniFED6', 'uniFEF8', 'uniFEFA', 'uniFEF6', 'lam_alefWaslaar.fina', 'uni066B', 'uni066C', 'uni2074', 'guillemotleft', 'trademark', 'logicalnot'] [code: mono-outliers]
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

	- gafsarkashcenterar

	- miniKehehar

	- threedotsdownabovear

	- threedotsupbelowar

	- twodotsverticalabovear

	- twodotsverticalbelowar

	- uniFB58

	- uniFB6C

	- uniFB7C

	- uniFB90

	- uniFB94

	- uniFE9F

	- uniFEBF

	- uniFEC7

	- uniFECF

	- uniFED7

	- uniFEDF

	- uniFEE3

	- uniFEF3 

	- And yehFarsiar.init
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: onequarter	Contours detected: 1	Expected: 3 or 4

	- Glyph name: onehalf	Contours detected: 1	Expected: 3

	- Glyph name: threequarters	Contours detected: 1	Expected: 3 or 4

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: aogonek	Contours detected: 0	Expected: 2

	- Glyph name: dcaron	Contours detected: 0	Expected: 3

	- Glyph name: dcroat	Contours detected: 0	Expected: 2

	- Glyph name: eogonek	Contours detected: 0	Expected: 2

	- Glyph name: uni0122	Contours detected: 1	Expected: 2

	- Glyph name: uni0123	Contours detected: 0	Expected: 3 or 4

	- Glyph name: Hbar	Contours detected: 0	Expected: 2

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

	- Glyph name: Eng	Contours detected: 0	Expected: 1

	- Glyph name: Hbar	Contours detected: 0	Expected: 2

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
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* W (U+0057): L<<100.0,696.0>--<106.0,519.0>> -> L<<106.0,519.0>--<137.0,100.0>>

	* W (U+0057): L<<137.0,100.0>--<164.0,215.0>> -> L<<164.0,215.0>--<216.0,504.0>>

	* W (U+0057): L<<293.0,507.0>--<314.0,387.0>> -> L<<314.0,387.0>--<368.0,100.0>>

	* W (U+0057): L<<368.0,100.0>--<386.0,272.0>> -> L<<386.0,272.0>--<415.0,698.0>>

	* W (U+0057): L<<77.0,8.0>--<24.0,688.0>> -> L<<24.0,688.0>--<24.0,696.0>>

	* Wacute (U+1E82): L<<100.0,696.0>--<106.0,519.0>> -> L<<106.0,519.0>--<137.0,100.0>>

	* Wacute (U+1E82): L<<137.0,100.0>--<164.0,215.0>> -> L<<164.0,215.0>--<216.0,504.0>>

	* Wacute (U+1E82): L<<293.0,507.0>--<314.0,387.0>> -> L<<314.0,387.0>--<368.0,100.0>>

	* Wacute (U+1E82): L<<368.0,100.0>--<386.0,272.0>> -> L<<386.0,272.0>--<415.0,698.0>>

	* Wacute (U+1E82): L<<77.0,8.0>--<24.0,688.0>> -> L<<24.0,688.0>--<24.0,696.0>>

	* Wcircumflex (U+0174): L<<100.0,696.0>--<106.0,519.0>> -> L<<106.0,519.0>--<137.0,100.0>>

	* Wcircumflex (U+0174): L<<137.0,100.0>--<164.0,215.0>> -> L<<164.0,215.0>--<216.0,504.0>>

	* Wcircumflex (U+0174): L<<293.0,507.0>--<314.0,387.0>> -> L<<314.0,387.0>--<368.0,100.0>>

	* Wcircumflex (U+0174): L<<368.0,100.0>--<386.0,272.0>> -> L<<386.0,272.0>--<415.0,698.0>>

	* Wcircumflex (U+0174): L<<77.0,8.0>--<24.0,688.0>> -> L<<24.0,688.0>--<24.0,696.0>>

	* Wdieresis (U+1E84): L<<100.0,696.0>--<106.0,519.0>> -> L<<106.0,519.0>--<137.0,100.0>>

	* Wdieresis (U+1E84): L<<137.0,100.0>--<164.0,215.0>> -> L<<164.0,215.0>--<216.0,504.0>>

	* Wdieresis (U+1E84): L<<293.0,507.0>--<314.0,387.0>> -> L<<314.0,387.0>--<368.0,100.0>>

	* Wdieresis (U+1E84): L<<368.0,100.0>--<386.0,272.0>> -> L<<386.0,272.0>--<415.0,698.0>>

	* Wdieresis (U+1E84): L<<77.0,8.0>--<24.0,688.0>> -> L<<24.0,688.0>--<24.0,696.0>>

	* Wgrave (U+1E80): L<<100.0,696.0>--<106.0,519.0>> -> L<<106.0,519.0>--<137.0,100.0>>

	* Wgrave (U+1E80): L<<137.0,100.0>--<164.0,215.0>> -> L<<164.0,215.0>--<216.0,504.0>>

	* Wgrave (U+1E80): L<<293.0,507.0>--<314.0,387.0>> -> L<<314.0,387.0>--<368.0,100.0>>

	* Wgrave (U+1E80): L<<368.0,100.0>--<386.0,272.0>> -> L<<386.0,272.0>--<415.0,698.0>>

	* Wgrave (U+1E80): L<<77.0,8.0>--<24.0,688.0>> -> L<<24.0,688.0>--<24.0,696.0>>

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
</div></details><br></div></details><details><summary><b>[9] HasubiMono-Medium.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 432, but got 360 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** Font is monospaced but 42 glyphs (7.06%) have a different width. You should check the widths of: ['AE', 'IJ', 'uni0136', 'Lcaron', 'uni0145', 'Eng', 'uni0156', 'aogonek', 'dcaron', 'dcroat', 'eogonek', 'uni0123', 'hbar', 'ij', 'lcaron', 'uni013C', 'lslash', 'uni0146', 'eng', 'uni0157', 'scedilla', 'uni0219', 'tcaron', 'uni021B', 'uogonek', 'uniFED2', 'uniFB6B', 'uni06A1.fina', 'uni066F', 'uni066F.fina', 'uni0642', 'uniFED6', 'uniFEF8', 'uniFEFA', 'uniFEF6', 'lam_alefWaslaar.fina', 'uni066B', 'uni066C', 'uni2074', 'guillemotleft', 'trademark', 'logicalnot'] [code: mono-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- doublestrokear

	- gafsarkashcenterar

	- miniKehehar

	- threedotsdownabovear

	- threedotsupbelowar

	- twodotsverticalabovear

	- twodotsverticalbelowar

	- uniFB58

	- uniFB6C

	- uniFB7C

	- uniFB90

	- uniFB94

	- uniFE9F

	- uniFEBF

	- uniFEC7

	- uniFECF

	- uniFED7

	- uniFEDF

	- uniFEE3

	- uniFEF3 

	- And yehFarsiar.init
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: onequarter	Contours detected: 1	Expected: 3 or 4

	- Glyph name: onehalf	Contours detected: 1	Expected: 3

	- Glyph name: threequarters	Contours detected: 1	Expected: 3 or 4

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: aogonek	Contours detected: 0	Expected: 2

	- Glyph name: dcaron	Contours detected: 0	Expected: 3

	- Glyph name: dcroat	Contours detected: 0	Expected: 2

	- Glyph name: eogonek	Contours detected: 0	Expected: 2

	- Glyph name: uni0122	Contours detected: 1	Expected: 2

	- Glyph name: uni0123	Contours detected: 0	Expected: 3 or 4

	- Glyph name: Hbar	Contours detected: 0	Expected: 2

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

	- Glyph name: Eng	Contours detected: 0	Expected: 1

	- Glyph name: Hbar	Contours detected: 0	Expected: 2

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
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* W (U+0057): L<<150.0,97.0>--<197.0,426.0>> -> L<<197.0,426.0>--<216.0,504.0>>

	* W (U+0057): L<<373.0,97.0>--<394.0,590.0>> -> L<<394.0,590.0>--<407.0,703.0>>

	* W (U+0057): L<<82.0,8.0>--<36.0,688.0>> -> L<<36.0,688.0>--<36.0,696.0>>

	* Wacute (U+1E82): L<<150.0,97.0>--<197.0,426.0>> -> L<<197.0,426.0>--<216.0,504.0>>

	* Wacute (U+1E82): L<<373.0,97.0>--<394.0,590.0>> -> L<<394.0,590.0>--<407.0,703.0>>

	* Wacute (U+1E82): L<<82.0,8.0>--<36.0,688.0>> -> L<<36.0,688.0>--<36.0,696.0>>

	* Wcircumflex (U+0174): L<<150.0,97.0>--<197.0,426.0>> -> L<<197.0,426.0>--<216.0,504.0>>

	* Wcircumflex (U+0174): L<<373.0,97.0>--<394.0,590.0>> -> L<<394.0,590.0>--<407.0,703.0>>

	* Wcircumflex (U+0174): L<<82.0,8.0>--<36.0,688.0>> -> L<<36.0,688.0>--<36.0,696.0>>

	* Wdieresis (U+1E84): L<<150.0,97.0>--<197.0,426.0>> -> L<<197.0,426.0>--<216.0,504.0>>

	* Wdieresis (U+1E84): L<<373.0,97.0>--<394.0,590.0>> -> L<<394.0,590.0>--<407.0,703.0>>

	* Wdieresis (U+1E84): L<<82.0,8.0>--<36.0,688.0>> -> L<<36.0,688.0>--<36.0,696.0>>

	* Wgrave (U+1E80): L<<150.0,97.0>--<197.0,426.0>> -> L<<197.0,426.0>--<216.0,504.0>>

	* Wgrave (U+1E80): L<<373.0,97.0>--<394.0,590.0>> -> L<<394.0,590.0>--<407.0,703.0>>

	* Wgrave (U+1E80): L<<82.0,8.0>--<36.0,688.0>> -> L<<36.0,688.0>--<36.0,696.0>>

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
</div></details><br></div></details><details><summary><b>[10] HasubiMono-Bold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 432, but got 360 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** Font is monospaced but 42 glyphs (7.06%) have a different width. You should check the widths of: ['AE', 'IJ', 'uni0136', 'Lcaron', 'uni0145', 'Eng', 'uni0156', 'aogonek', 'dcaron', 'dcroat', 'eogonek', 'uni0123', 'hbar', 'ij', 'lcaron', 'uni013C', 'lslash', 'uni0146', 'eng', 'uni0157', 'scedilla', 'uni0219', 'tcaron', 'uni021B', 'uogonek', 'uniFED2', 'uniFB6B', 'uni06A1.fina', 'uni066F', 'uni066F.fina', 'uni0642', 'uniFED6', 'uniFEF8', 'uniFEFA', 'uniFEF6', 'lam_alefWaslaar.fina', 'uni066B', 'uni066C', 'uni2074', 'guillemotleft', 'trademark', 'logicalnot'] [code: mono-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- doublestrokear

	- gafsarkashcenterar

	- miniKehehar

	- threedotsdownabovear

	- threedotsupbelowar

	- twodotsverticalabovear

	- twodotsverticalbelowar

	- uniFB58

	- uniFB6C

	- uniFB7C

	- uniFB90

	- uniFB94

	- uniFE9F

	- uniFEBF

	- uniFEC7

	- uniFECF

	- uniFED7

	- uniFEDF

	- uniFEE3

	- uniFEF3 

	- And yehFarsiar.init
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: onequarter	Contours detected: 1	Expected: 3 or 4

	- Glyph name: onehalf	Contours detected: 1	Expected: 3

	- Glyph name: threequarters	Contours detected: 1	Expected: 3 or 4

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: aogonek	Contours detected: 0	Expected: 2

	- Glyph name: dcaron	Contours detected: 0	Expected: 3

	- Glyph name: dcroat	Contours detected: 0	Expected: 2

	- Glyph name: eogonek	Contours detected: 0	Expected: 2

	- Glyph name: uni0122	Contours detected: 1	Expected: 2

	- Glyph name: uni0123	Contours detected: 0	Expected: 3 or 4

	- Glyph name: Hbar	Contours detected: 0	Expected: 2

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

	- Glyph name: Eng	Contours detected: 0	Expected: 1

	- Glyph name: Hbar	Contours detected: 0	Expected: 2

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

	* ampersand (U+0026): X=233.5,Y=1.5 (should be at baseline 0?)

	* parenleft (U+0028): X=224.0,Y=1.0 (should be at baseline 0?)

	* parenright (U+0029): X=296.0,Y=1.0 (should be at baseline 0?)

	* at (U+0040): X=349.5,Y=705.5 (should be at cap-height 704?)

	* a (U+0061): X=135.0,Y=0.5 (should be at baseline 0?)

	* a (U+0061): X=340.0,Y=510.0 (should be at x-height 512?)

	* b (U+0062): X=212.5,Y=513.0 (should be at x-height 512?)

	* b (U+0062): X=214.5,Y=-0.5 (should be at baseline 0?)

	* d (U+0064): X=297.5,Y=-0.5 (should be at baseline 0?)

	* d (U+0064): X=299.5,Y=513.0 (should be at x-height 512?)

	* j (U+006A): X=242.5,Y=702.0 (should be at cap-height 704?)

	* j (U+006A): X=333.5,Y=702.0 (should be at cap-height 704?)

	* m (U+006D): X=166.0,Y=510.5 (should be at x-height 512?)

	* m (U+006D): X=257.0,Y=510.5 (should be at x-height 512?)

	* m (U+006D): X=321.0,Y=510.5 (should be at x-height 512?)

	* p (U+0070): X=195.0,Y=510.0 (should be at x-height 512?)

	* q (U+0071): X=317.5,Y=510.0 (should be at x-height 512?)

	* s (U+0073): X=170.0,Y=-1.0 (should be at baseline 0?)

	* s (U+0073): X=351.0,Y=-2.0 (should be at baseline 0?)

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

	* sacute (U+015B): X=170.0,Y=-1.0 (should be at baseline 0?)

	* sacute (U+015B): X=351.0,Y=-2.0 (should be at baseline 0?)

	* scaron (U+0161): X=170.0,Y=-1.0 (should be at baseline 0?)

	* scaron (U+0161): X=351.0,Y=-2.0 (should be at baseline 0?)

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

	* uni0622 (U+0622): X=127.0,Y=706.0 (should be at cap-height 704?) 

	* And uni0622 (U+0622): X=92.0,Y=706.0 (should be at cap-height 704?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* W (U+0057): L<<104.0,696.0>--<114.0,413.0>> -> L<<114.0,413.0>--<141.0,99.0>>

	* W (U+0057): L<<141.0,99.0>--<175.0,285.0>> -> L<<175.0,285.0>--<216.0,504.0>>

	* W (U+0057): L<<295.0,505.0>--<325.0,315.0>> -> L<<325.0,315.0>--<370.0,99.0>>

	* W (U+0057): L<<370.0,99.0>--<389.0,378.0>> -> L<<389.0,378.0>--<412.0,700.0>>

	* W (U+0057): L<<79.0,8.0>--<28.0,688.0>> -> L<<28.0,688.0>--<28.0,696.0>>

	* Wacute (U+1E82): L<<104.0,696.0>--<114.0,413.0>> -> L<<114.0,413.0>--<141.0,99.0>>

	* Wacute (U+1E82): L<<141.0,99.0>--<175.0,285.0>> -> L<<175.0,285.0>--<216.0,504.0>>

	* Wacute (U+1E82): L<<295.0,505.0>--<325.0,315.0>> -> L<<325.0,315.0>--<370.0,99.0>>

	* Wacute (U+1E82): L<<370.0,99.0>--<389.0,378.0>> -> L<<389.0,378.0>--<412.0,700.0>>

	* Wacute (U+1E82): L<<79.0,8.0>--<28.0,688.0>> -> L<<28.0,688.0>--<28.0,696.0>>

	* Wcircumflex (U+0174): L<<104.0,696.0>--<114.0,413.0>> -> L<<114.0,413.0>--<141.0,99.0>>

	* Wcircumflex (U+0174): L<<141.0,99.0>--<175.0,285.0>> -> L<<175.0,285.0>--<216.0,504.0>>

	* Wcircumflex (U+0174): L<<295.0,505.0>--<325.0,315.0>> -> L<<325.0,315.0>--<370.0,99.0>>

	* Wcircumflex (U+0174): L<<370.0,99.0>--<389.0,378.0>> -> L<<389.0,378.0>--<412.0,700.0>>

	* Wcircumflex (U+0174): L<<79.0,8.0>--<28.0,688.0>> -> L<<28.0,688.0>--<28.0,696.0>>

	* Wdieresis (U+1E84): L<<104.0,696.0>--<114.0,413.0>> -> L<<114.0,413.0>--<141.0,99.0>>

	* Wdieresis (U+1E84): L<<141.0,99.0>--<175.0,285.0>> -> L<<175.0,285.0>--<216.0,504.0>>

	* Wdieresis (U+1E84): L<<295.0,505.0>--<325.0,315.0>> -> L<<325.0,315.0>--<370.0,99.0>>

	* Wdieresis (U+1E84): L<<370.0,99.0>--<389.0,378.0>> -> L<<389.0,378.0>--<412.0,700.0>>

	* Wdieresis (U+1E84): L<<79.0,8.0>--<28.0,688.0>> -> L<<28.0,688.0>--<28.0,696.0>>

	* Wgrave (U+1E80): L<<104.0,696.0>--<114.0,413.0>> -> L<<114.0,413.0>--<141.0,99.0>>

	* Wgrave (U+1E80): L<<141.0,99.0>--<175.0,285.0>> -> L<<175.0,285.0>--<216.0,504.0>>

	* Wgrave (U+1E80): L<<295.0,505.0>--<325.0,315.0>> -> L<<325.0,315.0>--<370.0,99.0>>

	* Wgrave (U+1E80): L<<370.0,99.0>--<389.0,378.0>> -> L<<389.0,378.0>--<412.0,700.0>>

	* Wgrave (U+1E80): L<<79.0,8.0>--<28.0,688.0>> -> L<<28.0,688.0>--<28.0,696.0>>

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
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* newGlyph (U+00B5): L<<59.0,-208.0>--<58.0,513.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[10] HasubiMono-Black.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 432, but got 360 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** Font is monospaced but 28 glyphs (4.71%) have a different width. You should check the widths of: ['AE', 'IJ', 'uni0136', 'uni0156', 'aogonek', 'eogonek', 'hbar', 'ij', 'uni0157', 'scedilla', 'uni0219', 'tcaron', 'uni021B', 'uniFED2', 'uniFB6B', 'uni06A1.fina', 'uni066F', 'uni066F.fina', 'uni0642', 'uniFED6', 'uniFEF8', 'uniFEFA', 'uniFEF6', 'lam_alefWaslaar.fina', 'uni066B', 'uni066C', 'guillemotleft', 'logicalnot'] [code: mono-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- doublestrokear

	- gafsarkashcenterar

	- miniKehehar

	- threedotsdownabovear

	- threedotsupbelowar

	- twodotsverticalabovear

	- twodotsverticalbelowar

	- uniFB58

	- uniFB6C

	- uniFB7C

	- uniFB90

	- uniFB94

	- uniFE9F

	- uniFEBF

	- uniFEC7

	- uniFECF

	- uniFED7

	- uniFEDF

	- uniFEE3

	- uniFEF3 

	- And yehFarsiar.init
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: onequarter	Contours detected: 1	Expected: 3 or 4

	- Glyph name: onehalf	Contours detected: 1	Expected: 3

	- Glyph name: threequarters	Contours detected: 1	Expected: 3 or 4

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: aogonek	Contours detected: 0	Expected: 2

	- Glyph name: dcaron	Contours detected: 0	Expected: 3

	- Glyph name: dcroat	Contours detected: 0	Expected: 2

	- Glyph name: eogonek	Contours detected: 0	Expected: 2

	- Glyph name: uni0122	Contours detected: 1	Expected: 2

	- Glyph name: uni0123	Contours detected: 0	Expected: 3 or 4

	- Glyph name: Hbar	Contours detected: 0	Expected: 2

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

	- Glyph name: Eng	Contours detected: 0	Expected: 1

	- Glyph name: Hbar	Contours detected: 0	Expected: 2

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

	* ampersand (U+0026): X=233.5,Y=1.5 (should be at baseline 0?)

	* parenleft (U+0028): X=224.0,Y=1.0 (should be at baseline 0?)

	* parenright (U+0029): X=296.0,Y=1.0 (should be at baseline 0?)

	* at (U+0040): X=349.5,Y=705.5 (should be at cap-height 704?)

	* a (U+0061): X=135.0,Y=0.5 (should be at baseline 0?)

	* a (U+0061): X=340.5,Y=510.0 (should be at x-height 512?)

	* b (U+0062): X=216.5,Y=-2.0 (should be at baseline 0?)

	* c (U+0063): X=357.5,Y=510.5 (should be at x-height 512?)

	* d (U+0064): X=295.5,Y=-2.0 (should be at baseline 0?)

	* j (U+006A): X=242.5,Y=702.0 (should be at cap-height 704?)

	* j (U+006A): X=333.5,Y=702.0 (should be at cap-height 704?)

	* m (U+006D): X=166.0,Y=510.5 (should be at x-height 512?)

	* m (U+006D): X=257.0,Y=510.5 (should be at x-height 512?)

	* m (U+006D): X=321.0,Y=510.5 (should be at x-height 512?)

	* p (U+0070): X=195.0,Y=510.0 (should be at x-height 512?)

	* q (U+0071): X=317.5,Y=510.0 (should be at x-height 512?)

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
</div></details><br></div></details><details><summary><b>[9] HasubiMono-SemiBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 432, but got 360 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** Font is monospaced but 42 glyphs (7.06%) have a different width. You should check the widths of: ['AE', 'IJ', 'uni0136', 'Lcaron', 'uni0145', 'Eng', 'uni0156', 'aogonek', 'dcaron', 'dcroat', 'eogonek', 'uni0123', 'hbar', 'ij', 'lcaron', 'uni013C', 'lslash', 'uni0146', 'eng', 'uni0157', 'scedilla', 'uni0219', 'tcaron', 'uni021B', 'uogonek', 'uniFED2', 'uniFB6B', 'uni06A1.fina', 'uni066F', 'uni066F.fina', 'uni0642', 'uniFED6', 'uniFEF8', 'uniFEFA', 'uniFEF6', 'lam_alefWaslaar.fina', 'uni066B', 'uni066C', 'uni2074', 'guillemotleft', 'trademark', 'logicalnot'] [code: mono-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- doublestrokear

	- gafsarkashcenterar

	- miniKehehar

	- threedotsdownabovear

	- threedotsupbelowar

	- twodotsverticalabovear

	- twodotsverticalbelowar

	- uniFB58

	- uniFB6C

	- uniFB7C

	- uniFB90

	- uniFB94

	- uniFE9F

	- uniFEBF

	- uniFEC7

	- uniFECF

	- uniFED7

	- uniFEDF

	- uniFEE3

	- uniFEF3 

	- And yehFarsiar.init
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: onequarter	Contours detected: 1	Expected: 3 or 4

	- Glyph name: onehalf	Contours detected: 1	Expected: 3

	- Glyph name: threequarters	Contours detected: 1	Expected: 3 or 4

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: aogonek	Contours detected: 0	Expected: 2

	- Glyph name: dcaron	Contours detected: 0	Expected: 3

	- Glyph name: dcroat	Contours detected: 0	Expected: 2

	- Glyph name: eogonek	Contours detected: 0	Expected: 2

	- Glyph name: uni0122	Contours detected: 1	Expected: 2

	- Glyph name: uni0123	Contours detected: 0	Expected: 3 or 4

	- Glyph name: Hbar	Contours detected: 0	Expected: 2

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

	- Glyph name: Eng	Contours detected: 0	Expected: 1

	- Glyph name: Hbar	Contours detected: 0	Expected: 2

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
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* W (U+0057): L<<108.0,696.0>--<122.0,307.0>> -> L<<122.0,307.0>--<145.0,98.0>>

	* W (U+0057): L<<145.0,98.0>--<186.0,355.0>> -> L<<186.0,355.0>--<216.0,504.0>>

	* W (U+0057): L<<298.0,502.0>--<336.0,242.0>> -> L<<336.0,242.0>--<371.0,98.0>>

	* W (U+0057): L<<371.0,98.0>--<391.0,484.0>> -> L<<391.0,484.0>--<409.0,701.0>>

	* W (U+0057): L<<80.0,8.0>--<32.0,688.0>> -> L<<32.0,688.0>--<32.0,696.0>>

	* Wacute (U+1E82): L<<108.0,696.0>--<122.0,307.0>> -> L<<122.0,307.0>--<145.0,98.0>>

	* Wacute (U+1E82): L<<145.0,98.0>--<186.0,355.0>> -> L<<186.0,355.0>--<216.0,504.0>>

	* Wacute (U+1E82): L<<298.0,502.0>--<336.0,242.0>> -> L<<336.0,242.0>--<371.0,98.0>>

	* Wacute (U+1E82): L<<371.0,98.0>--<391.0,484.0>> -> L<<391.0,484.0>--<409.0,701.0>>

	* Wacute (U+1E82): L<<80.0,8.0>--<32.0,688.0>> -> L<<32.0,688.0>--<32.0,696.0>>

	* Wcircumflex (U+0174): L<<108.0,696.0>--<122.0,307.0>> -> L<<122.0,307.0>--<145.0,98.0>>

	* Wcircumflex (U+0174): L<<145.0,98.0>--<186.0,355.0>> -> L<<186.0,355.0>--<216.0,504.0>>

	* Wcircumflex (U+0174): L<<298.0,502.0>--<336.0,242.0>> -> L<<336.0,242.0>--<371.0,98.0>>

	* Wcircumflex (U+0174): L<<371.0,98.0>--<391.0,484.0>> -> L<<391.0,484.0>--<409.0,701.0>>

	* Wcircumflex (U+0174): L<<80.0,8.0>--<32.0,688.0>> -> L<<32.0,688.0>--<32.0,696.0>>

	* Wdieresis (U+1E84): L<<108.0,696.0>--<122.0,307.0>> -> L<<122.0,307.0>--<145.0,98.0>>

	* Wdieresis (U+1E84): L<<145.0,98.0>--<186.0,355.0>> -> L<<186.0,355.0>--<216.0,504.0>>

	* Wdieresis (U+1E84): L<<298.0,502.0>--<336.0,242.0>> -> L<<336.0,242.0>--<371.0,98.0>>

	* Wdieresis (U+1E84): L<<371.0,98.0>--<391.0,484.0>> -> L<<391.0,484.0>--<409.0,701.0>>

	* Wdieresis (U+1E84): L<<80.0,8.0>--<32.0,688.0>> -> L<<32.0,688.0>--<32.0,696.0>>

	* Wgrave (U+1E80): L<<108.0,696.0>--<122.0,307.0>> -> L<<122.0,307.0>--<145.0,98.0>>

	* Wgrave (U+1E80): L<<145.0,98.0>--<186.0,355.0>> -> L<<186.0,355.0>--<216.0,504.0>>

	* Wgrave (U+1E80): L<<298.0,502.0>--<336.0,242.0>> -> L<<336.0,242.0>--<371.0,98.0>>

	* Wgrave (U+1E80): L<<371.0,98.0>--<391.0,484.0>> -> L<<391.0,484.0>--<409.0,701.0>>

	* Wgrave (U+1E80): L<<80.0,8.0>--<32.0,688.0>> -> L<<32.0,688.0>--<32.0,696.0>>

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
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* newGlyph (U+00B5): L<<59.0,-208.0>--<58.0,513.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[9] HasubiMono-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 432, but got 360 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** Font is monospaced but 22 glyphs (3.70%) have a different width. You should check the widths of: ['AE', 'Lcaron', 'uni0145', 'Eng', 'dcaron', 'dcroat', 'uni0123', 'lcaron', 'uni013C', 'lslash', 'uni0146', 'eng', 'uogonek', 'uniFEF8', 'uniFEFA', 'uniFEF6', 'lam_alefWaslaar.fina', 'uni066B', 'uni066C', 'uni2074', 'trademark', 'logicalnot'] [code: mono-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- doublestrokear

	- gafsarkashcenterar

	- miniKehehar

	- threedotsdownabovear

	- threedotsupbelowar

	- twodotsverticalabovear

	- twodotsverticalbelowar

	- uniFB58

	- uniFB6C

	- uniFB7C

	- uniFB90

	- uniFB94

	- uniFE9F

	- uniFEBF

	- uniFEC7

	- uniFECF

	- uniFED7

	- uniFEDF

	- uniFEE3

	- uniFEF3 

	- And yehFarsiar.init
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: onequarter	Contours detected: 1	Expected: 3 or 4

	- Glyph name: onehalf	Contours detected: 1	Expected: 3

	- Glyph name: threequarters	Contours detected: 1	Expected: 3 or 4

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: aogonek	Contours detected: 0	Expected: 2

	- Glyph name: dcaron	Contours detected: 0	Expected: 3

	- Glyph name: dcroat	Contours detected: 0	Expected: 2

	- Glyph name: eogonek	Contours detected: 0	Expected: 2

	- Glyph name: uni0122	Contours detected: 1	Expected: 2

	- Glyph name: uni0123	Contours detected: 0	Expected: 3 or 4

	- Glyph name: Hbar	Contours detected: 0	Expected: 2

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

	- Glyph name: Eng	Contours detected: 0	Expected: 1

	- Glyph name: Hbar	Contours detected: 0	Expected: 2

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
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* W (U+0057): L<<472.0,696.0>--<472.0,688.0>> -> L<<472.0,688.0>--<429.0,8.0>>

	* W (U+0057): L<<83.0,8.0>--<40.0,688.0>> -> L<<40.0,688.0>--<40.0,696.0>>

	* Wacute (U+1E82): L<<472.0,696.0>--<472.0,688.0>> -> L<<472.0,688.0>--<429.0,8.0>>

	* Wacute (U+1E82): L<<83.0,8.0>--<40.0,688.0>> -> L<<40.0,688.0>--<40.0,696.0>>

	* Wcircumflex (U+0174): L<<472.0,696.0>--<472.0,688.0>> -> L<<472.0,688.0>--<429.0,8.0>>

	* Wcircumflex (U+0174): L<<83.0,8.0>--<40.0,688.0>> -> L<<40.0,688.0>--<40.0,696.0>>

	* Wdieresis (U+1E84): L<<472.0,696.0>--<472.0,688.0>> -> L<<472.0,688.0>--<429.0,8.0>>

	* Wdieresis (U+1E84): L<<83.0,8.0>--<40.0,688.0>> -> L<<40.0,688.0>--<40.0,696.0>>

	* Wgrave (U+1E80): L<<472.0,696.0>--<472.0,688.0>> -> L<<472.0,688.0>--<429.0,8.0>> 

	* And Wgrave (U+1E80): L<<83.0,8.0>--<40.0,688.0>> -> L<<40.0,688.0>--<40.0,696.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* newGlyph (U+00B5): L<<59.0,-208.0>--<58.0,513.0>> [code: found-semi-vertical]
</div></details><br></div></details>
### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 12 | 45 | 668 | 37 | 525 | 0 |
| 0% | 1% | 3% | 52% | 3% | 41% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
