"""Audit raw records against frozen plans and report stopping logic without reruns."""
import json
from .prepare import OUT, load, write, text, verify
from .design import LEVELS, sha
from .analyze import development, metrics, order_metrics, decide, parse
from .run import STAGES


def read_rows(stage):
    return [json.loads(s) for s in (OUT/(stage+'_outputs.jsonl')).read_text(encoding='utf-8').splitlines() if s]


def audit_outputs(rows, plans):
    expected = {p['call_id']:p for p in plans}
    assert len({r['call_id'] for r in rows}) == len(rows)
    assert [r['call_id'] for r in rows] == [p['call_id'] for p in plans][:len(rows)]
    for r in rows:
        p = expected[r['call_id']]
        assert all(r[k] == v for k,v in p.items()), r['call_id']
        assert r['raw_sha256'] == sha(r['raw_text'])
        assert r['output_tokens'] == len(r['output_token_ids']) <= 96
        assert r['max_new_tokens'] == 96 and r['seed'] == 42
        assert r['new_chat'] and not r['use_cache'] and not r['constrained']


def report():
    verify()
    plan = load('prompt_plan.json')
    rows = {k:read_rows(k) for k in STAGES}
    audit_outputs(rows['development'],plan['development'])
    dev = development(rows['development'],load('development_cases.json'),plan['policy'])
    selected = dev['selected_level']
    for stage in ('confirmation','order_diagnostic'):
        audit_outputs(rows[stage],plan[stage][selected] if selected else [])
    confirmation = metrics(rows['confirmation'],[c['case_id'] for c in load('confirmation_cases.json')],plan['policy'],True)
    order = order_metrics(rows['order_diagnostic'],rows['development'],plan['order_case_ids'],selected,plan['policy'])
    infrastructure = load('run_state.json')['status'] != 'completed'
    decision = decide(dev,confirmation,order,infrastructure)
    gate = dict(final_decision=decision, selected_level=selected, ORDER_SENSITIVE_FRONTIER=order['ORDER_SENSITIVE_FRONTIER'],
                order_diagnostic_evaluated=order['evaluated'], calls={k:len(v) for k,v in rows.items()},
                maximum_calls=104, downstream_calls=0, policy=plan['policy'])
    for name,value in [('development_metrics.json',dev),('confirmation_metrics.json',confirmation),('order_diagnostic_metrics.json',order),('gate.json',gate)]:
        write(name,value)
    parsed = [parse(r,plan['policy'])|dict(stage=k) for k in STAGES for r in rows[k]]
    text('parsed_outcomes.jsonl',''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in parsed))
    table = '| 难度 | GOLD | TRACEABLE_WRONG（原始类别） | OUT_OF_UNIVERSE | INVALID | 截断 | Valid | 合格错误 | 通过 |\n|---|---|---|---|---|---|---|---|---|\n'
    for level in LEVELS:
        m = dev['levels'][level]
        counts = m['counts']
        table += f"| {level} | {counts['GOLD']}/24 | {counts['TRACEABLE_WRONG']}/24 | {counts['OUT_OF_UNIVERSE']}/24 | {counts['INVALID']}/24 | {m['truncated']}/24 | {m['valid']}/24 | {m['qualified_traceable_wrong']}/24 | {m['passed']} |\n"
    summary = f"# v3.6.4 — {decision}\n\n本版只测试自然第一跳错误产出，不测试下游传播。实际调用：{sum(gate['calls'].values())}；分阶段：{gate['calls']}；选定难度：{selected or '无'}。\n\n"+table
    if selected:
        summary += f"\n确认集：Valid {confirmation['valid']}/24，合格错误 {confirmation['qualified_traceable_wrong']}/24，INVALID {confirmation['counts']['INVALID']}/24，截断 {confirmation['truncated']}/24；通过={confirmation['passed']}。\n\n顺序诊断：{order['changed_identity']}/8 改变状态身份，可比较 {order['comparable_pairs']}/8；ORDER_SENSITIVE_FRONTIER={order['ORDER_SENSITIVE_FRONTIER']}。诊断不改变主门槛。\n"
    else:
        summary += '\n没有难度通过开发门槛，按预注册停止。确认集与顺序诊断未运行；evaluated=false 不是观察到失败或顺序稳定。\n'
    boundary = '\n结果仅适用于冻结的合成任务、模型和接口。失败不能证明自然错误不可能；确认通过也仅表示独立案例上错误产出达到门槛。未测自然错误传播、注入与自然错误等价、真实世界幻觉率、SHAR/HalluSE、内部机制或其他模型。没有继续下一版实验。\n'
    text('README.md',summary+'\n[完整提示和原始输出](inspection.md) · [预注册](pre_registration.md) · [门槛](gate.json)\n'+boundary)
    text('diagnosis.md',summary+boundary)
    text('interpretation.md',summary+'\n同一基础案例的三个难度不是独立样本。新增关系和无关属性共同改变选择负荷，不能分离两者因果作用。截断为测量标志，类别不是修复后的答案。\n'+boundary)
    inspection = [summary,'\n## 逐调用核验\n','每个提示和输出完整保留；A→marker→B 是本版唯一生成子问题。下游 B→C 只预先建表，没有向模型提问。\n']
    compatibility = load('downstream_compatibility.json')
    for stage in STAGES:
        for r in rows[stage]:
            p = parse(r,plan['policy'])
            inspection += [f"### {stage} / {r['call_id']}\n",f"问题：What state is associated with {r['query']}?\n\n金标准：`{r['expected']}`；解析：`{p['category']}`；截断：{p['truncated']}；合格错误：{p['qualified_wrong']}。\n",
                           '完整提示：\n\n```text\n'+r['prompt']+'\n```\n','原始输出：\n\n```text\n'+r['raw_text']+'\n```\n',
                           f"规范化输出：`{p['normalized']}`\n\n预冻结兼容映射（未向模型展示、未调用）：`{compatibility[r['case_id']].get(p['normalized'])}`\n"]
    text('inspection.md','\n'.join(inspection))
    pre = (OUT/'design_audit.pre_inference.md').read_text(encoding='utf-8')
    text('design_audit.md',pre+'\n## Post-inference verification\n\nFrozen sources/prompts/cases/ledger snapshot and all prior result bytes unchanged. Every output matches its frozen plan, rendered hash, cap and free-generation configuration. Required/conditional call counts checked.\n\n'+summary)
    text('CHANGELOG.md','# v3.6.4 CHANGELOG\n\nAdded pre-registered natural first-hop frontier qualification, independent confirmation and conditional non-gating order diagnostic. Explicit C02/C04/C05 changes and user counting resolution frozen before inference. No historical experiment edited; no downstream inference.\n\n'+summary)
    print(json.dumps(gate,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    report()
