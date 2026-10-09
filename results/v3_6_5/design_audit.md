# Pre-inference audit

Historical compatibility PASS24/24; ledger review PASS34 rows. All48 fresh targets and624 fresh record IDs;48 distinct bundles (40 historically fresh,8 reused),21 real people reused. Source evidence checks192/192; unique credited endpoint and distinct frozen downstream endpoints per case. All56 prompt/render hashes frozen. No inference-based selection or prohibited channel; empty aliases and cap96 frozen. User requires diagnostic even after failed development.

# v3.6.5 pre-registration

## Sole question and historical contract
Target v3.4.4 HARD=D4B2, N only: four credited-director links, two equal-depth comparison/associated branches, four complete candidate-name records, same substantive Film question and exact output-only-person-name instruction. Directly call unchanged no_list(c,4,2) and unchanged historical parse_natural. Rebuild all24 saved HARD/N development fixtures, full graph audits and chat strings with zero model calls. Recount historical24/24 strict-valid,5/24 wrong from raw outputs. Failure to establish this contract stops as HISTORICAL_INTERFACE_NOT_RECOVERABLE. This is not an EASY/MID search or v3.6.4 marker lookup.

## Fresh cohorts and endpoints
Fixed seed365 constructs24 development plus24 disjoint confirmation cases. Reuse the historical21 audited real people and their source-grounded downstream relation/endpoints; log reuse explicitly. Enumerate same-relation four-person bundles with disjoint endpoint alias sets; exclude all bundles from v3.4.1, v3.4.2 and v3.4.4, including held-out/unrun cases. Exactly40 fresh eligible bundles remain; use all40 plus8 seeded historically used bundles. The48 chosen bundles are distinct across both splits, then shuffled before assignment. No model output selects any case. Fresh targets48 and record IDs624 exclude all historical graph IDs. No historical target question/graph recurs. Each split has six gold identities in each candidate-array position and each initial candidate-name record position. The array is not an answer list and is never shown separately. Keep original graph semantics, path-order randomization and number/length family of IDs; new seeds/cohort sizes/bundles are documented differences.
Freeze192 candidate occurrences with their real downstream endpoints and evidence coordinates before inference, distinct endpoints within each case. No downstream endpoint appears in first-hop prompts. All candidate aliases are empty, exactly as historical v3.4.4 N; no added spelling/diacritic/punctuation tolerance. No new people are claimed.

## Parsing and gate definitions
Use historical raw.strip() only; unlike recent STATE tasks, do not add NFC normalization, terminal-period removal or casefold. Historical parser precedence: TRUNCATED first; exact canonical name (empty alias registry); multiple distinct mentions AMBIGUOUS; conservative unfamiliar name-shaped response OUT_OF_SET; otherwise NONCOMPLIANT. Supplementary mention/extraction fields never make a strict answer valid. Exact in-set output becomes IN_SET_VALID_GOLD or IN_SET_VALID_WRONG; wrong must have a pre-frozen endpoint or structural verification fails. Valid is only those two strict untruncated classes. Distinct wrong identities count canonical names, not spelling variants.
Development: fixed denominator24, Valid>=22, TRACEABLE_WRONG>=4, at least3 distinct wrong cases, AMBIGUOUS+NONCOMPLIANT+TRUNCATED<=2, every wrong has endpoint. All conjunctive. Confirmation: identical parser and definitions, wrong threshold3/24 and at least3 cases, all other thresholds unchanged. All48 cases/mappings/aliases and schedules freeze now. No repeated sampling, retries, cap sweeps, scoring/trie/likelihood calls, answer options or UNKNOWN option.

## Schedules and user resolution
Development24 in seed3651 shuffled order. Classify development before diagnostics; persist its gate before further calls. Eight diagnostic cases sampled from development with seed3652 before outputs; each receives exactly rotation2 (one-step cyclic permutation of the four complete candidate-name record lines). No graph facts, query, name-to-ID mapping or instruction changes. User explicitly resolved the conflicting stop instruction: run these8 diagnostics even when development fails. Confirmation24 in seed3653 order only if development passes, after the diagnostic; no diagnostic outcome selects/excludes errors or changes the gate. Calls32 if development fails,56 if it passes. No automatic next phase or downstream calls.

## Presentation-sensitivity definitions
Identity comparisons require both paired outputs strict-valid; report comparable coverage and missing pairs separately. Non-valid prose or unfamiliar names do not establish stable candidate identity. Fixed denominator8 for identity changes, with strict-valid coverage prominent. More than3 pairs changing candidate identity sets PRESENTATION_SENSITIVE=true; otherwise false. When unrun set not_evaluated; partial diagnostics are infrastructure failure. Also report same identity, gold-to-wrong, wrong-to-gold, wrong-to-different-wrong, same wrong identity and all paired categories. This limits interpretation but never changes the primary gate.

## Frozen runtime and priority
Same pinned Qwen3-4B-Instruct-2507 revision, tokenizer/template, NF4 double quantization/BF16, seed42, greedy fresh one-user calls, use_cache=False. Cap96 matches historical selected N cap, not a new sweep. Reuse only existing pure generate(), whose free-generation settings match the historical F path; do not call InterfaceAdapter.evaluate because it also scores. Historical render/parser compatibility is zero-call validation, not a model-stack experiment. No auxiliary model calls. Budget cannot guarantee no truncation; report it without repair.
Priority: true runtime/structural/hash/missing-call failure INFRASTRUCTURE_FAILURE; historical-contract failure HISTORICAL_INTERFACE_NOT_RECOVERABLE; failed development HARD_N_SIGNAL_NOT_REPLICATED; failed confirmation HARD_N_CONFIRMATION_FAILED; otherwise HARD_N_NATURAL_ERROR_SIGNAL_CONFIRMED. Presentation flag separate. A native loading crash terminates this attempt; no automatic retry.
The independent unit is a base case, not a diagnostic rotation; people recur across cases, limiting generalization. Confirmed means reproducible yield in this synthetic real-name interface only, not natural downstream propagation, real-world hallucination rate, natural/injected equivalence, internal mechanism or SHAR/HalluSE. If not replicated, the historical5/24 signal did not reproduce under this fresh targeted design; never claim errors impossible. Update ledger after this version, without running v3.6.6.

## Post-inference audit

All frozen inputs and historical artifacts unchanged; output plans and hashes checked; development classification persisted before diagnostics.

# v3.6.5 — HARD_N_SIGNAL_NOT_REPLICATED

只复现历史v3.4.4 HARD/N，不执行下游传播。实际调用：{'development': 24, 'presentation_diagnostic': 8, 'confirmation': 0}。

| 阶段 | Valid | Gold | Traceable wrong | Out-of-set | Ambiguous | Noncompliant | Truncated |
|---|---|---|---|---|---|---|---|
| 开发 | 24/24 | 21/24 | 3/24 | 0/24 | 0/24 | 0/24 | 0/24 |
| 确认 | 未运行 | — | — | — | — | — | — |

开发错误案例数：3；错误身份数：3。

非门槛呈现诊断：相同身份5/8、改变身份3/8；严格有效成对覆盖8/8；原始/置换严格有效分别8/8、8/8。gold→wrong=1，wrong→gold=1，wrong→different wrong=1，同一错误身份保持=0。PRESENTATION_SENSITIVE=False；诊断不改变主门槛，也不筛选错误案例。

历史HARD/N开发5/24错误信号未在这组新案例上达到预注册复现门槛；不追加难度搜索。
