# v3.3 frozen protocol

## Scope and cases

Twelve 2Wiki cases: retain the previous ten, regardless of their previous outcomes, and add The Ride (1994 film) / Jan Svěrák / father Zdeněk Svěrák, plus The Amorous Ones / Walter Hugo Khouri / death in São Paulo. The new support sentences explicitly identify the director and father, or the birth–death biographical place/date pair. Both new cases use previously reviewed, plausible director donors (Rahul Rawail and Bhappi Sonie). Four cases per downstream relation; donor reuse is disclosed, so the twelve cases are not fully independent entity samples. Earlier experiment results were already known; none of these cases were selected or replaced using v3.3 model outputs.

Use the exact cached Qwen3-4B-Instruct-2507 revision and NF4/BF16 GPU settings from v3–v3.2, greedy, 32 new tokens, thinking disabled. No new download, model family, SHARS/HalluSE, or expanded pilot. Preserve every earlier result file. All old code is reused unchanged; v3.3 has separate source and results.

## Natural checkpoint and downstream evidence

Phase A presents the original question plus a first-hop-only instruction with no first-hop or downstream evidence. The raw first-hop answer is saved exactly, with its actual chat-rendered prompt. The branch checkpoint is the same user prompt and assistant response including chat delimiters. Verify that its beginning exactly equals the Phase-A rendered prompt plus raw answer.

Every downstream call explicitly serializes that checkpoint into a fresh conversation and appends one continuation user message. No prior branch responses, retained messages, or KV cache enter a new call. Replay the text checkpoint rather than a hidden-state snapshot. Gold/wrong replacements change only the trimmed assistant answer span; any surrounding whitespace and all earlier prompt text remain unchanged. No extra explanation is generated or invented before the branch point.

All continuations receive the same two explicit downstream reference facts after the checkpoint. E0 has no added *first-hop* evidence; the downstream block is still present. Thus B0 measures evidence-assisted continuation from a naturally produced first hop, not an uninterrupted closed-book natural two-hop run. This choice implements the spec's shared downstream evidence/CLA/S0 controls while avoiding the known recall confound; report this limit on NPR.

E1 is the source-grounded simple sentence `"A" was directed by B.` E2 changes only the director name to the active wrong state. E3a/E3b concatenate those same sentences in opposite orders, with identical formatting. Counterfactual status is logged, never announced to the model. Across gold/wrong branches of a case, keep the downstream block, user continuation and evidence identical. Alternating reference order is fixed by case. No outcome-dependent wording changes.

## Eligibility and provenance

Freeze a lookup index of named entities, relation triples and exact supporting sentence coordinates from the existing frozen dev.json before Phase A. The index is a set of evidence candidates, not a verified relation database: target-string occurrence alone does not prove that sentence supports the relation. After Phase A, inspect any selected natural entity's identity, single-valued target, explicit support and granularity before permitting its use. Store the exact reviewed entry and source hash. Do not use web lookup or facts invented after generation.

The user explicitly approved case-level stopping: if a natural wrong state's downstream evidence is unavailable or ambiguous, stop that case's natural branch and record why. A clean, parseable first-hop answer can still be replaced with its pre-registered alternative for a separately identified counterfactual analysis. Do not count this fallback as a natural error propagation observation. Unknown/refusal/malformed prefixes are not assigned an entity span and receive no downstream branches. No replacement cases or first-hop retries.

All Phase-A classifications are preserved. An unrecognized non-gold name is provisionally OTHER_WRONG_ENTITY, with identity verification separately recorded; do not claim it is a valid real entity solely because the string parses. NFER is the non-correct first-hop rate over all twelve (includes unknown/invalid), reported alongside verified wrong-entity rate and unknown/invalid fraction. NPR uses only reviewed, distinct-target natural wrong states whose two direct lookups pass. No minimum natural-error yield.

## Execution and denominators

After reviewing Phase A, run the two independent direct lookups for every executable case before any branch. Stop globally if combined CLA is below 90%; a case failing either lookup is excluded from clean propagation analysis and is not silently replaced. Cases passing controls receive ten branch calls (gold/wrong × E0/E1/E2/E3a/E3b) plus wrong-state S0. S0 contains only downstream facts and the supplied state, with no natural transcript. The prefix comparison also includes the intended transcript/role framing difference, so it is not an isolated single-word effect.

B1 and B2 are logical names for gold/E0 and wrong/E0 (and their evidence extensions). B0 reuses an E0 call if the raw natural assistant response is byte-identical to that branch; otherwise perform one additional exact-natural-prefix E0 call. Deduplication is by exact prompt identity and is logged in logical_branches. At most 180 calls: twelve first hops plus twelve × (two controls + eleven branches + one possible extra B0). Normal exact-answer execution is 168 calls. Do not treat duplicated logical labels as independent observations.

CPR/OR/GSA and S0 use the common set of fully executed, direct-correct cases; report natural-wrong and registered-counterfactual strata separately. NPR uses natural-error B0 only. Missing measurements are null, never zero. Keep all first hops, exclusions and raw controls. A low GSA under E2 is a symmetry outcome, not an automatic validity failure.

## Gate and stop rules

Gate: combined CLA ≥90%; at least eight of twelve cases have a complete branch matrix with verified prefixes and no unsupported/invalid outputs; unsupported/invalid rate ≤10% among downstream state calls; verified exact allowed prefix changes; and independent fresh calls. UNKNOWN/REJECT is reported separately and does not count as an unsupported factual answer. Unresolved semantic mismatches require review before a final scientific gate decision.

Operational stop rules: natural-format invalidity above 25% of the twelve stops before downstream inference; direct CLA below 90% stops all branches; any illegal prefix change or unmatched evidence construction stops immediately; unsupported/invalid outputs above 50% of accumulated state calls stops after the current case. A missing natural mapping stops only that natural branch under the user's explicit resolution. No post-output prompt repair or relaxed gate.

For support diagnostics, a pair where both responses select the uniquely supported target under E1/E2 is STATE_SELECTIVE, including mirror effects. Both branches producing unsupported/invalid/unknown responses is GENERAL_INTERFERENCE; one unstable branch is unresolved interference. Stable state following and other supported selection are reported separately rather than forced into an unsupported binary interpretation. Report case counts, not an inferred cognitive mechanism.

## Review endpoint

Append Phase-A answers, reviewed eligibility and provenance to branch_audit.md while preserving branch_audit.pre_inference.md byte-for-byte. Save complete chat-rendered branch prompts, outputs, raw/checkpoint hashes, logical branch identities and classifications. Answer all nine diagnosis questions. Do not infer universal or population rates from twelve selected questions or claim natural propagation if no eligible natural error exists. Stop after the smoke analysis and human-review-ready artifacts; no automatic commit/push or follow-up experiment.
