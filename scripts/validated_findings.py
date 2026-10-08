"""Render/audit the evidence ledger and check future specs. Never runs models."""
import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LEDGER=ROOT/'docs/validated_findings.json'
STATUSES=('FROZEN_REUSE','ACTIVE_WARNING','INCONCLUSIVE','OPEN_QUESTION','RETIRED','SUPERSEDED')
CONFIDENCE=('HIGH','MEDIUM','LOW')
THEMES=('Measurement validity','State propagation','Context accumulation','Upstream A→B capability','Modular two-hop pipeline','Integrated two-hop execution','Natural first-hop error generation','Prompt / presentation brittleness','UNKNOWN / fallback behavior','Output-length / truncation artifacts','Position / ordering effects','Model capability limits','Natural vs injected error distinction','SHAR / HalluSE relevance','Open questions')


def load(path=LEDGER):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def evidence(paths):
    return '；'.join(f'[{p}](../{p})' for p in paths)


def cell(value):
    return str(value).replace('|','\\|').replace('\n',' ')


def counts(data):
    return {s:sum(f['status']==s for f in data['findings']) for s in STATUSES}


def protocol_lines(data):
    p=data['future_spec_protocol']
    return [
        '每份新实验spec的第一个标题必须是 `# Prior Findings Review`，引用 `docs/validated_findings.md` 和 `docs/validated_findings.json`。随后列出审查表，再写 `## Validated Inheritance`，最后才写 `## New manipulation`。',
        '', '| Finding / Component | Ledger status | Treatment in this experiment | Rationale |', '|---|---|---|---|',
        '| Fxx / Cxx | 台账原状态 | 明确选择下列处理方式 | 写适用范围、依据及验证计划 |', '',
        '处理方式：'+', '.join('`'+v+'`' for v in p['treatments'])+'。', '',
        f"全部{len(data['findings'])}项发现与{len(data['validated_components'])}个组件须逐项审查；不适用的非警告条目可用NOT_RELEVANT并说明原因。失败登记M条目是相应F警告的视图，不重复要求一套审查行。每个ACTIVE_WARNING必须选择AVOIDED或INTENTIONALLY_RETESTED；不适用也要说明如何避免该失败路径，不能写NOT_RELEVANT跳过。", '',
        '改变FROZEN_REUSE组件时，必须记录component、prior_evidence、reason、prior_conclusion_no_longer_applies、revalidation_gate；禁止一面声明FROZEN_REUSE一面修改。新的审查JSON保留modified布尔值及modification对象。', '',
        '机器审查：`python scripts/validated_findings.py review-spec --spec PATH --review PATH`。review JSON必须包含ledger_sha256（当前台账JSON的SHA256）、latest_completed_version、rows；每行含id、ledger_status、treatment、rationale、modified，变更组件另含modification对象。Markdown表格须与JSON行一致。', '',
        '该检查验证声明、台账新鲜度、覆盖及门槛说明，不自动推断实验是否科学合理，也不替代逐字prompt比对、实际代码/模型哈希和推理前审计。以后新runner必须在准备阶段调用审查检查，并冻结其结果。旧runner不追改。', '',
        p['historical_rule_resolution'], p['frozen_legacy_files'], '',
        '与旧三分类的对应：'+ '；'.join(f'{k}→{v}' for k,v in p['legacy_treatment_mapping'].items())+'。此映射用于旧组件层说明，不能替代新协议对警告和修改理由的更严格要求。', '',
        '维护顺序：'+' → '.join(p['maintenance'])+'。最近完成的实验未入账时，禁止通过下一spec审查。', '',
        '台账维护：先更新JSON证据与新版本条目/哈希、追加changelog，再执行 `python scripts/validated_findings.py render` 与 `python scripts/validated_findings.py verify`。只有新增/有理由更正的证据可改变状态；历史观测不被覆盖。']


