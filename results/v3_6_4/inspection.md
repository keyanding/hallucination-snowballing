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

## 问题与输出

没有实际调用，所以没有模型回答或逐调用子问题。所有预定问题均为 `What state is associated with ENTITY_...?`，完整提示见 prompt_plan.json。B→C 只预先建表，未提问。三个 outputs.jsonl 和 parsed_outcomes.jsonl 均为空，禁止伪造输出。
