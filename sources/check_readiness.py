"""Report design findings in every foreground master and built weight."""

from collections import Counter
import contextlib
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import tomllib
import unicodedata

from glyphsets import unicodes_per_glyphset

from fgtools import glif_lint, project, qa, shaped_font, source_inventory
from fontTools.ttLib import TTFont

from check_donors import affected, structure, users_of


def source_report(source, output):
    design = source.design()
    masters = {m: source_inventory.load_master(source.root, m, design) for m in source.masters}
    names = set.union(*(set(glyphs) for glyphs in masters.values()))
    missing = {m: sorted(names - glyphs.keys()) for m, glyphs in masters.items()}
    mismatch = []
    for name in sorted(set.intersection(*(set(g) for g in masters.values()))):
        records = [glyphs[name] for glyphs in masters.values()]
        if any(structure(record) != structure(records[0]) for record in records):
            mismatch.append(name)
    summary = {}
    for master, glyphs in masters.items():
        users = users_of(glyphs)
        green = {n for n, g in glyphs.items() if g['color']['protected']}
        donors = {n: sorted(affected(n, users) & green) for n in glyphs.keys() - green}
        summary[master] = {
            'glyphs': len(glyphs),
            'grades': Counter(g['color']['name'] for g in glyphs.values()),
            'protected_green': sorted(green),
            'additional_locked_donors': {n: locks for n, locks in sorted(donors.items()) if locks},
            'missing': missing[master],
            'width_exceptions': {n: g['advance'] for n, g in glyphs.items()
                                 if g['advance'] not in (None, 0, design['spacing']['terminal_cell'])},
        }
    with (output / 'glif-lint.txt').open('w') as stream, contextlib.redirect_stdout(stream):
        glif_lint.lint(root=source.root)
    # Nested UFO components are audit information. The production build flattens them.
    glif_issues = [line.strip() for line in (output / 'glif-lint.txt').read_text().splitlines()
                   if line.startswith('  ') and 'nested component ->' not in line]
    return {'masters': summary, 'incompatible': mismatch, 'structural_errors': glif_issues}


def location_report(instance, samples, cell, latin_core):
    inkless, widths = {}, {}
    for code, name in instance.cmap.items():
        char = chr(code)
        category = unicodedata.category(char)
        if category in ('Cc', 'Cf'):
            continue
        key = f'U+{code:04X} {name}'
        if not category.startswith('Z') and instance.bounds(name) is None:
            inkless[key] = unicodedata.name(char, '')
        advance = instance.shaper.get_glyph_h_advance(instance.font.getGlyphID(name))
        expected = 0 if category in ('Mn', 'Me') else cell
        if advance != expected:
            widths[key] = advance
    # The first release requires alef through tav, including the five finals.
    missing_hebrew = []
    hebrew = {code: instance.cmap.get(code) for code in range(0x05D0, 0x05EB)}
    mappings = Counter(hebrew.values())
    for code, name in hebrew.items():
        box = instance.bounds(name) if name and instance.font.getGlyphID(name) else None
        if mappings[name] != 1 or not box or box[0] >= box[2] or box[1] >= box[3]:
            missing_hebrew.append(f'U+{code:04X} {chr(code)}')
    words = {}
    for label, text in samples.items():
        rows = instance.shape(text)
        words[label] = {
            'text': text,
            'advance': sum(pos.x_advance for _, _, pos in rows),
            'glyphs': [name for name, _, _ in rows],
            'without_ink': sorted({name for name, box, _ in rows if box is None and name != 'space'}),
        }
    core_visible = {code for code in latin_core if not unicodedata.category(chr(code)).startswith('Z')
                    and unicodedata.category(chr(code)) not in ('Cc', 'Cf')}
    missing_core = sorted(latin_core - instance.cmap.keys())
    blank_core = [key for key in inkless if int(key.split()[0][2:], 16) in core_visible]
    latin = {
        'required_codepoints': len(latin_core), 'encoded': len(latin_core) - len(missing_core),
        'expected_to_show_ink': len(core_visible),
        'drawn_visible': len(core_visible - set(missing_core)) - len(blank_core),
        'missing': [f'U+{code:04X}' for code in missing_core], 'blank_visible': blank_core,
    }
    return {'gf_latin_core': latin, 'visible_without_ink': inkless, 'width_exceptions': widths, 'shaping': words,
            'hebrew_letters_drawn': 27 - len(missing_hebrew), 'hebrew_missing_blank_or_aliased': missing_hebrew}


