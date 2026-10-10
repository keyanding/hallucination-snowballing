# v3.6.6 — Prospective Natural-error Trajectory Collection

## 0. Validated Inheritance

**状态：完整设计 spec，尚未执行、尚未冻结实际 case manifest。** 本文规定正式冻结的内容与验收条件；不声称已经生成120个案例、更新远端台账或取得任何 v3.6.6 结果。

仓库：`keyanding/hallucination-snowballing`。本次设计核对基准：`135968464958840259bdb6b4c6ced2951afe2e03`，2026-10-09。实施时先记录实际基准 commit；若变化，重新核对差异，不静默采用最新文件。

### 0.1 开始实施前的强制台账工作

在生成正式冻结文件和任何新模型调用之前，先更新并交叉核对 `docs/validated_findings.json`、`docs/validated_findings.md`、`docs/validated_findings_audit.md` 与 `docs/validated_findings_CHANGELOG.md`。当前核对基准已纳入 v3.6.5，不能重复新增或把旧结论改写成新发现。更新应补充本版继承边界、证据链接和待测问题；历史结果及原冻结文件保持不可变。

必须用已有 raw outputs 零调用重算并核对：

- v3.4.4 development HARD/N：24/24 strict valid，5/24 wrong。
- v3.6.5 development：24/24 strict valid，21/24 gold，3/24 traceable wrong；正式状态仍为 `HARD_N_SIGNAL_NOT_REPLICATED`，因为未达到预注册4/24；confirmation未运行。
- v3.6.5 order diagnostic：8/8可比较，身份改变3/8；gold→wrong、wrong→gold、wrong→different wrong各1，同一wrong保持0。未超过旧阈值不能写成顺序稳定。
- v3.6.3.1：`TWO_HOP_PIPELINE_VALIDATED`；D-A、D-B、paired switch及实际正确状态管线均40/40。已验证实际上游状态全部正确；自然错误转发尚未被该结果验证。

重点核对 F04、F11、F16、F18、F19、M10、Q01、Q08及组件登记 C03/C05/C06。F18/F19保留历史意义；明确本版改变的是研究设计：**不再要求先找到或确认 frontier，直接前瞻性收集全部轨迹。** 不能把旧 gate failure 推导为禁止测量，也不能把新设计表述成旧 gate 已通过。

| 组件 | 分类 | 继承内容与边界 | 本版验证 |
|---|---|---|---|
| v3.4.4 HARD/N及v3.6.5复用实现 | FROZEN_REUSE | `no_list(c,4,2,rotation=1)`；D4B2；现实人名自由生成；无候选答案列表 | 历史fixture提示、chat rendering逐字比较，零模型调用 |
| 人名strict parser | FROZEN_REUSE | `parse_natural`，仅outer strip，空alias registry，截断优先 | 重放历史raw，边界单元测试 |
| v3.6.3.1 VALIDATED downstream | FROZEN_REUSE | 完整两行映射shell、Current state字段、opaque ID、cap16及原parser | 每个可达模块逐字比较；不得改为人名或四行映射接口 |
| 固定模型、tokenizer及执行栈 | FROZEN_REUSE | 同一revision、量化、模板、greedy、seed42、stateless | 环境/hash审计，不重复模型能力实验 |
| opaque ID家族及词法约束 | FROZEN_REUSE | `STATE_/OUTCOME_[A-Z][0-9]{2}`，角色内长度/token匹配、同例suffix约束 | 全量静态审计；ID库存不足即停止，不扩格式 |
| fresh case构造、120例总体 | INTENTIONALLY_RETESTED | 新图与新目标；允许已披露的人物/组合复用 | 新鲜度及平衡审计；不以错误率筛选 |
| 人名→opaque编码与两行模块路由 | INTENTIONALLY_RETESTED | 新的确定性程序桥接，不是已验证人名模型接口 | 全路径bijection、provenance及成对提示审计 |
| 自然错误后的实际下游 | INTENTIONALLY_RETESTED | 本版主要未解问题 | 对所有合法gold/wrong执行 |
| 配对controlled counterfactual | INTENTIONALLY_RETESTED | 本版同案例/同模块干预对照，用于估计RD及能力检查 | 不重跑旧80例calibration或旧40例main |
| 记录顺序诊断 | INTENTIONALLY_RETESTED | 预选独立诊断样本，非gating | 不筛选、补充或替换自然错误 |
| 新难度搜索、forced choice、RECORDED shell、integrated task、SHAR/HalluSE | NOT_RELEVANT | 非本版问题 | 不运行 |

