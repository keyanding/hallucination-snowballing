"""Conditional execution with persisted, unrepaired actual upstream states."""
import importlib.metadata
import json
import traceback
from .prepare import OUT, CAP, load, write, verify
from .design import pipeline
from .analyze import calibration, main_metrics
from src.calibration_choice import CalibrationAdapter
from src.calibration_v3_4_1 import REVISION
from experiments.v3_5_1.run_pilot import generate

FILES = ('calibration','main_upstream','main_downstream','pipeline_generated','shell_diagnostic','integrated')


def execute(plan, cal_cases, main_cases, invoke, emit, log_pipeline):
    rows = {k:[] for k in FILES}
    logs = []
    def call(stage,p):
        r = p | invoke(p)
        emit(stage,r)
        rows[stage].append(r)
        return r
    for p in plan['calibration']:
        call('calibration',p)
    _, gate = calibration(cal_cases,rows['calibration'])
    if not gate['passed']:
        return gate
    upstream = {}
    for stage in ('main_upstream','main_downstream'):
        for p in plan[stage]:
            r = call(stage,p)
            if p['condition']=='U-A':
                upstream[p['case_id']] = r
    by = {c['case_id']:c for c in main_cases}
    for cid in plan['pipeline_case_order']:
        p,metadata = pipeline(by[cid],upstream[cid])
        log_pipeline(metadata)
        logs.append(metadata)
        if p is not None:
            call('pipeline_generated',p | dict(upstream_source=metadata))
    _,main = main_metrics(main_cases,rows['main_upstream'],rows['main_downstream'],rows['pipeline_generated'],logs)
    assert main['complete'], 'Missing main calls or pipeline logs'
    for p in plan['shell_diagnostic']:
        call('shell_diagnostic',p)
    if main['passed']:
        for p in plan['integrated']:
            call('integrated',p)
    return gate


def run():
    assert not (OUT/'run_state.json').exists(), 'No reruns or overwrites'
    state = dict(status='preflight',counts={k:0 for k in FILES})
    write('run_state.json',state)
    for key in FILES+('pipeline_log',):
        (OUT/(key+'_outputs.jsonl' if key!='pipeline_log' else 'pipeline_log.jsonl')).write_text('',encoding='utf-8',newline='\n')
    try:
        verify()
        adapter = CalibrationAdapter('4bit-nf4','.cache/huggingface',REVISION)
        freeze = load('decoding_freeze.json')
        assert adapter.revision==REVISION and adapter.compute_dtype=='torch.bfloat16' and not adapter.offload
        assert adapter.tokenizer.chat_template==(OUT/'chat_template.txt').read_text(encoding='utf-8')
        versions = {n:importlib.metadata.version(n) for n in freeze['versions']}
        assert versions==freeze['versions']
        write('model_manifest.json',dict(revision=adapter.revision,versions=versions,compute_dtype=adapter.compute_dtype,
              device_map=adapter.device_map,offload=adapter.offload,gpu=adapter.torch.cuda.get_device_name(0)))
        verify()
        def invoke(p):
            if 'rendered_prompt' in p:
                assert adapter.render(p['prompt'])==p['rendered_prompt']
            return generate(adapter,p['prompt'],CAP)
        def emit(stage,r):
            with (OUT/(stage+'_outputs.jsonl')).open('a',encoding='utf-8',newline='\n') as f:
                f.write(json.dumps(r,ensure_ascii=False)+'\n')
                f.flush()
            state['counts'][stage] += 1
            state['status'] = stage
            write('run_state.json',state)
            print(f"{stage} {state['counts'][stage]} {r['case_id']}/{r['condition']}/{r.get('shell')}: {r['raw_text']!r}",flush=True)
        def log_pipeline(r):
            with (OUT/'pipeline_log.jsonl').open('a',encoding='utf-8',newline='\n') as f:
                f.write(json.dumps(r,ensure_ascii=False)+'\n')
                f.flush()
        gate = execute(load('prompt_plan.json'),load('calibration_cases.json'),load('main_cases.json'),invoke,emit,log_pipeline)
        write('calibration_gate.json',gate)
        verify()
        state.update(status='completed' if gate['passed'] else 'STOP_V3631_CALIBRATION_INVALID',memory=adapter.memory())
        write('run_state.json',state)
    except Exception:
        state['status']='INFRASTRUCTURE_FAILURE'
        write('run_state.json',state)
        write('failure.json',dict(error=traceback.format_exc()))
        write('gate.json',dict(final_decision='INFRASTRUCTURE_FAILURE',INTEGRATED_TWO_HOP_READY=False))
        raise


if __name__=='__main__':
    run()
