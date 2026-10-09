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


## 逐调用问题与输出

### development / v365-development-16/N

金标准：Bhappi Sonie；类别：IN_SET_VALID_WRONG；身份：Marcello Fondato；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R29016 names Marcello Fondato.
Record R89910 names Bhappi Sonie.
Record R44295 names Walter Hugo Khouri.
Record R95470 names Vojtěch Jasný.

Graph-link records:
Film T86246 has comparison-director link R18178.
Record R18178 has comparison-director link R97271.
Record R97271 has comparison-director link R84460.
Record R84460 has comparison-director link R29016.
Film T86246 has credited-director link R94922.
Record R94922 has credited-director link R44483.
Record R44483 has credited-director link R27764.
Record R27764 has credited-director link R89910.
Film T86246 has associated-director link R42065.
Record R42065 has associated-director link R25200.
Record R25200 has associated-director link R50369.
Record R50369 has associated-director link R44295.

Who is the credited director of Film T86246?

Output only the person's name.
```

原始回答：

```text
Marcello Fondato
```

预冻结下游端点（未展示、未调用）：San Felice Circeo

### development / v365-development-02/N

金标准：Anil Das；类别：IN_SET_VALID_WRONG；身份：Gu Changwei；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R38526 names Gu Changwei.
Record R11924 names Rolf Schübel.
Record R66550 names Anil Das.
Record R20168 names Fridrikh Ermler.

Graph-link records:
Film T60677 has credited-director link R56100.
Record R56100 has credited-director link R23108.
Record R23108 has credited-director link R46066.
Record R46066 has credited-director link R66550.
Film T60677 has comparison-director link R17128.
Record R17128 has comparison-director link R38252.
Record R38252 has comparison-director link R96156.
Record R96156 has comparison-director link R11924.
Film T60677 has associated-director link R49897.
Record R49897 has associated-director link R97490.
Record R97490 has associated-director link R51467.
Record R51467 has associated-director link R38526.

Who is the credited director of Film T60677?

Output only the person's name.
```

原始回答：

```text
Gu Changwei
```

预冻结下游端点（未展示、未调用）：Xi'an

### development / v365-development-09/N

金标准：Fridrikh Ermler；类别：IN_SET_VALID_GOLD；身份：Fridrikh Ermler；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R35261 names Rolf Schübel.
Record R49765 names Fridrikh Ermler.
Record R96622 names Rodrigo Grande.
Record R95515 names Helmut Käutner.

Graph-link records:
Film T38072 has comparison-director link R79436.
Record R79436 has comparison-director link R26757.
Record R26757 has comparison-director link R83279.
Record R83279 has comparison-director link R96622.
Film T38072 has associated-director link R43381.
Record R43381 has associated-director link R38182.
Record R38182 has associated-director link R26253.
Record R26253 has associated-director link R35261.
Film T38072 has credited-director link R49662.
Record R49662 has credited-director link R37906.
Record R37906 has credited-director link R36860.
Record R36860 has credited-director link R49765.

Who is the credited director of Film T38072?

Output only the person's name.
```

原始回答：

```text
Fridrikh Ermler
```

预冻结下游端点（未展示、未调用）：Rēzekne

### development / v365-development-23/N

金标准：Helmut Käutner；类别：IN_SET_VALID_GOLD；身份：Helmut Käutner；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R92856 names Feng Xiaoning.
Record R95607 names Rodrigo Grande.
Record R56294 names Anil Das.
Record R32463 names Helmut Käutner.

Graph-link records:
Film T59822 has comparison-director link R93219.
Record R93219 has comparison-director link R12661.
Record R12661 has comparison-director link R45413.
Record R45413 has comparison-director link R92856.
Film T59822 has associated-director link R91920.
Record R91920 has associated-director link R41461.
Record R41461 has associated-director link R67920.
Record R67920 has associated-director link R95607.
Film T59822 has credited-director link R21457.
Record R21457 has credited-director link R95347.
Record R95347 has credited-director link R63318.
Record R63318 has credited-director link R32463.

Who is the credited director of Film T59822?

Output only the person's name.
```

原始回答：

```text
Helmut Käutner
```

预冻结下游端点（未展示、未调用）：Düsseldorf

### development / v365-development-04/N

