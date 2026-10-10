"""Pre-inference freeze of all possible bridges, two-row modules and schedules."""
import importlib.metadata
import json
import random
import subprocess
from datetime import datetime,timezone
from pathlib import Path
from transformers import AutoTokenizer
from experiments.v3_6_0.prepare import MODEL,digest
from src.calibration_v3_4_1 import REVISION
from experiments.inheritance import validate
from experiments.v3_6_5.design import historical_audit
from experiments.v3_6_5.prepare import review as previous_review
from scripts.validated_findings import load as ledger_load,validate_data,review_spec
from .design import read,make_cases,make_mappings,first_prompt,down_prompt,sha,route

OUT=Path('results/v3_6_6')
BASELINE='135968464958840259bdb6b4c6ced2951afe2e03'


def load(name):return read(OUT/name)


def text(name,value):(OUT/name).write_text(value,encoding='utf-8',newline='\n')


def write(name,value):text(name,json.dumps(value,ensure_ascii=False,indent=2)+'\n')


def jsonl(name,rows):text(name,''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))


def review(data,h):
    r,_=previous_review(data,h)
    changes={
      'F01':('AVOIDED','Fixed120 denominators, invalid/skipped/missing separated; never replace primary cases.'),
      'F04':('FROZEN_REUSE','Exact two-row Current state shell and cap16; all360 modules compared byte for byte.'),
      'F11':('INTENTIONALLY_RETESTED','New lossless person encoding and routed natural wrong states; previous actual pipeline tested correct states only.'),
      'F12':('INTENTIONALLY_RETESTED','Paired controls on current routed modules estimate RD; never count controls as natural errors.'),
      'F14':('AVOIDED','Historical upstream cap96/downstream16 unchanged; truncation never repaired or retried.'),
      'F16':('INTENTIONALLY_RETESTED','24 seeded independent diagnostics; no gating or error supplementation.'),
      'F18':('TARGETED','Prospective collection replaces frontier selection; prior failure remains unchanged.'),
      'F19':('INTENTIONALLY_RETESTED','No yield gate; report all trajectories with actual W and information labels, never add cases to reach20.'),
      'F20':('TARGETED','Measure natural wrong identities routed into synthetic opaque modules, without claiming natural/injected equivalence.'),
      'F26':('FROZEN_REUSE','Use unchanged historical name parser upstream and v3.6.3 outcome parser downstream; no parser mixing.'),
      'F27':('FROZEN_REUSE','Same model/runtime, task-specific inherited cap96 and16; no new stack experiment.'),
      'C01':('FROZEN_REUSE','Exact validated two-row Current state mapping shell.'),
      'C03':('FROZEN_REUSE','Same STATE/OUTCOME families; fresh IDs, matched role token counts, eight distinct suffixes within case.'),
      'C04':('FROZEN_REUSE','Unchanged inherited downstream outcome parser; upstream names use distinct historical parser.'),
      'C05':('FROZEN_REUSE','Exact stack/seed/cache/template; downstream cap16 and historical HARD/N cap96 retained by task.'),
      'C06':('INTENTIONALLY_RETESTED','New deterministic person-state encoding and identity-dependent selection of pre-frozen two-row modules.')}
    known={x['id']:x for x in data['findings']+data['validated_components']}
    for x in r['rows']:
        rid=x['id']
        if rid in changes:x['treatment'],x['rationale']=changes[rid]
        x['modified']=rid=='C06';x.pop('modification',None)
        if x['modified']:x['modification']=dict(component=rid,prior_evidence=known[rid]['evidence_files'],reason=x['rationale'],
             prior_conclusion_no_longer_applies='Old actual-state pipeline used correct opaque states only, not natural wrong names or identity-dependent modules.',
             revalidation_gate='Static bijection/all-branch routing and exact byte audits, complete120-case trajectory collection, terminal capability and information labels.')
    table='| Finding / Component | Ledger status | Treatment in this experiment | Rationale |\n|---|---|---|---|\n'
    table+='\n'.join('| '+' | '.join(x[k] for k in ('id','ledger_status','treatment','rationale'))+' |' for x in r['rows'])+'\n'
    return r,table


