# Pre-inference design audit

| Prior | Component / result | Classification | Treatment | Validation |
|---|---|---|---|---|
| v3.6.1/v3.6.2 | minimal downstream shell: Minimal mapped-state interface passed | FROZEN_REUSE | Reuse Current state shell exactly | Byte equality to both frozen renderers; calibration C/D/F/G |
| v3.6.1 | mapped-state UNKNOWN policy: Fallback unnecessary for mapped-state assay; tested alternatives brittle | FROZEN_REUSE | No UNKNOWN rule in any prompt | Literal prompt audit |
| v3.6.1/v3.6.3 | identifiers and parser: Opaque matched IDs and exact parsing established | FROZEN_REUSE | Same generator, expanded historical exclusion; exact v3.6.3 parser | 7800-candidate token audit, freshness and parser tests |
| v3.6.2 | context accumulation: No failures up to 24 irrelevant mappings | NOT_RELEVANT | Use two mappings without distractors | Exactly two downstream records |
| v3.6.2 | record position: No position failures observed in tested diagnostic | NOT_RELEVANT | No new main position manipulation; retain balanced order construction | Inherited order construction audit |
| v3.6.3 | upstream shell: Calibration upstream A/B/paired each 20/20 | FROZEN_REUSE | Reuse upstream renderer exactly | Byte equality and calibration A/B/E/G |
| v3.6.3 | recorded shell: Recorded shell calibration had three exact-output failures | INTENTIONALLY_RETESTED | Exact former shell in independent diagnostic only | Paired same-state/mapping shell comparison; non-gating |
| v3.6.1/v3.6.2/v3.6.3 | model and decoding: Pinned NF4/BF16 stateless greedy stack used | FROZEN_REUSE | Same revision/tokenizer/chat template, seed42, cap16 | Versions, template hash, render hash and runtime manifest |
| v3.6.3 | integrated shell: Integrated shell frozen but untested after failed calibration | INTENTIONALLY_RETESTED | Reuse exact integrated renderer on 20 main cases after main passes | Separate readiness thresholds, no main-gate effect |

All 70 cases passed literal U/D/I A/B diffs; every validated downstream pair equals both v3.6.1 and v3.6.2 renderers byte for byte. Upstream/integrated/recorded diagnostic reuse v3.6.3 source directly. Main has no recorded heading, entities in downstream, UNKNOWN instructions or answer lists. 420 fresh unique IDs from 7800 tokenized candidates; matched role-pair token and character counts. Calibration/main/shell sets disjoint; integrated intentionally a main subset. No model outputs used for selection.

Maximum360 calls. Calibration gates precede any main/diagnostic call; main gates precede integrated only; independent shell diagnostic follows completed main regardless of main accuracy. Actual pipeline state is never repaired. Templates/builders and parser/gates are frozen; dynamic full hashes are saved at execution. No cap increase or next phase. Shell flags are frozen descriptive heuristics; no mechanism inference. Workflow validator and source comparison checks passed.

## Post-inference audit

| Calibration gate | Count | Minimum | Pass |
|---|---|---|---|
| A | 20/20 | 19 | True |
| B | 20/20 | 19 | True |
| C | 20/20 | 19 | True |
| D | 20/20 | 19 | True |
| E | 20/20 | 19 | True |
| F | 20/20 | 19 | True |
| G | 80/80 | 79 | True |

| Main metric | Count | Wilson 95% | Gate passed |
|---|---|---|---|
| A_U_A | 40/40 | [91.2%, 100.0%] | True |
| A_U_B | 40/40 | [91.2%, 100.0%] | True |
| A_D_A | 40/40 | [91.2%, 100.0%] | True |
| A_D_B | 40/40 | [91.2%, 100.0%] | True |
| S_D | 40/40 | [91.2%, 100.0%] | True |
| E2E | 40/40 | [91.2%, 100.0%] | True |

Decision: TWO_HOP_PIPELINE_VALIDATED. Readiness=False; evaluated=True. Frozen hashes and actual state forwarding verified.