金标准：Jan Svěrák；类别：IN_SET_VALID_GOLD；身份：Jan Svěrák；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R76868 names Jan Svěrák.
Record R42541 names Ildikó Enyedi.
Record R32372 names Tinnu Anand.
Record R21553 names Armando Robles Godoy.

Graph-link records:
Film T65604 has comparison-director link R45915.
Record R45915 has comparison-director link R49965.
Record R49965 has comparison-director link R57051.
Record R57051 has comparison-director link R32372.
Film T65604 has associated-director link R17144.
Record R17144 has associated-director link R99480.
Record R99480 has associated-director link R10243.
Record R10243 has associated-director link R21553.
Film T65604 has credited-director link R74482.
Record R74482 has credited-director link R96497.
Record R96497 has credited-director link R77672.
Record R77672 has credited-director link R76868.

Who is the credited director of Film T65604?

Output only the person's name.
```

原始回答：

```text
Jan Svěrák
```

预冻结下游端点（未展示、未调用）：Zdeněk Svěrák

### development / v365-development-03/N

金标准：León Klimovsky；类别：IN_SET_VALID_GOLD；身份：León Klimovsky；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R55936 names Bhappi Sonie.
Record R50492 names Marcello Fondato.
Record R69663 names James Goldstone.
Record R16343 names León Klimovsky.

Graph-link records:
Film T46536 has associated-director link R71413.
Record R71413 has associated-director link R25059.
Record R25059 has associated-director link R70761.
Record R70761 has associated-director link R50492.
Film T46536 has comparison-director link R50338.
Record R50338 has comparison-director link R61421.
Record R61421 has comparison-director link R24378.
Record R24378 has comparison-director link R69663.
Film T46536 has credited-director link R61485.
Record R61485 has credited-director link R82100.
Record R82100 has credited-director link R76639.
Record R76639 has credited-director link R16343.

Who is the credited director of Film T46536?

Output only the person's name.
```

原始回答：

```text
León Klimovsky
```

预冻结下游端点（未展示、未调用）：Madrid

### development / v365-development-19/N

金标准：Helmut Käutner；类别：IN_SET_VALID_GOLD；身份：Helmut Käutner；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R35432 names Helmut Käutner.
Record R42330 names Anil Das.
Record R36699 names Rodrigo Grande.
Record R32164 names Rolf Schübel.

Graph-link records:
Film T52693 has comparison-director link R96271.
Record R96271 has comparison-director link R23630.
Record R23630 has comparison-director link R45214.
Record R45214 has comparison-director link R42330.
Film T52693 has credited-director link R61370.
Record R61370 has credited-director link R70984.
Record R70984 has credited-director link R41159.
Record R41159 has credited-director link R35432.
Film T52693 has associated-director link R63546.
Record R63546 has associated-director link R37589.
Record R37589 has associated-director link R25945.
Record R25945 has associated-director link R36699.

Who is the credited director of Film T52693?

Output only the person's name.
```

原始回答：

```text
Helmut Käutner
```

预冻结下游端点（未展示、未调用）：Düsseldorf

### development / v365-development-10/N

金标准：Rodrigo Grande；类别：IN_SET_VALID_GOLD；身份：Rodrigo Grande；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R43176 names Rodrigo Grande.
Record R92802 names Feng Xiaoning.
Record R24250 names Fridrikh Ermler.
Record R28457 names Anil Das.

Graph-link records:
Film T70951 has associated-director link R98909.
Record R98909 has associated-director link R78960.
Record R78960 has associated-director link R90469.
Record R90469 has associated-director link R24250.
Film T70951 has comparison-director link R74398.
Record R74398 has comparison-director link R42108.
Record R42108 has comparison-director link R67266.
Record R67266 has comparison-director link R28457.
Film T70951 has credited-director link R27383.
Record R27383 has credited-director link R77897.
Record R77897 has credited-director link R95007.
Record R95007 has credited-director link R43176.

Who is the credited director of Film T70951?

Output only the person's name.
```

原始回答：

```text
Rodrigo Grande
```

预冻结下游端点（未展示、未调用）：Rosario

### development / v365-development-15/N

