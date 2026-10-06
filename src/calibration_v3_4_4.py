"""Run full frozen development and old diagnostics, then one confirmation policy."""
import argparse
import importlib.metadata
import json
import traceback
from datetime import datetime, timezone
from pathlib import Path

from .prepare_v3_4_4 import OUT, load, verify_frozen, POLICY, REVISION
from .common import read_jsonl, digest
from .experiment_v3 import write_json
from .interface_v3_4_4 import InterfaceAdapter, parse_natural
from .analysis_v3_4_4 import analyze, select_policy, natural_gate, gold_margin

CHANNELS={'L':('listed_choice_F.jsonl','listed_choice_C.jsonl','listed_choice_scores.jsonl'),
          'N':('no_list_free.jsonl',None,'no_list_scores.jsonl'),
          'R':('record_rotation_free.jsonl',None,'record_rotation_scores.jsonl')}


def append(name, row):
    with (OUT/name).open('a',encoding='utf-8',newline='\n') as f:
        f.write(json.dumps(row,ensure_ascii=False)+'\n')
        f.flush()


def collect():
    rows=[]
    for interface,files in CHANNELS.items():
        channels=[read_jsonl(OUT/f) if f and (OUT/f).exists() else [] for f in files]
        assert len(channels[0])==len(channels[2])
        if interface=='L':
            assert len(channels[0])==len(channels[1])
        for i,f in enumerate(channels[0]):
            s=channels[2][i]
            c=channels[1][i] if interface=='L' else None
            assert f['plan_id']==s['plan_id'] and f['prompt_sha256']==s['prompt_sha256']
            if c:
                assert c['plan_id']==f['plan_id'] and c['prompt_sha256']==f['prompt_sha256']
            meta={k:f[k] for k in ('plan_id','cohort','case_id','difficulty','depth','branches','interface','rotation','gold','candidate_order','record_order')}
            rows.append(meta|dict(F=f,C=c,S=s))
    assert len({r['plan_id'] for r in rows})==len(rows)
    return rows


def smoke_and_harness(adapter):
    # Independent format tasks: synthetic names and identifiers never used in study.
    names=['Ada Vale','Ben Cove','Cara Reed','Dion Lake']
    prompts=[f'Record X1 names Ada Vale.\nRecord X2 names Ben Cove.\nRecord X3 names Cara Reed.\nRecord X4 names Dion Lake.\nFilm SMOKE{i} has credited-director link X{i}.\nWho is the credited director of Film SMOKE{i}? Output only the person\'s name.' for i in range(1,5)]
    smoke=[]
    cap=96
    for p in prompts:
        f,_,s=adapter.evaluate(p,names,listed=False,free_cap=96)
        smoke.append(dict(cap=96,F=f,S=s))
    if any(r['F']['truncated'] for r in smoke):
        cap=192
        for p in prompts:
            f,_,s=adapter.evaluate(p,names,listed=False,free_cap=192)
            smoke.append(dict(cap=192,F=f,S=s))
    write_json(OUT/'format_smoke.json',dict(tasks=smoke,selected_NR_cap=cap,decision_rule=POLICY['cap_smoke']))
    # The first frozen v3.4.3 rendering; compare complete raw outputs and scores.
    oldplans=json.loads(Path('results/calibration_v3_4_3/permutation_plan.json').read_text(encoding='utf-8'))
    p=oldplans[0]
    f,c,s=adapter.evaluate(p['prompt'],p['candidate_order'])
    oldfiles=['free_channel.jsonl','constrained_channel.jsonl','likelihood_channel.jsonl']
    from .calibration_v3_4_1 import FILES
    previous=[read_jsonl(Path('results/calibration_v3_4_3')/name)[0] for name in FILES]
    comparisons=dict(rendered=f['rendered_prompt']==previous[0]['rendered_prompt'],F=f['raw_text']==previous[0]['raw_text'],
        C=c['raw_text']==previous[1]['raw_text'],scores=s['scores']==previous[2]['scores'])
    # Historical rows include rank/position metadata: compare numerical token scores.
    comparisons['scores']=all(a['token_logprobs']==b['token_logprobs'] and a['candidate']==b['candidate'] for a,b in zip(s['scores'],previous[2]['scores']))
    write_json(OUT/'harness_replay.json',dict(plan=p,comparisons=comparisons,F=f,C=c,S=s))
    assert all(comparisons.values()), 'Frozen harness failed before experimental calls'
    write_json(OUT/'decoding_freeze.json',dict(created_utc=datetime.now(timezone.utc).isoformat(),NR_max_new_tokens=cap,L_max_new_tokens=96,
        smoke_sha256=digest(OUT/'format_smoke.json'),harness_sha256=digest(OUT/'harness_replay.json'),aliases={},
        completed_before_experimental_calls=True))
    return cap


