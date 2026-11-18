"""Render the fgtools proof with Hasubi's Arabic mark and joining tables."""
import runpy
import sys
import unicodedata
from itertools import chain
from pathlib import Path

from fgtools import media, project
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.transformPen import TransformPen


def draw_marks(sheet, job):
    """Set the mark columns one layout unit inside each two-module cell."""
    marks = [
        ("Fatha", "َ"), ("Damma", "ُ"), ("Kasra", "ِ"), ("Sukun", "ْ"),
        ("Shadda", "ّ"), ("Fathatan", "ً"), ("Dammatan", "ٌ"), ("Kasratan", "ٍ"),
        ("Shadda a", "َّ"), ("Shadda i", "ِّ"),
    ]
    marks = [(name, mark) for name, mark in marks if job.type.covers(mark)]
    bases = [letter for letter in "ابحسصطعفكلمه" if job.type.covers(letter)]
    if not bases or not marks:
        return "the font has no Arabic marks or bases"

    rows = (sheet.rows - 2) // 2
    columns = sheet.cols // 2
    inset = sheet.grid["unit"] / sheet.grid["module"]
    for weight in sorted({job.type.low, job.type.high}):
        for first_mark in range(0, len(marks), columns):
            for first_base in range(0, len(bases), rows):
                page_bases = bases[first_base:first_base + rows]
                sheet.page()
                sheet.header(job.family, "Arabic marks", f"Wght {weight:g}", sheet.size(64), job.stamp)
                for col, (name, mark) in enumerate(marks[first_mark:first_mark + columns]):
                    sheet.label(name, 2 * col + inset, 1, drop=0)
                    for row, base in enumerate(page_bases):
                        sheet.text(base + mark, 2 * col + inset, 2.5 + 2 * row, 64, weight)
                for row in range(len(page_bases) + 1):
                    sheet.rule(2 + 2 * row)


def glyph_path(font, item):
    """Replace one shaped text item with the same ink drawn from the font file."""
    _, origin, baseline, size, weight, color, _, text = item
    font.font.set_variations({"wght": weight})
    buffer = font.hb.Buffer()
    buffer.add_str(text)
    buffer.guess_segment_properties()
    font.hb.shape(font.font, buffer)
    pen = RecordingPen()
    scale = size / font.upm
    for info, pos in zip(buffer.glyph_infos, buffer.glyph_positions):
        transform = (scale, 0, 0, -scale,
                     origin + scale * pos.x_offset, baseline - scale * pos.y_offset)
        font.font.draw_glyph_with_pen(info.codepoint, TransformPen(pen, transform))
        origin += pos.x_advance * scale
        baseline -= pos.y_advance * scale
    verbs = {"moveTo": "M", "lineTo": "L", "qCurveTo": "Q", "curveTo": "C", "closePath": "Z"}
    commands = [(verbs[verb], *chain.from_iterable(points)) for verb, points in pen.value]
    return "path", 0, color, commands


def draw(sheet, job):
    if sheet.name == "hasubi-marks":
        return draw_marks(sheet, job)
    # Use fgtools' exact joining strings and cell geometry. Its PDF renderer can
    # select a system font for a cluster containing an unencoded join control.
    table = runpy.run_path(str(media.DEFAULTS / "proofs" / "arabic-joining.py"))
    skipped = table["draw"](sheet, job)
    for page in sheet.pages:
        for index, item in enumerate(page["items"]):
            if item[0] == "text" and any(unicodedata.bidirectional(c) == "AL" for c in item[-1]):
                page["items"][index] = glyph_path(job.type, item)
    return skipped


def main():
    layout = project.load()
    brand = media.load_brand(layout)
    font, facts = media.font_type(layout)
    job = media.make_job(layout, brand, font, facts)
    # book() loads a built-in page by name, or a project format by its script.
    overrides = {"arabic-marks": "hasubi-marks", "arabic-joining": "hasubi-joining"}
    for name in overrides.values():
        brand["format"][name] = {"script": Path(__file__)}
    pages = [overrides.get(page, page) for page in media.pages(media.PROOF, sys.argv[1:])]
    media.book(layout, brand, job, media.project_layout(layout), media.brand_colors(brand),
               pages, "proof", "output/proof/proof.pdf")


if __name__ == "__main__":
    main()
