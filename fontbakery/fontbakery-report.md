## Fontbakery report

Fontbakery version: 0.8.8

<details><summary><b>[1] Family checks</b></summary><div><details><summary>🔥 <b>FAIL:</b> Each font in a family must have the same set of vertical metrics values. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/vertical_metrics">com.google.fonts/check/family/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** sTypoAscender is not the same across the family:
Hasubi Mono Bold: 773
Hasubi Mono Medium: 727
Hasubi Mono Heavy: 832
Hasubi Mono Regular: 704
Hasubi Mono ExtraBold: 795
Hasubi Mono SemiBold: 750 [code: sTypoAscender-mismatch]
* 🔥 **FAIL** sTypoLineGap is not the same across the family:
Hasubi Mono Bold: 219
Hasubi Mono Medium: 265
Hasubi Mono Heavy: 160
Hasubi Mono Regular: 288
Hasubi Mono ExtraBold: 197
Hasubi Mono SemiBold: 242 [code: sTypoLineGap-mismatch]
</div></details><br></div></details><details><summary><b>[21] HasubiMono-Bold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check `Google Fonts Latin Core` glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0021 (EXCLAMATION MARK)

	- 0x0022 (QUOTATION MARK)

	- 0x0023 (NUMBER SIGN)

	- 0x0024 (DOLLAR SIGN)

	- 0x0025 (PERCENT SIGN)

	- 0x0026 (AMPERSAND)

	- 0x0027 (APOSTROPHE)

	- 0x0028 (LEFT PARENTHESIS)

	- 0x0029 (RIGHT PARENTHESIS)

	- 0x002A (ASTERISK)
 
	- And 135 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** Font lacks NameID 13 (LICENSE DESCRIPTION). A proper licensing entry must be set. [code: missing]
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


* 🔥 **FAIL** OS/2 sTypoAscender (773) and hhea ascent (992) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> Font contains glyphs for whitespace characters? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphs">com.google.fonts/check/whitespace_glyphs</a>)</summary><div>


* 🔥 **FAIL** Whitespace glyph missing for codepoint 0x00A0. [code: missing-whitespace-glyph-0x00A0]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uniFEBB
	- uniFE8C
	- gafsarkashabovear
	- doublestrokear
	- uni066F.fina
	- uni0654064C
	- uni0651064C
	- uniFE88
	- lam_alefWaslaar.fina
	- miniKehehar 
	- And 77 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: comma	Contours detected: 0	Expected: 1
	- Glyph name: hyphen	Contours detected: 0	Expected: 1
	- Glyph name: period	Contours detected: 0	Expected: 1
	- Glyph name: zero	Contours detected: 0	Expected: 2 or 3
	- Glyph name: one	Contours detected: 0	Expected: 1
	- Glyph name: two	Contours detected: 0	Expected: 1
	- Glyph name: three	Contours detected: 0	Expected: 1
	- Glyph name: four	Contours detected: 0	Expected: 1 or 2
	- Glyph name: five	Contours detected: 0	Expected: 1
	- Glyph name: six	Contours detected: 0	Expected: 1 or 2 
	- And 64 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/hhea.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* ⚠ **WARN** OS/2 sTypoLineGap is not equal to 0. [code: OS/2]
