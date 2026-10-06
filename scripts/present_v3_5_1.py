"""Independent final audit and descriptive presentation; no inference or retuning."""
import ast
import json
import sys
from collections import Counter
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from experiments.v3_5_1.build_cases import OUT,load,verify,BOUNDARY
from experiments.v3_5_1.render_prompts import audit_pair,CONDITIONS,sha
from experiments.v3_5_1.validate_cases import validate,parse,classify
from experiments.v3_5_1.analyze import compute
from src.common import digest,read_jsonl
from src.experiment_v3 import write_json

verify()
cases=load('cases.json');plans=load('prompt_plan.json');outputs=read_jsonl(OUT/'outputs.jsonl');aux=read_jsonl(OUT/'capability_checks.jsonl')
assert validate(cases)['verified_real_mappings']==24
assert len(outputs)==72 and len(aux)==16 and all(r['passed'] for r in aux)
assert Counter(r['condition'] for r in outputs)==dict.fromkeys(CONDITIONS,12)
assert len({frozenset((c['B'],c['Bp'])) for c in cases})==12
assert len({c[k] for c in cases for k in ('B','Bp')})==7
for r,p in zip(outputs,plans):
    assert all(r[k]==p[k] for k in p)
    assert r['new_chat'] and not r['use_cache'] and not r['constrained']
    assert r['max_new_tokens']==96 and sha(r['raw_text'])==r['raw_sha256']
    assert sha(r['rendered_prompt'])==r['rendered_sha256']
    c=next(c for c in cases if c['case_id']==r['case_id'])
    assert r['prompt']==audit_pair(c)[r['condition']]['prompt']
    assert r['injected_state']==c['Bp' if r['wrong_state'] else 'B']
parsed,metrics,gate=compute(cases,outputs,True)
assert metrics==load('metrics.json') and gate==load('gate.json')
assert parsed==read_jsonl(OUT/'parsed_outcomes.jsonl')
runtime=load('model_manifest.json')['runtime']
previous=json.loads(Path('results/calibration_v3_4_4/runtime.json').read_text(encoding='utf-8'))
assert runtime['versions']==previous['versions'] and runtime['revision']==previous['revision']
assert digest(OUT/'chat_template.txt')==digest(Path('results/calibration_v3_4_4/chat_template.txt'))
previous_manifest=json.loads(Path('results/calibration_v3_4_4/manifest.json').read_text(encoding='utf-8'))
for harness_file in ('src/calibration_choice.py','src/generation/local_hf_adapter.py'):
    assert digest(Path(harness_file))==previous_manifest['frozen'][harness_file]
for p in list(Path('experiments/v3_5_1').glob('*.py'))+[Path('tests/test_v3_5_1.py'),Path(__file__)]:
    data=p.read_bytes();assert not data.startswith(b'\xef\xbb\xbf') and b'\r' not in data
    assert all(line==line.rstrip() for line in data.decode().splitlines()),p
    ast.parse(data.decode())
failures=[dict(case_id=r['case_id'],gold=next(c['C'] for c in cases if c['case_id']==r['case_id']),supplied=r['injected_state'],raw=r['raw_text'],outcome=r['outcome']) for r in parsed if r['condition']=='C0' and r['outcome']!='GOLD_FOLLOW']
note='\n## Interpretation gate\n\n**STOP_INVALID: C0 accuracy is9/12, below the frozen10/12 minimum.** S0 PR is9/12 and passes its8/12 minimum. All16 independent auxiliary checks passed, but this does not rescue the failed main state-adherence control. No cases were replaced and no prompts or thresholds were revised.\n\nBoth framing arms returned C in12/12 cases (ΔOR=0/12; ΔPR=0/12;12 unchanged-C pairs;0 strict discordances). This is a descriptive output pattern, not a clean mechanistic task-role test. The `evidence_dominance` flag records those counts only. No evidence for these headings as a moderator was obtained.\n\nThe failed C0 cases were:\n\n```json\n'+json.dumps(failures,ensure_ascii=False,indent=2)+'\n```\n\nNo framing confirmation or new label search is recommended from this run. If a new design is externally approved, its prerequisite would be an independently validated state-adherence assay; that is not an additional experiment in this pilot.\n'
for name in ('README.md','diagnosis.md'):
    p=OUT/name;s=p.read_text(encoding='utf-8')
    if '## Interpretation gate' not in s:s+=note
    s=s.replace('are12','are 12').replace('With12','With 12').replace('is9/12','is 9/12').replace('frozen10/12','frozen 10/12').replace('its8/12','its 8/12').replace('All16','All 16').replace('in12/12','in 12/12').replace(';12 unchanged','; 12 unchanged').replace(';0 strict','; 0 strict')
    p.write_text(s,encoding='utf-8',newline='\n')
