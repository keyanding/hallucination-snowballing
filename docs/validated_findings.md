# 项目已验证发现台账

## How to use this file

截至 2026-10-08（Asia/Shanghai），来源提交 `165b522384ef242a18bedc3534dc456756c18dc7`。零新模型调用；信心等级针对注明范围内陈述，非总体效应或假说真值概率。

JSON是规范数据源；本Markdown、audit和CHANGELOG由同一数据源生成。F为发现、C为可复用组件、M为测量失败视图、Q为待解决问题。HIGH表示范围内有直接且较强记录支撑，不表示跨模型/总体普适；LOW的开放问题仍是假说。

状态计数（仅F条目；M/C不重复计数）：FROZEN_REUSE=9，ACTIVE_WARNING=10，INCONCLUSIVE=6，OPEN_QUESTION=2，RETIRED=0，SUPERSEDED=0。

FROZEN_REUSE仍受scope约束；ACTIVE_WARNING是有观察依据的设计约束；INCONCLUSIVE不是零效应；OPEN_QUESTION不是已成立结论；RETIRED/SUPERSEDED须给证据及去向。UNVERIFIED_HISTORY单列，绝不冒充有效发现。

## Project-level research question

模型自然产生的错误中间状态是否传播为下游被接受的错误，何种干预能减少它？

## Current research boundary

已验证显式符号跟随、至24条无关映射已测鲁棒性、上游查表与正确实际状态模块管线；未验证自然错误传播、集成底层能力或SHAR/HalluSE作用。

当前最强正结论是**模块化显式符号管线通过**；最重要限制是**自然错误传播仍未测，集成底层能力仍不确定**。所有百分比须保留分母；同一案例的条件/顺序重复不当作独立样本。

## Version-by-version evidence map

共18个已执行版本；另1个准备草稿不计实验。早期目录使用smoke/calibration前缀，同样纳入。

| 版本 | 阶段 | 冻结门槛/研究状态 |
|---|---|---|
| v1 | 语义依赖smoke | STOP：依赖失败 |
| v2 | 封闭知识组合smoke | STOP：0合格 |
| v2.1 | 自然语言提示诊断 | STOP：0合格 |
| v3 | 受控合成状态传播 | 量化门槛通过 |
| v3.1 | 真实实体上下文阶梯 | PASS；9/10可解释 |
| v3.2 | 上下文消融 | FAIL：可解释4/10 |
| v3.3 | 自然第一跳及反事实分支 | 反事实PASS；自然未测 |
| v3.4 | 可追溯候选宇宙 | STOP：第一跳门槛失败 |
| v3.4.1 | 三通道机制难度校准 | NO_STABLE_FRONTIER |
| v3.4.2 | 图深度×分支 | FAIL：POSITION_BIAS |
| v3.4.3 | 候选列表顺序反事实 | 测量有效；未确认前沿 |
| v3.4.4 | 答案接口/记录顺序 | N/EASY确认通过；yield不足 |
| v3.5.1 | 任务角色heading | STOP_INVALID |
| v3.6.0 | 符号传播校准 | STOP_ASSAY_INVALID |
| v3.6.1 | 最小接口诊断 | MINIMAL_ASSAY_VALIDATED |
| v3.6.2 | 无关映射累积 | ROBUST_CONTEXT_ASSAY |
| v3.6.3 | 上游+新下游shell | STOP_TWO_HOP_CALIBRATION_INVALID |
| v3.6.3.1 | 冻结接口真实状态管线 | TWO_HOP_PIPELINE_VALIDATED；集成未就绪 |

### v1 — 语义依赖smoke

**状态：STOP：依赖失败**

**研究问题：** 错误中间事实是否传播，oracle能否纠正？

**最小设计：** Qwen3-0.6B/SHARS wrapper；3题×3条件=9生成。

**关键结果（保留分母）：** 自然轨迹建立所需第一跳0/3；各条件最终正确0/3；PG/IE null；40例仅准备未运行。

**有效结论：** 未建立两步语义依赖，不能估计效应。

**未建立：** 没有传播强弱、自动修复或SHAR有效性证据。

**测量问题：** 直接关系捷径；父亲重复为祖父；地点回答年份；可解析不等于有效。

**后续设计含义：** 先验证依赖；oracle是外部纠正，不是模型修复。

证据：[results/smoke/inspection.md](../results/smoke/inspection.md)；[results/smoke/gate.json](../results/smoke/gate.json)；[results/smoke/metrics.json](../results/smoke/metrics.json)；[results/smoke/trajectories.jsonl](../results/smoke/trajectories.jsonl)

### v2 — 封闭知识组合smoke

**状态：STOP：0合格**

**研究问题：** 明确r1/r2分工能否建立可识别干预？

**最小设计：** 固定5真实案例；4B NF4/BF16，baseline/oracle/donor各5次，cap128。

**关键结果（保留分母）：** 三资格臂各0/5；全门槛0/5；注入0，传播率null。

**有效结论：** 给定样本中的知识/关系/粒度不足以支撑测量。

**未建立：** 不是自然传播率零；国家级兼容答案不自动虚假；未做模型大小匹配比较。

**测量问题：** 错误实体、城市/国家粒度；格式不保证语义。

**后续设计含义：** 分别校准下游知识、oracle和donor；冻结别名粒度。

证据：[results/smoke_v2/inspection.md](../results/smoke_v2/inspection.md)；[results/smoke_v2/metrics.json](../results/smoke_v2/metrics.json)；[results/smoke_v2/gate.json](../results/smoke_v2/gate.json)；[results/smoke_v2/protocol.md](../results/smoke_v2/protocol.md)

### v2.1 — 自然语言提示诊断

**状态：STOP：0合格**

**研究问题：** 自然问句与明确oracle前提是否恢复能力？

**最小设计：** 复用5例、15调用，与保存v2输出比较。

**关键结果（保留分母）：** baseline0/5、oracle1/5、donor1/5；全门槛0/5；3格式失败含2复制占位符；无截断/注入。

**有效结论：** 少量单臂改善，资格仍未建立。

**未建立：** 问句/前提/粒度同时变化，不能归因单一句话。

**测量问题：** 复制模板、知识及粒度不匹配。

**后续设计含义：** 分开语义、格式和粒度；不能以格式代替能力。

证据：[results/smoke_v2_1/diagnosis.md](../results/smoke_v2_1/diagnosis.md)；[results/smoke_v2_1/metrics.json](../results/smoke_v2_1/metrics.json)；[results/smoke_v2_1/gate.json](../results/smoke_v2_1/gate.json)；[results/smoke_v2_1/inspection.md](../results/smoke_v2_1/inspection.md)

### v3 — 受控合成状态传播

**状态：量化门槛通过**

**研究问题：** 提供下游事实后能否沿B/B′输出C/C′？

**最小设计：** 10合成案例×两证据顺序×4探针=80调用。

**关键结果（保留分母）：** 直接40/40，baseline状态20/20，注入状态20/20；10/10合格；无顺序变化/无效/拒绝。

**有效结论：** 该样本的显式查询和外部状态跟随可靠。

**未建立：** 不是自然幻觉；重复顺序不增加独立案例数；无真实/合成匹配效应。

**测量问题：** 相较v2改动证据、实体、提示、cap及缓存，不能唯一定位旧失败。

**后续设计含义：** 显式事实可隔离传播；保留双向控制。

证据：[results/smoke_v3/diagnosis.md](../results/smoke_v3/diagnosis.md)；[results/smoke_v3/metrics.json](../results/smoke_v3/metrics.json)；[results/smoke_v3/gate.json](../results/smoke_v3/gate.json)；[results/smoke_v3/protocol.md](../results/smoke_v3/protocol.md)

### v3.1 — 真实实体上下文阶梯

**状态：PASS；9/10可解释**

**研究问题：** 原问题/背景/第一跳证据如何影响状态？

**最小设计：** 10固定真实案例×H0–H3×4=160调用。

**关键结果（保留分母）：** 各层direct20/20；PR10/10、10/10、9/10、2/10；OR0/10、0/10、1/10、8/10；GSA10/10、10/10、9/10、10/10。

**有效结论：** 第一跳支持伴随更多gold方向覆盖，而直接查询保持成功。

**未建立：** 不是自然纠错、纯长度效应或内部机制；neutral背景仍有主题线索。

**测量问题：** H2一例gold失败、另一例override。

**后续设计含义：** 同时看GSA/PR；语义背景不同于无关映射条数。

证据：[results/smoke_v3_1/diagnosis.md](../results/smoke_v3_1/diagnosis.md)；[results/smoke_v3_1/metrics.json](../results/smoke_v3_1/metrics.json)；[results/smoke_v3_1/gate.json](../results/smoke_v3_1/gate.json)；[results/smoke_v3_1/context_audit.md](../results/smoke_v3_1/context_audit.md)

### v3.2 — 上下文消融

**状态：FAIL：可解释4/10**

**研究问题：** 长度、名字、关系证据和冲突顺序有何影响？

**最小设计：** 统一H1底稿，8条件×10例×4=320调用。

**关键结果（保留分母）：** C0/C1/C2/C3/C4/C5/C6a/C6b PR为10/10、10/10、10/10、8/10、4/10、10/10、10/10、10/10；direct160/160；C5 GSA4/10；可解释4/10<8/10。

**有效结论：** 替代支持可覆盖两个方向的状态；高PR不是测量可靠性。

**未建立：** 整体未通过；C4与旧H3底稿不同，不是精确复现失败；不能推普遍顺序无关。

**测量问题：** C5破坏gold控制；C2一例gold失败；C6两顺序差异0/10。

**后续设计含义：** 失败保留原分母；跨版比完整提示。

证据：[results/smoke_v3_2/diagnosis.md](../results/smoke_v3_2/diagnosis.md)；[results/smoke_v3_2/metrics.json](../results/smoke_v3_2/metrics.json)；[results/smoke_v3_2/gate.json](../results/smoke_v3_2/gate.json)；[results/smoke_v3_2/context_ablation_audit.md](../results/smoke_v3_2/context_ablation_audit.md)