def inheritance():
    rows=[]
    for name,version,kind,prior,treatment in [
        ('HARD/N and name parser','v3.4.4/v3.6.5','FROZEN_REUSE','Historical24/24 valid5/24 wrong; recent3/24 wrong','Exact no_list D4B2 and parse_natural; zero-call fixtures'),
        ('Downstream shell/parser','v3.6.3.1','FROZEN_REUSE','D-A/D-B/paired40/40','Exact two-row VALIDATED renderer, cap16 and inherited parser'),
        ('Runtime and opaque lexical constraints','v3.6.3.1/v3.6.5','FROZEN_REUSE','Pinned stack and opaque family in validated interfaces','Same task caps, ID families, token matching, fresh suffix constraints'),
        ('120 fresh graphs','v3.6.5','INTENTIONALLY_RETESTED','No independently confirmed frontier','Prospective fixed cohort; no yield gate'),
        ('Identity bridge and natural routing','v3.6.3.1','INTENTIONALLY_RETESTED','Actual pipeline tested correct states only','Bijective encoding; three pre-frozen modules; every wrong branch retains its identity'),
        ('Paired controlled states','v3.6.3.1','INTENTIONALLY_RETESTED','External state switch validated','Current-cohort paired RD, no extra old calibration'),
        ('Record order diagnostic','v3.6.5','INTENTIONALLY_RETESTED','3/8 identity changes','24 independent fixed diagnostics, no gates'),
        ('Difficulty search and integrated task','v3.6.4/v3.6.3.1','NOT_RELEVANT','Separate questions','No such calls')]:
        modified=kind=='INTENTIONALLY_RETESTED'
        rows.append(dict(component=name,prior_version=version,classification=kind,prior_result=prior,treatment=treatment,
             validation='Frozen source hashes, byte comparisons, new-risk tests and complete namespace logs',modified=modified,
             reason=treatment if modified else '',prior_conclusion_no_longer_applies='Prior successful component evidence does not establish the new cohort/bridge/natural-wrong response' if modified else ''))
    return rows


RESOLUTIONS='''## Execution resolutions frozen before inference

This effective spec follows every numeric threshold, seed, parser, stage order and interval in the supplied spec. No new model calls before this freeze. Historical source audit was saved in docs/v3_6_6_preimplementation_audit.json and all four ledger documents updated before constructing the120-case cohort.
Person IDs are SHA256 prefixes of canonical name plus frozen source-row ID; assert uniqueness and stable name mapping. Four names map to four globally fresh STATE IDs and four OUTCOME IDs. Within each case all eight suffixes differ; role token counts/lengths match. This inherits the v3.6.3.1 distinct-suffix rule, not the earlier v3.6.1 stricter character-disjoint constraint. No entity ID is shown downstream; legacy entity fields hold audit-only person IDs. Eight IDs per case are assigned in frozen candidate-array order using seed3665, never predicted-name order. Downstream order60/60 uses that same seeded RNG. All inventory and historical ID exclusions saved.
First-hop parser aliases remain empty. Route provenance additionally includes a hash of the full case identity table; mapping_hash is the hash of the selected prebuilt legacy module, and source raw SHA is retained. Every natural and controlled call matches one of720 frozen module-arm prompts. These are potential prompts, not720 model calls.120 primary plus24 diagnostic and720 module-arm prompts total864 static entries. Actual cap/namespace/call IDs are logged at dispatch. There are120 natural schedule slots, with invalid slots explicitly skipped, and240 controlled schedule slots. All lists are saved. Controlled shuffle seed3664 repeats deterministic shuffles until no adjacent same-case arms; attempts saved.
Classify only after raw persistence. Log CALL_STARTED durably before each generation and CALL_COMPLETED after raw persistence; an unresolved start blocks all reuse. Native process death remains a failed attempt; no automatic resume. Model/revision/version/template mismatch is runtime drift; static hash/bridge mismatch is structural. No early scientific stop.
Intervals use pure-Python inversion of the finite binomial CDF for Clopper-Pearson, avoiding an unavailable SciPy dependency; tests cover endpoint analytic formulas, central cases and paired zero-discordance nonzero widths. Wilson z=1.959963984540054. No alternate narrower interval. On partial data, final UCR is null and cascade bounds are shown; complete-case wrong propagation is explicitly separate. Complete trajectory coverage includes observed invalid first hops with protocol skips; legal forwarding coverage counts returned natural responses/V.
For the diversity part of minimum information, report all-W diversity and additionally the conservative subset with both natural downstream and controlled pair complete; use that jointly complete subset for the5-identities/10-bundles rule. This changes no call schedule or W denominator. Every proportion includes its count and denominator; interval-null reflects empty denominator or incompleteness. Full data retain P+O+T=W; technical missing remains separate.
Information labels, capabilities and technical/collection statuses are separate. Diagnostic has no PRESENTATION_SENSITIVE threshold. Names/real source endpoints audit identity only; actual downstream opaque outcomes are synthetic. Historical frontier failures are not overridden or upgraded.
'''


