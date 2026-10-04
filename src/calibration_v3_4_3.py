"""Freeze byte-audited order-only counterfactuals and run the three channels."""
import argparse
from datetime import datetime, timezone
import difflib
import json
from pathlib import Path
import traceback

from .analysis_v3_4_3 import CASE_IDS, CONDITIONS, POLICY
from .analysis_v3_4_2 import margin
from .calibration_choice import CalibrationAdapter
from .calibration_v3_4_1 import REVISION, FILES
from .common import digest, read_jsonl
from .experiment_v3 import write_json
from .experiment_v3_3 import sha
from .graph_v3_4_2 import audit_prompt, validate_sources

OUT=Path('results/calibration_v3_4_3')
PRIOR=Path('results/calibration_v3_4_2')
START='\n\nCandidate names:\n'
END='\n\nCandidate-name records:\n'


def load(name):
    return json.loads((OUT/name).read_text(encoding='utf-8'))


def split_prompt(prompt):
    assert prompt.count(START)==1 and prompt.count(END)==1
    prefix,tail=prompt.split(START)
    options,suffix=tail.split(END)
    names=[]
    for i,line in enumerate(options.splitlines(),1):
        assert line.startswith(f'{i}. ')
        names.append(line[len(f'{i}. '):])
    assert len(names)==4 and len(set(names))==4
    return prefix+START,names,END+suffix


def rotate_prompt(prompt,permutation):
    assert permutation in (1,2,3,4)
    prefix,names,suffix=split_prompt(prompt)
    offset=permutation-1
    rotated=names[offset:]+names[:offset]
    return prefix+'\n'.join(f'{i}. {name}' for i,name in enumerate(rotated,1))+suffix,rotated


def build_plan():
    old_manifest=json.loads((PRIOR/'manifest.json').read_text(encoding='utf-8'))
    for name in ('dev_cases.json','prompt_plan.json'):
        assert digest(PRIOR/name)==old_manifest['frozen'][(PRIOR/name).as_posix()]
    pool={c['case_id']:c for c in json.loads((PRIOR/'dev_cases.json').read_text(encoding='utf-8'))}
    cases=[pool[cid] for cid in CASE_IDS]
    old_plans={(p['case_id'],p['depth'],p['branches']):p for p in json.loads((PRIOR/'prompt_plan.json').read_text(encoding='utf-8'))}
    plans=[]
    for difficulty,(d,b) in CONDITIONS.items():
        for c in cases:
            original=old_plans[c['case_id'],d,b]
            prefix,original_names,suffix=split_prompt(original['prompt'])
            assert original_names==[p['name'] for p in c['candidates']]
            for permutation in range(1,5):
                prompt,names=rotate_prompt(original['prompt'],permutation)
                left,current,right=split_prompt(prompt)
                assert left==prefix and right==suffix and current==names
                result=audit_prompt(c,d,b,prompt)
                assert result==original['audit']
                if permutation==1:
                    assert prompt.encode('utf-8')==original['prompt'].encode('utf-8')
                plans.append(dict(case_id=c['case_id'],difficulty=difficulty,depth=d,branches=b,
                    permutation=permutation,prompt=prompt,candidate_order=names,gold=c['gold'],gold_position=names.index(c['gold'])+1,
                    original_pos1=original_names[0],invariant_prefix_sha256=sha(prefix),invariant_suffix_sha256=sha(suffix),
                    prior_prompt_sha256=original['prompt_sha256'],prior_rendered_prompt=original['rendered_prompt'],graph_audit=result))
            subset=plans[-4:]
            assert all({p['candidate_order'].index(name)+1 for p in subset}=={1,2,3,4} for name in original_names)
    return cases,plans