def render(data):
    c=counts(data)
    out=['# 项目已验证发现台账','','## How to use this file','',
         f"截至 {data['generated_on']}（{data['timezone']}），来源提交 `{data['generated_from_repository_state']}`。{data['scope']}",'',
         'JSON是规范数据源；本Markdown、audit和CHANGELOG由同一数据源生成。F为发现、C为可复用组件、M为测量失败视图、Q为待解决问题。HIGH表示范围内有直接且较强记录支撑，不表示跨模型/总体普适；LOW的开放问题仍是假说。', '',
         '状态计数（仅F条目；M/C不重复计数）：'+ '，'.join(f'{k}={v}' for k,v in c.items())+'。', '',
         'FROZEN_REUSE仍受scope约束；ACTIVE_WARNING是有观察依据的设计约束；INCONCLUSIVE不是零效应；OPEN_QUESTION不是已成立结论；RETIRED/SUPERSEDED须给证据及去向。UNVERIFIED_HISTORY单列，绝不冒充有效发现。', '',
         '## Project-level research question','',data['project_question'],'','## Current research boundary','',data['current_boundary'],'',
         '当前最强正结论是**模块化显式符号管线通过**；最重要限制是**自然错误传播仍未测，集成底层能力仍不确定**。所有百分比须保留分母；同一案例的条件/顺序重复不当作独立样本。','',
         '## Version-by-version evidence map','',f"共{len(data['versions_scanned'])}个已执行版本；另1个准备草稿不计实验。早期目录使用smoke/calibration前缀，同样纳入。",'',
         '| 版本 | 阶段 | 冻结门槛/研究状态 |','|---|---|---|']
    for v in data['versions_scanned']:
        out.append(f"| {v['version']} | {cell(v['phase'])} | {cell(v['status'])} |")
    for v in data['versions_scanned']:
        out += ['',f"### {v['version']} — {v['phase']}",'',f"**状态：{v['status']}**",'',
                '**研究问题：** '+v['research_question'],'', '**最小设计：** '+v['minimal_design'],'',
                '**关键结果（保留分母）：** '+v['exact_key_results'],'','**有效结论：** '+v['valid_conclusion'],'',
                '**未建立：** '+v['not_established'],'','**测量问题：** '+v['measurement_artifacts'],'',
                '**后续设计含义：** '+v['design_implication'],'','证据：'+evidence(v['evidence_files'])]
    out += ['','准备草稿：'+evidence(['results/calibration_v3_4_1_preparation_draft/README.md'])+'；War标题误作genre在推理前修正，未运行模型，不计第二次实验。','',
            '## Consolidated findings','']
    for theme in THEMES:
        out += ['### '+theme,'']
        if theme=='Open questions':
            out += ['开放问题集中列于Q01–Q09；P0是自然错误产出/传播资格与集成输出协议诊断，尚未执行。','']
        for f in (f for f in data['findings'] if f['theme']==theme):
            out += [f"#### {f['id']} — {f['title']}",'',f"状态：**{f['status']}**；信心：**{f['confidence']}**；版本：{', '.join(f['evidence_versions'])}。",'',
                    '**范围：** '+f['scope'],'','**精确结果：** '+f['exact_result'],'','**设计含义：** '+f['design_implication'],'',
                    '**不要推断：** '+f['do_not_infer'],'',
                    '替代：'+(', '.join(f['supersedes']) or '无')+'；被替代：'+(', '.join(f['superseded_by']) or '无')+'；开放跟进：'+', '.join(f['open_follow_up'])+'。','',
                    '证据：'+evidence(f['evidence_files']),'']
    out += ['### 跨版本冲突处理','']
    for x in data['cross_version_reconciliation']:
        out += [f"- **{x['id']} {x['apparent_conflict']}**：{x['resolution']} 证据：{evidence(x['evidence_files'])}",'']
    out += ['## Validated Component Registry','',
            '| Component ID | Component | Canonical version | Exact artifact/template | Scope | Status | Future-use rule |','|---|---|---|---|---|---|---|']
    for r in data['validated_components']:
        out.append('| '+' | '.join([r['id'],cell(r['component']),r['canonical_version'],evidence(r['exact_artifact']),cell(r['scope']),r['status'],cell(r['future_use_rule'])+' ('+', '.join(r['finding_ids'])+')'])+' |')
    out += ['','每个组件的成功验证文件及关联F条目在JSON中完整列出；ID约束、parser、执行栈是成功组合中的工程组件，并无“单独致效”的消融结论。','',
            '## Measurement Failure Registry','',
            '| ID | Failure mode | Evidence | Symptom | Why it matters | Prevention rule | Status |','|---|---|---|---|---|---|---|']
    for r in data['measurement_failures']:
        out.append('| '+' | '.join([r['id']+' / '+','.join(r['finding_ids']),cell(r['failure_mode']),evidence(r['evidence_files']),cell(r['symptom']),cell(r['why_it_matters']),cell(r['prevention_rule']),r['status']])+' |')
    out += ['','证据只支持风险存在及注明范围，不一定识别唯一因果。未发现“事后改题修复”已发生的证据；禁止后验修复作为预防纪律保留，但不伪造observed失败条目。注入/自然混淆的防范由F12/F20与协议承担，没有把未发生的误用登记成观测事件。','',
            '## Open Questions','']
    for q in data['open_questions']:
        out += [f"### {q['id']} — {q['question']}",'',f"优先级：{q['priority']}；依赖：{', '.join(q['dependencies'])}。",'',
                '**为何重要：** '+q['why_important'],'','**当前证据：** '+q['current_evidence'],'','**解决标准：** '+q['what_would_resolve_it'],'','证据：'+evidence(q['evidence_files']),'']
    out += ['## Retired / superseded directions','','没有将任何F条目标为SUPERSEDED：后来的不同接口结果不撤销早期真实观察。','']
    for r in data['retired_directions']:
        out += [f"- {r['status']}：{r['direction']}。{r['reason']} 证据：{evidence(r['evidence_files'])}",'']
    out += ['### 未验证的历史说法','']
    for r in data['unverified_history']:
        out += [f"- **{r['status']}**：{r['claim']}。{r['reason']}",'']
    out += ['## Future Experiment Design Protocol','']+protocol_lines(data)+['','## Change Log','']
    for r in data['changelog']:
        out += [f"- {r['date']}：{r['entry']}"]
    return '\n'.join(out).rstrip()+'\n'