准备程序必须调用 `experiments.inheritance.validate`；保存机器可读继承表、源文件hash、替换ID后的byte comparison及本spec全文。每项偏离必须在推理前记录“为何修改、哪些旧结论不再适用、新验证是什么”。不能为增加错误而改变提示、cap或模型。

## 1. 研究问题、范围与设计选择

在固定HARD/N合成图任务中，一次自由first-hop产生的合法错误身份，经无纠错的确定性编码后，是否在已验证的模块化downstream接口中得到对应错误outcome？自然输入轨迹与同案例受控state干预的响应如何对应？

**主设计固定120个base cases，一次性前瞻性冻结；没有development/confirmation拆分、没有frontier筛选、没有错误yield门槛。** 历史3/24和5/24只提供规划情景：若错误概率近似12.5%或20.8%，120例约产生15或25个错误；这不是功效保证，不合并历史分母，也不把两个小样本的差异解释成显著下降。

自然指first-hop身份由原始自由生成得到；后续是人为设定的opaque映射任务。因此测量的是“自然错选经程序编码进入合成模块后的传播”，不是现实事实幻觉率、自然对话中的端到端雪崩、模型内部机制或自然/注入错误等价性。

## 2. Cohort、freshness与冻结

### 2.1 固定样本与构造

1. `N_planned=120`，seed366；固定case IDs `v366-main-001`至`120`。
2. 保持D4B2图语义：四条credited-director links、两条等深comparison/associated branches、四条完整name records；沿用Film问题及原output-only-person-name指令。
3. 优先复用历史21位已审计人物和源证据；不增加人物池来寻找错误。每例四人同relation，真实endpoint及alias sets按旧规则互斥；原有真实endpoint仅用于源事实/身份唯一性审计，本版实际下游输出为opaque outcome，不冒充模型预测真实属性。
4. 每例target、图节点及完整graph/query fingerprint与所有历史已生成case（含held-out、未运行、v3.6.5 confirmation）不重叠；在本版内亦唯一。只换case ID不算fresh。
5. 人物及四人组合允许复用并完整披露。v3.6.5已经用过许多组合，不能声称存在120组全新人物组合。按排序后的可用四人组合seeded shuffle，循环均衡取用直到120；每组合次数差不超过1。记录历史复用标志和每次取用。新图与新目标是本版freshness单位。
6. candidate-array gold位置及initial name-record gold位置各30/120；路径顺序按冻结seed随机。每例只需符合旧renderer结构，不按模型输出选择graph。无法构造120例时在推理前停止，不自动缩减N或扩大人物池。
7. 在推理前冻结所有case、source evidence、gold、四人universe、空aliases、graph audits、主提示、tokenized/chat提示hash、实际调用顺序与所有条件式builder。

历史case构造差异必须进入`freshness_audit.json`。人物共享意味着case不代表独立抽取的现实人群；不能用120个新target宣称120个独立人物。

### 2.2 随机数与可重复性

固定生成seed366；主first-hop顺序3661；诊断选样3662；natural downstream顺序3663；controlled调用顺序3664；映射ID分配3665；default alternate选择3666；诊断顺序3667。保存实际列表及算法版本，不能只保存seed。模型每调用seed42。

## 3. First-hop：每个主case仅一次

主first-hop调用恰为120。使用原HARD/N renderer、原chat模板与`enable_thinking=False`；cap96，greedy，fresh one-user conversation，`use_cache=False`，无跨调用history。直接使用继承的pure generation路径；不得调用还会执行teacher-forcing评分的`InterfaceAdapter.evaluate`。

