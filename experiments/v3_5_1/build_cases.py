"""Seeded pair sampling uses source mappings, never prior model outputs."""
import difflib
import itertools
import json
import random
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from src.common import digest
from src.experiment_v3 import write_json
from src.calibration_v3_4_1 import REVISION
from src.calibration_choice import CalibrationAdapter
from .render_prompts import render, audit_pair, sha, CONDITIONS
from .validate_cases import validate, normalize

OUT = Path('results/v3_5_1')
BOUNDARY = 'Same fact, same semantic relevance, different task-role heading; perceived authority not independently isolated.'
POLICY = dict(seed=351, generation_seed=42, C0_min=10, S0_min=8,
    framing_forward_min=4, framing_reverse_max=1, main_calls=72,
    auxiliary_budget='4 independent format calls + 1 exact repeat + 9 direct lookups + 2 synthetic state controls =16. Only if smoke truncates: four more format calls at192, total20.',
    cap_rule='Prefer96. Run four independent city-format smoke tasks. If any truncated, repeat all four at192 and freeze192; otherwise96. No main-case cap tuning.',
    capability_rule='All seven unique source-person direct lookups, two fictional context lookups, and two fictional state controls must pass before main; exact smoke replay required.',
    framing_heuristic='At least4 background non-C to current C, reverse at most1; also display strict Cp-to-C switches separately. Invalid/unknown switches cannot support the heuristic.',
    high_invalid_rule='More than2 INVALID outputs in either primary framing arm blocks framing interpretation.',
    majority_rule='Mainly gold or donor means at least8/12 in each primary arm.',
    valid_parse_denominator='Exact C/Cp aliases plus well-formed single OTHER_ANSWER; UNKNOWN and INVALID excluded. All-case denominators always12.',
    uncertainty='For at least4 strict C/Cp discordances report exact95% Clopper-Pearson interval for forward share, plus two-sided sign/binomial p descriptively; fewer: counts only.',
    order='Seed351 shuffle all72 condition/case calls before inference; downstream record order balanced6 gold-first/6 donor-first and fixed per case.',
    followup='Only STOP_INVALID, STOP_UNINFORMATIVE, PILOT_SIGNAL_CONFIRM_SEPARATELY; no additional labels, order perturbations, confirmation, or v3.5.2 automatically.',
    normalization='Unicode NFC, casefold, outer whitespace, one final period; city-only frozen aliases; no extraction from explanatory text.',
    limitations='Distinct pairs and anonymous targets; seven people reused, so not twelve disjoint entity populations. Provided context is available; synthetic lookups show capability, not proof every main city retrieval used context.')


def load(name):
    return json.loads((OUT/name).read_text(encoding='utf-8'))


def make_cases():
    source_files=[Path('results/calibration_v3_4_1')/n for n in ('dev_cases.json','heldout_cases.json')]
    people={p['name']:p for file in source_files for c in json.loads(file.read_text(encoding='utf-8')) for p in c['candidates'] if p['relation']=='place of birth'}
    rng=random.Random(351)
    pairs=[pair for pair in itertools.combinations(sorted(people),2) if normalize(people[pair[0]]['target'])!=normalize(people[pair[1]]['target'])]
    chosen=rng.sample(pairs,12)
    targets=rng.sample(range(351000,399999),12)
    orders=[['B','Bp']]*6+[['Bp','B']]*6
    rng.shuffle(orders)
    cases=[]
    for i,(pair,target,order) in enumerate(zip(chosen,targets,orders),1):
        names=list(pair);rng.shuffle(names)
        a,b=(people[n] for n in names)
        c=dict(case_id=f'v351-{i:02}',A=f'T{target}',B=a['name'],Bp=b['name'],C=a['target'],Cp=b['target'],
            C_aliases=sorted({a['target'],*(s for s in a['target_aliases'] if ',' not in s)}),
            Cp_aliases=sorted({b['target'],*(s for s in b['target_aliases'] if ',' not in s)}),
            r1='credited director',r2='place of birth',record_order=order,sources=dict(B=a,Bp=b),seed=351)
        c['gold_graph']=[[c['A'],c['r1'],c['B']],[c['B'],c['r2'],c['C']],[c['Bp'],c['r2'],c['Cp']]]
        cases.append(c)
    return cases,people,source_files


