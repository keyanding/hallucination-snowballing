"""Independent artifact checks and readable tables; never invokes a model."""
from collections import Counter
import json
import math
from pathlib import Path

from .calibration_v3_4_1 import OUT, FILES, load, collect, analyze, verify_frozen
from .common import digest
from .experiment_v3 import write_json
from .experiment_v3_3 import sha
from .prepare_v3_4_1 import LEVELS, evidence


def verify():
    # Original manifests retain the machine path for provenance; resolve it
    # relative to the checkout when independently verifying another clone.
    manifest=load('manifest.json')
    for category in ('frozen','prior_artifacts'):
        for name,expected in manifest[category].items():
            path=Path(name)
            if not path.exists() and '/src/' in name:
                path=Path('src') / name.split('/src/',1)[1]
            assert digest(path)==expected, f'Changed artifact: {name}'
    cases={c['case_id']:c for c in load('dev_cases.json')+load('heldout_cases.json')}
    source={r['_id']:r for r in json.loads(Path('data/dev.json').read_text(encoding='utf-8'))}
    expected_source=load('dataset_manifest.json')['source_sha256']
    assert digest(Path('data/dev.json'))==expected_source
    source_checks=0
    mapping_checks=0
    for c in cases.values():
        for candidate in c['candidates']:
            row=source[candidate['downstream_source_id']]
            ev=candidate['downstream_evidence']
            assert dict(row['context'])[ev['title']][ev['sentence_id']]==ev['text']
            assert [candidate['name'],candidate['relation'],candidate['target']] in row['evidences']
            mapping_checks+=1
        for film in [c['source_A'],c['near_wrong_film']]+([c['shared_attributes']['gold_film'],c['shared_attributes']['wrong_film']] if c['shared_attributes'] else []):
            context=dict(source[film['source_id']]['context'])
            ev=film['evidence']
            assert context[ev['title']][ev['sentence_id']]==ev['text']
            assert film['director'] in ev['text']
            source_checks+=1
        if c['shared_attributes']:
            for name in ('gold_genre_evidence','wrong_genre_evidence'):
                ev=c['shared_attributes'][name]
                assert dict(source[ev['source_id']]['context'])[ev['title']][ev['sentence_id']]==ev['text']
                source_checks+=1
    plans={(p['case_id'],p['mechanism'],p['difficulty']):p for p in load('prompt_plan.json')}
    rows=collect()
    assert len({(r['case_id'],r['mechanism'],r['difficulty']) for r in rows})==len(rows)
    for r in rows:
        c=cases[r['case_id']]
        plan=plans[r['case_id'],r['mechanism'],r['difficulty']]
        f,choice,l=r['F'],r['C'],r['L']
        names=[p['name'] for p in c['candidates']]
        assert r['gold']==c['B'] and r['gold_position']==c['gold_position']
        for channel in (f,choice,l):
            assert channel['prompt']==plan['prompt']
            assert channel['rendered_prompt']==plan['rendered_prompt']
            assert channel['prompt_sha256']==sha(plan['rendered_prompt'])
            assert channel['candidate_order']==names
            assert not channel['isolation']['use_cache']
        for channel in (f,choice):
            assert channel['raw_sha256']==sha(channel['raw_text'])
            assert channel['output_tokens']==len(channel['output_token_ids'])
        assert choice['raw_text']==choice['selected_candidate'] in names
        index=names.index(choice['selected_candidate'])
        assert choice['output_token_ids'][:-1]==plan['candidate_token_ids'][index]
        assert f['output_tokens']<=96
        assert [s['candidate'] for s in l['scores']]==names
        for index,s in enumerate(l['scores']):
            assert s['token_ids']==plan['candidate_token_ids'][index]
            assert s['token_count']==len(s['token_ids'])==len(s['token_logprobs'])
            assert math.isclose(s['sum_logprob'],sum(s['token_logprobs']),abs_tol=1e-8)
            assert math.isclose(s['mean_logprob_per_token'],s['sum_logprob']/s['token_count'],abs_tol=1e-8)
        ranked=sorted(l['scores'],key=lambda s:-s['mean_logprob_per_token'])
        assert l['top_candidate_by_mean_logprob']==ranked[0]['candidate']
        assert l['runner_up']==ranked[1]['candidate']
        assert math.isclose(l['margin_mean_logprob'],ranked[0]['mean_logprob_per_token']-ranked[1]['mean_logprob_per_token'])
    assert analyze(rows)==load('metrics.json')
    assert not any(k in json.dumps(load('metrics.json')) for k in ('"NPR"','"NRR"'))
    assert sum(r['split']=='dev' for r in rows)==96
    for m,selected in load('development_selection.json').items():
        actual=[r for r in rows if r['split']=='heldout' and r['mechanism']==m]
        assert len(actual)==(12 if selected['provisional'] else 0)
        assert all(r['difficulty']==selected['difficulty'] for r in actual)
    text='# v3.4.1 first-hop inspection\n\nAll outputs are verbatim; line breaks in tables are rendered as `<br>`. Margin means gold mean log probability minus the best wrong candidate mean, in nats/token. Exact prompts and token scores remain in the three JSONL files. Position rates are observational; this experiment does not swap orders to establish position sensitivity.\n'
    def cell(value):
        return str(value).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('|','&#124;').replace('\n','<br>')
    for case_id,c in cases.items():
        subset=[r for r in rows if r['case_id']==case_id]
        text+=f'\n## {case_id}\n\nQuestion: Who directed "{c["A"]}"?\n\nGold: {c["B"]}. Frozen gold position: {c["gold_position"]}.\n\n'
        text+='Candidates and frozen future targets (not supplied to the model):\n\n'
        text+='\n'.join(f'- {p["name"]} → {p["relation"]} → {p["target"]}' for p in c['candidates'])+'\n\n'
        if not subset:
            text+='Not evaluated: no development regime qualified for held-out confirmation.\n'
            continue
        text+='| Mechanism | Difficulty | Gold | Free | Constrained | Likelihood top-1 | Margin |\n|---|---|---|---|---|---|---|\n'
        notes=[]
        previous={}
        flipped=set()
        for r in subset:
            f,ch,l=r['F'],r['C'],r['L']
            scores={s['candidate']:s['mean_logprob_per_token'] for s in l['scores']}
            margin=scores[c['B']]-max(v for k,v in scores.items() if k!=c['B'])
            text+='| '+' | '.join(map(cell,[r['mechanism'],r['difficulty'],c['B'],f['raw_text'],ch['selected_candidate'],l['top_candidate_by_mean_logprob'],f'{margin:.4f}']))+' |\n'
            flags=[]
            if not f['exact_candidate_only']:
                flags.append('format-only failure' if f['extractable_candidate']==c['B'] else 'free format failure; semantic status reported separately')
            if f['extractable_candidate'] and f['extractable_candidate']!=ch['selected_candidate']: flags.append('extractable F/C disagreement')
            if abs(margin)<=.5: flags.append('near-zero/boundary margin (absolute value ≤0.5)')
            if f['out_of_set_name']: flags.append('heuristically detected out-of-set free name; inspect raw text')
            if f['truncated']: flags.append('free output truncated at 96 tokens')
            m=r['mechanism']
            if m in previous and previous[m]!=ch['selected_candidate'] and m not in flipped:
                flags.append('first constrained-choice flip')
                flipped.add(m)
            previous[m]=ch['selected_candidate']
            if flags: notes.append(f'- {m}/{r["difficulty"]}: '+ '; '.join(flags)+'.')
        text+='\n'+ ('\n'.join(notes) if notes else 'No choice flips, format failures, or near-boundary flags in this case.')+'\n'
        if c['split']=='dev' and case_id.endswith('01'):
            text+='\n### Exact D0–D3 evidence (same question and candidates)\n'
            for d in LEVELS:
                text+='\n'+d+'\n```text\n'+'\n'.join(evidence(c,c['mechanism'],d))+'\n```\n'
    (OUT/'inspection.md').write_text(text,encoding='utf-8')
    # Clarify rate-only eligibility versus the full preregistered selection rule.
    metrics=load('metrics.json')
    in_band=[f"{m}/{d} ({v['TWER_C']['count']}/6)" for m,levels in metrics['development'].items() for d,v in levels.items() if .2<=v['TWER_C']['rate']<=.4]
    diagnosis=(OUT/'diagnosis.md').read_text(encoding='utf-8')
    lines=diagnosis.splitlines()
    for i,line in enumerate(lines):
        if line.startswith('3. **'):
            lines[i]='3. **Gradual frontier or capability cliff?** Neither is established. M1 has an isolated D2 error that disappears at D3. M4 has errors at D0 and D3 but none at D1/D2. This is a sparse, non-monotonic pattern, not a demonstrated gradual frontier or a near-random cliff.'
        if line.startswith('4. **'):
            lines[i]='4. **Which pairs meet the target?** The error-rate band alone contains '+(', '.join(in_band) or 'none')+'. M4/D3 nevertheless has 0/6 cases inside the preregistered absolute gold-margin threshold of 0.5 nats/token (required 4/6); its median gold margin is 2.4502. Its two wrong-answer margins are -0.5065 and -0.5553. No threshold was relaxed after observing these values, and no pair qualifies provisionally.'
    diagnosis='\n'.join(lines)+'\n'
    diagnosis=diagnosis.split('\nThe three channels agree',1)[0].rstrip()+'\n'
    diagnosis+='\nThe three channels agree on all four wrong selections as well as the correct ones (96/96 agreement). This supports a semantic-selection interpretation within this task, not a claim that constrained and free decoding are generally equivalent. The 100% free-format result cannot be attributed solely to the 96-token cap because the prompt construction also differs from v3.4. Candidate plausibility is domain-level: age/country/era are not uniformly matched for all alternatives, especially older films; this can make some distractors weak.\n'
    (OUT/'diagnosis.md').write_text(diagnosis,encoding='utf-8')
    verification=load('verification.json')
    verification.update(independent_recomputation_passed=True,source_sentence_checks=source_checks,
        checked_triplets=len(rows), downstream_mapping_checks=mapping_checks, prior_artifact_count=len(manifest['prior_artifacts']), unique_keys=True, likelihood_arithmetic_verified=True,
        prompt_plan_match=True, report_generator_sha256=digest(Path(__file__)))
    write_json(OUT/'verification.json',verification)
    print(json.dumps(verification,indent=2))


if __name__=='__main__':
    verify()