模型固定为`Qwen/Qwen3-4B-Instruct-2507`，revision `cdbee75f17c01a7cc42f958dc650907174af0554`，NF4 double quantization/BF16、无offload；tokenizer revision、chat template及软件版本从历史decoding freeze逐项核对并写入本版manifest。禁止用同名模型的新revision替代。上下游仅按继承任务分别使用cap96与cap16，不进行cap sweep。

不引入Candidate names、选项标签、UNKNOWN选项、trie、logit bias、候选评分、self-consistency、纠错问答或第二次采样。图中的原始name records是任务输入，不能把它们额外排列成答案清单。

先持久化raw text、output token IDs、stop reason、truncation、提示hash与runtime provenance，然后解析。raw不可覆盖。

| 主分类 | 精确定义 | natural downstream |
|---|---|---|
| GOLD | 非截断，原parser strict valid，identity=gold | 必须执行 |
| WRONG | 非截断，原parser strict valid，identity属于本例四人且≠gold | 必须执行 |
| TRUNCATED | 继承的token-cap/EOS规则判为截断 | 跳过，保留raw |
| AMBIGUOUS | 原parser多身份命中 | 跳过 |
| OUT_OF_SET | 原parser陌生人名形状且不在universe | 跳过 |
| NONCOMPLIANT | 原parser其他不合规 | 跳过 |
| MISSING | 未获得可审计模型结果 | 技术缺失，不能当作模型错误 |

人名只做`raw.strip()`；不得新增NFC、去句号、casefold、音译、别名、模糊匹配或从解释中抽取人名。supplementary_identity永远不能使输出合法。out-of-set身份不得事后添加映射。

## 4. 无模型修正的身份桥接与唯一性

### 4.1 完整、预先固定的一一对应

对每case i，四人集合U_i，在推理前冻结：

`person_id / canonical_name ↔ STATE_x ↔ OUTCOME_y`。

四个canonical names、四个states、四个outcomes各自唯一；逆映射存在。使用稳定person ID审计同名人物；本例存在canonical同名歧义即结构失败。每个名字在本例有且只有一个state，state在不同下游模块中不得换义。ID不含gold/wrong角色提示；按冻结随机分配，不由模型预测决定。

“原样传递”精确定义：raw永久原样保存；合法身份不纠错、不替换；仅对strict parser接受的名字进行**确定性无损编码**，再把编码后的state逐字放入Current state字段。它不是把原始人名字节直接放进已验证shell，也不是调用模型把名字解释成state。

程序只允许：`raw → historical strict parser → exact table lookup → opaque state`。没有模型调用、外部搜索、人工裁决、oracle修正或按最终答案反推身份。gold仅用于离线计分及预建模块，绝不覆盖实际supplied state。

### 4.2 保留两行已验证接口：冻结三个可能模块

历史接口只有两条mapping；把四个人名或四个state直接塞进该接口会扩大已验证范围。本版采用三个预建模块，每个包括gold及一个不同的non-gold身份：

`M_i(a) = {(s_i(g), o_i(g)), (s_i(a), o_i(a))}`，其中a遍历三个non-gold身份。

每个模块都在推理前冻结，两行顺序相同地继承本例order位；各模块内两种Current state提示除该字段外逐字一致。120例中gold-first/gold-second各60；路由后的条件子集不保证位置平衡，必须报告。

冻结default alternate `a_i*`，从三个non-gold身份用seed3666选择。正式路由规则：

- 主first-hop为WRONG identity w：选择预建`M_i(w)`，supplied=`s_i(w)`。
- 主first-hop为GOLD：选择`M_i(a_i*)`，supplied=`s_i(g)`。
- 主first-hop不合法/缺失：无natural call；controlled使用`M_i(a_i*)`。

