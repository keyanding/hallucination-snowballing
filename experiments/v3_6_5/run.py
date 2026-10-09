"""Free-generation only; classify development before non-gating diagnostics."""
import importlib.metadata
import json
import traceback
from .prepare import OUT,CAP,load,write,verify
from .analyze import metrics
from src.calibration_choice import CalibrationAdapter
from src.calibration_v3_4_1 import REVISION
from experiments.v3_5_1.run_pilot import generate

STAGES=('development','presentation_diagnostic','confirmation')


def execute(plan,cases,aliases,invoke,emit,save_development):
    rows=[]
    for p in plan['development']:
        r=p|invoke(p);emit('development',r);rows.append(r)
    m=metrics(rows,[c['case_id'] for c in cases],aliases)
    assert m['complete']
    save_development(m)
    if m['passed'] or plan['policy']['diagnostic_on_development_failure']:
        for p in plan['presentation_diagnostic']:emit('presentation_diagnostic',p|invoke(p))
    if m['passed']:
        for p in plan['confirmation']:emit('confirmation',p|invoke(p))
    return m['passed']


def run():
    assert not (OUT/'run_state.json').exists(),'No reruns or overwrites'
    state=dict(status='preflight',counts={s:0 for s in STAGES})
    write('run_state.json',state)
    for s in STAGES:(OUT/(s+'_outputs.jsonl')).write_text('',encoding='utf-8',newline='\n')
    try:
        verify()
        adapter=CalibrationAdapter('4bit-nf4','.cache/huggingface',REVISION)
        freeze=load('decoding_freeze.json')
        assert adapter.revision==REVISION and adapter.compute_dtype=='torch.bfloat16' and not adapter.offload
        assert adapter.tokenizer.chat_template==(OUT/'chat_template.txt').read_text(encoding='utf-8')
        versions={n:importlib.metadata.version(n) for n in freeze['versions']}
        assert versions==freeze['versions']
        write('model_manifest.json',dict(model=freeze['model'],revision=REVISION,versions=versions,compute_dtype=adapter.compute_dtype,
              device_map=adapter.device_map,offload=adapter.offload,gpu=adapter.torch.cuda.get_device_name(0),cap=CAP,seed=42,use_cache=False,
              chat_template_sha256=freeze['chat_template_sha256']))
        verify()
        def invoke(p):
            assert adapter.render(p['prompt'])==p['rendered_prompt']
            return generate(adapter,p['prompt'],CAP)
        def emit(stage,r):
            with (OUT/(stage+'_outputs.jsonl')).open('a',encoding='utf-8',newline='\n') as f:
                f.write(json.dumps(r,ensure_ascii=False)+'\n');f.flush()
            state['counts'][stage]+=1;state['status']=stage;write('run_state.json',state)
            print(f"{stage} {state['counts'][stage]} {r['case_id']}: {r['raw_text']!r}",flush=True)
        passed=execute(load('prompt_plan.json'),load('development_cases.json'),load('alias_registry.json'),invoke,emit,lambda m:write('development_classification.before_diagnostic.json',m))
        verify()
        state.update(status='completed',development_passed=passed,memory=adapter.memory());write('run_state.json',state)
    except Exception:
        state['status']='INFRASTRUCTURE_FAILURE';write('run_state.json',state)
        write('failure.json',dict(error=traceback.format_exc()))
        write('gate.json',dict(final_decision='INFRASTRUCTURE_FAILURE',PRESENTATION_SENSITIVE='not_evaluated'))
        raise


if __name__=='__main__':run()