金标准：Rolf Schübel；类别：IN_SET_VALID_GOLD；身份：Rolf Schübel；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R83009 names Fridrikh Ermler.
Record R74319 names Rolf Schübel.
Record R90987 names Gu Changwei.
Record R42978 names Rodrigo Grande.

Graph-link records:
Film T42912 has associated-director link R32565.
Record R32565 has associated-director link R33019.
Record R33019 has associated-director link R86828.
Record R86828 has associated-director link R83009.
Film T42912 has comparison-director link R14250.
Record R14250 has comparison-director link R72596.
Record R72596 has comparison-director link R38784.
Record R38784 has comparison-director link R90987.
Film T42912 has credited-director link R15374.
Record R15374 has credited-director link R81343.
Record R81343 has credited-director link R46896.
Record R46896 has credited-director link R74319.

Who is the credited director of Film T42912?

Output only the person's name.
```

原始回答：

```text
Rolf Schübel
```

预冻结下游端点（未展示、未调用）：Stuttgart

### development / v365-development-24/N

金标准：Robert P. Kerr；类别：IN_SET_VALID_GOLD；身份：Robert P. Kerr；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R84795 names Vojtěch Jasný.
Record R93463 names Marcello Fondato.
Record R69562 names Robert P. Kerr.
Record R68211 names James Goldstone.

Graph-link records:
Film T47175 has associated-director link R55968.
Record R55968 has associated-director link R90271.
Record R90271 has associated-director link R33466.
Record R33466 has associated-director link R84795.
Film T47175 has credited-director link R26846.
Record R26846 has credited-director link R54754.
Record R54754 has credited-director link R20115.
Record R20115 has credited-director link R69562.
Film T47175 has comparison-director link R79805.
Record R79805 has comparison-director link R48319.
Record R48319 has comparison-director link R79968.
Record R79968 has comparison-director link R93463.

Who is the credited director of Film T47175?

Output only the person's name.
```

原始回答：

```text
Robert P. Kerr
```

预冻结下游端点（未展示、未调用）：Porterville

### development / v365-development-21/N

金标准：Vojtěch Jasný；类别：IN_SET_VALID_GOLD；身份：Vojtěch Jasný；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R25144 names Vojtěch Jasný.
Record R12045 names Robert P. Kerr.
Record R23124 names Bhappi Sonie.
Record R95062 names Marcello Fondato.

Graph-link records:
Film T28375 has associated-director link R84127.
Record R84127 has associated-director link R14796.
Record R14796 has associated-director link R42085.
Record R42085 has associated-director link R95062.
Film T28375 has comparison-director link R49519.
Record R49519 has comparison-director link R65789.
Record R65789 has comparison-director link R35733.
Record R35733 has comparison-director link R23124.
Film T28375 has credited-director link R42902.
Record R42902 has credited-director link R70477.
Record R70477 has credited-director link R42458.
Record R42458 has credited-director link R25144.

Who is the credited director of Film T28375?

Output only the person's name.
```

原始回答：

```text
Vojtěch Jasný
```

预冻结下游端点（未展示、未调用）：Přerov

### development / v365-development-08/N

金标准：Rodrigo Grande；类别：IN_SET_VALID_GOLD；身份：Rodrigo Grande；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R49112 names Rodrigo Grande.
Record R46941 names Helmut Käutner.
Record R16092 names Fridrikh Ermler.
Record R67173 names Anil Das.

Graph-link records:
Film T61497 has credited-director link R66459.
Record R66459 has credited-director link R11652.
Record R11652 has credited-director link R62525.
Record R62525 has credited-director link R49112.
Film T61497 has associated-director link R35702.
Record R35702 has associated-director link R47960.
Record R47960 has associated-director link R60550.
Record R60550 has associated-director link R16092.
Film T61497 has comparison-director link R70419.
Record R70419 has comparison-director link R49666.
Record R49666 has comparison-director link R91787.
Record R91787 has comparison-director link R67173.

Who is the credited director of Film T61497?

Output only the person's name.
```

原始回答：

```text
Rodrigo Grande
```

预冻结下游端点（未展示、未调用）：Rosario

### development / v365-development-05/N

金标准：Vojtěch Jasný；类别：IN_SET_VALID_GOLD；身份：Vojtěch Jasný；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R14753 names Vojtěch Jasný.
Record R96674 names Robert P. Kerr.
Record R92314 names Walter Hugo Khouri.
Record R34925 names Bhappi Sonie.

