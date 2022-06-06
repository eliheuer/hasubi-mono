## Fontbakery report

Fontbakery version: 0.8.8

<details><summary><b>[15] HasubiMono-Medium.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check `Google Fonts Latin Core` glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x00B2 (SUPERSCRIPT TWO)

	- 0x00B3 (SUPERSCRIPT THREE)

	- 0x00B4 (ACUTE ACCENT)

	- 0x00B7 (MIDDLE DOT)

	- 0x00B8 (CEDILLA)

	- 0x00B9 (SUPERSCRIPT ONE)

	- 0x00BA (MASCULINE ORDINAL INDICATOR)

	- 0x00BB (RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK)

	- 0x00BC (VULGAR FRACTION ONE QUARTER)

	- 0x00BD (VULGAR FRACTION ONE HALF)
 
	- And 87 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
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
* ⚠ **WARN** Font is monospaced but 193 glyphs (68.93%) have a different width. You should check the widths of: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ordfeminine', 'uni0621', 'uni0627', 'uniFE8E', 'uni0623', 'uniFE84', 'uni0625', 'uniFE88', 'uni066E', 'uni066E.fina', 'uni066E.medi', 'uni066E.init', 'uni0628', 'uniFE90', 'uniFE92', 'uniFE91', 'uni062A', 'uniFE96', 'uniFE98', 'uniFE97', 'uni062B', 'uniFE9A', 'uniFE9C', 'uniFE9B', 'uniFEA0', 'uniFE9F', 'uni062D', 'uniFEA2', 'uniFEA4', 'uniFEA3', 'uni062E', 'uniFEA6', 'uniFEA8', 'uniFEA7', 'uni062F', 'uniFEAA', 'uni0630', 'uniFEAC', 'uni0631', 'uni0633', 'uniFEB2', 'uniFEB4', 'uniFEB3', 'uni0634', 'uniFEB6', 'uniFEB8', 'uniFEB7', 'uniFECC', 'uniFED3', 'uni06A1.init', 'uniFEDC', 'uniFEDB', 'uni0646', 'uniFEE6', 'uniFEE8', 'uniFEE7', 'uni06BA', 'uniFB9F', 'uni0648', 'uniFEEE', 'uniFEF4', 'uniFEF3', 'uni0640', 'uniFEFB', 'uniFEFC', 'uni0660', 'uni0661', 'uni0662', 'uni0663', 'uni0664', 'uni0665', 'uni0666', 'uni0667', 'uni0668', 'uni0669', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'space', 'uni00A0', 'uni060C', 'uni061B', 'uni061F', 'uni066D', 'uniFD3E', 'uniFD3F', 'period', 'comma', 'colon', 'semicolon', 'exclam', 'exclamdown', 'question', 'asterisk', 'numbersign', 'slash', 'backslash', 'hyphen', 'underscore', 'parenleft', 'parenright', 'braceleft', 'braceright', 'bracketleft', 'bracketright', 'guillemotleft', 'quotedbl', 'quotesingle', 'at', 'ampersand', 'paragraph', 'section', 'copyright', 'registered', 'degree', 'bar', 'brokenbar', 'cent', 'dollar', 'sterling', 'yen', 'plus', 'minus', 'equal', 'greater', 'less', 'plusminus', 'asciitilde', 'asciicircum', 'newGlyph', 'percent', 'dieresis', 'grave', 'macron'] [code: mono-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uniFE9F
	- threedotsdowncenterar
	- doublestrokear
	- threedotsupbelowar
	- dotcenterar
	- uniFEF9
	- uniFEF5
	- uniFEA0
	- uniFEF3
	- threedotsdownabovear 
	- And 10 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
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
	* j (U+006A): X=242.5,Y=702.0 (should be at cap-height 704?) and 12 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
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
</div></details><br></div></details><details><summary><b>[15] HasubiMono-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check `Google Fonts Latin Core` glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x00B2 (SUPERSCRIPT TWO)

	- 0x00B3 (SUPERSCRIPT THREE)

	- 0x00B4 (ACUTE ACCENT)

	- 0x00B7 (MIDDLE DOT)

	- 0x00B8 (CEDILLA)

	- 0x00B9 (SUPERSCRIPT ONE)

	- 0x00BA (MASCULINE ORDINAL INDICATOR)

	- 0x00BB (RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK)

	- 0x00BC (VULGAR FRACTION ONE QUARTER)

	- 0x00BD (VULGAR FRACTION ONE HALF)
 
	- And 87 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
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
* ⚠ **WARN** Font is monospaced but 42 glyphs (15.00%) have a different width. You should check the widths of: ['uni0635', 'uniFEBA', 'uniFEBC', 'uniFEBB', 'uni0639', 'uniFECA', 'uniFECB', 'uni0641', 'uniFED2', 'uni06A4', 'uni06A1', 'uni06A1.fina', 'uni06A1.medi', 'uni066F', 'uni066F.fina', 'uni0643', 'uniFEDA', 'uni0647', 'uniFEEA', 'uniFEEC', 'uniFEEB', 'uni0624', 'uniFE86', 'uni0649', 'uniFEF0', 'uni064A', 'uni0626', 'uniFE8A', 'uniFE8C', 'uniFE8B', 'uniFEF7', 'uniFEF8', 'uniFEF9', 'uniFEFA', 'uniFEF5', 'uniFEF6', 'lam_alefWaslaar', 'lam_alefWaslaar.fina', 'uni066B', 'uni066C', 'uni066A', 'logicalnot'] [code: mono-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uniFE9F
	- threedotsdowncenterar
	- doublestrokear
	- threedotsupbelowar
	- dotcenterar
	- uniFEF9
	- uniFEF5
	- uniFEA0
	- uniFEF3
	- threedotsdownabovear 
	- And 10 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
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
	* d (U+0064): X=299.5,Y=511.5 (should be at x-height 512?) and 16 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:
	* W (U+0057): L<<472.0,696.0>--<472.0,688.0>> -> L<<472.0,688.0>--<429.0,8.0>> and W (U+0057): L<<83.0,8.0>--<40.0,688.0>> -> L<<40.0,688.0>--<40.0,696.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:
 * newGlyph (U+00B5): L<<59.0,-208.0>--<58.0,513.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[17] HasubiMono-Heavy.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking file is named canonically. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/canonical_filename">com.google.fonts/check/canonical_filename</a>)</summary><div>


* 🔥 **FAIL** Style name used in "fonts/ttf/HasubiMono-Heavy.ttf" is not canonical. You should rebuild the font using any of the following style names: "Thin", "ExtraLight", "Light", "Regular", "Medium", "SemiBold", "Bold", "ExtraBold", "Black", "Thin Italic", "ExtraLight Italic", "Light Italic", "Italic", "Medium Italic", "SemiBold Italic", "Bold Italic", "ExtraBold Italic", "Black Italic". [code: bad-static-filename]
</div></details><details><summary>🔥 <b>FAIL:</b> Check `Google Fonts Latin Core` glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x00B2 (SUPERSCRIPT TWO)

	- 0x00B3 (SUPERSCRIPT THREE)

	- 0x00B4 (ACUTE ACCENT)

	- 0x00B7 (MIDDLE DOT)

	- 0x00B8 (CEDILLA)

	- 0x00B9 (SUPERSCRIPT ONE)

	- 0x00BA (MASCULINE ORDINAL INDICATOR)

	- 0x00BB (RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK)

	- 0x00BC (VULGAR FRACTION ONE QUARTER)

	- 0x00BD (VULGAR FRACTION ONE HALF)
 
	- And 87 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
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
* ⚠ **WARN** Font is monospaced but 154 glyphs (55.00%) have a different width. You should check the widths of: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ordfeminine', 'uni0621', 'uni0627', 'uniFE8E', 'uni0623', 'uniFE84', 'uni0625', 'uniFE88', 'uni066E.medi', 'uniFE92', 'uniFE98', 'uniFE9C', 'uniFED3', 'uni06A1.init', 'uniFEDC', 'uniFEDB', 'uni0646', 'uniFEE6', 'uniFEE8', 'uni06BA', 'uniFB9F', 'uni0648', 'uniFEEE', 'uniFEF4', 'uni0640', 'uniFEFB', 'uniFEFC', 'uni0660', 'uni0661', 'uni0662', 'uni0663', 'uni0664', 'uni0665', 'uni0666', 'uni0667', 'uni0668', 'uni0669', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'space', 'uni00A0', 'uni060C', 'uni061B', 'uni061F', 'uni066D', 'uniFD3E', 'uniFD3F', 'period', 'comma', 'colon', 'semicolon', 'exclam', 'exclamdown', 'question', 'asterisk', 'numbersign', 'slash', 'backslash', 'hyphen', 'underscore', 'parenleft', 'parenright', 'braceleft', 'braceright', 'bracketleft', 'bracketright', 'quotedbl', 'quotesingle', 'at', 'ampersand', 'paragraph', 'section', 'copyright', 'registered', 'degree', 'bar', 'brokenbar', 'cent', 'dollar', 'sterling', 'yen', 'plus', 'minus', 'equal', 'greater', 'less', 'plusminus', 'asciitilde', 'asciicircum', 'newGlyph', 'percent', 'dieresis', 'grave', 'macron'] [code: mono-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uniFE9F
	- threedotsdowncenterar
	- doublestrokear
	- threedotsupbelowar
	- dotcenterar
	- uniFEF9
	- uniFEF5
	- uniFEA0
	- uniFEF3
	- threedotsdownabovear 
	- And 10 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
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
	* j (U+006A): X=242.5,Y=702.0 (should be at cap-height 704?) and 11 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:
	* W (U+0057): L<<75.0,8.0>--<17.0,688.0>> -> L<<17.0,688.0>--<17.0,696.0>>
	* W (U+0057): L<<93.0,696.0>--<93.0,688.0>> -> L<<93.0,688.0>--<130.0,102.0>> and w (U+0077): L<<93.0,504.0>--<93.0,496.0>> -> L<<93.0,496.0>--<130.0,102.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:
 * newGlyph (U+00B5): L<<59.0,-208.0>--<58.0,513.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[20] HasubiMono-Bold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check `Google Fonts Latin Core` glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x00B2 (SUPERSCRIPT TWO)

	- 0x00B3 (SUPERSCRIPT THREE)

	- 0x00B4 (ACUTE ACCENT)

	- 0x00B7 (MIDDLE DOT)

	- 0x00B8 (CEDILLA)

	- 0x00B9 (SUPERSCRIPT ONE)

	- 0x00BA (MASCULINE ORDINAL INDICATOR)

	- 0x00BB (RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK)

	- 0x00BC (VULGAR FRACTION ONE QUARTER)

	- 0x00BD (VULGAR FRACTION ONE HALF)
 
	- And 87 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


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
* ⚠ **WARN** Font is monospaced but 193 glyphs (68.93%) have a different width. You should check the widths of: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ordfeminine', 'uni0621', 'uni0627', 'uniFE8E', 'uni0623', 'uniFE84', 'uni0625', 'uniFE88', 'uni066E', 'uni066E.fina', 'uni066E.medi', 'uni066E.init', 'uni0628', 'uniFE90', 'uniFE92', 'uniFE91', 'uni062A', 'uniFE96', 'uniFE98', 'uniFE97', 'uni062B', 'uniFE9A', 'uniFE9C', 'uniFE9B', 'uniFEA0', 'uniFE9F', 'uni062D', 'uniFEA2', 'uniFEA4', 'uniFEA3', 'uni062E', 'uniFEA6', 'uniFEA8', 'uniFEA7', 'uni062F', 'uniFEAA', 'uni0630', 'uniFEAC', 'uni0631', 'uni0633', 'uniFEB2', 'uniFEB4', 'uniFEB3', 'uni0634', 'uniFEB6', 'uniFEB8', 'uniFEB7', 'uniFECC', 'uniFED3', 'uni06A1.init', 'uniFEDC', 'uniFEDB', 'uni0646', 'uniFEE6', 'uniFEE8', 'uniFEE7', 'uni06BA', 'uniFB9F', 'uni0648', 'uniFEEE', 'uniFEF4', 'uniFEF3', 'uni0640', 'uniFEFB', 'uniFEFC', 'uni0660', 'uni0661', 'uni0662', 'uni0663', 'uni0664', 'uni0665', 'uni0666', 'uni0667', 'uni0668', 'uni0669', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'space', 'uni00A0', 'uni060C', 'uni061B', 'uni061F', 'uni066D', 'uniFD3E', 'uniFD3F', 'period', 'comma', 'colon', 'semicolon', 'exclam', 'exclamdown', 'question', 'asterisk', 'numbersign', 'slash', 'backslash', 'hyphen', 'underscore', 'parenleft', 'parenright', 'braceleft', 'braceright', 'bracketleft', 'bracketright', 'guillemotleft', 'quotedbl', 'quotesingle', 'at', 'ampersand', 'paragraph', 'section', 'copyright', 'registered', 'degree', 'bar', 'brokenbar', 'cent', 'dollar', 'sterling', 'yen', 'plus', 'minus', 'equal', 'greater', 'less', 'plusminus', 'asciitilde', 'asciicircum', 'newGlyph', 'percent', 'dieresis', 'grave', 'macron'] [code: mono-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uniFE9F
	- threedotsdowncenterar
	- doublestrokear
	- threedotsupbelowar
	- dotcenterar
	- uniFEF9
	- uniFEF5
	- uniFEA0
	- uniFEF3
	- threedotsdownabovear 
	- And 10 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
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
	* d (U+0064): X=299.5,Y=513.0 (should be at x-height 512?) and 15 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
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
</div></details><br></div></details><details><summary><b>[15] HasubiMono-SemiBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check `Google Fonts Latin Core` glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x00B2 (SUPERSCRIPT TWO)

	- 0x00B3 (SUPERSCRIPT THREE)

	- 0x00B4 (ACUTE ACCENT)

	- 0x00B7 (MIDDLE DOT)

	- 0x00B8 (CEDILLA)

	- 0x00B9 (SUPERSCRIPT ONE)

	- 0x00BA (MASCULINE ORDINAL INDICATOR)

	- 0x00BB (RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK)

	- 0x00BC (VULGAR FRACTION ONE QUARTER)

	- 0x00BD (VULGAR FRACTION ONE HALF)
 
	- And 87 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
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
* ⚠ **WARN** Font is monospaced but 193 glyphs (68.93%) have a different width. You should check the widths of: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ordfeminine', 'uni0621', 'uni0627', 'uniFE8E', 'uni0623', 'uniFE84', 'uni0625', 'uniFE88', 'uni066E', 'uni066E.fina', 'uni066E.medi', 'uni066E.init', 'uni0628', 'uniFE90', 'uniFE92', 'uniFE91', 'uni062A', 'uniFE96', 'uniFE98', 'uniFE97', 'uni062B', 'uniFE9A', 'uniFE9C', 'uniFE9B', 'uniFEA0', 'uniFE9F', 'uni062D', 'uniFEA2', 'uniFEA4', 'uniFEA3', 'uni062E', 'uniFEA6', 'uniFEA8', 'uniFEA7', 'uni062F', 'uniFEAA', 'uni0630', 'uniFEAC', 'uni0631', 'uni0633', 'uniFEB2', 'uniFEB4', 'uniFEB3', 'uni0634', 'uniFEB6', 'uniFEB8', 'uniFEB7', 'uniFECC', 'uniFED3', 'uni06A1.init', 'uniFEDC', 'uniFEDB', 'uni0646', 'uniFEE6', 'uniFEE8', 'uniFEE7', 'uni06BA', 'uniFB9F', 'uni0648', 'uniFEEE', 'uniFEF4', 'uniFEF3', 'uni0640', 'uniFEFB', 'uniFEFC', 'uni0660', 'uni0661', 'uni0662', 'uni0663', 'uni0664', 'uni0665', 'uni0666', 'uni0667', 'uni0668', 'uni0669', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'space', 'uni00A0', 'uni060C', 'uni061B', 'uni061F', 'uni066D', 'uniFD3E', 'uniFD3F', 'period', 'comma', 'colon', 'semicolon', 'exclam', 'exclamdown', 'question', 'asterisk', 'numbersign', 'slash', 'backslash', 'hyphen', 'underscore', 'parenleft', 'parenright', 'braceleft', 'braceright', 'bracketleft', 'bracketright', 'guillemotleft', 'quotedbl', 'quotesingle', 'at', 'ampersand', 'paragraph', 'section', 'copyright', 'registered', 'degree', 'bar', 'brokenbar', 'cent', 'dollar', 'sterling', 'yen', 'plus', 'minus', 'equal', 'greater', 'less', 'plusminus', 'asciitilde', 'asciicircum', 'newGlyph', 'percent', 'dieresis', 'grave', 'macron'] [code: mono-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uniFE9F
	- threedotsdowncenterar
	- doublestrokear
	- threedotsupbelowar
	- dotcenterar
	- uniFEF9
	- uniFEF5
	- uniFEA0
	- uniFEF3
	- threedotsdownabovear 
	- And 10 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
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
	* j (U+006A): X=242.5,Y=702.0 (should be at cap-height 704?) and 11 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
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
</div></details><br></div></details><details><summary><b>[16] HasubiMono-ExtraBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check `Google Fonts Latin Core` glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x00B2 (SUPERSCRIPT TWO)

	- 0x00B3 (SUPERSCRIPT THREE)

	- 0x00B4 (ACUTE ACCENT)

	- 0x00B7 (MIDDLE DOT)

	- 0x00B8 (CEDILLA)

	- 0x00B9 (SUPERSCRIPT ONE)

	- 0x00BA (MASCULINE ORDINAL INDICATOR)

	- 0x00BB (RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK)

	- 0x00BC (VULGAR FRACTION ONE QUARTER)

	- 0x00BD (VULGAR FRACTION ONE HALF)
 
	- And 87 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
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
* ⚠ **WARN** Font is monospaced but 193 glyphs (68.93%) have a different width. You should check the widths of: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ordfeminine', 'uni0621', 'uni0627', 'uniFE8E', 'uni0623', 'uniFE84', 'uni0625', 'uniFE88', 'uni066E', 'uni066E.fina', 'uni066E.medi', 'uni066E.init', 'uni0628', 'uniFE90', 'uniFE92', 'uniFE91', 'uni062A', 'uniFE96', 'uniFE98', 'uniFE97', 'uni062B', 'uniFE9A', 'uniFE9C', 'uniFE9B', 'uniFEA0', 'uniFE9F', 'uni062D', 'uniFEA2', 'uniFEA4', 'uniFEA3', 'uni062E', 'uniFEA6', 'uniFEA8', 'uniFEA7', 'uni062F', 'uniFEAA', 'uni0630', 'uniFEAC', 'uni0631', 'uni0633', 'uniFEB2', 'uniFEB4', 'uniFEB3', 'uni0634', 'uniFEB6', 'uniFEB8', 'uniFEB7', 'uniFECC', 'uniFED3', 'uni06A1.init', 'uniFEDC', 'uniFEDB', 'uni0646', 'uniFEE6', 'uniFEE8', 'uniFEE7', 'uni06BA', 'uniFB9F', 'uni0648', 'uniFEEE', 'uniFEF4', 'uniFEF3', 'uni0640', 'uniFEFB', 'uniFEFC', 'uni0660', 'uni0661', 'uni0662', 'uni0663', 'uni0664', 'uni0665', 'uni0666', 'uni0667', 'uni0668', 'uni0669', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'space', 'uni00A0', 'uni060C', 'uni061B', 'uni061F', 'uni066D', 'uniFD3E', 'uniFD3F', 'period', 'comma', 'colon', 'semicolon', 'exclam', 'exclamdown', 'question', 'asterisk', 'numbersign', 'slash', 'backslash', 'hyphen', 'underscore', 'parenleft', 'parenright', 'braceleft', 'braceright', 'bracketleft', 'bracketright', 'guillemotleft', 'quotedbl', 'quotesingle', 'at', 'ampersand', 'paragraph', 'section', 'copyright', 'registered', 'degree', 'bar', 'brokenbar', 'cent', 'dollar', 'sterling', 'yen', 'plus', 'minus', 'equal', 'greater', 'less', 'plusminus', 'asciitilde', 'asciicircum', 'newGlyph', 'percent', 'dieresis', 'grave', 'macron'] [code: mono-outliers]
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
	- threedotsdowncenterar
	- doublestrokear
	- threedotsupbelowar
	- dotcenterar
	- uniFEF9
	- uniFEF5
	- uniFEA0
	- uniFEF3
	- threedotsdownabovear 
	- And 10 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
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
	* b (U+0062): X=212.0,Y=514.0 (should be at x-height 512?) and 18 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
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
</div></details><br></div></details>
### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 43 | 55 | 653 | 37 | 482 | 0 |
| 0% | 3% | 4% | 51% | 3% | 38% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