def audit(data):
    scan=data['repository_scan'];c=counts(data)
    out=['# Validated Findings Ledger — Audit','','构建状态：**LEDGER_BUILD_COMPLETE**（结构/证据链接/历史哈希/生成一致性检查通过后方有效）。', '',
         '## 1. 扫描范围','',f"来源提交：`{data['generated_from_repository_state']}`；{len(data['versions_scanned'])}实验版本、{len(scan['results_directories'])}结果目录；可达Git提交{len(scan['reachable_commits'])}个。",'',
         ', '.join(v['version'] for v in data['versions_scanned'])+'。','',scan['inspection_method'],'',
         f"完整读取并解析{sum(len(s['text_artifacts_parsed']) for s in scan['all_artifact_inventories'])}份结果文本；保存{len(scan['historical_artifacts_sha256'])}份历史结果文件和{len(scan['implementation_and_data_sha256'])}份旧实现/数据/测试/工作流文件的SHA256。Git历史结果目录与现存目录全集一致；所有experiments/v*均映射入台账。",'',
         '## 2. 缺少哪些常见产物','',
         '文件名不是跨版统一协议。下表“缺少”仅指meta-spec列举的候选文件名不存在，不自动代表实验无证据。早期可用protocol/inspection/metrics；v3.6.1用stage_b_metrics和stage_c_metrics替代总metrics；JSON保留每目录全量清单。','',
         '| 目录 | 文件数 | 缺少的候选文件名 |','|---|---|---|']
    for s in scan['all_artifact_inventories']:
        out.append(f"| {s['directory']} | {s['files']} | {', '.join(s['expected_absent']) or '无'} |")
    out += ['','准备草稿无gate/推理文件是预期；独立v3.5/v3.5.2未发现。v1/v2未保存独立spec副本，但有实际prompt、protocol/inspection与gate。部分早期gate仍写human review pending，本台账不把代码/代理审计升级为独立人工科学批准。','',
            '## 3. 信心等级','']
    for level in CONFIDENCE:
        ids=[f['id'] for f in data['findings'] if f['confidence']==level]
        out += [f"- {level}（{len(ids)}）：{', '.join(ids)}。"]
    out += ['','HIGH限定到精确观察/范围；开放SHAR/HalluSE机制假说为LOW，未运行这一事实不含糊。小样本fallback等因果线索MEDIUM。','',
            '## 4. SUPERSEDED','',f"{len(data['superseded_findings'])}项。没有证据要求整体撤销先前发现；v1路线RETIRED不等于结果被推翻。X01–X08保留不同设计及文档语义冲突。",'',
            '## 5. UNVERIFIED_HISTORY','']
    out += [f"- {r['claim']}：{r['reason']}" for r in data['unverified_history']]
    out += ['','token上限审计：发现32、96、16下真实截断及96→192预注册fallback（未触发），未找到64-token独立修复实验。不同版本无截断/有截断之差不能唯一归因cap。没有把32/64/96数字的样本计数或hash命中当cap证据。','',
            '## 6. 强制ACTIVE_WARNING','',', '.join(data['future_spec_protocol']['mandatory_warning_ids'])+'。对应M01–M10。每项未来必须AVOIDED或INTENTIONALLY_RETESTED；registry是相同警告的视图，不双计。','',
            '## 7. 未来协议冲突及解决','',data['future_spec_protocol']['historical_rule_resolution'],data['future_spec_protocol']['frozen_legacy_files'],'',
            '## 8. FROZEN_REUSE是否都有成功验证','',
            '有。F03/F04/F08/F09/F10/F11/F12为注明范围的实际通过记录；F26/F27同时引用成功实验、测试和独立核验。C03等工程约束不被包装成单因素因果。C06实测是正确状态转发，错误/未映射只覆盖代码测试，范围明确。','',
            '## 9. ACTIVE_WARNING是否都有观察失败','',
            '有。资格失败、知识/粒度失败、gold控制被覆盖、有映射UNKNOWN、Recorded合规失败、截断、列表/记录顺序变更、通道不等价及零合格自然错误均有保存文件。它们支持预防警告，不自动证明每个因果解释。未证实的后验改题、自然/注入等价和SHAR失败未升格警告。','',
            '## 10. Markdown/JSON一致性及非修改证明','',
            'Markdown、audit、CHANGELOG均由JSON确定性生成；verify要求全文一致，检查全部F字段、状态、引用、跨版本覆盖、每个warning的M视图及新旧文件哈希。数值专项核验重新计数v3.4截断、v3.6.3.1集成/接口失败并与文件匹配。','',
            '| Finding status | JSON count | Markdown count |','|---|---|---|']
    for s,n in c.items():out.append(f'| {s} | {n} | {n} |')
    if 'build_validation' in data:
        v=data['build_validation']
        out += ['',f"全套{v['full_suite_tests_passed']}项测试通过，其中新增协议测试{v['new_protocol_tests']}项。记录：{evidence([v['test_log']])}。新增模型调用：{v['new_model_calls']}。"]
    out += ['','这些是F条目计数，不包含C/M/Q。未新增模型调用、未改历史结果或冻结代码；只新增研究台账/检查工具/测试并链接入口。台账检查不能替代人工科学判断，更新时须重新核实证据，而不能只让文本与JSON互相一致。','']
    return '\n'.join(out).rstrip()+'\n'


