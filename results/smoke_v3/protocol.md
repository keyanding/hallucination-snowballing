# v3 Track A smoke protocol — fixed before model execution

## Scope and fixed inputs

Run ten synthetic pairs with seed 42: four birthplace, three death-place, three father relations. Save the generated dataset before inference and never replace failures. Names come from fixed pronounceable nonce-name pools, not model generation. Full entity/target strings do not repeat across samples. Inspect for obvious public-figure/place resemblance; this screening cannot prove absence from model pretraining.

Preparation-only validation rejected the initial pair Kirva Ravdek / Tivra Dalvek as too visually similar. Before saving the fixed dataset or invoking the model, the surname pool entry Dalvek was changed to Moshun. No model output informed this change.

Use cached Qwen3-4B-Instruct-2507 revision `cdbee75f17c01a7cc42f958dc650907174af0554`, NF4/BF16, seed 42, greedy decoding, thinking disabled and at most 32 new tokens. HF receives `temperature=None` because temperature sampling is disabled by `do_sample=False` (the conceptual deterministic temperature is zero). Each call tokenizes a fresh single-user message; no prior messages or outputs are passed and `use_cache=False` disables KV caching even inside generation.

## Call matrix and matching

There are 80 calls: ten pairs × two evidence orders × four conditions (`direct_B`, `direct_B_prime`, `state_B`, `state_B_prime`). Run all 40 direct probes first, then all 40 state probes. Within each phase, order 1 precedes order 2; within each case B precedes B′. Every call is independent. The two facts are the entire context; no first-hop question, claim that B is correct, or original 2Wiki information is supplied.

The reference block and question in paired state prompts are byte-identical. Only the state field changes. Reversing evidence order changes only the fact block, not the state or question. Direct probes use the same reference block and explicitly name the queried person without mentioning a current state. These existing calls also serve as context-stability controls A and B; do not duplicate them.

All state probes run for diagnostic completeness, including cases failing lookup. Only cases passing both direct lookups in both evidence orders (four exact results) enter primary state/outcome metrics. Per-record `gate_pass` means that call's exact expected-answer check, not case eligibility; case eligibility is recorded separately in metrics.

## Parsing and outcomes

Keep raw output and exact prompt. Strip surrounding whitespace; matching uses Unicode NFKC, case folding, collapsed spaces and a trailing period. Do not extract answers from prose or strip output labels. A short answer is a single line, at most eight words / 100 characters, without markup, placeholders, labels, relation arrows or obvious explanatory clauses. Refusals and empty answers are UNKNOWN_REJECT, separate from INVALID_OUTPUT. Truncated outputs are invalid.

The synthetic closed-world answer vocabulary is exactly C and C′. A parseable non-refusal answer outside this set is OUT_OF_CONTEXT_HALLUCINATION, an operational closed-world label rather than a judgment of real-world falsity. C′ under B′ is PROPAGATE; C under B′ is OVERRIDE_TO_GOLD, not factual recovery. Formatting and unknown/reject outcomes remain separate.

## Denominators

CLA-all is exact direct lookups divided by all 40 direct calls and is the capability gate. CLA-eligible is also reported, but is necessarily 1 by selection. SAR-base and SAR-injected each have two observations per eligible case. PR equals SAR-injected. Outcome rates use all eligible injected calls as denominator, including invalid/refusal counts as separate categories. OHR additionally reports its rate conditional on valid non-refusal answers; neither refusals nor malformed outputs enter its numerator. Rates are null when the denominator is zero.

Evidence orders are repeated observations of the same ten cases, not independent samples. Report counts and denominators, without population claims or significance tests.

## Pre-run gate interpretation

The spec gives numerical thresholds for lookup, baseline accuracy and interpretable cases, but uses qualitative terms for order/material formatting/interference. Operationalize them before seeing outcomes:

- Direct accuracy at least 90% across all 40 probes.
- State-baseline accuracy at least 90% both across all 20 baseline probes and across eligible baseline probes.
- Evidence-order disagreement at most 10% for each of the four conditions (at most one of ten cases for each condition).
- At least eight cases are fully interpretable: all four direct probes pass, all state outputs have valid short-answer/refusal structure, and each of the four conditions is stable across orders. This does not require PROPAGATE or a specific injected answer.
- Invalid output rate at most 5% across 80 calls; zero copied placeholders/instruction strings.
- Baseline direct-correct/state-wrong rate at most 10% among eligible baseline calls.
- Non-target/invalid/refusal state failures at most 10% among all eligible state calls.

Flag every direct-correct/state-wrong comparison as STATE_FRAME_INTERFERENCE, including an injected override. To respect the spec's explicit instruction not to require a particular propagation rate, a stable exact C response under B′ remains an allowed OVERRIDE_TO_GOLD outcome, not automatic structural gate failure. Such flags must be inspected and cannot be described as factual recovery. The structural interference threshold concerns baseline failures and non-target/invalid/refusal state failures. This is an explicit operational distinction, not an inference about internal mechanisms.

The quantitative gate does not authorize further execution. After reviewing all prompts and outputs, stop for human review as requested in specification §24 step 11. Do not run the 30–50-pair pilot or real-entity Track B in this turn. Do not integrate SHARS/HalluSE.

## Preservation

Hash all prior v1/v2/v2.1 artifacts before inference and verify them afterwards. Refuse to overwrite an existing prepared directory or an existing run. Save runtime failures rather than silently retrying or replacing cases. Record model, source, dataset and prompt/raw-output hashes.