def prepare():
    if OUT.exists():
        raise FileExistsError('Refusing to overwrite preregistration')
    cases,plans=build_plan()
    mapping_count=validate_sources(cases)
    from transformers import AutoTokenizer
    adapter=object.__new__(CalibrationAdapter)
    adapter.tokenizer=AutoTokenizer.from_pretrained('Qwen/Qwen3-4B-Instruct-2507',cache_dir='.cache/huggingface',revision=REVISION,local_files_only=True)
    for plan in plans:
        rendered=adapter.render(plan['prompt'])
        ids,sequences,trie=adapter.tokenize_choice(rendered,plan['candidate_order'])
        if plan['permutation']==1:
            assert rendered==plan['prior_rendered_prompt'] and sha(rendered)==plan['prior_prompt_sha256']
        plan.update(rendered_prompt=rendered,prompt_sha256=sha(rendered),input_tokens=len(ids),
                    candidate_token_ids=sequences,all_candidates_reachable=trie.audit())
    prior={p.as_posix():digest(p) for p in Path('results').rglob('*') if p.is_file() and '__pycache__' not in str(p)}
    OUT.mkdir(parents=True)
    write_json(OUT/'case_manifest.json',dict(cases=cases,case_ids=list(CASE_IDS),conditions=CONDITIONS,
        roles=dict(always_wrong=['dev-04','dev-07'],boundary='dev-05',additional='dev-01',easy_controls=['dev-06','dev-08']),
        selection='Exactly user-specified v3.4.2 development cases; not a random sample',mapping_checks=mapping_count))
    write_json(OUT/'permutation_plan.json',plans)
    diff='# Prompt invariance and counterfactual diff audit\n\nP1 is byte-identical to its original v3.4.2 prompt and rendered chat. Only the four numbered answer-option lines change. Original name-record order is retained as the canonical evidence order; the candidate list is not relocated to the preferred example layout because that would introduce another intervention.\n'
    for difficulty in CONDITIONS:
        for cid in CASE_IDS:
            group=[p for p in plans if p['case_id']==cid and p['difficulty']==difficulty]
            first=group[0]
            diff+=f'\n## {cid}/{difficulty}\n\nFixed prefix SHA256: `{first["invariant_prefix_sha256"]}`. Fixed suffix (name records, graph, query, output instruction) SHA256: `{first["invariant_suffix_sha256"]}`. Gold identity: {first["gold"]}. Every identity occupies each position once.\n'
            for other in group[1:]:
                lines=difflib.unified_diff(first['prompt'].splitlines(),other['prompt'].splitlines(),fromfile='P1',tofile=f'P{other["permutation"]}',n=1,lineterm='')
                diff+='\n```diff\n'+'\n'.join(lines)+'\n```\n'
    (OUT/'prompt_diff_audit.md').write_text(diff,encoding='utf-8',newline='\n')
    intentions=[
        ('Separate position from identity','Four fixed cyclic rotations per case-condition','72 plans; every identity at each position once','Identity and position remain confounded'),
        ('Test candidate-position primacy','Replace only explicit four-line candidate list','PSR, GPA, paired identity Delta, choice changes','No causal candidate-list-order evidence'),
        ('Keep evidence order fixed','Original v3.4.2 name and graph records kept byte-identical','Fixed suffix hashes and all 54 prompt diffs','Evidence order is confounded'),
        ('Test complexity x primacy','EASY D1B0, MID D3B0, HARD D4B2','PSR1/PFR/Delta separately on six paired cases','Interaction cannot be assessed'),
        ('Preserve prior frontier evidence','Original graphs and exact P1 rendering','All 18 P1 prompts reproduce; compare new P1 calls diagnostically','Original result not reproduced'),
        ('Preserve traceability','Same four candidates and downstream mappings per case','24/24 mapping records audited','Cannot reconnect to future propagation'),
        ('Avoid format confounds','Unchanged F96/C exact trie/L same-template scoring','C validity, FCA, LCA; all candidate terminals reachable','Interface contamination'),
        ('Avoid post-hoc selection','Six specified cases frozen; 72 new calls','Manifest/code/data hashes; no replacements','Cherry-picking risk'),
        ('Keep causal claim narrow','Only answer-option list changes','No evidence-order change; no internal-mechanism claim','Cannot infer general sequence primacy'),
        ('Keep calibration scope','No downstream continuation','Propagation metrics absent','Premature propagation claim')]
    audit='# v3.4.3 pre-inference design audit\n\n| Design intention | Experimental feature | Observable check | Failure meaning |\n|---|---|---|---|\n'
    audit+='\n'.join('| '+' | '.join(row)+' |' for row in intentions)+'\n'
    audit+='\n## Preregistered definitions\n\n```json\n'+json.dumps(POLICY,indent=2)+'\n```\n'
    audit+='\nPFR is reported both literally and with strict previous-selection/change requirements. Identity-locked choices can sometimes select the new first option without following position, so the literal rate alone is not evidence of primacy. All 18 sets and six cases remain visible; no permutation test or independent-prompt p-value is planned. Quantitative descriptive flags operationalize unspecified words such as strong/high; they are not significance thresholds. A causal effect here means an output change under the controlled list intervention, not a claim about internal attention or the v3.3 evidence-order mechanism.\n'
    (OUT/'design_audit.pre_inference.md').write_text(audit,encoding='utf-8',newline='\n')
    (OUT/'design_audit.md').write_text(audit,encoding='utf-8',newline='\n')
    spec=Path('C:/Users/kding/Downloads/experiment_v3_4_3_codex_spec.md')
    (OUT/'spec.md').write_bytes(spec.read_bytes())
    frozen=list(Path('src').rglob('*.py'))+[OUT/n for n in ('case_manifest.json','permutation_plan.json','prompt_diff_audit.md','design_audit.pre_inference.md','spec.md')]
    write_json(OUT/'manifest.json',dict(created_utc=datetime.now(timezone.utc).isoformat(),model='Qwen/Qwen3-4B-Instruct-2507',
        revision=REVISION,quantization='4bit-nf4',compute_dtype='torch.bfloat16',generation_seed=42,
        F_max_new_tokens=96,C_EOS=adapter.tokenizer.eos_token_id,L_scoring='Mean/token; sums retained; EOS excluded; same rendered prompt',
        policy=POLICY,source_sha256=digest(Path('data/dev.json')),frozen={p.as_posix():digest(p) for p in frozen},
        prior_artifacts=prior,prompt_count=72,repeated_sets=18,cases=6,prior_P1_byte_matches=18))
    print('Frozen 72 permutations; 18 exact P1 replications; 24 mappings; no inference yet.',flush=True)


