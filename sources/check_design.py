"""Inspect Hasubi master compatibility, source widths and component references."""
import argparse

from fgtools import project, source_inventory


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("glyphs", nargs="*", help="default: every glyph outside the green grade")
    args = parser.parse_args()
    source = project.load()
    design = source.design()
    masters = {m: source_inventory.load_master(source.root, m, design) for m in source.masters}
    names = set(args.glyphs) or {
        name for glyphs in masters.values() for name, record in glyphs.items()
        if not record["color"]["protected"]
    }
    cell = design["spacing"]["terminal_cell"]
    errors = []
    for name in sorted(names):
        structures = []
        for master, glyphs in masters.items():
            if name not in glyphs:
                errors.append(f"{master} {name}: absent")
                continue
            record = glyphs[name]
            parts = [c["base"] for c in record["components"]]
            structures.append((record["point_types"], parts))
            for part in parts:
                if part not in glyphs:
                    errors.append(f"{master} {name}: missing component {part}")
            advance = record["advance"] or 0
            if advance not in (0, cell):
                print(f"Review width: {master} {name} has advance {advance:g}.")
        if structures and any(s != structures[0] for s in structures[1:]):
            errors.append(f"{name}: contour, point types or component order differ between masters")
    for error in errors:
        print(error)
    print(f"{len(names)} glyphs inspected across {len(masters)} masters, {len(errors)} structural issues.")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