Graph-link records:
Film T57743 has associated-director link R51363.
Record R51363 has associated-director link R62999.
Record R62999 has associated-director link R70256.
Record R70256 has associated-director link R92314.
Film T57743 has comparison-director link R17541.
Record R17541 has comparison-director link R67235.
Record R67235 has comparison-director link R10834.
Record R10834 has comparison-director link R34925.
Film T57743 has credited-director link R99621.
Record R99621 has credited-director link R36949.
Record R36949 has credited-director link R82954.
Record R82954 has credited-director link R14753.

Who is the credited director of Film T57743?

Output only the person's name.
```

原始回答：

```text
Vojtěch Jasný
```

预冻结下游端点（未展示、未调用）：Přerov

### development / v365-development-14/N

金标准：Yuen Woo-ping；类别：IN_SET_VALID_GOLD；身份：Yuen Woo-ping；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R61204 names Armando Robles Godoy.
Record R13749 names Yuen Woo-ping.
Record R43578 names Ildikó Enyedi.
Record R17892 names Leopoldo Torre Nilsson.

Graph-link records:
Film T97862 has associated-director link R39137.
Record R39137 has associated-director link R73791.
Record R73791 has associated-director link R18808.
Record R18808 has associated-director link R61204.
Film T97862 has credited-director link R77009.
Record R77009 has credited-director link R37118.
Record R37118 has credited-director link R78760.
Record R78760 has credited-director link R13749.
Film T97862 has comparison-director link R63057.
Record R63057 has comparison-director link R79316.
Record R79316 has comparison-director link R70928.
Record R70928 has comparison-director link R43578.

Who is the credited director of Film T97862?

Output only the person's name.
```

原始回答：

```text
Yuen Woo-ping
```

预冻结下游端点（未展示、未调用）：Yuen Siu-tien

### development / v365-development-18/N

金标准：Rolf Schübel；类别：IN_SET_VALID_GOLD；身份：Rolf Schübel；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R18280 names Fridrikh Ermler.
Record R34698 names Helmut Käutner.
Record R80847 names Anil Das.
Record R80368 names Rolf Schübel.

Graph-link records:
Film T86441 has associated-director link R46577.
Record R46577 has associated-director link R95143.
Record R95143 has associated-director link R36874.
Record R36874 has associated-director link R80847.
Film T86441 has credited-director link R73815.
Record R73815 has credited-director link R14643.
Record R14643 has credited-director link R11297.
Record R11297 has credited-director link R80368.
Film T86441 has comparison-director link R12425.
Record R12425 has comparison-director link R65433.
Record R65433 has comparison-director link R82679.
Record R82679 has comparison-director link R34698.

Who is the credited director of Film T86441?

Output only the person's name.
```

原始回答：

```text
Rolf Schübel
```

预冻结下游端点（未展示、未调用）：Stuttgart

### development / v365-development-01/N

金标准：Ildikó Enyedi；类别：IN_SET_VALID_GOLD；身份：Ildikó Enyedi；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R99220 names Armando Robles Godoy.
Record R30517 names Ildikó Enyedi.
Record R27460 names Leopoldo Torre Nilsson.
Record R85180 names Jan Svěrák.

Graph-link records:
Film T37900 has comparison-director link R40255.
Record R40255 has comparison-director link R51367.
Record R51367 has comparison-director link R79584.
Record R79584 has comparison-director link R27460.
Film T37900 has credited-director link R15328.
Record R15328 has credited-director link R68643.
Record R68643 has credited-director link R71138.
Record R71138 has credited-director link R30517.
Film T37900 has associated-director link R66381.
Record R66381 has associated-director link R43776.
Record R43776 has associated-director link R47858.
Record R47858 has associated-director link R85180.

Who is the credited director of Film T37900?

Output only the person's name.
```

原始回答：

```text
Ildikó Enyedi
```

预冻结下游端点（未展示、未调用）：György Enyedi

### development / v365-development-07/N

金标准：Rodrigo Grande；类别：IN_SET_VALID_GOLD；身份：Rodrigo Grande；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R80693 names Gu Changwei.
Record R77265 names Helmut Käutner.
Record R80158 names Rolf Schübel.
Record R50895 names Rodrigo Grande.

