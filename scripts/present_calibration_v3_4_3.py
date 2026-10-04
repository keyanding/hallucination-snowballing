"""Add transparent case-level interpretation of already frozen observations."""
import json
from pathlib import Path

root=Path(__file__).resolve().parents[1]
out=root/'results/calibration_v3_4_3'
metrics=json.loads((out/'metrics.json').read_text(encoding='utf-8'))
rows=[json.loads(line) for line in (out/'constrained_choice.jsonl').read_text(encoding='utf-8').splitlines()]
trajectories=json.loads((out/'dev05_trajectories.json').read_text(encoding='utf-8'))
text='## Observed case-level interpretation\n\n'
text+='The controlled rotations support a candidate-position effect that increases with difficulty in this selected sample. They do not support a universal always-first strategy: identity/case dependence remains, and several sets are gold-stable. No non-gold identity is selected in all four orders of any set.\n\n'
for cid in ('dev-04','dev-07'):
    group=[r for r in rows if r['case_id']==cid]
    identity=group[0]['original_pos1']
    baseline=[r for r in group if r['permutation']==1]
    moved=[r for r in group if r['permutation']!=1]
    still=sum(r['selected_candidate']==identity for r in moved)
    initial=sum(r['selected_candidate']==identity for r in baseline)
    text+=f'- {cid}: original first identity **{identity}** is selected {initial}/{len(baseline)} times in P1 across the three difficulties, but only {still}/{len(moved)} times after it moves to positions 4/3/2. This contradicts an order-invariant wrong-identity lock, without implying all remaining choices follow position 1.\n'
monotonic=sum(t['margins'][0]>t['margins'][1]>t['margins'][2] for t in trajectories)
easy_to_hard=sum(not t['errors'][0] and t['errors'][2] for t in trajectories)
mid_wrong=sum(t['errors'][1] for t in trajectories)
text+=f'\nFor dev-05, gold margin declines strictly EASY→MID→HARD in **{monotonic}/4** fixed-order trajectories, and EASY-correct→HARD-wrong occurs in **{easy_to_hard}/4**. The original MID error survives in only **{mid_wrong}/4** orders. Thus degradation across complexity remains, while the location of the behavioral boundary changes with candidate order; the reported 1/4 strict original-pattern retention must not be read as absence of all complexity effects.\n\n'
text+='Four F outputs first emit a candidate and then begin reconsideration/explanation before truncating at the frozen 96-token cap. Their one-name extraction is auxiliary only: it is not a completed natural answer or strict compliance. The run does not establish whether longer free reasoning would repair them. C measures guided candidate choice; agreement with F is 68/68 among strict outputs, not 72/72 completed free answers.\n\n'
text+='MID retains diagnostic frontier-like averages, but its PSR1 remains 54.2%; HARD has PSR1 66.7% and only 8.3% near-boundary coverage. Counterbalancing equalizes identity exposure; it does not eliminate the model\'s observed first-position preference. Neither clean route is supported, and no propagation run is authorized.\n\n'
text+='![Candidate-order controls](position_controls.png)\n'
p=out/'diagnosis.md'
original=p.read_text(encoding='utf-8').split('\n## Observed case-level interpretation',1)[0].rstrip()
p.write_text(original+'\n\n'+text,encoding='utf-8',newline='\n')
