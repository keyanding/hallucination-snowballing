# v3.6.5 — HARD_N_SIGNAL_NOT_REPLICATED

只复现历史v3.4.4 HARD/N，不执行下游传播。实际调用：{'development': 24, 'presentation_diagnostic': 8, 'confirmation': 0}。

| 阶段 | Valid | Gold | Traceable wrong | Out-of-set | Ambiguous | Noncompliant | Truncated |
|---|---|---|---|---|---|---|---|
| 开发 | 24/24 | 21/24 | 3/24 | 0/24 | 0/24 | 0/24 | 0/24 |
| 确认 | 未运行 | — | — | — | — | — | — |

开发错误案例数：3；错误身份数：3。

非门槛呈现诊断：相同身份5/8、改变身份3/8；严格有效成对覆盖8/8；原始/置换严格有效分别8/8、8/8。gold→wrong=1，wrong→gold=1，wrong→different wrong=1，同一错误身份保持=0。PRESENTATION_SENSITIVE=False；诊断不改变主门槛，也不筛选错误案例。

历史HARD/N开发5/24错误信号未在这组新案例上达到预注册复现门槛；不追加难度搜索。

21位真实人物复用；48个图/目标新建，40组新组合、8组历史组合，开发与确认组合互不重复。自然错误仅指合成图任务中的自由生成人名错选，不是事实知识幻觉率。没有自然下游传播、注入/自然等价、内部机制、SHAR/HalluSE或其他模型结论。原始错误不修复。

[逐调用提示/输出](inspection.md) · [历史兼容审计](historical_interface_audit.md) · [预注册](pre_registration.md)

PRESENTATION_SENSITIVE=false只表示3/8未超过预注册的>3/8阈值，不表示记录顺序稳定。开发只差错误产出门槛；这也不是与历史5/24存在统计显著差异的证明。详见[诊断解释](diagnostic_observations.md)。