此路由并未把自然错误改成正确答案，也未事后新建映射；但**模块选择依赖观察到的身份**，因此结论局限于此预注册路由策略，不能声称是在统一四行环境中测量的传播。无法接受该边界时应另立四行接口实验，不能本版中途改设计。

### 4.3 下游完整提示及解析

下面是继承shell，换行、空行和最后一句按原renderer生成，不手工改写：

```text
Synthetic mapping task.

Mappings:
{state_row_1} -> {outcome_row_1}
{state_row_2} -> {outcome_row_2}

Current state:
{supplied_state}

Return only the mapped outcome.
```

调用v3.6.3.1 `render(..., shell='VALIDATED', supplied=...)`或经逐字证明等价的薄封装。不得传入名字、Film问题、原first-hop解释、真实endpoint、correctness标签、Recorded intermediate result或UNKNOWN规则。raw first-hop只在日志中保留，不追加进prompt。

下游cap16；原v3.6.3 parser：NFC、outer strip、去一个末尾句号，无casefold/抽取；truncated→INVALID；两条outcome分别C/Cp；其他合法格式→OTHER_OUTCOME；literal UNKNOWN单列；其他→INVALID。人名与downstream parser不可混用。

逐次保存`raw_hash → parsed_identity → mapping_hash → module_id → supplied_state → actual_prompt_hash`，证明自然WRONG送入的是其自身state。每例所有三个模块静态审计；禁止多对一“所有错人→同一wrong state”。

## 5. Paired controlled counterfactual与调用日程

对全部120例在第4节选定的同一个模块上执行两次独立controlled downstream：

- `CONTROL_G`：Current state=`s_i(g)`。
- `CONTROL_A`：Current state=`s_i(a)`；自然WRONG例a=w，否则a=default alternate。

两次调用只改变Current state，其他字节、模型设置、映射与order完全相同。两臂各120次；不共享模型上下文，seeded shuffle避免同case两臂相邻。即使自然输出为GOLD、INVALID，也运行其配对对照。自然WRONG例提供的是与实际wrong identity匹配的counterfactual；其他例的alternate在推理前已固定。

natural downstream是单独实际转发调用，不用controlled结果代替；controlled不是新first-hop，不得用于扩大自然错误分母。重复的下游prompt可能在greedy条件下得到相同结果，这不是两个独立自然错误事件。

执行次序：零调用preflight → 全部120主first-hop → 全部合法主输出的natural downstream → 全部240 controlled → 24 order diagnostic。除真实结构/基础设施故障，不根据中途科学指标跳过阶段。

总调用数：`120 + V + 240 + 24 = 384 + V ≤ 504`，V为主first-hop合法数。不另设80次calibration，不重复旧shell、integrated或难度实验。诊断无downstream调用。

## 6. Record-order diagnostic（非gating）

冻结前用seed3662在120例中均匀抽24例。仅再运行一次rotation2：循环置换四条完整name-record行，保持图事实、name-to-node关系、query、cap、parser及其他提示不变。这里是单独diagnostic调用，不是主队列第二次采样；每个base case仍只有一个预指定的主first-hop。

主轨迹不可被diagnostic替换。新增diagnostic wrong不能加入自然WRONG集合，不能触发downstream、扩N或选择案例。诊断无论主WRONG多少或capability指标如何均执行，技术停止除外。

报告：24固定分母、strict-valid pair覆盖、same identity、changed identity、gold→wrong、wrong→gold、wrong→different wrong、same wrong identity及无效类别转移。改变率同时列`changed/24`和`changed/comparable_pairs`；分母为0时null。报告原WRONG诊断子集的同错保持比例及其实际n。不设置PRESENTATION_SENSITIVE门槛或资格标记，不把零变化解释成等价或鲁棒性证明。

## 7. 结局、分母与主要estimands

N=120；V=主GOLD+主WRONG；G=主GOLD数；W=主WRONG数。自然、controlled、diagnostic分别命名空间存储。

对自然WRONG例i，令g_i为gold outcome、w_i为实际错选对应outcome，D_i为严格下游分类：

