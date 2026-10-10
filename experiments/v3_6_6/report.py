"""Rebuild fixed-cohort reports from frozen inputs and auditable raw records."""
import csv
import json
from .prepare import OUT,load,write,text,verify
from .design import route,sha
from .analyze import analyze
from .run import STAGES

LIMITATIONS='''# Limitations and selection biases

HARD/N was chosen using historical results. The21 people/source evidence are a convenience sample. Only strict in-universe outputs can be encoded; report exclusions and V/120 alongside cascade rates. Natural WRONG membership depends on difficulty, identity and presentation. Module selection depends on the observed wrong identity: this is a pre-registered three-module routing policy, not a common four-line environment. Repeated people/bundles induce dependence;120 new targets are not120 independent people. Two-line opaque modules make downstream mapping relatively easy. Diagnostics cover only24 preselected cases and never replace primary answers. Technical missingness may be nonrandom.

Wilson/CP intervals use working case independence. Minimum-information labels are reporting conventions, not power guarantees or mechanism validation. Controlled successes never enlarge W. OVERRIDE means returning the gold outcome, not detecting/correcting the hidden upstream mistake. Natural and matched CONTROL_A may have identical prompt bytes; agreement supports traceability/interface response, not identical hidden states or natural/injected equivalence.

The measured process is free-generated catalog misselection losslessly encoded into synthetic modules. It does not establish real-world factual hallucination rates, unmediated conversational snowballing, internal mechanisms, SHAR/HalluSE effects or other-model behavior. Historical v3.6.5 gate failure remains unchanged. No frontier/yield running gate and no extra cases to reach20 errors.
'''


def rows(name):
    p=OUT/name
    return [json.loads(s) for s in p.read_text(encoding='utf-8').splitlines() if s] if p.exists() else []


def rate(p):
    if p['rate'] is None:return f"{p['count']}/{p['denominator']}; rate/CI=null"
    lo,hi=p['wilson95'];return f"{p['count']}/{p['denominator']} = {p['rate']:.3%}; Wilson95% [{lo:.3%}, {hi:.3%}]"