def prepare():
    assert not OUT.exists(),'Never overwrite a frozen experiment'
    cases,people,source_files=make_cases()
    checks=validate(cases)
    # Required reference fixture is verified against the same frozen biographical evidence.
    assert people['Helmut Käutner']['target']=='Düsseldorf' and people['Rolf Schübel']['target']=='Stuttgart'
    fixture=dict(case_id='illustrative-only',A='T64218',B='Helmut Käutner',Bp='Rolf Schübel',C='Düsseldorf',Cp='Stuttgart',record_order=['B','Bp'])
    fixture_rows=audit_pair(fixture)
    from transformers import AutoTokenizer
    adapter=object.__new__(CalibrationAdapter)
    adapter.tokenizer=AutoTokenizer.from_pretrained('Qwen/Qwen3-4B-Instruct-2507',cache_dir='.cache/huggingface',revision=REVISION,local_files_only=True)
    plans=[render(c,k) for c in cases for k in CONDITIONS]
    for p in plans:
        p['rendered_prompt']=adapter.render(p['prompt'])
        p['rendered_sha256']=sha(p['rendered_prompt'])
        p['input_tokens']=len(adapter.tokenizer.encode(p['rendered_prompt'],add_special_tokens=False))
        p['fact_token_ids']=adapter.tokenizer.encode(p['fact'],add_special_tokens=False) if p['fact'] else []
    for c in cases:
        a,b=[next(p for p in plans if p['case_id']==c['case_id'] and p['condition']==k) for k in ('G-CURRENT','G-BACKGROUND')]
        assert a['fact_token_ids']==b['fact_token_ids']
    random.Random(351).shuffle(plans)
    for i,p in enumerate(plans):p['execution_index']=i+1
    smoke=[dict(check_id=f'format-{i}',prompt=f"Reference note: {person}'s place of birth is {city}.\nQuestion: What is {person}'s place of birth?\nOutput only the city name.",expected=city) for i,(person,city) in enumerate(zip(['Ava Mire','Bo Vell','Cia Norr','Dax Penn'],['Luma','Vela','Naro','Sora']),1)]
    capability=[dict(check_id=f'lookup-{i}',kind='real_direct_lookup',prompt=f"Reference note (source: project record set): {n}'s place of birth is {p['target']}.\nQuestion: What is {n}'s place of birth?\nOutput only the city name.",expected=p['target'],aliases=sorted({p['target'],*(a for a in p['target_aliases'] if ',' not in a)})) for i,(n,p) in enumerate(sorted(people.items()),1)]
    capability += [dict(check_id=f'context-{i}',kind='fictional_context_lookup',prompt=f"For this fictional record set, {person}'s place of birth is {city}.\nQuestion: What is {person}'s place of birth?\nOutput only the city name.",expected=city,aliases=[city]) for i,(person,city) in enumerate([('Ena Dorr','Toma'),('Fay Voss','Rina')],1)]
    synthetic=dict(case_id='aux-state',A='AUX351',B='Gio Marr',Bp='Hia Tern',C='Pela',Cp='Dora',record_order=['Bp','B'])
    for condition,expected in [('S0','Dora'),('C0','Pela')]:
        capability.append(dict(check_id='state-'+condition,kind='fictional_state_control',prompt=render(synthetic,condition)['prompt'],expected=expected,aliases=[expected]))
    prior={p.as_posix():digest(p) for p in Path('results').rglob('*') if p.is_file()}
    OUT.mkdir(parents=True)
    write_json(OUT/'cases.json',cases)
    write_json(OUT/'prompt_plan.json',plans)
    write_json(OUT/'auxiliary_plan.json',dict(smoke=smoke,capability=capability))
    write_json(OUT/'example_fixture.json',dict(prompts=fixture_rows,literal_cities_source_verified=True,queried=False))
    write_json(OUT/'mechanical_checks.json',checks)
    audit='# Pre-run design audit\n\n'+BOUNDARY+'\n\n| Design intention | Feature | Observable check | Failure meaning |\n|---|---|---|---|\n'
    intentions=[('Study propagation not initiation','Explicit external state','S0 PR and Cp trace','No reliable propagation assay'),('Verify gold path','C0 plus independent direct lookups','C0>=10/12 and all auxiliary checks','Capability not established'),('Isolate task-role framing','Same fact; heading-only change','Literal equality after heading replacement','Authority/freshness not isolated'),('Separate correctness from heading','Two gold arms plus W-CURRENT','PR and OR by arm','Content vs heading distinction lost'),('Reverse influence','C0 vs C-WCURRENT','Paired induced-wrong flips','No symmetry assumption'),('Avoid option primacy','Unconstrained city output','No enumerated answer list or trie','Prior artifact returns'),('Control record order','Fixed two mapping statements','Single record-block hash per case','Evidence-order confound'),('Interpretable categories','Frozen exact city parser','Raw and parsed output agreement','Mislabelled propagation'),('Preserve inference limits','12 unique pairs; seed351','72 complete calls; no replacements','Inflated inference; people reused'),('Stop at boundary','Frozen thresholds and budget','Machine-readable final recommendation','Adaptive search')]
    audit+='\n'.join('| '+' | '.join(row)+' |' for row in intentions)+'\n'
    audit+=f'\nActual prompt plan SHA256: `{digest(OUT/"prompt_plan.json")}`. All 72 graph/prompt conditions validated. Dossier source tags identical; timestamp absent in both arms. Evidence occupies the same block, with the same whitespace and surrounding text. Any heading-token-length difference is part of the label intervention, not an independently controlled freshness/trust manipulation.\n'
    for name in ('design_audit.pre_inference.md','design_audit.md'):(OUT/name).write_text(audit,encoding='utf-8',newline='\n')
    prereg='# v3.5.1 preregistration\n\nEstimand: **response difference under current-task vs background dossier label with identical relevant fact.**\n\n'+BOUNDARY+'\n\nExternally injected Bp, not spontaneous first-hop hallucination. Twelve anonymous synthetic films and twelve distinct unordered person pairs; people recur. All second-hop outcomes use city granularity. Source-backed city aliases with country/province suffixes are excluded from accepted output aliases. No v3.4.4 model outputs used in sampling.\n\n```json\n'+json.dumps(POLICY,indent=2)+'\n```\n'
    (OUT/'pre_registration.md').write_text(prereg,encoding='utf-8',newline='\n')
    diffs='# Exact framing diffs\n\n'+BOUNDARY+'\n'
    for c in cases:
        pair=audit_pair(c)
        diffs+=f'\n## {c["case_id"]}\n\nRecord block SHA256 `{pair["G-CURRENT"]["record_order_sha256"]}`; gold evidence SHA256 `{sha(pair["G-CURRENT"]["fact"])}`.\n\n```diff\n'
        diffs+='\n'.join(difflib.unified_diff(pair['G-BACKGROUND']['prompt'].splitlines(),pair['G-CURRENT']['prompt'].splitlines(),fromfile='G-BACKGROUND',tofile='G-CURRENT',n=2,lineterm=''))+'\n```\n'
    (OUT/'prompt_diff_audit.md').write_text(diffs,encoding='utf-8',newline='\n')
    (OUT/'chat_template.txt').write_text(adapter.tokenizer.chat_template,encoding='utf-8',newline='\n')
    (OUT/'spec.md').write_bytes(Path('C:/Users/kding/Downloads/v3_5_1_task_role_framing_spec_revised.md').read_bytes())
    frozen=list(Path('experiments/v3_5_1').glob('*.py'))+[Path('tests/test_v3_5_1.py')]+[p for p in OUT.iterdir() if p.name!='design_audit.md']
    write_json(OUT/'model_manifest.json',dict(created_utc=datetime.now(timezone.utc).isoformat(),git_commit=subprocess.check_output(['git','-c','safe.directory='+Path.cwd().as_posix(),'rev-parse','HEAD'],text=True).strip(),
        model='Qwen/Qwen3-4B-Instruct-2507',revision=REVISION,quantization='NF4 double quantization',compute_dtype='torch.bfloat16',policy=POLICY,
        source_files={p.as_posix():digest(p) for p in source_files},source_sha256=digest(Path('data/dev.json')),
        frozen={p.as_posix():digest(p) for p in frozen},prior_artifacts=prior))
    print('Frozen12 cases /72 main prompts /16 or20 predeclared auxiliary calls; no model inference yet.',flush=True)


def verify():
    m=load('model_manifest.json')
    for kind in ('source_files','frozen','prior_artifacts'):
        for name,h in m[kind].items():assert digest(Path(name))==h,name
    assert digest(Path('data/dev.json'))==m['source_sha256']


if __name__=='__main__':prepare()