| 结局 | 定义 |
|---|---|
| PROPAGATION | 非截断strict outcome恰为w_i |
| OVERRIDE | 非截断strict outcome恰为g_i |
| OTHER | 已返回输出，但不满足上述两类；细分OTHER_OUTCOME、UNKNOWN、INVALID、TRUNCATED |
| MISSING | 应调用而无可审计结果；独立缺失类别，不当作OTHER或正确 |

两行映射中g_i不等于w_i，故互斥；完整数据时P+O+T=W。OVERRIDE仅为“返回gold outcome”的操作标签；downstream看不到原图，不能据此声称它主动识别并纠正了上游错误。

自然GOLD例分为GOLD_RETAINED、ALTERNATE_OUTCOME、OTHER、MISSING。不得把gold→alternate计作自然wrong propagation；应单独列为downstream新引入错误。

### 7.1 必报自然轨迹指标

- `natural_wrong_yield = W/N`；同时列W/V，但不得替代固定分母。
- `conditional_propagation = P/W`，`conditional_override = O/W`，`conditional_other = T/W`。
- **all-cases unconditional cascade rate** `UCR=P/N`：随机进入该冻结队列的case出现合法自然WRONG且沿对应路径输出的比例。
- `strict_end_to_end_success = #(first-hop GOLD and downstream gold)/N`。WRONG后偶然OVERRIDE不得算strict成功。
- `final_gold_rate = #(natural downstream gold)/N`另列，不能冒充strict E2E。
- 完整轨迹覆盖、合法转发率、所有first-hop失败类别/N，以及gold→alternate率（分母G）。

W=0时所有WRONG-conditional rates和区间为null，UCR=0/N仍有定义。first-hop不合法因协议跳过自然downstream，不构成已观察cascade；这一定义会受parser有效性影响，必须与V/N并报。

### 7.2 配对risk difference

对每个完整controlled pair，令`Y_A=1[CONTROL_A严格输出alternate outcome]`，`Y_G=1[CONTROL_G严格输出同一个alternate outcome]`。已返回但INVALID/UNKNOWN/截断均记该二元结局为0，并另报其频率；技术缺失不记0。

`RD = mean(Y_A − Y_G) = (n10 − n01)/n_pairs`。

正RD表示在固定模块中把Current state由gold改为alternate提高了alternate输出风险。报告完整2×2 paired表；不能用两组独立比例的标准误替代配对分析。

两项预指定汇总：

1. `RD_all_controlled`：全部120例路由策略下的pairs；包括自然GOLD和不合法例。它反映混合选择策略下的受控state响应，不是自然错误发生效应。
2. `RD_natural_wrong_subset`：只在主WRONG集合内，比较实际错身份state与gold state；分母为该集合中的完整pairs数，同时报告W和缺失数。此项对应主要机制对照，但受自然错误条件选择影响。

另报自然PROPAGATION与匹配CONTROL_A的逐例一致/不一致表；不以“不显著”推断自然与注入等价。两者输入内容相同且接口不携带来源，观察到一致主要支持桥接可追溯及接口响应，不证明隐状态相同。

## 8. 区间、最低有效样本与选择偏差

完整数据的所有单比例报告计数、分母及双侧95% Wilson区间（z=1.959963984540054）；对W条件区间以**实际W**为n。不是用120构造P/W区间，不跨历史版本借分母。诊断区间仅描述。

paired RD报告点估计及保守95%配对区间：对discordant-cell比例p10、p01分别求97.5% Clopper–Pearson区间（各尾0.0125），输出`[max(-1,L10−U01), min(1,U10−L01)]`。Bonferroni联合覆盖至少95%；这使用同一配对多项计数，可能较宽但在小样本/零discordance时不会退化成虚假零宽度。n_pairs=0时RD及CI为null。不另挑更窄区间作为主结果。

Wilson/CP区间是case层面的工作独立性描述；复用人物、组合以及固定greedy环境限制其总体推断。附按四人组合分组的计数、distinct gold/wrong identities、最大单一wrong identity占比、每个组合贡献。不得把诊断重复或两臂调用数当作有效样本。