def run_profile(source, output, fonts):
    checks = ('interpolation_issues', 'contour_count', 'outline_direction',
              'overlapping_path_segments', 'opentype/monospace', 'family/win_ascent_and_descent',
              'googlefonts/glyphsets/shape_languages', 'fontgarden/arabic_joins',
              'fontgarden/mark_glyphs', 'fontgarden/marks_attach', 'fontgarden/stacked_marks',
              'fontgarden/hebrew_marks_clear', 'fontgarden/precomposed_match')
    with tempfile.TemporaryDirectory() as scratch:
        plugin = Path(scratch) / 'fontgarden-fontspectorplugin'
        plugin.write_text(qa.PLUGIN.format(python=sys.executable))
        plugin.chmod(0o755)
        scratch_report = Path(scratch) / 'design-checks.json'
        command = [Path(sys.executable).with_name('fontspector'), '--plugin', plugin, '-p', 'fontgarden',
                   '--full-lists', '--skip-network', '--succinct', '--json', scratch_report]
        for check in checks:
            command.extend(['-c', check])
        with (output / 'fontspector.log').open('w') as log:
            result = subprocess.run([*command, *fonts], stdout=log, stderr=subprocess.STDOUT,
                                    env=dict(os.environ, FGTOOLS_PROJECT=str(source.root)))
        if result.returncode not in (0, 1):
            raise RuntimeError(f"Fontspector failed. See {log.name}")
        report = json.loads(scratch_report.read_text())
        (output / 'design-checks.json').write_bytes(scratch_report.read_bytes())
    findings = []
    for path, sections in report['results'].items():
        for section in sections.values():
            for check in section:
                if check['worst_status'] in {'WARN', 'FAIL', 'ERROR', 'FATAL'}:
                    findings.append({'font': Path(path).name, 'check': check['check_id'],
                                     'status': check['worst_status']})
    return findings


def write_summary(output, report):
    first, *rest = report['weights'].values()
    locations = [first, *rest]
    missing_hebrew = {item for loc in locations for item in loc['hebrew_missing_blank_or_aliased']}
    hebrew = 27 - len(missing_hebrew)
    core = first['gf_latin_core']
    blank = sorted({key for loc in locations for key in loc['gf_latin_core']['blank_visible']})
    widths = sorted({key for loc in locations for key in loc['width_exceptions']})
    checks = {f['check'] for f in report['fontspector_findings']}
    lines = [
        '# Hasubi Mono design readiness', '',
        f"Variable font SHA-256 `{report['sha256']}`. Tested weights {', '.join(report['weights'])}.", '',
        '## First-release drawings', '',
        f'- **Hebrew** · {hebrew}/27 distinct encoded letters have ink at every sampled location '
        'from alef through tav, including the five finals.',
    ]
    if hebrew < 27:
        lines += [
            '  Begin with a designer-led Regular pilot of א ב ו מ ש. Inspect אבא, שוב and מבוא '
            'in terminal text. Approve the construction, then review Black and an intermediate weight.',
            '  Extend the pilot in three groups, ד ה ח ר ת כ ך, then ג ז י ל נ ן ס ם, then ט ע פ ף צ ץ ק. '
            'Review finals in words and שלום beside numbers and Latin code. The designer grades the drawings.',
        ]
    lines.append(
        f"- **GF Latin Core** · {core['encoded']}/{core['required_codepoints']} encoded at the first weight. "
        f"{core['drawn_visible']}/{core['expected_to_show_ink']} visible characters have ink there. "
        f"Visible characters missing ink across tested weights include {', '.join(blank) or 'none'}. Check marks alone and on letters."
    )
    missing_ink = {k: name for loc in locations for k, name in loc['visible_without_ink'].items()}
    arabic = sorted(key.split()[0] for key, name in missing_ink.items() if 'ARABIC' in name)
    if arabic:
        lines.append('- **Arabic** · Draw the blank punctuation, signs and combining marks. Check '
                     'beh with fatha, damma, kasra and shadda in real words. The following Arabic codepoints are blank across the samples: '
                     + ', '.join(arabic) + '.')
    lines += ['', '## Shaping and terminal text', '']
    cases = {
        'googlefonts/glyphsets/shape_languages': 'Inspect the failing language rows and reproduce each string '
            'with HarfBuzz. Review modern Arabic joining and Latin combining-mark coverage.',
        'fontgarden/marks_attach': 'Proof combining marks on their actual bases at terminal size. '
            'Compare x plus acute followed by x, and Dutch íj́.',
        'fontgarden/precomposed_match': 'Compare the precomposed and decomposed forms in subsets. '
            'Check the drawing and anchor offsets in both masters before changing shared donors.',
        'fontgarden/stacked_marks': 'Review close accent stacks at the heaviest weight and check mark-to-mark anchors.',
        'fontgarden/arabic_joins': 'Compare the measured gaps against Hasubi’s intended metal-type effect in '
            'real Arabic words. The shared gap test alone cannot determine whether a join is broken.',
        'family/win_ascent_and_descent': 'Compare the highest accented outlines to the clipping bounds. '
            'Decide the vertical metrics with the designer.',
    }
    for check, advice in cases.items():
        if check in checks:
            lines.append(f'- {advice} (`{check}`)')
    if widths:
        lines.append('- Review width exceptions in repeated code columns and choose which should occupy a '
                     f"full terminal cell: {', '.join(widths)}.")
    issues = len(report['incompatible']) + len(report['structural_errors'])
    lines += ['', '## Masters and grades', '',
              f'- Cross-master structure and foreground GLIF lint found {issues} structural errors '
              '(nested source components are reported separately).',
              '- The compiled interpolation check ' + ('flagged glyphs for review.'
              if 'interpolation_issues' in checks else 'reported no interpolation findings.'),
              '- Existing greens lock source drawings and their component donors under the project’s drafting '
              'workflow. Counts describe editing permissions. Human review establishes design approval.', '',
              '[Glyph-level design results](design.json) · [Fontspector details](design-checks.json) · '
              '[Foreground GLIF lint](glif-lint.txt)', '']
    (output / 'design.md').write_text('\n'.join(lines))