### v3.3 — 自然第一跳及反事实分支

**状态：反事实PASS；自然未测**

**研究问题：** 自然错误是否可追溯传播？

**最小设计：** 12第一跳+24lookup+132注册反事实探针=168调用；逐例停止无证据自然分支。

**关键结果（保留分母）：** 非gold12/12；人工身份可证9/12，3未核实；合格自然下游关系0/12，NPR分母0/null。S0 CPR12/12；E0/E1/E2/E3a/E3b为11/12、0/12、12/12、4/12、12/12。

**有效结论：** 支持与顺序改变注册反事实目标选择；自然传播未测。

**未建立：** 不能说12个都是已证真实实体；不能把反事实加进自然分母。

**测量问题：** 地点出现在电影标题不是birthplace证据；自动索引身份1/12不等于人工9/12；冲突wrong8/12、gold5/12答案变更。

**后续设计含义：** 核实关系而非字符串共现；自然/反事实分层。

证据：[results/smoke_v3_3/diagnosis.md](../results/smoke_v3_3/diagnosis.md)；[results/smoke_v3_3/metrics.json](../results/smoke_v3_3/metrics.json)；[results/smoke_v3_3/gate.json](../results/smoke_v3_3/gate.json)；[results/smoke_v3_3/eligibility_review.json](../results/smoke_v3_3/eligibility_review.json)；[results/smoke_v3_3/natural_evidence_search.json](../results/smoke_v3_3/natural_evidence_search.json)；[results/smoke_v3_3/review.json](../results/smoke_v3_3/review.json)

### v3.4 — 可追溯候选宇宙

**状态：STOP：第一跳门槛失败**

**研究问题：** 全候选都有下游映射能否产生自然错选？

**最小设计：** 20题四候选组合证据；只跑20第一跳，cap32。

**关键结果（保留分母）：** 正确11/20，traceable wrong0/20，parseable out-of-set0/20，INVALID9/20且全截断；valid11<15，错误0<5；下游0调用、指标null。

**有效结论：** 解决映射覆盖并未产生合格自然错误。

**未建立：** 不能报全样本100%正确；无效说明不是自然错误状态；lookup也未测。

**测量问题：** 解释性输出与32-token截断；能力/格式未分离。

**后续设计含义：** 独立校准输出协议，不从解释抽取候选补分母。

证据：[results/smoke_v3_4/diagnosis.md](../results/smoke_v3_4/diagnosis.md)；[results/smoke_v3_4/metrics.json](../results/smoke_v3_4/metrics.json)；[results/smoke_v3_4/gate.json](../results/smoke_v3_4/gate.json)；[results/smoke_v3_4/first_hop_generations.jsonl](../results/smoke_v3_4/first_hop_generations.jsonl)

### v3.4.1 — 三通道机制难度校准

**状态：NO_STABLE_FRONTIER**

**研究问题：** 四机制是否给出合格错误前沿？

**最小设计：** 每机制6例×4难度=96提示、F/C/L；12held-out未查询。

**关键结果（保留分母）：** M1错0/6、0/6、1/6、0/6；M2/M3全0/6；M4错1/6、0/6、0/6、2/6。M4/D3近边界0/6<4/6；FSC/FCA/LCA96/96，截断0。

**有效结论：** 没有稳定且全门槛合格前沿；三通道在4错选上也一致。

**未建立：** 无普遍难度单调/通道等价；cap96不是单独致效实验。

**测量问题：** 错误网格粗、非单调，候选不等强；人工独立审计pending。

**后续设计含义：** 不放宽门槛，不用held-out调参。

证据：[results/calibration_v3_4_1/diagnosis.md](../results/calibration_v3_4_1/diagnosis.md)；[results/calibration_v3_4_1/metrics.json](../results/calibration_v3_4_1/metrics.json)；[results/calibration_v3_4_1/gate.json](../results/calibration_v3_4_1/gate.json)；[results/calibration_v3_4_1/design_audit.pre_inference.md](../results/calibration_v3_4_1/design_audit.pre_inference.md)

### v3.4.2 — 图深度×分支

**状态：FAIL：POSITION_BIAS**

**研究问题：** 深度与分支是否形成渐进前沿？

**最小设计：** 8开发例×4深度×3分支=96提示，F/C/L；12held-out未跑。

**关键结果（保留分母）：** 错38/96；第一位置54/96，承载34/38错；D3B0/D4B2被位置规则排除；深度/分支margin非增7/9、7/8；F/C有效96/96，LCA95/96。

**有效结论：** 有部分难度趋势与强位置关联，需顺序反事实。

**未建立：** 固定位置无法区分身份/位置因果；96为重复观察；无held-out实测失败。

**测量问题：** 两例贡献24/38错；深度/分支与长度共变。

**后续设计含义：** 前沿确认前排查位置，不只看错误率。

证据：[results/calibration_v3_4_2/diagnosis.md](../results/calibration_v3_4_2/diagnosis.md)；[results/calibration_v3_4_2/metrics.json](../results/calibration_v3_4_2/metrics.json)；[results/calibration_v3_4_2/gate.json](../results/calibration_v3_4_2/gate.json)；[results/calibration_v3_4_2/position_audit.md](../results/calibration_v3_4_2/position_audit.md)

### v3.4.3 — 候选列表顺序反事实

**状态：测量有效；未确认前沿**

**研究问题：** 只旋转答案列表能否改变选择？

**最小设计：** 6有意选旧例×3难度×4旋转=72提示/216通道评估。

**关键结果（保留分母）：** 身份变化11/18集合；第一位置37/72，E/M/H为8/24、13/24、16/24；F严格68/72含4截断；C有效72/72，L/C72/72；18/18旧P1原文/选择/分数复现。

**有效结论：** 这些输入上的列表顺序干预有行为因果效应，描述性随难度增强。

**未建立：** 不是总选第一、内部机制或普遍效应；18集合嵌套6例；列表不等同证据顺序。

**测量问题：** 6/18位置1锁定、7/18gold稳定；无非gold身份4/4稳定集合。

**后续设计含义：** 均衡曝光不等于消偏；需新独立开发确认。

证据：[results/calibration_v3_4_3/diagnosis.md](../results/calibration_v3_4_3/diagnosis.md)；[results/calibration_v3_4_3/metrics.json](../results/calibration_v3_4_3/metrics.json)；[results/calibration_v3_4_3/gate.json](../results/calibration_v3_4_3/gate.json)；[results/calibration_v3_4_3/prompt_diff_audit.md](../results/calibration_v3_4_3/prompt_diff_audit.md)；[results/calibration_v3_4_3/frontier_salvage.md](../results/calibration_v3_4_3/frontier_salvage.md)

### v3.4.4 — 答案接口/记录顺序

**状态：N/EASY确认通过；yield不足**

**研究问题：** 去列表、旋转记录、旋转选项影响如何？

**最小设计：** 24新开发+16确认+6旧诊断；882renderings/2116主通道评估，另11检查。

**关键结果（保留分母）：** L第一位置E/M/H=25/96、45/96、67/96；身份敏感2/24、14/24、20/24。N各24/24有效，错0/24、1/24、5/24；R敏感0/24、4/24、14/23；N/EASY确认16/16有效、错0/16。L/R各0/72开发cells有同错身份4/4。

**有效结论：** 列表/记录顺序敏感都存在；N/EASY单轨迹接口确认但无错误yield。

**未建立：** 不是传播就绪；N/L还改措辞/解码；评分不算自然生成；无稳定错误证据。

**测量问题：** L HARD错52/96，N错5/24；R HARD最早41/95。

**后续设计含义：** 自由与约束通道分开，错误yield独立设门槛。

证据：[results/calibration_v3_4_4/README.md](../results/calibration_v3_4_4/README.md)；[results/calibration_v3_4_4/diagnosis.md](../results/calibration_v3_4_4/diagnosis.md)；[results/calibration_v3_4_4/gate.json](../results/calibration_v3_4_4/gate.json)；[results/calibration_v3_4_4/metrics.json](../results/calibration_v3_4_4/metrics.json)；[results/calibration_v3_4_4/supplementary_diagnostics.md](../results/calibration_v3_4_4/supplementary_diagnostics.md)；[results/calibration_v3_4_4/format_smoke.json](../results/calibration_v3_4_4/format_smoke.json)

### v3.5.1 — 任务角色heading

**状态：STOP_INVALID**

**研究问题：** 当前/背景heading是否调节传播？

**最小设计：** 12匿名影片/真实人物映射×6=72主+16辅助。

**关键结果（保留分母）：** S0 Cp9/12；C0 C9/12<10/12，另2Cp+1UNKNOWN；两个G heading各C12/12，ΔOR/PR0/12；辅助16/16。

**有效结论：** 两个heading输出相同，但主状态控制失败，调节机制未识别。

**未建立：** 不证明heading普遍无效或权威机制；辅助不能挽救C0。

**测量问题：** 合规不保证状态跟随；真实知识影响未独立分离。

**后续设计含义：** 先验证稳定状态测量，再测heading。

证据：[results/v3_5_1/README.md](../results/v3_5_1/README.md)；[results/v3_5_1/metrics.json](../results/v3_5_1/metrics.json)；[results/v3_5_1/gate.json](../results/v3_5_1/gate.json)；[results/v3_5_1/diagnosis.md](../results/v3_5_1/diagnosis.md)

### v3.6.0 — 符号传播校准

**状态：STOP_ASSAY_INVALID**

**研究问题：** full shell/UNKNOWN/不变性控制是否有效？

**最小设计：** 20校准×8正式条件=160；40main未跑。

**关键结果（保留分母）：** A–H=39/40、17/20、20/20、19/20、15/20、20/20、160/160、17/20；B/E/H失败，main0/80。

**有效结论：** full shell未通过；反序和实体标签可改答案。

**未建立：** H不是17/20正确率；3个标签差异均纠正；E5差异为3纠正+2新错。

