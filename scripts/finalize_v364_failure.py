"""Close the observed zero-call native crash; never loads a model or changes the freeze.

The frozen generic report prints zero counts against planned denominators on an
incomplete run. This post-run presentation supplement explicitly labels these
metrics UNRUN; it changes no inference source, scientific gate or frozen input.
"""
import json
from pathlib import Path
from transformers import AutoTokenizer
from experiments.v3_6_4.prepare import OUT, load, write, text, verify, MODEL, REVISION
from experiments.v3_6_4.design import LEVELS, SIZES, render, sha


def finalize():
    verify()
    gate = load('gate.json')
    assert gate['final_decision'] == 'INFRASTRUCTURE_FAILURE'
    assert all(n == 0 for n in gate['calls'].values())
    assert load('failure.json')['windows_exception_code'] == '0xc0000005'
    for stage in ('development','confirmation','order_diagnostic'):
        assert (OUT/(stage+'_outputs.jsonl')).read_bytes() == b''
    plan = load('prompt_plan.json')
    cases = {c['case_id']:c for c in load('development_cases.json')+load('confirmation_cases.json')}
    mappings = load('downstream_compatibility.json')
    prompts = plan['development']+[p for k in LEVELS for p in plan['confirmation'][k]+plan['order_diagnostic'][k]]
    tok = AutoTokenizer.from_pretrained(MODEL,revision=REVISION,cache_dir='.cache/huggingface',local_files_only=True)
    for p in prompts:
        c = cases[p['case_id']]
        assert p['expected'] in p['state_universe'] and len(p['state_universe']) == SIZES[p['level']]
        assert p['downstream_compatibility'] == {s:mappings[p['case_id']][s] for s in p['state_universe']}
        rebuilt = render(c,p['level'],p['permutation'])
        assert all(p[k] == v for k,v in rebuilt.items())
        rendered = tok.apply_chat_template([dict(role='user',content=p['prompt'])],tokenize=False,add_generation_prompt=True,enable_thinking=False)
        assert rendered == p['rendered_prompt'] and sha(rendered) == p['rendered_sha256']
        assert 'OUTCOME_' not in p['prompt']
    assert len(prompts) == 168
    for k in LEVELS:
        m = load('development_metrics.json')['levels'][k]
        assert not m['evaluated'] and not m['complete'] and m['qualified_wrong_rate'] is None
    assert not load('confirmation_metrics.json')['evaluated']
    assert not load('order_diagnostic_metrics.json')['evaluated']
    summary = '''# v3.6.4 — INFRASTRUCTURE_FAILURE

用户确认的计数规则已在推理前写入并冻结：Valid 只计未截断的 GOLD/TRACEABLE_WRONG；OUT_OF_UNIVERSE、INVALID 和所有截断调用均不计入 Valid。TRACEABLE_WRONG 必须是 case/difficulty 的提示中明确存在的 exact 非gold状态，并已有预定义 downstream mapping。EASY/MID/HARD 的全集分别为3/5/8个状态。开发与确认使用同一实现。

模型在加载权重阶段发生原生进程崩溃，尚未执行任何生成调用。Windows Application Error 1000 记录时间2026-10-09 08:56:47（Asia/Shanghai），模块 torch_cpu.dll，异常码0xc0000005。Python层未捕获异常堆栈，进程退出码1。该日志定位到原生访问冲突，不能据此断言内存不足、显卡故障或权重损坏。

| 阶段 | 已执行调用 | 计划调用 | 研究指标 |
|---|---:|---:|---|
| 开发 EASY | 0 | 24 | 未评估 |
| 开发 MID | 0 | 24 | 未评估 |
| 开发 HARD | 0 | 24 | 未评估 |
| 独立确认 | 0 | 条件触发后24 | 未评估 |
| 顺序诊断 | 0 | 条件触发后8 | 未评估 |
| 下游传播 | 0 | 0 | 本版不测试 |

最终标签是 INFRASTRUCTURE_FAILURE，**不是 NO_NATURAL_ERROR_FRONTIER**。尚未选择难度；没有正确率、错误产出率或顺序稳定性观察。指标文件中的计数0表示没有记录，denominator=24仅是预注册计划分母，evaluated=false/complete=false，错误率为null；不能将其解释为0/24错误率。ORDER_SENSITIVE_FRONTIER=false同时伴随evaluated=false，不表示顺序稳定。

157项测试通过；48个基础案例、1152个新标识符、168个备选提示及映射已冻结。未修复或放宽阈值，没有重试、替换案例、cap sweep或下游调用。恢复模型加载应作为单独的环境排障；任何恢复执行都应保留此次失败记录和冻结输入，不覆盖它。

这次尝试不增加关于自然第一跳错误、自然传播、注入/自然等价、真实世界幻觉、SHAR/HalluSE或模型能力的科学证据。
'''
    for name in ('README.md','diagnosis.md','interpretation.md'):
        text(name,summary+'\n证据：[故障记录](failure.json)、[Windows事件](windows_crash_event.json)、[门槛](gate.json)、[预注册](pre_registration.md)、[原始提示计划](prompt_plan.json)。\n')
    text('inspection.md',summary+'\n## 问题与输出\n\n没有实际调用，所以没有模型回答或逐调用子问题。所有预定问题均为 `What state is associated with ENTITY_...?`，完整提示见 prompt_plan.json。B→C 只预先建表，未提问。三个 outputs.jsonl 和 parsed_outcomes.jsonl 均为空，禁止伪造输出。\n')
    pre = (OUT/'design_audit.pre_inference.md').read_text(encoding='utf-8')
    text('design_audit.md',pre+'\n## Post-run infrastructure failure audit\n\n'+summary)
    text('CHANGELOG.md','# v3.6.4 CHANGELOG\n\n用户确认口径后冻结全部输入，157项测试通过。首次运行于模型加载阶段原生崩溃；零生成调用，记录INFRASTRUCTURE_FAILURE。补充未运行展示，避免将零条记录误读为零错误率；未改冻结代码、门槛或输入。\n')
    (OUT/'tests.pre_inference.log').write_bytes(Path('experiments/v3_6_4/pre_inference_tests.log').read_bytes())
    required = 'README.md spec.md pre_registration.md prior_findings_review.md design_audit.pre_inference.md design_audit.md development_cases.json confirmation_cases.json downstream_compatibility.json identifier_tokenization_audit.json prompt_plan.json prompt_diff_audit.md decoding_freeze.json model_manifest.json development_outputs.jsonl development_metrics.json confirmation_outputs.jsonl confirmation_metrics.json order_diagnostic_outputs.jsonl order_diagnostic_metrics.json parsed_outcomes.jsonl gate.json diagnosis.md interpretation.md inspection.md CHANGELOG.md'.split()
    assert all((OUT/p).is_file() for p in required)
    assert (OUT/'design_audit.md').read_bytes().startswith((OUT/'design_audit.pre_inference.md').read_bytes())
    verify()
    write('independent_verification.json',dict(frozen_inputs_unchanged=True,prior_result_files_unchanged=len(load('manifest.json')['prior_artifacts']),
          potential_prompts_rebuilt=168,tokenizer_only_no_model_loaded=True,required_artifacts_present=len(required),
          raw_model_calls=0,scientific_outcomes_evaluated=False,stop='INFRASTRUCTURE_FAILURE',
          tests_passed_before_inference=157,post_run_presentation_supplement=__file__,frozen_report_source_unchanged=True))
    print('Verified immutable freeze,168 prompt renders, required artifacts and zero-call infrastructure failure.')


if __name__ == '__main__':
    finalize()
