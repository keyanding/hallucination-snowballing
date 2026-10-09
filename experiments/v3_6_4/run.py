"""Execute only the pre-registered free-generation stages, once."""
import importlib.metadata
import json
import traceback
from .prepare import OUT, CAP, load, write, verify
from .analyze import development
from src.calibration_choice import CalibrationAdapter
from src.calibration_v3_4_1 import REVISION
from experiments.v3_5_1.run_pilot import generate

STAGES = ('development', 'confirmation', 'order_diagnostic')


def execute(plan, dev_cases, invoke, emit):
    rows = []
    for p in plan['development']:
        row = p | invoke(p)
        emit('development',row)
        rows.append(row)
    result = development(rows,dev_cases,plan['policy'])
    assert result['complete'], 'Missing development calls'
    selected = result['selected_level']
    if selected is not None:
        for stage in ('confirmation','order_diagnostic'):
            for p in plan[stage][selected]:
                emit(stage,p | invoke(p))
    return selected


def run():
    assert not (OUT/'run_state.json').exists(), 'No reruns or overwrites'
    state = dict(status='preflight', counts={k:0 for k in STAGES})
    write('run_state.json',state)
    for k in STAGES:
        (OUT/(k+'_outputs.jsonl')).write_text('',encoding='utf-8',newline='\n')
    try:
        verify()
        adapter = CalibrationAdapter('4bit-nf4','.cache/huggingface',REVISION)
        freeze = load('decoding_freeze.json')
        assert adapter.revision == REVISION and adapter.compute_dtype == 'torch.bfloat16' and not adapter.offload
        assert adapter.tokenizer.chat_template == (OUT/'chat_template.txt').read_text(encoding='utf-8')
        versions = {n:importlib.metadata.version(n) for n in freeze['versions']}
        assert versions == freeze['versions']
        write('model_manifest.json',dict(model=freeze['model'],revision=adapter.revision,versions=versions,
              compute_dtype=adapter.compute_dtype,device_map=adapter.device_map,offload=adapter.offload,
              gpu=adapter.torch.cuda.get_device_name(0),cap=CAP,seed=42,use_cache=False,
              chat_template_sha256=freeze['chat_template_sha256']))
        verify()
        def invoke(p):
            assert adapter.render(p['prompt']) == p['rendered_prompt']
            r = generate(adapter,p['prompt'],CAP)
            assert r['rendered_sha256'] == p['rendered_sha256']
            return r
        def emit(stage,row):
            with (OUT/(stage+'_outputs.jsonl')).open('a',encoding='utf-8',newline='\n') as f:
                f.write(json.dumps(row,ensure_ascii=False)+'\n')
                f.flush()
            state['counts'][stage] += 1
            state['status'] = stage
            write('run_state.json',state)
            print(f"{stage} {state['counts'][stage]} {row['call_id']}: {row['raw_text']!r}",flush=True)
        selected = execute(load('prompt_plan.json'),load('development_cases.json'),invoke,emit)
        verify()
        state.update(status='completed', selected_level=selected, memory=adapter.memory())
        write('run_state.json',state)
    except Exception:
        state['status'] = 'INFRASTRUCTURE_FAILURE'
        write('run_state.json',state)
        write('failure.json',dict(error=traceback.format_exc()))
        write('gate.json',dict(final_decision='INFRASTRUCTURE_FAILURE',ORDER_SENSITIVE_FRONTIER=False))
        raise


if __name__ == '__main__':
    run()
