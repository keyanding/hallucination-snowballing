"""Preregistered v3.4.4 cases, prompt interventions and validity policy."""
import copy
import difflib
import itertools
import json
import random
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from .common import digest, norm
from .experiment_v3 import write_json
from .experiment_v3_3 import sha
from .graph_v3_4_2 import render, audit_prompt, validate_sources, name_records
from .calibration_v3_4_3 import rotate_prompt, split_prompt
from .analysis_v3_4_3 import CASE_IDS, CONDITIONS
from .calibration_v3_4_1 import REVISION
from .interface_v3_4_4 import InterfaceAdapter

OUT = Path('results/calibration_v3_4_4')
POLICY = dict(seed=344, generation_seed=42, interfaces=['L', 'N', 'R'],
    strict_coverage_min=.90, record_three_of_four_min=.75, record_four_of_four_min=.50,
    earliest_record_flag=.40, agreement_min=.85, aliases={},
    natural_parser='TRUNCATED first; exact canonical/approved alias; multiple mentions AMBIGUOUS; conservative name-shaped unknown OUT_OF_SET; rest NONCOMPLIANT. Supplementary extraction never changes primary.',
    L_aggregate='Unique modal C identity; ties missing. Three-of-four wrong is not robust wrong.',
    R_aggregate='All four strictly valid and at least three agree, otherwise UNSTABLE_OR_UNRESOLVED.',
    route_order=['N', 'R', 'L'], difficulty_tiebreak=['EASY', 'MID', 'HARD'],
    selection='First route with a passing difficulty; easiest passing difficulty. Never maximize wrong yield. L fallback requires C validity, at least 75% identity-stable cells and first fraction below 40%; admits forced-choice selection only.',
    record_flag_rule='Flag >=40% earliest among valid R rejects N/R gate; no discretionary override. Report identity-matched scores and per-case effects as investigation.',
    N_gate='N coverage >=90%; R 3/4 >=75%, 4/4 >=50%; no record flag; N versus unique L mode agreement >=85% among strict N with non-tied L.',
    R_gate='R aggregate coverage >=90%; same record-stability thresholds and flag; N versus L agreement >=85%.',
    wrong_yield='At least one strict wrong N or wrong R aggregate required for observed traceable wrong yield; separate from interface usability. Zero yield never triggers retuning.',
    confirmation='One chosen difficulty. L4+N1 for all 16; add R4 if selected N or R. No confirmation if no policy. Apply same route gate; no fallback or retuning after confirmation.',
    cap_smoke='Four independent format tasks at 96. If any truncated, repeat all four at 192. Choose 192 only in that case. No experimental case enters smoke. L always 96.',
    duplicates='N and R1 are identical prompts but are independently evaluated and retained, as budgeted.',
    budget=dict(development_renderings=648, old_diagnostic_renderings=90,
                development_channel_evaluations=1584, old_channel_evaluations=180,
                confirmation_L_renderings=80, confirmation_NR_renderings=144),
    score='EOS excluded; raw sum and mean/token both retained. Mean/token is not a probability; no normalized choice probabilities claimed.',
    bootstrap='2000 seeded case-resampling replicates; percentile 95% intervals; rotations/depths never independent units.',
    hypotheses=dict(H1='New L identity changes plus positive mean identity-matched first-position score shift; otherwise unsupported.',
                    H2='R identity changes among strict outputs demonstrate residual record-order effect; no such changes fails to support effect.',
                    H3='Paired HARD minus EASY L sensitivity and first-position rate positive; nonpositive results fail directional hypothesis; mixed cases limit consistency.',
                    H4='Report both stable-wrong and changing sets separately; zero stable-wrong does not establish such subtype.'))


def load(name):
    return json.loads((OUT / name).read_text(encoding='utf-8'))


def jsonl(path, rows):
    path.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows), encoding='utf-8', newline='\n')


def no_list(case, depth, branches, rotation=1):
    original = render(case, depth, branches)
    prefix, _, suffix = split_prompt(original)
    text = prefix.removesuffix('\n\nCandidate names:\n') + suffix
    text = text.replace('Which candidate is the credited director', 'Who is the credited director')
    text = text.replace('Answer with only one candidate name.', "Output only the person's name.")
    records = name_records(case)
    k = rotation - 1
    return text.replace('\n'.join(records), '\n'.join(records[k:] + records[:k]))


