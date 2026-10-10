# Validated Findings Ledger — Audit

构建状态：**LEDGER_BUILD_COMPLETE**（结构/证据链接/历史哈希/生成一致性检查通过后方有效）。

## 1. 扫描范围

来源提交：`135968464958840259bdb6b4c6ced2951afe2e03 + uncommitted v3.6.6 frozen collection`；21实验版本、22结果目录；可达Git提交20个。

v1, v2, v2.1, v3, v3.1, v3.2, v3.3, v3.4, v3.4.1, v3.4.2, v3.4.3, v3.4.4, v3.5.1, v3.6.0, v3.6.1, v3.6.2, v3.6.3, v3.6.3.1, v3.6.4, v3.6.5, v3.6.6。

枚举全部可达Git提交和现存目录；所有结果文本完整读取、JSON/JSONL解析及哈希；人工综合主要报告、门槛、诊断和目标原始失败，并非逐行重新人工裁决所有历史输出。 2026-10-09补充读取v3.6.4全部文件并检查零调用、原生崩溃记录与168提示重建；此目录尚未提交，history目录集包括待提交失败记录，历史旧目录未变。 单独核验attempt_02的72条输出token解码、完整文本分类及停止门槛；首次失败文件全部哈希不变。 v3.6.5新增目录为待提交冻结实验；完整读取其结果，重建24历史fixture、独立核验32输出和192映射。 原始台账生成器中的固定旧摘要保留为历史模板：当前自然编码后传播证据以v3.6.6/F28/Q01为准；原C06仍限定旧正确状态接口。维护本身零调用，不是说本版实验零调用。

完整读取并解析623份结果文本；保存641份历史结果文件和128份旧实现/数据/测试/工作流文件的SHA256。Git历史结果目录与现存目录全集一致；所有experiments/v*均映射入台账。

## 2. 缺少哪些常见产物

文件名不是跨版统一协议。下表“缺少”仅指meta-spec列举的候选文件名不存在，不自动代表实验无证据。早期可用protocol/inspection/metrics；v3.6.1用stage_b_metrics和stage_c_metrics替代总metrics；JSON保留每目录全量清单。

| 目录 | 文件数 | 缺少的候选文件名 |
|---|---|---|
| results/calibration_v3_4_1 | 19 | spec.md, original_spec.md, pre_registration.md, README.md, interpretation.md, calibration_gate.json, CHANGELOG.md, independent_verification.json, prompt_diff_audit.md |
| results/calibration_v3_4_1_preparation_draft | 4 | spec.md, original_spec.md, pre_registration.md, diagnosis.md, interpretation.md, inspection.md, metrics.json, gate.json, calibration_gate.json, design_audit.md, design_audit.pre_inference.md, CHANGELOG.md, verification.json, independent_verification.json, prompt_diff_audit.md |
| results/calibration_v3_4_2 | 23 | original_spec.md, pre_registration.md, README.md, interpretation.md, calibration_gate.json, CHANGELOG.md, independent_verification.json, prompt_diff_audit.md |
| results/calibration_v3_4_3 | 23 | original_spec.md, pre_registration.md, README.md, interpretation.md, calibration_gate.json, CHANGELOG.md, independent_verification.json |
| results/calibration_v3_4_4 | 43 | original_spec.md, pre_registration.md, interpretation.md, calibration_gate.json |
| results/smoke | 11 | spec.md, original_spec.md, pre_registration.md, README.md, diagnosis.md, interpretation.md, calibration_gate.json, design_audit.md, design_audit.pre_inference.md, CHANGELOG.md, verification.json, independent_verification.json, prompt_diff_audit.md |
| results/smoke_v2 | 27 | spec.md, original_spec.md, pre_registration.md, README.md, diagnosis.md, interpretation.md, calibration_gate.json, design_audit.md, design_audit.pre_inference.md, CHANGELOG.md, independent_verification.json, prompt_diff_audit.md |
| results/smoke_v2_1 | 17 | original_spec.md, pre_registration.md, README.md, interpretation.md, calibration_gate.json, design_audit.md, design_audit.pre_inference.md, CHANGELOG.md, independent_verification.json, prompt_diff_audit.md |
| results/smoke_v3 | 20 | original_spec.md, pre_registration.md, README.md, interpretation.md, calibration_gate.json, design_audit.md, design_audit.pre_inference.md, CHANGELOG.md, independent_verification.json, prompt_diff_audit.md |
| results/smoke_v3_1 | 20 | original_spec.md, pre_registration.md, README.md, interpretation.md, calibration_gate.json, design_audit.md, design_audit.pre_inference.md, CHANGELOG.md, independent_verification.json, prompt_diff_audit.md |
| results/smoke_v3_2 | 22 | original_spec.md, pre_registration.md, README.md, interpretation.md, calibration_gate.json, design_audit.md, design_audit.pre_inference.md, CHANGELOG.md, independent_verification.json, prompt_diff_audit.md |
| results/smoke_v3_3 | 31 | original_spec.md, pre_registration.md, README.md, interpretation.md, calibration_gate.json, design_audit.md, design_audit.pre_inference.md, CHANGELOG.md, independent_verification.json, prompt_diff_audit.md |
| results/smoke_v3_4 | 23 | original_spec.md, pre_registration.md, README.md, interpretation.md, calibration_gate.json, design_audit.md, design_audit.pre_inference.md, CHANGELOG.md, independent_verification.json, prompt_diff_audit.md |
| results/v3_5_1 | 28 | original_spec.md, interpretation.md, calibration_gate.json |
| results/v3_6_0 | 27 | interpretation.md |
| results/v3_6_1 | 41 | original_spec.md, metrics.json, calibration_gate.json |
| results/v3_6_2 | 30 | calibration_gate.json |
| results/v3_6_3 | 36 | original_spec.md |
| results/v3_6_3_1 | 40 | original_spec.md |
| results/v3_6_4 | 74 | metrics.json, calibration_gate.json, verification.json, original_spec.md |
| results/v3_6_5 | 41 | metrics.json, calibration_gate.json, verification.json, original_spec.md |
| results/v3_6_6 | 41 | calibration_gate.json, diagnosis.md, interpretation.md, original_spec.md, prompt_diff_audit.md, verification.json |

