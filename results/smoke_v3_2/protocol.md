# v3.2 frozen pre-inference protocol

## Design resolution approved by the user

The specification describes C4 as equivalent to old H3, which contained the old H2 sentence, while also asking for matched blocks changing only one added context. The user selected the common-H1-backbone design in this conversation. Accordingly:

- C0 and C1 exactly reuse the v3.1 H0/H1 prompts, including question and instruction.
- C2–C6 all use the identical H1 backbone, without the old H2 sentence.
- C4 contains the original first-hop evidence text unchanged, under the common `Task context` heading. It is a test of the same gold-evidence ingredient, not a verbatim replication of old H3. Old H3 outcomes are available for descriptive comparison, not a perfectly matched replication claim.
- C5 changes only the single B occurrence in that sentence to B′. It is counterfactual task context, not a corrected real-world dataset fact. C6a and C6b contain exactly these two sentences separated by a newline, in opposite orders.

C7 is omitted: inserting a third intermediate without its downstream fact would introduce a missing-evidence confound.

## Fixed cases and prompt matching

Reuse `data/candidates_v3_1.jsonl` byte-for-byte (ten cases; hash `74713eafdf4864bea3e9f1b2afcf2986b3271df26e36e102712837608bbdb191`). No alias, supporting fact, downstream reference or case change is permitted. Keep the original five/five downstream order balance fixed within each case. Only the ablation block changes between C2–C6; only the current-state field changes between paired state branches. Direct controls use identical context and explicitly name the person. All four call types are run for each condition.

The pre-inference audit includes every added block and all 320 complete prompts. Tests verify that removing the added block recovers the exact H1 prompt, that C0/C1 match the earlier templates exactly, and that swapping the state field leaves the rest identical. The two conflicting first-hop statements in C6 use identical wording except for the person name; C6a/C6b have the same total token count for all ten cases.

## Token-length controls

Use the locally cached tokenizer for the exact model revision, without generation. C2 is a sentence describing ordinary objects (paper, box, notebook, envelope, etc.), with no geographic, film, family or first-hop relation terms. C3 uses the same mundane vocabulary while mentioning B as a name, without A, B′, C, C′ or an A→B assertion. Neither condition contains real biographical assertions about B.

Select from a deterministic bank of grammatical sentences solely by closeness to the original first-hop evidence's tokenizer length, then by character length and lexical order. No model output is involved. Both C2 and C3 must be within two tokens of C4; the frozen actual plan is within one token for every case. Full-prompt token counts are also saved. C4/C5 can differ in token count because B and B′ tokenize differently (−4 to +4 tokens in this set); no unrelated padding is added to obscure that intervention.

These are approximate length/content controls, not identical-token semantics. C3 replaces some mundane vocabulary with the name. C4 introduces the original A→B statement plus any film metadata present in that original sentence (year, country, cast, etc.). Thus the C4−C3 contrast concerns an explicit evidence block versus a matched lexical cue; it cannot isolate the relation predicate alone from all other contents of that evidence sentence. This limitation is fixed and reported rather than concealed.

## Runtime

Same Qwen3-4B-Instruct-2507 revision, NF4/BF16, greedy decoding, thinking disabled and 32-token cap as v3/v3.1. HF receives `temperature=None` with `do_sample=False`, so temperature sampling is disabled. Reuse the tested independent adapter: fresh single-user input, no conversation carryover and `use_cache=False`. Call order is C0, C1, C2, C3, C4, C5, C6a, C6b. Within each condition run all direct B, direct B′, state B, state B′ calls. Maximum 320 calls; no reruns or expanded sample.

## Measures and review

Reuse the established short-answer parser and frozen complete aliases. Report combined and separate CLA, GSA, PR, OR, SFIR by branch and secondary injected outcomes. All completed conditions use the same ten cases: CLA combined n=20; GSA/PR/OR n=10. SFIR conditions on successful direct lookup. Retain control failures in denominators. Missing conditions and contrasts are null/unavailable, not zero.

Primary contrasts are PR(C2)−PR(C1), PR(C3)−PR(C2), PR(C4)−PR(C3), and PR(C5)−PR(C4). C6a/C6b are paired within case. C6a's last claim supports B′; C6b's last claim supports B. Opposite outcome patterns can be described as consistent with recency/primacy, without inferring internal reasoning. Unsupported real-entity mismatches remain provisional pending evidence/context review; alias lists will not be expanded silently.

## Gate and stopping policy fixed before inference

The measurement gate requires CLA ≥90% and GSA ≥90% in every condition; invalid outputs ≤5%; at least eight cases interpretable across C0–C5; no systematic unsupported-output or placeholder collapse. An interpretable case has exact direct and gold-state controls throughout C0–C5, parseable alternative-state answers and no unresolved semantic review. No PR/OR threshold is imposed.

Operationalize the qualitative stop conditions as follows:

- CLA below 90% in a completed condition stops further conditions.
- GSA below 90% in two distinct completed conditions constitutes the specified multiple-condition collapse and stops further conditions. A single below-threshold condition already fails the final GSA gate, even if execution continues for remaining contrasts.
- More than 20% provisional unsupported answers among a condition's twenty state calls stops for inspection.
- More than 5% invalid outputs overall or any placeholder copies fails the measurement gate; no prompt modification or rerun is performed.

C6 may legitimately have order-dependent or uncertain alternative-state outcomes. These are reported rather than used as a requirement for high PR. The specification's explicit CLA/GSA controls still apply to C6; do not waive them after observing a useful effect. If early stopping leaves a contrast unavailable, report that limitation instead of continuing silently.

## Preservation and endpoint

The candidate file, source code, context plan, audit and policy are hashed before inference. All v1/v2/v2.1/v3/v3.1 artifacts are hashed and rechecked. A prepared directory or existing model run cannot be overwritten. Save any failures/partial run. Stop after this ablation and review; no natural trajectory branching or SHARS/HalluSE integration follows automatically.