Graph-link records:
Film T69477 has associated-director link R89988.
Record R89988 has associated-director link R81033.
Record R81033 has associated-director link R32662.
Record R32662 has associated-director link R80693.
Film T69477 has comparison-director link R12365.
Record R12365 has comparison-director link R77895.
Record R77895 has comparison-director link R77238.
Record R77238 has comparison-director link R77265.
Film T69477 has credited-director link R68179.
Record R68179 has credited-director link R20072.
Record R20072 has credited-director link R28105.
Record R28105 has credited-director link R50895.

Who is the credited director of Film T69477?

Output only the person's name.
```

原始回答：

```text
Rodrigo Grande
```

预冻结下游端点（未展示、未调用）：Rosario

### development / v365-development-12/N

金标准：Jan Svěrák；类别：IN_SET_VALID_GOLD；身份：Jan Svěrák；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R59351 names Rahul Rawail.
Record R77019 names Armando Robles Godoy.
Record R14829 names Yuen Woo-ping.
Record R76750 names Jan Svěrák.

Graph-link records:
Film T59096 has comparison-director link R69341.
Record R69341 has comparison-director link R44331.
Record R44331 has comparison-director link R48936.
Record R48936 has comparison-director link R77019.
Film T59096 has credited-director link R99821.
Record R99821 has credited-director link R63379.
Record R63379 has credited-director link R23375.
Record R23375 has credited-director link R76750.
Film T59096 has associated-director link R98295.
Record R98295 has associated-director link R76731.
Record R76731 has associated-director link R41309.
Record R41309 has associated-director link R59351.

Who is the credited director of Film T59096?

Output only the person's name.
```

原始回答：

```text
Jan Svěrák
```

预冻结下游端点（未展示、未调用）：Zdeněk Svěrák

### development / v365-development-11/N

金标准：Leopoldo Torre Nilsson；类别：IN_SET_VALID_WRONG；身份：Rahul Rawail；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R79145 names Rahul Rawail.
Record R66787 names Leopoldo Torre Nilsson.
Record R13111 names Ildikó Enyedi.
Record R61846 names Jan Svěrák.

Graph-link records:
Film T66257 has credited-director link R63618.
Record R63618 has credited-director link R53202.
Record R53202 has credited-director link R81595.
Record R81595 has credited-director link R66787.
Film T66257 has comparison-director link R17937.
Record R17937 has comparison-director link R63313.
Record R63313 has comparison-director link R51614.
Record R51614 has comparison-director link R79145.
Film T66257 has associated-director link R45688.
Record R45688 has associated-director link R38949.
Record R38949 has associated-director link R29160.
Record R29160 has associated-director link R61846.

Who is the credited director of Film T66257?

Output only the person's name.
```

原始回答：

```text
Rahul Rawail
```

预冻结下游端点（未展示、未调用）：H. S. Rawail

### development / v365-development-22/N

金标准：Bhappi Sonie；类别：IN_SET_VALID_GOLD；身份：Bhappi Sonie；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R78951 names James Goldstone.
Record R42254 names Robert P. Kerr.
Record R11077 names Bhappi Sonie.
Record R57295 names Walter Hugo Khouri.

Graph-link records:
Film T18498 has comparison-director link R10702.
Record R10702 has comparison-director link R80095.
Record R80095 has comparison-director link R45027.
Record R45027 has comparison-director link R78951.
Film T18498 has associated-director link R65823.
Record R65823 has associated-director link R79710.
Record R79710 has associated-director link R28592.
Record R28592 has associated-director link R57295.
Film T18498 has credited-director link R26691.
Record R26691 has credited-director link R65186.
Record R65186 has credited-director link R89281.
Record R89281 has credited-director link R11077.

Who is the credited director of Film T18498?

Output only the person's name.
```

原始回答：

```text
Bhappi Sonie
```

预冻结下游端点（未展示、未调用）：Mumbai

### development / v365-development-13/N

金标准：Yuen Woo-ping；类别：IN_SET_VALID_GOLD；身份：Yuen Woo-ping；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R80996 names Jan Svěrák.
Record R29533 names Ildikó Enyedi.
Record R33151 names Yuen Woo-ping.
Record R92244 names Leopoldo Torre Nilsson.