def report():
    verify();cases=load('cases.json');identity=load('identity_state_map.json');modules=load('downstream_modules.json');schedule=load('call_schedule.json')
    plans={p['plan_id']:p for p in rows('prompt_plan.jsonl')};raw={s:rows(s+'_raw.jsonl') for s in STAGES}
    journal=rows('call_journal.jsonl');started=[r for r in journal if r['status']=='CALL_STARTED'];completed=[r for r in journal if r['status']=='CALL_COMPLETED']
    assert len({r['call_id'] for r in started})==len(started)
    assert len({r['call_id'] for r in completed})==len(completed)
    rawby={r['call_id']:r for rs in raw.values() for r in rs};assert len(rawby)==sum(map(len,raw.values()))
    assert set(rawby)<={r['call_id'] for r in started} and {r['call_id'] for r in completed}<=set(rawby)
    first={r['case_id']:r for r in raw['first_hop']};cby={c['case_id']:c for c in cases}
    routes={cid:route(c,first.get(cid),identity,modules) for cid,c in cby.items()}
    expected_ids=dict(first_hop=[cid+'/FIRST' for cid in schedule['first_hop']],
        natural_downstream=[cid+'/NATURAL' for cid in schedule['natural_downstream'] if routes[cid][1] is not None],
        controlled=[slot['case_id']+'/CONTROL_'+slot['arm'] for slot in schedule['controlled']],
        order_diagnostic=[cid+'/DIAGNOSTIC' for cid in schedule['order_diagnostic']])
    for stage,rs in raw.items():assert [r['call_id'] for r in rs]==expected_ids[stage][:len(rs)]
    logs={r['case_id']:r for r in rows('pipeline_log.jsonl')}
    for cid,log in logs.items():
        assert all(log[k]==v for k,v in routes[cid][2].items())
        assert log['identity_map_hash']==sha(json.dumps(identity[cid],sort_keys=True,ensure_ascii=False))
    for stage,rs in raw.items():
        for r in rs:
            p=plans[r['plan_id']];assert all(r[k]==v for k,v in p.items())
            assert r['raw_sha256']==sha(r['raw_text']) and r['output_tokens']==len(r['output_token_ids'])<=r['cap']
            assert r['max_new_tokens']==r['cap'] and r['seed']==42 and r['new_chat'] and not r['use_cache'] and not r['constrained']
            if stage in ('natural_downstream','controlled'):
                module,prompt,log=routes[r['case_id']];assert r['module_id']==module['module_id']
                if stage=='natural_downstream':assert prompt and r['supplied_state']==log['supplied_state'] and r['upstream_provenance']==logs[r['case_id']]
                else:assert r['arm']==r['call_id'][-1]
    state=load('run_state.json');technical=state.get('technical_status','NONE')
    if state['status']!='completed' and technical=='NONE':technical='INFRASTRUCTURE_FAILURE'
    if set(rawby)!={r['call_id'] for r in completed}:technical='INFRASTRUCTURE_FAILURE'
    attempted=sum(r['stage']=='first_hop' for r in started)
    result=analyze(cases,identity,modules,raw,schedule,technical,attempted)
    write('metrics.json',result);write('paired_tables.json',result['paired'])
    gate={k:result[k] for k in ('technical_status','collection_status','N_planned','N_attempted','N_observed','V','G','W','stage_counts')}
    gate.update(capability=result['capability']['status'],information=result['information']['status']);write('gate.json',gate)
    with (OUT/'case_outcomes.csv').open('w',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(result['case_outcomes'][0]),lineterminator='\n');writer.writeheader();writer.writerows(result['case_outcomes'])
    lines=['# v3.6.6 — Prospective natural-error trajectory collection','','## 1. 技术与采集完整性','',
      f"技术状态：{result['technical_status']}；采集：{result['collection_status']}。计划120，尝试{attempted}，观察{result['N_observed']}。阶段调用：{result['stage_counts']}。最大504，无科学指标early stop。",'',
      '## 2. 全部120例first-hop','','| 类别 | 计数/分母、比例、95% Wilson |','|---|---|']
    lines+=['| '+k+' | '+rate(v)+' |' for k,v in result['first_hop'].items()]
    for k in ('natural_wrong_yield','valid_coverage','wrong_given_valid'):lines+=['',k+': '+rate(result['proportions'][k])]
    lines+=['','## 3. 自然WRONG及总体cascade','','| 指标 | 计数/分母、比例、95% Wilson |','|---|---|']
    for k in ('conditional_propagation','conditional_override','conditional_other','UCR','strict_end_to_end_success','final_gold_rate','complete_trajectory_coverage','legal_forwarding_rate'):
        lines.append('| '+k+' | '+rate(result['proportions'][k])+' |')
    lines+=['',f"自然WRONG结局：{result['natural_wrong_counts']}；缺失bounds：{result['cascade_missing_bounds']}。OVERRIDE不能称为主动纠错。",'',
      '## 4. 自然GOLD轨迹','',f"结局：{result['natural_gold_counts']}。gold→alternate：{rate(result['proportions']['gold_to_alternate'])}。",'',
      '## 5. 配对controlled RD与能力','',f"能力：{result['capability']['status']}；检查：{result['capability']['checks']}。",'']
    for k in ('G_adherence','A_adherence','paired_both_correct','G_permitted','A_permitted'):lines.append('- '+k+': '+rate(result['capability'][k]))
    for k in ('all_controlled','natural_wrong_subset'):
        p=result['paired'][k];lines+=['',f"{k}: n_pairs={p['n_pairs']}, table(Y_A,Y_G)={p['table']}, RD={p['RD']}, conservative paired95%={p['paired95']}。"]
    lines+=['',f"自然propagation/匹配CONTROL_A一致表：{result['paired']['natural_vs_controlled_table']}；同输入一致不证明自然/注入等价。",'',
      '## 6. 信息量、集中性与独立诊断','',str(result['information']),'',
      f"Gold身份数={result['concentration']['distinct_gold_identities']}；wrong身份计数={result['concentration']['wrong_identity_counts']}；最大wrong身份占比：{rate(result['concentration']['maximum_wrong_identity_share'])}。逐组合贡献见metrics.json。",'',
      f"order诊断：{result['diagnostic']['counts']}；changed/24：{rate(result['diagnostic']['changed_fixed'])}；changed/comparable：{rate(result['diagnostic']['changed_comparable'])}；主WRONG子集同错保持：{rate(result['diagnostic']['same_wrong_persistence'])}。没有资格阈值，不补主错误分母。",'',
      '## 7. 解释边界','',LIMITATIONS.split('\n',1)[1],'','[逐调用检视](inspection.md) · [120例总表](case_outcomes.csv) · [完整指标](metrics.json) · [配对表](paired_tables.json)']
    summary='\n'.join(lines)+'\n';text('README.md',summary);text('limitations.md',LIMITATIONS)
    inspection=[summary,'\n## 每例主轨迹与所有调用\n']
    for c,o in zip(cases,result['case_outcomes']):
        cid=c['case_id'];inspection += [f'### {cid}\n','```json\n'+json.dumps(o,ensure_ascii=False,indent=2)+'\n```\n']
        if cid in logs:inspection.append('桥接provenance：\n```json\n'+json.dumps(logs[cid],ensure_ascii=False,indent=2)+'\n```\n')
        for stage in STAGES:
            for r in raw[stage]:
                if r['case_id']==cid:inspection += [f"#### {stage} / {r['call_id']}\n",'完整提问：\n```text\n'+r['prompt']+'\n```\n','原始回答：\n```text\n'+r['raw_text']+'\n```\n']
    text('inspection.md','\n'.join(inspection))
    text('CHANGELOG.md','# v3.6.6 CHANGELOG\n\n固定120例前瞻性设计，映射、身份路由、阈值、区间推理前冻结。没有frontier/yield运行门槛；不改变历史结论。\n\n'+json.dumps(gate,ensure_ascii=False,indent=2)+'\n')
    text('design_audit.md',(OUT/'design_audit.pre_inference.md').read_text(encoding='utf-8')+'\n## Post-inference audit\n\nFrozen inputs/prior artifacts unchanged. Raw/hash/plans and reconstructed routes/journal checked.\n\n'+json.dumps(gate,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(gate,ensure_ascii=False,indent=2))


if __name__=='__main__':report()
