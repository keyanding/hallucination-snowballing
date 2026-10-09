"""Fresh graphs using the unchanged historical HARD/N renderer and person parser."""
import copy
import itertools
import json
import random
from pathlib import Path
from src.common import norm
from src.prepare_v3_4_4 import no_list, make_cases as historical_cases
from src.graph_v3_4_2 import audit_prompt, validate_sources
from src.interface_v3_4_4 import parse_natural
from experiments.v3_6_1.design import sha


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def make_cases():
    old = []
    for folder, names in [('calibration_v3_4_1', ('dev_cases.json','heldout_cases.json')),
                          ('calibration_v3_4_2', ('dev_cases.json','heldout_cases.json')),
                          ('calibration_v3_4_4', ('development_cases.json','confirmation_cases.json'))]:
        for name in names:
            old += read(Path('results')/folder/name)
    people = {p['name']:p for c in old for p in c['candidates']}
    seen = {tuple(sorted(p['name'] for p in c['candidates'])) for c in old}
    fresh, reused = [], []
    for rel in sorted({p['relation'] for p in people.values()}):
        for group in itertools.combinations(sorted(n for n,p in people.items() if p['relation']==rel),4):
            aliases = [{norm(people[n]['target']),*(norm(a) for a in people[n]['target_aliases'])} for n in group]
            if all(not a & b for a,b in itertools.combinations(aliases,2)):
                (reused if group in seen else fresh).append(group)
    rng = random.Random(365)
    rng.shuffle(fresh)
    rng.shuffle(reused)
    bundles = fresh[:48]+reused[:max(0,48-len(fresh))]
    assert len(bundles)==len(set(bundles))==48
    rng.shuffle(bundles)
    graphs = [c for c in old if 'name_nodes' in c]
    old_targets = {c['target'] for c in graphs}
    old_nodes = {n for c in graphs for n in list(c['name_nodes'].values())+[n for p in c['paths'] for n in p['nodes']]}
    targets = rng.sample([f'T{x}' for x in range(10000,99999) if f'T{x}' not in old_targets],48)
    nodes = iter(rng.sample([f'R{x}' for x in range(10000,99999) if f'R{x}' not in old_nodes],624))
    cases = []
    for split,offset in [('development',0),('confirmation',24)]:
        positions,record_positions = list(range(4))*6,list(range(4))*6
        rng.shuffle(positions)
        rng.shuffle(record_positions)
        for i in range(24):
            group = bundles[offset+i]
            names = list(group)
            rng.shuffle(names)
            gold = names[positions[i]]
            others = [n for n in names if n!=gold]
            order = rng.sample(others,3)
            order.insert(record_positions[i],gold)
            ids = [next(nodes) for _ in range(13)]
            endpoints = [gold]+rng.sample(others,2)
            candidates = [copy.deepcopy(people[n]) for n in names]
            c = dict(case_id=f'v365-{split}-{i+1:02}',split=split,target=targets[offset+i],gold=gold,
                     gold_position=positions[i]+1,candidates=candidates,name_nodes=dict(zip(names,ids[:4])),
                     name_record_order=order,paths=[dict(endpoint=n,nodes=ids[4+j*3:7+j*3]) for j,n in enumerate(endpoints)],
                     path_order=rng.sample([0,1,2],3),candidate_source_case='Same21 audited real people as v3.4.4; reused identities explicitly logged',
                     entity_bundle_previously_used=group in seen,
                     candidate_list_sha256=sha(json.dumps(candidates,sort_keys=True,ensure_ascii=False)))
            cases.append(c)
    assert validate_sources(cases)==192
    for c in cases:
        for rotation in (1,2):
            audit_prompt(c,4,2,no_list(c,4,2,rotation))
        assert c['target'] not in old_targets
    return cases[:24],cases[24:],dict(seed=365,people_reused=sorted(people),fresh_bundles=sum(not c['entity_bundle_previously_used'] for c in cases),
          reused_bundles=[c['case_id'] for c in cases if c['entity_bundle_previously_used']],historical_targets_excluded=len(old_targets),historical_nodes_excluded=len(old_nodes))


def render(c,rotation=1):
    prompt = no_list(c,4,2,rotation)
    audit_prompt(c,4,2,prompt)
    endpoints = {p['name']:p['target'] for p in c['candidates']}
    assert len(endpoints)==4 and len(set(endpoints.values()))==4
    assert all(p['target'] not in prompt and all(a not in prompt for a in p['target_aliases']) for p in c['candidates'])
    assert 'Candidate names:\n' not in prompt and 'UNKNOWN' not in prompt
    return dict(call_id=c['case_id']+('/N' if rotation==1 else '/R2'),case_id=c['case_id'],split=c['split'],rotation=rotation,
                gold=c['gold'],names=[p['name'] for p in c['candidates']],downstream_endpoints=endpoints,
                prompt=prompt,text_sha256=sha(prompt),graph_audit=audit_prompt(c,4,2,prompt))


def historical_audit(tok):
    dev,confirm,_ = historical_cases()
    assert dev==read('results/calibration_v3_4_4/development_cases.json')
    assert confirm==read('results/calibration_v3_4_4/confirmation_cases.json')
    plans = [json.loads(s) for s in Path('results/calibration_v3_4_4/prompt_plan.jsonl').read_text(encoding='utf-8').splitlines()]
    checks = []
    for c in dev:
        p = next(p for p in plans if p['case_id']==c['case_id'] and p['difficulty']=='HARD' and p['interface']=='N')
        prompt = no_list(c,4,2)
        chat = tok.apply_chat_template([dict(role='user',content=prompt)],tokenize=False,add_generation_prompt=True,enable_thinking=False)
        assert prompt==p['prompt'] and chat==p['rendered_prompt']
        assert audit_prompt(c,4,2,prompt)==p['graph_audit']
        checks.append(dict(case_id=c['case_id'],text_sha256=sha(prompt),rendered_sha256=sha(chat),exact_match=True))
    rows = [json.loads(s) for s in Path('results/calibration_v3_4_4/no_list_free.jsonl').read_text(encoding='utf-8').splitlines()]
    selected = [r for r in rows if r['cohort']=='development' and r['difficulty']=='HARD']
    assert len(selected)==24
    wrong = 0
    for r in selected:
        c = next(c for c in dev if c['case_id']==r['case_id'])
        p = parse_natural(r['raw_text'],[p['name'] for p in c['candidates']],r['truncated'],{})
        assert p['strict_valid']
        wrong += p['identity']!=c['gold']
    assert wrong==5
    assert read('results/calibration_v3_4_4/decoding_freeze.json')['NR_max_new_tokens']==96
    return dict(recovered=True,fixtures=checks,anchor=dict(valid=24,wrong=5,denominator=24),model_calls=0,
                differences='Fresh case/graph IDs and bundles, cohort sizes/seeds, new yield gates and only F calls. No prompt/parser/chat-render contract changes; scoring omitted.')