</div></details><details><summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info">com.google.fonts/check/gpos_kerning_info</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* uni0628 (U+0628): X=306.0,Y=-206.0 (should be at descender -208?) and uni0628 (U+0628): X=306.0,Y=-206.0 (should be at descender -208?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:
	* H (U+0048) contains a short segment L<<88.0,0.0>--<80.0,8.0>>
	* H (U+0048) contains a short segment L<<80.0,696.0>--<88.0,704.0>>
	* H (U+0048) contains a short segment L<<144.0,704.0>--<152.0,696.0>>
	* H (U+0048) contains a short segment L<<152.0,407.0>--<160.0,399.0>>
	* H (U+0048) contains a short segment L<<352.0,399.0>--<360.0,407.0>>
	* H (U+0048) contains a short segment L<<360.0,696.0>--<368.0,704.0>>
	* H (U+0048) contains a short segment L<<424.0,704.0>--<432.0,696.0>>
	* H (U+0048) contains a short segment L<<432.0,8.0>--<424.0,0.0>>
	* H (U+0048) contains a short segment L<<368.0,0.0>--<360.0,8.0>>
	* H (U+0048) contains a short segment L<<360.0,311.0>--<352.0,319.0>> and 52 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:
	* G (U+0047): L<<401.0,0.0>--<390.0,136.0>>/B<<390.0,136.0>-<387.0,96.0>-<367.0,63.0>> = 8.91330465724806
	* M (U+004D): L<<217.0,223.0>--<118.0,627.0>>/L<<118.0,627.0>--<120.0,0.0>> = 13.586215426835068 and M (U+004D): L<<393.0,0.0>--<396.0,623.0>>/L<<396.0,623.0>--<294.0,223.0>> = 14.029651349071994 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:
 * C (U+0043): L<<476.0,491.0>--<346.0,492.0>>
 * E (U+0045): L<<120.0,458.0>--<440.0,457.0>>
 * E (U+0045): L<<440.0,361.0>--<120.0,362.0>>
 * F (U+0046): L<<146.0,470.0>--<440.0,469.0>>
 * G (U+0047): L<<464.0,516.0>--<333.0,517.0>>
 * G (U+0047): L<<474.0,390.0>--<476.0,0.0>>
 * M (U+004D): L<<118.0,627.0>--<120.0,0.0>>
 * M (U+004D): L<<393.0,0.0>--<396.0,623.0>> and M (U+004D): L<<472.0,768.0>--<471.0,0.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[16] HasubiMono-Medium.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check `Google Fonts Latin Core` glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0021 (EXCLAMATION MARK)

	- 0x0022 (QUOTATION MARK)

	- 0x0023 (NUMBER SIGN)

	- 0x0024 (DOLLAR SIGN)

	- 0x0025 (PERCENT SIGN)

	- 0x0026 (AMPERSAND)

	- 0x0027 (APOSTROPHE)

	- 0x0028 (LEFT PARENTHESIS)

	- 0x0029 (RIGHT PARENTHESIS)

	- 0x002A (ASTERISK)
 
	- And 135 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** Font lacks NameID 13 (LICENSE DESCRIPTION). A proper licensing entry must be set. [code: missing]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 272, but got 208 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>


* 🔥 **FAIL** OS/2 sTypoAscender (727) and hhea ascent (992) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> Font contains glyphs for whitespace characters? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphs">com.google.fonts/check/whitespace_glyphs</a>)</summary><div>


* 🔥 **FAIL** Whitespace glyph missing for codepoint 0x00A0. [code: missing-whitespace-glyph-0x00A0]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uniFEBB
	- uniFE8C
	- gafsarkashabovear
	- doublestrokear
	- uni066F.fina
	- uni0654064C
	- uni0651064C
	- uniFE88
	- lam_alefWaslaar.fina
	- miniKehehar 
	- And 77 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: comma	Contours detected: 0	Expected: 1
	- Glyph name: hyphen	Contours detected: 0	Expected: 1
	- Glyph name: period	Contours detected: 0	Expected: 1
	- Glyph name: zero	Contours detected: 0	Expected: 2 or 3
	- Glyph name: one	Contours detected: 0	Expected: 1
	- Glyph name: two	Contours detected: 0	Expected: 1
	- Glyph name: three	Contours detected: 0	Expected: 1
	- Glyph name: four	Contours detected: 0	Expected: 1 or 2
	- Glyph name: five	Contours detected: 0	Expected: 1
	- Glyph name: six	Contours detected: 0	Expected: 1 or 2 
	- And 64 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/hhea.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* ⚠ **WARN** OS/2 sTypoLineGap is not equal to 0. [code: OS/2]
