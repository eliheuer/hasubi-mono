# Hasubi Mono

Hasubi Mono (حاسوبي مونو) is Eli Heuer’s condensed, horizontal-contrast monospace for terminals and text editors. The Arabic gives the family its stroke contrast. Latin follows it across the same narrow columns. Hebrew is part of the design brief. The 27 encoded Hebrew letters currently have empty outlines.

## Construction

1. Keep the 1000-unit em, the terminal cell specified below and the existing per-glyph advances. The sources include width exceptions. Test a line of code for column alignment and marks for attachment. An assignment to one letter does not authorize a change to the family’s metrics.
2. Follow the Arabic-derived horizontal contrast. Judge the stroke direction, counter and terminal against Hasubi drawings at the same weight. The designspace records separate H and Arabic stroke measurements. Preserve existing contour points, optical offsets and curve handles when reusing a construction.
3. Preserve the deliberate gaps in Arabic joins. Compare the initial, medial and final forms in the same word against the print specimen. The reference photograph of Browne’s 1918 *Materials for the Study of the Bábí Religion* illustrates the influence of metal type. The proposed GAPS axis has no masters or coordinates in this source.
4. Keep the Regular and Black masters compatible across the mapped weight axis. User weights 400, 500, 600, 700, 800 and 900 map to source positions 72, 82, 92, 102, 112 and 128. Inspect an intermediate weight as well as both ends. Preserve point order, component transforms, mark anchors and mark stacking.
5. Keep inherited placeholders visible in proofs. Encoding a character and drawing it are separate steps. A designer assignment is required for new drawings, including Hebrew and unfinished Arabic marks.

The DrawBot print proof supplies Arabic joining sequences, terminal code and paired Arabic and Latin samples. The accent test string comes from `sources/test-strings.txt`. The historical width comparison is with Input Mono Compressed.

## Source colors

The original Glyphs file uses two distinct greens (indices 4 and 5), red (0) and unmarked glyphs. Preserve both green values in the UFOs. Both are protected along with their component donors. Their original distinction has no documented review meaning. The designer identifies which protected glyphs are suitable drawing references before an agent uses them.

```toml
[spacing]
terminal_cell = 512

[colors.green]
rgba = [[0.04, 0.57, 0.04, 1], [0.67, 0.95, 0.38, 1], [0, 1, 0, 1], [0.09, 0.72, 0.44, 1]]
policy = "Frozen. Confirm donor eligibility with the designer."
[colors.red]
rgba = [[0.85, 0.26, 0.06, 1], [1, 0, 0, 1], [1, 0.29, 0.24, 1]]
policy = "Needs work. Edit only on assignment."
[colors.purple]
rgba = [[0.54, 0.44, 0.88, 1], [0.5, 0, 1, 1]]
policy = "Agent draft awaiting designer review."
[colors.yellow]
rgba = [[1, 1, 0, 1], [1, 0.86, 0.2, 1]]
policy = "Close. Refine the existing construction."
[colors.orange]
rgba = [[1, 0.5, 0, 1], [1, 0.6, 0.06, 1]]
policy = "Revise the named construction."
```

## Quality review

The full Fontspector report retains inherited findings from the Glyphs build, including off-grid coordinates, intentional join gaps, missing ink, mark placement and exceptional widths. The Hasubi baseline gate checks new failures in each font and check. A passing migration gate does not establish release readiness.

## Hebrew

The first release includes all 27 base and final letters from alef to tav. Review a pilot in both masters before extending the alphabet. Set the letters on the family’s terminal cell and establish the horizontal stroke contrast, counters, roof heights and terminal shapes in actual Hebrew words. The designer chooses the references and grades the pilot. Proof the five finals at word endings and test the completed alphabet alongside Latin code, Arabic text, numerals and punctuation.
