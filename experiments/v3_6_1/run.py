"""One-shot 270-call execution; Stage C is not gated by Stage B performance."""
import importlib.metadata
import json
import traceback
from .prepare import OUT, CAP, load, write, verify
from src.calibration_choice import CalibrationAdapter
from src.calibration_v3_4_1 import REVISION
from experiments.v3_5_1.run_pilot import generate

STAGES = ('stage_b', 'stage_c', 'unmapped', 'record_order')


def execute(plans, invoke, emit):
    for stage in STAGES:
        for row in plans[stage]:
            emit(stage, row | invoke(row))


def run():
    verify()
    assert not (OUT/'run_state.json').exists(), 'No rerun or overwrite'
    state = dict(status='loading_model', counts={k:0 for k in STAGES})
    write('run_state.json', state)
    for stage in STAGES:
        (OUT/(stage+'_outputs.jsonl')).write_text('', encoding='utf-8', newline='\n')
    try:
        adapter = CalibrationAdapter('4bit-nf4', '.cache/huggingface', REVISION)
        freeze = load('decoding_freeze.json')
        assert adapter.revision == REVISION and adapter.compute_dtype == 'torch.bfloat16' and not adapter.offload
        assert adapter.tokenizer.chat_template == (OUT/'chat_template.txt').read_text(encoding='utf-8')
        versions = {n:importlib.metadata.version(n) for n in freeze['versions']}
        assert versions == freeze['versions']
        write('model_manifest.json', dict(revision=adapter.revision, compute_dtype=adapter.compute_dtype,
              device_map=adapter.device_map, offload=adapter.offload, versions=versions, gpu=adapter.torch.cuda.get_device_name(0)))
        verify()

        def invoke(row):
            assert adapter.render(row['prompt']) == row['rendered_prompt']
            return generate(adapter, row['prompt'], CAP)

        def emit(stage, row):
            with (OUT/(stage+'_outputs.jsonl')).open('a', encoding='utf-8', newline='\n') as f:
                f.write(json.dumps(row, ensure_ascii=False)+'\n')
                f.flush()
            state['counts'][stage] += 1
            state['status'] = stage
            write('run_state.json', state)
            print(f"{stage} {state['counts'][stage]} {row['case_id']}/{row['family']}/{row['condition']}: {row['raw_text']!r}", flush=True)

        execute({k:load(k+'_prompt_plan.json') for k in STAGES}, invoke, emit)
        verify()
        state.update(status='completed', memory=adapter.memory())
        write('run_state.json', state)
    except Exception:
        state['status'] = 'INFRASTRUCTURE_FAILURE'
        write('run_state.json', state)
        write('failure.json', dict(error=traceback.format_exc()))
        write('gate.json', dict(stage_b_completed=state['counts']['stage_b'] == 160,
              stage_b_best_descriptive_condition=None, stage_c_pass=None, record_order_diagnostic_pass=None,
              stronger_model_diagnostic_status='STRONGER_MODEL_DIAGNOSTIC_NOT_RUN', final_decision='INFRASTRUCTURE_FAILURE'))
        raise


if __name__ == '__main__':
    run()
