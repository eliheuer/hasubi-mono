"""Compare migrated sources using the compiler selected for Hasubi."""
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

from fgtools import diff, project
from fgtools.build_source_snapshot import build_fonts

source = project.load()
with TemporaryDirectory(prefix="hasubi-diff-") as tmp:
    tmp = Path(tmp)
    base = diff.sources_at(sys.argv[1], source.root, tmp / "base")
    before = build_fonts(base, tmp / "before", "fontmake", quiet=True)
    after = build_fonts(source.config_path, tmp / "after", "fontmake", quiet=True)
    old = {font.relative_to(tmp / "before"): font for font in before}
    new = {font.relative_to(tmp / "after"): font for font in after}
    changed = old.keys() != new.keys()
    for name in sorted(old.keys() ^ new.keys()):
        print("Font inventory changed:", name)
    for name in sorted(old.keys() & new.keys()):
        report = source.root / "output/diff" / name.stem
        lines, images_changed = diff.summary(diff.diffenator(old[name], new[name], report))
        print(name, *lines, sep="\n")
        changed |= images_changed
    raise SystemExit(int(changed))
