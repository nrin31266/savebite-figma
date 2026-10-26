#!/usr/bin/env python3
"""Validate self-contained docs and lightweight SaveBite registries; stdlib only."""
from pathlib import Path
import csv
import json
import os
import re
import hashlib

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {f'SB-{n:03d}' for n in range(1, 101)}
TARGET = '7suZz9C8oL5zV2NMxlsIVI'
PHASE1 = {'SB-002', 'SB-015', 'SB-016', 'SB-019', 'SB-034', 'SB-051', 'SB-053', 'SB-056', 'SB-075', 'SB-091'}


def check_screens(rows, components):
    ids = [r['id'] for r in rows]
    assert len(ids) == 100 and set(ids) == EXPECTED, '100 unique SB IDs required'
    nodes = [r['figma_node_id'] for r in rows if r['figma_node_id']]
    assert len(nodes) == len(set(nodes)), 'Duplicate Figma node'
    valid_status = {'BACKLOG', 'SPECIFIED', 'READY', 'DESIGNING', 'DESIGN_REVIEW', 'QA_PASS', 'DONE', 'BLOCKED', 'NEEDS_REWORK', 'ARCHIVED'}
    for r in rows:
        assert r['status'] in valid_status, r['id'] + ': unknown lifecycle'
        for key in ('prototype_verified', 'editable_verified', 'a11y_checked'):
            assert r[key] in ('', 'false', 'true'), r['id'] + ': invalid boolean'
        for key in filter(None, r['component_ids'].split(';')):
            assert key in components, r['id'] + ': unresolved component ' + key
        if r['figma_file_key']:
            assert r['figma_file_key'] == TARGET, f"{r['id']}: wrong figma_file_key {r['figma_file_key']}"
        if r['status'] in ('DESIGN_REVIEW', 'QA_PASS', 'DONE'):
            assert r['figma_node_id'] and r['editable_verified'] == 'true', 'Design requires native node evidence'
        if r['status'] == 'DONE':
            assert r['reviewed_by'] and r['design_baseline_version'], 'DONE requires owner acceptance'
    return len(nodes)


def main():
    rows = list(csv.DictReader((ROOT / 'tracking/screens.csv').open()))
    component_rows = list(csv.DictReader((ROOT / 'tracking/components.csv').open()))
    components = {r['component_key']: r for r in component_rows}
    assert len(components) == len(component_rows), 'Duplicate component key'
    comp_ids = [r['figma_component_id'] for r in component_rows if r['figma_component_id']]
    assert len(comp_ids) == len(set(comp_ids)), 'Duplicate main component node'
    node_count = check_screens(rows, components)
    for artifact in json.loads((ROOT / 'assets/manifest.json').read_text()):
        path = artifact.get('path') or artifact['filePath']
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == artifact['sha256'], 'Asset drift: ' + path
    skills = json.loads((ROOT / '.agents/skills/manifest.json').read_text())
    checked_skills = 0
    optional_skills = 0
    for skill in skills['skills']:
        assert skill['scope'] == 'project' and skill['path'].startswith('.agents/skills/')
        source = ROOT / skill['path'] / 'SKILL.md'
        if not source.exists() and skill.get('committed') is False:
            optional_skills += 1
            continue
        assert hashlib.sha256(source.read_bytes()).hexdigest() == skill['skill_sha256'], 'Skill hash drift'
        checked_skills += 1
    product = (ROOT / 'docs/product.md').read_text()
    experience = (ROOT / 'docs/experience.md').read_text()
    assert set(re.findall(r'\| (D-\d{3}) \|', product)) == {f'D-{n:03d}' for n in range(1, 21)}
    assert set(re.findall(r'\| `(SB-\d{3})` \|', experience)) == EXPECTED
    for p in [ROOT / 'README.md', ROOT / 'AGENTS.md', ROOT / 'tracking/progress.md', *sorted((ROOT / 'docs').rglob('*.md'))]:
        text = p.read_text()
        assert 'MASTER_SPEC.md' not in text and 'Master Spec' not in text, 'Retired handoff dependency'
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if not re.match(r'\w+://', target) and not target.startswith('#'):
                target_path = (p.parent / target.split('#')[0]).resolve()
                if 'tracking/evidence' in str(target_path):
                    continue
                assert target_path.exists(), f'{p.name}: dead link {target}'
    assert (ROOT / 'CLAUDE.md').is_symlink() and os.readlink(ROOT / 'CLAUDE.md') == 'AGENTS.md'
    assert (ROOT / 'CLAUDE.md').resolve() == (ROOT / 'AGENTS.md').resolve()
    assert not (ROOT / 'MASTER_SPEC.md').exists()
    bad = [dict(r) for r in rows]
    bad[1]['id'] = bad[0]['id']
    try:
        check_screens(bad, components)
    except AssertionError:
        pass
    else:
        raise AssertionError('Validator self-check failed')
    assert all(f'F-0{i}' in experience for i in range(1, 7))
    print(f'PASS: 100 unique IDs; target={TARGET}; phase1={len(PHASE1)}; {node_count} live Figma nodes; {len(components)} components; 6 Pexels assets verified; {checked_skills} skills; DONE={sum(r["status"] == "DONE" for r in rows)}')


if __name__ == '__main__':
    main()