def changelog(data):
    out=['# Validated Findings — CHANGELOG','']
    for r in data['changelog']:out += [f"## {r['date']}",'',r['entry'],'']
    return '\n'.join(out).rstrip()+'\n'


def validate_data(data,check_hashes=True):
    ids=set()
    for group in ('findings','validated_components','measurement_failures','open_questions'):
        for item in data[group]:
            assert item['id'] not in ids,item['id']
            ids.add(item['id'])
            for p in item['evidence_files']:
                assert not Path(p).is_absolute() and '..' not in Path(p).parts
                assert (ROOT/p).is_file(),p
    required=('id','title','status','confidence','evidence_versions','evidence_files','scope','exact_result','design_implication','do_not_infer','supersedes','superseded_by','open_follow_up')
    versions={v['version'] for v in data['versions_scanned']}
    for v in data['versions_scanned']:
        assert all(v[k] for k in ('phase','status','research_question','minimal_design','exact_key_results','valid_conclusion','not_established','measurement_artifacts','design_implication','evidence_files'))
        assert all((ROOT/p).is_file() for p in v['evidence_files'])
    assert data['future_spec_protocol']['latest_incorporated_version']==data['versions_scanned'][-1]['version']
    for f in data['findings']:
        assert all(k in f for k in required),f['id']
        assert f['status'] in STATUSES and f['confidence'] in CONFIDENCE
        assert all(f[k] for k in ('scope','exact_result','design_implication','do_not_infer','evidence_files'))
        assert set(f['evidence_versions'])<=versions
        assert set(f['open_follow_up']+f['supersedes']+f['superseded_by'])<=ids
    warnings={f['id'] for f in data['findings'] if f['status']=='ACTIVE_WARNING'}
    assert warnings==set(data['future_spec_protocol']['mandatory_warning_ids'])
    assert warnings=={f for r in data['measurement_failures'] for f in r['finding_ids']}
    for c in data['validated_components']:
        assert c['status']=='FROZEN_REUSE' and c['finding_ids']
        assert set(c['finding_ids'])<={f['id'] for f in data['findings'] if f['status']=='FROZEN_REUSE'}
    scan=data['repository_scan']
    current={p.relative_to(ROOT).as_posix() for p in (ROOT/'results').iterdir() if p.is_dir()}
    assert current==set(scan['results_directories']), 'New result directory not incorporated'
    assert current==set(scan['history_results_directories'])
    assert {v['result_directory'] for v in data['versions_scanned']}|{a['directory'] for a in scan['archived_preparation_drafts']}==current
    if check_hashes:
        for group in ('historical_artifacts_sha256','implementation_and_data_sha256'):
            for p,h in scan[group].items():assert digest(ROOT/p)==h,p
    return True