**测量问题：** 有映射时UNKNOWN；token数未区分错例；不变性与正确性不同。

**后续设计含义：** fallback/实体表面不可默认为无害；并报invariance与accuracy。

证据：[results/v3_6_0/README.md](../results/v3_6_0/README.md)；[results/v3_6_0/calibration_gate.json](../results/v3_6_0/calibration_gate.json)；[results/v3_6_0/gate.json](../results/v3_6_0/gate.json)；[results/v3_6_0/calibration_outputs.jsonl](../results/v3_6_0/calibration_outputs.jsonl)

### v3.6.1 — 最小接口诊断

**状态：MINIMAL_ASSAY_VALIDATED**

**研究问题：** 最小shell能否可靠执行状态映射？

**最小设计：** 旧例四模板160+fresh成对80+unmapped10+反序20=270。

**关键结果（保留分母）：** FULL_UNKNOWN39/40，其他三模板40/40；fresh C0/W0/paired各40/40；误UNKNOWN/OTHER/INVALID均0/80；unmapped10/10，反序20/20。

**有效结论：** 最小primitive通过；fallback/full交互只是小线索。

**未建立：** 短UNKNOWN句不是旧版精确重放；一例差异非普遍因果；未做更大模型比较。

**测量问题：** prompt/ID构造共同变化；40/40 Wilson95%下限约91.2%。

**后续设计含义：** 复用确切模板；mapped不需UNKNOWN，unmapped独立检验。

证据：[results/v3_6_1/README.md](../results/v3_6_1/README.md)；[results/v3_6_1/stage_b_metrics.json](../results/v3_6_1/stage_b_metrics.json)；[results/v3_6_1/stage_c_metrics.json](../results/v3_6_1/stage_c_metrics.json)；[results/v3_6_1/interpretation.md](../results/v3_6_1/interpretation.md)；[results/v3_6_1/v360_failure_audit.json](../results/v3_6_1/v360_failure_audit.json)；[results/v3_6_1/gate.json](../results/v3_6_1/gate.json)

### v3.6.2 — 无关映射累积

**状态：ROBUST_CONTEXT_ASSAY**

**研究问题：** K至24及位置改变是否降低primitive？

**最小设计：** 40基础×4K×2=320；12例K24×3位置×2=72。

**关键结果（保留分母）：** K0/4/12/24各C0/W0/paired40/40，UNKNOWN/OTHER/INVALID0；Δ全0；各位置24/24。

**有效结论：** 已测无冲突符号记录/位置范围可靠。

**未建立：** 不推任意长上下文、语义冲突或普遍位置无关；72诊断来自12例。

**测量问题：** 和早期语义背景不是同操纵；零事件非零总体风险。

**后续设计含义：** 保留最小shell基线，变背景类型重新校准。

证据：[results/v3_6_2/README.md](../results/v3_6_2/README.md)；[results/v3_6_2/metrics.json](../results/v3_6_2/metrics.json)；[results/v3_6_2/position_diagnostic_metrics.json](../results/v3_6_2/position_diagnostic_metrics.json)；[results/v3_6_2/gate.json](../results/v3_6_2/gate.json)

### v3.6.3 — 上游+新下游shell

**状态：STOP_TWO_HOP_CALIBRATION_INVALID**

**研究问题：** 上游与recorded shell能否组成两跳？

**最小设计：** 20校准×4=80；main/pipeline/integrated/order均停止。

**关键结果（保留分母）：** U两臂/paired20/20；P-GOLD18/20、P-ALT19/20、paired17/20；permitted77/80；C/F/G失败。3INVALID含1截断、1缺前缀、1整句。

**有效结论：** 上游校准成功；下游合规失败阻断整体。

**未建立：** integrated false/evaluated=false是未跑；代码测试不算pipeline实测。

**测量问题：** 介绍、heading、位置、指令及新ID共同变动。

**后续设计含义：** 不默改验证模板；新shell独立校准。

证据：[results/v3_6_3/README.md](../results/v3_6_3/README.md)；[results/v3_6_3/calibration_gate.json](../results/v3_6_3/calibration_gate.json)；[results/v3_6_3/gate.json](../results/v3_6_3/gate.json)；[results/v3_6_3/interpretation.md](../results/v3_6_3/interpretation.md)；[results/v3_6_3/calibration_outputs.jsonl](../results/v3_6_3/calibration_outputs.jsonl)

### v3.6.3.1 — 冻结接口真实状态管线

**状态：TWO_HOP_PIPELINE_VALIDATED；集成未就绪**

**研究问题：** 原样转发实际U输出能否完成两跳？

**最小设计：** 20校准+40main+10独立shell+20main集成子集；80+200+40+40=360。

**关键结果（保留分母）：** 校准A–F20/20、G80/80；主六指标各40/40，G7 0/160；40实际状态不修复。Current20/20 vs Recorded17/20；I-A7/20、I-B9/20、paired2/20；24INVALID中17截断。

**有效结论：** 模块管线与反事实切换通过；单提示exact接口未就绪。

**未建立：** 底层集成能力不确定；U-A全对，自然错误传播未测；加长cap未验证。

**测量问题：** Recorded3失败全解释截断；集成合规与cap16混合限制。

**后续设计含义：** 复用模块接口；另预注册集成协议/cap检验，不追改历史。

证据：[results/v3_6_3_1/README.md](../results/v3_6_3_1/README.md)；[results/v3_6_3_1/gate.json](../results/v3_6_3_1/gate.json)；[results/v3_6_3_1/metrics.json](../results/v3_6_3_1/metrics.json)；[results/v3_6_3_1/integrated_metrics.json](../results/v3_6_3_1/integrated_metrics.json)；[results/v3_6_3_1/shell_diagnostic_metrics.json](../results/v3_6_3_1/shell_diagnostic_metrics.json)；[results/v3_6_3_1/diagnostic_observations.md](../results/v3_6_3_1/diagnostic_observations.md)；[results/v3_6_3_1/parsed_outcomes.jsonl](../results/v3_6_3_1/parsed_outcomes.jsonl)

准备草稿：[results/calibration_v3_4_1_preparation_draft/README.md](../results/calibration_v3_4_1_preparation_draft/README.md)；War标题误作genre在推理前修正，未运行模型，不计第二次实验。

## Consolidated findings

### Measurement validity

#### F01 — 先验证资格，失败门槛不产生主效应

状态：**ACTIVE_WARNING**；信心：**HIGH**；版本：v1, v2, v3.2, v3.5.1, v3.6.0。

**范围：** 各版各自冻结门槛。

**精确结果：** v1依赖0/3；v2合格0/5；v3.2可解释4/10；v3.5.1 C0 9/12；v3.6.0 main0/80。

**设计含义：** 停止后报告null/未跑，保留失败样本；辅助不能救主控制。

**不要推断：** null不是0%；单元测试不是模型结果；失败assay不支持机制。

替代：无；被替代：无；开放跟进：Q01, Q02。

证据：[results/smoke/inspection.md](../results/smoke/inspection.md)；[results/smoke_v2/metrics.json](../results/smoke_v2/metrics.json)；[results/smoke_v3_2/gate.json](../results/smoke_v3_2/gate.json)；[results/v3_5_1/README.md](../results/v3_5_1/README.md)；[results/v3_6_0/gate.json](../results/v3_6_0/gate.json)

#### F02 — 封闭知识、关系与粒度是早期瓶颈

状态：**ACTIVE_WARNING**；信心：**MEDIUM**；版本：v2, v2.1, v3。

**范围：** 5例真实闭卷与10例不同合成显式事实任务。

**精确结果：** v2三臂各0/5；v2.1为0/5、1/5、1/5；v3 direct40/40。

**设计含义：** 先校准关系/实体/粒度；显式下游映射可隔离查询和传播。

**不要推断：** 跨版多因素不能证明世界知识是唯一原因；兼容粗粒度不自动虚假。

替代：无；被替代：无；开放跟进：Q01。

证据：[results/smoke_v2/inspection.md](../results/smoke_v2/inspection.md)；[results/smoke_v2/metrics.json](../results/smoke_v2/metrics.json)；[results/smoke_v2_1/diagnosis.md](../results/smoke_v2_1/diagnosis.md)；[results/smoke_v3/diagnosis.md](../results/smoke_v3/diagnosis.md)

#### F17 — 自由、约束和评分通道不可自动互换

状态：**ACTIVE_WARNING**；信心：**MEDIUM**；版本：v3.4.1, v3.4.3, v3.4.4。

**范围：** F自然生成/C受限选择/L或S似然各有不同观察单位。

**精确结果：** v3.4.1三通道96/96一致；v3.4.3 F严格68/72、C有效72/72；v3.4.4 HARD L-C错52/96、N-F错5/24。

**设计含义：** 显式分母/通道/valid条件；自然轨迹不可由受限选择代替。

**不要推断：** N/L还改措辞/解码，非纯列表因果；score不是校准概率。

替代：无；被替代：无；开放跟进：Q01。

证据：[results/calibration_v3_4_1/diagnosis.md](../results/calibration_v3_4_1/diagnosis.md)；[results/calibration_v3_4_3/diagnosis.md](../results/calibration_v3_4_3/diagnosis.md)；[results/calibration_v3_4_4/README.md](../results/calibration_v3_4_4/README.md)；[results/calibration_v3_4_4/supplementary_diagnostics.md](../results/calibration_v3_4_4/supplementary_diagnostics.md)

#### F26 — 精确解析及原始输出保留可复用

状态：**FROZEN_REUSE**；信心：**HIGH**；版本：v3.6.3, v3.6.3.1。

**范围：** uppercase opaque IDs；NFC/外侧strip/去一末尾句点，截断INVALID。

**精确结果：** 137测试；360token回译/分类复核，40原始状态转发验证。

**设计含义：** 不抽取不修前缀；新答案格式须重验parser。

**不要推断：** 精确格式不等于事实正确，不通用于所有自然语言。

替代：无；被替代：无；开放跟进：Q02。

