## Fontbakery report

Fontbakery version: 0.8.10

<details><summary><b>[11] HasubiMono-Black.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Familyname must be unique according to namecheck.fontdata.com (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fontdata_namecheck">com.google.fonts/check/fontdata_namecheck</a>)</summary><div>


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

	* a (U+0061): X=146.0,Y=1.0 (should be at baseline 0?)

	* b (U+0062): X=209.0,Y=-1.0 (should be at baseline 0?)

	* c (U+0063): X=357.5,Y=510.5 (should be at x-height 512?)

	* d (U+0064): X=303.0,Y=-1.0 (should be at baseline 0?)

	* g (U+0067): X=303.0,Y=513.0 (should be at x-height 512?)

	* h (U+0068): X=219.5,Y=513.0 (should be at x-height 512?)

	* p (U+0070): X=209.0,Y=513.0 (should be at x-height 512?)

	* q (U+0071): X=303.0,Y=513.0 (should be at x-height 512?)

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

	* oe (U+0153): X=455.5,Y=1.5 (should be at baseline 0?)

	* oe (U+0153): X=221.0,Y=-2.0 (should be at baseline 0?)

	* umacron (U+016B): X=294.5,Y=2.0 (should be at baseline 0?)

	* ubreve (U+016D): X=294.5,Y=2.0 (should be at baseline 0?)

	* uring (U+016F): X=294.5,Y=2.0 (should be at baseline 0?)

	* uhungarumlaut (U+0171): X=294.5,Y=2.0 (should be at baseline 0?)

	* uni0635 (U+0635): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0635 (U+0635): X=-32.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=-32.0,Y=-261.0 (should be at descender -260?)

	* uni0654 (U+0654): X=300.0,Y=734.0 (should be at cap-height 736?) 

	* And uni0654 (U+0654): X=273.0,Y=734.0 (should be at cap-height 736?) [code: found-misalignments]
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

	* w (U+0077): L<<93.0,504.0>--<93.0,496.0>> -> L<<93.0,496.0>--<130.0,102.0>>

	* wacute (U+1E83): L<<93.0,504.0>--<93.0,496.0>> -> L<<93.0,496.0>--<130.0,102.0>>

	* wcircumflex (U+0175): L<<93.0,504.0>--<93.0,496.0>> -> L<<93.0,496.0>--<130.0,102.0>>

	* wdieresis (U+1E85): L<<93.0,504.0>--<93.0,496.0>> -> L<<93.0,496.0>--<130.0,102.0>> 

	* And wgrave (U+1E81): L<<93.0,504.0>--<93.0,496.0>> -> L<<93.0,496.0>--<130.0,102.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* newGlyph (U+00B5): L<<59.0,-208.0>--<58.0,513.0>> 

	* And uniFEDC (U+FEDC): L<<481.0,148.0>--<480.0,8.0>> [code: found-semi-vertical]
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

	* G (U+0047): X=308.5,Y=1.0 (should be at baseline 0?)

	* a (U+0061): X=146.0,Y=1.0 (should be at baseline 0?)

	* a (U+0061): X=163.5,Y=538.5 (should be at x-height 538?)

	* b (U+0062): X=209.0,Y=-1.0 (should be at baseline 0?)

	* d (U+0064): X=303.0,Y=-1.0 (should be at baseline 0?)

	* f (U+0066): X=479.0,Y=734.0 (should be at cap-height 736?)

	* g (U+0067): X=303.0,Y=539.0 (should be at x-height 538?)

	* h (U+0068): X=219.5,Y=539.0 (should be at x-height 538?)

	* p (U+0070): X=209.0,Y=539.0 (should be at x-height 538?)

	* q (U+0071): X=303.0,Y=539.0 (should be at x-height 538?)

	* u (U+0075): X=294.5,Y=2.0 (should be at baseline 0?)

	* w (U+0077): X=416.0,Y=537.0 (should be at x-height 538?)

	* copyright (U+00A9): X=370.0,Y=-0.5 (should be at baseline 0?)

	* copyright (U+00A9): X=142.5,Y=-0.5 (should be at baseline 0?)

	* newGlyph (U+00B5): X=184.0,Y=-1.5 (should be at baseline 0?)

	* Igrave (U+00CC): X=153.0,Y=938.0 (should be at ascender 940?)

	* Igrave (U+00CC): X=245.0,Y=938.0 (should be at ascender 940?)

	* Iacute (U+00CD): X=279.0,Y=938.0 (should be at ascender 940?)

	* Iacute (U+00CD): X=371.0,Y=938.0 (should be at ascender 940?)

	* Icircumflex (U+00CE): X=210.0,Y=938.0 (should be at ascender 940?)

	* Icircumflex (U+00CE): X=306.0,Y=938.0 (should be at ascender 940?)

	* agrave (U+00E0): X=146.0,Y=1.0 (should be at baseline 0?)

	* aacute (U+00E1): X=146.0,Y=1.0 (should be at baseline 0?)

	* acircumflex (U+00E2): X=146.0,Y=1.0 (should be at baseline 0?)

	* atilde (U+00E3): X=146.0,Y=1.0 (should be at baseline 0?)

	* adieresis (U+00E4): X=146.0,Y=1.0 (should be at baseline 0?)

	* aring (U+00E5): X=146.0,Y=1.0 (should be at baseline 0?)

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

	* Gbreve (U+011E): X=308.5,Y=1.0 (should be at baseline 0?)

	* Gdotaccent (U+0120): X=308.5,Y=1.0 (should be at baseline 0?)

	* uni0122 (U+0122): X=308.5,Y=1.0 (should be at baseline 0?)

	* oe (U+0153): X=455.5,Y=1.5 (should be at baseline 0?)

	* oe (U+0153): X=221.0,Y=-2.0 (should be at baseline 0?)

	* Sacute (U+015A): X=277.0,Y=938.0 (should be at ascender 940?)

	* Sacute (U+015A): X=369.0,Y=938.0 (should be at ascender 940?)

	* Scaron (U+0160): X=128.0,Y=942.0 (should be at ascender 940?)

	* Scaron (U+0160): X=176.0,Y=942.0 (should be at ascender 940?)

	* Scaron (U+0160): X=336.0,Y=942.0 (should be at ascender 940?)

	* Scaron (U+0160): X=384.0,Y=942.0 (should be at ascender 940?)

	* umacron (U+016B): X=294.5,Y=2.0 (should be at baseline 0?)

	* ubreve (U+016D): X=294.5,Y=2.0 (should be at baseline 0?)

	* uring (U+016F): X=294.5,Y=2.0 (should be at baseline 0?)

	* uhungarumlaut (U+0171): X=294.5,Y=2.0 (should be at baseline 0?)

	* uni0635 (U+0635): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0635 (U+0635): X=-32.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=128.0,Y=-261.0 (should be at descender -260?) 

	* And uni0636 (U+0636): X=-32.0,Y=-261.0 (should be at descender -260?) [code: found-misalignments]
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

	* w (U+0077): L<<364.0,97.0>--<403.0,459.0>> -> L<<403.0,459.0>--<416.0,537.0>>

	* wacute (U+1E83): L<<364.0,97.0>--<403.0,459.0>> -> L<<403.0,459.0>--<416.0,537.0>>

	* wcircumflex (U+0175): L<<364.0,97.0>--<403.0,459.0>> -> L<<403.0,459.0>--<416.0,537.0>>

	* wdieresis (U+1E85): L<<364.0,97.0>--<403.0,459.0>> -> L<<403.0,459.0>--<416.0,537.0>> 

	* And wgrave (U+1E81): L<<364.0,97.0>--<403.0,459.0>> -> L<<403.0,459.0>--<416.0,537.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* newGlyph (U+00B5): L<<59.0,-208.0>--<58.0,513.0>> [code: found-semi-vertical]
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

	* a (U+0061): X=146.0,Y=1.0 (should be at baseline 0?)

	* b (U+0062): X=209.0,Y=-1.0 (should be at baseline 0?)

	* d (U+0064): X=303.0,Y=-1.0 (should be at baseline 0?)

	* g (U+0067): X=303.0,Y=534.0 (should be at x-height 533?)

	* h (U+0068): X=219.5,Y=534.0 (should be at x-height 533?)

	* p (U+0070): X=209.0,Y=534.0 (should be at x-height 533?)

	* q (U+0071): X=303.0,Y=534.0 (should be at x-height 533?)

	* u (U+0075): X=294.5,Y=2.0 (should be at baseline 0?)

	* copyright (U+00A9): X=370.0,Y=-0.5 (should be at baseline 0?)

	* copyright (U+00A9): X=142.5,Y=-0.5 (should be at baseline 0?)

	* newGlyph (U+00B5): X=184.0,Y=-1.5 (should be at baseline 0?)

	* Igrave (U+00CC): X=161.0,Y=941.0 (should be at ascender 940?)

	* Igrave (U+00CC): X=237.0,Y=941.0 (should be at ascender 940?)

	* Iacute (U+00CD): X=287.0,Y=941.0 (should be at ascender 940?)

	* Iacute (U+00CD): X=363.0,Y=941.0 (should be at ascender 940?)

	* Icircumflex (U+00CE): X=218.0,Y=941.0 (should be at ascender 940?)

	* Icircumflex (U+00CE): X=298.0,Y=941.0 (should be at ascender 940?)

	* agrave (U+00E0): X=146.0,Y=1.0 (should be at baseline 0?)

	* aacute (U+00E1): X=146.0,Y=1.0 (should be at baseline 0?)

	* acircumflex (U+00E2): X=146.0,Y=1.0 (should be at baseline 0?)

	* atilde (U+00E3): X=146.0,Y=1.0 (should be at baseline 0?)

	* adieresis (U+00E4): X=146.0,Y=1.0 (should be at baseline 0?)

	* aring (U+00E5): X=146.0,Y=1.0 (should be at baseline 0?)

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

	* ccaron (U+010D): X=125.0,Y=735.0 (should be at cap-height 736?)

	* ccaron (U+010D): X=397.0,Y=735.0 (should be at cap-height 736?)

	* ncaron (U+0148): X=126.0,Y=735.0 (should be at cap-height 736?)

	* ncaron (U+0148): X=398.0,Y=735.0 (should be at cap-height 736?)

	* oe (U+0153): X=455.5,Y=1.5 (should be at baseline 0?)

	* oe (U+0153): X=221.0,Y=-2.0 (should be at baseline 0?)

	* rcaron (U+0159): X=135.0,Y=735.0 (should be at cap-height 736?)

	* rcaron (U+0159): X=407.0,Y=735.0 (should be at cap-height 736?)

	* Sacute (U+015A): X=285.0,Y=941.0 (should be at ascender 940?)

	* Sacute (U+015A): X=361.0,Y=941.0 (should be at ascender 940?)

	* scaron (U+0161): X=116.0,Y=735.0 (should be at cap-height 736?)

	* scaron (U+0161): X=388.0,Y=735.0 (should be at cap-height 736?)

	* umacron (U+016B): X=294.5,Y=2.0 (should be at baseline 0?)

	* ubreve (U+016D): X=294.5,Y=2.0 (should be at baseline 0?)

	* uring (U+016F): X=294.5,Y=2.0 (should be at baseline 0?)

	* uhungarumlaut (U+0171): X=294.5,Y=2.0 (should be at baseline 0?)

	* uni0635 (U+0635): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0635 (U+0635): X=-32.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=-32.0,Y=-261.0 (should be at descender -260?)

	* uni0654 (U+0654): X=169.0,Y=734.0 (should be at cap-height 736?) 

	* And uni0654 (U+0654): X=343.0,Y=734.0 (should be at cap-height 736?) [code: found-misalignments]
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
</div></details><br></div></details><details><summary><b>[11] HasubiMono-Regular.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Familyname must be unique according to namecheck.fontdata.com (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fontdata_namecheck">com.google.fonts/check/fontdata_namecheck</a>)</summary><div>


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
* ⚠ **WARN** Font is monospaced but 20 glyphs (3.21%) have a different width. You should check the widths of: ['Lcaron', 'uni0145', 'Eng', 'dcaron', 'dcroat', 'uni0123', 'lcaron', 'uni013C', 'lslash', 'uni0146', 'eng', 'uogonek', 'uniFEF8', 'uniFEFA', 'uniFEF6', 'uni066B', 'uni066C', 'uni2074', 'trademark', 'logicalnot'] [code: mono-outliers]
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

	* parenleft (U+0028): X=182.0,Y=738.0 (should be at cap-height 736?)

	* parenright (U+0029): X=330.0,Y=738.0 (should be at cap-height 736?)

	* G (U+0047): X=306.5,Y=-1.0 (should be at baseline 0?)

	* a (U+0061): X=146.0,Y=1.0 (should be at baseline 0?)

	* b (U+0062): X=209.0,Y=-1.0 (should be at baseline 0?)

	* d (U+0064): X=303.0,Y=-1.0 (should be at baseline 0?)

	* g (U+0067): X=303.0,Y=545.0 (should be at x-height 544?)

	* h (U+0068): X=219.5,Y=545.0 (should be at x-height 544?)

	* i (U+0069): X=202.5,Y=734.0 (should be at cap-height 736?)

	* i (U+0069): X=293.5,Y=734.0 (should be at cap-height 736?)

	* j (U+006A): X=242.5,Y=734.0 (should be at cap-height 736?)

	* j (U+006A): X=333.5,Y=734.0 (should be at cap-height 736?)

	* n (U+006E): X=217.5,Y=542.0 (should be at x-height 544?)

	* p (U+0070): X=209.0,Y=545.0 (should be at x-height 544?)

	* q (U+0071): X=303.0,Y=545.0 (should be at x-height 544?)

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

	* aring (U+00E5): X=201.5,Y=737.0 (should be at cap-height 736?)

	* aring (U+00E5): X=314.5,Y=737.0 (should be at cap-height 736?)

	* ae (U+00E6): X=461.5,Y=1.5 (should be at baseline 0?)

	* ae (U+00E6): X=38.5,Y=0.5 (should be at baseline 0?)

	* eth (U+00F0): X=299.5,Y=1.0 (should be at baseline 0?)

	* ugrave (U+00F9): X=294.5,Y=2.0 (should be at baseline 0?)

	* uacute (U+00FA): X=294.5,Y=2.0 (should be at baseline 0?)

	* ucircumflex (U+00FB): X=294.5,Y=2.0 (should be at baseline 0?)

	* udieresis (U+00FC): X=294.5,Y=2.0 (should be at baseline 0?)

	* thorn (U+00FE): X=212.5,Y=1.0 (should be at baseline 0?)

	* amacron (U+0101): X=146.0,Y=1.0 (should be at baseline 0?)

	* amacron (U+0101): X=106.0,Y=735.0 (should be at cap-height 736?)

	* amacron (U+0101): X=414.0,Y=735.0 (should be at cap-height 736?)

	* abreve (U+0103): X=146.0,Y=1.0 (should be at baseline 0?)

	* abreve (U+0103): X=143.0,Y=738.0 (should be at cap-height 736?)

	* abreve (U+0103): X=196.0,Y=738.0 (should be at cap-height 736?)

	* abreve (U+0103): X=310.0,Y=738.0 (should be at cap-height 736?)

	* abreve (U+0103): X=363.0,Y=738.0 (should be at cap-height 736?)

	* cdotaccent (U+010B): X=216.0,Y=735.5 (should be at cap-height 736?)

	* cdotaccent (U+010B): X=295.5,Y=735.5 (should be at cap-height 736?)

	* Gbreve (U+011E): X=306.5,Y=-1.0 (should be at baseline 0?)

	* gbreve (U+011F): X=151.0,Y=738.0 (should be at cap-height 736?)

	* gbreve (U+011F): X=204.0,Y=738.0 (should be at cap-height 736?)

	* gbreve (U+011F): X=318.0,Y=738.0 (should be at cap-height 736?)

	* gbreve (U+011F): X=371.0,Y=738.0 (should be at cap-height 736?)

	* Gdotaccent (U+0120): X=306.5,Y=-1.0 (should be at baseline 0?)

	* gdotaccent (U+0121): X=226.0,Y=735.5 (should be at cap-height 736?)

	* gdotaccent (U+0121): X=305.5,Y=735.5 (should be at cap-height 736?)

	* uni0122 (U+0122): X=306.5,Y=-1.0 (should be at baseline 0?)

	* oe (U+0153): X=455.5,Y=1.5 (should be at baseline 0?)

	* oe (U+0153): X=221.0,Y=-2.0 (should be at baseline 0?)

	* umacron (U+016B): X=294.5,Y=2.0 (should be at baseline 0?)

	* ubreve (U+016D): X=294.5,Y=2.0 (should be at baseline 0?)

	* uring (U+016F): X=294.5,Y=2.0 (should be at baseline 0?)

	* uhungarumlaut (U+0171): X=294.5,Y=2.0 (should be at baseline 0?)

	* uni0635 (U+0635): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0635 (U+0635): X=-32.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=-32.0,Y=-261.0 (should be at descender -260?)

	* uniFED3 (U+FED3): X=240.5,Y=735.5 (should be at cap-height 736?) 

	* And uniFED3 (U+FED3): X=319.5,Y=735.5 (should be at cap-height 736?) [code: found-misalignments]
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

	* And Ygrave (U+1EF2): L<<280.0,416.0>--<313.0,512.0>> -> L<<313.0,512.0>--<404.0,728.0>> [code: found-colinear-vectors]
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

	* parenleft (U+0028): X=316.0,Y=736.5 (should be at cap-height 736?)

	* parenright (U+0029): X=196.0,Y=736.5 (should be at cap-height 736?)

	* zero (U+0030): X=256.0,Y=735.0 (should be at cap-height 736?)

	* S (U+0053): X=256.0,Y=735.0 (should be at cap-height 736?)

	* a (U+0061): X=146.0,Y=1.0 (should be at baseline 0?)

	* a (U+0061): X=377.0,Y=525.0 (should be at x-height 527?)

	* b (U+0062): X=209.0,Y=-1.0 (should be at baseline 0?)

	* d (U+0064): X=303.0,Y=-1.0 (should be at baseline 0?)

	* g (U+0067): X=303.0,Y=528.0 (should be at x-height 527?)

	* h (U+0068): X=219.5,Y=528.0 (should be at x-height 527?)

	* j (U+006A): X=288.0,Y=735.0 (should be at cap-height 736?)

	* p (U+0070): X=209.0,Y=528.0 (should be at x-height 527?)

	* q (U+0071): X=303.0,Y=528.0 (should be at x-height 527?)

	* s (U+0073): X=130.0,Y=527.5 (should be at x-height 527?)

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

	* ae (U+00E6): X=461.5,Y=1.5 (should be at baseline 0?)

	* ae (U+00E6): X=38.5,Y=0.5 (should be at baseline 0?)

	* eth (U+00F0): X=299.5,Y=1.0 (should be at baseline 0?)

	* ugrave (U+00F9): X=294.5,Y=2.0 (should be at baseline 0?)

	* uacute (U+00FA): X=294.5,Y=2.0 (should be at baseline 0?)

	* ucircumflex (U+00FB): X=294.5,Y=2.0 (should be at baseline 0?)

	* udieresis (U+00FC): X=294.5,Y=2.0 (should be at baseline 0?)

	* thorn (U+00FE): X=212.5,Y=1.0 (should be at baseline 0?)

	* amacron (U+0101): X=146.0,Y=1.0 (should be at baseline 0?)

	* Abreve (U+0102): X=149.0,Y=938.0 (should be at ascender 940?)

	* Abreve (U+0102): X=185.0,Y=938.0 (should be at ascender 940?)

	* Abreve (U+0102): X=327.0,Y=938.0 (should be at ascender 940?)

	* Abreve (U+0102): X=363.0,Y=938.0 (should be at ascender 940?)

	* abreve (U+0103): X=146.0,Y=1.0 (should be at baseline 0?)

	* abreve (U+0103): X=144.0,Y=734.5 (should be at cap-height 736?)

	* abreve (U+0103): X=187.0,Y=734.5 (should be at cap-height 736?)

	* abreve (U+0103): X=311.0,Y=734.5 (should be at cap-height 736?)

	* abreve (U+0103): X=354.0,Y=734.5 (should be at cap-height 736?)

	* ccaron (U+010D): X=170.5,Y=738.0 (should be at cap-height 736?)

	* ccaron (U+010D): X=353.5,Y=738.0 (should be at cap-height 736?)

	* Gbreve (U+011E): X=149.0,Y=938.0 (should be at ascender 940?)

	* Gbreve (U+011E): X=185.0,Y=938.0 (should be at ascender 940?)

	* Gbreve (U+011E): X=327.0,Y=938.0 (should be at ascender 940?)

	* Gbreve (U+011E): X=363.0,Y=938.0 (should be at ascender 940?)

	* gbreve (U+011F): X=156.0,Y=734.5 (should be at cap-height 736?)

	* gbreve (U+011F): X=199.0,Y=734.5 (should be at cap-height 736?)

	* gbreve (U+011F): X=323.0,Y=734.5 (should be at cap-height 736?)

	* gbreve (U+011F): X=366.0,Y=734.5 (should be at cap-height 736?)

	* ncaron (U+0148): X=170.5,Y=738.0 (should be at cap-height 736?)

	* ncaron (U+0148): X=353.5,Y=738.0 (should be at cap-height 736?)

	* oe (U+0153): X=455.5,Y=1.5 (should be at baseline 0?)

	* oe (U+0153): X=221.0,Y=-2.0 (should be at baseline 0?)

	* rcaron (U+0159): X=179.5,Y=738.0 (should be at cap-height 736?)

	* rcaron (U+0159): X=362.5,Y=738.0 (should be at cap-height 736?)

	* Sacute (U+015A): X=256.0,Y=735.0 (should be at cap-height 736?)

	* Scaron (U+0160): X=256.0,Y=735.0 (should be at cap-height 736?)

	* Scaron (U+0160): X=136.0,Y=939.0 (should be at ascender 940?)

	* Scaron (U+0160): X=160.0,Y=939.0 (should be at ascender 940?)

	* Scaron (U+0160): X=352.0,Y=939.0 (should be at ascender 940?)

	* Scaron (U+0160): X=376.0,Y=939.0 (should be at ascender 940?)

	* scaron (U+0161): X=161.5,Y=738.0 (should be at cap-height 736?)

	* scaron (U+0161): X=344.5,Y=738.0 (should be at cap-height 736?)

	* umacron (U+016B): X=294.5,Y=2.0 (should be at baseline 0?)

	* Ubreve (U+016C): X=148.0,Y=938.0 (should be at ascender 940?)

	* Ubreve (U+016C): X=184.0,Y=938.0 (should be at ascender 940?)

	* Ubreve (U+016C): X=326.0,Y=938.0 (should be at ascender 940?)

	* Ubreve (U+016C): X=362.0,Y=938.0 (should be at ascender 940?)

	* ubreve (U+016D): X=294.5,Y=2.0 (should be at baseline 0?)

	* uring (U+016F): X=294.5,Y=2.0 (should be at baseline 0?)

	* uhungarumlaut (U+0171): X=294.5,Y=2.0 (should be at baseline 0?)

	* uni0635 (U+0635): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0635 (U+0635): X=-32.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=128.0,Y=-261.0 (should be at descender -260?)

	* uni0636 (U+0636): X=-32.0,Y=-261.0 (should be at descender -260?)

	* uni0686 (U+0686): X=272.0,Y=-262.0 (should be at descender -260?) 

	* And uni0686 (U+0686): X=384.0,Y=-262.0 (should be at descender -260?) [code: found-misalignments]
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

	* a (U+0061): X=146.0,Y=1.0 (should be at baseline 0?)

	* b (U+0062): X=209.0,Y=-1.0 (should be at baseline 0?)

	* d (U+0064): X=303.0,Y=-1.0 (should be at baseline 0?)

	* g (U+0067): X=303.0,Y=522.0 (should be at x-height 521?)

	* h (U+0068): X=219.5,Y=522.0 (should be at x-height 521?)

	* i (U+0069): X=234.0,Y=738.0 (should be at cap-height 736?)

	* p (U+0070): X=209.0,Y=522.0 (should be at x-height 521?)

	* q (U+0071): X=303.0,Y=522.0 (should be at x-height 521?)

	* u (U+0075): X=294.5,Y=2.0 (should be at baseline 0?)

	* w (U+0077): X=483.0,Y=519.0 (should be at x-height 521?)

	* copyright (U+00A9): X=370.0,Y=-0.5 (should be at baseline 0?)

	* copyright (U+00A9): X=142.5,Y=-0.5 (should be at baseline 0?)

	* newGlyph (U+00B5): X=184.0,Y=-1.5 (should be at baseline 0?)

	* agrave (U+00E0): X=146.0,Y=1.0 (should be at baseline 0?)

	* aacute (U+00E1): X=146.0,Y=1.0 (should be at baseline 0?)

	* acircumflex (U+00E2): X=146.0,Y=1.0 (should be at baseline 0?)

	* atilde (U+00E3): X=146.0,Y=1.0 (should be at baseline 0?)

	* adieresis (U+00E4): X=146.0,Y=1.0 (should be at baseline 0?)

	* aring (U+00E5): X=146.0,Y=1.0 (should be at baseline 0?)

	* aring (U+00E5): X=252.0,Y=735.0 (should be at cap-height 736?)

	* ae (U+00E6): X=461.5,Y=1.5 (should be at baseline 0?)

	* ae (U+00E6): X=38.5,Y=0.5 (should be at baseline 0?)

	* eth (U+00F0): X=299.5,Y=1.0 (should be at baseline 0?)

	* ugrave (U+00F9): X=294.5,Y=2.0 (should be at baseline 0?)

	* uacute (U+00FA): X=294.5,Y=2.0 (should be at baseline 0?)

	* ucircumflex (U+00FB): X=294.5,Y=2.0 (should be at baseline 0?)

	* udieresis (U+00FC): X=294.5,Y=2.0 (should be at baseline 0?)

	* thorn (U+00FE): X=212.5,Y=1.0 (should be at baseline 0?)

	* amacron (U+0101): X=146.0,Y=1.0 (should be at baseline 0?)

	* Abreve (U+0102): X=149.0,Y=939.0 (should be at ascender 940?)

	* Abreve (U+0102): X=185.0,Y=939.0 (should be at ascender 940?)

	* Abreve (U+0102): X=327.0,Y=939.0 (should be at ascender 940?)

	* Abreve (U+0102): X=363.0,Y=939.0 (should be at ascender 940?)

	* abreve (U+0103): X=146.0,Y=1.0 (should be at baseline 0?)

	* abreve (U+0103): X=156.0,Y=734.0 (should be at cap-height 736?)

	* abreve (U+0103): X=171.0,Y=734.0 (should be at cap-height 736?)

	* abreve (U+0103): X=323.0,Y=734.0 (should be at cap-height 736?)

	* abreve (U+0103): X=338.0,Y=734.0 (should be at cap-height 736?)

	* ccaron (U+010D): X=141.0,Y=734.0 (should be at cap-height 736?)

	* ccaron (U+010D): X=158.0,Y=734.0 (should be at cap-height 736?)

	* ccaron (U+010D): X=368.0,Y=734.0 (should be at cap-height 736?)

	* ccaron (U+010D): X=385.0,Y=734.0 (should be at cap-height 736?)

	* Gbreve (U+011E): X=149.0,Y=939.0 (should be at ascender 940?)

	* Gbreve (U+011E): X=185.0,Y=939.0 (should be at ascender 940?)

	* Gbreve (U+011E): X=327.0,Y=939.0 (should be at ascender 940?)

	* Gbreve (U+011E): X=363.0,Y=939.0 (should be at ascender 940?)

	* gbreve (U+011F): X=170.0,Y=734.0 (should be at cap-height 736?)

	* gbreve (U+011F): X=185.0,Y=734.0 (should be at cap-height 736?)

	* gbreve (U+011F): X=337.0,Y=734.0 (should be at cap-height 736?)

	* gbreve (U+011F): X=352.0,Y=734.0 (should be at cap-height 736?)

	* ncaron (U+0148): X=140.0,Y=734.0 (should be at cap-height 736?)

	* ncaron (U+0148): X=157.0,Y=734.0 (should be at cap-height 736?)

	* ncaron (U+0148): X=367.0,Y=734.0 (should be at cap-height 736?)

	* ncaron (U+0148): X=384.0,Y=734.0 (should be at cap-height 736?)

	* oe (U+0153): X=455.5,Y=1.5 (should be at baseline 0?)

	* oe (U+0153): X=221.0,Y=-2.0 (should be at baseline 0?)

	* rcaron (U+0159): X=149.0,Y=734.0 (should be at cap-height 736?)

	* rcaron (U+0159): X=166.0,Y=734.0 (should be at cap-height 736?)

	* rcaron (U+0159): X=376.0,Y=734.0 (should be at cap-height 736?)

	* rcaron (U+0159): X=393.0,Y=734.0 (should be at cap-height 736?)

	* scaron (U+0161): X=133.0,Y=734.0 (should be at cap-height 736?)

	* scaron (U+0161): X=150.0,Y=734.0 (should be at cap-height 736?)

	* scaron (U+0161): X=360.0,Y=734.0 (should be at cap-height 736?)

	* scaron (U+0161): X=377.0,Y=734.0 (should be at cap-height 736?)

	* umacron (U+016B): X=294.5,Y=2.0 (should be at baseline 0?)

	* Ubreve (U+016C): X=148.0,Y=939.0 (should be at ascender 940?)

	* Ubreve (U+016C): X=184.0,Y=939.0 (should be at ascender 940?)

	* Ubreve (U+016C): X=326.0,Y=939.0 (should be at ascender 940?)

	* Ubreve (U+016C): X=362.0,Y=939.0 (should be at ascender 940?)

	* ubreve (U+016D): X=294.5,Y=2.0 (should be at baseline 0?)

	* uring (U+016F): X=294.5,Y=2.0 (should be at baseline 0?)

	* uhungarumlaut (U+0171): X=294.5,Y=2.0 (should be at baseline 0?)

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
| 6 | 12 | 49 | 668 | 37 | 515 | 0 |
| 0% | 1% | 4% | 52% | 3% | 40% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
