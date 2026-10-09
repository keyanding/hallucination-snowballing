"""Deterministic nested relation tasks; no model-dependent construction."""
import random
import re
from experiments.v3_6_1.design import normalize, sha, token_info

LEVELS = ('EASY', 'MID', 'HARD')
SIZES = dict(EASY=3, MID=5, HARD=8)
DISTRACTORS = dict(EASY=0, MID=2, HARD=6)


def make_cases(tok, old):
    pool = [f'{role}_{letter}{n:02}' for role in ('ENTITY', 'STATE', 'OUTCOME')
            for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' for n in range(100)]
    audit = [token_info(tok, v) | dict(eligible=v not in old) for v in pool]
    rng = random.Random(3640)
    candidates = {}
    for role in ('ENTITY', 'STATE', 'OUTCOME'):
        sub = [r for r in audit if r['eligible'] and r['raw'].startswith(role+'_')]
        minimum = min(r['token_count'] for r in sub)
        candidates[role] = [r['raw'] for r in sub if r['token_count'] == minimum]
        rng.shuffle(candidates[role])
    used, cases = set(), []
    for split in ('development', 'confirmation'):
        for i in range(24):
            suffixes = set()
            def take(role):
                value = next(v for v in candidates[role] if v not in used and v.split('_')[-1] not in suffixes)
                used.add(value)
                suffixes.add(value.split('_')[-1])
                return value
            markers = rng.sample(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 8)
            members = [dict(entity=take('ENTITY'), state=take('STATE'), outcome=take('OUTCOME'), marker=m) for m in markers]
            eo, mo = list(range(8)), list(range(8))
            rng.shuffle(eo)
            rng.shuffle(mo)
            cases.append(dict(case_id=f'v364-{split}-{i+1:03}', split=split,
                              members=members, entity_order=eo, mapping_order=mo,
                              query=members[0]['entity'], gold=members[0]['state']))
    assert len(used) == 1152 and not used & old
    return cases[:24], cases[24:], [r | dict(selected=r['raw'] in used) for r in audit]


def render(c, level, permutation=False):
    n = SIZES[level]
    members = c['members'][:n]
    entity = [f"{c['members'][i]['entity']} has marker {c['members'][i]['marker']}." for i in c['entity_order'] if i < n]
    mapping = [f"Marker {c['members'][i]['marker']} maps to {c['members'][i]['state']}." for i in c['mapping_order'] if i < n]
    # Properties neither assign markers nor map states; same first two at MID/HARD.
    properties = ('smooth', 'rough', 'striped', 'dotted', 'plain', 'ridged')
    extra = [f"Marker {c['members'][i]['marker']} has texture {properties[i]}." for i in range(DISTRACTORS[level])]
    records = entity + mapping + extra
    if permutation:
        rng = random.Random('v364-order-'+c['case_id']+'-'+level)
        original = records[:]
        rng.shuffle(records)
        assert records != original
    prompt = 'Synthetic relation task.\n\nRecords:\n'+'\n'.join(records)+f"\n\nQuestion:\nWhat state is associated with {c['query']}?\n\nReturn only the state identifier."
    return dict(case_id=c['case_id'], split=c['split'], level=level, permutation=permutation,
                call_id=c['case_id']+'/'+level+('/ORDER' if permutation else ''),
                query=c['query'], expected=c['gold'], state_universe=[m['state'] for m in members],
                downstream_compatibility={m['state']:m['outcome'] for m in members},
                records=records, prompt=prompt, text_sha256=sha(prompt))


def audit_cases(dev, confirm, compatibility):
    assert len(dev) == len(confirm) == 24
    assert len({c['case_id'] for c in dev+confirm}) == 48
    allids = []
    for c in dev+confirm:
        ms = c['members']
        ids = [m[k] for m in ms for k in ('entity', 'state', 'outcome')]
        allids += ids
        assert len(set(ids)) == len({v.split('_')[-1] for v in ids}) == 24
        assert len({m['marker'] for m in ms}) == 8
        assert c['query'] == ms[0]['entity'] and c['gold'] == ms[0]['state']
        assert sorted(c['entity_order']) == sorted(c['mapping_order']) == list(range(8))
        assert compatibility[c['case_id']] == {m['state']:m['outcome'] for m in ms}
        prior = set()
        for level in LEVELS:
            p = render(c, level)
            q = render(c, level, True)
            assert len(p['records']) == 2*SIZES[level]+DISTRACTORS[level]
            assert prior <= set(p['records'])
            prior = set(p['records'])
            assert sorted(p['records']) == sorted(q['records'])
            assert len(set(p['state_universe'])) == SIZES[level]
            assert p['state_universe'].count(c['gold']) == 1
            assert p['prompt'].count('maps to '+c['gold']+'.') == 1
            assert not re.search(r'^\d+[.)] |UNKNOWN|OUTCOME_|candidate|option', p['prompt'], re.M)
    assert len(set(allids)) == 1152
    return dict(passed=True, cases=48, globally_unique_identifiers=1152, all_levels_audited=144)