准备草稿无gate/推理文件是预期；独立v3.5/v3.5.2未发现。v1/v2未保存独立spec副本，但有实际prompt、protocol/inspection与gate。部分早期gate仍写human review pending，本台账不把代码/代理审计升级为独立人工科学批准。

## 3. 信心等级

- HIGH（20）：F01, F03, F04, F05, F07, F08, F10, F11, F12, F13, F14, F15, F16, F18, F19, F20, F21, F26, F27, F28。
- MEDIUM（6）：F02, F06, F09, F17, F24, F25。
- LOW（2）：F22, F23。

HIGH限定到精确观察/范围；开放SHAR/HalluSE机制假说为LOW，未运行这一事实不含糊。小样本fallback等因果线索MEDIUM。

## 4. SUPERSEDED

0项。没有证据要求整体撤销先前发现；v1路线RETIRED不等于结果被推翻。X01–X08保留不同设计及文档语义冲突。

## 5. UNVERIFIED_HISTORY

- 同提示32→64→96实验证明能力恢复：有截断记录和96独立smoke；未见仅改cap的该对照链。
- 已验证SHAR失败或HalluSE漏检一致错误：无处理组/漏检率；wrapper/oracle不是SHAR策略。
- 自然/注入等价且自然传播率已量化：自然合格分母未建立，已有下游错状态是反事实。
- 已观察到按模型错误后验改题修复：v2/v3.4.1调整在推理前；未找到后验替换证据，不能列作observed警告。

token上限审计：发现32、96、16下真实截断及96→192预注册fallback（未触发），未找到64-token独立修复实验。不同版本无截断/有截断之差不能唯一归因cap。没有把32/64/96数字的样本计数或hash命中当cap证据。

## 6. 强制ACTIVE_WARNING

F01, F02, F05, F06, F07, F14, F15, F16, F17, F19。对应M01–M10。每项未来必须AVOIDED或INTENTIONALLY_RETESTED；registry是相同警告的视图，不双计。

## 7. 未来协议冲突及解决

新协议补充全项目review入口；旧三分类保留为组件层映射。ACTIVE_WARNING必须AVOIDED说明规避/不适用路径，或INTENTIONALLY_RETESTED。旧cap16只冻结旧实验，新集成设计可声明有理由的改变与重验证，禁止追改旧结果。
EXPERIMENT_WORKFLOW.md和experiments/inheritance.py在旧manifest冻结，本次不修改；README和新审查脚本激活新协议。

## 8. FROZEN_REUSE是否都有成功验证

有。F03/F04/F08/F09/F10/F11/F12为注明范围的实际通过记录；F26/F27同时引用成功实验、测试和独立核验。C03等工程约束不被包装成单因素因果。C06实测是正确状态转发，错误/未映射只覆盖代码测试，范围明确。

## 9. ACTIVE_WARNING是否都有观察失败

有。资格失败、知识/粒度失败、gold控制被覆盖、有映射UNKNOWN、Recorded合规失败、截断、列表/记录顺序变更、通道不等价及零合格自然错误均有保存文件。它们支持预防警告，不自动证明每个因果解释。未证实的后验改题、自然/注入等价和SHAR失败未升格警告。

## 10. Markdown/JSON一致性及非修改证明

Markdown、audit、CHANGELOG均由JSON确定性生成；verify要求全文一致，检查全部F字段、状态、引用、跨版本覆盖、每个warning的M视图及新旧文件哈希。数值专项核验重新计数v3.4截断、v3.6.3.1集成/接口失败并与文件匹配。

| Finding status | JSON count | Markdown count |
|---|---|---|
| FROZEN_REUSE | 9 | 9 |
| ACTIVE_WARNING | 10 | 10 |
| INCONCLUSIVE | 7 | 7 |
| OPEN_QUESTION | 2 | 2 |
| RETIRED | 0 | 0 |
| SUPERSEDED | 0 | 0 |

全套183项测试通过，其中新增协议测试8项。记录：[docs/validated_findings_tests.log](../docs/validated_findings_tests.log)。新增模型调用：0。

这些是F条目计数，不包含C/M/Q。未新增模型调用、未改历史结果或冻结代码；只新增研究台账/检查工具/测试并链接入口。台账检查不能替代人工科学判断，更新时须重新核实证据，而不能只让文本与JSON互相一致。
