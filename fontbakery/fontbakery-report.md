## Fontbakery report

Fontbakery version: 0.8.8

<details><summary><b>[15] HasubiMono-Medium.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** Font lacks NameID 13 (LICENSE DESCRIPTION). A proper licensing entry must be set. [code: missing]
</div></details><details><summary>🔥 <b>FAIL:</b> Version format is correct in 'name' table? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/version_format">com.google.fonts/check/name/version_format</a>)</summary><div>


* 🔥 **FAIL** The NameID.VERSION_STRING (nameID=5) value must follow the pattern "Version X.Y" with X.Y greater than or equal to 1.000. Current version string is: "Version 0.100; ttfautohint (v1.8.4.7-5d5b)" [code: bad-version-strings]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 272, but got 208 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>


* 🔥 **FAIL** OS/2 sTypoAscender (768) and hhea ascent (992) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** On monospaced fonts, the value of post.isFixedPitch must be set to a non-zero value (meaning 'fixed width monospaced'), but got 0 instead. [code: mono-bad-post-isFixedPitch]
* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** Font is monospaced but 283 glyphs (74.08%) have a different width. You should check the widths of: ['A', 'Aacute', 'Acircumflex', 'Adieresis', 'Agrave', 'Aring', 'Atilde', 'B', 'C', 'Ccedilla', 'D', 'Eth', 'E', 'Eacute', 'Ecircumflex', 'Edieresis', 'Egrave', 'F', 'G', 'H', 'I', 'Iacute', 'Icircumflex', 'Idieresis', 'Igrave', 'J', 'K', 'L', 'M', 'N', 'Ntilde', 'O', 'Oacute', 'Ocircumflex', 'Odieresis', 'Ograve', 'Oslash', 'Otilde', 'OE', 'P', 'Thorn', 'Q', 'R', 'S', 'T', 'U', 'Uacute', 'Ucircumflex', 'Udieresis', 'Ugrave', 'V', 'W', 'X', 'Y', 'Yacute', 'Z', 'a', 'aacute', 'acircumflex', 'adieresis', 'agrave', 'aring', 'atilde', 'ae', 'b', 'c', 'ccedilla', 'd', 'eth', 'e', 'eacute', 'ecircumflex', 'edieresis', 'egrave', 'f', 'g', 'h', 'i', 'dotlessi', 'iacute', 'icircumflex', 'idieresis', 'igrave', 'j', 'k', 'l', 'm', 'n', 'ntilde', 'o', 'oacute', 'ocircumflex', 'odieresis', 'ograve', 'oslash', 'otilde', 'oe', 'p', 'thorn', 'q', 'r', 's', 'germandbls', 't', 'u', 'uacute', 'ucircumflex', 'udieresis', 'ugrave', 'v', 'w', 'x', 'y', 'yacute', 'ydieresis', 'z', 'ordfeminine', 'ordmasculine', 'uni0621', 'uni0627', 'uniFE8E', 'uni0623', 'uniFE84', 'uni0625', 'uniFE88', 'uni066E', 'uni066E.fina', 'uni066E.medi', 'uni066E.init', 'uni0628', 'uniFE90', 'uniFE92', 'uniFE91', 'uni062A', 'uniFE96', 'uniFE98', 'uniFE97', 'uni062B', 'uniFE9A', 'uniFE9C', 'uniFE9B', 'uniFEA0', 'uniFE9F', 'uni062D', 'uniFEA2', 'uniFEA4', 'uniFEA3', 'uni062E', 'uniFEA6', 'uniFEA8', 'uniFEA7', 'uni062F', 'uniFEAA', 'uni0630', 'uniFEAC', 'uni0631', 'uni0633', 'uniFEB2', 'uniFEB4', 'uniFEB3', 'uni0634', 'uniFEB6', 'uniFEB8', 'uniFEB7', 'uniFECC', 'uniFED3', 'uni06A1.init', 'uniFEDC', 'uniFEDB', 'uni0646', 'uniFEE6', 'uniFEE8', 'uniFEE7', 'uni06BA', 'uniFB9F', 'uni0648', 'uniFEEE', 'uniFEF4', 'uniFEF3', 'uni0640', 'uniFEFB', 'uniFEFC', 'uni0660', 'uni0661', 'uni0662', 'uni0663', 'uni0664', 'uni0665', 'uni0666', 'uni0667', 'uni0668', 'uni0669', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'fraction', 'onehalf', 'onequarter', 'threequarters', 'uni00B9', 'uni00B2', 'uni00B3', 'uni2074', 'space', 'uni00A0', 'period', 'comma', 'colon', 'semicolon', 'ellipsis', 'exclam', 'exclamdown', 'question', 'questiondown', 'periodcentered', 'bullet', 'asterisk', 'numbersign', 'slash', 'backslash', 'hyphen', 'endash', 'emdash', 'underscore', 'parenleft', 'parenright', 'braceleft', 'braceright', 'bracketleft', 'bracketright', 'quotesinglbase', 'quotedblbase', 'quotedblleft', 'quotedblright', 'quoteleft', 'quoteright', 'guillemotleft', 'guillemotright', 'guilsinglleft', 'guilsinglright', 'quotedbl', 'quotesingle', 'at', 'ampersand', 'paragraph', 'section', 'copyright', 'registered', 'degree', 'bar', 'brokenbar', 'cent', 'dollar', 'Euro', 'sterling', 'yen', 'plus', 'minus', 'multiply', 'divide', 'equal', 'greater', 'less', 'plusminus', 'asciitilde', 'asciicircum', 'newGlyph', 'percent', 'dieresis', 'grave', 'acute', 'circumflex', 'ring', 'tilde', 'macron', 'cedilla'] [code: mono-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uniFE9F
	- uniFEFB
	- uniFEF9
	- gafsarkashcenterar
	- gafsarkashabovear
	- uniFEA0
	- twodotsverticalabovear
	- uniFEF5
	- miniKehehar
	- twodotsverticalbelowar
	- threedotsdownbelowar
	- uniFEF3
	- uniFEF7
	- lam_alefWaslaar
	- threedotsdowncenterar
	- threedotsdownabovear
	- waslaar
	- dotcenterar
	- doublestrokear 
	- And threedotsupbelowar
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: onequarter	Contours detected: 1	Expected: 3 or 4
	- Glyph name: onehalf	Contours detected: 1	Expected: 3
	- Glyph name: threequarters	Contours detected: 1	Expected: 3 or 4
	- Glyph name: oslash	Contours detected: 2	Expected: 3
	- Glyph name: onehalf	Contours detected: 1	Expected: 3
	- Glyph name: onequarter	Contours detected: 1	Expected: 3 or 4
	- Glyph name: oslash	Contours detected: 2	Expected: 3 
	- And Glyph name: threequarters	Contours detected: 1	Expected: 3 or 4
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/hhea.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* ⚠ **WARN** OS/2 sTypoLineGap is not equal to 0. [code: OS/2]
</div></details><details><summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info">com.google.fonts/check/gpos_kerning_info</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* ampersand (U+0026): X=233.5,Y=1.5 (should be at baseline 0?)
	* parenleft (U+0028): X=224.0,Y=1.0 (should be at baseline 0?)
	* parenright (U+0029): X=296.0,Y=1.0 (should be at baseline 0?)
	* at (U+0040): X=349.5,Y=705.5 (should be at cap-height 704?)
	* W (U+0057): X=407.0,Y=703.0 (should be at cap-height 704?)
	* backslash (U+005C): X=71.0,Y=703.0 (should be at cap-height 704?)
	* backslash (U+005C): X=441.0,Y=-207.0 (should be at descender -208?)
	* a (U+0061): X=135.0,Y=0.5 (should be at baseline 0?)
	* a (U+0061): X=340.0,Y=510.0 (should be at x-height 512?)
	* j (U+006A): X=242.5,Y=702.0 (should be at cap-height 704?)
	* j (U+006A): X=333.5,Y=702.0 (should be at cap-height 704?)
	* m (U+006D): X=166.0,Y=510.5 (should be at x-height 512?)
	* m (U+006D): X=257.0,Y=510.5 (should be at x-height 512?)
	* m (U+006D): X=321.0,Y=510.5 (should be at x-height 512?)
	* p (U+0070): X=195.0,Y=510.0 (should be at x-height 512?)
	* q (U+0071): X=317.5,Y=510.0 (should be at x-height 512?)
	* s (U+0073): X=351.5,Y=-2.0 (should be at baseline 0?)
	* w (U+0077): X=416.0,Y=511.0 (should be at x-height 512?)
	* sterling (U+00A3): X=371.0,Y=769.5 (should be at ascender 768?)
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
	* oe (U+0153): X=455.5,Y=1.5 (should be at baseline 0?)
	* oe (U+0153): X=221.0,Y=-2.0 (should be at baseline 0?)
	* ring (U+02DA): X=199.5,Y=705.0 (should be at cap-height 704?)
	* ring (U+02DA): X=312.5,Y=705.0 (should be at cap-height 704?)
	* uni030A (U+030A): X=199.5,Y=705.0 (should be at cap-height 704?)
	* uni030A (U+030A): X=312.5,Y=705.0 (should be at cap-height 704?) and Euro (U+20AC): X=371.0,Y=769.5 (should be at ascender 768?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:
	* W (U+0057): L<<150.0,97.0>--<197.0,426.0>> -> L<<197.0,426.0>--<216.0,504.0>>
	* W (U+0057): L<<373.0,97.0>--<394.0,590.0>> -> L<<394.0,590.0>--<407.0,703.0>>
	* W (U+0057): L<<82.0,8.0>--<36.0,688.0>> -> L<<36.0,688.0>--<36.0,696.0>>
	* backslash (U+005C): L<<148.0,697.0>--<395.0,-40.0>> -> L<<395.0,-40.0>--<441.0,-207.0>>
	* backslash (U+005C): L<<364.0,-201.0>--<117.0,536.0>> -> L<<117.0,536.0>--<71.0,703.0>> and w (U+0077): L<<364.0,97.0>--<403.0,432.0>> -> L<<403.0,432.0>--<416.0,511.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:
 * newGlyph (U+00B5): L<<59.0,-208.0>--<58.0,513.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[16] HasubiMono-ExtraBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** Font lacks NameID 13 (LICENSE DESCRIPTION). A proper licensing entry must be set. [code: missing]
</div></details><details><summary>🔥 <b>FAIL:</b> Version format is correct in 'name' table? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/version_format">com.google.fonts/check/name/version_format</a>)</summary><div>


* 🔥 **FAIL** The NameID.VERSION_STRING (nameID=5) value must follow the pattern "Version X.Y" with X.Y greater than or equal to 1.000. Current version string is: "Version 0.100; ttfautohint (v1.8.4.7-5d5b)" [code: bad-version-strings]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 272, but got 208 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>


* 🔥 **FAIL** OS/2 sTypoAscender (768) and hhea ascent (992) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** On monospaced fonts, the value of post.isFixedPitch must be set to a non-zero value (meaning 'fixed width monospaced'), but got 0 instead. [code: mono-bad-post-isFixedPitch]
* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** Font is monospaced but 283 glyphs (74.08%) have a different width. You should check the widths of: ['A', 'Aacute', 'Acircumflex', 'Adieresis', 'Agrave', 'Aring', 'Atilde', 'B', 'C', 'Ccedilla', 'D', 'Eth', 'E', 'Eacute', 'Ecircumflex', 'Edieresis', 'Egrave', 'F', 'G', 'H', 'I', 'Iacute', 'Icircumflex', 'Idieresis', 'Igrave', 'J', 'K', 'L', 'M', 'N', 'Ntilde', 'O', 'Oacute', 'Ocircumflex', 'Odieresis', 'Ograve', 'Oslash', 'Otilde', 'OE', 'P', 'Thorn', 'Q', 'R', 'S', 'T', 'U', 'Uacute', 'Ucircumflex', 'Udieresis', 'Ugrave', 'V', 'W', 'X', 'Y', 'Yacute', 'Z', 'a', 'aacute', 'acircumflex', 'adieresis', 'agrave', 'aring', 'atilde', 'ae', 'b', 'c', 'ccedilla', 'd', 'eth', 'e', 'eacute', 'ecircumflex', 'edieresis', 'egrave', 'f', 'g', 'h', 'i', 'dotlessi', 'iacute', 'icircumflex', 'idieresis', 'igrave', 'j', 'k', 'l', 'm', 'n', 'ntilde', 'o', 'oacute', 'ocircumflex', 'odieresis', 'ograve', 'oslash', 'otilde', 'oe', 'p', 'thorn', 'q', 'r', 's', 'germandbls', 't', 'u', 'uacute', 'ucircumflex', 'udieresis', 'ugrave', 'v', 'w', 'x', 'y', 'yacute', 'ydieresis', 'z', 'ordfeminine', 'ordmasculine', 'uni0621', 'uni0627', 'uniFE8E', 'uni0623', 'uniFE84', 'uni0625', 'uniFE88', 'uni066E', 'uni066E.fina', 'uni066E.medi', 'uni066E.init', 'uni0628', 'uniFE90', 'uniFE92', 'uniFE91', 'uni062A', 'uniFE96', 'uniFE98', 'uniFE97', 'uni062B', 'uniFE9A', 'uniFE9C', 'uniFE9B', 'uniFEA0', 'uniFE9F', 'uni062D', 'uniFEA2', 'uniFEA4', 'uniFEA3', 'uni062E', 'uniFEA6', 'uniFEA8', 'uniFEA7', 'uni062F', 'uniFEAA', 'uni0630', 'uniFEAC', 'uni0631', 'uni0633', 'uniFEB2', 'uniFEB4', 'uniFEB3', 'uni0634', 'uniFEB6', 'uniFEB8', 'uniFEB7', 'uniFECC', 'uniFED3', 'uni06A1.init', 'uniFEDC', 'uniFEDB', 'uni0646', 'uniFEE6', 'uniFEE8', 'uniFEE7', 'uni06BA', 'uniFB9F', 'uni0648', 'uniFEEE', 'uniFEF4', 'uniFEF3', 'uni0640', 'uniFEFB', 'uniFEFC', 'uni0660', 'uni0661', 'uni0662', 'uni0663', 'uni0664', 'uni0665', 'uni0666', 'uni0667', 'uni0668', 'uni0669', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'fraction', 'onehalf', 'onequarter', 'threequarters', 'uni00B9', 'uni00B2', 'uni00B3', 'uni2074', 'space', 'uni00A0', 'period', 'comma', 'colon', 'semicolon', 'ellipsis', 'exclam', 'exclamdown', 'question', 'questiondown', 'periodcentered', 'bullet', 'asterisk', 'numbersign', 'slash', 'backslash', 'hyphen', 'endash', 'emdash', 'underscore', 'parenleft', 'parenright', 'braceleft', 'braceright', 'bracketleft', 'bracketright', 'quotesinglbase', 'quotedblbase', 'quotedblleft', 'quotedblright', 'quoteleft', 'quoteright', 'guillemotleft', 'guillemotright', 'guilsinglleft', 'guilsinglright', 'quotedbl', 'quotesingle', 'at', 'ampersand', 'paragraph', 'section', 'copyright', 'registered', 'degree', 'bar', 'brokenbar', 'cent', 'dollar', 'Euro', 'sterling', 'yen', 'plus', 'minus', 'multiply', 'divide', 'equal', 'greater', 'less', 'plusminus', 'asciitilde', 'asciicircum', 'newGlyph', 'percent', 'dieresis', 'grave', 'acute', 'circumflex', 'ring', 'tilde', 'macron', 'cedilla'] [code: mono-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Hasubi Mono ExtraBold' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uniFE9F
	- uniFEFB
	- uniFEF9
	- gafsarkashcenterar
	- gafsarkashabovear
	- uniFEA0
	- twodotsverticalabovear
	- uniFEF5
	- miniKehehar
	- twodotsverticalbelowar
	- threedotsdownbelowar
	- uniFEF3
	- uniFEF7
	- lam_alefWaslaar
	- threedotsdowncenterar
	- threedotsdownabovear
	- waslaar
	- dotcenterar
	- doublestrokear 
	- And threedotsupbelowar
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: onequarter	Contours detected: 1	Expected: 3 or 4
	- Glyph name: onehalf	Contours detected: 1	Expected: 3
	- Glyph name: threequarters	Contours detected: 1	Expected: 3 or 4
	- Glyph name: oslash	Contours detected: 2	Expected: 3
	- Glyph name: onehalf	Contours detected: 1	Expected: 3
	- Glyph name: onequarter	Contours detected: 1	Expected: 3 or 4
	- Glyph name: oslash	Contours detected: 2	Expected: 3 
	- And Glyph name: threequarters	Contours detected: 1	Expected: 3 or 4
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/hhea.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* ⚠ **WARN** OS/2 sTypoLineGap is not equal to 0. [code: OS/2]
</div></details><details><summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info">com.google.fonts/check/gpos_kerning_info</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* ampersand (U+0026): X=233.5,Y=1.5 (should be at baseline 0?)
	* parenleft (U+0028): X=224.0,Y=1.0 (should be at baseline 0?)
	* parenright (U+0029): X=296.0,Y=1.0 (should be at baseline 0?)
	* at (U+0040): X=349.5,Y=705.5 (should be at cap-height 704?)
	* W (U+0057): X=483.0,Y=702.0 (should be at cap-height 704?)
	* backslash (U+005C): X=369.0,Y=-206.0 (should be at descender -208?)
	* backslash (U+005C): X=143.0,Y=702.0 (should be at cap-height 704?)
	* a (U+0061): X=135.0,Y=0.5 (should be at baseline 0?)
	* a (U+0061): X=340.0,Y=510.0 (should be at x-height 512?)
	* b (U+0062): X=212.0,Y=514.0 (should be at x-height 512?)
	* b (U+0062): X=215.5,Y=-1.0 (should be at baseline 0?)
	* c (U+0063): X=354.5,Y=510.5 (should be at x-height 512?)
	* d (U+0064): X=296.5,Y=-1.0 (should be at baseline 0?)
	* d (U+0064): X=300.0,Y=514.0 (should be at x-height 512?)
	* j (U+006A): X=242.5,Y=702.0 (should be at cap-height 704?)
	* j (U+006A): X=333.5,Y=702.0 (should be at cap-height 704?)
	* m (U+006D): X=166.0,Y=510.5 (should be at x-height 512?)
	* m (U+006D): X=257.0,Y=510.5 (should be at x-height 512?)
	* m (U+006D): X=321.0,Y=510.5 (should be at x-height 512?)
	* p (U+0070): X=195.0,Y=510.0 (should be at x-height 512?)
	* q (U+0071): X=317.5,Y=510.0 (should be at x-height 512?)
	* s (U+0073): X=172.5,Y=-1.5 (should be at baseline 0?)
	* s (U+0073): X=350.5,Y=-2.0 (should be at baseline 0?)
	* w (U+0077): X=483.0,Y=510.0 (should be at x-height 512?)
	* sterling (U+00A3): X=371.0,Y=769.5 (should be at ascender 768?)
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
	* oe (U+0153): X=455.5,Y=1.5 (should be at baseline 0?)
	* oe (U+0153): X=221.0,Y=-2.0 (should be at baseline 0?)
	* ring (U+02DA): X=199.5,Y=705.0 (should be at cap-height 704?)
	* ring (U+02DA): X=312.5,Y=705.0 (should be at cap-height 704?)
	* uni030A (U+030A): X=199.5,Y=705.0 (should be at cap-height 704?)
	* uni030A (U+030A): X=312.5,Y=705.0 (should be at cap-height 704?) and Euro (U+20AC): X=371.0,Y=769.5 (should be at ascender 768?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:
	* W (U+0057): L<<100.0,696.0>--<106.0,519.0>> -> L<<106.0,519.0>--<137.0,100.0>>
	* W (U+0057): L<<137.0,100.0>--<164.0,215.0>> -> L<<164.0,215.0>--<216.0,504.0>>
	* W (U+0057): L<<293.0,507.0>--<314.0,387.0>> -> L<<314.0,387.0>--<368.0,100.0>>
	* W (U+0057): L<<368.0,100.0>--<386.0,272.0>> -> L<<386.0,272.0>--<415.0,698.0>>
	* W (U+0057): L<<77.0,8.0>--<24.0,688.0>> -> L<<24.0,688.0>--<24.0,696.0>>
	* backslash (U+005C): L<<143.0,702.0>--<234.0,440.0>> -> L<<234.0,440.0>--<446.0,-202.0>>
	* backslash (U+005C): L<<369.0,-206.0>--<278.0,56.0>> -> L<<278.0,56.0>--<66.0,698.0>>
	* w (U+0077): L<<139.0,100.0>--<166.0,180.0>> -> L<<166.0,180.0>--<218.0,333.0>> and w (U+0077): L<<96.0,504.0>--<109.0,382.0>> -> L<<109.0,382.0>--<139.0,100.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:
 * newGlyph (U+00B5): L<<59.0,-208.0>--<58.0,513.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[20] HasubiMono-Bold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** Font lacks NameID 13 (LICENSE DESCRIPTION). A proper licensing entry must be set. [code: missing]
</div></details><details><summary>🔥 <b>FAIL:</b> Version format is correct in 'name' table? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/version_format">com.google.fonts/check/name/version_format</a>)</summary><div>


* 🔥 **FAIL** The NameID.VERSION_STRING (nameID=5) value must follow the pattern "Version X.Y" with X.Y greater than or equal to 1.000. Current version string is: "Version 0.100; ttfautohint (v1.8.4.7-5d5b)" [code: bad-version-strings]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 fsSelection value. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fsselection">com.google.fonts/check/fsselection</a>)</summary><div>


* 🔥 **FAIL** OS/2 fsSelection REGULAR bit should be unset. [code: bad-REGULAR]
* 🔥 **FAIL** OS/2 fsSelection BOLD bit should be set. [code: bad-BOLD]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking head.macStyle value. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/mac_style">com.google.fonts/check/mac_style</a>)</summary><div>


* 🔥 **FAIL** head macStyle BOLD bit should be set. [code: bad-BOLD]
</div></details><details><summary>🔥 <b>FAIL:</b> Check name table: FONT_FAMILY_NAME entries. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/familyname">com.google.fonts/check/name/familyname</a>)</summary><div>


* 🔥 **FAIL** Entry [FONT_FAMILY_NAME(1):WINDOWS(3)] on the "name" table: Expected "Hasubi Mono" but got "Hasubi Mono Bold". [code: mismatch]
</div></details><details><summary>🔥 <b>FAIL:</b> Check name table: FONT_SUBFAMILY_NAME entries. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/subfamilyname">com.google.fonts/check/name/subfamilyname</a>)</summary><div>


* 🔥 **FAIL** SUBFAMILY_NAME for Win "Regular" must be "Bold" [code: bad-familyname]
</div></details><details><summary>🔥 <b>FAIL:</b> Check name table: TYPOGRAPHIC_FAMILY_NAME entries. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/typographicfamilyname">com.google.fonts/check/name/typographicfamilyname</a>)</summary><div>


* 🔥 **FAIL** Font style is "Bold" and, for that reason, it is not expected to have a [TYPOGRAPHIC_FAMILY_NAME(16):WINDOWS(3)] entry! [code: ribbi]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 272, but got 208 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>


* 🔥 **FAIL** OS/2 sTypoAscender (768) and hhea ascent (992) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** On monospaced fonts, the value of post.isFixedPitch must be set to a non-zero value (meaning 'fixed width monospaced'), but got 0 instead. [code: mono-bad-post-isFixedPitch]
* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** Font is monospaced but 283 glyphs (74.08%) have a different width. You should check the widths of: ['A', 'Aacute', 'Acircumflex', 'Adieresis', 'Agrave', 'Aring', 'Atilde', 'B', 'C', 'Ccedilla', 'D', 'Eth', 'E', 'Eacute', 'Ecircumflex', 'Edieresis', 'Egrave', 'F', 'G', 'H', 'I', 'Iacute', 'Icircumflex', 'Idieresis', 'Igrave', 'J', 'K', 'L', 'M', 'N', 'Ntilde', 'O', 'Oacute', 'Ocircumflex', 'Odieresis', 'Ograve', 'Oslash', 'Otilde', 'OE', 'P', 'Thorn', 'Q', 'R', 'S', 'T', 'U', 'Uacute', 'Ucircumflex', 'Udieresis', 'Ugrave', 'V', 'W', 'X', 'Y', 'Yacute', 'Z', 'a', 'aacute', 'acircumflex', 'adieresis', 'agrave', 'aring', 'atilde', 'ae', 'b', 'c', 'ccedilla', 'd', 'eth', 'e', 'eacute', 'ecircumflex', 'edieresis', 'egrave', 'f', 'g', 'h', 'i', 'dotlessi', 'iacute', 'icircumflex', 'idieresis', 'igrave', 'j', 'k', 'l', 'm', 'n', 'ntilde', 'o', 'oacute', 'ocircumflex', 'odieresis', 'ograve', 'oslash', 'otilde', 'oe', 'p', 'thorn', 'q', 'r', 's', 'germandbls', 't', 'u', 'uacute', 'ucircumflex', 'udieresis', 'ugrave', 'v', 'w', 'x', 'y', 'yacute', 'ydieresis', 'z', 'ordfeminine', 'ordmasculine', 'uni0621', 'uni0627', 'uniFE8E', 'uni0623', 'uniFE84', 'uni0625', 'uniFE88', 'uni066E', 'uni066E.fina', 'uni066E.medi', 'uni066E.init', 'uni0628', 'uniFE90', 'uniFE92', 'uniFE91', 'uni062A', 'uniFE96', 'uniFE98', 'uniFE97', 'uni062B', 'uniFE9A', 'uniFE9C', 'uniFE9B', 'uniFEA0', 'uniFE9F', 'uni062D', 'uniFEA2', 'uniFEA4', 'uniFEA3', 'uni062E', 'uniFEA6', 'uniFEA8', 'uniFEA7', 'uni062F', 'uniFEAA', 'uni0630', 'uniFEAC', 'uni0631', 'uni0633', 'uniFEB2', 'uniFEB4', 'uniFEB3', 'uni0634', 'uniFEB6', 'uniFEB8', 'uniFEB7', 'uniFECC', 'uniFED3', 'uni06A1.init', 'uniFEDC', 'uniFEDB', 'uni0646', 'uniFEE6', 'uniFEE8', 'uniFEE7', 'uni06BA', 'uniFB9F', 'uni0648', 'uniFEEE', 'uniFEF4', 'uniFEF3', 'uni0640', 'uniFEFB', 'uniFEFC', 'uni0660', 'uni0661', 'uni0662', 'uni0663', 'uni0664', 'uni0665', 'uni0666', 'uni0667', 'uni0668', 'uni0669', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'fraction', 'onehalf', 'onequarter', 'threequarters', 'uni00B9', 'uni00B2', 'uni00B3', 'uni2074', 'space', 'uni00A0', 'period', 'comma', 'colon', 'semicolon', 'ellipsis', 'exclam', 'exclamdown', 'question', 'questiondown', 'periodcentered', 'bullet', 'asterisk', 'numbersign', 'slash', 'backslash', 'hyphen', 'endash', 'emdash', 'underscore', 'parenleft', 'parenright', 'braceleft', 'braceright', 'bracketleft', 'bracketright', 'quotesinglbase', 'quotedblbase', 'quotedblleft', 'quotedblright', 'quoteleft', 'quoteright', 'guillemotleft', 'guillemotright', 'guilsinglleft', 'guilsinglright', 'quotedbl', 'quotesingle', 'at', 'ampersand', 'paragraph', 'section', 'copyright', 'registered', 'degree', 'bar', 'brokenbar', 'cent', 'dollar', 'Euro', 'sterling', 'yen', 'plus', 'minus', 'multiply', 'divide', 'equal', 'greater', 'less', 'plusminus', 'asciitilde', 'asciicircum', 'newGlyph', 'percent', 'dieresis', 'grave', 'acute', 'circumflex', 'ring', 'tilde', 'macron', 'cedilla'] [code: mono-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uniFE9F
	- uniFEFB
	- uniFEF9
	- gafsarkashcenterar
	- gafsarkashabovear
	- uniFEA0
	- twodotsverticalabovear
	- uniFEF5
	- miniKehehar
	- twodotsverticalbelowar
	- threedotsdownbelowar
	- uniFEF3
	- uniFEF7
	- lam_alefWaslaar
	- threedotsdowncenterar
	- threedotsdownabovear
	- waslaar
	- dotcenterar
	- doublestrokear 
	- And threedotsupbelowar
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: onequarter	Contours detected: 1	Expected: 3 or 4
	- Glyph name: onehalf	Contours detected: 1	Expected: 3
	- Glyph name: threequarters	Contours detected: 1	Expected: 3 or 4
	- Glyph name: oslash	Contours detected: 2	Expected: 3
	- Glyph name: onehalf	Contours detected: 1	Expected: 3
	- Glyph name: onequarter	Contours detected: 1	Expected: 3 or 4
	- Glyph name: oslash	Contours detected: 2	Expected: 3 
	- And Glyph name: threequarters	Contours detected: 1	Expected: 3 or 4
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/hhea.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* ⚠ **WARN** OS/2 sTypoLineGap is not equal to 0. [code: OS/2]
</div></details><details><summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info">com.google.fonts/check/gpos_kerning_info</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


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
	* sterling (U+00A3): X=371.0,Y=769.5 (should be at ascender 768?)
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
	* oe (U+0153): X=455.5,Y=1.5 (should be at baseline 0?)
	* oe (U+0153): X=221.0,Y=-2.0 (should be at baseline 0?)
	* ring (U+02DA): X=199.5,Y=705.0 (should be at cap-height 704?)
	* ring (U+02DA): X=312.5,Y=705.0 (should be at cap-height 704?)
	* uni030A (U+030A): X=199.5,Y=705.0 (should be at cap-height 704?)
	* uni030A (U+030A): X=312.5,Y=705.0 (should be at cap-height 704?)
	* uni0628 (U+0628): X=306.0,Y=-206.0 (should be at descender -208?)
	* uni0628 (U+0628): X=306.0,Y=-206.0 (should be at descender -208?) and Euro (U+20AC): X=371.0,Y=769.5 (should be at ascender 768?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:
	* W (U+0057): L<<104.0,696.0>--<114.0,413.0>> -> L<<114.0,413.0>--<141.0,99.0>>
	* W (U+0057): L<<141.0,99.0>--<175.0,285.0>> -> L<<175.0,285.0>--<216.0,504.0>>
	* W (U+0057): L<<295.0,505.0>--<325.0,315.0>> -> L<<325.0,315.0>--<370.0,99.0>>
	* W (U+0057): L<<370.0,99.0>--<389.0,378.0>> -> L<<389.0,378.0>--<412.0,700.0>>
	* W (U+0057): L<<79.0,8.0>--<28.0,688.0>> -> L<<28.0,688.0>--<28.0,696.0>>
	* backslash (U+005C): L<<145.0,700.0>--<288.0,280.0>> -> L<<288.0,280.0>--<444.0,-204.0>>
	* backslash (U+005C): L<<367.0,-204.0>--<224.0,216.0>> -> L<<224.0,216.0>--<68.0,700.0>>
	* w (U+0077): L<<145.0,99.0>--<179.0,229.0>> -> L<<179.0,229.0>--<220.0,345.0>>
	* w (U+0077): L<<365.0,99.0>--<394.0,289.0>> -> L<<394.0,289.0>--<417.0,508.0>> and w (U+0077): L<<99.0,504.0>--<119.0,310.0>> -> L<<119.0,310.0>--<145.0,99.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:
 * newGlyph (U+00B5): L<<59.0,-208.0>--<58.0,513.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[18] HasubiMono-Heavy.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking file is named canonically. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/canonical_filename">com.google.fonts/check/canonical_filename</a>)</summary><div>


* 🔥 **FAIL** Style name used in "fonts/ttf/HasubiMono-Heavy.ttf" is not canonical. You should rebuild the font using any of the following style names: "Thin", "ExtraLight", "Light", "Regular", "Medium", "SemiBold", "Bold", "ExtraBold", "Black", "Thin Italic", "ExtraLight Italic", "Light Italic", "Italic", "Medium Italic", "SemiBold Italic", "Bold Italic", "ExtraBold Italic", "Black Italic". [code: bad-static-filename]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWeightClass. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/usweightclass">com.google.fonts/check/usweightclass</a>)</summary><div>


* 🔥 **FAIL** OS/2 usWeightClass is '900' when it should be '400'. [code: bad-value]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** Font lacks NameID 13 (LICENSE DESCRIPTION). A proper licensing entry must be set. [code: missing]
</div></details><details><summary>🔥 <b>FAIL:</b> Version format is correct in 'name' table? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/version_format">com.google.fonts/check/name/version_format</a>)</summary><div>


* 🔥 **FAIL** The NameID.VERSION_STRING (nameID=5) value must follow the pattern "Version X.Y" with X.Y greater than or equal to 1.000. Current version string is: "Version 0.100; ttfautohint (v1.8.4.7-5d5b)" [code: bad-version-strings]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 272, but got 208 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>


* 🔥 **FAIL** OS/2 sTypoAscender (768) and hhea ascent (992) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** On monospaced fonts, the value of post.isFixedPitch must be set to a non-zero value (meaning 'fixed width monospaced'), but got 0 instead. [code: mono-bad-post-isFixedPitch]
* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** Font is monospaced but 244 glyphs (63.87%) have a different width. You should check the widths of: ['A', 'Aacute', 'Acircumflex', 'Adieresis', 'Agrave', 'Aring', 'Atilde', 'B', 'C', 'Ccedilla', 'D', 'Eth', 'E', 'Eacute', 'Ecircumflex', 'Edieresis', 'Egrave', 'F', 'G', 'H', 'I', 'Iacute', 'Icircumflex', 'Idieresis', 'Igrave', 'J', 'K', 'L', 'M', 'N', 'Ntilde', 'O', 'Oacute', 'Ocircumflex', 'Odieresis', 'Ograve', 'Oslash', 'Otilde', 'OE', 'P', 'Thorn', 'Q', 'R', 'S', 'T', 'U', 'Uacute', 'Ucircumflex', 'Udieresis', 'Ugrave', 'V', 'W', 'X', 'Y', 'Yacute', 'Z', 'a', 'aacute', 'acircumflex', 'adieresis', 'agrave', 'aring', 'atilde', 'ae', 'b', 'c', 'ccedilla', 'd', 'eth', 'e', 'eacute', 'ecircumflex', 'edieresis', 'egrave', 'f', 'g', 'h', 'i', 'dotlessi', 'iacute', 'icircumflex', 'idieresis', 'igrave', 'j', 'k', 'l', 'm', 'n', 'ntilde', 'o', 'oacute', 'ocircumflex', 'odieresis', 'ograve', 'oslash', 'otilde', 'oe', 'p', 'thorn', 'q', 'r', 's', 'germandbls', 't', 'u', 'uacute', 'ucircumflex', 'udieresis', 'ugrave', 'v', 'w', 'x', 'y', 'yacute', 'ydieresis', 'z', 'ordfeminine', 'ordmasculine', 'uni0621', 'uni0627', 'uniFE8E', 'uni0623', 'uniFE84', 'uni0625', 'uniFE88', 'uni066E.medi', 'uniFE92', 'uniFE98', 'uniFE9C', 'uniFED3', 'uni06A1.init', 'uniFEDC', 'uniFEDB', 'uni0646', 'uniFEE6', 'uniFEE8', 'uni06BA', 'uniFB9F', 'uni0648', 'uniFEEE', 'uniFEF4', 'uni0640', 'uniFEFB', 'uniFEFC', 'uni0660', 'uni0661', 'uni0662', 'uni0663', 'uni0664', 'uni0665', 'uni0666', 'uni0667', 'uni0668', 'uni0669', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'fraction', 'onehalf', 'onequarter', 'threequarters', 'uni00B9', 'uni00B2', 'uni00B3', 'uni2074', 'space', 'uni00A0', 'period', 'comma', 'colon', 'semicolon', 'ellipsis', 'exclam', 'exclamdown', 'question', 'questiondown', 'periodcentered', 'bullet', 'asterisk', 'numbersign', 'slash', 'backslash', 'hyphen', 'endash', 'emdash', 'underscore', 'parenleft', 'parenright', 'braceleft', 'braceright', 'bracketleft', 'bracketright', 'quotesinglbase', 'quotedblbase', 'quotedblleft', 'quotedblright', 'quoteleft', 'quoteright', 'guillemotright', 'guilsinglleft', 'guilsinglright', 'quotedbl', 'quotesingle', 'at', 'ampersand', 'paragraph', 'section', 'copyright', 'registered', 'degree', 'bar', 'brokenbar', 'cent', 'dollar', 'Euro', 'sterling', 'yen', 'plus', 'minus', 'multiply', 'divide', 'equal', 'greater', 'less', 'plusminus', 'asciitilde', 'asciicircum', 'newGlyph', 'percent', 'dieresis', 'grave', 'acute', 'circumflex', 'ring', 'tilde', 'macron', 'cedilla'] [code: mono-outliers]
</div></details><details><summary>🔥 <b>FAIL:</b> Check glyphs do not have duplicate components which have the same x,y coordinates. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/glyf.html#com.google.fonts/check/glyf_non_transformed_duplicate_components">com.google.fonts/check/glyf_non_transformed_duplicate_components</a>)</summary><div>


* 🔥 **FAIL** The following glyphs have duplicate components which have the same x,y coordinates:
	* {'glyph': 'quotedblbase', 'component': 'comma', 'x': 0, 'y': 0} [code: found-duplicates]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uniFE9F
	- uniFEFB
	- uniFEF9
	- gafsarkashcenterar
	- gafsarkashabovear
	- uniFEA0
	- twodotsverticalabovear
	- uniFEF5
	- miniKehehar
	- twodotsverticalbelowar
	- threedotsdownbelowar
	- uniFEF3
	- uniFEF7
	- lam_alefWaslaar
	- threedotsdowncenterar
	- threedotsdownabovear
	- waslaar
	- dotcenterar
	- doublestrokear 
	- And threedotsupbelowar
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: onequarter	Contours detected: 1	Expected: 3 or 4
	- Glyph name: onehalf	Contours detected: 1	Expected: 3
	- Glyph name: threequarters	Contours detected: 1	Expected: 3 or 4
	- Glyph name: oslash	Contours detected: 2	Expected: 3
	- Glyph name: onehalf	Contours detected: 1	Expected: 3
	- Glyph name: onequarter	Contours detected: 1	Expected: 3 or 4
	- Glyph name: oslash	Contours detected: 2	Expected: 3 
	- And Glyph name: threequarters	Contours detected: 1	Expected: 3 or 4
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/hhea.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* ⚠ **WARN** OS/2 sTypoLineGap is not equal to 0. [code: OS/2]
</div></details><details><summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info">com.google.fonts/check/gpos_kerning_info</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


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
	* sterling (U+00A3): X=371.0,Y=769.5 (should be at ascender 768?)
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
	* oe (U+0153): X=455.5,Y=1.5 (should be at baseline 0?)
	* oe (U+0153): X=221.0,Y=-2.0 (should be at baseline 0?)
	* ring (U+02DA): X=199.5,Y=705.0 (should be at cap-height 704?)
	* ring (U+02DA): X=312.5,Y=705.0 (should be at cap-height 704?)
	* uni030A (U+030A): X=199.5,Y=705.0 (should be at cap-height 704?)
	* uni030A (U+030A): X=312.5,Y=705.0 (should be at cap-height 704?) and Euro (U+20AC): X=371.0,Y=769.5 (should be at ascender 768?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:
	* W (U+0057): L<<75.0,8.0>--<17.0,688.0>> -> L<<17.0,688.0>--<17.0,696.0>>
	* W (U+0057): L<<93.0,696.0>--<93.0,688.0>> -> L<<93.0,688.0>--<130.0,102.0>> and w (U+0077): L<<93.0,504.0>--<93.0,496.0>> -> L<<93.0,496.0>--<130.0,102.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:
 * newGlyph (U+00B5): L<<59.0,-208.0>--<58.0,513.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[15] HasubiMono-SemiBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** Font lacks NameID 13 (LICENSE DESCRIPTION). A proper licensing entry must be set. [code: missing]
</div></details><details><summary>🔥 <b>FAIL:</b> Version format is correct in 'name' table? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/version_format">com.google.fonts/check/name/version_format</a>)</summary><div>


* 🔥 **FAIL** The NameID.VERSION_STRING (nameID=5) value must follow the pattern "Version X.Y" with X.Y greater than or equal to 1.000. Current version string is: "Version 0.100; ttfautohint (v1.8.4.7-5d5b)" [code: bad-version-strings]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 272, but got 208 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>


* 🔥 **FAIL** OS/2 sTypoAscender (768) and hhea ascent (992) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** On monospaced fonts, the value of post.isFixedPitch must be set to a non-zero value (meaning 'fixed width monospaced'), but got 0 instead. [code: mono-bad-post-isFixedPitch]
* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** Font is monospaced but 283 glyphs (74.08%) have a different width. You should check the widths of: ['A', 'Aacute', 'Acircumflex', 'Adieresis', 'Agrave', 'Aring', 'Atilde', 'B', 'C', 'Ccedilla', 'D', 'Eth', 'E', 'Eacute', 'Ecircumflex', 'Edieresis', 'Egrave', 'F', 'G', 'H', 'I', 'Iacute', 'Icircumflex', 'Idieresis', 'Igrave', 'J', 'K', 'L', 'M', 'N', 'Ntilde', 'O', 'Oacute', 'Ocircumflex', 'Odieresis', 'Ograve', 'Oslash', 'Otilde', 'OE', 'P', 'Thorn', 'Q', 'R', 'S', 'T', 'U', 'Uacute', 'Ucircumflex', 'Udieresis', 'Ugrave', 'V', 'W', 'X', 'Y', 'Yacute', 'Z', 'a', 'aacute', 'acircumflex', 'adieresis', 'agrave', 'aring', 'atilde', 'ae', 'b', 'c', 'ccedilla', 'd', 'eth', 'e', 'eacute', 'ecircumflex', 'edieresis', 'egrave', 'f', 'g', 'h', 'i', 'dotlessi', 'iacute', 'icircumflex', 'idieresis', 'igrave', 'j', 'k', 'l', 'm', 'n', 'ntilde', 'o', 'oacute', 'ocircumflex', 'odieresis', 'ograve', 'oslash', 'otilde', 'oe', 'p', 'thorn', 'q', 'r', 's', 'germandbls', 't', 'u', 'uacute', 'ucircumflex', 'udieresis', 'ugrave', 'v', 'w', 'x', 'y', 'yacute', 'ydieresis', 'z', 'ordfeminine', 'ordmasculine', 'uni0621', 'uni0627', 'uniFE8E', 'uni0623', 'uniFE84', 'uni0625', 'uniFE88', 'uni066E', 'uni066E.fina', 'uni066E.medi', 'uni066E.init', 'uni0628', 'uniFE90', 'uniFE92', 'uniFE91', 'uni062A', 'uniFE96', 'uniFE98', 'uniFE97', 'uni062B', 'uniFE9A', 'uniFE9C', 'uniFE9B', 'uniFEA0', 'uniFE9F', 'uni062D', 'uniFEA2', 'uniFEA4', 'uniFEA3', 'uni062E', 'uniFEA6', 'uniFEA8', 'uniFEA7', 'uni062F', 'uniFEAA', 'uni0630', 'uniFEAC', 'uni0631', 'uni0633', 'uniFEB2', 'uniFEB4', 'uniFEB3', 'uni0634', 'uniFEB6', 'uniFEB8', 'uniFEB7', 'uniFECC', 'uniFED3', 'uni06A1.init', 'uniFEDC', 'uniFEDB', 'uni0646', 'uniFEE6', 'uniFEE8', 'uniFEE7', 'uni06BA', 'uniFB9F', 'uni0648', 'uniFEEE', 'uniFEF4', 'uniFEF3', 'uni0640', 'uniFEFB', 'uniFEFC', 'uni0660', 'uni0661', 'uni0662', 'uni0663', 'uni0664', 'uni0665', 'uni0666', 'uni0667', 'uni0668', 'uni0669', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'fraction', 'onehalf', 'onequarter', 'threequarters', 'uni00B9', 'uni00B2', 'uni00B3', 'uni2074', 'space', 'uni00A0', 'period', 'comma', 'colon', 'semicolon', 'ellipsis', 'exclam', 'exclamdown', 'question', 'questiondown', 'periodcentered', 'bullet', 'asterisk', 'numbersign', 'slash', 'backslash', 'hyphen', 'endash', 'emdash', 'underscore', 'parenleft', 'parenright', 'braceleft', 'braceright', 'bracketleft', 'bracketright', 'quotesinglbase', 'quotedblbase', 'quotedblleft', 'quotedblright', 'quoteleft', 'quoteright', 'guillemotleft', 'guillemotright', 'guilsinglleft', 'guilsinglright', 'quotedbl', 'quotesingle', 'at', 'ampersand', 'paragraph', 'section', 'copyright', 'registered', 'degree', 'bar', 'brokenbar', 'cent', 'dollar', 'Euro', 'sterling', 'yen', 'plus', 'minus', 'multiply', 'divide', 'equal', 'greater', 'less', 'plusminus', 'asciitilde', 'asciicircum', 'newGlyph', 'percent', 'dieresis', 'grave', 'acute', 'circumflex', 'ring', 'tilde', 'macron', 'cedilla'] [code: mono-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uniFE9F
	- uniFEFB
	- uniFEF9
	- gafsarkashcenterar
	- gafsarkashabovear
	- uniFEA0
	- twodotsverticalabovear
	- uniFEF5
	- miniKehehar
	- twodotsverticalbelowar
	- threedotsdownbelowar
	- uniFEF3
	- uniFEF7
	- lam_alefWaslaar
	- threedotsdowncenterar
	- threedotsdownabovear
	- waslaar
	- dotcenterar
	- doublestrokear 
	- And threedotsupbelowar
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: onequarter	Contours detected: 1	Expected: 3 or 4
	- Glyph name: onehalf	Contours detected: 1	Expected: 3
	- Glyph name: threequarters	Contours detected: 1	Expected: 3 or 4
	- Glyph name: oslash	Contours detected: 2	Expected: 3
	- Glyph name: onehalf	Contours detected: 1	Expected: 3
	- Glyph name: onequarter	Contours detected: 1	Expected: 3 or 4
	- Glyph name: oslash	Contours detected: 2	Expected: 3 
	- And Glyph name: threequarters	Contours detected: 1	Expected: 3 or 4
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/hhea.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* ⚠ **WARN** OS/2 sTypoLineGap is not equal to 0. [code: OS/2]
</div></details><details><summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info">com.google.fonts/check/gpos_kerning_info</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* ampersand (U+0026): X=233.5,Y=1.5 (should be at baseline 0?)
	* parenleft (U+0028): X=224.0,Y=1.0 (should be at baseline 0?)
	* parenright (U+0029): X=296.0,Y=1.0 (should be at baseline 0?)
	* at (U+0040): X=349.5,Y=705.5 (should be at cap-height 704?)
	* a (U+0061): X=135.0,Y=0.5 (should be at baseline 0?)
	* a (U+0061): X=340.0,Y=510.0 (should be at x-height 512?)
	* b (U+0062): X=212.5,Y=512.5 (should be at x-height 512?)
	* d (U+0064): X=299.5,Y=512.5 (should be at x-height 512?)
	* f (U+0066): X=259.5,Y=704.5 (should be at cap-height 704?)
	* j (U+006A): X=242.5,Y=702.0 (should be at cap-height 704?)
	* j (U+006A): X=333.5,Y=702.0 (should be at cap-height 704?)
	* m (U+006D): X=166.0,Y=510.5 (should be at x-height 512?)
	* m (U+006D): X=257.0,Y=510.5 (should be at x-height 512?)
	* m (U+006D): X=321.0,Y=510.5 (should be at x-height 512?)
	* p (U+0070): X=195.0,Y=510.0 (should be at x-height 512?)
	* q (U+0071): X=317.5,Y=510.0 (should be at x-height 512?)
	* s (U+0073): X=351.5,Y=-2.0 (should be at baseline 0?)
	* sterling (U+00A3): X=371.0,Y=769.5 (should be at ascender 768?)
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
	* oe (U+0153): X=455.5,Y=1.5 (should be at baseline 0?)
	* oe (U+0153): X=221.0,Y=-2.0 (should be at baseline 0?)
	* ring (U+02DA): X=199.5,Y=705.0 (should be at cap-height 704?)
	* ring (U+02DA): X=312.5,Y=705.0 (should be at cap-height 704?)
	* uni030A (U+030A): X=199.5,Y=705.0 (should be at cap-height 704?)
	* uni030A (U+030A): X=312.5,Y=705.0 (should be at cap-height 704?) and Euro (U+20AC): X=371.0,Y=769.5 (should be at ascender 768?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:
	* W (U+0057): L<<108.0,696.0>--<122.0,307.0>> -> L<<122.0,307.0>--<145.0,98.0>>
	* W (U+0057): L<<145.0,98.0>--<186.0,355.0>> -> L<<186.0,355.0>--<216.0,504.0>>
	* W (U+0057): L<<298.0,502.0>--<336.0,242.0>> -> L<<336.0,242.0>--<371.0,98.0>>
	* W (U+0057): L<<371.0,98.0>--<391.0,484.0>> -> L<<391.0,484.0>--<409.0,701.0>>
	* W (U+0057): L<<80.0,8.0>--<32.0,688.0>> -> L<<32.0,688.0>--<32.0,696.0>>
	* backslash (U+005C): L<<146.0,699.0>--<341.0,120.0>> -> L<<341.0,120.0>--<443.0,-205.0>>
	* backslash (U+005C): L<<366.0,-203.0>--<171.0,376.0>> -> L<<171.0,376.0>--<69.0,701.0>>
	* w (U+0077): L<<101.0,504.0>--<128.0,239.0>> -> L<<128.0,239.0>--<151.0,98.0>> and w (U+0077): L<<365.0,98.0>--<398.0,360.0>> -> L<<398.0,360.0>--<416.0,509.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:
 * newGlyph (U+00B5): L<<59.0,-208.0>--<58.0,513.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[15] HasubiMono-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** Font lacks NameID 13 (LICENSE DESCRIPTION). A proper licensing entry must be set. [code: missing]
</div></details><details><summary>🔥 <b>FAIL:</b> Version format is correct in 'name' table? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/version_format">com.google.fonts/check/name/version_format</a>)</summary><div>


* 🔥 **FAIL** The NameID.VERSION_STRING (nameID=5) value must follow the pattern "Version X.Y" with X.Y greater than or equal to 1.000. Current version string is: "Version 0.100; ttfautohint (v1.8.4.7-5d5b)" [code: bad-version-strings]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 272, but got 208 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>


* 🔥 **FAIL** OS/2 sTypoAscender (768) and hhea ascent (992) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** On monospaced fonts, the value of post.isFixedPitch must be set to a non-zero value (meaning 'fixed width monospaced'), but got 0 instead. [code: mono-bad-post-isFixedPitch]
* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** Font is monospaced but 43 glyphs (11.26%) have a different width. You should check the widths of: ['AE', 'uni0635', 'uniFEBA', 'uniFEBC', 'uniFEBB', 'uni0639', 'uniFECA', 'uniFECB', 'uni0641', 'uniFED2', 'uni06A4', 'uni06A1', 'uni06A1.fina', 'uni06A1.medi', 'uni066F', 'uni066F.fina', 'uni0643', 'uniFEDA', 'uni0647', 'uniFEEA', 'uniFEEC', 'uniFEEB', 'uni0624', 'uniFE86', 'uni0649', 'uniFEF0', 'uni064A', 'uni0626', 'uniFE8A', 'uniFE8C', 'uniFE8B', 'uniFEF7', 'uniFEF8', 'uniFEF9', 'uniFEFA', 'uniFEF5', 'uniFEF6', 'lam_alefWaslaar', 'lam_alefWaslaar.fina', 'uni066B', 'uni066C', 'uni2074', 'logicalnot'] [code: mono-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uniFE9F
	- uniFEFB
	- uniFEF9
	- gafsarkashcenterar
	- gafsarkashabovear
	- uniFEA0
	- twodotsverticalabovear
	- uniFEF5
	- miniKehehar
	- twodotsverticalbelowar
	- threedotsdownbelowar
	- uniFEF3
	- uniFEF7
	- lam_alefWaslaar
	- threedotsdowncenterar
	- threedotsdownabovear
	- waslaar
	- dotcenterar
	- doublestrokear 
	- And threedotsupbelowar
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: onequarter	Contours detected: 1	Expected: 3 or 4
	- Glyph name: onehalf	Contours detected: 1	Expected: 3
	- Glyph name: threequarters	Contours detected: 1	Expected: 3 or 4
	- Glyph name: oslash	Contours detected: 2	Expected: 3
	- Glyph name: onehalf	Contours detected: 1	Expected: 3
	- Glyph name: onequarter	Contours detected: 1	Expected: 3 or 4
	- Glyph name: oslash	Contours detected: 2	Expected: 3 
	- And Glyph name: threequarters	Contours detected: 1	Expected: 3 or 4
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/hhea.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* ⚠ **WARN** OS/2 sTypoLineGap is not equal to 0. [code: OS/2]
</div></details><details><summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info">com.google.fonts/check/gpos_kerning_info</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* ampersand (U+0026): X=233.5,Y=1.5 (should be at baseline 0?)
	* parenleft (U+0028): X=224.0,Y=1.0 (should be at baseline 0?)
	* parenright (U+0029): X=296.0,Y=1.0 (should be at baseline 0?)
	* at (U+0040): X=349.5,Y=705.5 (should be at cap-height 704?)
	* a (U+0061): X=135.0,Y=0.5 (should be at baseline 0?)
	* a (U+0061): X=340.0,Y=510.0 (should be at x-height 512?)
	* b (U+0062): X=212.5,Y=511.5 (should be at x-height 512?)
	* b (U+0062): X=212.5,Y=1.0 (should be at baseline 0?)
	* d (U+0064): X=299.5,Y=1.0 (should be at baseline 0?)
	* d (U+0064): X=299.5,Y=511.5 (should be at x-height 512?)
	* i (U+0069): X=218.5,Y=702.0 (should be at cap-height 704?)
	* i (U+0069): X=309.5,Y=702.0 (should be at cap-height 704?)
	* j (U+006A): X=242.5,Y=702.0 (should be at cap-height 704?)
	* j (U+006A): X=333.5,Y=702.0 (should be at cap-height 704?)
	* m (U+006D): X=166.0,Y=510.5 (should be at x-height 512?)
	* m (U+006D): X=257.0,Y=510.5 (should be at x-height 512?)
	* m (U+006D): X=321.0,Y=510.5 (should be at x-height 512?)
	* n (U+006E): X=215.0,Y=510.5 (should be at x-height 512?)
	* p (U+0070): X=195.0,Y=510.0 (should be at x-height 512?)
	* q (U+0071): X=317.5,Y=510.0 (should be at x-height 512?)
	* r (U+0072): X=221.0,Y=510.0 (should be at x-height 512?)
	* s (U+0073): X=352.0,Y=-2.0 (should be at baseline 0?)
	* sterling (U+00A3): X=371.0,Y=769.5 (should be at ascender 768?)
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
	* oe (U+0153): X=455.5,Y=1.5 (should be at baseline 0?)
	* oe (U+0153): X=221.0,Y=-2.0 (should be at baseline 0?)
	* ring (U+02DA): X=199.5,Y=705.0 (should be at cap-height 704?)
	* ring (U+02DA): X=312.5,Y=705.0 (should be at cap-height 704?)
	* uni030A (U+030A): X=199.5,Y=705.0 (should be at cap-height 704?)
	* uni030A (U+030A): X=312.5,Y=705.0 (should be at cap-height 704?) and Euro (U+20AC): X=371.0,Y=769.5 (should be at ascender 768?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:
	* W (U+0057): L<<472.0,696.0>--<472.0,688.0>> -> L<<472.0,688.0>--<429.0,8.0>> and W (U+0057): L<<83.0,8.0>--<40.0,688.0>> -> L<<40.0,688.0>--<40.0,696.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:
 * newGlyph (U+00B5): L<<59.0,-208.0>--<58.0,513.0>> [code: found-semi-vertical]
</div></details><br></div></details>
### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 38 | 61 | 653 | 37 | 481 | 0 |
| 0% | 3% | 5% | 51% | 3% | 38% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