证据：[experiments/v3_6_3/design.py](../experiments/v3_6_3/design.py)；[experiments/v3_6_3_1/design.py](../experiments/v3_6_3_1/design.py)；[tests/test_v3_6_3_1.py](../tests/test_v3_6_3_1.py)；[results/v3_6_3_1/tests.log](../results/v3_6_3_1/tests.log)；[results/v3_6_3_1/independent_verification.json](../results/v3_6_3_1/independent_verification.json)

#### F27 — 固定stateless greedy栈在当前接口可复用

状态：**FROZEN_REUSE**；信心：**HIGH**；版本：v3.6.1, v3.6.2, v3.6.3.1。

**范围：** Qwen3-4B-Instruct-2507 revision cdbee75f17c01a7cc42f958dc650907174af0554；NF4/BF16，greedy seed42、fresh chat、use_cache=False。

**精确结果：** 同栈primitive重复通过；最新360输出/渲染/token核验。

**设计含义：** 冻结模型/模板/isolation；cap16仅继承已验证单ID组件，集成须响应F14。

**不要推断：** 不是cap16适合所有任务、跨硬件逐bit复现或量化等价证明。

替代：无；被替代：无；开放跟进：Q02, Q09。

证据：[results/v3_6_3_1/decoding_freeze.json](../results/v3_6_3_1/decoding_freeze.json)；[results/v3_6_3_1/model_manifest.json](../results/v3_6_3_1/model_manifest.json)；[results/v3_6_3_1/independent_verification.json](../results/v3_6_3_1/independent_verification.json)；[experiments/v3_5_1/run_pilot.py](../experiments/v3_5_1/run_pilot.py)

### State propagation

#### F03 — 最小符号状态传播已重复通过

状态：**FROZEN_REUSE**；信心：**HIGH**；版本：v3.6.1, v3.6.2, v3.6.3.1。

**范围：** 同一4B NF4/BF16，明确无冲突STATE→OUTCOME。

**精确结果：** v3.6.1 C0/W0/paired各40/40；v3.6.2每K各40/40；v3.6.3.1 D-A/D-B/paired各40/40。

**设计含义：** 复用作为后续基线，保留双向及paired控制。

**不要推断：** 不是自然事实、任意上下文或自然错误率；重复条件非独立样本。

替代：无；被替代：无；开放跟进：Q01。

证据：[results/v3_6_1/stage_c_metrics.json](../results/v3_6_1/stage_c_metrics.json)；[results/v3_6_1/README.md](../results/v3_6_1/README.md)；[results/v3_6_2/metrics.json](../results/v3_6_2/metrics.json)；[results/v3_6_3_1/metrics.json](../results/v3_6_3_1/metrics.json)

#### F05 — 支持上下文可覆盖状态，高PR不代表可靠

状态：**ACTIVE_WARNING**；信心：**HIGH**；版本：v3.1, v3.2, v3.3, v3.5.1。

**范围：** 选定实体/第一跳支持文本。

**精确结果：** v3.1 H3 PR2/10；v3.2 C5 PR10/10但GSA4/10；v3.3 E2 CPR12/12但GSA1/12。

**设计含义：** 两个状态方向均须检查；不得隐藏gold控制失败。

**不要推断：** 不是自然纠错/内部检测，不否定最小符号primitive。

替代：无；被替代：无；开放跟进：Q01, Q06。

证据：[results/smoke_v3_1/diagnosis.md](../results/smoke_v3_1/diagnosis.md)；[results/smoke_v3_2/diagnosis.md](../results/smoke_v3_2/diagnosis.md)；[results/smoke_v3_3/diagnosis.md](../results/smoke_v3_3/diagnosis.md)；[results/v3_5_1/README.md](../results/v3_5_1/README.md)

### Context accumulation

#### F08 — 至24条无关映射未见传播下降

状态：**FROZEN_REUSE**；信心：**HIGH**；版本：v3.6.2。

**范围：** 40基础案例、K0/4/12/24嵌套不冲突记录。

**精确结果：** 每K C0/W0/paired40/40；main320无UNKNOWN/OTHER/INVALID；ΔS0/40。

**设计含义：** 基本管线可复用此基线；新背景类型重新校准。

**不要推断：** 不是任意长上下文或有语义/冲突支持也无效应。

替代：无；被替代：无；开放跟进：Q08。

证据：[results/v3_6_2/README.md](../results/v3_6_2/README.md)；[results/v3_6_2/metrics.json](../results/v3_6_2/metrics.json)；[results/v3_6_2/pre_registration.md](../results/v3_6_2/pre_registration.md)

### Upstream A→B capability

#### F10 — 显式上游A→B在固定shell中可靠

状态：**FROZEN_REUSE**；信心：**HIGH**；版本：v3.6.3, v3.6.3.1。

**范围：** 不透明双ENTITY→STATE显式查表。

**精确结果：** 旧两臂/paired各20/20；新校准各20/20，主两臂各40/40。

**设计含义：** 原样复用；增加关系复杂度/自然知识需新资格检查。

**不要推断：** 不表示真实世界第一跳可靠，也无自然错选样本。

替代：无；被替代：无；开放跟进：Q01。

证据：[experiments/v3_6_3/design.py](../experiments/v3_6_3/design.py)；[results/v3_6_3/calibration_gate.json](../results/v3_6_3/calibration_gate.json)；[results/v3_6_3_1/calibration_gate.json](../results/v3_6_3_1/calibration_gate.json)；[results/v3_6_3_1/metrics.json](../results/v3_6_3_1/metrics.json)

### Modular two-hop pipeline

#### F11 — 实际生成状态模块化两跳已验证

状态：**FROZEN_REUSE**；信心：**HIGH**；版本：v3.6.3.1。

**范围：** 40fresh主例；独立U-A后原样转发归一化实际输出。

**精确结果：** 严格E2E40/40；条件下游40/40；40实际状态核验，无skip/修复。

**设计含义：** 复用真实转发、invalid跳过、错上游不被末端偶然C掩盖的计分。

**不要推断：** 本次上游全对；wrong/unmapped只代码路径测试，未实测自然错误管线。

替代：无；被替代：无；开放跟进：Q01, Q03。

证据：[results/v3_6_3_1/metrics.json](../results/v3_6_3_1/metrics.json)；[results/v3_6_3_1/pipeline_log.jsonl](../results/v3_6_3_1/pipeline_log.jsonl)；[results/v3_6_3_1/pipeline_generated_outputs.jsonl](../results/v3_6_3_1/pipeline_generated_outputs.jsonl)；[results/v3_6_3_1/independent_verification.json](../results/v3_6_3_1/independent_verification.json)

### Integrated two-hop execution

#### F13 — 集成两跳底层能力仍不可判定

状态：**INCONCLUSIVE**；信心：**HIGH**；版本：v3.6.3, v3.6.3.1。

**范围：** 只有新版本真正运行20例×两实体；exact outcome/cap16。

**精确结果：** I-A7/20、I-B9/20、paired2/20；24失败全INVALID，17截断；旧版集成未跑。

**设计含义：** 历史ready=false保留；新设计先分离输出协议/长度与能力。

**不要推断：** 不能断言不会两跳；不抽链末答案追改成功；加cap不保证恢复。

替代：无；被替代：无；开放跟进：Q02。

证据：[results/v3_6_3/gate.json](../results/v3_6_3/gate.json)；[results/v3_6_3_1/integrated_metrics.json](../results/v3_6_3_1/integrated_metrics.json)；[results/v3_6_3_1/integrated_outputs.jsonl](../results/v3_6_3_1/integrated_outputs.jsonl)；[results/v3_6_3_1/diagnostic_observations.md](../results/v3_6_3_1/diagnostic_observations.md)

### Natural first-hop error generation

#### F18 — 未建立稳定可用的自然错误前沿

状态：**INCONCLUSIVE**；信心：**HIGH**；版本：v3.4.1, v3.4.2, v3.4.3, v3.4.4。

**范围：** 各自开发/诊断/确认设计，不是统一连续难度标尺。

**精确结果：** v3.4.1无前沿；v3.4.2候选cell被position排除；最新确认错0/16，L/R同错4/4各0/72开发cells。

**设计含义：** 需新独立前沿与错误yield确认，不能按错挑例或放宽阈值。

**不要推断：** 不是已取得顺序稳定错误状态，也非所有任务均不能产错。

替代：无；被替代：无；开放跟进：Q01。

证据：[results/calibration_v3_4_1/gate.json](../results/calibration_v3_4_1/gate.json)；[results/calibration_v3_4_1/diagnosis.md](../results/calibration_v3_4_1/diagnosis.md)；[results/calibration_v3_4_2/gate.json](../results/calibration_v3_4_2/gate.json)；[results/calibration_v3_4_2/diagnosis.md](../results/calibration_v3_4_2/diagnosis.md)；[results/calibration_v3_4_3/frontier_salvage.md](../results/calibration_v3_4_3/frontier_salvage.md)；[results/calibration_v3_4_4/gate.json](../results/calibration_v3_4_4/gate.json)；[results/calibration_v3_4_4/README.md](../results/calibration_v3_4_4/README.md)

#### F19 — 合格自然错误产出持续不足

状态：**ACTIVE_WARNING**；信心：**HIGH**；版本：v3.3, v3.4, v3.4.4, v3.6.3.1。

**范围：** 已执行传播分支及被选择/确认的路线；自然状态需未强制生成、有效、错误且关系证据可追溯，不表示所有开发条件都没有错选。

**精确结果：** v3.3非gold12/12但关系资格0；v3.4 wrong0/20；v3.4.4确认错0/16；最新U-A错0/40。 v3.4.4 HARD N确有5/24自然错选，但不是被选中并确认的传播路线，且没有执行其下游传播。

**设计含义：** 自然错误yield与证据资格前置；零合格传播率null。

**不要推断：** 注入B′不补自然分母；零合格不等于零传播。

替代：无；被替代：无；开放跟进：Q01。