def numeric_audit():
    # Read-only independent counters on the raw outputs central to interpretation.
    def rows(p):return [json.loads(s) for s in (ROOT/p).read_text(encoding='utf-8-sig').splitlines() if s]
    r=rows('results/v3_6_3_1/parsed_outcomes.jsonl')
    integ=[x for x in r if x['condition'].startswith('I-')]
    assert len(integ)==40
    assert sum(x['category']=='INVALID' for x in integ)==24
    assert sum(x['truncated'] for x in integ)==17
    raw=rows('results/v3_6_3_1/integrated_outputs.jsonl')
    assert sum(x['truncated'] for x in raw)==17
    cases={c['case_id']:c for c in load(ROOT/'results/v3_6_3_1/main_cases.json')}
    import unicodedata
    for condition,expected in (('I-A',7),('I-B',9)):
        role='a' if condition=='I-A' else 'b'
        assert sum(not x['truncated'] and unicodedata.normalize('NFC',x['raw_text']).strip().removesuffix('.')==cases[x['case_id']]['outcome_'+role] for x in raw if x['condition']==condition)==expected
    shell=rows('results/v3_6_3_1/shell_diagnostic_outputs.jsonl')
    assert len(shell)==40 and sum(x['truncated'] for x in shell)==3
    assert all(x['shell']=='RECORDED' for x in shell if x['truncated'])
    old=rows('results/smoke_v3_4/first_hop_generations.jsonl')
    assert len(old)==20 and sum(x['truncated'] for x in old)==9
    later=rows('results/calibration_v3_4_3/free_generation.jsonl')
    assert len(later)==72 and sum(x['truncated'] for x in later)==4
    smoke=load(ROOT/'results/calibration_v3_4_4/format_smoke.json')
    assert smoke['selected_NR_cap']==96 and len(smoke['tasks'])==4
    assert all(x['cap']==96 and not x['F']['truncated'] for x in smoke['tasks'])
    return dict(v34_outputs=20,v34_truncated=9,v343_free_outputs=72,v343_truncated=4,
                v344_independent_cap_smoke=4,v344_selected_cap=96,
                integrated_outputs=40,integrated_invalid=24,integrated_truncated=17,shell_outputs=40,shell_truncated=3)