def evaluate_plan(adapter,p,cap):
    f,c,s=adapter.evaluate(p['prompt'],p['candidate_order'],listed=p['interface']=='L',free_cap=96 if p['interface']=='L' else cap)
    assert f['rendered_prompt']==p['rendered_prompt'] and s['prompt_sha256']==p['prompt_sha256']
    meta={k:p[k] for k in ('plan_id','cohort','case_id','difficulty','depth','branches','interface','rotation','gold','candidate_order','record_order')}
    if c:
        assert c['exact_allowed_candidate'] and c['all_candidates_reachable']
    s['gold_vs_best_wrong_margin']=gold_margin(dict(gold=p['gold'],S=s))
    for file,value in zip(CHANNELS[p['interface']],(f,c,s)):
        if file:
            append(file,meta|value)
    return f,c


def run():
    verify_frozen()
    assert not (OUT/'run_state.json').exists(), 'No silent reruns; inspect partial records first'
    write_json(OUT/'run_state.json',dict(status='loading_model'))
    adapter=InterfaceAdapter('4bit-nf4','.cache/huggingface',REVISION)
    assert adapter.revision==REVISION and adapter.compute_dtype=='torch.bfloat16' and not adapter.offload
    write_json(OUT/'runtime.json',dict(revision=adapter.revision,compute_dtype=adapter.compute_dtype,device_map=adapter.device_map,
        quantization=adapter.quantization,offload=adapter.offload,versions={n:importlib.metadata.version(n) for n in ['torch','transformers','bitsandbytes','accelerate','numpy']},
        chat_template_sha256=digest(OUT/'chat_template.txt')))
    try:
        cap=smoke_and_harness(adapter)
        plans=read_jsonl(OUT/'prompt_plan.jsonl')
        development=[p for p in plans if p['cohort'] in ('development','old')]
        assert len(development)==738
        for i,p in enumerate(development,1):
            f,c=evaluate_plan(adapter,p,cap)
            write_json(OUT/'run_state.json',dict(status='development',completed=i,total=738,last=p['plan_id']))
            print(f'{i}/738 {p["plan_id"]}: {f["category"]} {f["identity"]}',flush=True)
        verify_frozen()
        rows=collect()
        metrics=analyze(rows)
        write_json(OUT/'development_metrics.json',metrics)
        selection=select_policy(metrics,rows)
        selection.update(created_utc=datetime.now(timezone.utc).isoformat(),development_metrics_sha256=digest(OUT/'development_metrics.json'),confirmation_calls_so_far=0)
        write_json(OUT/'policy_selection.json',selection)
        (OUT/'interface_policy.md').write_text('# Development-only interface policy\n\nFrozen before confirmation inference.\n\n```json\n'+json.dumps(selection,indent=2)+'\n```\n',encoding='utf-8',newline='\n')
        confirmation=[p for p in plans if p['cohort']=='confirmation' and p['difficulty']==selection['difficulty'] and (p['interface']!='R' or selection['confirmation_with_R'])] if selection['route'] else []
        assert len(confirmation)==(144 if selection['confirmation_with_R'] else 80) if selection['route'] else not confirmation
        for i,p in enumerate(confirmation,1):
            f,c=evaluate_plan(adapter,p,cap)
            write_json(OUT/'run_state.json',dict(status='confirmation',completed=i,total=len(confirmation),last=p['plan_id']))
            print(f'confirmation {i}/{len(confirmation)} {p["plan_id"]}: {f["category"]} {f["identity"]}',flush=True)
        verify_frozen()
        rows=collect()
        write_json(OUT/'metrics.json',analyze(rows))
        write_json(OUT/'memory.json',adapter.memory())
        write_json(OUT/'run_state.json',dict(status='completed',development_renderings=648,old_renderings=90,confirmation_renderings=len(confirmation),
            total_renderings=len(rows),main_channel_evaluations=sum(3 if r['interface']=='L' else 2 for r in rows),
            smoke_channel_evaluations=len(load('format_smoke.json')['tasks'])*2,harness_channel_evaluations=3))
    except Exception:
        write_json(OUT/'failure.json',dict(error=traceback.format_exc(),state=load('run_state.json')))
        raise


if __name__=='__main__':
    run()
