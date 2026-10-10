# v3.6.6 — Prospective natural-error trajectory collection

## 1. 技术与采集完整性

技术状态：NONE；采集：PROSPECTIVE_COLLECTION_COMPLETE。计划120，尝试120，观察120。阶段调用：{'first_hop': 120, 'natural_downstream': 118, 'controlled': 240, 'order_diagnostic': 24}。最大504，无科学指标early stop。

## 2. 全部120例first-hop

| 类别 | 计数/分母、比例、95% Wilson |
|---|---|
| GOLD | 98/120 = 81.667%; Wilson95% [73.799%, 87.570%] |
| WRONG | 20/120 = 16.667%; Wilson95% [11.056%, 24.345%] |
| TRUNCATED | 2/120 = 1.667%; Wilson95% [0.458%, 5.874%] |
| AMBIGUOUS | 0/120 = 0.000%; Wilson95% [0.000%, 3.102%] |
| OUT_OF_SET | 0/120 = 0.000%; Wilson95% [0.000%, 3.102%] |
| NONCOMPLIANT | 0/120 = 0.000%; Wilson95% [0.000%, 3.102%] |
| MISSING | 0/120 = 0.000%; Wilson95% [0.000%, 3.102%] |

natural_wrong_yield: 20/120 = 16.667%; Wilson95% [11.056%, 24.345%]

valid_coverage: 118/120 = 98.333%; Wilson95% [94.126%, 99.542%]

wrong_given_valid: 20/118 = 16.949%; Wilson95% [11.248%, 24.734%]

## 3. 自然WRONG及总体cascade

| 指标 | 计数/分母、比例、95% Wilson |
|---|---|
| conditional_propagation | 20/20 = 100.000%; Wilson95% [83.887%, 100.000%] |
| conditional_override | 0/20 = 0.000%; Wilson95% [0.000%, 16.113%] |
| conditional_other | 0/20 = 0.000%; Wilson95% [0.000%, 16.113%] |
| UCR | 20/120 = 16.667%; Wilson95% [11.056%, 24.345%] |
| strict_end_to_end_success | 98/120 = 81.667%; Wilson95% [73.799%, 87.570%] |
| final_gold_rate | 98/120 = 81.667%; Wilson95% [73.799%, 87.570%] |
| complete_trajectory_coverage | 120/120 = 100.000%; Wilson95% [96.898%, 100.000%] |
| legal_forwarding_rate | 118/118 = 100.000%; Wilson95% [96.847%, 100.000%] |

自然WRONG结局：{'PROPAGATION': 20}；缺失bounds：{'observed_P': 20, 'uncertain_cases': 0, 'denominator': 120, 'lower': 0.16666666666666666, 'upper': 0.16666666666666666, 'final': True}。OVERRIDE不能称为主动纠错。

## 4. 自然GOLD轨迹

结局：{'GOLD_RETAINED': 98}。gold→alternate：0/98 = 0.000%; Wilson95% [0.000%, 3.772%]。

## 5. 配对controlled RD与能力

能力：CURRENT_COHORT_CAPABILITY_SUPPORTED；检查：{'C1': True, 'C2': True, 'C3': True, 'C4_G': True, 'C4_A': True}。

- G_adherence: 120/120 = 100.000%; Wilson95% [96.898%, 100.000%]
- A_adherence: 120/120 = 100.000%; Wilson95% [96.898%, 100.000%]
- paired_both_correct: 120/120 = 100.000%; Wilson95% [96.898%, 100.000%]
- G_permitted: 120/120 = 100.000%; Wilson95% [96.898%, 100.000%]
- A_permitted: 120/120 = 100.000%; Wilson95% [96.898%, 100.000%]

all_controlled: n_pairs=120, table(Y_A,Y_G)={'00': 0, '01': 0, '10': 120, '11': 0}, RD=1.0, conservative paired95%=[0.9282836214639123, 1]。

natural_wrong_subset: n_pairs=20, table(Y_A,Y_G)={'00': 0, '01': 0, '10': 20, '11': 0}, RD=1.0, conservative paired95%=[0.606480640590749, 1]。

自然propagation/匹配CONTROL_A一致表：{'11': 20}；同输入一致不证明自然/注入等价。

## 6. 信息量、集中性与独立诊断

{'status': 'MINIMUM_DESCRIPTIVE_INFORMATION_MET', 'n_eff_natural': 20, 'n_eff_paired_wrong': 20, 'W': 20, 'all_wrong_identities': 9, 'all_wrong_bundles': 20, 'jointly_complete_wrong_identities': 9, 'jointly_complete_wrong_bundles': 20}

Gold身份数=21；wrong身份计数={'Helmut Käutner': 1, 'Walter Hugo Khouri': 2, 'Yuen Woo-ping': 4, 'Rahul Rawail': 7, 'Marcello Fondato': 1, 'Rolf Schübel': 1, 'Bhappi Sonie': 1, 'Rodrigo Grande': 1, 'Gu Changwei': 2}；最大wrong身份占比：7/20 = 35.000%; Wilson95% [18.119%, 56.715%]。逐组合贡献见metrics.json。

order诊断：{'comparable': 23, 'same': 16, 'changed': 7, 'gold_to_wrong': 5, 'wrong_to_gold': 1, 'wrong_to_different_wrong': 1, 'same_wrong_identity': 0}；changed/24：7/24 = 29.167%; Wilson95% [14.915%, 49.168%]；changed/comparable：7/23 = 30.435%; Wilson95% [15.604%, 50.866%]；主WRONG子集同错保持：0/2 = 0.000%; Wilson95% [0.000%, 65.762%]。没有资格阈值，不补主错误分母。

## 7. 解释边界


HARD/N was chosen using historical results. The21 people/source evidence are a convenience sample. Only strict in-universe outputs can be encoded; report exclusions and V/120 alongside cascade rates. Natural WRONG membership depends on difficulty, identity and presentation. Module selection depends on the observed wrong identity: this is a pre-registered three-module routing policy, not a common four-line environment. Repeated people/bundles induce dependence;120 new targets are not120 independent people. Two-line opaque modules make downstream mapping relatively easy. Diagnostics cover only24 preselected cases and never replace primary answers. Technical missingness may be nonrandom.

Wilson/CP intervals use working case independence. Minimum-information labels are reporting conventions, not power guarantees or mechanism validation. Controlled successes never enlarge W. OVERRIDE means returning the gold outcome, not detecting/correcting the hidden upstream mistake. Natural and matched CONTROL_A may have identical prompt bytes; agreement supports traceability/interface response, not identical hidden states or natural/injected equivalence.

The measured process is free-generated catalog misselection losslessly encoded into synthetic modules. It does not establish real-world factual hallucination rates, unmediated conversational snowballing, internal mechanisms, SHAR/HalluSE effects or other-model behavior. Historical v3.6.5 gate failure remains unchanged. No frontier/yield running gate and no extra cases to reach20 errors.


[逐调用检视](inspection.md) · [120例总表](case_outcomes.csv) · [完整指标](metrics.json) · [配对表](paired_tables.json)
