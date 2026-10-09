"""Frozen-plan checks and separate primary/diagnostic reporting."""
import json
from .prepare import OUT,load,write,text,verify
from .analyze import metrics,diagnostic,decide,parse
from .design import sha
from .run import STAGES


def report():
    verify()
    plan=load('prompt_plan.json');aliases=load('alias_registry.json')
    rows={s:[json.loads(line) for line in (OUT/(s+'_outputs.jsonl')).read_text(encoding='utf-8').splitlines() if line] for s in STAGES}
    for stage,rs in rows.items():
        assert len(rs)<=len(plan[stage])
        for r,p in zip(rs,plan[stage]):
            assert all(r[k]==v for k,v in p.items())
            assert sha(r['raw_text'])==r['raw_sha256'] and len(r['output_token_ids'])==r['output_tokens']<=96
            assert r['max_new_tokens']==96 and r['seed']==42 and r['new_chat'] and not r['use_cache'] and not r['constrained']
    dev=metrics(rows['development'],[c['case_id'] for c in load('development_cases.json')],aliases)
    conf=metrics(rows['confirmation'],[c['case_id'] for c in load('confirmation_cases.json')],aliases,True)
    diag=diagnostic(rows['presentation_diagnostic'],rows['development'],plan['diagnostic_ids'],aliases)
    decision=decide(dev,conf,diag,plan['policy'],load('run_state.json')['status']!='completed')
    if dev['complete']:assert dev==load('development_classification.before_diagnostic.json')
    gate=dict(final_decision=decision,PRESENTATION_SENSITIVE=diag['PRESENTATION_SENSITIVE'],development_passed=dev['passed'],
              confirmation_evaluated=conf['evaluated'],confirmation_passed=conf['passed'],presentation_evaluated=diag['evaluated'],
              calls={s:len(rs) for s,rs in rows.items()},downstream_calls=0,maximum_calls=56,policy=plan['policy'])
    for n,v in [('gate.json',gate),('development_metrics.json',dev),('confirmation_metrics.json',conf),('presentation_diagnostic_metrics.json',diag)]:write(n,v)
    parsed=[parse(r,aliases)|dict(stage=s) for s,rs in rows.items() for r in rs]
    text('parsed_outcomes.jsonl',''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in parsed))
    summary=f'# v3.6.5 — {decision}\n\n只复现历史v3.4.4 HARD/N，不执行下游传播。实际调用：{gate["calls"]}。\n\n'
    summary+='| 阶段 | Valid | Gold | Traceable wrong | Out-of-set | Ambiguous | Noncompliant | Truncated |\n|---|---|---|---|---|---|---|---|\n'
    for name,m in [('开发',dev),('确认',conf)]:
        if not m['evaluated']:
            summary+=f'| {name} | 未运行 | — | — | — | — | — | — |\n'
        else:
            c=m['counts'];summary+=f"| {name} | {m['valid']}/24 | {c['IN_SET_VALID_GOLD']}/24 | {m['traceable_wrong']}/24 | {c['OUT_OF_SET']}/24 | {c['AMBIGUOUS']}/24 | {c['NONCOMPLIANT']}/24 | {c['TRUNCATED']}/24 |\n"
    summary+=f"\n开发错误案例数：{dev['distinct_wrong_cases']}；错误身份数：{dev['distinct_wrong_identities']}。\n"
    if diag['evaluated']:
        summary+=f"\n非门槛呈现诊断：相同身份{diag['same_identity']}/8、改变身份{diag['changed_identity']}/8；严格有效成对覆盖{diag['comparable']}/8；原始/置换严格有效分别{diag['primary_strict_valid']}/8、{diag['diagnostic_strict_valid']}/8。gold→wrong={diag['gold_to_wrong']}，wrong→gold={diag['wrong_to_gold']}，wrong→different wrong={diag['wrong_to_different_wrong']}，同一错误身份保持={diag['same_wrong_identity']}。PRESENTATION_SENSITIVE={diag['PRESENTATION_SENSITIVE']}；诊断不改变主门槛，也不筛选错误案例。\n"
    reason={'HARD_N_SIGNAL_NOT_REPLICATED':'历史HARD/N开发5/24错误信号未在这组新案例上达到预注册复现门槛；不追加难度搜索。',
            'HARD_N_CONFIRMATION_FAILED':'开发信号出现，但未通过新确认集；不挑选开发错误开展传播。',
            'HARD_N_NATURAL_ERROR_SIGNAL_CONFIRMED':'该冻结接口在开发与独立确认集均产生达到门槛的可追溯自然错误；仅建立错误来源资格。',
            'INFRASTRUCTURE_FAILURE':'结构或运行完整性失败，未完成阶段不能解释成零错误率。'}[decision]
    summary+='\n'+reason+'\n'
    boundary='\n21位真实人物复用；48个图/目标新建，40组新组合、8组历史组合，开发与确认组合互不重复。自然错误仅指合成图任务中的自由生成人名错选，不是事实知识幻觉率。没有自然下游传播、注入/自然等价、内部机制、SHAR/HalluSE或其他模型结论。原始错误不修复。\n'
    for name in ('README.md','diagnosis.md','interpretation.md'):text(name,summary+boundary+'\n[逐调用提示/输出](inspection.md) · [历史兼容审计](historical_interface_audit.md) · [预注册](pre_registration.md)\n')
    inspect=[summary,boundary,'\n## 逐调用问题与输出\n']
    for stage,rs in rows.items():
        for r in rs:
            p=parse(r,aliases)
            inspect += [f"### {stage} / {r['call_id']}\n",f"金标准：{r['gold']}；类别：{p['category']}；身份：{p['identity']}；截断：{r['truncated']}。\n",
                        '完整提问：\n\n```text\n'+r['prompt']+'\n```\n','原始回答：\n\n```text\n'+r['raw_text']+'\n```\n',
                        '预冻结下游端点（未展示、未调用）：'+str(r['downstream_endpoints'].get(p['identity']))+'\n']
    text('inspection.md','\n'.join(inspect))
    text('design_audit.md',(OUT/'design_audit.pre_inference.md').read_text(encoding='utf-8')+'\n## Post-inference audit\n\nAll frozen inputs and historical artifacts unchanged; output plans and hashes checked; development classification persisted before diagnostics.\n\n'+summary)
    text('CHANGELOG.md','# v3.6.5 CHANGELOG\n\nHistorical HARD/N reused exactly; user resolved diagnostics to run even after development failure. Cases/mappings/parser/thresholds frozen before inference.\n\n'+summary)
    print(json.dumps(gate,ensure_ascii=False,indent=2))


if __name__=='__main__':report()
