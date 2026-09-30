# v2.1 reviewed diagnosis

## Decision

**STOP. Measurement setup remains insufficiently identified.** None of the five fixed candidates passed all three strict gates, so no injected calls were made. Propagation and recovery rates remain null, not zero. Human review is required before any further experiment.

| Check | v2 | v2.1 |
|---|---:|---:|
| Baseline exact chain | 0/5 | 0/5 |
| Oracle exact downstream | 0/5 | 1/5 |
| Donor exact downstream | 0/5 | 1/5 |
| All gates for the same candidate | 0/5 | 0/5 |

## Did natural-language questions fix relation execution?

Not reliably. All five baseline first-hop identities remain wrong against the saved evidence. Four outputs now have the requested short field structure, but identify M. S. Viswanathan, David O. Russell, William A. Wellman and The Weeknd instead of the annotated people. La caída produces a long self-correction with repeated labels and is INVALID_OUTPUT. The original composer output was a location (Kerala); the new composer output is a person but still the wrong composer. Pluto no longer emits relation arrows but still identifies the wrong performer.

These observations separate surface compliance from task success. Baseline downstream labels compare with the original question's target; they do not establish whether a location is true of the model's incorrectly identified person.

## Did explicit Oracle premises resolve the supplied-input failures?

Only partially. Björk's birthplace improved from Iceland to the exact Reykjavík. Helmut Käutner changed from the compatible but broad Germany to the wrong city Berlin. Gustaf Molander still yields Stockholm, and M. B. Sreenivasan still yields Chennai. In the father question, the earlier COPY_INPUT behavior disappeared, but the new José Torre Nilsson answer still differs from the evidence-backed Leopoldo Torres Ríos.

Four of five Oracle calls therefore still fail. Explicit premises do not establish reliable downstream capability on this set. These are observed behavior changes, not evidence about the model's internal reasoning.

## Did donor capability improve?

One donor now succeeds: Gustaf Molander gives Helsinki, a saved alias of Helsingfors. The same person in the Oracle condition gives Stockholm, showing context sensitivity on this small set. Helmut Käutner gives Berlin and Chuck Berry gives Rock Island. Isaac Schwartz returns the literal `<specific location>` and Armando Robles Godoy returns `<person>`; both are INVALID_OUTPUT, not valid answers or evidence of factual knowledge.

No failed donor was substituted. No prompts were retried or edited after observing these outputs.

## Geography and evaluation

No v2.1 output was BROADER_CORRECT. The failures are therefore not explained solely by city-to-country granularity. The new location evaluator nevertheless keeps this distinction: Düsseldorf → Germany and Reykjavík → Iceland are compatible broader answers and fail only the exact-state criterion. The former is established by the saved Helmut Käutner supporting sentence; the latter by the [official Reykjavík destination site](https://visitreykjavik.is/reykjavik-fourteen-city-areas-one-capital). Geographic profiles and their evidence were fixed before generation.

Other documented containment mappings use saved evidence and official geography: [Lakshadweep's administration](https://lakshadweep.gov.in/about-lakshadweep/) identifies it as an Indian archipelago/union territory, while [St. Louis city government](https://www.stlouis-mo.gov/government/about/city-government-structure.cfm) explains its US context and distinction from St. Louis County. The map is deliberately finite; unmatched values require review rather than automatic hallucination claims. Historical Russian Empire containment for Helsingfors is not equated with present-day Russia.

## Review and reproducibility

All 15 calls used the same five candidates, Qwen3-4B-Instruct-2507 revision, NF4/BF16 GPU adapter, seed 42, greedy decoding and 128-token maximum as v2. No output was truncated; three violate the format. Peak reserved GPU memory was 3,535,798,272 bytes (about 3.29 GiB). There were no runtime failures.

`trajectories.jsonl` preserves original prompts, responses and automatic diagnoses. Ten provisional mismatch records were inspected against the saved gold/donor sentences. `semantic_reviews.jsonl` binds each confirmation to its raw-output hash and field-specific evidence; `reviewed_trajectories.jsonl` is a separate derived log. No labels or gates were changed during confirmation. `metrics.json` and `inspection.md` reflect these confirmations. Human approval is still pending.

The prior 38 v1/v2 artifact files are unchanged relative to the start of this task, including the previous task's uncommitted format-check report updates. `prior_artifact_hashes.json` and `preservation_check.json` record this check. The original SHARS source is not used or modified by v2.1.

This comparison changes natural-language phrasing, explicit Oracle premises, granularity guidance and entity-only reminders together. Two exact downstream improvements do not isolate a single cause; persistent failures cannot be attributed to model knowledge alone or to NF4 alone. No evidence about propagation strength or absence is established.