Graph-link records:
Film T76103 has credited-director link R43853.
Record R43853 has credited-director link R86914.
Record R86914 has credited-director link R28116.
Record R28116 has credited-director link R33151.
Film T76103 has associated-director link R55120.
Record R55120 has associated-director link R34585.
Record R34585 has associated-director link R40482.
Record R40482 has associated-director link R29533.
Film T76103 has comparison-director link R70711.
Record R70711 has comparison-director link R17863.
Record R17863 has comparison-director link R14630.
Record R14630 has comparison-director link R92244.

Who is the credited director of Film T76103?

Output only the person's name.
```

原始回答：

```text
Yuen Woo-ping
```

预冻结下游端点（未展示、未调用）：Yuen Siu-tien

### development / v365-development-17/N

金标准：Rahul Rawail；类别：IN_SET_VALID_GOLD；身份：Rahul Rawail；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R94559 names Tinnu Anand.
Record R40242 names Armando Robles Godoy.
Record R84804 names Ildikó Enyedi.
Record R24910 names Rahul Rawail.

Graph-link records:
Film T55040 has credited-director link R15160.
Record R15160 has credited-director link R95403.
Record R95403 has credited-director link R58288.
Record R58288 has credited-director link R24910.
Film T55040 has comparison-director link R61191.
Record R61191 has comparison-director link R84121.
Record R84121 has comparison-director link R77636.
Record R77636 has comparison-director link R40242.
Film T55040 has associated-director link R46996.
Record R46996 has associated-director link R74131.
Record R74131 has associated-director link R92126.
Record R92126 has associated-director link R84804.

Who is the credited director of Film T55040?

Output only the person's name.
```

原始回答：

```text
Rahul Rawail
```

预冻结下游端点（未展示、未调用）：H. S. Rawail

### development / v365-development-06/N

金标准：James Goldstone；类别：IN_SET_VALID_GOLD；身份：James Goldstone；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R44784 names Walter Hugo Khouri.
Record R36266 names Robert P. Kerr.
Record R41066 names James Goldstone.
Record R94845 names Marcello Fondato.

Graph-link records:
Film T64641 has comparison-director link R29646.
Record R29646 has comparison-director link R72651.
Record R72651 has comparison-director link R18313.
Record R18313 has comparison-director link R44784.
Film T64641 has associated-director link R21206.
Record R21206 has associated-director link R44052.
Record R44052 has associated-director link R85041.
Record R85041 has associated-director link R94845.
Film T64641 has credited-director link R30925.
Record R30925 has credited-director link R28068.
Record R28068 has credited-director link R44154.
Record R44154 has credited-director link R41066.

Who is the credited director of Film T64641?

Output only the person's name.
```

原始回答：

```text
James Goldstone
```

预冻结下游端点（未展示、未调用）：Shaftsbury, Vermont

### development / v365-development-20/N

金标准：León Klimovsky；类别：IN_SET_VALID_GOLD；身份：León Klimovsky；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R70435 names Vojtěch Jasný.
Record R51845 names James Goldstone.
Record R84049 names León Klimovsky.
Record R72323 names Bhappi Sonie.

Graph-link records:
Film T26615 has credited-director link R10549.
Record R10549 has credited-director link R84080.
Record R84080 has credited-director link R38140.
Record R38140 has credited-director link R84049.
Film T26615 has associated-director link R56082.
Record R56082 has associated-director link R18662.
Record R18662 has associated-director link R57337.
Record R57337 has associated-director link R51845.
Film T26615 has comparison-director link R64024.
Record R64024 has comparison-director link R61725.
Record R61725 has comparison-director link R18677.
Record R18677 has comparison-director link R72323.

Who is the credited director of Film T26615?

Output only the person's name.
```

原始回答：

```text
León Klimovsky
```

预冻结下游端点（未展示、未调用）：Madrid

### presentation_diagnostic / v365-development-15/R2

金标准：Rolf Schübel；类别：IN_SET_VALID_GOLD；身份：Rolf Schübel；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R74319 names Rolf Schübel.
Record R90987 names Gu Changwei.
Record R42978 names Rodrigo Grande.
Record R83009 names Fridrikh Ermler.

