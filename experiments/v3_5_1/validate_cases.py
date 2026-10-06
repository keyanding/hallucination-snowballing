"""Mechanical chain/source validation and frozen city-only output parser."""
import json
import re
import unicodedata
from pathlib import Path
from src.common import digest


def normalize(text):
    return unicodedata.normalize('NFC', text.strip()).casefold().removesuffix('.')


def parse(raw, case, truncated=False):
    value = normalize(raw)
    aliases = {normalize(a): k for k in ('C', 'Cp') for a in case[k + '_aliases']}
    found = {k for a, k in aliases.items() if re.search(r'(?<!\w)' + re.escape(a) + r'(?!\w)', value)}
    if truncated:
        category, subtype, identity = 'INVALID', 'TRUNCATED', None
    elif value in aliases:
        category, subtype, identity = 'VALID', None, aliases[value]
    elif len(found) > 1:
        category, subtype, identity = 'INVALID', 'MULTIPLE', None
    elif value in {'unknown', 'i don\'t know', 'i do not know', 'cannot determine', 'not enough information', 'uncertain'}:
        category, subtype, identity = 'UNKNOWN', None, None
    elif any(term in value for term in ('cannot answer', 'unable to', 'cannot determine', 'not provided', 'not specified')):
        category, subtype, identity = 'UNKNOWN', None, None
    elif found or '\n' in value or len(value.split()) > 8 or not re.fullmatch(r"[^\W\d_]+(?:[ '\-’][^\W\d_]+){0,7}", value):
        category, subtype, identity = 'INVALID', 'NONCOMPLIANT', None
    elif any(w in value.split() for w in ('the', 'is', 'answer', 'because', 'wait', 'sorry')):
        category, subtype, identity = 'INVALID', 'NONCOMPLIANT', None
    else:
        category, subtype, identity = 'OTHER_ANSWER', None, None
    return dict(parse_category=category, invalid_subtype=subtype, identity=identity,
                parse_valid=category in ('VALID', 'OTHER_ANSWER'),
                supplementary_mentions=sorted(found), raw_text=raw)


def classify(parsed, wrong_state):
    if parsed['identity'] == 'C':
        return 'OVERRIDE_TO_GOLD' if wrong_state else 'GOLD_FOLLOW'
    if parsed['identity'] == 'Cp':
        return 'PROPAGATE_WRONG' if wrong_state else 'INDUCED_WRONG'
    return parsed['parse_category']


def validate(cases):
    assert len(cases) == 12 and len({c['A'] for c in cases}) == 12
    assert len({tuple(sorted((c['B'], c['Bp']))) for c in cases}) == 12
    source_path = Path('data/dev.json')
    manifest = json.loads(Path('results/calibration_v3_4_1/dataset_manifest.json').read_text(encoding='utf-8'))
    assert digest(source_path) == manifest['source_sha256']
    source = {r['_id']: r for r in json.loads(source_path.read_text(encoding='utf-8'))}
    from .render_prompts import audit_pair
    for c in cases:
        assert c['B'] != c['Bp'] and normalize(c['C']) != normalize(c['Cp'])
        assert not {normalize(a) for a in c['C_aliases']} & {normalize(a) for a in c['Cp_aliases']}
        for slot, target in [('B', 'C'), ('Bp', 'Cp')]:
            p = c['sources'][slot]
            r = source[p['downstream_source_id']]
            e = p['downstream_evidence']
            assert dict(r['context'])[e['title']][e['sentence_id']] == e['text']
            assert [c[slot], 'place of birth', c[target]] in r['evidences']
            assert parse(c[target], c)['identity'] == target
        # Independent relation parser: a unique synthetic gold edge and unique birth endpoints.
        edges = c['gold_graph']
        first = [e[2] for e in edges if e[:2] == [c['A'], 'credited director']]
        assert first == [c['B']]
        assert [e[2] for e in edges if e[:2] == [c['B'], 'place of birth']] == [c['C']]
        assert [e[2] for e in edges if e[:2] == [c['Bp'], 'place of birth']] == [c['Cp']]
        assert len({c['A'], c['B'], c['Bp'], c['C'], c['Cp']}) == 5
        audit_pair(c)
    return dict(cases=12, unique_gold_paths=12, verified_real_mappings=24, aliases_disjoint=True, main_prompts=72)
