"""Render the fgtools proof with room for Hasubi's Arabic sidebearings."""
import sys
from pathlib import Path

from fgtools import media, project


def draw(sheet, job):
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


def main():
    layout = project.load()
    brand = media.load_brand(layout)
    font, facts = media.font_type(layout)
    job = media.make_job(layout, brand, font, facts)
    # book() loads a built-in page by name, or a project format by its script.
    brand["format"]["hasubi-marks"] = {"script": Path(__file__)}
    pages = ["hasubi-marks" if page == "arabic-marks" else page
             for page in media.pages(media.PROOF, sys.argv[1:])]
    media.book(layout, brand, job, media.project_layout(layout), media.brand_colors(brand),
               pages, "proof", "output/proof/proof.pdf")


if __name__ == "__main__":
    main()