</div></details><details><summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info">com.google.fonts/check/gpos_kerning_info</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* C (U+0043): X=420.0,Y=725.5 (should be at ascender 727?)
	* c (U+0063): X=87.0,Y=526.0 (should be at x-height 528?)
	* c (U+0063): X=425.5,Y=529.0 (should be at x-height 528?)
	* uni0654 (U+0654): X=14.0,Y=717.0 (should be at cap-height 715?) and uni0654 (U+0654): X=143.0,Y=714.0 (should be at cap-height 715?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:
	* H (U+0048) contains a short segment L<<88.0,0.0>--<80.0,8.0>>
	* H (U+0048) contains a short segment L<<80.0,696.0>--<88.0,704.0>>
	* H (U+0048) contains a short segment L<<144.0,704.0>--<152.0,696.0>>
	* H (U+0048) contains a short segment L<<152.0,407.0>--<160.0,399.0>>
	* H (U+0048) contains a short segment L<<352.0,399.0>--<360.0,407.0>>
	* H (U+0048) contains a short segment L<<360.0,696.0>--<368.0,704.0>>
	* H (U+0048) contains a short segment L<<424.0,704.0>--<432.0,696.0>>
	* H (U+0048) contains a short segment L<<432.0,8.0>--<424.0,0.0>>
	* H (U+0048) contains a short segment L<<368.0,0.0>--<360.0,8.0>>
	* H (U+0048) contains a short segment L<<360.0,311.0>--<352.0,319.0>> and 52 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:
	* G (U+0047): L<<401.0,0.0>--<390.0,136.0>>/B<<390.0,136.0>-<387.0,96.0>-<367.0,63.0>> = 8.91330465724806
	* M (U+004D): L<<217.0,223.0>--<118.0,627.0>>/L<<118.0,627.0>--<120.0,0.0>> = 13.586215426835068 and M (U+004D): L<<393.0,0.0>--<396.0,623.0>>/L<<396.0,623.0>--<294.0,223.0>> = 14.029651349071994 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:
 * C (U+0043): L<<476.0,491.0>--<346.0,492.0>>
 * E (U+0045): L<<120.0,458.0>--<440.0,457.0>>
 * E (U+0045): L<<440.0,361.0>--<120.0,362.0>>
 * F (U+0046): L<<129.0,462.0>--<440.0,461.0>>
 * F (U+0046): L<<440.0,348.0>--<129.0,349.0>>
 * G (U+0047): L<<464.0,516.0>--<333.0,517.0>>
 * G (U+0047): L<<474.0,390.0>--<476.0,0.0>>
 * M (U+004D): L<<118.0,627.0>--<120.0,0.0>>
 * M (U+004D): L<<393.0,0.0>--<396.0,623.0>> and M (U+004D): L<<472.0,768.0>--<471.0,0.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[18] HasubiMono-Heavy.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking file is named canonically. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/canonical_filename">com.google.fonts/check/canonical_filename</a>)</summary><div>


* 🔥 **FAIL** Style name used in "fonts/ttf/HasubiMono-Heavy.ttf" is not canonical. You should rebuild the font using any of the following style names: "Thin", "ExtraLight", "Light", "Regular", "Medium", "SemiBold", "Bold", "ExtraBold", "Black", "Thin Italic", "ExtraLight Italic", "Light Italic", "Italic", "Medium Italic", "SemiBold Italic", "Bold Italic", "ExtraBold Italic", "Black Italic". [code: bad-static-filename]
</div></details><details><summary>🔥 <b>FAIL:</b> Check `Google Fonts Latin Core` glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0021 (EXCLAMATION MARK)

	- 0x0022 (QUOTATION MARK)

	- 0x0023 (NUMBER SIGN)

	- 0x0024 (DOLLAR SIGN)

	- 0x0025 (PERCENT SIGN)

	- 0x0026 (AMPERSAND)

	- 0x0027 (APOSTROPHE)

	- 0x0028 (LEFT PARENTHESIS)

	- 0x0029 (RIGHT PARENTHESIS)

	- 0x002A (ASTERISK)
 
	- And 135 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWeightClass. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/usweightclass">com.google.fonts/check/usweightclass</a>)</summary><div>


* 🔥 **FAIL** OS/2 usWeightClass is '900' when it should be '400'. [code: bad-value]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** Font lacks NameID 13 (LICENSE DESCRIPTION). A proper licensing entry must be set. [code: missing]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 272, but got 208 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>


* 🔥 **FAIL** OS/2 sTypoAscender (832) and hhea ascent (992) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> Font contains glyphs for whitespace characters? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphs">com.google.fonts/check/whitespace_glyphs</a>)</summary><div>


* 🔥 **FAIL** Whitespace glyph missing for codepoint 0x00A0. [code: missing-whitespace-glyph-0x00A0]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** On monospaced fonts, the value of post.isFixedPitch must be set to a non-zero value (meaning 'fixed width monospaced'), but got 0 instead. [code: mono-bad-post-isFixedPitch]
* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** Font is monospaced but 76 glyphs (33.04%) have a different width. You should check the widths of: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'uni0621', 'uni0627', 'uniFE8E', 'uni0623', 'uniFE84', 'uni0625', 'uniFE88', 'uni066E.medi', 'uniFE92', 'uniFE98', 'uniFE9C', 'uniFEDC', 'uniFEDB', 'uni0646', 'uniFEE6', 'uniFEE8', 'uni06BA', 'uniFB9F', 'uni0648', 'uniFEEE', 'uniFEF4', 'uni0640', 'uniFEFB', 'uniFEFC'] [code: mono-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uniFEBB
	- uniFE8C
	- gafsarkashabovear
	- doublestrokear
	- uni066F.fina
	- uni0654064C
	- uni0651064C
	- uniFE88
	- lam_alefWaslaar.fina
	- miniKehehar 
	- And 77 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: comma	Contours detected: 0	Expected: 1
	- Glyph name: hyphen	Contours detected: 0	Expected: 1
	- Glyph name: period	Contours detected: 0	Expected: 1
	- Glyph name: zero	Contours detected: 0	Expected: 2 or 3
	- Glyph name: one	Contours detected: 0	Expected: 1
	- Glyph name: two	Contours detected: 0	Expected: 1
	- Glyph name: three	Contours detected: 0	Expected: 1
	- Glyph name: four	Contours detected: 0	Expected: 1 or 2
	- Glyph name: five	Contours detected: 0	Expected: 1
	- Glyph name: six	Contours detected: 0	Expected: 1 or 2 
	- And 64 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/hhea.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* ⚠ **WARN** OS/2 sTypoLineGap is not equal to 0. [code: OS/2]
</div></details><details><summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info">com.google.fonts/check/gpos_kerning_info</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:
	* H (U+0048) contains a short segment L<<88.0,0.0>--<80.0,8.0>>
	* H (U+0048) contains a short segment L<<80.0,696.0>--<88.0,704.0>>
	* H (U+0048) contains a short segment L<<144.0,704.0>--<152.0,696.0>>
	* H (U+0048) contains a short segment L<<152.0,407.0>--<160.0,399.0>>
	* H (U+0048) contains a short segment L<<352.0,399.0>--<360.0,407.0>>
	* H (U+0048) contains a short segment L<<360.0,696.0>--<368.0,704.0>>
	* H (U+0048) contains a short segment L<<424.0,704.0>--<432.0,696.0>>
	* H (U+0048) contains a short segment L<<432.0,8.0>--<424.0,0.0>>
	* H (U+0048) contains a short segment L<<368.0,0.0>--<360.0,8.0>>
	* H (U+0048) contains a short segment L<<360.0,311.0>--<352.0,319.0>> and 52 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:
	* G (U+0047): L<<401.0,0.0>--<390.0,136.0>>/B<<390.0,136.0>-<387.0,96.0>-<367.0,63.0>> = 8.91330465724806
	* M (U+004D): L<<217.0,223.0>--<118.0,627.0>>/L<<118.0,627.0>--<120.0,0.0>> = 13.586215426835068 and M (U+004D): L<<393.0,0.0>--<396.0,623.0>>/L<<396.0,623.0>--<294.0,223.0>> = 14.029651349071994 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:
 * C (U+0043): L<<476.0,491.0>--<346.0,492.0>>
 * E (U+0045): L<<120.0,458.0>--<440.0,457.0>>
 * E (U+0045): L<<440.0,361.0>--<120.0,362.0>>
 * G (U+0047): L<<464.0,516.0>--<333.0,517.0>>
 * G (U+0047): L<<474.0,390.0>--<476.0,0.0>>
 * M (U+004D): L<<118.0,627.0>--<120.0,0.0>>
 * M (U+004D): L<<393.0,0.0>--<396.0,623.0>> and M (U+004D): L<<472.0,768.0>--<471.0,0.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[17] HasubiMono-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check `Google Fonts Latin Core` glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0021 (EXCLAMATION MARK)

	- 0x0022 (QUOTATION MARK)

	- 0x0023 (NUMBER SIGN)

	- 0x0024 (DOLLAR SIGN)

	- 0x0025 (PERCENT SIGN)

	- 0x0026 (AMPERSAND)

	- 0x0027 (APOSTROPHE)

	- 0x0028 (LEFT PARENTHESIS)

	- 0x0029 (RIGHT PARENTHESIS)

	- 0x002A (ASTERISK)
 
	- And 135 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** Font lacks NameID 13 (LICENSE DESCRIPTION). A proper licensing entry must be set. [code: missing]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 272, but got 208 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>


* 🔥 **FAIL** OS/2 sTypoAscender (704) and hhea ascent (992) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> Font contains glyphs for whitespace characters? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphs">com.google.fonts/check/whitespace_glyphs</a>)</summary><div>


* 🔥 **FAIL** Whitespace glyph missing for codepoint 0x00A0. [code: missing-whitespace-glyph-0x00A0]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>


* 🔥 **FAIL** On monospaced fonts, the value of post.isFixedPitch must be set to a non-zero value (meaning 'fixed width monospaced'), but got 0 instead. [code: mono-bad-post-isFixedPitch]
* 🔥 **FAIL** The PANOSE numbers are incorrect for a monospaced font. Note: Family Type is set to 0, which does not seem right. [code: mono-bad-panose]
* ⚠ **WARN** Font is monospaced but 117 glyphs (50.87%) have a different width. You should check the widths of: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'uni0621', 'uni0627', 'uniFE8E', 'uni0623', 'uniFE84', 'uni0625', 'uniFE88', 'uni066E', 'uni066E.fina', 'uni066E.medi', 'uni066E.init', 'uni0628', 'uniFE90', 'uniFE92', 'uniFE91', 'uni062A', 'uniFE96', 'uniFE98', 'uniFE97', 'uni062B', 'uniFE9A', 'uniFE9C', 'uniFE9B', 'uniFEA0', 'uniFE9F', 'uni062D', 'uniFEA2', 'uniFEA4', 'uniFEA3', 'uni062E', 'uniFEA6', 'uniFEA8', 'uniFEA7', 'uni062F', 'uniFEAA', 'uni0630', 'uniFEAC', 'uni0631', 'uni0633', 'uniFEB2', 'uniFEB4', 'uniFEB3', 'uni0634', 'uniFEB6', 'uniFEB8', 'uniFEB7', 'uniFECC', 'uniFED3', 'uni06A1.init', 'uniFEDC', 'uniFEDB', 'uni0646', 'uniFEE6', 'uniFEE8', 'uniFEE7', 'uni06BA', 'uniFB9F', 'uni0648', 'uniFEEE', 'uniFEF4', 'uniFEF3', 'uni0640', 'uniFEFB', 'uniFEFC', 'space'] [code: mono-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uniFEBB
	- uniFE8C
	- gafsarkashabovear
	- doublestrokear
	- uni066F.fina
	- uni0654064C
	- uni0651064C
	- uniFE88
	- lam_alefWaslaar.fina
	- miniKehehar 
	- And 77 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: comma	Contours detected: 0	Expected: 1
	- Glyph name: hyphen	Contours detected: 0	Expected: 1
	- Glyph name: period	Contours detected: 0	Expected: 1
	- Glyph name: zero	Contours detected: 0	Expected: 2 or 3
	- Glyph name: one	Contours detected: 0	Expected: 1
	- Glyph name: two	Contours detected: 0	Expected: 1
	- Glyph name: three	Contours detected: 0	Expected: 1
	- Glyph name: four	Contours detected: 0	Expected: 1 or 2
	- Glyph name: five	Contours detected: 0	Expected: 1
	- Glyph name: six	Contours detected: 0	Expected: 1 or 2 
	- And 64 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/hhea.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* ⚠ **WARN** OS/2 sTypoLineGap is not equal to 0. [code: OS/2]
</div></details><details><summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info">com.google.fonts/check/gpos_kerning_info</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* m (U+006D): X=305.0,Y=514.0 (should be at x-height 512?) and m (U+006D): X=202.0,Y=511.0 (should be at x-height 512?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:
	* H (U+0048) contains a short segment L<<88.0,0.0>--<80.0,8.0>>
	* H (U+0048) contains a short segment L<<80.0,696.0>--<88.0,704.0>>
	* H (U+0048) contains a short segment L<<144.0,704.0>--<152.0,696.0>>
	* H (U+0048) contains a short segment L<<152.0,407.0>--<160.0,399.0>>
	* H (U+0048) contains a short segment L<<352.0,399.0>--<360.0,407.0>>
	* H (U+0048) contains a short segment L<<360.0,696.0>--<368.0,704.0>>
	* H (U+0048) contains a short segment L<<424.0,704.0>--<432.0,696.0>>
	* H (U+0048) contains a short segment L<<432.0,8.0>--<424.0,0.0>>
	* H (U+0048) contains a short segment L<<368.0,0.0>--<360.0,8.0>>
	* H (U+0048) contains a short segment L<<360.0,311.0>--<352.0,319.0>> and 52 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:
	* G (U+0047): L<<401.0,0.0>--<390.0,136.0>>/B<<390.0,136.0>-<387.0,96.0>-<367.0,63.0>> = 8.91330465724806
	* M (U+004D): L<<217.0,223.0>--<118.0,627.0>>/L<<118.0,627.0>--<120.0,0.0>> = 13.586215426835068 and M (U+004D): L<<393.0,0.0>--<396.0,623.0>>/L<<396.0,623.0>--<294.0,223.0>> = 14.029651349071994 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:
 * C (U+0043): L<<476.0,491.0>--<346.0,492.0>>
 * E (U+0045): L<<120.0,458.0>--<440.0,457.0>>
 * E (U+0045): L<<440.0,361.0>--<120.0,362.0>>
 * F (U+0046): L<<120.0,458.0>--<440.0,457.0>>
 * F (U+0046): L<<440.0,361.0>--<120.0,362.0>>
 * G (U+0047): L<<464.0,516.0>--<333.0,517.0>>
 * G (U+0047): L<<474.0,390.0>--<476.0,0.0>>
 * M (U+004D): L<<118.0,627.0>--<120.0,0.0>>
 * M (U+004D): L<<393.0,0.0>--<396.0,623.0>> and M (U+004D): L<<472.0,768.0>--<471.0,0.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[17] HasubiMono-ExtraBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check `Google Fonts Latin Core` glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0021 (EXCLAMATION MARK)

	- 0x0022 (QUOTATION MARK)

	- 0x0023 (NUMBER SIGN)

	- 0x0024 (DOLLAR SIGN)

	- 0x0025 (PERCENT SIGN)

	- 0x0026 (AMPERSAND)

	- 0x0027 (APOSTROPHE)

	- 0x0028 (LEFT PARENTHESIS)

	- 0x0029 (RIGHT PARENTHESIS)

	- 0x002A (ASTERISK)
 
	- And 135 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** Font lacks NameID 13 (LICENSE DESCRIPTION). A proper licensing entry must be set. [code: missing]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 272, but got 208 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>


* 🔥 **FAIL** OS/2 sTypoAscender (795) and hhea ascent (992) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> Font contains glyphs for whitespace characters? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphs">com.google.fonts/check/whitespace_glyphs</a>)</summary><div>


* 🔥 **FAIL** Whitespace glyph missing for codepoint 0x00A0. [code: missing-whitespace-glyph-0x00A0]
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
	- uniFEBB
	- uniFE8C
	- gafsarkashabovear
	- doublestrokear
	- uni066F.fina
	- uni0654064C
	- uni0651064C
	- uniFE88
	- lam_alefWaslaar.fina
	- miniKehehar 
	- And 77 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: comma	Contours detected: 0	Expected: 1
	- Glyph name: hyphen	Contours detected: 0	Expected: 1
	- Glyph name: period	Contours detected: 0	Expected: 1
	- Glyph name: zero	Contours detected: 0	Expected: 2 or 3
	- Glyph name: one	Contours detected: 0	Expected: 1
	- Glyph name: two	Contours detected: 0	Expected: 1
	- Glyph name: three	Contours detected: 0	Expected: 1
	- Glyph name: four	Contours detected: 0	Expected: 1 or 2
	- Glyph name: five	Contours detected: 0	Expected: 1
	- Glyph name: six	Contours detected: 0	Expected: 1 or 2 
	- And 64 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/hhea.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* ⚠ **WARN** OS/2 sTypoLineGap is not equal to 0. [code: OS/2]
</div></details><details><summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info">com.google.fonts/check/gpos_kerning_info</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* m (U+006D): X=444.0,Y=574.5 (should be at x-height 575?)
	* uni0654 (U+0654): X=54.0,Y=797.0 (should be at ascender 795?) and uni0654 (U+0654): X=134.0,Y=749.0 (should be at cap-height 750?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:
	* H (U+0048) contains a short segment L<<88.0,0.0>--<80.0,8.0>>
	* H (U+0048) contains a short segment L<<80.0,696.0>--<88.0,704.0>>
	* H (U+0048) contains a short segment L<<144.0,704.0>--<152.0,696.0>>
	* H (U+0048) contains a short segment L<<152.0,407.0>--<160.0,399.0>>
	* H (U+0048) contains a short segment L<<352.0,399.0>--<360.0,407.0>>
	* H (U+0048) contains a short segment L<<360.0,696.0>--<368.0,704.0>>
	* H (U+0048) contains a short segment L<<424.0,704.0>--<432.0,696.0>>
	* H (U+0048) contains a short segment L<<432.0,8.0>--<424.0,0.0>>
	* H (U+0048) contains a short segment L<<368.0,0.0>--<360.0,8.0>>
	* H (U+0048) contains a short segment L<<360.0,311.0>--<352.0,319.0>> and 52 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:
	* G (U+0047): L<<401.0,0.0>--<390.0,136.0>>/B<<390.0,136.0>-<387.0,96.0>-<367.0,63.0>> = 8.91330465724806
	* M (U+004D): L<<217.0,223.0>--<118.0,627.0>>/L<<118.0,627.0>--<120.0,0.0>> = 13.586215426835068 and M (U+004D): L<<393.0,0.0>--<396.0,623.0>>/L<<396.0,623.0>--<294.0,223.0>> = 14.029651349071994 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:
 * C (U+0043): L<<476.0,491.0>--<346.0,492.0>>
 * E (U+0045): L<<120.0,458.0>--<440.0,457.0>>
 * E (U+0045): L<<440.0,361.0>--<120.0,362.0>>
 * F (U+0046): L<<154.0,474.0>--<440.0,473.0>>
 * G (U+0047): L<<464.0,516.0>--<333.0,517.0>>
 * G (U+0047): L<<474.0,390.0>--<476.0,0.0>>
 * M (U+004D): L<<118.0,627.0>--<120.0,0.0>>
 * M (U+004D): L<<393.0,0.0>--<396.0,623.0>> and M (U+004D): L<<472.0,768.0>--<471.0,0.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[16] HasubiMono-SemiBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check `Google Fonts Latin Core` glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0021 (EXCLAMATION MARK)

	- 0x0022 (QUOTATION MARK)

	- 0x0023 (NUMBER SIGN)

	- 0x0024 (DOLLAR SIGN)

	- 0x0025 (PERCENT SIGN)

	- 0x0026 (AMPERSAND)

	- 0x0027 (APOSTROPHE)

	- 0x0028 (LEFT PARENTHESIS)

	- 0x0029 (RIGHT PARENTHESIS)

	- 0x002A (ASTERISK)
 
	- And 135 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** Font lacks NameID 13 (LICENSE DESCRIPTION). A proper licensing entry must be set. [code: missing]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 272, but got 208 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>


* 🔥 **FAIL** OS/2 sTypoAscender (750) and hhea ascent (992) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> Font contains glyphs for whitespace characters? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphs">com.google.fonts/check/whitespace_glyphs</a>)</summary><div>


* 🔥 **FAIL** Whitespace glyph missing for codepoint 0x00A0. [code: missing-whitespace-glyph-0x00A0]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
	- uniFEBB
	- uniFE8C
	- gafsarkashabovear
	- doublestrokear
	- uni066F.fina
	- uni0654064C
	- uni0651064C
	- uniFE88
	- lam_alefWaslaar.fina
	- miniKehehar 
	- And 77 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: comma	Contours detected: 0	Expected: 1
	- Glyph name: hyphen	Contours detected: 0	Expected: 1
	- Glyph name: period	Contours detected: 0	Expected: 1
	- Glyph name: zero	Contours detected: 0	Expected: 2 or 3
	- Glyph name: one	Contours detected: 0	Expected: 1
	- Glyph name: two	Contours detected: 0	Expected: 1
	- Glyph name: three	Contours detected: 0	Expected: 1
	- Glyph name: four	Contours detected: 0	Expected: 1 or 2
	- Glyph name: five	Contours detected: 0	Expected: 1
	- Glyph name: six	Contours detected: 0	Expected: 1 or 2 
	- And 64 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/hhea.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* ⚠ **WARN** OS/2 sTypoLineGap is not equal to 0. [code: OS/2]
</div></details><details><summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info">com.google.fonts/check/gpos_kerning_info</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* C (U+0043): X=420.0,Y=725.5 (should be at cap-height 727?) and uni0654 (U+0654): X=134.0,Y=749.0 (should be at ascender 750?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:
	* H (U+0048) contains a short segment L<<88.0,0.0>--<80.0,8.0>>
	* H (U+0048) contains a short segment L<<80.0,696.0>--<88.0,704.0>>
	* H (U+0048) contains a short segment L<<144.0,704.0>--<152.0,696.0>>
	* H (U+0048) contains a short segment L<<152.0,407.0>--<160.0,399.0>>
	* H (U+0048) contains a short segment L<<352.0,399.0>--<360.0,407.0>>
	* H (U+0048) contains a short segment L<<360.0,696.0>--<368.0,704.0>>
	* H (U+0048) contains a short segment L<<424.0,704.0>--<432.0,696.0>>
	* H (U+0048) contains a short segment L<<432.0,8.0>--<424.0,0.0>>
	* H (U+0048) contains a short segment L<<368.0,0.0>--<360.0,8.0>>
	* H (U+0048) contains a short segment L<<360.0,311.0>--<352.0,319.0>> and 52 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:
	* G (U+0047): L<<401.0,0.0>--<390.0,136.0>>/B<<390.0,136.0>-<387.0,96.0>-<367.0,63.0>> = 8.91330465724806
	* M (U+004D): L<<217.0,223.0>--<118.0,627.0>>/L<<118.0,627.0>--<120.0,0.0>> = 13.586215426835068 and M (U+004D): L<<393.0,0.0>--<396.0,623.0>>/L<<396.0,623.0>--<294.0,223.0>> = 14.029651349071994 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:
 * C (U+0043): L<<476.0,491.0>--<346.0,492.0>>
 * E (U+0045): L<<120.0,458.0>--<440.0,457.0>>
 * E (U+0045): L<<440.0,361.0>--<120.0,362.0>>
 * F (U+0046): L<<137.0,466.0>--<440.0,465.0>>
 * F (U+0046): L<<440.0,335.0>--<137.0,336.0>>
 * G (U+0047): L<<464.0,516.0>--<333.0,517.0>>
 * G (U+0047): L<<474.0,390.0>--<476.0,0.0>>
 * M (U+004D): L<<118.0,627.0>--<120.0,0.0>>
 * M (U+004D): L<<393.0,0.0>--<396.0,623.0>> and M (U+004D): L<<472.0,768.0>--<471.0,0.0>> [code: found-semi-vertical]
</div></details><br></div></details>
### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 40 | 66 | 665 | 37 | 462 | 0 |
| 0% | 3% | 5% | 52% | 3% | 36% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