证据：[results/smoke_v3_3/eligibility_review.json](../results/smoke_v3_3/eligibility_review.json)；[results/smoke_v3_3/diagnosis.md](../results/smoke_v3_3/diagnosis.md)；[results/smoke_v3_4/metrics.json](../results/smoke_v3_4/metrics.json)；[results/smoke_v3_4/diagnosis.md](../results/smoke_v3_4/diagnosis.md)；[results/calibration_v3_4_4/gate.json](../results/calibration_v3_4_4/gate.json)；[results/v3_6_3_1/metrics.json](../results/v3_6_3_1/metrics.json)；[results/calibration_v3_4_4/README.md](../results/calibration_v3_4_4/README.md)

### Prompt / presentation brittleness

#### F04 — Current state最小shell是已验证接口

状态：**FROZEN_REUSE**；信心：**HIGH**；版本：v3.6.1, v3.6.2, v3.6.3.1。

**范围：** 无entity、选项列表和mapped UNKNOWN句的完整minimal shell。

**精确结果：** 新validated提示逐字匹配v3.6.1 minimal及v3.6.2 K0；主80/80、独立shell20/20。

**设计含义：** 按C01渲染器逐字复用；变化须声明和重验。

**不要推断：** 不是Current state单独两个词的因果效应。

替代：无；被替代：无；开放跟进：Q02。

证据：[experiments/v3_6_1/design.py](../experiments/v3_6_1/design.py)；[experiments/v3_6_2/design.py](../experiments/v3_6_2/design.py)；[experiments/v3_6_3_1/design.py](../experiments/v3_6_3_1/design.py)；[results/v3_6_3_1/prompt_diff_audit.md](../results/v3_6_3_1/prompt_diff_audit.md)；[results/v3_6_3_1/README.md](../results/v3_6_3_1/README.md)

#### F07 — Recorded整套shell存在精确合规风险

状态：**ACTIVE_WARNING**；信心：**HIGH**；版本：v3.6.3, v3.6.3.1。

**范围：** 同模型/cap16；后者10独立例×2状态matched整个shell。

**精确结果：** 旧P两臂18/20、19/20；新Current20/20 vs Recorded17/20，3discordance均不利Recorded。

**设计含义：** 主管线复用验证shell；Recorded仅明确重测。

**不要推断：** 不证明单个heading、内部机制或旧失败唯一原因。

替代：无；被替代：无；开放跟进：Q02。

证据：[results/v3_6_3/interpretation.md](../results/v3_6_3/interpretation.md)；[results/v3_6_3/calibration_outputs.jsonl](../results/v3_6_3/calibration_outputs.jsonl)；[results/v3_6_3_1/shell_diagnostic_metrics.json](../results/v3_6_3_1/shell_diagnostic_metrics.json)；[results/v3_6_3_1/shell_diagnostic_outputs.jsonl](../results/v3_6_3_1/shell_diagnostic_outputs.jsonl)

#### F15 — 候选列表位置偏差随已测难度增加

状态：**ACTIVE_WARNING**；信心：**HIGH**；版本：v3.4.2, v3.4.3, v3.4.4。

**范围：** 6选定旧例与24新开发例的循环列表旋转。

**精确结果：** 旧身份变化11/18集合，位置1=8/24→13/24→16/24；新身份敏感2/24→14/24→20/24，位置1=25/96→45/96→67/96。

**设计含义：** 避开未校准列表或明确重测完整order控制；按基础例分析。

**不要推断：** 均衡曝光不等于消偏；非总选第一；不解释全部错或内部机制。

替代：无；被替代：无；开放跟进：Q01, Q08。

证据：[results/calibration_v3_4_2/position_audit.md](../results/calibration_v3_4_2/position_audit.md)；[results/calibration_v3_4_3/diagnosis.md](../results/calibration_v3_4_3/diagnosis.md)；[results/calibration_v3_4_3/prompt_diff_audit.md](../results/calibration_v3_4_3/prompt_diff_audit.md)；[results/calibration_v3_4_4/README.md](../results/calibration_v3_4_4/README.md)；[results/calibration_v3_4_4/supplementary_diagnostics.md](../results/calibration_v3_4_4/supplementary_diagnostics.md)

#### F24 — 任务角色heading调节未被有效识别

状态：**INCONCLUSIVE**；信心：**MEDIUM**；版本：v3.5.1。

**范围：** 同事实/相关性，不同角色heading，权威未单独操纵。

**精确结果：** 两个heading均C12/12、Δ0/12；C0 9/12导致STOP_INVALID。

**设计含义：** 先过状态资格，再测heading。

**不要推断：** 不是证明heading普遍无效或内部证据支配。

替代：无；被替代：无；开放跟进：Q06。

证据：[results/v3_5_1/README.md](../results/v3_5_1/README.md)；[results/v3_5_1/metrics.json](../results/v3_5_1/metrics.json)；[results/v3_5_1/gate.json](../results/v3_5_1/gate.json)

### UNKNOWN / fallback behavior

#### F06 — UNKNOWN策略有小样本提示交互风险

状态：**ACTIVE_WARNING**；信心：**MEDIUM**；版本：v3.6.0, v3.6.1。

**范围：** full shell mapped状态及更短fallback句四模板诊断。

**精确结果：** 旧C0 17/20，失败为有映射时UNKNOWN；新FULL_UNKNOWN39/40，其余三模板40/40。

**设计含义：** mapped复用无UNKNOWN句；fallback另测mapped/unmapped。

**不要推断：** 一例差异不证明普遍有害；最小有/无UNKNOWN都40/40；不唯一归因旧长句。

替代：无；被替代：无；开放跟进：Q07。

证据：[results/v3_6_0/calibration_outputs.jsonl](../results/v3_6_0/calibration_outputs.jsonl)；[results/v3_6_0/calibration_gate.json](../results/v3_6_0/calibration_gate.json)；[results/v3_6_1/stage_b_metrics.json](../results/v3_6_1/stage_b_metrics.json)；[results/v3_6_1/interpretation.md](../results/v3_6_1/interpretation.md)；[results/v3_6_1/v360_failure_audit.json](../results/v3_6_1/v360_failure_audit.json)

### Output-length / truncation artifacts

#### F14 — 解释性输出与截断会使能力解释失真

状态：**ACTIVE_WARNING**；信心：**HIGH**；版本：v3.4, v3.4.1, v3.4.3, v3.4.4, v3.6.3.1。

**范围：** 观察cap/输出，不把不同设计当单因素cap比较。

**精确结果：** v3.4 cap32截断9/20；v3.4.1 cap96零截断；v3.4.3 cap96仍4/72；最新集成cap16截断17/40。v3.4.4独立四题96均无截断，未触发192。

**设计含义：** 独立样本预检cap再冻结；格式/截断分列；刻意短cap须声明为接口重测。

**不要推断：** 没有32→64→96同提示修复曲线；长cap不能保证exact；不重写旧结果。

替代：无；被替代：无；开放跟进：Q02。

证据：[results/smoke_v3_4/diagnosis.md](../results/smoke_v3_4/diagnosis.md)；[results/smoke_v3_4/first_hop_generations.jsonl](../results/smoke_v3_4/first_hop_generations.jsonl)；[results/calibration_v3_4_1/diagnosis.md](../results/calibration_v3_4_1/diagnosis.md)；[results/calibration_v3_4_3/diagnosis.md](../results/calibration_v3_4_3/diagnosis.md)；[results/calibration_v3_4_4/format_smoke.json](../results/calibration_v3_4_4/format_smoke.json)；[results/calibration_v3_4_4/supplementary_diagnostics.md](../results/calibration_v3_4_4/supplementary_diagnostics.md)；[results/v3_6_3_1/diagnostic_observations.md](../results/v3_6_3_1/diagnostic_observations.md)

### Position / ordering effects

#### F09 — 最小映射已测位置及反序保持稳定

状态：**FROZEN_REUSE**；信心：**MEDIUM**；版本：v3.6.1, v3.6.2。

**范围：** 10例反序及12例K24三位置。

**精确结果：** 反序20/20不变；起/中/末各24/24正确。

**设计含义：** 区分映射顺序、冲突证据、姓名记录和答案列表。

**不要推断：** 不是普遍顺序无关，不覆盖复杂图/竞争证据。

替代：无；被替代：无；开放跟进：Q08。

证据：[results/v3_6_1/stage_c_metrics.json](../results/v3_6_1/stage_c_metrics.json)；[results/v3_6_1/README.md](../results/v3_6_1/README.md)；[results/v3_6_2/position_diagnostic_metrics.json](../results/v3_6_2/position_diagnostic_metrics.json)

#### F16 — 复杂记录/冲突证据顺序并非无害

状态：**ACTIVE_WARNING**；信心：**HIGH**；版本：v3.3, v3.4.4, v3.6.0。

**范围：** 三类操纵分开解释。

**精确结果：** v3.3冲突wrong8/12、gold5/12变更；v3.4.4 HARD R14/23敏感、最早41/95；v3.6.0反序5/20差异。

**设计含义：** 复杂/竞争证据设置order对照，不借F09免检。

**不要推断：** 不与最小位置稳定矛盾，也非统一primacy机制。

替代：无；被替代：无；开放跟进：Q08。

证据：[results/smoke_v3_3/diagnosis.md](../results/smoke_v3_3/diagnosis.md)；[results/calibration_v3_4_4/diagnosis.md](../results/calibration_v3_4_4/diagnosis.md)；[results/calibration_v3_4_4/record_rotation_free.jsonl](../results/calibration_v3_4_4/record_rotation_free.jsonl)；[results/v3_6_1/v360_failure_audit.json](../results/v3_6_1/v360_failure_audit.json)

### Model capability limits

#### F21 — 模型能力边界必须按任务/接口描述

状态：**INCONCLUSIVE**；信心：**HIGH**；版本：v1, v2.1, v3.6.1, v3.6.3.1。

**范围：** v1为0.6B，后期固定4B；没有同题同协议跨模型比较。

**精确结果：** 闭卷资格失败，符号模块E2E40/40，集成exact16/40；更大模型未跑。

