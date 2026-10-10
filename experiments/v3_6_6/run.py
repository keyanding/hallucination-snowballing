"""Durable one-attempt collection; no scientific early stopping or auto-resume."""
import importlib.metadata
import json
import os
import traceback
from .prepare import OUT,load,write,verify
from .design import first_parse,route,sha
from src.calibration_choice import CalibrationAdapter
from src.calibration_v3_4_1 import REVISION
from experiments.v3_5_1.run_pilot import generate

STAGES=('first_hop','natural_downstream','controlled','order_diagnostic')


def execute(cases,identity,modules,schedule,plans,invoke,emit,event,pipeline):
    cby={c['case_id']:c for c in cases};seen=set();first={};routes={}
    def call(stage,p,cid):
        assert cid not in seen,'Duplicate dispatch forbidden'
        seen.add(cid);event(dict(status='CALL_STARTED',stage=stage,call_id=cid,case_id=p['case_id'],prompt_hash=p['text_sha256']))
        r=p|invoke(p)|dict(call_id=cid,stage=stage)
        emit(stage,r)
        event(dict(status='CALL_COMPLETED',stage=stage,call_id=cid,case_id=p['case_id'],raw_hash=r['raw_sha256']))
        return r
    for cid in schedule['first_hop']:
        r=call('first_hop',plans[cid+'/FIRST'],cid+'/FIRST');first[cid]=r
        event(dict(status='FIRST_CLASSIFIED',case_id=cid,raw_hash=r['raw_sha256'],parsed=first_parse(r,cby[cid])))
    for cid in schedule['natural_downstream']:
        module,p,log=route(cby[cid],first[cid],identity,modules)
        log['identity_map_hash']=sha(json.dumps(identity[cid],sort_keys=True,ensure_ascii=False))
        pipeline(log);routes[cid]=module
        if p is not None:
            selected=plans[module['module_id']+'/'+p['arm']]
            assert selected['supplied_state']==log['supplied_state'] and selected['text_sha256']==log['actual_prompt_hash']
            call('natural_downstream',selected|dict(upstream_provenance=log),cid+'/NATURAL')
    for slot in schedule['controlled']:
        cid=slot['case_id'];arm=slot['arm'];module=routes[cid]
        call('controlled',plans[module['module_id']+'/'+arm],cid+'/CONTROL_'+arm)
    for cid in schedule['order_diagnostic']:
        call('order_diagnostic',plans[cid+'/DIAGNOSTIC'],cid+'/DIAGNOSTIC')
    return len(seen)


def append(name,row):
    with (OUT/name).open('a',encoding='utf-8',newline='\n') as f:
        f.write(json.dumps(row,ensure_ascii=False)+'\n');f.flush();os.fsync(f.fileno())


def run():
    assert not (OUT/'run_state.json').exists(),'Existing attempt; no resume or duplicate requests'
    state=dict(status='preflight',technical_status='NONE',counts={s:0 for s in STAGES})
    write('run_state.json',state)
    for name in [s+'_raw.jsonl' for s in STAGES]+['pipeline_log.jsonl','call_journal.jsonl']:
        with (OUT/name).open('x',encoding='utf-8'):pass
    try:
        verify()
        adapter=CalibrationAdapter('4bit-nf4','.cache/huggingface',REVISION);freeze=load('decoding_freeze.json')
        versions={n:importlib.metadata.version(n) for n in freeze['versions']}
        if not(adapter.revision==REVISION and adapter.compute_dtype=='torch.bfloat16' and not adapter.offload and versions==freeze['versions'] and sha(adapter.tokenizer.chat_template)==freeze['chat_template_sha256']):
            raise RuntimeError('Runtime/model/template drift')
        write('model_manifest.json',dict(model=freeze['model'],revision=REVISION,versions=versions,compute_dtype=adapter.compute_dtype,
              device_map=adapter.device_map,offload=adapter.offload,gpu=adapter.torch.cuda.get_device_name(0),chat_template_sha256=sha(adapter.tokenizer.chat_template)))
        plans={p['plan_id']:p for p in [json.loads(s) for s in (OUT/'prompt_plan.jsonl').read_text(encoding='utf-8').splitlines()]}
        def invoke(p):
            assert adapter.render(p['prompt'])==p['rendered_prompt']
            assert adapter.tokenizer.encode(p['rendered_prompt'],add_special_tokens=False)==p['input_token_ids']
            return generate(adapter,p['prompt'],p['cap'])
        def emit(stage,r):
            append(stage+'_raw.jsonl',r);state['counts'][stage]+=1;state['status']=stage;write('run_state.json',state)
            print(f"{stage} {state['counts'][stage]} {r['call_id']}: {r['raw_text']!r}",flush=True)
        count=execute(load('cases.json'),load('identity_state_map.json'),load('downstream_modules.json'),load('call_schedule.json'),plans,
                      invoke,emit,lambda r:append('call_journal.jsonl',r),lambda r:append('pipeline_log.jsonl',r))
        verify();state.update(status='completed',total_calls=count,memory=adapter.memory());write('run_state.json',state)
    except Exception as e:
        status='STRUCTURAL_FAILURE' if isinstance(e,AssertionError) else 'INFRASTRUCTURE_FAILURE'
        state.update(status=status,technical_status=status);write('run_state.json',state)
        write('failure.json',dict(status=status,error=traceback.format_exc(),automatic_retry=False));raise


if __name__=='__main__':run()
