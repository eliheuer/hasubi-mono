"""Assemble a local google/fonts preview from Hasubi's current build."""

from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory

from fontTools.ttLib import TTFont
from gfmetadata import FamilyProto
from gftools.util.google_fonts import ReadProto, WriteMetadata


ROOT = Path(__file__).resolve().parents[1]
UPSTREAM = "https://github.com/eliheuer/hasubi-mono"
FONT = "fonts/variable/Hasubi-Mono[wght].ttf"
FILES = {
    FONT: "HasubiMono[wght].ttf",
    "OFL.txt": "OFL.txt",
    "documentation/article/ARTICLE.en_us.html": "article/ARTICLE.en_us.html",
}


def main():
    output = ROOT / "output/google-fonts"
    output.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(dir=output) as temporary:
        package = Path(temporary) / "ofl/hasubimono"
        for source, destination in FILES.items():
            path = package / destination
            path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / source, path)

        gftools = Path(sys.executable).with_name("gftools")
        subprocess.run([gftools, "add-font", str(package)], check=True)
        path = package / "METADATA.pb"
        metadata = ReadProto(FamilyProto(), path)
        with TTFont(package / FILES[FONT]) as font:
            metadata.designer = font["name"].getDebugName(9)
        metadata.category[:] = ["MONOSPACE"]
        metadata.classifications[:] = ["MONOSPACE"]
        metadata.primary_script = "Arab"
        metadata.date_added = ""
        # The broad Arabic subset falls below add-font's automatic percentage
        # threshold. It carries the inked letters in the family's Arabic name.
        # Keep the inferred subsets visible for review in the full package QA.
        metadata.subsets[:] = sorted(set(metadata.subsets) | {"arabic"})
        metadata.source.repository_url = UPSTREAM
        metadata.source.branch = "main"
        metadata.source.config_yaml = "sources/config.yaml"
        for source, destination in FILES.items():
            metadata.source.files.add(source_file=source, dest_file=destination)
        # Include a revision only if the package inputs match a Git revision.
        # The built VF is derived from the designspace and UFOs by make build.
        inputs = [
            "Makefile", "requirements.txt", "sources/config.yaml", "sources/*.ufo",
            "sources/*.designspace", "OFL.txt", "documentation/article",
        ]
        dirty = subprocess.check_output(
            ["git", "status", "--porcelain", "--", *inputs], cwd=ROOT
        )
        if not dirty:
            metadata.source.commit = subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
            ).strip()
        WriteMetadata(metadata, path, comments=None)
        text = path.read_text()
        path.write_text(
            "# Local preview. Google Fonts assigns date_added at onboarding.\n"
            "# MONOSPACE and Arab describe the intended category and primary script.\n"
            + text
        )
        target = output / "ofl/hasubimono"
        target.parent.mkdir(exist_ok=True)
        if target.exists():
            shutil.rmtree(target)
        package.rename(target)
    print(f"Local preview: {target}")


if __name__ == "__main__":
    main()
