# Building Hasubi Mono

Install Python 3.13 or 3.14 and Rust with Cargo. On Ubuntu, install pkg-config and libfontconfig1-dev for DesignBot. Run `make setup`, then `make build`, `make test` and `make proof`. The build produces a variable TTF, six static TTFs, six OTFs and webfonts. Open the print proof at `output/proof/proof.pdf`. The full Fontspector report is in `output/qa/all/`. If the external font-name service is unavailable after a retry, the development gate reports that check as inconclusive. Release builds require a response. The DrawBot scripts and their checked-in images document earlier design stages.

## Editable sources

Edit the two UFOs referenced by `sources/Hasubi-Mono.designspace`. These derive from all 860 glyphs in the original Glyphs 3 file. The original file and the older 622-glyph UFO snapshot under `sources/master_ufo/` are retained for provenance. Their histories diverged before the migration. Edits go into the top-level designspace and its masters.

The export used the pinned glyphsLib with Glyphs metadata and GDEF generation. Glyphs’ implicit component anchors become explicit, nonspacing marks retain their editor width in the originalWidth lib value, and colliding backup-layer names receive numbered suffixes. The original background-image reference on the sheqel points to a TIFF absent from the repository. The pinned fontc rejects that reference. The build uses the pinned fontmake backend, which preserves the image reference and reproduces the original-source build. Compare future source changes with `make diff BASE=<revision>` using a migrated base.

## Publishing

Push tested work to main. CI builds the fonts, runs QA, and publishes the current print proof and QA report to the project’s GitHub Pages site. Each build provides downloadable font and QA artifacts. Set the version in both masters before tagging. A published GitHub release receives the tested font archive. Creating a release is a separate designer decision. The family is in development under the SIL Open Font License 1.1.
