"""Check a drawing assignment against the protected glyphs in its base commit."""

import argparse
from collections import defaultdict
import io
from pathlib import Path
import subprocess
import tarfile
import tempfile

from fgtools import project, source_inventory


def git(root, *args):
    return subprocess.check_output(["git", *args], cwd=root)


def read_base(root, base, directory):
    # A single snapshot supplies both the dependency graph and the color rules.
    # Recoloring a composite in the working tree cannot unlock its donors.
    archive = git(root, "archive", base, "CONTEXT.md", "sources/config.yaml",
                  ":(glob)sources/*.designspace", ":(glob)sources/*.ufo/glyphs/*")
    with tarfile.open(fileobj=io.BytesIO(archive)) as tree:
        tree.extractall(directory, filter="data")
    before = project.load(directory)
    contract = before.design()
    return {m: source_inventory.load_master(directory, m, contract)
            for m in before.masters}, contract


def users_of(glyphs):
    users = defaultdict(set)
    for name, glyph in glyphs.items():
        for component in glyph["components"]:
            users[component["base"]].add(name)
    return users


def affected(name, users):
    """Every glyph whose rendered design depends on name, including itself."""
    pending = [name]
    seen = set()
    while pending:
        current = pending.pop()
        if current not in seen:
            seen.add(current)
            pending.extend(users[current])
    return seen


def structure(record):
    return (record["point_types"], [c["base"] for c in record["components"]])


def changed_paths(root, base):
    tracked = git(root, "diff", "--name-only", "--no-renames", "-z", base)
    new = git(root, "ls-files", "--others", "--exclude-standard", "-z")
    return {p.decode() for p in (tracked + new).split(b"\0") if p}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default="main")
    parser.add_argument("--glyphs", default="", help="space-separated assigned glyphs")
    parser.add_argument("--masters", default="", help="space-separated assigned masters")
    parser.add_argument("--plan", action="store_true", help="check candidates before editing")
    args = parser.parse_args()
    source = project.load()
    revision = git(source.root, "rev-parse", "--verify", args.base + "^{commit}").decode().strip()
    with tempfile.TemporaryDirectory() as directory:
        before, contract = read_base(source.root, revision, Path(directory))

    masters = set(args.masters.split()) or set(before)
    names = set(args.glyphs.split())
    if not masters <= before.keys():
        parser.error("unknown master: " + ", ".join(sorted(masters - before.keys())))
    if args.plan and not names:
        parser.error("--plan needs --glyphs")
    for master in sorted(masters):
        missing = names - before[master].keys()
        if missing:
            parser.error(f"{master}: unknown glyphs: {', '.join(sorted(missing))}")

    changed = changed_paths(source.root, revision)
    errors = []
    touched = set()
    for master, glyphs in before.items():
        users = users_of(glyphs)
        for name, glyph in glyphs.items():
            edited = glyph["path"] in changed
            if args.plan:
                if master not in masters or name not in names:
                    continue
            elif edited:
                changed.remove(glyph["path"])
                touched.add((master, name))
                if not (source.root / glyph["path"]).is_file():
                    errors.append(f"{master} {name}: assigned GLIF was removed")
                if master not in masters or (names and name not in names):
                    errors.append(f"{master} {name}: outside the assignment")
            else:
                continue
            dependents = affected(name, users)
            locked = sorted(n for n in dependents if glyphs[n]["color"]["protected"])
            print(f"{master} {name} affects: {', '.join(sorted(dependents))}")
            if locked:
                errors.append(f"{master} {name}: protected by {', '.join(locked)}")

    if not args.plan:
        errors.extend(f"Outside assigned foreground GLIFs: {path}" for path in sorted(changed))
        if touched and not errors:
            after = {m: source_inventory.load_master(source.root, m, contract) for m in before}
            for master, name in sorted(touched):
                if after[master][name]["color"]["name"] != "purple":
                    errors.append(f"{master} {name}: a draft must be purple")
            for name in sorted({n for _, n in touched}):
                records = [glyphs.get(name) for glyphs in after.values()]
                if any(r is None for r in records) or any(
                        structure(r) != structure(records[0]) for r in records):
                    errors.append(f"{name}: incompatible contours, point types or components")
    for error in errors:
        print(error)
    print(f"{'FAIL' if errors else 'PASS'} against {revision[:12]}")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