Graph-link records:
Film T42912 has associated-director link R32565.
Record R32565 has associated-director link R33019.
Record R33019 has associated-director link R86828.
Record R86828 has associated-director link R83009.
Film T42912 has comparison-director link R14250.
Record R14250 has comparison-director link R72596.
Record R72596 has comparison-director link R38784.
Record R38784 has comparison-director link R90987.
Film T42912 has credited-director link R15374.
Record R15374 has credited-director link R81343.
Record R81343 has credited-director link R46896.
Record R46896 has credited-director link R74319.

Who is the credited director of Film T42912?

Output only the person's name.
```

原始回答：

```text
Rolf Schübel
```

预冻结下游端点（未展示、未调用）：Stuttgart

### presentation_diagnostic / v365-development-02/R2

金标准：Anil Das；类别：IN_SET_VALID_WRONG；身份：Rolf Schübel；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R11924 names Rolf Schübel.
Record R66550 names Anil Das.
Record R20168 names Fridrikh Ermler.
Record R38526 names Gu Changwei.

Graph-link records:
Film T60677 has credited-director link R56100.
Record R56100 has credited-director link R23108.
Record R23108 has credited-director link R46066.
Record R46066 has credited-director link R66550.
Film T60677 has comparison-director link R17128.
Record R17128 has comparison-director link R38252.
Record R38252 has comparison-director link R96156.
Record R96156 has comparison-director link R11924.
Film T60677 has associated-director link R49897.
Record R49897 has associated-director link R97490.
Record R97490 has associated-director link R51467.
Record R51467 has associated-director link R38526.

Who is the credited director of Film T60677?

Output only the person's name.
```

原始回答：

```text
Rolf Schübel
```

预冻结下游端点（未展示、未调用）：Stuttgart

### presentation_diagnostic / v365-development-01/R2

金标准：Ildikó Enyedi；类别：IN_SET_VALID_GOLD；身份：Ildikó Enyedi；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R30517 names Ildikó Enyedi.
Record R27460 names Leopoldo Torre Nilsson.
Record R85180 names Jan Svěrák.
Record R99220 names Armando Robles Godoy.

Graph-link records:
Film T37900 has comparison-director link R40255.
Record R40255 has comparison-director link R51367.
Record R51367 has comparison-director link R79584.
Record R79584 has comparison-director link R27460.
Film T37900 has credited-director link R15328.
Record R15328 has credited-director link R68643.
Record R68643 has credited-director link R71138.
Record R71138 has credited-director link R30517.
Film T37900 has associated-director link R66381.
Record R66381 has associated-director link R43776.
Record R43776 has associated-director link R47858.
Record R47858 has associated-director link R85180.

Who is the credited director of Film T37900?

Output only the person's name.
```

原始回答：

```text
Ildikó Enyedi
```

预冻结下游端点（未展示、未调用）：György Enyedi

### presentation_diagnostic / v365-development-11/R2

金标准：Leopoldo Torre Nilsson；类别：IN_SET_VALID_GOLD；身份：Leopoldo Torre Nilsson；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R66787 names Leopoldo Torre Nilsson.
Record R13111 names Ildikó Enyedi.
Record R61846 names Jan Svěrák.
Record R79145 names Rahul Rawail.

Graph-link records:
Film T66257 has credited-director link R63618.
Record R63618 has credited-director link R53202.
Record R53202 has credited-director link R81595.
Record R81595 has credited-director link R66787.
Film T66257 has comparison-director link R17937.
Record R17937 has comparison-director link R63313.
Record R63313 has comparison-director link R51614.
Record R51614 has comparison-director link R79145.
Film T66257 has associated-director link R45688.
Record R45688 has associated-director link R38949.
Record R38949 has associated-director link R29160.
Record R29160 has associated-director link R61846.

Who is the credited director of Film T66257?

Output only the person's name.
```

原始回答：

```text
Leopoldo Torre Nilsson
```

预冻结下游端点（未展示、未调用）：Leopoldo Torres Ríos

### presentation_diagnostic / v365-development-17/R2

金标准：Rahul Rawail；类别：IN_SET_VALID_GOLD；身份：Rahul Rawail；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R40242 names Armando Robles Godoy.
Record R84804 names Ildikó Enyedi.
Record R24910 names Rahul Rawail.
Record R94559 names Tinnu Anand.