**设计含义：** 限定revision/量化/提示/任务；能力比较需matched设计。

**不要推断：** 不能推一般不会推理、规模效应或其他模型表现。

替代：无；被替代：无；开放跟进：Q02, Q09。

证据：[results/smoke/inspection.md](../results/smoke/inspection.md)；[results/smoke_v2_1/diagnosis.md](../results/smoke_v2_1/diagnosis.md)；[results/v3_6_1/stronger_model_diagnostic.json](../results/v3_6_1/stronger_model_diagnostic.json)；[results/v3_6_3_1/diagnostic_observations.md](../results/v3_6_3_1/diagnostic_observations.md)

#### F25 — 旧符号失败没有简单token长度解释

状态：**INCONCLUSIVE**；信心：**MEDIUM**；版本：v3.6.0, v3.6.1。

**范围：** 20旧校准例静态表面审计。

**精确结果：** 失败3/通过17的state/outcome/entity均4tokens；反序5变更=3纠正+2新错；标签3变更均纠正。

**设计含义：** token匹配非充分有效性；保留表面及顺序控制。

**不要推断：** 不证明opaque ID本身有害、某字母致错或已排除所有表面效应。

替代：无；被替代：无；开放跟进：Q07。

证据：[results/v3_6_1/v360_failure_audit.json](../results/v3_6_1/v360_failure_audit.json)；[results/v3_6_1/interpretation.md](../results/v3_6_1/interpretation.md)

### Natural vs injected error distinction

#### F12 — 外部替代状态导致预期下游切换

状态：**FROZEN_REUSE**；信心：**HIGH**；版本：v3, v3.6.1, v3.6.2, v3.6.3.1。

**范围：** D-A/D-B仅改supplied state，操作层do(B:=B′)。

**精确结果：** v3注入20/20；v3.6.1/3.6.3.1 paired各40/40。

**设计含义：** 标注外部状态干预/条件传播，自然来源独立分母。

**不要推断：** 不能等同自然幻觉、内部belief或自然/注入等价。

替代：无；被替代：无；开放跟进：Q01, Q06。

证据：[results/smoke_v3/diagnosis.md](../results/smoke_v3/diagnosis.md)；[results/v3_6_1/stage_c_metrics.json](../results/v3_6_1/stage_c_metrics.json)；[results/v3_6_3_1/metrics.json](../results/v3_6_3_1/metrics.json)；[results/v3_6_3_1/prompt_diff_audit.md](../results/v3_6_3_1/prompt_diff_audit.md)

#### F20 — 自然传播率及注入/自然等价未建立

状态：**INCONCLUSIVE**；信心：**HIGH**；版本：v3.3, v3.4, v3.6.3.1。

**范围：** 自然来源分支与注册反事实不同。

**精确结果：** v3.3 NPR分母0；v3.4下游0；最新实际U-A全对40/40。

**设计含义：** 自然、注入、oracle分层，未来相同证据接口下比较。

**不要推断：** 不能将F12称为自然snowballing已验证。

替代：无；被替代：无；开放跟进：Q01。

证据：[results/smoke_v3_3/metrics.json](../results/smoke_v3_3/metrics.json)；[results/smoke_v3_3/diagnosis.md](../results/smoke_v3_3/diagnosis.md)；[results/smoke_v3_4/gate.json](../results/smoke_v3_4/gate.json)；[results/v3_6_3_1/pipeline_log.jsonl](../results/v3_6_3_1/pipeline_log.jsonl)；[results/v3_6_3_1/metrics.json](../results/v3_6_3_1/metrics.json)

### SHAR / HalluSE relevance

#### F22 — SHAR是否及如何减少传播尚未验证

状态：**OPEN_QUESTION**；信心：**LOW**；版本：v1, v3.6.3.1。

**范围：** 早期wrapper复用不等于拒绝/重采样策略实验。

**精确结果：** PG/IE null；无SHAR处理组或过滤/换题分解。

**设计含义：** 有效自然错误assay后，比较接受错误/覆盖率/换题。

**不要推断：** 不能宣称SHAR成败，oracle不是其性能。

替代：无；被替代：无；开放跟进：Q04。

证据：[results/smoke/inspection.md](../results/smoke/inspection.md)；[results/smoke/metrics.json](../results/smoke/metrics.json)；[results/v3_6_3_1/interpretation.md](../results/v3_6_3_1/interpretation.md)；[src/generation/shar_adapter.py](../src/generation/shar_adapter.py)；[README.md](../README.md)

#### F23 — HalluSE漏检一致错误仍属待测假说

状态：**OPEN_QUESTION**；信心：**LOW**；版本：v1, v3.4.4。

**范围：** 没有一致错误的HalluSE评分/接受实验。

**精确结果：** L/R同错身份4/4各0/72开发cells；没有据此推漏检的处理组。

**设计含义：** 先得可追溯稳定错误，冻结评分/阈值再测漏检。

**不要推断：** 一致性不等于真值，但未测不能说必然漏检。

替代：无；被替代：无；开放跟进：Q03, Q05。

证据：[results/smoke/metrics.json](../results/smoke/metrics.json)；[results/smoke/inspection.md](../results/smoke/inspection.md)；[results/calibration_v3_4_4/README.md](../results/calibration_v3_4_4/README.md)；[results/calibration_v3_4_4/supplementary_diagnostics.md](../results/calibration_v3_4_4/supplementary_diagnostics.md)；[README.md](../README.md)

### Open questions

开放问题集中列于Q01–Q09；P0是自然错误产出/传播资格与集成输出协议诊断，尚未执行。

### 跨版本冲突处理

- **X01 语义背景抑制 vs 无关映射稳定**：前者有语义/竞争第一跳，后者只增加不冲突记录，不互相推翻。 证据：[results/smoke_v3_1/diagnosis.md](../results/smoke_v3_1/diagnosis.md)；[results/v3_6_2/README.md](../results/v3_6_2/README.md)

- **X02 早期顺序不变 vs 后期顺序敏感**：列表、姓名记录、竞争证据、简单映射是不同order操纵，不能归并。 证据：[results/smoke_v3_2/diagnosis.md](../results/smoke_v3_2/diagnosis.md)；[results/smoke_v3_3/diagnosis.md](../results/smoke_v3_3/diagnosis.md)；[results/calibration_v3_4_4/diagnosis.md](../results/calibration_v3_4_4/diagnosis.md)；[results/v3_6_2/README.md](../results/v3_6_2/README.md)

- **X03 v3.6.3停校准 vs 新管线通过**：前者换整个shell，后者恢复最小shell并独立matched对照；旧失败保留。 证据：[results/v3_6_3/interpretation.md](../results/v3_6_3/interpretation.md)；[results/v3_6_3_1/README.md](../results/v3_6_3_1/README.md)

- **X04 模块40/40 vs 集成paired2/20**：两次查表和单提示组合接口不同；集成24个失败全格式无效，底层能力INCONCLUSIVE。 证据：[results/v3_6_3_1/metrics.json](../results/v3_6_3_1/metrics.json)；[results/v3_6_3_1/integrated_metrics.json](../results/v3_6_3_1/integrated_metrics.json)；[results/v3_6_3_1/diagnostic_observations.md](../results/v3_6_3_1/diagnostic_observations.md)

- **X05 UNKNOWN脆弱 vs fallback成功**：unmapped10/10，mapped minimal有/无UNKNOWN都40/40；full差1/40，不是普遍害处。 证据：[results/v3_6_1/README.md](../results/v3_6_1/README.md)；[results/v3_6_1/interpretation.md](../results/v3_6_1/interpretation.md)

- **X06 v3.4.4通过 vs 自然错误研究未就绪**：通过N/EASY接口确认，错误yield0/16；两个门槛不同。 证据：[results/calibration_v3_4_4/gate.json](../results/calibration_v3_4_4/gate.json)

- **X07 v3.4.2 gate.reason看似held-out失败**：原文No held-out condition satisfies；诊断与指标明确held-out未运行，不能记成确认实测失败。 证据：[results/calibration_v3_4_2/gate.json](../results/calibration_v3_4_2/gate.json)；[results/calibration_v3_4_2/diagnosis.md](../results/calibration_v3_4_2/diagnosis.md)

- **X08 v3.3自动身份1/12 vs 人工9/12**：自动只匹配relation index；人工核实9身份但0下游关系；原始字段保持。 证据：[results/smoke_v3_3/diagnosis.md](../results/smoke_v3_3/diagnosis.md)；[results/smoke_v3_3/review.json](../results/smoke_v3_3/review.json)；[results/smoke_v3_3/eligibility_review.json](../results/smoke_v3_3/eligibility_review.json)

## Validated Component Registry