def verify_frozen():
    manifest=load('manifest.json')
    for kind in ('frozen','prior_artifacts'):
        for name,expected in manifest[kind].items():
            assert digest(Path(name))==expected, f'Changed frozen file: {name}'
    assert digest(Path('data/dev.json'))==manifest['source_sha256']


def collect():
    channels=[read_jsonl(OUT/f) if (OUT/f).exists() else [] for f in FILES]
    assert len(set(map(len,channels)))==1,'Incomplete triplet: inspect, never silently rerun'
    rows=[]
    for f,c,l in zip(*channels):
        fields=('case_id','difficulty','permutation','depth','branches','gold','gold_position','original_pos1')
        assert all(f[k]==c[k]==l[k] for k in fields+('candidate_order','prompt_sha256'))
        rows.append({k:f[k] for k in fields}|dict(F=f,C=c,L=l))
    return rows


def run():
    verify_frozen()
    if (OUT/'run_state.json').exists() or any((OUT/f).exists() for f in FILES):
        raise FileExistsError('Run already started; no silent retry')
    write_json(OUT/'run_state.json',dict(status='loading_model'))
    adapter=CalibrationAdapter('4bit-nf4','.cache/huggingface',REVISION)
    assert adapter.revision==REVISION and adapter.compute_dtype=='torch.bfloat16' and not adapter.offload
    write_json(OUT/'runtime.json',dict(revision=adapter.revision,compute_dtype=adapter.compute_dtype,
        device_map=adapter.device_map,quantization=adapter.quantization,offload=adapter.offload))
    try:
        for index,plan in enumerate(load('permutation_plan.json'),1):
            meta={k:plan[k] for k in ('case_id','difficulty','permutation','depth','branches','gold','gold_position','original_pos1')}
            write_json(OUT/'run_state.json',dict(status='evaluating',current=meta,completed=index-1))
            f,c,l=adapter.evaluate(plan['prompt'],plan['candidate_order'])
            for channel in (f,c,l):
                assert channel['rendered_prompt']==plan['rendered_prompt'] and channel['candidate_order']==plan['candidate_order']
            f.update(strict_exact_candidate=f['exact_candidate_only'],out_of_set=bool(f['out_of_set_name']))
            ranked=sorted(l['scores'],key=lambda s:-s['mean_logprob_per_token'])
            for rank,s in enumerate(ranked,1):
                s.update(rank=rank,identity=s['candidate'],absolute_candidate_position=plan['candidate_order'].index(s['candidate'])+1)
            l['gold_vs_best_wrong_margin']=margin(dict(gold=plan['gold'],L=l))
            for filename,value in zip(FILES,(f,c,l)):
                with (OUT/filename).open('a',encoding='utf-8',newline='\n') as handle:
                    handle.write(json.dumps(meta|value,ensure_ascii=False)+'\n')
                    handle.flush()
            print(f'{index}/72 {plan["case_id"]} {plan["difficulty"]} P{plan["permutation"]}: C={c["selected_candidate"]}; pos={plan["candidate_order"].index(c["selected_candidate"])+1}; GM={l["gold_vs_best_wrong_margin"]:.3f}',flush=True)
            if index%24==0:
                group=[r for r in collect() if r['difficulty']==plan['difficulty'] and r['F']['exact_candidate_only']]
                if len(group)>=12 and sum(r['F']['strict_candidate']==r['C']['selected_candidate'] for r in group)/len(group)<.8:
                    raise ValueError('Preregistered large F/C divergence stop')
        verify_frozen()
        write_json(OUT/'memory.json',adapter.memory())
        write_json(OUT/'run_state.json',dict(status='completed',triplets=72))
    except Exception:
        write_json(OUT/'failure.json',dict(error=traceback.format_exc(),state=load('run_state.json'),policy='Preserve all partial records; no automatic rerun'))
        raise
    from .report_v3_4_3 import report
    report()


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('action',choices=['prepare','run','verify','report'])
    args=parser.parse_args()
    if args.action in ('prepare','run'):
        globals()[args.action]()
    else:
        from .report_v3_4_3 import report, verify
        {'report':report,'verify':verify}[args.action]()