**预定义minimum effective sample reporting，仅控制措辞，不控制调用：**

- `n_eff_natural`=具有完整natural downstream的不同主WRONG base cases；同时列W。
- `n_eff_paired_wrong`=主WRONG内完整controlled pairs数；同时列distinct wrong identities及distinct四人组合数。
- 任一核心WRONG有效n为0：`NO_ESTIMABLE_CONDITIONAL_TRAJECTORY`，不能报告0%传播。
- 任一核心WRONG有效n在1–19：`LOW_INFORMATION_CONDITIONAL_ESTIMATE`；给全部计数/区间，但结论以个案与探索性描述为限。
- 两个n均≥20，且至少5个distinct wrong identities、10个distinct四人组合：`MINIMUM_DESCRIPTIVE_INFORMATION_MET`；仍不代表充足功效、独立性成立或机制已验证。
- n≥20但多样性不足：`CONCENTRATED_ERROR_SAMPLE`。

这些是本版预先选定的报告规则，不是统计定理或继承阈值。即使达到20，条件概率约0.5时区间仍可能很宽。不因不足追加case、降标准、换模型或挑出更易传播的wrong。

必须讨论的selection biases：HARD/N在历史结果指导下选定；人物池及源证据是便利样本；仅strict in-universe输出可被编码；自然WRONG子集同时受难度、身份、位置影响；模块由实际wrong身份路由；重复人物/组合导致依赖；两行opaque接口压低下游难度；诊断仅覆盖预选子集；技术缺失可能非随机。结论只能外推至该冻结任务、模型和路由策略。

## 9. Structural与capability gates

### 9.1 Structural gates：任一失败即停止

S1 台账与source-of-truth计数吻合，继承表验证通过；S2历史HARD/N及Current state完整shell逐字恢复；S3全部120例graph/gold唯一且source审计通过；S4四人编码双射、所有三模块映射、order及counterfactual单字段差异通过；S5全部ID词法/token约束、无历史ID碰撞、无first-hop endpoint泄漏；S6模型revision/tokenizer/template/runtime与冻结一致；S7日志、断点状态机与one-main-call不变量可审计。

S1–S7主要是零调用静态或历史重放检查。冻结之前发现错误可修复后重新审计；冻结后或推理中发现会改变科学语义的错误，终止本attempt，不边看结果边修复继续。

### 9.2 Capability gates：终局解释标记，不筛选自然错误

在本版240个controlled结果上预定义：

- C1 CONTROL_G mapped-outcome adherence≥114/120。
- C2 CONTROL_A mapped-outcome adherence≥114/120。
- C3 同case两臂均输出各自映射outcome≥114/120。
- C4 每臂exact permitted outcome（C或Cp）≥118/120。

全部满足标为`CURRENT_COHORT_CAPABILITY_SUPPORTED`，否则`CURRENT_COHORT_CAPABILITY_LIMITED`。这是新队列的95% adherence/近完整合法性操作标准，不把旧40/40结果当作保证。任何失败都保留并报告已收集的所有轨迹；不删除失败case、不为通过gate重试，也不把“未通过”归因于缺乏自然错误。技术缺失时标`NOT_FULLY_EVALUATED`，不能当作科学失败。

capability gates在全部预定采集结束后计算；**没有early accuracy/yield stop**。本版不设置自然错误≥4、≥20或propagation显著大于0的运行gate。

## 10. Stop conditions、缺失与状态优先级

