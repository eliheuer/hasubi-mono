"""Apply the pinned layout and link checks while retaining Hasubi's design archive."""
from fgtools import check_repository as checks
from fgtools import project

root = project.load().root
files = checks.tracked(root)
# These inputs and specimens predate the Font.Garden layout. Preserve the
# original Glyphs file, including its editor metadata, above the shared size cap.
legacy = {
    "sources/Hasubi-Mono.glyphs", "sources/gf-core-glyphs.txt",
    "sources/test-strings.txt", "documentation/refrence/browne.jpg",
}
archive_dirs = ("sources/master_ufo/", "documentation/drawbot/")
current = [p for p in files if p not in legacy and not p.startswith(archive_dirs)]
checks.OPTIONAL = [*checks.OPTIONAL, "sources/qa-baseline.toml", "documentation/site.html"]
issues = (checks.layout_problems(root, current) + checks.reference_problems(root, files)
          + checks.contents_problems(root, files))
for issue in issues:
    print(issue)
if issues:
    raise SystemExit(1)
print("Repository layout and document references pass.")