Graph-link records:
Film T55040 has credited-director link R15160.
Record R15160 has credited-director link R95403.
Record R95403 has credited-director link R58288.
Record R58288 has credited-director link R24910.
Film T55040 has comparison-director link R61191.
Record R61191 has comparison-director link R84121.
Record R84121 has comparison-director link R77636.
Record R77636 has comparison-director link R40242.
Film T55040 has associated-director link R46996.
Record R46996 has associated-director link R74131.
Record R74131 has associated-director link R92126.
Record R92126 has associated-director link R84804.

Who is the credited director of Film T55040?

Output only the person's name.
```

原始回答：

```text
Rahul Rawail
```

预冻结下游端点（未展示、未调用）：H. S. Rawail

### presentation_diagnostic / v365-development-12/R2

金标准：Jan Svěrák；类别：IN_SET_VALID_WRONG；身份：Armando Robles Godoy；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R77019 names Armando Robles Godoy.
Record R14829 names Yuen Woo-ping.
Record R76750 names Jan Svěrák.
Record R59351 names Rahul Rawail.

Graph-link records:
Film T59096 has comparison-director link R69341.
Record R69341 has comparison-director link R44331.
Record R44331 has comparison-director link R48936.
Record R48936 has comparison-director link R77019.
Film T59096 has credited-director link R99821.
Record R99821 has credited-director link R63379.
Record R63379 has credited-director link R23375.
Record R23375 has credited-director link R76750.
Film T59096 has associated-director link R98295.
Record R98295 has associated-director link R76731.
Record R76731 has associated-director link R41309.
Record R41309 has associated-director link R59351.

Who is the credited director of Film T59096?

Output only the person's name.
```

原始回答：

```text
Armando Robles Godoy
```

预冻结下游端点（未展示、未调用）：Daniel Alomía Robles

### presentation_diagnostic / v365-development-04/R2

金标准：Jan Svěrák；类别：IN_SET_VALID_GOLD；身份：Jan Svěrák；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R42541 names Ildikó Enyedi.
Record R32372 names Tinnu Anand.
Record R21553 names Armando Robles Godoy.
Record R76868 names Jan Svěrák.

Graph-link records:
Film T65604 has comparison-director link R45915.
Record R45915 has comparison-director link R49965.
Record R49965 has comparison-director link R57051.
Record R57051 has comparison-director link R32372.
Film T65604 has associated-director link R17144.
Record R17144 has associated-director link R99480.
Record R99480 has associated-director link R10243.
Record R10243 has associated-director link R21553.
Film T65604 has credited-director link R74482.
Record R74482 has credited-director link R96497.
Record R96497 has credited-director link R77672.
Record R77672 has credited-director link R76868.

Who is the credited director of Film T65604?

Output only the person's name.
```

原始回答：

```text
Jan Svěrák
```

预冻结下游端点（未展示、未调用）：Zdeněk Svěrák

### presentation_diagnostic / v365-development-20/R2

金标准：León Klimovsky；类别：IN_SET_VALID_GOLD；身份：León Klimovsky；截断：False。

完整提问：

```text
This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; the candidate names refer to real people. Use only the records below. The relation vocabulary is credited-director, comparison-director, associated-director. Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. Comparison-director and associated-director links describe separate catalog relations. The credited director means the candidate reached by that traversal.

Candidate-name records:
Record R51845 names James Goldstone.
Record R84049 names León Klimovsky.
Record R72323 names Bhappi Sonie.
Record R70435 names Vojtěch Jasný.

Graph-link records:
Film T26615 has credited-director link R10549.
Record R10549 has credited-director link R84080.
Record R84080 has credited-director link R38140.
Record R38140 has credited-director link R84049.
Film T26615 has associated-director link R56082.
Record R56082 has associated-director link R18662.
Record R18662 has associated-director link R57337.
Record R57337 has associated-director link R51845.
Film T26615 has comparison-director link R64024.
Record R64024 has comparison-director link R61725.
Record R61725 has comparison-director link R18677.
Record R18677 has comparison-director link R72323.

Who is the credited director of Film T26615?

Output only the person's name.
```

原始回答：

```text
León Klimovsky
```

预冻结下游端点（未展示、未调用）：Madrid