| Component ID | Component | Canonical version | Exact artifact/template | Scope | Status | Future-use rule |
|---|---|---|---|---|---|---|
| C01 | 最小下游shell | v3.6.1 | [experiments/v3_6_1/design.py](../experiments/v3_6_1/design.py)；[results/v3_6_1/stage_c_prompt_plan.json](../results/v3_6_1/stage_c_prompt_plan.json) | MINIMAL_NO_UNKNOWN mapped prompts | FROZEN_REUSE | 标识符替换后逐字比较，保留双状态控制。 (F03, F04) |
| C02 | 上游A→B shell | v3.6.3 | [experiments/v3_6_3/design.py](../experiments/v3_6_3/design.py) | 双ENTITY→STATE显式查表 | FROZEN_REUSE | 只改Current entity；新增复杂度另校准。 (F10) |
| C03 | 不透明ID生成及匹配约束 | v3.6.3.1 | [experiments/v3_6_3/design.py](../experiments/v3_6_3/design.py)；[experiments/v3_6_3_1/design.py](../experiments/v3_6_3_1/design.py)；[results/v3_6_3_1/identifier_tokenization_audit.json](../results/v3_6_3_1/identifier_tokenization_audit.json) | 当前uppercase双数字ID家族，角色内匹配token/长度，新旧全ID不重叠、同例suffix不同 | FROZEN_REUSE | 复用构造/审计；这是成功组件中的工程约束，不证明约束单独致效。 (F03, F11) |
| C04 | 精确parser和invalid分类 | v3.6.3 | [experiments/v3_6_3/design.py](../experiments/v3_6_3/design.py)；[tests/test_v3_6_3_1.py](../tests/test_v3_6_3_1.py) | uppercase opaque IDs | FROZEN_REUSE | 不抽取、不修前缀，保留UNKNOWN/OTHER/INVALID。 (F26) |
| C05 | stateless greedy执行栈 | v3.6.3.1 | [results/v3_6_3_1/decoding_freeze.json](../results/v3_6_3_1/decoding_freeze.json)；[results/v3_6_3_1/chat_template.txt](../results/v3_6_3_1/chat_template.txt)；[experiments/v3_5_1/run_pilot.py](../experiments/v3_5_1/run_pilot.py) | 固定4B NF4/BF16，cap16仅已验证单ID组件 | FROZEN_REUSE | 校验环境/模板/isolation；新集成任务cap须响应F14。 (F27) |
| C06 | 实际状态转发和严格E2E | v3.6.3.1 | [experiments/v3_6_3_1/design.py](../experiments/v3_6_3_1/design.py)；[experiments/v3_6_3_1/run.py](../experiments/v3_6_3_1/run.py)；[experiments/v3_6_3_1/analyze.py](../experiments/v3_6_3_1/analyze.py)；[results/v3_6_3_1/pipeline_log.jsonl](../results/v3_6_3_1/pipeline_log.jsonl) | 正确实际状态40例已实测；wrong/unmapped仅代码测试 | FROZEN_REUSE | 持久化上游后原样转发，invalid跳过算失败，错上游不能被末端C掩盖。 (F11) |
| C07 | 嵌套无关映射/位置诊断 | v3.6.2 | [experiments/v3_6_2/design.py](../experiments/v3_6_2/design.py)；[results/v3_6_2/prompt_plan.json](../results/v3_6_2/prompt_plan.json)；[results/v3_6_2/position_schedule.json](../results/v3_6_2/position_schedule.json) | K0/4/12/24及12例三位置，均不冲突 | FROZEN_REUSE | 复用已测基线，不外推冲突/语义背景。 (F08, F09) |

每个组件的成功验证文件及关联F条目在JSON中完整列出；ID约束、parser、执行栈是成功组合中的工程组件，并无“单独致效”的消融结论。

## Measurement Failure Registry

| ID | Failure mode | Evidence | Symptom | Why it matters | Prevention rule | Status |
|---|---|---|---|---|---|---|
| M01 / F01 | 资格/依赖门槛失败 | [results/smoke/inspection.md](../results/smoke/inspection.md)；[results/smoke_v2/metrics.json](../results/smoke_v2/metrics.json)；[results/smoke_v3_2/gate.json](../results/smoke_v3_2/gate.json)；[results/v3_5_1/README.md](../results/v3_5_1/README.md)；[results/v3_6_0/gate.json](../results/v3_6_0/gate.json) | 格式有效或aux通过，主测量无资格 | 无有效分母仍报主效应造成假结论 | 停止后报告null/未跑，保留失败样本；辅助不能救主控制。 | ACTIVE_WARNING |
| M02 / F02 | 封闭知识与粒度混杂 | [results/smoke_v2/inspection.md](../results/smoke_v2/inspection.md)；[results/smoke_v2/metrics.json](../results/smoke_v2/metrics.json)；[results/smoke_v2_1/diagnosis.md](../results/smoke_v2_1/diagnosis.md)；[results/smoke_v3/diagnosis.md](../results/smoke_v3/diagnosis.md) | oracle/donor不能给精确目标 | 不知答案与不跟随状态无法区分 | 先校准关系/实体/粒度；显式下游映射可隔离查询和传播。 | ACTIVE_WARNING |
| M03 / F05 | 支持文本覆盖gold控制 | [results/smoke_v3_1/diagnosis.md](../results/smoke_v3_1/diagnosis.md)；[results/smoke_v3_2/diagnosis.md](../results/smoke_v3_2/diagnosis.md)；[results/smoke_v3_3/diagnosis.md](../results/smoke_v3_3/diagnosis.md)；[results/v3_5_1/README.md](../results/v3_5_1/README.md) | 高PR和低GSA并存 | 高注入成功不是有效状态测量 | 两个状态方向均须检查；不得隐藏gold控制失败。 | ACTIVE_WARNING |
| M04 / F06 | 有映射却UNKNOWN | [results/v3_6_0/calibration_outputs.jsonl](../results/v3_6_0/calibration_outputs.jsonl)；[results/v3_6_0/calibration_gate.json](../results/v3_6_0/calibration_gate.json)；[results/v3_6_1/stage_b_metrics.json](../results/v3_6_1/stage_b_metrics.json)；[results/v3_6_1/interpretation.md](../results/v3_6_1/interpretation.md)；[results/v3_6_1/v360_failure_audit.json](../results/v3_6_1/v360_failure_audit.json) | C0应可查却回退 | fallback可能和full结构交互 | mapped复用无UNKNOWN句；fallback另测mapped/unmapped。 | ACTIVE_WARNING |
| M05 / F07 | 新shell精确输出不合规 | [results/v3_6_3/interpretation.md](../results/v3_6_3/interpretation.md)；[results/v3_6_3/calibration_outputs.jsonl](../results/v3_6_3/calibration_outputs.jsonl)；[results/v3_6_3_1/shell_diagnostic_metrics.json](../results/v3_6_3_1/shell_diagnostic_metrics.json)；[results/v3_6_3_1/shell_diagnostic_outputs.jsonl](../results/v3_6_3_1/shell_diagnostic_outputs.jsonl) | 解释/缺前缀/截断 | 等义提示不保证输出协议等效 | 主管线复用验证shell；Recorded仅明确重测。 | ACTIVE_WARNING |
| M06 / F14 | 解释性输出与cap截断 | [results/smoke_v3_4/diagnosis.md](../results/smoke_v3_4/diagnosis.md)；[results/smoke_v3_4/first_hop_generations.jsonl](../results/smoke_v3_4/first_hop_generations.jsonl)；[results/calibration_v3_4_1/diagnosis.md](../results/calibration_v3_4_1/diagnosis.md)；[results/calibration_v3_4_3/diagnosis.md](../results/calibration_v3_4_3/diagnosis.md)；[results/calibration_v3_4_4/format_smoke.json](../results/calibration_v3_4_4/format_smoke.json)；[results/calibration_v3_4_4/supplementary_diagnostics.md](../results/calibration_v3_4_4/supplementary_diagnostics.md)；[results/v3_6_3_1/diagnostic_observations.md](../results/v3_6_3_1/diagnostic_observations.md) | 32/16甚至96出现截断 | 格式失败不能直接归为能力失败 | 独立样本预检cap再冻结；格式/截断分列；刻意短cap须声明为接口重测。 | ACTIVE_WARNING |
| M07 / F15 | 候选列表位置偏差 | [results/calibration_v3_4_2/position_audit.md](../results/calibration_v3_4_2/position_audit.md)；[results/calibration_v3_4_3/diagnosis.md](../results/calibration_v3_4_3/diagnosis.md)；[results/calibration_v3_4_3/prompt_diff_audit.md](../results/calibration_v3_4_3/prompt_diff_audit.md)；[results/calibration_v3_4_4/README.md](../results/calibration_v3_4_4/README.md)；[results/calibration_v3_4_4/supplementary_diagnostics.md](../results/calibration_v3_4_4/supplementary_diagnostics.md) | 仅旋转列表即改身份 | 错误可能不代表稳定错误状态 | 避开未校准列表或明确重测完整order控制；按基础例分析。 | ACTIVE_WARNING |
| M08 / F16 | 复杂记录/竞争证据顺序敏感 | [results/smoke_v3_3/diagnosis.md](../results/smoke_v3_3/diagnosis.md)；[results/calibration_v3_4_4/diagnosis.md](../results/calibration_v3_4_4/diagnosis.md)；[results/calibration_v3_4_4/record_rotation_free.jsonl](../results/calibration_v3_4_4/record_rotation_free.jsonl)；[results/v3_6_1/v360_failure_audit.json](../results/v3_6_1/v360_failure_audit.json) | 旋转/倒置引起输出变化 | 简单位置稳定不能免除复杂任务控制 | 复杂/竞争证据设置order对照，不借F09免检。 | ACTIVE_WARNING |
| M09 / F17 | 通道测量不等价 | [results/calibration_v3_4_1/diagnosis.md](../results/calibration_v3_4_1/diagnosis.md)；[results/calibration_v3_4_3/diagnosis.md](../results/calibration_v3_4_3/diagnosis.md)；[results/calibration_v3_4_4/README.md](../results/calibration_v3_4_4/README.md)；[results/calibration_v3_4_4/supplementary_diagnostics.md](../results/calibration_v3_4_4/supplementary_diagnostics.md) | C有效而F截断，N与L差异 | 受限选择不是完成的自然第一跳 | 显式分母/通道/valid条件；自然轨迹不可由受限选择代替。 | ACTIVE_WARNING |
| M10 / F19 | 缺乏合格自然错误 | [results/smoke_v3_3/eligibility_review.json](../results/smoke_v3_3/eligibility_review.json)；[results/smoke_v3_3/diagnosis.md](../results/smoke_v3_3/diagnosis.md)；[results/smoke_v3_4/metrics.json](../results/smoke_v3_4/metrics.json)；[results/smoke_v3_4/diagnosis.md](../results/smoke_v3_4/diagnosis.md)；[results/calibration_v3_4_4/gate.json](../results/calibration_v3_4_4/gate.json)；[results/v3_6_3_1/metrics.json](../results/v3_6_3_1/metrics.json)；[results/calibration_v3_4_4/README.md](../results/calibration_v3_4_4/README.md) | 错误缺关系、无效或全对 | 没有自然传播分母 | 自然错误yield与证据资格前置；零合格传播率null。 | ACTIVE_WARNING |

