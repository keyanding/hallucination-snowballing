"""Freeze and execute v3.4.2 exactly once using the verified local adapter."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path
import traceback

from .analysis_v3_4_2 import POLICY, analyze, margin
from .calibration_choice import CalibrationAdapter
from .calibration_v3_4_1 import REVISION, FILES
from .common import digest, read_jsonl
from .experiment_v3 import write_json
from .experiment_v3_3 import sha
from .graph_v3_4_2 import OUT, GRID, RELATIONS, audit_prompt, key, load, make_cases, render, validate_sources


def prepare():
    if OUT.exists():
        raise FileExistsError('Refusing to overwrite preregistration')
    dev, held = make_cases()
    assert len(dev)==8 and len(held)==12
    assert len({c['target'] for c in dev+held})==20
    assert Counter(c['gold_position'] for c in dev)==Counter({i:2 for i in range(1,5)})
    assert Counter(c['gold_position'] for c in held)==Counter({i:3 for i in range(1,5)})
    mappings = validate_sources(dev+held)
    from transformers import AutoTokenizer
    adapter = object.__new__(CalibrationAdapter)
    adapter.tokenizer = AutoTokenizer.from_pretrained('Qwen/Qwen3-4B-Instruct-2507', cache_dir='.cache/huggingface', revision=REVISION, local_files_only=True)
    plan = []
    for c in dev+held:
        for d,b in GRID:
            prompt = render(c,d,b)
            audit = audit_prompt(c,d,b,prompt)
            rendered = adapter.render(prompt)
            ids, sequences, trie = adapter.tokenize_choice(rendered,[p['name'] for p in c['candidates']])
            plan.append(dict(case_id=c['case_id'],split=c['split'],depth=d,branches=b,condition=key(d,b),
                prompt=prompt,rendered_prompt=rendered,prompt_sha256=sha(rendered),
                candidate_list_sha256=c['candidate_list_sha256'],input_tokens=len(ids),
                candidate_token_ids=sequences,all_candidates_reachable=trie.audit(),audit=audit))
    old_artifacts = {p.as_posix():digest(p) for p in Path('results').rglob('*') if p.is_file() and '__pycache__' not in str(p)}
    OUT.mkdir(parents=True)
    write_json(OUT/'dev_cases.json',dev)
    write_json(OUT/'heldout_cases.json',held)
    write_json(OUT/'prompt_plan.json',plan)
    table = [
        ('Build a monotonic difficulty axis','Depth 1–4 × branch count 0–2; eight paired dev cases','ER and median gold margin on all 12 cells; 9 depth and 8 branch comparisons','Observed difficulty may not be ordered'),
        ('Separate two sources of difficulty','At fixed depth all paths have equal length; branch count adds whole parallel paths','Factor-specific curves and paired neighboring changes','Cannot attribute difficulty source'),
        ('Preserve traceability','Four real directors per case with distinct frozen targets and aliases','80/80 mapping records checked against source triples and sentences','Future propagation cannot be measured'),
        ('Avoid candidate-identity confounds','Candidate list, order, name records, and targets fixed across all conditions','Candidate hashes and prompt invariant sections; 2/position dev, 3/position held-out','Difficulty mixed with identity replacement'),
        ('Avoid format confounds','Existing exact trie C; F greedy 96 tokens; one identical rendered prompt','C validity 100%; all candidate terminals reachable; FCA','Interface failure'),
        ('Measure capability boundary','Teacher-forced candidate mean log probability; EOS excluded','Gold margin, NBF using fixed absolute threshold 0.75; sum scores also retained','Errors may be isolated case artifacts'),
        ('Avoid isolated-error selection','Immediate easier neighbor must have strictly lower ER or higher GM','Per-condition local-support table; no new conditions after inference','Selected condition is a spike'),
        ('Prevent overfitting','Eight dev symbolic targets and twelve new held-out targets, sampled seed 342 before inference','At most two conditions, each on all twelve held-out once','Frontier does not replicate'),
        ('Preserve unique answer','Credited path plus equal-depth comparison/associated paths with disjoint nodes','Parse all 240 rendered graphs; exactly one queried endpoint, no cycles','Errors may reflect ambiguity'),
        ('Keep calibration scope','Only first-hop F/C/L evaluations','No downstream continuation or propagation metrics','Premature propagation claim')]
    text = '# v3.4.2 pre-inference design audit\n\n| Design intention | Experimental feature | Observable check | Failure meaning |\n|---|---|---|---|\n'
    text += '\n'.join('| '+' | '.join(row)+' |' for row in table)+'\n'
    text += '\n## Frozen decisions\n\n```json\n'+json.dumps(POLICY,indent=2)+'\n```\n'
    text += '\n## Interpretation and invariance review\n\nTargets are anonymous synthetic Film identifiers, not claims about real films. Candidate bundles are sampled deterministically from the v3.4.1 pre-inference datasets, without consulting output correctness; only candidate identities and source-backed downstream mappings are reused. Dev/held-out target questions are disjoint, while entities may overlap. Every future v3.5 target must be separate from both splits.\n\nAll relation vocabulary appears in the same convention even when a relation has no link records. A competing path uses one non-query relation consistently on all its edges, following the spec section 9 example; it differs from the queried path in relation type, not by exactly one altered edge. Every path has the selected depth and terminates at a distinct registered candidate. Candidate-name records precede graph links in a fixed order. Three possible path blocks have a frozen random order per case; absent branches are omitted. Node IDs are sampled independently of candidate order. Only path length and the number of included path blocks vary. Longer paths also increase token count, an inherent limitation of this depth manipulation.\n\nThe verifier parses the actual rendered records and traverses relation-specific links; it does not rely only on the graph generator. All four candidate strings have been tokenized against the exact pinned chat template and every guided terminal is reachable. Programmatic graph validation is not represented as an independent human audit.\n'
    (OUT/'design_audit.pre_inference.md').write_text(text,encoding='utf-8',newline='\n')
    (OUT/'design_audit.md').write_text(text,encoding='utf-8',newline='\n')
    spec = Path('C:/Users/kding/Downloads/experiment_v3_4_2_codex_spec.md')
    if spec.exists():
        (OUT/'spec.md').write_bytes(spec.read_bytes())
    frozen = list(Path('src').rglob('*.py')) + [OUT/n for n in ('dev_cases.json','heldout_cases.json','prompt_plan.json','design_audit.pre_inference.md')]
    if (OUT/'spec.md').exists():
        frozen.append(OUT/'spec.md')
    write_json(OUT/'manifest.json',dict(created_utc=datetime.now(timezone.utc).isoformat(),
        model='Qwen/Qwen3-4B-Instruct-2507',revision=REVISION,quantization='4bit-nf4',compute_dtype='torch.bfloat16',
        generation_seed=42,data_seed=342,policy=POLICY,relation_vocabulary=list(RELATIONS),
        F=dict(max_new_tokens=96,do_sample=False),C=dict(method='prefix_allowed_tokens_fn exact candidate trie',EOS=adapter.tokenizer.eos_token_id),
        L=dict(method='same rendered prompt teacher forcing',primary='mean_logprob_per_token',EOS_scored=False),
        source_sha256=digest(Path('data/dev.json')),frozen={p.as_posix():digest(p) for p in frozen},
        prior_artifacts=old_artifacts,structural_and_tokenizer_checks=len(plan),candidate_mapping_checks=mappings,
        selection_order='All 96 dev prompts, freeze selection, then selected held-out conditions only',
        heldout_new_targets=True,entity_overlap_allowed=True))
    print('Frozen 20 cases, 240 graph/tokenizer checks, 80 downstream mappings; inference not started.',flush=True)


def verify_frozen():
    manifest=load('manifest.json')
    for category in ('frozen','prior_artifacts'):
        for name,expected in manifest[category].items():
            assert digest(Path(name))==expected, f'Changed frozen artifact: {name}'
    assert digest(Path('data/dev.json'))==manifest['source_sha256']


def collect():
    channels=[read_jsonl(OUT/name) if (OUT/name).exists() else [] for name in FILES]
    assert len(set(map(len,channels)))==1, 'Partial channel triplet; do not silently rerun'
    result=[]
    for f,c,l in zip(*channels):
        fields=('case_id','split','depth','branches','gold','gold_position','prompt_sha256','candidate_order','selection_sha256')
        assert all(f[name]==c[name]==l[name] for name in fields)
        result.append({name:f[name] for name in fields[:6]} | dict(F=f,C=c,L=l))
    return result


def run():
    verify_frozen()
    if (OUT/'run_state.json').exists() or any((OUT/name).exists() for name in FILES):
        raise FileExistsError('Run already started; no automatic retries or overwrites')
    write_json(OUT/'run_state.json',dict(status='loading_model'))
    adapter=CalibrationAdapter('4bit-nf4','.cache/huggingface',REVISION)
    assert adapter.compute_dtype=='torch.bfloat16' and not adapter.offload and adapter.revision==REVISION
    write_json(OUT/'runtime.json',dict(revision=adapter.revision,device_map=adapter.device_map,
        quantization=adapter.quantization,compute_dtype=adapter.compute_dtype,offload=adapter.offload))
    plans={(p['case_id'],p['depth'],p['branches']):p for p in load('prompt_plan.json')}
    def execute(case,d,b,selection_hash=None):
        plan=plans[case['case_id'],d,b]
        meta=dict(case_id=case['case_id'],split=case['split'],depth=d,branches=b,
                  gold=case['gold'],gold_position=case['gold_position'],selection_sha256=selection_hash)
        write_json(OUT/'run_state.json',dict(status='evaluating',current=meta))
        values=adapter.evaluate(plan['prompt'],[p['name'] for p in case['candidates']])
        for value in values:
            assert value['rendered_prompt']==plan['rendered_prompt']
        f,c,l=values
        f.update(strict_exact_candidate=f['exact_candidate_only'],out_of_set=bool(f['out_of_set_name']))
        ranked=sorted(l['scores'],key=lambda s:-s['mean_logprob_per_token'])
        for i,score in enumerate(ranked,1):
            score['rank']=i
        l['gold_vs_best_wrong_margin']=margin(dict(gold=case['gold'],L=l))
        for filename,value in zip(FILES,values):
            with (OUT/filename).open('a',encoding='utf-8',newline='\n') as handle:
                handle.write(json.dumps(meta|value,ensure_ascii=False)+'\n')
                handle.flush()
        print(f'{case["case_id"]} {key(d,b)}: C={c["selected_candidate"]}; correct={c["selected_candidate"]==case["gold"]}; GM={l["gold_vs_best_wrong_margin"]:.3f}',flush=True)
    try:
        for d,b in GRID:
            for case in load('dev_cases.json'):
                execute(case,d,b)
        metrics=analyze(collect())
        write_json(OUT/'development_selection.json',metrics['selection'])
        selection_hash=digest(OUT/'development_selection.json')
        for condition in metrics['selection']['selected']:
            detail=metrics['selection']['conditions'][condition]
            for case in load('heldout_cases.json'):
                execute(case,detail['depth'],detail['branches'],selection_hash)
        verify_frozen()
        write_json(OUT/'memory.json',adapter.memory())
        write_json(OUT/'run_state.json',dict(status='completed',triplets=len(collect())))
    except Exception:
        write_json(OUT/'failure.json',dict(error=traceback.format_exc(),state=load('run_state.json'),
            policy='Retain partial output; do not replace cases or repeat calls automatically'))
        raise
    from .report_v3_4_2 import report
    report()


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('action',choices=['prepare','run','verify','report'])
    args=parser.parse_args()
    if args.action in ('prepare','run'):
        globals()[args.action]()
    else:
        from .report_v3_4_2 import report, verify
        {'report':report,'verify':verify}[args.action]()
