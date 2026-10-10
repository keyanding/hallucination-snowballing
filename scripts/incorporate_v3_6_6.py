"""Incorporate verified v3.6.6 evidence; preserve frozen legacy renderer and inputs."""
import copy
import json
import shutil
from pathlib import Path

from scripts.validated_findings import digest, expected_outputs, validate_data

OUT = Path('results/v3_6_6')


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def save(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8', newline='\n')


def rate(p):
    if p['rate'] is None:
        return f"{p['count']}/{p['denominator']}，比例/区间null"
    lo, hi = p['wilson95']
    return f"{p['count']}/{p['denominator']}={p['rate']:.2%}（Wilson95% {lo:.2%}–{hi:.2%}）"


def main():
    m = read(OUT/'metrics.json')
    independent = read(OUT/'independent_verification.json')
    assert independent['passed'] and m['collection_status'] == 'PROSPECTIVE_COLLECTION_COMPLETE'
    data = read(OUT/'prior_ledger_snapshot.json')
    assert data['versions_scanned'][-1]['version'] == 'v3.6.5'
    shutil.copyfile('experiments/v3_6_6/pre_inference_tests.log', OUT/'tests.pre_inference.log')
    props = m['proportions']
    W, G, V = m['W'], m['G'], m['V']
    info = m['information']
    pairs = m['paired']
    diagnostic = m['diagnostic']
    calls = sum(m['stage_counts'].values())
    evidence = [str(OUT/p).replace('\\', '/') for p in ('README.md', 'metrics.json', 'case_outcomes.csv', 'paired_tables.json', 'independent_verification.json', 'inspection.md', 'limitations.md')]
    result = (f"固定120例；Valid{V}/120，GOLD{G}/120，WRONG{W}/120，TRUNCATED{m['first_hop']['TRUNCATED']['count']}/120。"
              f"自然传播{rate(props['conditional_propagation'])}；总体UCR {rate(props['UCR'])}；"
              f"strict E2E {rate(props['strict_end_to_end_success'])}；final gold {rate(props['final_gold_rate'])}。"
              f"自然WRONG结局{m['natural_wrong_counts']}；自然GOLD结局{m['natural_gold_counts']}。")
    rd = '; '.join(f"{k}: n={pairs[k]['n_pairs']}, RD={pairs[k]['RD']}, conservative95%={pairs[k]['paired95']}, table={pairs[k]['table']}" for k in ('all_controlled', 'natural_wrong_subset'))
    diag = (f"v3.6.6预选24例记录顺序诊断：严格有效可比{diagnostic['counts']['comparable']}/24，"
            f"changed {rate(diagnostic['changed_fixed'])}；可比条件下{rate(diagnostic['changed_comparable'])}；"
            f"转移计数{diagnostic['counts']}。无本版敏感性阈值，诊断不加入主WRONG集合。")
    boundary = ("这是自由生成目录错选经无损身份编码进入预建两行合成模块的观察；模块选择依赖实际错身份。"
                "未验证未经程序编码的自然对话传播、真实世界事实幻觉、自然/注入隐状态等价、集成底层能力或SHAR/HalluSE。"
                "复用21人物和组合，区间依赖case层工作独立性；不把受控调用当自然错误。")
    conclusion = f"在该冻结模型/任务/路由策略下保存了{W}个实际自然错选的完整下游轨迹；{info['status']}。{boundary}"
    data['generated_on'] = '2026-10-10'
    data['generated_from_repository_state'] = '135968464958840259bdb6b4c6ced2951afe2e03 + uncommitted v3.6.6 frozen collection'
    data['scope'] = f"登记21个已有模型调用的版本，保留所有失败与未运行阶段。v3.6.6共{calls}次模型调用；台账维护和独立核验本身零模型调用。"
    data['current_boundary'] = (result + f" {m['capability']['status']}；{info['status']}。" + boundary +
        "\n\n版本说明：生成器已被历史实验及本版推理前hash冻结，因此保留其固定模板。紧随本段的“自然错误传播仍未测”以及Open questions节“尚未执行”是截至v3.6.5的旧摘要，已由本段、F28和Q01更新；不能用这些旧模板句否认本版已测的编码后轨迹。C06仍专指旧正确状态组件，新身份桥接证据单列F28，不扩大旧验证范围。\n\n以下固定模板句仅作截至v3.6.5的历史摘要：")
    legacy_notice = "原始台账生成器中的固定旧摘要保留为历史模板：当前自然编码后传播证据以v3.6.6/F28/Q01为准；原C06仍限定旧正确状态接口。维护本身零调用，不是说本版实验零调用。"
    data['repository_scan']['inspection_method'] += ' '+legacy_notice
    data['future_spec_protocol']['latest_incorporated_version'] = 'v3.6.6'
    data['preimplementation_v3_6_6']['status'] = 'COMPLETED_WITH_FROZEN_PREIMPLEMENTATION_SNAPSHOT'
    data['preimplementation_v3_6_6']['design'] = conclusion
    data['preimplementation_v3_6_6']['result_evidence'] = evidence
    data['build_validation'].update(full_suite_tests_passed=183, new_prospective_tests=14, prospective_model_calls=calls)
    planned = ' v3.6.6拟采用固定120例前瞻性采集，无frontier/yield运行门槛；这不改变旧gate结果或扩大旧正确状态管线证据，待测桥接/路由及自然错误下游须单列。'
    for f in data['findings']:
        f['design_implication'] = f['design_implication'].replace(planned, ' v3.6.6已按固定120例完成前瞻性采集；新桥接/路由及实际错误下游证据见F28，历史gate与旧接口范围不变。')
    for c in data['validated_components']:
        c['future_use_rule'] = c['future_use_rule'].replace(planned, ' v3.6.6新身份桥接与条件模块路由见F28；本组件旧验证范围保持不变。')
    by = {f['id']: f for f in data['findings']}
    for fid in ('F14', 'F16', 'F18', 'F19', 'F20'):
        by[fid]['evidence_versions'].append('v3.6.6')
        by[fid]['evidence_files'] += evidence[:2]
    by['F14']['exact_result'] += f" v3.6.6主首跳截断{m['first_hop']['TRUNCATED']['count']}/120，按协议不提取人名；其他类别见全120例表。"
    by['F16']['exact_result'] += ' '+diag
    by['F18']['exact_result'] += f" v3.6.6固定120例实际WRONG{W}/120；这不是独立frontier确认，不改写旧失败。"
    by['F18']['design_implication'] = '历史前沿未确认的事实保留。v3.6.6证明可采用无yield运行门槛的固定队列完整采集；不得继续将旧frontier资格当作所有新设计的运行前提。新设计必须明示选择机制、有效分母与外推范围。'
    by['F19']['exact_result'] += ' '+result+f" 有效自然/配对WRONG样本分别{info['n_eff_natural']}/{info['n_eff_paired_wrong']}；{info['status']}。"
    by['F19']['design_implication'] = '分别报告错误yield、合法覆盖和实际W；W=0条件率null，W不足时保留探索性区间，不追加样本、不借controlled成功扩自然分母。无yield gate的前瞻性设计可以完整运行；本版不推翻历史失败。'
    by['F20'].update(title='编码后自然错选传播已有有界观察；未建立自然/注入等价',
        scope='区分历史零合格分母、v3.6.6编码后合成轨迹与未测的未经编码自然端到端过程。',
        exact_result='历史v3.3 NPR分母0、v3.4下游0、v3.6.3.1实际上游40/40全对。v3.6.6新增：'+result,
        design_implication='采用F28的明确范围与信息量；同prompt自然/CONTROL_A一致不能证明隐状态或来源等价。',
        do_not_infer=boundary)
    f = copy.deepcopy(by['F20'])
    f.update(id='F28', title='前瞻性队列中自然错选经编码进入合成下游的轨迹',
        theme='State propagation', status='INCONCLUSIVE', confidence='HIGH', evidence_versions=['v3.6.6'], evidence_files=evidence,
        scope='HARD/N D4B2；120新图/目标、21复用人物，Qwen3-4B固定栈；无损人名→opaque state桥接、按实际身份选预冻结两行模块。HIGH仅表示保存的计数/可追溯性；INCONCLUSIVE指条件率及机制的推广。',
        exact_result=result+' '+rd+f" 能力{m['capability']['status']}；信息量{info}。",
        design_implication='完整保留固定队列和分母；复用实现不等于把本样本条件率当保证。下一版须独立预注册并审查人物/组合依赖、路由选择与截断。',
        do_not_infer=boundary, supersedes=[], superseded_by=[], open_follow_up=['Q01','Q08'])
    data['findings'].append(f)
    for q in data['open_questions']:
        q['current_evidence'] = q['current_evidence'].replace(' v3.6.6处于设计实施前核对阶段，计划固定120例采集；尚无新观察。','')
        if q['id'] == 'Q01':
            q['current_evidence'] = '截至v3.6.5自然传播未测；v3.6.6已取得编码后合成轨迹：'+result+f" {info['status']}。"+boundary
            q['what_would_resolve_it'] = '已有有界描述，不再要求先复现旧frontier gate。后续独立预注册扩大有效错误样本和身份/组合覆盖，或验证不同桥接/真实语义接口；不能事后补本队列或混合注入分母。'
            q['evidence_files'] += evidence[:2]
        if q['id'] == 'Q08':
            q['current_evidence'] += ' '+diag
            q['evidence_files'] += evidence[:2]
    failure = next(x for x in data['measurement_failures'] if x['id']=='M10')
    failure['symptom'] += f" v3.6.6实际W={W}/120且完成下游；不能把过往零分母写成最新仍为零。当前信息量标记{info['status']}。"
    failure['prevention_rule'] = by['F19']['design_implication']
    failure['evidence_files'] += evidence[:2]
    data['cross_version_reconciliation'].append(dict(id='X11', apparent_conflict='旧台账未测自然传播与v3.6.6有编码后传播记录',
        resolution='历史观察不改写。新前瞻性设计不使用旧yield gate，新增无损编码及条件模块路由；有界轨迹已测，不能继续一概称未测，也不能称真实对话snowballing或自然/注入等价已验证。冻结模板的旧摘要按current_boundary明确标为历史。', evidence_files=evidence[:2]))
    files = sorted(p for p in OUT.rglob('*') if p.is_file())
    for p in files:
        if p.suffix == '.json': read(p)
        elif p.suffix == '.jsonl':
            for line in p.read_text(encoding='utf-8').splitlines():
                if line: json.loads(line)
        else: p.read_text(encoding='utf-8-sig')
    candidates = set().union(*(set(v['artifact_inventory']['expected_present']+v['artifact_inventory']['expected_absent']) for v in data['versions_scanned']))
    inventory = dict(directory=OUT.as_posix(), files=len(files), text_artifacts_parsed=[p.as_posix() for p in files],
        expected_present=sorted(n for n in candidates if (OUT/n).is_file()), expected_absent=sorted(n for n in candidates if not (OUT/n).is_file()))
    data['versions_scanned'].append(dict(version='v3.6.6', phase='固定120例前瞻性自然错选轨迹采集',
        status=m['collection_status']+' / '+m['capability']['status']+' / '+info['status'],
        research_question='自然错选经冻结双射和模块路由后是否输出对应错误outcome；同模块state干预的配对风险差是多少？',
        minimal_design=f"120主首跳+{V}合法自然下游+240配对对照+24独立顺序诊断={calls}次；无yield门槛或科学指标early stop。360模块/864潜在提示/960新ID推理前冻结。",
        exact_key_results=result+' '+rd+' '+diag, valid_conclusion=conclusion,
        not_established=boundary, measurement_artifacts='截断按独立失败计，不能提取首个人名。完整队列coverage包括有明确协议skip的不合法首跳；合法双跳coverage为V/120，转发率为returned/V。自然与control可能同prompt但分别调用。',
        design_implication='以后同时评估固定队列cascade、实际WRONG条件率及有效样本多样性；不把capability终局标记或错误样本量改成运行gate。',
        evidence_files=evidence, result_directory=OUT.as_posix(), artifact_inventory=inventory,
        gate_scalar_snapshot=read(OUT/'gate.json'), implementation_files=[p.as_posix() for p in sorted(Path('experiments/v3_6_6').glob('*.py'))]))
    scan = data['repository_scan']
    for key in ('results_directories','history_results_directories'): scan[key].append(OUT.as_posix())
    scan['experiments_directories'].append('experiments/v3_6_6')
    scan['all_artifact_inventories'].append(inventory)
    scan['historical_artifacts_sha256'].update({p.as_posix():digest(p) for p in files})
    implementation = list(Path('experiments/v3_6_6').glob('*.py'))+[Path('tests/test_v3_6_6.py'),Path('scripts/verify_v3_6_6.py'),Path('scripts/incorporate_v3_6_6.py')]
    scan['implementation_and_data_sha256'].update({p.as_posix():digest(p) for p in implementation})
    data['changelog'].append(dict(date='2026-10-10',entry=f"纳入v3.6.6：{calls}次完整采集，新增F28及21号版本；更新F14/F16/F18/F19/F20、M10、Q01/Q08。"+result+' '+boundary+' 冻结模板保留但明确标注旧摘要；全部旧结果及冻结代码hash不变。'))
    validate_data(data)
    save('docs/validated_findings.json',data)
    for name, content in expected_outputs(data).items():
        Path('docs',name).write_text(content,encoding='utf-8',newline='\n')
    print(json.dumps(dict(versions=len(data['versions_scanned']),findings=len(data['findings']),model_calls=calls),indent=2))


if __name__ == '__main__':
    main()
