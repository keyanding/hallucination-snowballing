"""Present observed position/case diagnostics without altering frozen selection."""
import json
from pathlib import Path
import re

root=Path(__file__).resolve().parents[1]
out=root/'results/calibration_v3_4_2'
m=json.loads((out/'metrics.json').read_text(encoding='utf-8'))
o=m['development_overall']
near=[name for name,s in m['selection']['conditions'].items() if s['failed_checks']==['no_position_bias']]
positions=o['positions']
always=[name for name,s in m['case_consistency'].items() if 'CASE_ALWAYS_WRONG' in s['labels']]
always_errors=sum(m['case_consistency'][name]['wrong_count'] for name in always)
text='## Position and case diagnostics\n\n'
text+=f'The preregistered pooled POSITION_BIAS flag is **{o["POSITION_BIAS"]}**. '+(', '.join(near) or 'No condition')+' meets all other development criteria but is not selected. No new threshold, candidate ordering, or model call was introduced in this presentation step.\n\n'
text+='| Candidate position | Times selected / 96 | Gold occurrences | Wrong selections | Wrong selections when gold elsewhere / 72 | Share of 38 errors |\n|---|---|---|---|---|---|\n'
for position,p in positions.items():
    share=p['wrong_selections']/o['ER']['count'] if o['ER']['count'] else 0
    text+=f'| {position} | {p["selected"]["count"]}/96 | {p["gold_count"]} | {p["wrong_selections"]} | {p["wrong_when_gold_elsewhere"]["count"]}/72 | {share:.1%} |\n'
text+=f'\nAlways-wrong base cases: {", ".join(always) or "none"}; these contribute {always_errors}/{o["ER"]["count"]} errors. The 96 decisions are repeated measurements on eight base cases, not 96 independent cases. Because candidate identities remain at fixed positions within each case, the position flag cannot distinguish index preference from candidate-identity or case effects. It is a conservative exclusion signal, not proof of a causal position effect. No candidate-order counterfactual was run.\n\n'
text+='The observed axis is partly ordered, not globally monotonic: depth ER/GM satisfy 6/9 and 7/9 adjacent comparisons, while branch ER/GM both satisfy 7/8. Margin support at selected-looking cells does not override the position exclusion. The held-out split remains unqueried.\n'
(out/'position_audit.md').write_text(text,encoding='utf-8',newline='\n')
start='<!-- v342 observed-outcome start -->'
end='<!-- v342 observed-outcome end -->'
summary=start+'\n\n**Outcome: gate failed because the frozen position-bias exclusion fired.** '+', '.join(near)+' meet all other development criteria. The first candidate is selected 54/96 times; 34/38 wrong selections are at position 1. Held-out was not run. See the position table below for counts and interpretation limits.\n\n'+end+'\n\n'
p=out/'diagnosis.md'
original=p.read_text(encoding='utf-8')
original=re.sub(re.escape(start)+r'.*?'+re.escape(end)+r'\n*','',original,flags=re.S)
original=original.split('\n## Position and case diagnostics',1)[0].rstrip()+'\n'
heading,body=original.split('\n',1)
p.write_text(heading+'\n\n'+summary+body.lstrip()+'\n'+text+'\n![Development grid](development_grid.png)\n',encoding='utf-8',newline='\n')