def verify():
    m=load('freeze_manifest.json')
    for group in ('frozen','prior_artifacts'):
        for p,h in m[group].items():assert digest(p)==h,p
    spec=(OUT/'spec.md').read_text(encoding='utf-8')
    validate(spec,load('validated_inheritance.json'))
    review_spec(load('prior_ledger_snapshot.json'),spec,load('prior_findings_review.json'),digest(OUT/'prior_ledger_snapshot.json'))


def prepare():
    assert not OUT.exists(),'Existing attempt: no overwrite'
    head=subprocess.check_output(['git','-c','safe.directory='+Path.cwd().as_posix(),'rev-parse','HEAD'],text=True).strip()
    assert head==BASELINE,'Changed baseline requires explicit difference review'
    data=ledger_load();validate_data(data);assert data['future_spec_protocol']['latest_incorporated_version']=='v3.6.5'
    assert read('docs/v3_6_6_preimplementation_audit.json')['baseline_matches']
    tok=AutoTokenizer.from_pretrained(MODEL,revision=REVISION,cache_dir='.cache/huggingface',local_files_only=True)
    history=historical_audit(tok)
    cases,fresh=make_cases();identity,modules,tokens=make_mappings(cases,tok)
    ids=[c['case_id'] for c in cases];schedule={}
    for name,seed in [('first_hop',3661),('natural_downstream',3663)]:
        schedule[name]=ids[:];random.Random(seed).shuffle(schedule[name])
    schedule['diagnostic_ids']=random.Random(3662).sample(ids,24)
    schedule['order_diagnostic']=schedule['diagnostic_ids'][:];random.Random(3667).shuffle(schedule['order_diagnostic'])
    controls=[dict(case_id=cid,arm=a) for cid in ids for a in ('G','A')];rng=random.Random(3664);attempts=0
    while True:
        rng.shuffle(controls);attempts+=1
        if all(a['case_id']!=b['case_id'] for a,b in zip(controls,controls[1:])):break
    schedule.update(controlled=controls,controlled_shuffle_attempts=attempts,seeds=dict(cases=366,first_hop=3661,diagnostic_selection=3662,natural=3663,controls=3664,mapping=3665,alternate=3666,diagnostic_order=3667))
    plans=[];cby={c['case_id']:c for c in cases}
    for cid in schedule['first_hop']:plans.append(first_prompt(cby[cid])|dict(kind='FIRST',plan_id=cid+'/FIRST'))
    for cid in schedule['order_diagnostic']:plans.append(first_prompt(cby[cid],True)|dict(kind='DIAGNOSTIC',plan_id=cid+'/DIAGNOSTIC'))
    for mid,module in modules.items():
        for arm in ('G','A'):plans.append(down_prompt(module,arm)|dict(kind='DOWN',plan_id=mid+'/'+arm))
    for p in plans:
        chat=tok.apply_chat_template([dict(role='user',content=p['prompt'])],tokenize=False,add_generation_prompt=True,enable_thinking=False)
        token_ids=tok.encode(chat,add_special_tokens=False)
        p.update(rendered_prompt=chat,rendered_sha256=sha(chat),input_token_ids=token_ids,tokenized_sha256=sha(json.dumps(token_ids)))
    routechecks=[]
    for c in cases:
        for name in identity[c['case_id']]['by_name']:
            raw=dict(raw_text=name,truncated=False,raw_sha256=sha(name));module,p,log=route(c,raw,identity,modules)
            assert p['supplied_state']==identity[c['case_id']]['by_name'][name]['state']
            assert log['parsed_identity']==name
            routechecks.append(log)
    versions={n:importlib.metadata.version(n) for n in ('torch','transformers','bitsandbytes','accelerate','numpy')}
    assert versions==read('results/v3_6_5/decoding_freeze.json')['versions']
    assert sha(tok.chat_template)==digest('results/v3_6_3_1/chat_template.txt')==digest('results/calibration_v3_4_4/chat_template.txt')
    original=Path('C:/Users/kding/Downloads/v3.6.6_prospective_natural_error_trajectory_collection_spec.md').read_text(encoding='utf-8-sig')
    r,table=review(data,digest('docs/validated_findings.json'));inherit=inheritance()
    spec='# Prior Findings Review\n\nReferences: docs/validated_findings.md and docs/validated_findings.json.\n\n'+table+'\n## Validated Inheritance\n\n'+json.dumps(inherit,ensure_ascii=False,indent=2)+'\n\n## New manipulation\n\nFixed prospective120-case natural trajectories with lossless encoding and matched controls.\n\n'+RESOLUTIONS+'\n## Supplied specification (full text)\n\n'+original
    reviewed=review_spec(data,spec,r,digest('docs/validated_findings.json'));assert validate(spec,inherit)
    OUT.mkdir()
    (OUT/'prior_ledger_snapshot.json').write_bytes(Path('docs/validated_findings.json').read_bytes())
    (OUT/'historical_raw_audit.json').write_bytes(Path('docs/v3_6_6_preimplementation_audit.json').read_bytes())
    for n,v in [('spec.md',spec),('spec.original.md',original),('pre_registration.md','# v3.6.6 pre-registration\n\n'+RESOLUTIONS+'\n'+original),('chat_template.txt',tok.chat_template)]:text(n,v)
    for n,v in [('cases.json',cases),('freshness_audit.json',fresh),('identity_state_map.json',identity),('downstream_modules.json',modules),('identifier_tokenization_audit.json',tokens),('call_schedule.json',schedule),('validated_inheritance.json',inherit),('prior_findings_review.json',r),('historical_interface_audit.json',history),('static_routing_audit.json',routechecks),('alias_registry.json',{})]:write(n,v)
    write('inheritance_audit.json',dict(passed=True,ledger_review=reviewed,legacy_validator=True,historical_fixtures=24,downstream_module_byte_pairs=360,all_person_routes=480,baseline_commit=head))
    jsonl('prompt_plan.jsonl',plans)
    write('decoding_freeze.json',dict(model=MODEL,revision=REVISION,versions=versions,first_hop_cap=96,downstream_cap=16,seed=42,use_cache=False,do_sample=False,enable_thinking=False,compute_dtype='torch.bfloat16',quantization='NF4 double quantization',offload=False,chat_template_sha256=sha(tok.chat_template)))
    audit='# Pre-inference structural audit\n\nS1–S5 passed: historical raw recount and both validators;24 HARD/N fixtures;120 fresh graphs/targets and480 source mappings;480 bijective routes,360 exact downstream module-arm pairs;960 fresh IDs and864 tokenized prompts. S6 runtime checked at model load; S7 tested durable dispatch/one-main-call state machine. Maximum504 calls; no yield gate.\n\n'+RESOLUTIONS
    text('design_audit.pre_inference.md',audit);text('design_audit.md',audit)
    code=list(Path('src').glob('*.py'))+list(Path('experiments').rglob('*.py'))+[Path('tests/test_v3_6_6.py'),Path('scripts/validated_findings.py'),Path('data/dev.json')]
    frozen={p.as_posix():digest(p) for p in code+list(OUT.iterdir()) if p.name!='design_audit.md'}
    prior={p.as_posix():digest(p) for p in Path('results').rglob('*') if p.is_file() and OUT not in p.parents}
    write('freeze_manifest.json',dict(created_utc=datetime.now(timezone.utc).isoformat(),baseline_commit=head,frozen=frozen,prior_artifacts=prior,maximum_calls=504,planned_N=120))
    verify();print('Frozen120 cases,360 modules,864 potential prompts. Maximum504 calls; no yield gate.',flush=True)


if __name__=='__main__':prepare()
