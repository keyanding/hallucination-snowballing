"""Preregister, run once, and report the v3.4.1 calibration (no propagation)."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path
from statistics import median

from .calibration_choice import CalibrationAdapter
from .common import digest, norm, read_jsonl
from .experiment_v3 import fraction, write_json
from .prepare_v3_4_1 import OUT, MECHANISMS, LEVELS, evidence, prompt, resolve_rendered

REVISION = 'cdbee75f17c01a7cc42f958dc650907174af0554'
FILES = ('free_generation.jsonl', 'constrained_choice.jsonl', 'candidate_likelihoods.jsonl')
POLICY = dict(near_boundary_nats_per_token=0.5, minimum_boundary_cases=4,
    dev_band=[0.2, 0.4], heldout_band=[0.15, 0.45], minimum_lca=0.8,
    minimum_heldout_free_coverage=0.7,
    position_bias='At a level: selected position >=50%, with >=2 wrong selections there and wrong selection >=40% among cases whose gold is elsewhere. Any flagged dev level blocks family promotion.',
    free_outset_stop='More than 50% short parseable out-of-set free answers blocks promotion.',
    tie_rule='Lowest difficulty; nearest-band ties also use lowest difficulty.',
    human_audit='Independent human review is not available in this automated run. Gate requires a recorded human audit before authorization.')


def load(name):
    return json.loads((OUT / name).read_text(encoding='utf-8'))


def summarize(rows):
    n = len(rows)
    strict = [r for r in rows if r['F']['exact_candidate_only']]
    extract = [r for r in rows if r['F']['contains_exactly_one_candidate']]
    margins = []
    positions = {}
    for r in rows:
        scores = {s['candidate']: s['mean_logprob_per_token'] for s in r['L']['scores']}
        margins.append(scores[r['gold']] - max(v for k, v in scores.items() if k != r['gold']))
    for p in range(1, 5):
        chosen = [r for r in rows if r['C']['candidate_order'].index(r['C']['selected_candidate']) + 1 == p]
        nongold = sum(r['gold_position'] != p for r in rows)
        wrong = sum(r['C']['selected_candidate'] != r['gold'] for r in chosen)
        positions[str(p)] = dict(selected=fraction(len(chosen), n), gold_count=n-nongold,
            wrong_selections=wrong, wrong_when_gold_elsewhere=fraction(wrong, nongold),
            bias_flag=bool(n and len(chosen)/n >= .5 and wrong >= 2 and nongold and wrong/nongold >= .4))
    return dict(count=n, TWER_C=fraction(sum(r['C']['selected_candidate'] != r['gold'] for r in rows), n),
        C_valid=fraction(sum(r['C']['exact_allowed_candidate'] for r in rows), n),
        FSC=fraction(len(strict), n), FCA=fraction(sum(r['F']['strict_candidate'] == r['C']['selected_candidate'] for r in strict), len(strict)),
        EFCA=fraction(sum(r['F']['extractable_candidate'] == r['C']['selected_candidate'] for r in extract), len(extract)),
        LCA=fraction(sum(r['L']['top_candidate_by_mean_logprob'] == r['C']['selected_candidate'] for r in rows), n),
        free_coverage=fraction(len(extract), n), free_outset=fraction(sum(bool(r['F']['out_of_set_name']) for r in rows), n),
        free_truncated=sum(r['F']['truncated'] for r in rows),
        L_gold_top1=fraction(sum(r['L']['top_candidate_by_mean_logprob'] == r['gold'] for r in rows), n),
        gold_vs_best_wrong_margins=margins, median_gold_margin=median(margins) if margins else None,
        near_boundary=fraction(sum(abs(m) <= POLICY['near_boundary_nats_per_token'] for m in margins), n),
        positions=positions, POSITION_BIAS=any(v['bias_flag'] for v in positions.values()))


def select(levels):
    eligible = [d for d in LEVELS if .2 <= levels[d]['TWER_C']['rate'] <= .4]
    selected = eligible[0] if eligible else min(LEVELS, key=lambda d: max(.2-levels[d]['TWER_C']['rate'], levels[d]['TWER_C']['rate']-.4, 0))
    s = levels[selected]
    reasons = []
    if not eligible:
        reasons.append('NO_STABLE_FRONTIER_FOUND')
    if s['near_boundary']['count'] < 4:
        reasons.append('INSUFFICIENT_LIKELIHOOD_BOUNDARY_SIGNAL')
    if any(v['POSITION_BIAS'] for v in levels.values()):
        reasons.append('POSITION_BIAS')
    if s['LCA']['rate'] < .8:
        reasons.append('LOW_LCA')
    if s['free_outset']['rate'] > .5:
        reasons.append('FREE_OUTSET_NONREPRESENTATIVE')
    return dict(difficulty=selected, provisional=not reasons, reasons=reasons,
                status='PROVISIONAL' if not reasons else ('NO_STABLE_FRONTIER_FOUND' if not eligible else 'REJECTED'))


def prepare():
    if (OUT / 'manifest.json').exists():
        raise FileExistsError('Preregistration already frozen')
    dev, held = load('dev_cases.json'), load('heldout_cases.json')
    assert len(dev) == 24 and len(held) == 12 and len({c['A'] for c in dev+held}) == 36
    from transformers import AutoTokenizer
    adapter = object.__new__(CalibrationAdapter)
    adapter.tokenizer = AutoTokenizer.from_pretrained('Qwen/Qwen3-4B-Instruct-2507', cache_dir='.cache/huggingface', revision=REVISION, local_files_only=True)
    plans = []
    for case in dev+held:
        names = [p['name'] for p in case['candidates']]
        assert len(set(names)) == 4 and len({norm(p['target']) for p in case['candidates']}) == 4
        assert all(p['downstream_evidence'] and p['target_aliases'] for p in case['candidates'])
        for m in ([case['mechanism']] if case['split'] == 'dev' else MECHANISMS):
            assert Counter(evidence(case, 'M3', 'D2')) == Counter(evidence(case, 'M3', 'D3'))
            for d in LEVELS:
                gold, steps = resolve_rendered(case, m, d)
                raw = prompt(case, m, d)
                rendered = adapter.render(raw)
                ids, seqs, trie = adapter.tokenize_choice(rendered, names)
                plans.append(dict(case_id=case['case_id'], split=case['split'], mechanism=m, difficulty=d,
                    prompt=raw, rendered_prompt=rendered, unique_resolved_gold=gold, composition_steps=steps,
                    input_tokens=len(ids), candidate_token_ids=seqs, reachable=trie.audit()))
    write_json(OUT / 'prompt_plan.json', plans)
    table = [
        ('Find Qwen3-specific error surface','Four mechanisms, four levels, six dev cases each','96 Channel-C choices','No empirical frontier'),
        ('Preserve traceability','Four real directors with frozen distinct targets','36/36 candidate universes covered','Cannot support future propagation'),
        ('Avoid output-format confound','Exact token trie; EOS only at complete names','All four reachable; no other terminals','Measurement interface failed'),
        ('Preserve natural-behavior visibility','Greedy free generation, 96 tokens','FSC, FCA, EFCA; raw output retained','Constrained external validity uncertain'),
        ('Measure decision confidence','Teacher force same prompt and candidate tokens; EOS excluded','Sum, mean, gold margin, LCA; boundary <=0.5 nats/token','Preference insufficiently characterized'),
        ('Avoid assuming old-model failure modes','Frozen Qwen3-4B revision, NF4/BF16','All predeclared curves measured','Mechanisms may not transfer'),
        ('Avoid overfitting calibration set','24 dev films; 12 disjoint held-out films; entities may overlap','Every selected mechanism uses all 12 once','No held-out generalization'),
        ('Preserve unique ground truth','Explicit deterministic catalog credit paths; other link types non-credit','288 rendered paths resolve uniquely; independent human audit pending','No human-certified ambiguity clearance'),
        ('Prevent position shortcuts','Dev positions 2/2/1/1, held-out 3/3/3/3; frozen order','Position-conditioned rates and preregistered bias rule','Candidate index confound'),
        ('Keep scope to calibration','Only first-hop F/C/L','No downstream generation or propagation metrics','Scope violation')]
    audit = '# v3.4.1 pre-inference design audit\n\n| Design intention | Experimental feature | Observable check | Failure meaning |\n|---|---|---|---|\n'
    audit += '\n'.join('| '+' | '.join(row)+' |' for row in table)
    audit += '\n\n## Preregistered policy\n\n```json\n'+json.dumps(POLICY, indent=2)+'\n```\n'
    audit += '\n## Construction and audit limits\n\nCatalog IDs and comparison links are experimental constructs, explicitly identified in every prompt. Film-director endpoints and shared attributes are sourced from the frozen dataset. M2 keeps candidates fixed and highlights era/genre similarity to one alternative; a 50-year era band is coarse. This tests attribute salience, not changing candidate proximity. M1/M3 overlap in relation/order manipulations; these are operational families, not independent causal mechanisms. Prior-version entities and some questions may recur; only dev/held-out target films are disjoint. No independent human audit has been claimed.\n\nEvery possible rendering is preserved in prompt_plan.json, including unexecuted held-out levels; access before inference is structural auditing, not model-based selection.\n'
    (OUT / 'design_audit.pre_inference.md').write_text(audit, encoding='utf-8')
    (OUT / 'design_audit.md').write_text(audit, encoding='utf-8')
    frozen = [Path('src/calibration_choice.py'), Path('src/prepare_v3_4_1.py'), Path(__file__), Path('src/generation/local_hf_adapter.py'), Path('src/experiment_v3.py'), Path('src/experiment_v3_3.py'), Path('src/common.py')]
    frozen += [OUT / f for f in ('dev_cases.json','heldout_cases.json','dataset_manifest.json','prompt_plan.json','design_audit.pre_inference.md')]
    old = {p.as_posix():digest(p) for folder in Path('results').glob('smoke*') for p in folder.rglob('*') if p.is_file() and '__pycache__' not in str(p)}
    write_json(OUT / 'manifest.json', dict(created_utc=datetime.now(timezone.utc).isoformat(), model='Qwen/Qwen3-4B-Instruct-2507', revision=REVISION,
        quantization='4bit-nf4', compute_dtype='torch.bfloat16', seed=42, F_max_new_tokens=96,
        C='Greedy exact token trie; all candidate strings reachable', L='Mean token log probability; sum also recorded; EOS excluded',
        policy=POLICY, frozen={p.as_posix():digest(p) for p in frozen}, prior_artifacts=old, tokenizer_preflight_renderings=len(plans)))
    print('Frozen 288 structural/tokenizer checks; no model inference performed.', flush=True)


def verify_frozen():
    manifest = load('manifest.json')
    for key in ('frozen','prior_artifacts'):
        for path, expected in manifest[key].items():
            assert digest(Path(path)) == expected, f'Changed frozen file: {path}'


def collect():
    channels = [read_jsonl(OUT / f) if (OUT / f).exists() else [] for f in FILES]
    assert len(set(map(len, channels))) == 1, 'Incomplete channel triplet: inspect, do not rerun silently'
    rows = []
    for f,c,l in zip(*channels):
        assert all(f[k] == c[k] == l[k] for k in ('case_id','split','mechanism','difficulty','prompt_sha256','candidate_order'))
        rows.append({k:f[k] for k in ('case_id','split','mechanism','difficulty','gold','gold_position')} | dict(F=f,C=c,L=l))
    return rows


def analyze(rows):
    dev = {m:{d:summarize([r for r in rows if r['split']=='dev' and r['mechanism']==m and r['difficulty']==d]) for d in LEVELS} for m in MECHANISMS}
    choices = {m:select(dev[m]) for m in MECHANISMS}
    held = {m:summarize([r for r in rows if r['split']=='heldout' and r['mechanism']==m]) for m in MECHANISMS if choices[m]['provisional']}
    return dict(development=dev, selection=choices, heldout=held, overall=summarize(rows))


def run():
    verify_frozen()
    if any((OUT/f).exists() for f in FILES):
        raise FileExistsError('Outputs exist: inspect rather than repeat inference')
    adapter = CalibrationAdapter('4bit-nf4', '.cache/huggingface', REVISION)
    assert adapter.compute_dtype == 'torch.bfloat16' and not adapter.offload and adapter.revision == REVISION
    write_json(OUT / 'runtime.json', dict(revision=adapter.revision, device_map=adapter.device_map, compute_dtype=adapter.compute_dtype, quantization=adapter.quantization))
    def execute(case,m,d):
        meta = dict(case_id=case['case_id'],split=case['split'],mechanism=m,difficulty=d,gold=case['B'],gold_position=case['gold_position'])
        values = adapter.evaluate(prompt(case,m,d), [p['name'] for p in case['candidates']])
        for file, value in zip(FILES, values):
            with (OUT/file).open('a',encoding='utf-8') as handle:
                handle.write(json.dumps(meta|value,ensure_ascii=False)+'\n')
                handle.flush()
        print(f'{case["case_id"]} {m}/{d}: C={values[1]["selected_candidate"]}; correct={values[1]["selected_candidate"]==case["B"]}; F_strict={values[0]["exact_candidate_only"]}', flush=True)
    for m in MECHANISMS:
        for d in LEVELS:
            for case in load('dev_cases.json'):
                if case['mechanism']==m:
                    execute(case,m,d)
    metrics=analyze(collect())
    write_json(OUT/'development_selection.json', metrics['selection'])
    for m, selected in metrics['selection'].items():
        if selected['provisional']:
            for case in load('heldout_cases.json'):
                execute(case,m,selected['difficulty'])
    write_json(OUT/'memory.json',adapter.memory())
    verify_frozen()
    report()


def report():
    verify_frozen()
    rows=collect()
    assert sum(r['split']=='dev' for r in rows)==96
    metrics=analyze(rows)
    assert metrics['selection']==load('development_selection.json')
    write_json(OUT/'metrics.json', metrics)
    passed=[]
    for m,s in metrics['heldout'].items():
        if s['count']==12 and .15<=s['TWER_C']['rate']<=.45 and s['C_valid']['rate']==1 and s['LCA']['rate']>=.8 and s['free_coverage']['rate']>=.7 and not s['POSITION_BIAS']:
            passed.append(m)
    gate=dict(pass_gate=False, statistical_qualifiers=passed, human_audit_status='PENDING_INDEPENDENT_HUMAN_REVIEW',
        reason='No stable confirmed frontier' if not passed else 'Statistical criteria met, but independent human ambiguity audit required',
        v35_authorized=False, downstream_branches_run=0)
    write_json(OUT/'gate.json',gate)
    frontier='# Frontier selection\n\nLowest in-band difficulty; nearest out-of-band level is diagnostic only. No post-output tuning.\n\n| Mechanism | D0 | D1 | D2 | D3 | Selected/diagnostic | Status |\n|---|---|---|---|---|---|---|\n'
    for m in MECHANISMS:
        rates=[f'{metrics["development"][m][d]["TWER_C"]["count"]}/6' for d in LEVELS]
        s=metrics['selection'][m]
        frontier+='| '+' | '.join([m]+rates+[s['difficulty'],s['status']+': '+', '.join(s['reasons'])])+' |\n'
    (OUT/'frontier_selection.md').write_text(frontier,encoding='utf-8')
    inspection='# First-hop calibration inspection\n\nMargin is gold mean log probability minus best wrong mean log probability. Full exact prompts and raw outputs are in the JSONL channel files.\n'
    cases={c['case_id']:c for c in load('dev_cases.json')+load('heldout_cases.json')}
    for case_id,case in cases.items():
        subset=[r for r in rows if r['case_id']==case_id]
        inspection+=f'\n## {case_id}: Who directed "{case["A"]}"?\n\n'
        if not subset:
            inspection+='Not evaluated: no selected mechanism requested this held-out case.\n'
            continue
        inspection+='| Mechanism | Difficulty | Gold | Free | Constrained | Likelihood top-1 | Margin |\n|---|---|---|---|---|---|---|\n'
        previous={}
        for r in subset:
            f,c,l=r['F'],r['C'],r['L']
            scores={x['candidate']:x['mean_logprob_per_token'] for x in l['scores']}
            margin=scores[r['gold']]-max(v for k,v in scores.items() if k!=r['gold'])
            raw=f['raw_text'].replace('|','\\|').replace('\n','<br>')
            inspection+='| '+' | '.join([r['mechanism'],r['difficulty'],r['gold'],raw,c['selected_candidate'],l['top_candidate_by_mean_logprob'],f'{margin:.4f}'])+' |\n'
            flags=[]
            if not f['exact_candidate_only']: flags.append('free format failure (not counted as semantic error)')
            if f['extractable_candidate'] and f['extractable_candidate']!=c['selected_candidate']: flags.append('F/C disagreement')
            if abs(margin)<=.5: flags.append('near boundary')
            if f['out_of_set_name']: flags.append('possible out-of-set free name')
            if r['mechanism'] in previous and previous[r['mechanism']]!=c['selected_candidate']: flags.append('constrained choice flip')
            previous[r['mechanism']]=c['selected_candidate']
            if flags: inspection+='\n'+r['mechanism']+'/'+r['difficulty']+': '+ '; '.join(flags)+'.\n\n'
        if case['split']=='dev' and case_id.endswith('01'):
            inspection+='\n### Exact evidence by difficulty\n'
            for d in LEVELS:
                inspection+='\n'+d+'\n```text\n'+'\n'.join(evidence(case,case['mechanism'],d))+'\n```\n'
    (OUT/'inspection.md').write_text(inspection,encoding='utf-8')
    errors=[m for m in MECHANISMS if any(metrics['development'][m][d]['TWER_C']['count'] for d in LEVELS)]
    o=metrics['overall']
    diagnosis='# v3.4.1 diagnosis\n\nThis is calibration of one frozen Qwen3-4B NF4/BF16 model and a constructed catalog task, not a propagation experiment or a general research conclusion.\n\n'
    answers=[('Which families cause errors?',str(errors) if errors else 'None of the four tested families produced a constrained-choice error.'),
        ('Which do not?',str([m for m in MECHANISMS if m not in errors])),
        ('Gradual frontier or capability cliff?','See the complete predeclared curves below. No untested intermediate difficulty is inferred.'),
        ('Which pairs meet the target?',str({m:s for m,s in metrics['selection'].items() if s['provisional']}) or 'None'),
        ('Held-out confirmation?',json.dumps(metrics['heldout'],ensure_ascii=False) if metrics['heldout'] else 'Not run: no provisional frontier. The twelve frozen cases remain unqueried.'),
        ('Does free generation support constrained choice?',f'FSC={o["FSC"]}; FCA={o["FCA"]}; EFCA={o["EFCA"]}; truncated={o["free_truncated"]}. Formatting failures are separate from semantic choices.'),
        ('Does likelihood support constrained choice?',f'LCA={o["LCA"]}; gold margin distributions and boundary fractions are in metrics.json. Mean-normalized likelihood is diagnostic, never a substitute for C.'),
        ('Ambiguity, position bias, or formatting?',f'Every rendered credit path resolves uniquely in the programmatic audit. Independent human review remains pending. Flagged families: {[m for m in MECHANISMS if any(metrics["development"][m][d]["POSITION_BIAS"] for d in LEVELS)]}. Position rates do not establish causal position sensitivity without order swaps; no swaps were run.'),
        ('What should be frozen for v3.5?',gate['reason']+'. No v3.5 launch or construction recommendation is authorized by this run.')]
    for i,(q,a) in enumerate(answers,1): diagnosis+=f'{i}. **{q}** {a}\n\n'
    diagnosis+=frontier+'\n## Limits\n\nSix development cases per family give a coarse error grid (only 2/6 lies inside 20–40%). This design may remain too easy; that is a valid negative calibration outcome. Catalog conventions explicitly disambiguate relations, and composition is index traversal rather than unrestricted factual reasoning. M2 highlights shared attributes for one alternative, uses broad 50-year bands, and does not change the candidate set. Entities can recur across splits; only target film questions are disjoint. Do not redesign or retune using held-out answers. Future evaluation must exclude all 36 films.\n'
    (OUT/'diagnosis.md').write_text(diagnosis,encoding='utf-8')
    audit=(OUT/'design_audit.pre_inference.md').read_text(encoding='utf-8')
    audit+='\n## Post-inference achievement check\n\n| Design intention | Achieved / evidence |\n|---|---|\n'
    achievements=[('Error surface',f'96 development renderings completed; frontier found: {bool(passed)}'),('Traceability','All frozen candidate mappings retained'),('Format separation',f'C validity {o["C_valid"]}'),('Natural behavior',f'FSC/FCA/EFCA reported for {len(rows)} prompts'),('Confidence','All four token-level scores and margins retained'),('Model-specific calibration','Pinned Qwen3 revision, NF4/BF16'),('Hold-out protection',f'{sum(r["split"]=="heldout" for r in rows)} held-out renderings, only dev-selected regimes'),('Unique ground truth','Structural audit passed; independent human certification pending'),('Position control','Frozen balanced positions; conditional rates reported'),('Calibration scope','Zero downstream calls; propagation metrics absent')]
    audit+='\n'.join('| '+a+' | '+b+' |' for a,b in achievements)+'\n'
    (OUT/'design_audit.md').write_text(audit,encoding='utf-8')
    write_json(OUT/'verification.json',dict(frozen_inputs_unchanged=True,prior_artifacts_unchanged=True,channel_triplets=len(rows),
        output_hashes={f:digest(OUT/f) for f in FILES}, selection_sha256=digest(OUT/'development_selection.json')))
    print(json.dumps(gate),flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('action',choices=['prepare','run','report'])
    args=parser.parse_args()
    globals()[args.action]()
