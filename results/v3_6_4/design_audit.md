# Pre-inference design audit

{
  "passed": true,
  "cases": 48,
  "globally_unique_identifiers": 1152,
  "all_levels_audited": 144,
  "reviewed_findings_components": 34,
  "warnings_addressed": 10
}

All48 cases,168 potential prompts (at most104 executed), compatibility mappings, parser/gates, and user resolution are frozen. Three difficulty levels have nested shared records, one unique gold path, no candidate lists/UNKNOWN/downstream outputs. No selection used model outputs. Original and effective specs retained.

# v3.6.4 pre-registration

## Data and manipulation
24 development and24 independent confirmation base cases; each has8 unique entity/marker/state paths and8 pre-frozen state-to-outcome mappings. Query is the first generated member; no gold label is shown. Seed3640 constructs all cases before inference. All1152 ENTITY/STATE/OUTCOME identifiers are globally unique and excluded from v3.6.0–v3.6.3.1 used or prepared cases. Every case has24 distinct suffixes. Token count is matched within each identifier family using the smallest eligible tokenizer bucket. Audit all7800 candidate identifiers; no model outputs select cases.
EASY/MID/HARD take the first3/5/8 paths of the same base case, retaining the same query/gold and the relative order of shared records. Entity records precede marker mappings. Two independently shuffled full8-member index orders (seed3640) are filtered for each level. Positions are random, not forced or claimed balanced. MID adds2 and HARD6 marker texture statements (smooth, rough, striped, dotted, plain, ridged); EASY has none. These add no entity-to-marker/state relation. Shared texture records remain identical. This compound selection-load manipulation adds relations and irrelevant attributes; it does not isolate their individual causal effects.
The frozen state universe for each rendered case is its visible3/5/8 states. The full8-state compatibility dictionary for every base case is prepared before outputs, never shown. Confirmation queries/entities/states/outcomes are disjoint from development. Markers/texture vocabulary intentionally recur; independence refers to fresh base cases and IDs, not an unobserved task distribution.

## Parsing and gate policy
Use the separately frozen user_resolution.json as the authoritative Valid-counting policy. Normalize NFC, outer strip and remove exactly one terminal period; no extraction, casefold or prefix repair. GOLD/TRACEABLE_WRONG/OUT_OF_UNIVERSE/INVALID depend on normalized whole text, regardless of truncation. TRUNCATED is orthogonal; censored responses never count as eligible Valid or qualified wrong. Always report raw categories and eligible counts separately. All denominators remain24, never filtered by validity. A completed wrong state qualifies only within the displayed case-level universe and its pre-frozen mapping. Confirmation tests independent yield, not recurrence of the same lexical state ID on disjoint cases.
Development qualifies with Valid>=22/24, eligible TRACEABLE_WRONG>=4/24, INVALID<=1/24, TRUNCATED<=1/24, and>=3 distinct wrong case IDs. Select easiest qualifying EASY, then MID, then HARD; no yield maximization. Confirmation same gates except wrong>=3/24. All criteria conjunctive. No threshold, case, budget, parser or prompt changes after inference.

## Schedules and conditional calls
72 development calls (seed3641 shuffled schedule with no adjacent same-case calls). All72 possible confirmation prompts and24 possible diagnostic prompts are frozen as contingencies, not all executed. Confirmation schedule shuffles24 cases per level using seeds3642/3643/3644. Eight development IDs sampled with seed3645, independent of model outputs. Each selected-level diagnostic uses one deterministic full record-block shuffle seeded by 'v364-order-'+case_id+'-'+level, leaving instructions/question unchanged. Maximum104 calls=72+24+8. No extra smoke, calibration, cap sweep, replay, scoring, constrained decoding or downstream calls.
If no development level qualifies, stop at72; confirmation/order files remain empty and evaluated=false. If a level qualifies, run24 confirmation then8 order calls regardless of confirmation success. No next experiment or automatic natural-state propagation. A genuine run/structure/hash/parser failure stops execution without retries or replacement.

## Non-gating order diagnostic
Compare paired normalized state identities only when both outputs are syntactically well-formed and untruncated (including OUT_OF_UNIVERSE); record incomparable pairs separately, never call unchanged prose a stable state. Report comparable coverage, same identity, changed identity, original/permuted Valid, both TRACEABLE_WRONG, same wrong identity, and all paired categories. More than3 of the fixed8 pairs changing identity sets ORDER_SENSITIVE_FRONTIER=true; otherwise false. Unrun means evaluated=false and flag=false, not observed stability. Invalid/incomparable pairs remain prominent even if flag=false. This diagnostic cannot alter the primary frontier gate.

## Inheritance and decision
Use the unchanged v3.5.1 generate() only (not its runner), same pinned Qwen3-4B-Instruct-2507 revision, tokenizer/chat template, NF4 double quantization/BF16, no offload, seed42, greedy, fresh one-user chats, use_cache=False; sole decoding change cap96. Token cap is a preventive choice, not a guarantee of no censoring. Snapshot prior ledger and verify all inherited source/result hashes before/after. C02 task, C04 category/truncation interface and C05 cap modifications are explicitly reviewed, not silently inherited validation.
Decision priority: real infrastructure failure/missing required calls -> INFRASTRUCTURE_FAILURE; no qualifying level -> NO_NATURAL_ERROR_FRONTIER; confirmation fail -> NATURAL_ERROR_FRONTIER_NOT_CONFIRMED; else NATURAL_ERROR_FRONTIER_CONFIRMED. Order flag separate.
Confirmed licenses reproducible nonzero natural first-hop wrong yield on this tested synthetic interface only. No natural downstream propagation, natural/injected equivalence, real-world hallucination rate, SHAR/HalluSE, internal mechanism or larger-model claim. Failure of this frozen design does not prove natural errors impossible. Incorporate result in project ledger; do not design/run v3.6.5 here.

## Post-run infrastructure failure audit

# v3.6.4 — INFRASTRUCTURE_FAILURE

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