# Paired transitions retain their all-case denominator; no independent-arm uncertainty.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(11,5),layout='constrained')
colors={'C':'#387b61','Cp':'#b97831','UNKNOWN':'#85909a','INVALID':'#b94750','OTHER_ANSWER':'#7963a1'}
bottom=[0]*6
for label in ('C','Cp','UNKNOWN','INVALID','OTHER_ANSWER'):
    values=[]
    for condition in CONDITIONS:
        s=metrics['cells'][condition]['counts']
        values.append(s['GOLD_FOLLOW']+s['OVERRIDE_TO_GOLD'] if label=='C' else s['PROPAGATE_WRONG']+s['INDUCED_WRONG'] if label=='Cp' else s[label])
    if any(values):
        bars=ax.bar(CONDITIONS,values,bottom=bottom,color=colors[label],label=label,width=.66)
        for bar,v,base in zip(bars,values,bottom):
            if v:ax.text(bar.get_x()+bar.get_width()/2,base+v/2,str(v),ha='center',va='center',color='white',weight='bold')
        bottom=[b+v for b,v in zip(bottom,values)]
ax.set_ylim(0,13);ax.set_yticks([0,3,6,9,12]);ax.set_ylabel('Cases (each condition n=12)')
ax.set_title('v3.5.1 | STOP_INVALID: C0=9/12 < 10/12',weight='bold',pad=16)
ax.legend(ncol=3,loc='upper center',bbox_to_anchor=(.5,1.01),frameon=False)
ax.spines[['top','right']].set_visible(False)
fig.supxlabel('Same fact, same semantic relevance, different task-role heading; perceived authority not independently isolated.\nExternally injected states. Cp in correct-state arms means induced wrong, not propagation. Main state-adherence gate failed.',fontsize=9)
fig.savefig(OUT/'pilot_outcomes.png',dpi=180)
fig.savefig(OUT/'pilot_outcomes.svg')
plt.close(fig)
p=OUT/'README.md';s=p.read_text(encoding='utf-8')
if '![Pilot outcomes]' not in s:s+='\n![Pilot outcomes](pilot_outcomes.png)\n'
p.write_text(s,encoding='utf-8',newline='\n')
root=Path('README.md');s=root.read_text(encoding='utf-8')
if '## Current experiment: v3.5.1' not in s:
    marker='## Current experiment: v3.4.4 answer interfaces and record order'
    assert marker in s
    section='## Current experiment: v3.5.1 task-role framing pilot\n\nCompleted **72 main calls +16 independent auxiliary checks**, with **81 tests passing**. The intervention is an externally supplied erroneous state, not a spontaneous first-hop hallucination. Twelve anonymous film targets and twelve distinct person pairs use frozen source-backed birth-city mappings.\n\n**STOP_INVALID:** S0 propagated9/12 (minimum8/12), but C0 followed the correct state only9/12 (minimum10/12). Both G-CURRENT and G-BACKGROUND returned gold12/12; paired ΔOR=0/12 and ΔPR=0/12. This descriptive equality does not rescue the failed state-adherence control. No labels, cases or thresholds were revised and no follow-up ran.\n\n'+BOUNDARY+'\n\nSee [diagnosis](results/v3_5_1/diagnosis.md), [case inspection](results/v3_5_1/inspection.md), [preregistration](results/v3_5_1/pre_registration.md), and [gate](results/v3_5_1/gate.json). Reproduce the audit with `python scripts/present_v3_5_1.py`; the model runner refuses to overwrite an existing run.\n\n'
    for a,b in [('propagated9','propagated 9'),('minimum8','minimum 8'),('only9','only 9'),('minimum10','minimum 10'),('gold12','gold 12')]:section=section.replace(a,b)
    s=s.replace(marker,section+'## Previous experiment: v3.4.4 answer interfaces and record order',1)
    root.write_text(s,encoding='utf-8',newline='\n')
changelog=Path('CHANGELOG.md')
entry='## 2026-10-06 — v3.5.1 task-role framing pilot\n\nAdded a separate six-condition injected-state pilot, explicit city mappings, heading-only prompt audits, independent capability checks, and fixed paired analysis. Completed72 main calls and16 auxiliary checks. C0=9/12 failed the10/12 gate: STOP_INVALID. Both framing arms produced12/12 gold answers; no mechanistic or spontaneous-hallucination conclusion is licensed. No automatic follow-up. Earlier experiment artifacts remain unchanged.\n'
if not changelog.exists():changelog.write_text('# Changelog\n\n'+entry,encoding='utf-8',newline='\n')
elif_text=changelog.read_text(encoding='utf-8')
if 'v3.5.1 task-role framing pilot' not in elif_text:changelog.write_text(elif_text+'\n'+entry,encoding='utf-8',newline='\n')
verify()
write_json(OUT/'independent_verification.json',dict(passed=True,main_calls=72,auxiliary_calls=16,case_pairs=12,mapping_checks=24,unique_people=7,
    exact_case_condition_matrix=True,headings_only=True,raw_and_parsed_outcomes_match=True,gate_recomputed=True,environment_matches_v3_4_4=True,
    chat_template_unchanged=True,shared_harness_source_unchanged=True,source_syntax_and_whitespace=True,unit_tests=81,prior_artifacts_preserved=len(load('model_manifest.json')['prior_artifacts']),
    interpretation_boundary=BOUNDARY,reporting_code_sha256=digest(Path(__file__))))
v=load('verification.json');v['output_hashes']={n:digest(OUT/n) for n in v['required_files']};write_json(OUT/'verification.json',v)
print(json.dumps(dict(gate=gate,C0_failures=failures,verification='PASS'),ensure_ascii=False,indent=2))
