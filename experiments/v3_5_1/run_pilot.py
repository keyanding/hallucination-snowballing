"""One-shot greedy pilot: independent checks then all72 frozen main calls."""
import importlib.metadata
import json
import time
import traceback
from datetime import datetime,timezone
from pathlib import Path
from src.calibration_choice import CalibrationAdapter
from src.calibration_v3_4_1 import REVISION
from src.experiment_v3 import write_json
from .build_cases import OUT,load,verify
from .render_prompts import sha
from .validate_cases import normalize


def append(name,row):
    with (OUT/name).open('a',encoding='utf-8',newline='\n') as f:
        f.write(json.dumps(row,ensure_ascii=False)+'\n');f.flush()


def generate(adapter,prompt,cap):
    tc=adapter.torch
    rendered=adapter.render(prompt)
    ids=adapter.tokenizer.encode(rendered,add_special_tokens=False)
    inputs=dict(input_ids=tc.tensor([ids],device=adapter.model.device),attention_mask=tc.ones((1,len(ids)),dtype=tc.long,device=adapter.model.device))
    tc.manual_seed(42);tc.cuda.synchronize();start=time.perf_counter()
    with tc.inference_mode():
        output=adapter.model.generate(**inputs,do_sample=False,temperature=None,top_k=None,top_p=None,use_cache=False,
            max_new_tokens=cap,eos_token_id=adapter.tokenizer.eos_token_id,pad_token_id=adapter.tokenizer.eos_token_id)
    tc.cuda.synchronize()
    new=output[0,len(ids):].tolist();raw=adapter.tokenizer.decode(new,skip_special_tokens=True)
    truncated=len(new)>=cap and new[-1]!=adapter.tokenizer.eos_token_id
    return dict(prompt=prompt,rendered_prompt=rendered,rendered_sha256=sha(rendered),input_tokens=len(ids),
        output_token_ids=new,raw_text=raw,raw_sha256=sha(raw),output_tokens=len(new),max_new_tokens=cap,
        truncated=truncated,stop_reason='TOKEN_CAP' if truncated else 'EOS',seed=42,
        new_chat=True,use_cache=False,constrained=False,created_utc=datetime.now(timezone.utc).isoformat(),latency_seconds=time.perf_counter()-start)


def run():
    verify()
    assert not (OUT/'run_state.json').exists(),'No automatic reruns or output overwrite'
    state=dict(status='loading_model',main_calls=0,auxiliary_calls=0,capability_pass=False)
    write_json(OUT/'run_state.json',state)
    try:
        adapter=CalibrationAdapter('4bit-nf4','.cache/huggingface',REVISION)
        assert adapter.revision==REVISION and adapter.compute_dtype=='torch.bfloat16' and not adapter.offload
        runtime=dict(revision=adapter.revision,compute_dtype=adapter.compute_dtype,device_map=adapter.device_map,offload=adapter.offload,
            versions={n:importlib.metadata.version(n) for n in ('torch','transformers','bitsandbytes','accelerate','numpy')},
            gpu=adapter.torch.cuda.get_device_name(0),chat_template_sha256=sha(adapter.tokenizer.chat_template))
        m=load('model_manifest.json');m['runtime']=runtime;write_json(OUT/'model_manifest.json',m)
        aux=load('auxiliary_plan.json')
        def auxiliary(task,cap,kind):
            r=generate(adapter,task['prompt'],cap)
            passed=not r['truncated'] and normalize(r['raw_text']) in {normalize(a) for a in task.get('aliases',[task['expected']])}
            row=task|r|dict(kind=kind,passed=passed)
            append('capability_checks.jsonl',row)
            state['auxiliary_calls']+=1;write_json(OUT/'run_state.json',state)
            print(f'aux {state["auxiliary_calls"]}: {task["check_id"]} {r["raw_text"]!r} pass={passed}',flush=True)
            return row
        smoke=[auxiliary(t,96,'format_smoke') for t in aux['smoke']]
        cap=192 if any(r['truncated'] for r in smoke) else 96
        if cap==192:smoke=[auxiliary(t,192,'format_smoke') for t in aux['smoke']]
        assert all(r['passed'] for r in smoke),'Independent format check failed'
        repeat=auxiliary(aux['smoke'][0],cap,'deterministic_replay')
        assert repeat['output_token_ids']==smoke[0]['output_token_ids'],'Inference replay differs'
        write_json(OUT/'decoding_freeze.json',dict(selected_cap=cap,seed=42,greedy=True,use_cache=False,constrained=False,
            created_before_main=True,created_utc=datetime.now(timezone.utc).isoformat(),replay_token_exact=True))
        m=load('model_manifest.json');m['main_max_new_tokens']=cap;write_json(OUT/'model_manifest.json',m)
        for task in aux['capability']:
            r=auxiliary(task,cap,task['kind'])
            assert r['passed'],'Independent capability failure: '+task['check_id']
        state.update(status='main',capability_pass=True);write_json(OUT/'run_state.json',state)
        verify()
        for p in load('prompt_plan.json'):
            r=generate(adapter,p['prompt'],cap)
            assert r['rendered_prompt']==p['rendered_prompt'] and r['rendered_sha256']==p['rendered_sha256']
            append('outputs.jsonl',p|r)
            state['main_calls']+=1;state['last']=dict(case_id=p['case_id'],condition=p['condition']);write_json(OUT/'run_state.json',state)
            print(f'{state["main_calls"]}/72 {p["case_id"]}/{p["condition"]}: {r["raw_text"]!r}',flush=True)
        verify()
        state.update(status='completed',memory=adapter.memory());write_json(OUT/'run_state.json',state)
    except Exception:
        state['status']='stopped_invalid';write_json(OUT/'run_state.json',state)
        write_json(OUT/'failure.json',dict(error=traceback.format_exc(),state=state))
        raise


if __name__=='__main__':run()