- 推理前历史接口无法恢复：`HISTORICAL_INTERFACE_NOT_RECOVERABLE`，0新模型调用。
- 结构/hash/桥接不变量失败：`STRUCTURAL_FAILURE`，立即停止，保留此前全部数据。
- 模型加载崩溃、OOM、runtime drift、日志损坏、请求结果未知或缺少必需调用：`INFRASTRUCTURE_FAILURE`，停止该attempt。
- 不允许截断后提高cap、输出无效后retry、因错误太少补N、因结果“成功”提前停。
- 一次请求是否执行不明确时不得重新采样同case。恢复日志可零调用分析；任何续跑须另作公开预注册amendment，保留原attempt及缺失，不能当作本版自动恢复路径。
- 首先报告技术状态，随后报告采集完成状态、capability标记、样本信息量标记；不得将这些压成“自然错误不复现”的单一标签。

完整无技术失败：`PROSPECTIVE_COLLECTION_COMPLETE`，无论W=0、传播为0或capability有限。该状态意味着采集完成，不意味着自然传播假设成立。

部分数据不静默改分母：N_planned仍120，另列N_attempted、N_observed、V、W和各阶段完成数。报告`observed_P/120`为已确认cascade的固定队列下界；若u例cascade结局无法确定，上界为`(observed_P+u)/120`。尚未运行first-hop及应运行而缺失的WRONG downstream可进入u；已观测GOLD/不合法first-hop在本协议cascade定义下不进入u。条件比率可另列完整案例描述，但同时给缺失数，不能把技术缺失编码OTHER或0；部分队列不发布“最终UCR”的单一点估计。

## 11. 实施产物与验收

建议目录 `experiments/v3_6_6/` 与 `results/v3_6_6/`。至少保存：

| 文件 | 必需内容 |
|---|---|
| spec.md / pre_registration.md / freeze_manifest.json | 本文、执行resolved spec、时间戳、commit、全部hash、阈值、seeds和调用上限 |
| validated_inheritance.json / inheritance_audit.json | 分类、来源hash、byte comparisons与台账核对 |
| cases.json / freshness_audit.json | 全120例、图、来源、历史/本版复用及排除清单 |
| identity_state_map.json / downstream_modules.json | 四人双射、全部360个预建模块、default alternate、路由规则 |
| identifier_tokenization_audit.json / decoding_freeze.json | ID约束及完整模型/tokenizer/模板/量化/软件设置 |
| prompt_plan.jsonl / call_schedule.json | 主提示、所有潜在下游提示、builder和实际次序 |
| first_hop_raw.jsonl / natural_downstream_raw.jsonl | 原始text、tokens、stop、hash、分类、provenance |
| controlled_raw.jsonl / order_diagnostic_raw.jsonl | 独立命名空间，明确pair/diagnostic IDs |
| pipeline_log.jsonl | 每例raw→identity→state→module→prompt链及skip原因 |
| case_outcomes.csv / metrics.json / paired_tables.json | 固定分母、null、缺失、CI、RD、能力及信息量标签 |
| README.md / inspection.md / limitations.md / CHANGELOG.md | 完整结论、逐调用检视、边界及变更日志 |

必须能仅从冻结manifest及raw重建所有分类、分母和报告。每个主case一行总表，包含first-hop状态、实际身份、gold、state、module、natural结局、两个controls、是否诊断及缺失理由。以base case去重，禁止以call_id数量代替n。

必要测试只覆盖新风险：全四人双射/逆映射；每条错误分支不被gold替换；三个模块可达；两臂单字段差异；parser继承及截断；GOLD/WRONG都转发；invalid跳过；diagnostic不混入主分母；W=0/null；缺失bounds；pair-RD计数；freeze/hash及禁止重复主调用。旧结果用缓存重放，禁止为了“验证已验证组件”新增模型调用。

### 最终报告顺序

1. 技术完整性、已冻结/已运行/缺失调用数及是否有偏离。
2. 120例first-hop完整分类、W/120、V/120、人物/组合覆盖。
3. natural WRONG的propagation/override/other/missing及条件区间；UCR及strict E2E。
4. gold轨迹及downstream新引入错误。
5. 两套paired RD、2×2表、capability gates及natural-vs-controlled一致表。
6. 信息量标记与错误集中性；order diagnostic仅作独立描述。
7. selection biases、适用范围、未测内容；更新台账时只新增本版实际证据。

