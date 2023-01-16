## Fontbakery report

Fontbakery version: 0.8.10

<details><summary><b>[11] HasubiMono-Regular.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Familyname must be unique according to namecheck.fontdata.com (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fontdata_namecheck">com.google.fonts/check/fontdata_namecheck</a>)</summary><div>


* 💔 **ERROR** Failed to access: http://namecheck.fontdata.com.
		This check relies on the external service http://namecheck.fontdata.com via the internet. While the service cannot be reached or does not respond this check is broken.

		You can exclude this check with the command line option:
		-x com.google.fonts/check/fontdata_namecheck

		Or you can wait until the service is available again.
		If the problem persists please report this issue at: https://github.com/googlefonts/fontbakery/issues

		Original error message:
		<class 'requests.exceptions.ConnectionError'> [code: namecheck-service]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1035, but got 960 instead [code: ascent]
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

	* d (U+0064): X=308.5,Y=510.0 (should be at x-height 512?)

	* d (U+0064): X=303.5,Y=1.0 (should be at baseline 0?)

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

	* uni0635 (U+0635): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0635 (U+0635): X=-32.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=-32.0,Y=-261.0 (should be at descender -260?)

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
</div></details><br></div></details><details><summary><b>[11] HasubiMono-Medium.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Familyname must be unique according to namecheck.fontdata.com (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fontdata_namecheck">com.google.fonts/check/fontdata_namecheck</a>)</summary><div>


* 💔 **ERROR** Failed to access: http://namecheck.fontdata.com.
		This check relies on the external service http://namecheck.fontdata.com via the internet. While the service cannot be reached or does not respond this check is broken.

		You can exclude this check with the command line option:
		-x com.google.fonts/check/fontdata_namecheck

		Or you can wait until the service is available again.
		If the problem persists please report this issue at: https://github.com/googlefonts/fontbakery/issues

		Original error message:
		<class 'requests.exceptions.ConnectionError'> [code: namecheck-service]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1035, but got 960 instead [code: ascent]
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

	* a (U+0061): X=135.0,Y=0.5 (should be at baseline 0?)

	* a (U+0061): X=340.0,Y=510.0 (should be at x-height 512?)

	* d (U+0064): X=303.0,Y=511.0 (should be at x-height 512?)

	* h (U+0068): X=79.0,Y=734.0 (should be at cap-height 736?)

	* h (U+0068): X=151.0,Y=734.0 (should be at cap-height 736?)

	* p (U+0070): X=195.0,Y=510.0 (should be at x-height 512?)

	* q (U+0071): X=317.5,Y=510.0 (should be at x-height 512?)

	* r (U+0072): X=283.5,Y=513.0 (should be at x-height 512?)

	* s (U+0073): X=351.5,Y=-2.0 (should be at baseline 0?)

	* w (U+0077): X=416.0,Y=511.0 (should be at x-height 512?)

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

	* sacute (U+015B): X=351.5,Y=-2.0 (should be at baseline 0?)

	* scaron (U+0161): X=351.5,Y=-2.0 (should be at baseline 0?)

	* uni0635 (U+0635): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0635 (U+0635): X=-32.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=128.0,Y=-261.0 (should be at descender -260?) 

	* And uni0636 (U+0636): X=-32.0,Y=-261.0 (should be at descender -260?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* W (U+0057): L<<492.0,728.0>--<492.0,709.0>> -> L<<492.0,709.0>--<441.0,8.0>>

	* W (U+0057): L<<71.0,8.0>--<20.0,709.0>> -> L<<20.0,709.0>--<20.0,728.0>>

	* Wacute (U+1E82): L<<492.0,728.0>--<492.0,709.0>> -> L<<492.0,709.0>--<441.0,8.0>>

	* Wacute (U+1E82): L<<71.0,8.0>--<20.0,709.0>> -> L<<20.0,709.0>--<20.0,728.0>>

	* Wcircumflex (U+0174): L<<492.0,728.0>--<492.0,709.0>> -> L<<492.0,709.0>--<441.0,8.0>>

	* Wcircumflex (U+0174): L<<71.0,8.0>--<20.0,709.0>> -> L<<20.0,709.0>--<20.0,728.0>>

	* Wdieresis (U+1E84): L<<492.0,728.0>--<492.0,709.0>> -> L<<492.0,709.0>--<441.0,8.0>>

	* Wdieresis (U+1E84): L<<71.0,8.0>--<20.0,709.0>> -> L<<20.0,709.0>--<20.0,728.0>>

	* Wgrave (U+1E80): L<<492.0,728.0>--<492.0,709.0>> -> L<<492.0,709.0>--<441.0,8.0>>

	* Wgrave (U+1E80): L<<71.0,8.0>--<20.0,709.0>> -> L<<20.0,709.0>--<20.0,728.0>>

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
</div></details><br></div></details><details><summary><b>[11] HasubiMono-Black.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Familyname must be unique according to namecheck.fontdata.com (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fontdata_namecheck">com.google.fonts/check/fontdata_namecheck</a>)</summary><div>


* 💔 **ERROR** Failed to access: http://namecheck.fontdata.com.
		This check relies on the external service http://namecheck.fontdata.com via the internet. While the service cannot be reached or does not respond this check is broken.

		You can exclude this check with the command line option:
		-x com.google.fonts/check/fontdata_namecheck

		Or you can wait until the service is available again.
		If the problem persists please report this issue at: https://github.com/googlefonts/fontbakery/issues

		Original error message:
		<class 'requests.exceptions.ConnectionError'> [code: namecheck-service]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1035, but got 960 instead [code: ascent]
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

	* d (U+0064): X=267.0,Y=-2.0 (should be at baseline 0?)

	* m (U+006D): X=166.0,Y=510.5 (should be at x-height 512?)

	* m (U+006D): X=257.0,Y=510.5 (should be at x-height 512?)

	* m (U+006D): X=321.0,Y=510.5 (should be at x-height 512?)

	* p (U+0070): X=195.0,Y=510.0 (should be at x-height 512?)

	* q (U+0071): X=317.5,Y=510.0 (should be at x-height 512?)

	* r (U+0072): X=287.5,Y=513.0 (should be at x-height 512?)

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

	* ae (U+00E6): X=461.5,Y=1.5 (should be at baseline 0?)

	* ae (U+00E6): X=38.5,Y=0.5 (should be at baseline 0?)

	* eth (U+00F0): X=299.5,Y=1.0 (should be at baseline 0?)

	* thorn (U+00FE): X=212.5,Y=1.0 (should be at baseline 0?)

	* amacron (U+0101): X=135.0,Y=0.5 (should be at baseline 0?)

	* abreve (U+0103): X=135.0,Y=0.5 (should be at baseline 0?)

	* oe (U+0153): X=455.5,Y=1.5 (should be at baseline 0?)

	* oe (U+0153): X=221.0,Y=-2.0 (should be at baseline 0?)

	* sacute (U+015B): X=177.5,Y=-2.0 (should be at baseline 0?)

	* scaron (U+0161): X=177.5,Y=-2.0 (should be at baseline 0?)

	* uni0635 (U+0635): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0635 (U+0635): X=-32.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=-32.0,Y=-261.0 (should be at descender -260?)

	* uni0654 (U+0654): X=300.0,Y=734.0 (should be at cap-height 736?) 

	* And uni0654 (U+0654): X=273.0,Y=734.0 (should be at cap-height 736?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* W (U+0057): L<<51.0,8.0>--<0.0,656.0>> -> L<<0.0,656.0>--<0.0,728.0>>

	* W (U+0057): L<<512.0,728.0>--<512.0,656.0>> -> L<<512.0,656.0>--<461.0,8.0>>

	* Wacute (U+1E82): L<<51.0,8.0>--<0.0,656.0>> -> L<<0.0,656.0>--<0.0,728.0>>

	* Wacute (U+1E82): L<<512.0,728.0>--<512.0,656.0>> -> L<<512.0,656.0>--<461.0,8.0>>

	* Wcircumflex (U+0174): L<<51.0,8.0>--<0.0,656.0>> -> L<<0.0,656.0>--<0.0,728.0>>

	* Wcircumflex (U+0174): L<<512.0,728.0>--<512.0,656.0>> -> L<<512.0,656.0>--<461.0,8.0>>

	* Wdieresis (U+1E84): L<<51.0,8.0>--<0.0,656.0>> -> L<<0.0,656.0>--<0.0,728.0>>

	* Wdieresis (U+1E84): L<<512.0,728.0>--<512.0,656.0>> -> L<<512.0,656.0>--<461.0,8.0>>

	* Wgrave (U+1E80): L<<51.0,8.0>--<0.0,656.0>> -> L<<0.0,656.0>--<0.0,728.0>>

	* Wgrave (U+1E80): L<<512.0,728.0>--<512.0,656.0>> -> L<<512.0,656.0>--<461.0,8.0>>

	* w (U+0077): L<<93.0,504.0>--<93.0,496.0>> -> L<<93.0,496.0>--<130.0,102.0>>

	* wacute (U+1E83): L<<93.0,504.0>--<93.0,496.0>> -> L<<93.0,496.0>--<130.0,102.0>>

	* wcircumflex (U+0175): L<<93.0,504.0>--<93.0,496.0>> -> L<<93.0,496.0>--<130.0,102.0>>

	* wdieresis (U+1E85): L<<93.0,504.0>--<93.0,496.0>> -> L<<93.0,496.0>--<130.0,102.0>> 

	* And wgrave (U+1E81): L<<93.0,504.0>--<93.0,496.0>> -> L<<93.0,496.0>--<130.0,102.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* newGlyph (U+00B5): L<<59.0,-208.0>--<58.0,513.0>> 

	* And uniFEDC (U+FEDC): L<<481.0,148.0>--<480.0,8.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[12] HasubiMono-ExtraBold.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Familyname must be unique according to namecheck.fontdata.com (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fontdata_namecheck">com.google.fonts/check/fontdata_namecheck</a>)</summary><div>


* 💔 **ERROR** Failed to access: http://namecheck.fontdata.com.
		This check relies on the external service http://namecheck.fontdata.com via the internet. While the service cannot be reached or does not respond this check is broken.

		You can exclude this check with the command line option:
		-x com.google.fonts/check/fontdata_namecheck

		Or you can wait until the service is available again.
		If the problem persists please report this issue at: https://github.com/googlefonts/fontbakery/issues

		Original error message:
		<class 'requests.exceptions.ConnectionError'> [code: namecheck-service]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1035, but got 960 instead [code: ascent]
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

	* a (U+0061): X=135.0,Y=0.5 (should be at baseline 0?)

	* a (U+0061): X=340.0,Y=510.0 (should be at x-height 512?)

	* b (U+0062): X=212.0,Y=514.0 (should be at x-height 512?)

	* b (U+0062): X=215.5,Y=-1.0 (should be at baseline 0?)

	* c (U+0063): X=354.5,Y=510.5 (should be at x-height 512?)

	* d (U+0064): X=286.5,Y=514.0 (should be at x-height 512?)

	* d (U+0064): X=277.5,Y=-1.0 (should be at baseline 0?)

	* p (U+0070): X=195.0,Y=510.0 (should be at x-height 512?)

	* q (U+0071): X=317.5,Y=510.0 (should be at x-height 512?)

	* r (U+0072): X=286.0,Y=513.0 (should be at x-height 512?)

	* s (U+0073): X=172.5,Y=-1.5 (should be at baseline 0?)

	* s (U+0073): X=350.5,Y=-2.0 (should be at baseline 0?)

	* w (U+0077): X=483.0,Y=510.0 (should be at x-height 512?)

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

	* sacute (U+015B): X=172.5,Y=-1.5 (should be at baseline 0?)

	* sacute (U+015B): X=350.5,Y=-2.0 (should be at baseline 0?)

	* scaron (U+0161): X=172.5,Y=-1.5 (should be at baseline 0?)

	* scaron (U+0161): X=350.5,Y=-2.0 (should be at baseline 0?)

	* uni0635 (U+0635): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0635 (U+0635): X=-32.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=-32.0,Y=-261.0 (should be at descender -260?)

	* uni0654 (U+0654): X=185.0,Y=735.0 (should be at cap-height 736?)

	* uni0654 (U+0654): X=206.0,Y=735.0 (should be at cap-height 736?)

	* uni0654 (U+0654): X=268.0,Y=735.0 (should be at cap-height 736?) 

	* And uni0654 (U+0654): X=327.0,Y=735.0 (should be at cap-height 736?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* W (U+0057): L<<505.0,728.0>--<505.0,674.0>> -> L<<505.0,674.0>--<454.0,8.0>>

	* W (U+0057): L<<58.0,8.0>--<7.0,674.0>> -> L<<7.0,674.0>--<7.0,728.0>>

	* Wacute (U+1E82): L<<505.0,728.0>--<505.0,674.0>> -> L<<505.0,674.0>--<454.0,8.0>>

	* Wacute (U+1E82): L<<58.0,8.0>--<7.0,674.0>> -> L<<7.0,674.0>--<7.0,728.0>>

	* Wcircumflex (U+0174): L<<505.0,728.0>--<505.0,674.0>> -> L<<505.0,674.0>--<454.0,8.0>>

	* Wcircumflex (U+0174): L<<58.0,8.0>--<7.0,674.0>> -> L<<7.0,674.0>--<7.0,728.0>>

	* Wdieresis (U+1E84): L<<505.0,728.0>--<505.0,674.0>> -> L<<505.0,674.0>--<454.0,8.0>>

	* Wdieresis (U+1E84): L<<58.0,8.0>--<7.0,674.0>> -> L<<7.0,674.0>--<7.0,728.0>>

	* Wgrave (U+1E80): L<<505.0,728.0>--<505.0,674.0>> -> L<<505.0,674.0>--<454.0,8.0>>

	* Wgrave (U+1E80): L<<58.0,8.0>--<7.0,674.0>> -> L<<7.0,674.0>--<7.0,728.0>>

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

	* newGlyph (U+00B5): L<<59.0,-208.0>--<58.0,513.0>> 

	* And uniFEDC (U+FEDC): L<<481.0,126.0>--<480.0,8.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[11] HasubiMono-SemiBold.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Familyname must be unique according to namecheck.fontdata.com (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fontdata_namecheck">com.google.fonts/check/fontdata_namecheck</a>)</summary><div>


* 💔 **ERROR** Failed to access: http://namecheck.fontdata.com.
		This check relies on the external service http://namecheck.fontdata.com via the internet. While the service cannot be reached or does not respond this check is broken.

		You can exclude this check with the command line option:
		-x com.google.fonts/check/fontdata_namecheck

		Or you can wait until the service is available again.
		If the problem persists please report this issue at: https://github.com/googlefonts/fontbakery/issues

		Original error message:
		<class 'requests.exceptions.ConnectionError'> [code: namecheck-service]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1035, but got 960 instead [code: ascent]
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

	* p (U+0070): X=195.0,Y=510.0 (should be at x-height 512?)

	* q (U+0071): X=317.5,Y=510.0 (should be at x-height 512?)

	* r (U+0072): X=284.5,Y=513.0 (should be at x-height 512?)

	* s (U+0073): X=351.5,Y=-2.0 (should be at baseline 0?)

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

	* sacute (U+015B): X=351.5,Y=-2.0 (should be at baseline 0?)

	* scaron (U+0161): X=351.5,Y=-2.0 (should be at baseline 0?)

	* uni0635 (U+0635): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0635 (U+0635): X=-32.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=-32.0,Y=-261.0 (should be at descender -260?)

	* uni0654 (U+0654): X=169.0,Y=734.0 (should be at cap-height 736?) 

	* And uni0654 (U+0654): X=343.0,Y=734.0 (should be at cap-height 736?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* W (U+0057): L<<497.0,728.0>--<497.0,697.0>> -> L<<497.0,697.0>--<446.0,8.0>>

	* W (U+0057): L<<66.0,8.0>--<15.0,697.0>> -> L<<15.0,697.0>--<15.0,728.0>>

	* Wacute (U+1E82): L<<497.0,728.0>--<497.0,697.0>> -> L<<497.0,697.0>--<446.0,8.0>>

	* Wacute (U+1E82): L<<66.0,8.0>--<15.0,697.0>> -> L<<15.0,697.0>--<15.0,728.0>>

	* Wcircumflex (U+0174): L<<497.0,728.0>--<497.0,697.0>> -> L<<497.0,697.0>--<446.0,8.0>>

	* Wcircumflex (U+0174): L<<66.0,8.0>--<15.0,697.0>> -> L<<15.0,697.0>--<15.0,728.0>>

	* Wdieresis (U+1E84): L<<497.0,728.0>--<497.0,697.0>> -> L<<497.0,697.0>--<446.0,8.0>>

	* Wdieresis (U+1E84): L<<66.0,8.0>--<15.0,697.0>> -> L<<15.0,697.0>--<15.0,728.0>>

	* Wgrave (U+1E80): L<<497.0,728.0>--<497.0,697.0>> -> L<<497.0,697.0>--<446.0,8.0>>

	* Wgrave (U+1E80): L<<66.0,8.0>--<15.0,697.0>> -> L<<15.0,697.0>--<15.0,728.0>>

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
</div></details><br></div></details><details><summary><b>[11] HasubiMono-Bold.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Familyname must be unique according to namecheck.fontdata.com (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fontdata_namecheck">com.google.fonts/check/fontdata_namecheck</a>)</summary><div>


* 💔 **ERROR** Failed to access: http://namecheck.fontdata.com.
		This check relies on the external service http://namecheck.fontdata.com via the internet. While the service cannot be reached or does not respond this check is broken.

		You can exclude this check with the command line option:
		-x com.google.fonts/check/fontdata_namecheck

		Or you can wait until the service is available again.
		If the problem persists please report this issue at: https://github.com/googlefonts/fontbakery/issues

		Original error message:
		<class 'requests.exceptions.ConnectionError'> [code: namecheck-service]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1035, but got 960 instead [code: ascent]
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

	* b (U+0062): X=212.5,Y=513.0 (should be at x-height 512?)

	* b (U+0062): X=214.5,Y=-0.5 (should be at baseline 0?)

	* d (U+0064): X=292.0,Y=513.0 (should be at x-height 512?)

	* d (U+0064): X=284.0,Y=-0.5 (should be at baseline 0?)

	* f (U+0066): X=330.0,Y=738.0 (should be at cap-height 736?)

	* f (U+0066): X=485.0,Y=738.0 (should be at cap-height 736?)

	* p (U+0070): X=195.0,Y=510.0 (should be at x-height 512?)

	* q (U+0071): X=317.5,Y=510.0 (should be at x-height 512?)

	* r (U+0072): X=285.0,Y=513.0 (should be at x-height 512?)

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

	* ae (U+00E6): X=461.5,Y=1.5 (should be at baseline 0?)

	* ae (U+00E6): X=38.5,Y=0.5 (should be at baseline 0?)

	* eth (U+00F0): X=299.5,Y=1.0 (should be at baseline 0?)

	* thorn (U+00FE): X=212.5,Y=1.0 (should be at baseline 0?)

	* amacron (U+0101): X=135.0,Y=0.5 (should be at baseline 0?)

	* abreve (U+0103): X=135.0,Y=0.5 (should be at baseline 0?)

	* oe (U+0153): X=455.5,Y=1.5 (should be at baseline 0?)

	* oe (U+0153): X=221.0,Y=-2.0 (should be at baseline 0?)

	* sacute (U+015B): X=170.0,Y=-1.0 (should be at baseline 0?)

	* sacute (U+015B): X=351.0,Y=-2.0 (should be at baseline 0?)

	* scaron (U+0161): X=170.0,Y=-1.0 (should be at baseline 0?)

	* scaron (U+0161): X=351.0,Y=-2.0 (should be at baseline 0?)

	* uni0635 (U+0635): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0635 (U+0635): X=-32.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=-32.0,Y=-261.0 (should be at descender -260?)

	* uni0686 (U+0686): X=272.0,Y=-262.0 (should be at descender -260?) 

	* And uni0686 (U+0686): X=384.0,Y=-262.0 (should be at descender -260?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* W (U+0057): L<<501.0,728.0>--<501.0,686.0>> -> L<<501.0,686.0>--<450.0,8.0>>

	* W (U+0057): L<<62.0,8.0>--<11.0,686.0>> -> L<<11.0,686.0>--<11.0,728.0>>

	* Wacute (U+1E82): L<<501.0,728.0>--<501.0,686.0>> -> L<<501.0,686.0>--<450.0,8.0>>

	* Wacute (U+1E82): L<<62.0,8.0>--<11.0,686.0>> -> L<<11.0,686.0>--<11.0,728.0>>

	* Wcircumflex (U+0174): L<<501.0,728.0>--<501.0,686.0>> -> L<<501.0,686.0>--<450.0,8.0>>

	* Wcircumflex (U+0174): L<<62.0,8.0>--<11.0,686.0>> -> L<<11.0,686.0>--<11.0,728.0>>

	* Wdieresis (U+1E84): L<<501.0,728.0>--<501.0,686.0>> -> L<<501.0,686.0>--<450.0,8.0>>

	* Wdieresis (U+1E84): L<<62.0,8.0>--<11.0,686.0>> -> L<<11.0,686.0>--<11.0,728.0>>

	* Wgrave (U+1E80): L<<501.0,728.0>--<501.0,686.0>> -> L<<501.0,686.0>--<450.0,8.0>>

	* Wgrave (U+1E80): L<<62.0,8.0>--<11.0,686.0>> -> L<<11.0,686.0>--<11.0,728.0>>

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
</div></details><br></div></details>
### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 6 | 12 | 49 | 668 | 37 | 515 | 0 |
| 0% | 1% | 4% | 52% | 3% | 40% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