证据只支持风险存在及注明范围，不一定识别唯一因果。未发现“事后改题修复”已发生的证据；禁止后验修复作为预防纪律保留，但不伪造observed失败条目。注入/自然混淆的防范由F12/F20与协议承担，没有把未发生的误用登记成观测事件。

## Open Questions

### Q01 — 合格自然第一跳错误是否沿实际状态传播？

优先级：P0；依赖：C01, C06, F15, F19。

**为何重要：** 核心目标未被注入实验替代。

**当前证据：** 自然关系分母0；候选任务错误yield不足；最新U-A全对。

**解决标准：** 独立确认足够未强制、严格有效、错误且关系可追溯的状态，原样转发；报告条件分母/正确上游对照。

证据：[results/smoke_v3_3/diagnosis.md](../results/smoke_v3_3/diagnosis.md)；[results/calibration_v3_4_4/gate.json](../results/calibration_v3_4_4/gate.json)；[results/v3_6_3_1/metrics.json](../results/v3_6_3_1/metrics.json)

### Q02 — 分离格式/截断后集成两跳是否可靠？

优先级：P0；依赖：F13, F14, C04, C05。

**为何重要：** ready失败非唯一的能力解释。

**当前证据：** I-A7/20、I-B9/20；24INVALID中17截断；无只改cap对照。

**解决标准：** 新独立样本预注册协议/cap诊断，分别报完成率、合规率、准确率；不重写旧标签。

证据：[results/v3_6_3_1/integrated_metrics.json](../results/v3_6_3_1/integrated_metrics.json)；[results/v3_6_3_1/diagnostic_observations.md](../results/v3_6_3_1/diagnostic_observations.md)

### Q03 — 错误进入verified文本是否导致下游被接受错误？

优先级：P1；依赖：Q01, C06。

**为何重要：** 连接条件跟随与系统接受错误。

**当前证据：** 只有外部state操作与正确状态管线；未做verified污染实验。

**解决标准：** 记录来源、verified写入、下游、验收及真值；设独立干预对照。

证据：[results/v3_6_3_1/interpretation.md](../results/v3_6_3_1/interpretation.md)；[results/v3_6_3_1/pipeline_log.jsonl](../results/v3_6_3_1/pipeline_log.jsonl)

### Q04 — SHAR通过过滤还是换题减少传播？

优先级：P1；依赖：Q01, Q03。

**为何重要：** 正确率与覆盖/主题变化可能混杂。

**当前证据：** wrapper及oracle非SHAR处理组。

**解决标准：** 有/无SHAR及策略消融；测接受错误、覆盖、拒绝、同题重试和换题。

证据：[results/smoke/inspection.md](../results/smoke/inspection.md)；[results/smoke/metrics.json](../results/smoke/metrics.json)

### Q05 — HalluSE能否漏检一致错误？

优先级：P1；依赖：Q01, Q03。

**为何重要：** 一致性不等于正确性。

**当前证据：** 无HalluSE实测；v3.4.4无同错身份4/4开发cell。

**解决标准：** 独立获得证据已知稳定错误，冻结评分/阈值，报漏检率分母。

证据：[results/calibration_v3_4_4/supplementary_diagnostics.md](../results/calibration_v3_4_4/supplementary_diagnostics.md)

### Q06 — 状态跟随和上下文覆盖的内部机制是什么？

优先级：P2；依赖：C01, Q01。

**为何重要：** 行为输出不支持神经机制归因。

**当前证据：** 有行为对照，无内部因果干预。

**解决标准：** 稳定assay后预注册内部干预及必要性/充分性控制。

证据：[results/smoke_v3_3/diagnosis.md](../results/smoke_v3_3/diagnosis.md)；[results/v3_6_3_1/interpretation.md](../results/v3_6_3_1/interpretation.md)

### Q07 — fallback/标签/词形何时引起脆弱性？

优先级：P2；依赖：F06, F25。

**为何重要：** 避免小样本关联泛化。

**当前证据：** full UNKNOWN仅差1/40；token均4；旧标签差异3次均纠正。

**解决标准：** 独立样本单因素matched提示及mapped/unmapped控制。

证据：[results/v3_6_1/interpretation.md](../results/v3_6_1/interpretation.md)；[results/v3_6_1/v360_failure_audit.json](../results/v3_6_1/v360_failure_audit.json)

### Q08 — 顺序及背景效应的边界在哪里？

优先级：P2；依赖：F08, F09, F15, F16。

**为何重要：** 简单稳定，复杂/冲突敏感。

**当前证据：** 简单三位置24/24；HARD R14/23敏感；冲突wrong8/12改变。

**解决标准：** 分别控制列表、记录、竞争证据和语义背景，检验交互。

证据：[results/v3_6_2/position_diagnostic_metrics.json](../results/v3_6_2/position_diagnostic_metrics.json)；[results/calibration_v3_4_4/diagnosis.md](../results/calibration_v3_4_4/diagnosis.md)；[results/smoke_v3_3/diagnosis.md](../results/smoke_v3_3/diagnosis.md)

### Q09 — 能否推广到其他模型/量化/真实任务？

优先级：P2；依赖：C01, C05, Q02。

**为何重要：** 主要证据局限一个4B栈。

**当前证据：** 0.6B与4B不matched；更大模型诊断未跑。

**解决标准：** 同题同协议同门槛模型/量化比较和外部复现。

证据：[results/v3_6_1/stronger_model_diagnostic.json](../results/v3_6_1/stronger_model_diagnostic.json)；[results/smoke/inspection.md](../results/smoke/inspection.md)

## Retired / superseded directions

没有将任何F条目标为SUPERSEDED：后来的不同接口结果不撤销早期真实观察。

- RETIRED：v1可直接作答的父母→配偶路线及原smoke配置。依赖失败后改为明确组合；不否定旧观察。 证据：[results/smoke/inspection.md](../results/smoke/inspection.md)

### 未验证的历史说法

- **UNVERIFIED_HISTORY**：同提示32→64→96实验证明能力恢复。有截断记录和96独立smoke；未见仅改cap的该对照链。

- **UNVERIFIED_HISTORY**：已验证SHAR失败或HalluSE漏检一致错误。无处理组/漏检率；wrapper/oracle不是SHAR策略。

- **UNVERIFIED_HISTORY**：自然/注入等价且自然传播率已量化。自然合格分母未建立，已有下游错状态是反事实。

- **UNVERIFIED_HISTORY**：已观察到按模型错误后验改题修复。v2/v3.4.1调整在推理前；未找到后验替换证据，不能列作observed警告。

## Future Experiment Design Protocol

每份新实验spec的第一个标题必须是 `# Prior Findings Review`，引用 `docs/validated_findings.md` 和 `docs/validated_findings.json`。随后列出审查表，再写 `## Validated Inheritance`，最后才写 `## New manipulation`。

| Finding / Component | Ledger status | Treatment in this experiment | Rationale |
|---|---|---|---|
| Fxx / Cxx | 台账原状态 | 明确选择下列处理方式 | 写适用范围、依据及验证计划 |

处理方式：`FROZEN_REUSE`, `INTENTIONALLY_RETESTED`, `OVERRIDDEN`, `AVOIDED`, `TARGETED`, `NOT_RELEVANT`。

全部27项发现与7个组件须逐项审查；不适用的非警告条目可用NOT_RELEVANT并说明原因。失败登记M条目是相应F警告的视图，不重复要求一套审查行。每个ACTIVE_WARNING必须选择AVOIDED或INTENTIONALLY_RETESTED；不适用也要说明如何避免该失败路径，不能写NOT_RELEVANT跳过。

改变FROZEN_REUSE组件时，必须记录component、prior_evidence、reason、prior_conclusion_no_longer_applies、revalidation_gate；禁止一面声明FROZEN_REUSE一面修改。新的审查JSON保留modified布尔值及modification对象。

机器审查：`python scripts/validated_findings.py review-spec --spec PATH --review PATH`。review JSON必须包含ledger_sha256（当前台账JSON的SHA256）、latest_completed_version、rows；每行含id、ledger_status、treatment、rationale、modified，变更组件另含modification对象。Markdown表格须与JSON行一致。

该检查验证声明、台账新鲜度、覆盖及门槛说明，不自动推断实验是否科学合理，也不替代逐字prompt比对、实际代码/模型哈希和推理前审计。以后新runner必须在准备阶段调用审查检查，并冻结其结果。旧runner不追改。

新协议补充全项目review入口；旧三分类保留为组件层映射。ACTIVE_WARNING必须AVOIDED说明规避/不适用路径，或INTENTIONALLY_RETESTED。旧cap16只冻结旧实验，新集成设计可声明有理由的改变与重验证，禁止追改旧结果。
EXPERIMENT_WORKFLOW.md和experiments/inheritance.py在旧manifest冻结，本次不修改；README和新审查脚本激活新协议。

与旧三分类的对应：FROZEN_REUSE→FROZEN_REUSE；INTENTIONALLY_RETESTED→INTENTIONALLY_RETESTED；OVERRIDDEN→INTENTIONALLY_RETESTED；AVOIDED→NOT_RELEVANT；TARGETED→INTENTIONALLY_RETESTED；NOT_RELEVANT→NOT_RELEVANT。此映射用于旧组件层说明，不能替代新协议对警告和修改理由的更严格要求。

维护顺序：冻结实验结果 → 更新JSON及Markdown → 更新审计 → 追加CHANGELOG → 再设计下一实验。最近完成的实验未入账时，禁止通过下一spec审查。

台账维护：先更新JSON证据与新版本条目/哈希、追加changelog，再执行 `python scripts/validated_findings.py render` 与 `python scripts/validated_findings.py verify`。只有新增/有理由更正的证据可改变状态；历史观测不被覆盖。

## Change Log

- 2026-10-08：创建项目级研究台账，扫描18实验版本/19结果目录（含1个推理前草稿），提取27发现，激活未来spec继承协议；零新模型调用，历史不变。
