# v3 Track A: reviewed smoke result

**Quantitative gate PASS; stop for human review.** All ten fixed synthetic cases are eligible and fully interpretable. The 80 recorded calls contain no errors, refusals, format failures, truncations or order-dependent answers.

| Outcome | Count | Rate |
|---|---:|---:|
| Direct context lookup (CLA) | 40/40 | 100% |
| Baseline state adherence | 20/20 | 100% |
| Injected state adherence / PROPAGATE | 20/20 | 100% |
| OVERRIDE_TO_GOLD | 0/20 | 0% |
| OUT_OF_CONTEXT_HALLUCINATION | 0/20 | 0% |
| UNKNOWN_REJECT | 0/20 | 0% |
| Injected INVALID_OUTPUT | 0/20 | 0% |
| Evidence-order disagreement | 0/40 paired comparisons | 0% |
| Direct-success / state-failure contrasts | 0/40 | 0% |

The relation breakdown is four birthplace, three death-place and three father pairs. Every pair gives C under B and C′ under B′ for both evidence orders. For example, Lorvi Polven's supplied father fact yields Zevra Kelmor, while changing only the current-state field to Peldra Dirvek yields Pavrek Zemrik. The two reference facts and downstream question are unchanged. Reversing the two facts leaves both answers unchanged.

All answers are literal target names after the stated whitespace normalization; no answer extraction, alias addition, semantic relabeling or output-dependent case substitution was needed. Inspection confirms that the prompts contain only two downstream facts, an optional state field, one relation question and one short output instruction. Direct controls never mention the current-state frame. No first-hop clue or assertion that one state is correct appears in the prompts.

This establishes a successful **controlled state-following assay on these ten synthetic cases**: when the model is externally assigned either intermediate entity and given the relevant facts, it selects that entity's downstream target. The design does not establish that B′ was spontaneously hallucinated, nor that it is internally regarded as false. With no original first-hop task, B and B′ are experimental assignments. The 100% figure is not an estimate of natural hallucination propagation in open-ended reasoning.

Compared with v2/v2.1, the apparatus now demonstrates reliable reference lookup and stable use of the state frame on this synthetic set. It does not isolate a single cause of the earlier failures: the entity domain, supplied evidence, prompt structure, output instruction, token cap and caching configuration also differ. The result does not yet establish real-entity robustness; Track B remains unrun.

The original threshold policy was fixed before inference in `protocol.md` and `preparation.json`. No particular propagation rate was required to pass. Evidence orders are repeated measurements of the same ten cases, not 20 independently sampled cases. There is no population-level or statistical-significance claim.

The existing Qwen3-4B model ran with NF4/BF16 entirely on GPU, using independent single-user prompts, greedy decoding and a 32-token cap. KV caching was disabled. Per-call isolation fields and a regression test cover the actual adapter path. Source/data/prompt/raw-response hashes are recorded. Peak reserved GPU memory was 3,500,146,688 bytes (about 3.26 GiB). All 55 prior v1/v2/v2.1 artifact files remain byte-identical.

Specification §24 explicitly says **“Stop for human review”** after producing the smoke inspection. Accordingly, no 30–50-pair pilot or real-entity Track B has been started. `gate.json` records a passed measurement gate while leaving `human_review_required=true`, `scale_authorized=false` and `track_b_authorized=false`. SHARS/HalluSE remains outside this experiment.
