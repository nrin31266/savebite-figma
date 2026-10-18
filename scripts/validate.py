#!/usr/bin/env python3
"""Validate self-contained docs and evidence-backed SaveBite registries; stdlib only."""
from pathlib import Path
import csv
import json
import os
import re
import hashlib

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {f'SB-{n:03d}' for n in range(1, 101)}
TARGET = 'NLTv70kDZ2i3HpOnOKQCDY'
PILOT = {'SB-015', 'SB-034', 'SB-051', 'SB-053', 'SB-056'}


def check_screens(rows, components, evidence):
    ids = [r['id'] for r in rows]
    assert len(ids) == 100 and set(ids) == EXPECTED, '100 unique SB IDs required'
    nodes = [r['figma_node_id'] for r in rows if r['figma_node_id']]
    assert len(nodes) == len(set(nodes)), 'Duplicate Figma node'
    valid_status = {'BACKLOG', 'SPECIFIED', 'READY', 'DESIGNING', 'DESIGN_REVIEW', 'QA_PASS', 'DONE', 'BLOCKED', 'NEEDS_REWORK', 'ARCHIVED'}
    live = {s['screenId']: s for s in evidence.get('screens', [])}
    for r in rows:
        assert r['status'] in valid_status, r['id'] + ': unknown lifecycle'
        for key in ('prototype_verified', 'editable_verified', 'a11y_checked'):
            assert r[key] in ('', 'false', 'true'), r['id'] + ': invalid boolean'
        for key in filter(None, r['component_ids'].split(';')):
            assert key in components, r['id'] + ': unresolved component ' + key
        if r['figma_node_id']:
            assert r['figma_file_key'] == TARGET and r['figma_page_id'], 'Wrong file/page'
            assert r['id'] in live and live[r['id']]['id'] == r['figma_node_id'], 'Missing read-back mapping'
        if r['status'] in ('DESIGN_REVIEW', 'QA_PASS', 'DONE'):
            assert r['figma_node_id'] and r['editable_verified'] == 'true', 'Design requires native node evidence'
        if r['status'] in ('QA_PASS', 'DONE'):
            assert r['qa_result'] == 'PASS' and r['qa_screenshot'] and r['a11y_checked'] == 'true', 'QA evidence missing'
        if r['status'] == 'DONE':
            assert r['reviewed_by'] and r['design_baseline_version'], 'DONE requires owner acceptance'
    if live:
        assert set(live) == PILOT, 'Pilot scope changed'
        assert evidence['fileKey'] == TARGET, 'Evidence from wrong file'
    return len(nodes)


def main():
    rows = list(csv.DictReader((ROOT / 'tracking/screens.csv').open()))
    components = {r['component_key']: r for r in csv.DictReader((ROOT / 'tracking/components.csv').open())}
    path = ROOT / 'tracking/evidence/figma-readback.json'
    evidence = json.loads(path.read_text()) if path.exists() else {}
    node_count = check_screens(rows, components, evidence)
    live_components = {c['id'] for c in evidence.get('components', [])}
    assert len(components) == 15 and {c['figma_component_id'] for c in components.values()} == live_components, 'Component read-back drift'
    qa = json.loads((ROOT / 'tracking/evidence/qa.json').read_text())
    assert not evidence['errors'] and qa['readback_checks'] == evidence['checks']
    assert {w['width'] for w in qa['width_stress']} == {360, 430}
    assert all(not s['overflows'] for w in qa['width_stress'] for s in w['screens'])
    assert all(s['width'] == 390 for s in evidence['screens']), 'Stress width not restored'
    assert all(c['ratio'] >= 4.5 for c in qa['contrast'])
    assert len(qa['connected_hit_targets']) == 9 and all(t['width'] >= 48 and t['height'] >= 48 for t in qa['connected_hit_targets'])
    for artifact in [*qa['screenshots'], *json.loads((ROOT / 'assets/manifest.json').read_text())]:
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
            continue  # Optional local install; not redistributed in public clones.
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
                assert (p.parent / target.split('#')[0]).exists(), f'{p.name}: dead link {target}'
    assert (ROOT / 'CLAUDE.md').is_symlink() and os.readlink(ROOT / 'CLAUDE.md') == 'AGENTS.md'
    assert (ROOT / 'CLAUDE.md').resolve() == (ROOT / 'AGENTS.md').resolve()
    assert not (ROOT / 'MASTER_SPEC.md').exists()
    # Self-check the guard against a duplicate ID, which must fail even with 100 rows.
    bad = [dict(r) for r in rows]
    bad[1]['id'] = bad[0]['id']
    try:
        check_screens(bad, components, evidence)
    except AssertionError:
        pass
    else:
        raise AssertionError('Validator self-check failed')
    assert all(f'F-0{i}' in experience for i in range(1, 7))
    print(f'PASS: 100 unique IDs; 20 defaults; 6 flows; docs links; canonical symlink; {node_count} Figma mappings; 15 components; QA/asset hashes; {checked_skills} skill hashes ({optional_skills} optional local installs absent); 360/430 widths; contrast; 9 targets; DONE={sum(r["status"] == "DONE" for r in rows)}; duplicate-ID self-check')


if __name__ == '__main__':
    main()
