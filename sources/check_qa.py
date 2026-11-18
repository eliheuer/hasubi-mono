"""Run the complete pinned profile and gate its findings against Hasubi's source baseline."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import subprocess
import sys
import tomllib

from fgtools import project


def measure(check, finding):
    """Fontspector groups many design faults into a single FAIL message."""
    code = finding["code"]
    message = finding.get("message", "")
    if check == "contour_count" and code == "no-contour":
        return code, len(finding["metadata"])
    if check == "fontgarden/grid" and code == "off-grid":
        weight, count = re.match(r"At \{'wght': ([\d.]+)\}, (\d+) glyphs", message).groups()
        return f"{code}@{float(weight):g}", int(count)
    if check.startswith("fontgarden/") and code in {
        "no-ink", "not-attached", "marks-touch", "join-gap", "composite-differs"
    }:
        return code, int(message.split()[0])
    return code, 1


def assess(report, baseline, font_dir):
    limits = baseline["limits"]
    required = set(baseline["subjects"].values())
    subjects = {path: name for name, path in baseline["subjects"].items()}
    seen = set()
    actual = Counter()
    errors, network_errors = [], []
    for path, sections in report["results"].items():
        relative = Path(path).relative_to(font_dir).as_posix()
        seen.add(relative)
        for checks in sections.values():
            for check in checks:
                identifier = check["check_id"]
                for item in check["subresults"]:
                    status = item["severity"]
                    if status == "FAIL":
                        code, amount = measure(identifier, item)
                        actual[(relative, f"{identifier}:{code}")] += amount
                    elif status in {"ERROR", "FATAL"}:
                        message = item.get("message", status)
                        problem = f"{relative} {identifier}: {message}"
                        if identifier == "fontdata_namecheck" and "network error" in message.lower():
                            network_errors.append(problem)
                        else:
                            errors.append(problem)
    errors.extend(f"Missing QA input: {path}" for path in sorted(required - seen))
    for (path, code), count in sorted(actual.items()):
        bound = limits.get(code, {}).get(subjects.get(path), 0)
        if count > bound:
            errors.append(f"{path} {code}: {count} (baseline {bound})")
    return errors, network_errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-online", action="store_true",
                        help="also require the remote font-name service to respond")
    args = parser.parse_args()
    source = project.load()
    baseline = tomllib.loads((source.sources / "qa-baseline.toml").read_text())
    report_path = source.root / "output/qa/all/fontspector.json"
    if source.design().get("qa", {}).get("exclude"):
        sys.exit("Hasubi runs the full profile. Remove check exclusions before comparing.")
    for attempt in range(2):
        # A tool startup failure must never reuse a passing report from a previous run.
        report_path.unlink(missing_ok=True)
        result = subprocess.run([Path(sys.executable).with_name("fgtools"), "qa"])
        if result.returncode not in {0, 1} or not report_path.is_file():
            sys.exit(f"Fontspector did not finish (exit {result.returncode}).")
        report = json.loads(report_path.read_text())
        errors, network_errors = assess(report, baseline, source.fonts)
        if errors or not network_errors or attempt:
            break
        print("The online font name service did not respond. Retrying the full profile.", flush=True)
    if network_errors:
        print("Online name verification was inconclusive after retry:", file=sys.stderr)
        for issue in network_errors:
            print(issue, file=sys.stderr)
        if args.require_online:
            errors.extend(network_errors)
    if errors:
        sys.exit("\n".join(errors))
    if result.returncode and not (report["summary"].get("FAIL") or network_errors):
        sys.exit("Fontspector exited with an error and reported no inherited failures.")
    print(f"Full profile: {report['summary']}. No design failure exceeds the Hasubi baseline.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