不得只展示wrong子集而隐藏全部120例，也不得把controlled successes写成自然传播数。

## 12. No posthoc changes与change log

正式推理前冻结N、所有case和映射、aliases、renderer/parser、cap、模型revision、route、controls、诊断子集、seeds、指标、区间方法、gate、缺失规则和报告措辞阈值。

开始采集后：不得按结果更换case、wrong identity、default alternate、模块、cap、解析容忍度、分母、阈值或主指标；不得延长到“凑够20个错误”。追加分析必须标`POSTHOC_EXPLORATORY`，与预注册结果并列，不能替代。任何科学实现变更要求新版本/独立attempt和新冻结；历史raw及原报告永久保留。

| 日期/阶段 | 改动 | 理由 | 对历史结论的影响 |
|---|---|---|---|
| 2026-10-09 / spec草案 | 从frontier replication改为120例prospective collection | 直接估计全部自然轨迹，避免按yield决定是否测下游 | v3.6.5 gate结果不变 |
| 同上 | 新增无损人名编码、预建两行模块路由 | 保持validated opaque shell，明确人名接口未验证 | 新桥接须静态验证；不扩大旧接口结论 |
| 同上 | 增加每例paired controls及非gating order diagnostic | 估计同模块state干预效应并揭示呈现敏感性 | 不增加自然错误分母 |
| 实施冻结前 | 填入实际commit、文件hash、环境、审计结果及resolved差异 | 使spec成为可执行预注册 | 未填完整不得推理 |
| 执行后 | 仅附实际调用、偏离、结果及台账证据链接 | 保持审计轨迹 | 不覆写旧阈值/冻结文件 |

## 13. 已核对来源

以下链接固定在本次核对commit，避免main后续变化造成含混：

- [实验继承工作流](https://github.com/keyanding/hallucination-snowballing/blob/135968464958840259bdb6b4c6ced2951afe2e03/EXPERIMENT_WORKFLOW.md)
- [Validated findings台账](https://github.com/keyanding/hallucination-snowballing/blob/135968464958840259bdb6b4c6ced2951afe2e03/docs/validated_findings.md)
- [台账更新日志](https://github.com/keyanding/hallucination-snowballing/blob/135968464958840259bdb6b4c6ced2951afe2e03/docs/validated_findings_CHANGELOG.md)
- [v3.6.5结果](https://github.com/keyanding/hallucination-snowballing/blob/135968464958840259bdb6b4c6ced2951afe2e03/results/v3_6_5/README.md)与[预注册](https://github.com/keyanding/hallucination-snowballing/blob/135968464958840259bdb6b4c6ced2951afe2e03/results/v3_6_5/pre_registration.md)
- [HARD/N复用及历史5/24审计实现](https://github.com/keyanding/hallucination-snowballing/blob/135968464958840259bdb6b4c6ced2951afe2e03/experiments/v3_6_5/design.py)
- [原人名parser](https://github.com/keyanding/hallucination-snowballing/blob/135968464958840259bdb6b4c6ced2951afe2e03/src/interface_v3_4_4.py)
- [v3.6.3.1结果](https://github.com/keyanding/hallucination-snowballing/blob/135968464958840259bdb6b4c6ced2951afe2e03/results/v3_6_3_1/README.md)、[冻结协议](https://github.com/keyanding/hallucination-snowballing/blob/135968464958840259bdb6b4c6ced2951afe2e03/results/v3_6_3_1/pre_registration.md)及[接口实现](https://github.com/keyanding/hallucination-snowballing/blob/135968464958840259bdb6b4c6ced2951afe2e03/experiments/v3_6_3_1/design.py)
- [完整Current state shell](https://github.com/keyanding/hallucination-snowballing/blob/135968464958840259bdb6b4c6ced2951afe2e03/experiments/v3_6_1/design.py)与[继承downstream parser](https://github.com/keyanding/hallucination-snowballing/blob/135968464958840259bdb6b4c6ced2951afe2e03/experiments/v3_6_3/design.py)
