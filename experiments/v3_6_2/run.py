"""One-shot frozen392-call experiment with explicit infrastructure failures."""
import importlib.metadata
import json
import traceback
from .prepare import OUT,CAP,load,write,verify
from src.calibration_choice import CalibrationAdapter
from src.calibration_v3_4_1 import REVISION
from experiments.v3_5_1.run_pilot import generate


def execute(plan,invoke,emit):
    for stage in ('main','position_diagnostic'):
        for row in plan[stage]:
            emit(stage,row|invoke(row))


def run():
    assert not (OUT/'run_state.json').exists(),'No reruns or overwrites'
    state=dict(status='preflight',counts=dict(main=0,position_diagnostic=0))
    write('run_state.json',state)
    for stage in state['counts']:
        (OUT/(stage+'_outputs.jsonl')).write_text('',encoding='utf-8',newline='\n')
    try:
        verify()
        adapter=CalibrationAdapter('4bit-nf4','.cache/huggingface',REVISION)
        freeze=load('decoding_freeze.json')
        assert adapter.revision==REVISION and adapter.compute_dtype=='torch.bfloat16' and not adapter.offload
        assert adapter.tokenizer.chat_template==(OUT/'chat_template.txt').read_text(encoding='utf-8')
        versions={n:importlib.metadata.version(n) for n in freeze['versions']}
        assert versions==freeze['versions']
        write('model_manifest.json',dict(revision=adapter.revision,compute_dtype=adapter.compute_dtype,
              versions=versions,device_map=adapter.device_map,offload=adapter.offload,gpu=adapter.torch.cuda.get_device_name(0)))
        verify()

        def invoke(row):
            assert adapter.render(row['prompt'])==row['rendered_prompt']
            result=generate(adapter,row['prompt'],CAP)
            assert result['input_tokens']==row['input_tokens']
            return result

        def emit(stage,row):
            with (OUT/(stage+'_outputs.jsonl')).open('a',encoding='utf-8',newline='\n') as f:
                f.write(json.dumps(row,ensure_ascii=False)+'\n')
                f.flush()
            state['counts'][stage]+=1
            state['status']=stage
            write('run_state.json',state)
            print(f"{stage} {state['counts'][stage]} {row['case_id']}/K{row['k']}/{row['condition']}/{row['position_band']}: {row['raw_text']!r}",flush=True)

        execute(load('prompt_plan.json'),invoke,emit)
        verify()
        state.update(status='completed',memory=adapter.memory())
        write('run_state.json',state)
    except Exception:
        state['status']='INFRASTRUCTURE_FAILURE'
        write('run_state.json',state)
        write('failure.json',dict(error=traceback.format_exc()))
        write('gate.json',dict(final_decision='INFRASTRUCTURE_FAILURE',context_interpretation_allowed=False))
        raise


if __name__=='__main__':
    run()
