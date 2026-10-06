"""Complete provenance metadata and repository navigation after verified inference."""
import json
import sys
from datetime import datetime,timezone
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from src.prepare_v3_4_4 import OUT,load
from src.common import digest
from src.experiment_v3 import write_json
from src.calibration_v3_4_4 import collect

original=OUT/'manifest.original.json'
assert not original.exists(), 'Finalize once; do not overwrite original provenance'
original.write_bytes((OUT/'manifest.json').read_bytes())
m=load('manifest.json')
m.update(completed_utc=datetime.now(timezone.utc).isoformat(),runtime_environment=load('runtime.json'),
         decoding=load('decoding_freeze.json'),execution_counts=load('run_state.json'),
         postrun_reporting_code_sha256={p.as_posix():digest(p) for p in Path('scripts').glob('*v3_4_4.py')},
         original_manifest_sha256=digest(original),
         provenance_note='Original manifest copied byte-for-byte at finalization, not claimed to have a new pre-run timestamp. Frozen input/source/policy hashes unchanged. Runtime metadata and completion counts appended.',
         runtime_sha256=digest(OUT/'runtime.json'),policy_selection_sha256=digest(OUT/'policy_selection.json'))
write_json(OUT/'manifest.json',m)
metrics=load('metrics.json');gate=load('gate.json');selection=load('policy_selection.json');state=load('run_state.json')
dev=metrics['cohorts']['development']
rows=collect()
counts=dict(renderings=len(rows),distinct_rendered_prompts=len({r['F']['rendered_prompt'] for r in rows}),
            main_channel_evaluations=state['main_channel_evaluations'],
            independent_smoke_and_harness_evaluations=state['smoke_channel_evaluations']+state['harness_channel_evaluations'])
write_json(OUT/'call_counts.json',counts)
section='## Current experiment: v3.4.4 answer interfaces and record order\n\n'
section+=f'Completed **{counts["renderings"]} renderings / {counts["main_channel_evaluations"]} main channel evaluations**, plus {counts["independent_smoke_and_harness_evaluations"]} independent smoke/harness evaluations. The frozen study contains 24 new development cases, six separate old diagnostic cases, and 16 confirmation cases. N is unconstrained no-list generation; R rotates complete name records; L rotates listed answer options and uses constrained selection as primary. Reused people are logged; new target IDs, graph nodes and candidate bundles are disjoint.\n\n'
section+='| Development difficulty | L first selection | L identity-sensitive cells | N strict coverage | N wrong / valid | R record-first selection |\n|---|---|---|---|---|---|\n'
for d,s in dev.items():
    values=[f'{s[k]["count"]}/{s[k]["denominator"]}' for k in ['L_first','L_order_sensitive','N_coverage','N_wrong_given_valid','R_earliest']]
    section+='| '+' | '.join([d,*values])+' |\n'
section+=f'\nDevelopment selected **{selection["route"] or "NO ROUTE"} / {selection["difficulty"] or "none"}**; confirmation passed: **{gate["passed"]}**. {gate["licensed_claim"]} Error-yield insufficient: **{gate["error_yield_insufficient"]}**. These engineering checks do not prove no residual bias. **No downstream experiment or v3.5 was executed.**\n\n'
section+='See [experiment README](results/calibration_v3_4_4/README.md), [diagnosis](results/calibration_v3_4_4/diagnosis.md), [paired inspection](results/calibration_v3_4_4/inspection.md), [supplementary diagnostics](results/calibration_v3_4_4/supplementary_diagnostics.md), and [verification](results/calibration_v3_4_4/independent_verification.json).\n\n'
section+='Post-report audit: `python scripts/verify_calibration_v3_4_4.py`. Model runs are one-shot and refuse to overwrite prior records. The original pre-inference design-audit bytes are retained separately; the completed audit appends its required results table.\n\n'
p=Path('README.md');s=p.read_text(encoding='utf-8');marker='## Current experiment: v3.4.3 candidate-order counterfactual control'
assert marker in s
s=s.replace(marker,section+'## Previous experiment: v3.4.3 candidate-order counterfactual control',1)
p.write_text(s,encoding='utf-8',newline='\n')
v=load('verification.json');v['output_hashes']={n:digest(OUT/n) for n in v['required_files_present']}
write_json(OUT/'verification.json',v)
print(json.dumps(counts,indent=2))