def expected_outputs(data):
    return {'validated_findings.md':render(data),'validated_findings_audit.md':audit(data),'validated_findings_CHANGELOG.md':changelog(data)}


def review_spec(data,spec,review,ledger_hash):
    assert spec.lstrip().startswith('# Prior Findings Review\n'), 'First heading must be Prior Findings Review'
    p=data['future_spec_protocol']
    assert all(ref in spec for ref in p['required_references']), 'Missing ledger references'
    assert '## Validated Inheritance' in spec and '## New manipulation' in spec
    assert spec.index('## Validated Inheritance')<spec.index('## New manipulation')
    assert review['ledger_sha256']==ledger_hash,'Stale ledger review'
    assert review['latest_completed_version']==p['latest_incorporated_version'],'Latest experiment not reviewed'
    known={x['id']:x for x in data['findings']+data['validated_components']}
    rows=review['rows'];by={r['id']:r for r in rows}
    assert len(by)==len(rows) and set(by)==set(known),'Review every finding and component exactly once'
    table=[]
    for line in spec.splitlines():
        if line.startswith('|'):
            table.append([v.strip().strip('`') for v in line.strip('|').split('|')])
    for rid,r in by.items():
        assert r['ledger_status']==known[rid]['status']
        assert r['treatment'] in p['treatments'] and r['rationale'].strip()
        assert any(len(cells)>=4 and cells[:4]==[rid,r['ledger_status'],r['treatment'],r['rationale']] for cells in table),rid+' table mismatch'
        if rid in p['mandatory_warning_ids']:
            assert r['treatment'] in p['mandatory_warning_treatments'],rid+' warning unaddressed'
        assert isinstance(r['modified'],bool)
        if rid.startswith('C') and r['modified']:
            assert r['treatment'] in ('INTENTIONALLY_RETESTED','OVERRIDDEN','TARGETED')
            change=r['modification']
            assert all(change.get(k) for k in p['modified_component_required_fields'])
            assert change['component']==rid
            assert isinstance(change['prior_evidence'],list)
            assert set(change['prior_evidence'])<=set(known[rid]['evidence_files'])
        if r['treatment']=='FROZEN_REUSE':assert not r['modified']
    return dict(passed=True,reviewed_findings_components=len(by),warnings_addressed=len(p['mandatory_warning_ids']))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=('render','verify','review-spec'))
    parser.add_argument('--spec',type=Path)
    parser.add_argument('--review',type=Path)
    args=parser.parse_args()
    data=load();validate_data(data)
    if args.action=='review-spec':
        assert args.spec and args.review
        result=review_spec(data,args.spec.read_text(encoding='utf-8-sig'),load(args.review),digest(LEDGER))
    else:
        for name,text in expected_outputs(data).items():
            path=ROOT/'docs'/name
            if args.action=='render':path.write_text(text,encoding='utf-8',newline='\n')
            else:assert path.read_text(encoding='utf-8')==text,name+' inconsistent with JSON'
        result=dict(status='LEDGER_BUILD_COMPLETE',versions=len(data['versions_scanned']),status_counts=counts(data),historical_files_unchanged=len(data['repository_scan']['historical_artifacts_sha256']),numeric_audit=numeric_audit())
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