def make_cases():
    rng = random.Random(344)
    old = []
    for name in ('dev_cases.json', 'heldout_cases.json'):
        old += json.loads(Path('results/calibration_v3_4_1', name).read_text(encoding='utf-8'))
    people = {p['name']: p for c in old for p in c['candidates']}
    seen = {tuple(sorted(p['name'] for p in c['candidates'])) for c in old}
    bundles = []
    for relation in sorted({p['relation'] for p in people.values()}):
        for group in itertools.combinations(sorted(n for n, p in people.items() if p['relation'] == relation), 4):
            alias_sets = [{norm(people[n]['target']), *(norm(a) for a in people[n]['target_aliases'])} for n in group]
            if group not in seen and all(not a.intersection(b) for a, b in itertools.combinations(alias_sets, 2)):
                bundles.append(group)
    rng.shuffle(bundles)
    assert len(bundles) >= 40
    previous = sum([json.loads(Path('results/calibration_v3_4_2', n).read_text(encoding='utf-8')) for n in ('dev_cases.json', 'heldout_cases.json')], [])
    used_targets = {c['target'] for c in previous}
    used_nodes = {n for c in previous for n in list(c['name_nodes'].values()) + [n for p in c['paths'] for n in p['nodes']]}
    targets = rng.sample([f'T{x}' for x in range(10000, 99999) if f'T{x}' not in used_targets], 40)
    nodes = iter(rng.sample([f'R{x}' for x in range(10000, 99999) if f'R{x}' not in used_nodes], 520))
    cases = []
    for split, count, offset in [('development', 24, 0), ('confirmation', 16, 24)]:
        positions = list(range(4)) * (count // 4)
        record_positions = list(range(4)) * (count // 4)
        rng.shuffle(positions)
        rng.shuffle(record_positions)
        for i in range(count):
            names = list(bundles[offset + i])
            rng.shuffle(names)
            gold = names[positions[i]]
            others = [n for n in names if n != gold]
            record_order = rng.sample(others, 3)
            record_order.insert(record_positions[i], gold)
            ids = [next(nodes) for _ in range(13)]
            endpoints = [gold] + rng.sample(others, 2)
            candidates = [copy.deepcopy(people[n]) for n in names]
            cases.append(dict(case_id=f'v344-{split}-{i+1:02}', split=split, target=targets[offset+i],
                gold=gold, gold_position=positions[i]+1, candidates=candidates,
                name_nodes=dict(zip(names, ids[:4])), name_record_order=record_order,
                paths=[dict(endpoint=n, nodes=ids[4+j*3:7+j*3]) for j, n in enumerate(endpoints)],
                path_order=rng.sample([0, 1, 2], 3), candidate_source_case='recombined audited v3.4.1 people; all identities reused',
                entity_bundle_previously_used=False, candidate_list_sha256=sha(json.dumps(candidates, sort_keys=True, ensure_ascii=False))))
    return cases[:24], cases[24:], previous


def plans_for(cases, cohort):
    plans = []
    for c in cases:
        for difficulty, (d, b) in CONDITIONS.items():
            baseline = render(c, d, b)
            canonical = no_list(c, d, b)
            for interface in (['N', 'R'] if cohort == 'old' else ['L', 'N', 'R']):
                for rotation in range(1, 2 if interface == 'N' else 5):
                    prompt, names = rotate_prompt(baseline, rotation) if interface == 'L' else (no_list(c, d, b, rotation), [p['name'] for p in c['candidates']])
                    record_names = c['name_record_order']
                    if interface == 'R':
                        record_names = record_names[rotation-1:] + record_names[:rotation-1]
                        assert prompt.split('\n\nGraph-link records:\n')[1] == canonical.split('\n\nGraph-link records:\n')[1]
                        assert sorted(x for x in prompt.splitlines() if x.startswith('Record ') and ' names ' in x) == sorted(name_records(c))
                    if interface == 'L':
                        assert split_prompt(prompt)[0::2] == split_prompt(baseline)[0::2]
                    graph = audit_prompt(c, d, b, prompt)
                    for p in c['candidates']:
                        assert all(a not in prompt for a in {p['target'], *p['target_aliases']}), 'Downstream answer leaked'
                    plans.append(dict(plan_id=f'{cohort}/{c["case_id"]}/{difficulty}/{interface}{rotation}',
                        cohort=cohort, case_id=c['case_id'], difficulty=difficulty, depth=d, branches=b,
                        interface=interface, rotation=rotation, gold=c['gold'], candidate_order=names,
                        record_order=record_names, prompt=prompt, graph_audit=graph))
    return plans


def prepare():
    assert not OUT.exists(), 'Never overwrite a preregistration'
    dev, confirmation, previous = make_cases()
    old = [copy.deepcopy(next(c for c in previous if c['case_id'] == cid)) for cid in CASE_IDS]
    checked = validate_sources(dev + confirmation + old)
    plans = plans_for(dev, 'development') + plans_for(old, 'old') + plans_for(confirmation, 'confirmation')
    from transformers import AutoTokenizer
    adapter = object.__new__(InterfaceAdapter)
    adapter.tokenizer = AutoTokenizer.from_pretrained('Qwen/Qwen3-4B-Instruct-2507', cache_dir='.cache/huggingface', revision=REVISION, local_files_only=True)
    name_audit = {}
    for plan in plans:
        rendered = adapter.render(plan['prompt'])
        ids, seqs, trie = adapter.tokenize_choice(rendered, plan['candidate_order'])
        plan.update(rendered_prompt=rendered, prompt_sha256=sha(rendered), input_tokens=len(ids),
                    graph_tokens=len(adapter.tokenizer.encode(plan['prompt'].split('Graph-link records:\n')[1].split('\n\n')[0])),
                    candidate_token_ids=seqs, all_candidates_reachable=trie.audit())
        for name, seq in zip(plan['candidate_order'], seqs):
            name_audit[name] = dict(tokens=seq, count=len(seq), spelling=name)
    assert max(v['count'] for v in name_audit.values()) <= 12
    assert all(Counter(c['gold_position'] for c in cases) == {1:len(cases)//4, 2:len(cases)//4, 3:len(cases)//4, 4:len(cases)//4} for cases in (dev, confirmation))
    for cohort, cases in [('development', dev), ('confirmation', confirmation)]:
        for c in cases:
            for difficulty in CONDITIONS:
                for interface, field in [('L', 'candidate_order'), ('R', 'record_order')]:
                    group = [p for p in plans if (p['cohort'],p['case_id'],p['difficulty'],p['interface']) == (cohort,c['case_id'],difficulty,interface)]
                    assert all(sorted(p[field].index(n)+1 for p in group) == [1,2,3,4] for n in group[0][field])
    prior = {p.as_posix():digest(p) for p in Path('results').rglob('*') if p.is_file()}
    OUT.mkdir(parents=True)
    write_json(OUT/'development_cases.json', dev)
    write_json(OUT/'confirmation_cases.json', confirmation)
    write_json(OUT/'case_manifest.json', dict(old_diagnostic_cases=old, mapping_checks=checked,
        old_case_ids=list(CASE_IDS), fresh_target_ids=True, fresh_record_ids=True, fresh_bundles=40,
        people_reuse='All 21 source identities reused; 40 new bundles, synthetic targets and graphs. Not independent generalization to unseen people.',
        name_token_audit=name_audit, name_review='All canonical names preserved including accents; exact token roundtrip; <=12 tokens. Length remains a scoring confound; sum/mean rank disagreements reported.',
        source_sha256=digest(Path('data/dev.json'))))
    jsonl(OUT/'prompt_plan.jsonl', plans)
    (OUT/'chat_template.txt').write_text(adapter.tokenizer.chat_template, encoding='utf-8', newline='\n')
    diffs = '# Frozen prompt intervention audit\n\nAll planned cells, including unqueried confirmation difficulties, pass independent graph traversal, exact L prefix/suffix equality and R graph/query equality. N removes the separate list and changes only the two query/output phrases documented below. R1 and N are equal and are evaluated separately.\n'
    for cohort, cases in [('development',dev),('old',old),('confirmation',confirmation)]:
        for c in cases:
            for difficulty,(d,b) in CONDITIONS.items():
                base=render(c,d,b)
                diffs+=f'\n## {cohort}/{c["case_id"]}/{difficulty}\n\nL1 sha256 `{sha(base)}`; N sha256 `{sha(no_list(c,d,b))}`.\n'
                variants=[('N',no_list(c,d,b))]+[(f'L{i}',rotate_prompt(base,i)[0]) for i in range(2,5)]+[(f'R{i}',no_list(c,d,b,i)) for i in range(2,5)]
                for tag,text in variants:
                    original=no_list(c,d,b) if tag.startswith('R') else base
                    diffs+='\n```diff\n'+'\n'.join(difflib.unified_diff(original.splitlines(),text.splitlines(),fromfile='N' if tag.startswith('R') else 'L1',tofile=tag,n=0,lineterm=''))+'\n```\n'
    (OUT/'prompt_diff_audit.md').write_text(diffs,encoding='utf-8',newline='\n')
    intentions=[
      ('Separate option artifacts from semantics','L four option rotations; evidence fixed','Exact invariant prefix/suffix, graph solution','Changed C identity and matched position score shift','No changes/positive shift fails H1'),
      ('Measure natural no-list selection','N omits list; unconstrained F primary','Exact N vs L diff and no trie call','Strict coverage and wrong/all plus wrong/valid','Invalid output is not a correct answer'),
      ('Check residual record order','R rotates complete name-record lines','IDs move with names; graph/query identical','Record sensitivity and earliest-record selection','No identity changes fails H2; record flag rejects natural policy'),
      ('Separate format failures','Frozen exact parser and categories','Unit tests plus independent cap smoke','Five exclusive categories; extraction supplementary','Explanations/truncation cannot establish completed natural choice'),
      ('Counterbalance identity positions','Every name every L/R position; gold baseline balanced','All rotations audited; hashes frozen','Identity-matched first-position mean-score shift','Token length and identity remain cross-person confounds'),
      ('Test complexity interaction','Same cases EASY/MID/HARD','Graph tokens/depth/branches logged','Paired case trajectories and bootstrap','Mixed/nonpositive differences limit H3; length not isolated'),
      ('Prevent selection overfit','24 fresh development, 16 untouched confirmation','New targets/nodes/bundles and split hashes','Single policy+difficulty confirmation','No retuning; reused people limit external validity'),
      ('Keep wrong states traceable','Frozen real r2 evidence; synthetic first hop','184 source mappings checked against source coordinates','Stable wrong identities can map to r2 later','No downstream execution or propagation inference'),
      ('Interpret scores correctly','Same prompt F/C/S; sums and means; EOS excluded','Token boundaries/trie, frozen replay harness','Rank disagreement and gold margins','Mean scores are not choice probabilities'),
      ('Make failure informative','Full planned dataset even poor empirical results','Fixed gate, denominators and route rules','Usability and wrong yield separate','No target-error chasing or automatic v3.5')]
    audit='# v3.4.4 pre-inference design audit\n\n| Design intention | Implemented intervention | Pre-run validity check | Observable outcome | What would falsify it / limit interpretation |\n|---|---|---|---|---|\n'
    audit+='\n'.join('| '+' | '.join(row)+' |' for row in intentions)+'\n\nActual prompt plan SHA256: `'+digest(OUT/'prompt_plan.jsonl')+'`; exact per-cell prompt diffs/hashes: `prompt_diff_audit.md` (SHA256 `'+digest(OUT/'prompt_diff_audit.md')+'`). All 1170 plans validated before inference.\n\n## Frozen policy and falsifiable hypotheses\n\n```json\n'+json.dumps(POLICY,indent=2)+'\n```\n'
    for filename in ('design_audit.md','design_audit.pre_inference.md'):
        (OUT/filename).write_text(audit,encoding='utf-8',newline='\n')
    (OUT/'spec.md').write_bytes(Path('C:/Users/kding/Downloads/experiment_v3_4_4_codex_spec.md').read_bytes())
    frozen=list(Path('src').rglob('*.py'))+list(Path('tests').glob('*v3_4_4*'))+list(OUT.iterdir())
    write_json(OUT/'manifest.json',dict(created_utc=datetime.now(timezone.utc).isoformat(),
        git_commit=subprocess.check_output(['git','-c','safe.directory='+Path.cwd().as_posix(),'rev-parse','HEAD'],text=True).strip(), model='Qwen/Qwen3-4B-Instruct-2507',revision=REVISION,
        quantization='NF4 double quantization',compute_dtype='torch.bfloat16',policy=POLICY,
        frozen={p.as_posix():digest(p) for p in frozen},prior_artifacts=prior,
        source_sha256=digest(Path('data/dev.json')),planned_development=648,planned_old=90,
        confirmation_all_difficulties_frozen_but_not_queried=432,planned_main_channel_evaluations_before_confirmation=1764))
    print(f'Frozen {len(plans)} renderings (including 432 conditional confirmation plans); {checked} audited mappings.',flush=True)


def verify_frozen():
    m=load('manifest.json')
    for kind in ('frozen','prior_artifacts'):
        for name, expected in m[kind].items():
            assert digest(Path(name)) == expected, f'Frozen bytes changed: {name}'
    assert digest(Path('data/dev.json')) == m['source_sha256']


if __name__ == '__main__':
    prepare()
