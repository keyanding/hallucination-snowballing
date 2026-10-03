# v3.4 pre-inference protocol

## Fixed universe and evidence

Twenty unique real film questions from the frozen 2Wiki dev.json, seed 42. Gold directors are Gu Changwei, Yuen Woo-ping, Rahul Rawail, Ildikó Enyedi, James Goldstone, León Klimovsky, Bhappi Sonie and Walter Hugo Khouri. These eight have multiple films with explicit single-director source evidence and previously reviewed downstream facts. Their twenty available selected films comprise three birth-place, eight father and nine death-place tasks. Directors and targets recur across cases; these are twenty questions, not twenty independent entity samples. The choice uses source availability and earlier reviewed evidence, not v3.4 outputs.

Each case has one gold and three alternative real directors. Prefer the nearest documented film eras, with a maximum 30-year gap for alternative-director film evidence; break ties by name/title, enforce distinct target values and disjoint frozen aliases. Anil Das's Alice film year is explicitly sourced to sentence 8 of his article (2014), not guessed from the film article, which omits a year. Gold positions are balanced five per candidate-list slot; candidate order, evidence order and the registered W0 alternative are frozen with seed 42.

Design A is a five-sentence composition task: A and a bridge film Y have the same director, plus four distinct bridge-film/director facts (one per candidate). The shared-director equality is a derived fact grounded in two explicit source claims, not a direct quotation or an invented event. All raw supporting sentences and source coordinates are saved. The prompt never gives A→B directly. Mentioning all four candidate names in the evidence removes a shortcut based on the only name appearing. No adversarially false evidence or output-dependent difficulty tuning.

Every candidate's downstream mapping reuses an explicitly reviewed fact from the v3.3 source pool. Exact source sentences are checked again against frozen dev.json. Unique targets and disjoint aliases are mandatory; ambiguous combinations are rejected before inference. No new mappings or aliases may be added after Phase A.

## Prompts, checkpoints and isolation

First-hop input contains the original question, four candidates and five first-hop facts. Downstream facts are withheld until continuation, so first-hop selection cannot use their wording as an extra cue. Answer must be one listed candidate name. Candidate matching is exact after trimming outer whitespace; even punctuation/case variants that are not listed are OUT_OF_SET_ENTITY, never coerced. The existing short-answer parser separates malformed/unknown responses as INVALID_OUTPUT. OSER counts parseable out-of-set responses; invalid rate is reported separately, with all four first-hop classes summing to twenty.

Reuse the same Qwen3-4B-Instruct-2507 revision, NF4/BF16, greedy decoding, 32-token limit and disabled thinking. The v3.3 adapter is reused unchanged. Save the exact rendered first-hop prompt, raw answer and completed chat checkpoint; verify the checkpoint begins with the actual rendered prompt plus answer.

N0 replays that checkpoint exactly. C0 replaces only the assistant answer span with B; W0 uses the natural wrong candidate if present, otherwise the frozen alternative. All three append the same new user message with all four downstream mappings and a second-hop-only question. Each is a fresh call with explicit transcript replay and no cross-call history or KV cache. There is no first-hop regeneration and no E1/E2/E3 manipulation. S0 contains only four downstream facts and the natural wrong state, and runs only for eligible natural errors. Its comparison with N0 includes the intentional task-transcript/chat-role difference.

Exact duplicate rendered branch prompts share one actual model call. logical_branches.json maps N0/C0/W0/S0 to immutable call IDs. Do not treat reused labels as independent observations. If all cases execute, the total is 20 first hops + 80 lookups + 40 distinct N0/C0/W0 calls + one S0 per eligible natural error (maximum 160).

## Stage progression and stop policy

Run all twenty first-hop selections once. If fewer than five TRACEABLE_WRONG_CANDIDATE responses occur, fewer than fifteen in-set valid responses occur, or OSER exceeds 25%, stop before direct lookups and downstream branches. Save an empty branch_trajectories.jsonl, null unmeasured metrics and a failed gate. A low error yield is not permission to swap candidates, increase difficulty or run a replacement sample.

Otherwise run all eighty direct lookup controls independently. If CLA_all <95%, stop before branches. A case must pass all four direct controls to enter clean branch analysis. Invalid/out-of-set first hops are retained but not assigned a candidate. Never force an out-of-set entity into W0. Execute the complete branch matrix for each remaining case; if invalid downstream outputs exceed 10% of accumulated state calls, stop after the case. Illegal prefix changes or ambiguous/unmatched mappings stop immediately.

## Metrics and gate

IFHA, TNER, OSER and first-hop invalid rate use all twenty questions. NPR/NRR/CCS/SCS/S0 use the common complete set of traceable natural errors with all four lookups correct. CWP uses all complete direct-correct valid cases, with W0 aliases deduplicated in actual call counts. A STATE_CAUSAL_SWITCH requires N0 to return the natural wrong candidate's target and C0 to return the gold target for that same error. Other candidate targets, out-of-universe values, refusals and invalid answers remain separate; no outcome is silently reassigned to the nearest target. Missing denominators yield null, not zero.

Gate: CLA ≥95%; ≥15/20 valid in-set first hops and complete branch cases; ≥5 traceable natural errors; OSER ≤25%; invalid downstream output ≤10%; exact permitted replay and fresh-call isolation; immutable candidate mappings. No NPR minimum. On early stop, unmeasured checks remain null and the gate fails. This experiment's mandatory natural-error yield differs deliberately from v3.3.

Inspect the smoke and answer all nine diagnosis questions. Stop at twenty cases. A 50–100-case pilot or redesigned universe needs a subsequent user request; do not scale automatically, integrate SHARS/HalluSE, change model or push GitHub as part of this run.
