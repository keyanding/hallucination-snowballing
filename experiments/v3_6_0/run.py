"""One-shot sequential calibration gate followed by conditional frozen main."""
import importlib.metadata
import traceback
from .prepare import OUT, CAP, load, write, verify, digest
from .analyze import calibration_metrics
from src.calibration_choice import CalibrationAdapter
from src.calibration_v3_4_1 import REVISION
from experiments.v3_5_1.run_pilot import generate


def execute(plan, invoke, emit):
    calibration = []
    for row in plan['calibration']:
        result = row | invoke(row)
        emit('calibration_outputs.jsonl', result)
        calibration.append(result)
    _, metrics = calibration_metrics(load('calibration_cases.json'), calibration)
    write('calibration_gate.json', metrics)
    if not metrics['passed']:
        return False
    for row in plan['main']:
        emit('main_outputs.jsonl', row | invoke(row))
    return True


def run():
    import json
    verify()
    assert not (OUT/'run_state.json').exists(), 'No reruns or overwrites'
    state = dict(status='loading_model', calibration_calls=0, main_calls=0)
    write('run_state.json', state)
    for name in ('calibration_outputs.jsonl', 'main_outputs.jsonl'):
        (OUT/name).write_text('', encoding='utf-8', newline='\n')
    try:
        adapter = CalibrationAdapter('4bit-nf4', '.cache/huggingface', REVISION)
        freeze = load('decoding_freeze.json')
        assert adapter.revision == REVISION and adapter.compute_dtype == 'torch.bfloat16' and not adapter.offload
        assert adapter.tokenizer.chat_template == (OUT/'chat_template.txt').read_text(encoding='utf-8')
        versions = {n:importlib.metadata.version(n) for n in freeze['versions']}
        assert versions == freeze['versions']
        write('model_manifest.json', dict(revision=adapter.revision, compute_dtype=adapter.compute_dtype, device_map=adapter.device_map, offload=adapter.offload, versions=versions, gpu=adapter.torch.cuda.get_device_name(0)))
        verify()

        def invoke(row):
            assert adapter.render(row['prompt']) == row['rendered_prompt']
            return generate(adapter, row['prompt'], CAP)

        def emit(name, row):
            with (OUT/name).open('a', encoding='utf-8', newline='\n') as f:
                f.write(json.dumps(row, ensure_ascii=False)+'\n')
                f.flush()
            key = 'calibration_calls' if name.startswith('calibration') else 'main_calls'
            state[key] += 1
            state['status'] = key
            write('run_state.json', state)
            print(f"{key} {state[key]} {row['case_id']} {row['condition']}: {row['raw_text']!r}", flush=True)

        passed = execute(load('prompt_plan.json'), invoke, emit)
        verify()
        state.update(status='completed' if passed else 'STOP_ASSAY_INVALID', memory=adapter.memory())
        write('run_state.json', state)
    except Exception:
        state['status'] = 'runtime_failure'
        write('run_state.json', state)
        write('failure.json', dict(error=traceback.format_exc()))
        raise


if __name__ == '__main__':
    run()