def main():
    source = project.load()
    output = source.root / 'output/readiness'
    output.mkdir(parents=True, exist_ok=True)
    masters = source_report(source, output)
    path, = (source.fonts / 'variable').glob('*.ttf')
    data = path.read_bytes()
    samples = {key: row['text'] for key, row in
               tomllib.loads((source.sources / 'proof-samples.toml').read_text())['sample'].items()}
    # Keep samples for the three languages flagged by the orthography check.
    samples.update({'dutch-acute': 'íj́', 'arabic-maksura': 'ى‍ى‍', 'vietnamese-horn': 'ơ'})
    cell = source.design()['spacing']['terminal_cell']
    latin_core = set(unicodes_per_glyphset('GF_Latin_Core'))
    with TTFont(path) as font:
        axis, = [axis for axis in font['fvar'].axes if axis.axisTag == 'wght']
        named = sorted({axis.minValue, axis.maxValue, *(i.coordinates['wght'] for i in font['fvar'].instances)})
        weights = sorted({*named, *((a + b) / 2 for a, b in zip(named, named[1:]))})
        locations = {}
        for weight in weights:
            instance = shaped_font.Instance(path.name, font, data, weight)
            locations[f'{weight:g}'] = location_report(instance, samples, cell, latin_core)
    findings = run_profile(source, output, [path, *sorted((source.fonts / 'ttf').glob('*.ttf'))])
    report = {**masters, 'variable_font': path.name, 'sha256': hashlib.sha256(data).hexdigest(),
              'weights': locations, 'fontspector_findings': findings}
    write_summary(output, report)
    (output / 'design.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    for master, info in masters['masters'].items():
        print(f"{master}: {info['glyphs']} foreground glyphs, {len(info['protected_green'])} green, "
              f"{len(info['additional_locked_donors'])} additional locked donors.")
    for weight, location in locations.items():
        print(f"{weight}: {len(location['visible_without_ink'])} visible characters without ink, "
              f"{len(location['width_exceptions'])} encoded width exceptions, "
              f"{location['hebrew_letters_drawn']}/27 Hebrew letters drawn.")
    print(f"Full design evidence: {output}")
    return bool(masters['incompatible'] or masters['structural_errors']
                or any(m['missing'] for m in masters['masters'].values())
                or any(loc['hebrew_letters_drawn'] < 27 or loc['gf_latin_core']['missing']
                       or loc['visible_without_ink'] or loc['width_exceptions']
                       for loc in locations.values())
                or any(row['status'] in {'ERROR', 'FATAL'}
                       or row['status'] == 'FAIL' and row['check'] != 'fontgarden/arabic_joins'
                       or row['check'] == 'interpolation_issues' for row in findings))


if __name__ == '__main__':
    raise SystemExit(main())
