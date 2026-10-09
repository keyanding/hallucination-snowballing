# v3.6.4 CHANGELOG

Added pre-registered natural first-hop frontier qualification, independent confirmation and conditional non-gating order diagnostic. Explicit C02/C04/C05 changes and user counting resolution frozen before inference. No historical experiment edited; no downstream inference.

# v3.6.4 — NO_NATURAL_ERROR_FRONTIER

本版只测试自然第一跳错误产出，不测试下游传播。实际调用：72；分阶段：{'development': 72, 'confirmation': 0, 'order_diagnostic': 0}；选定难度：无。

| 难度 | GOLD | TRACEABLE_WRONG（原始类别） | OUT_OF_UNIVERSE | INVALID | 截断 | Valid | 合格错误 | 通过 |
|---|---|---|---|---|---|---|---|---|
| EASY | 24/24 | 0/24 | 0/24 | 0/24 | 0/24 | 24/24 | 0/24 | False |
| MID | 23/24 | 0/24 | 0/24 | 1/24 | 0/24 | 23/24 | 0/24 | False |
| HARD | 23/24 | 0/24 | 0/24 | 1/24 | 0/24 | 23/24 | 0/24 | False |

没有难度通过开发门槛，按预注册停止。确认集与顺序诊断未运行；evaluated=false 不是观察到失败或顺序稳定。

本目录是用户明确授权的一次重试。首次尝试在模型加载阶段崩溃、0调用，原记录保存在父目录，未覆盖。重试复用完全相同的科学冻结输入与执行代码；72次输出均通过独立token解码和类别重计数检查。
