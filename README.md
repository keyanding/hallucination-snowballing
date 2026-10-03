# Hallucination snowballing pilot

Standalone research project staged inside the existing checkout. Original SHARS source files are not modified or copied. Move this directory elsewhere and supply `--shar-repo` to keep running it independently.

## Current experiment: v3.4.2 factorial graph calibration

V3.4.2 completed **8 base cases × 4 depths × 3 branch counts × 3 channels = 288 channel evaluations** (96 paired prompts). Twenty anonymous synthetic Film targets were frozen: eight development and twelve held-out, with gold positions balanced 2/slot and 3/slot. Each target has four real candidate directors and audited, distinct downstream targets. Candidate bundles are sampled from the prior frozen datasets without consulting model outputs; graph node IDs and target questions are new. Entities may recur across splits.

The credited-director path has one to four links. Zero, one, or two equally long comparison-director/associated-director paths terminate at other registered candidates. Candidate records, order, vocabulary, question, chat template, and answer contract stay fixed within each base case. The existing F/C/L adapter is reused unchanged: free greedy generation (96 tokens), exact constrained choice, and teacher-forced candidate likelihood. The preregistered near-boundary threshold is **absolute gold margin ≤0.75 nats/token**.

| Depth | Branch 0 errors | Branch 1 errors | Branch 2 errors |
|---|---|---|---|
| 1 | 3/8 | 3/8 | 3/8 |
| 2 | 2/8 | 2/8 | 4/8 |
| 3 | 3/8 | 4/8 | 4/8 |
| 4 | 3/8 | 4/8 | 3/8 |

**Gate failed on the preregistered position-bias exclusion.** D3B0 and D4B2 meet the other development criteria, but candidate position 1 is selected **54/96** times and contains **34/38** wrong selections. Two always-wrong base cases contribute 24 of the 38 errors. Fixed within-case order prevents separating index preference from candidate identity or case effects; this is a descriptive exclusion flag, not a causal position-effect finding. No condition was promoted, so all twelve held-out targets remain unqueried and v3.5 is not authorized.

The gold median margin decreases in **7/9** adjacent depth comparisons and **7/8** adjacent branch comparisons; error rates are non-decreasing in **6/9** and **7/8**, respectively. This is partial ordering with recoveries, not a globally monotonic difficulty axis. C validity, free strict compliance, and F/C agreement are 96/96; L/C agreement is 95/96. No downstream continuation was run.

See [diagnosis](results/calibration_v3_4_2/diagnosis.md), [inspection](results/calibration_v3_4_2/inspection.md), [position audit](results/calibration_v3_4_2/position_audit.md), [frontier selection](results/calibration_v3_4_2/frontier_selection.md), and [development grid](results/calibration_v3_4_2/development_grid.png).

```powershell
# Fresh output directory only; refuses overwrite/retries.
$env:HF_HUB_OFFLINE='1'
python -m unittest discover -s tests
python -m src.calibration_v3_4_2 prepare
python -m src.calibration_v3_4_2 run
# Verification and presentation only; no model calls:
python -m src.calibration_v3_4_2 verify
python scripts/plot_calibration_v3_4_2.py
python scripts/present_calibration_v3_4_2.py
```

All **64 tests** passed. Pre-inference checks covered all **240 possible graph/tokenizer renderings** and **80 candidate mappings**. Post-run verification checks every prompt, token path, likelihood sum/mean/rank, frozen selection, and all **191 prior artifact hashes**. No previous experiment was rewritten. Plotting and the observed-position presentation are separate post-run steps; the frozen inference and selection code remains unchanged.

## Previous experiment: v3.4.1 first-hop calibration

V3.4.1 completed **96 development prompts × three channels = 288 channel evaluations**, using the cached Qwen3-4B-Instruct-2507 NF4/BF16 model. Twenty-four development films (six per mechanism) and twelve disjoint held-out films were frozen before inference. Four real candidate directors and their downstream mappings remain fixed per case. Task-local catalog links implement relation competition, shared-attribute salience, evidence order, and one-to-three-step composition. Those index links are explicit experimental constructs; sourced film credits remain factual.

F uses greedy free generation with 96 tokens; C uses an exact candidate-token trie; L teacher-forces each candidate on the identical rendered prompt and reports both sum and mean/token log probability. Candidate reachability and prompt/token boundaries were checked on all 288 possible dev/held-out renderings before inference. The user-approved M2 design keeps candidates fixed and increases shared era/genre salience. Each qualifying mechanism would use all twelve held-out cases once.

| Mechanism | D0 wrong | D1 wrong | D2 wrong | D3 wrong |
|---|---|---|---|---|
| M1 relation competition | 0/6 | 0/6 | 1/6 | 0/6 |
| M2 shared-attribute salience | 0/6 | 0/6 | 0/6 | 0/6 |
| M3 evidence order | 0/6 | 0/6 | 0/6 | 0/6 |
| M4 composition length | 1/6 | 0/6 | 0/6 | 2/6 |

**Gate failed.** M4/D3 reaches the 20–40% error-rate band, but only **0/6** cases meet the preregistered likelihood-boundary criterion (absolute gold-vs-best-wrong mean margin ≤0.5 nats/token; at least 4/6 required). No regime qualifies for held-out confirmation; all twelve held-out cases remain unqueried. No downstream branches were run and no v3.5 experiment is authorized. Free strict compliance, F/C agreement, and L/C agreement are all 96/96. No position-bias flag fired under the preregistered rule. Structural uniqueness was checked; independent human ambiguity certification is not claimed.

See [diagnosis](results/calibration_v3_4_1/diagnosis.md), [per-case inspection](results/calibration_v3_4_1/inspection.md), [design audit](results/calibration_v3_4_1/design_audit.md), and [frontier selection](results/calibration_v3_4_1/frontier_selection.md). Six cases per family provide a coarse calibration grid; index traversal, coarse era bands, and entity reuse limit generalization. The format improvement over v3.4 cannot be attributed solely to the token cap because prompts also changed.

```powershell
# Fresh output directory only; preparation and inference refuse overwrite.
python -m src.prepare_v3_4_1
$env:HF_HUB_OFFLINE='1'
python -m src.calibration_v3_4_1 prepare
python -m unittest discover -s tests
python -m src.calibration_v3_4_1 run
# Recompute and verify recorded outputs without model calls:
python -m src.verify_calibration_v3_4_1
```

The independent verifier checks prompt equality, candidate token paths, likelihood arithmetic, all 144 candidate-to-target source mappings, and 167 prior artifact hashes. All 56 unit tests passed. A pre-inference preparation draft is retained separately: source review removed a spurious genre match from a trilogy title before the final split was frozen; no model outputs informed that revision. The inference-source byte hashes are preserved through Git attributes. No existing experiment artifacts were rewritten.

## Previous experiment: v3.4 traceable candidate-universe selection

V3.4 freezes twenty real film questions with four director candidates each. Every candidate has an explicit, previously reviewed downstream fact; all four target values and their aliases are distinct within a case. A shared-director link plus four bridge-film/director facts makes the first hop a composition task without directly stating the target film's director. Alternatives have documented films within thirty years of the target film, and gold positions are balanced five per slot. The twenty questions share eight gold directors and are not independent entity samples.

Phase A generates a candidate name naturally and saves its exact chat checkpoint. Only exact listed names qualify; out-of-set answers are preserved. If fewer than five traceable natural errors occur, execution stops before downstream calls and reports NPR/CLA as unmeasured. Otherwise eighty direct lookups precede N0 (natural state), C0 (gold replacement), W0 (natural wrong or registered wrong state), plus S0 for eligible natural errors. All branches share four explicit downstream facts, and only the assistant answer span changes. Identical logical branches reuse one actual call.

```powershell
python -m src.prepare_v3_4
python -m src.experiment_v3_4 prepare
# Inspect candidate_audit.md and record its hash-bound audit_review.json.
python -m unittest discover -s tests -v
$env:HF_HUB_OFFLINE='1'
python -m src.experiment_v3_4 run
```

Preparation and execution refuse overwrite. See [candidate audit](results/smoke_v3_4/candidate_audit.md), [protocol](results/smoke_v3_4/protocol.md), [inspection](results/smoke_v3_4/inspection.md) and [diagnosis](results/smoke_v3_4/diagnosis.md). The smoke requires CLA ≥95%, at least fifteen valid cases, at least five traceable natural errors, OSER ≤25%, low invalid output and verified replay/isolation. A low NPR does not itself fail the gate. No post-output candidate replacement, richer evidence ablation, new model or automatic pilot is included.

Actual v3.4 outcome: execution **stopped after 20 first-hop calls**. There were **11 correct, 0 traceable wrong, 0 parseable out-of-set and 9 invalid outputs**; every invalid output was an explanation truncated at the fixed 32-token limit. The gate fails both valid-first-hop count (11/20, required ≥15) and traceable error yield (0/20, required ≥5). No lookup or downstream branch was run; **CLA/NPR/NRR/CCS/CWP/SCS remain null**, and the branch log is intentionally empty. No name extraction, retry or candidate replacement was used to rescue the result. All 52 tests passed and 145 prior artifacts retained their hashes. See the diagnosis for the separate format-reliability and error-yield limitations.

## Previous experiment: v3.3 natural first-hop checkpoints

V3.3 freezes twelve real 2Wiki questions (the previous ten plus two evidence-reviewed additions; four per downstream relation). Phase A asks for the first-hop name without evidence and saves the exact model output and chat-rendered checkpoint. Every downstream call starts fresh, explicitly replays that checkpoint, and changes only the assistant answer span and/or the added first-hop evidence. No hidden-state snapshot or cross-call KV cache is reused. All downstream branches receive a shared pair of reference facts after the checkpoint, so this measures evidence-assisted continuation rather than unrestricted closed-book two-hop generation.

Gold and wrong states are crossed with E0 (no first-hop evidence), E1 (gold support), E2 (matched wrong support), E3a/E3b (both claims in opposite orders). S0 strips the natural task transcript and retains just facts plus state. Two independent direct lookups precede each case's branch matrix. Exact duplicate B0/B1/B2 logical branches reuse one model call. Natural-error eligibility requires a distinct downstream target, explicit frozen-source evidence and successful lookup controls. Per the user's approved case-level stop rule, unavailable natural mappings are preserved as exclusions while registered counterfactual branches may proceed separately; they never enter NPR.

```powershell
python -m src.prepare_v3_3
python -m src.experiment_v3_3 prepare
# Review branch_audit.pre_inference.md and save hash-bound audit_review.json.
python -m unittest discover -s tests -v
$env:HF_HUB_OFFLINE='1'
python -m src.experiment_v3_3 phase-a
# Review natural entities against frozen evidence; save eligibility_review.json.
python -m src.experiment_v3_3 phase-b
python -m results.smoke_v3_3.verify_artifacts
```

Preparation and phases refuse overwrite. See [protocol](results/smoke_v3_3/protocol.md), [branch audit](results/smoke_v3_3/branch_audit.md), [inspection](results/smoke_v3_3/inspection.md) and [diagnosis](results/smoke_v3_3/diagnosis.md). The gate checks lookup, valid execution, unsupported outputs, exact matched prefixes and isolation. It does not require high propagation, high gold-state adherence under competing evidence, or a minimum number of natural errors. Evidence-driven mirror effects are reported separately from unsupported general interference.

Actual v3.3 result: **168 calls** (12 natural first hops, 24 lookups, 132 counterfactual probes). All twelve first-hop answers were non-gold; none had eligible explicit downstream evidence in the frozen source, so **NPR is unavailable (n=0)** and no natural B0 was run. Counterfactual CPR across E0/E1/E2/E3a/E3b is **11/12, 0/12, 12/12, 4/12, 12/12**; S0 is 12/12. Direct lookup is 24/24 and all state outputs are supported targets. Gold support overrides 12/12 wrong branches; wrong support overrides 11/12 gold branches. Conflict order changes eight wrong-state pairs, consistent with a first-sentence tendency on those cases. The counterfactual measurement gate passes, but the natural-propagation objective remains unmeasured. All 46 tests passed and 116 prior artifacts retain their hashes. See the diagnosis for denominators, exclusions and scope limits.

## Previous experiment: v3.2 contextual evidence ablation

V3.2 freezes all ten v3.1 cases, aliases, reference facts and evidence orders. C0/C1 reuse H0/H1 verbatim. With the user's approved design, C2–C6 share the H1 backbone and omit the old H2 sentence: C2 adds length-matched mundane context, C3 mentions only the gold intermediate, C4 adds original first-hop evidence, C5 substitutes the alternative intermediate in that same evidence, and C6a/C6b present both claims in opposite orders. C4 is therefore not a verbatim H3 replication. Optional C7 is omitted because a third entity would lack a matched downstream fact.

Each condition has two direct lookups and two state-framed probes per case, with at most 320 independent calls. The pre-inference plan uses the cached model's tokenizer: C2/C3 are within one token of C4 for every case. The original C4 evidence retains its film metadata; its contrast with C3 is an evidence-block contrast, not a perfectly isolated relation-predicate effect.

```powershell
python -m src.experiment_v3_2 prepare
# Inspect context_ablation_audit.md and save its hash-bound audit_review.json.
python -m unittest discover -s tests -v
$env:HF_HUB_OFFLINE='1'
python -m src.experiment_v3_2 run
```

These commands refuse to overwrite the recorded preparation or run. See [pre-inference audit](results/smoke_v3_2/context_ablation_audit.md), [protocol](results/smoke_v3_2/protocol.md), and [full inspection](results/smoke_v3_2/inspection.md). Direct lookup below 90%, gold-state adherence below 90% in multiple conditions, or unsupported-output collapse stops further conditions. Missing comparisons remain unavailable. No prompts, aliases or cases are revised after observing outputs. The final gate additionally requires at least eight interpretable cases across C0–C5 and gold-state adherence of at least 90% in every condition; it imposes no propagation-rate threshold.

Actual v3.2 result: all **320 calls** completed. PR across C0/C1/C2/C3/C4/C5/C6a/C6b is **100%, 100%, 100%, 80%, 40%, 100%, 100%, 100%**; direct lookup is 20/20 in every condition. C5 gold-state adherence falls to **4/10** (C2: 9/10; all others: 10/10), leaving only **4/10** cross-C0–C5 interpretable cases. The measurement gate therefore **fails**. Both conflict orders follow the supplied state with no observed order-sensitive answers. These are descriptive controlled-context results, not a fully validated assay or evidence of naturally generated hallucinations. See [diagnosis](results/smoke_v3_2/diagnosis.md) and [verification](results/smoke_v3_2/verification.json). All 42 tests passed and 95 prior artifacts retained their hashes; work ends at this review.

## Previous experiment: v3.1 real-entity context ladder

V3.1 uses ten fixed, evidence-reviewed real 2Wiki cases (four birthplace, three death-place, three father relations), each with twenty distinct intermediate people across the gold/donor branches in total. All first hops identify a single film director. The downstream facts are supplied explicitly; the model is not required to recall them. Candidate selection, aliases, source sentence indices and hashes live in `data/candidates_v3_1.jsonl` and its manifest.

Each case receives four cumulative contexts: H0 has just two downstream facts; H1 adds the original task; H2 adds one neutral sentence from the exact original film article; H3 adds its explicit first-hop evidence. Within each level, paired state prompts differ only in the supplied entity. Two direct context-lookup controls and two state-framed probes give 160 planned independent calls. Reference order is balanced five/five across cases and fixed within each case across levels. This version reuses v3's isolation-tested NF4 adapter and short-answer parser.

```powershell
python -m src.prepare_v3_1
python -m src.experiment_v3_1 prepare
# Inspect context_audit.md and save its hash-bound audit_review.json before inference.
python -m unittest discover -s tests -v
$env:HF_HUB_OFFLINE='1'
python -m src.experiment_v3_1 run
```

Preparation and execution refuse overwrite of the recorded run. See [context audit](results/smoke_v3_1/context_audit.md) and [pre-run protocol](results/smoke_v3_1/protocol.md). The audit catches partial-name leaks and neutral sentences mistakenly drawn from a same-title remake. The cumulative context blocks, paired prompt identity, thresholds and aliases are fixed before generation. Calibration collapse at H0–H2 stops progression; failed cases are never replaced.

Metrics retain the same ten-case denominator across levels: separate and combined CLA, GSA, PR, OR, conditional SFIR by entity, ΔPR from H0, and secondary outcomes. H3 OVERRIDE_TO_GOLD is a meaningful response to conflicting first-hop evidence and does not fail the assay. Real-entity answer mismatches remain provisional until inspected. The experiment ends after inspection/diagnosis; no natural-trajectory branching, model-family comparison or SHARS/HalluSE integration is included.

Actual v3.1 result: **PR = 100%, 100%, 90%, 20%** across H0–H3; OR = 0%, 0%, 10%, 80%. Direct lookup remains **20/20 at every level**. Gold-state adherence is 10/10, 10/10, 9/10, 10/10; the H2 gold-state failure is retained and documented. The smoke gate passes with nine cross-H0–H2 interpretable cases. See [full inspection](results/smoke_v3_1/inspection.md) and [reviewed diagnosis](results/smoke_v3_1/diagnosis.md). No next experiment is automatically launched.

## Previous experiment: v3 controlled-context synthetic assay

V3 removes closed-book recall from the downstream task. Ten fixed synthetic pairs (seed 42; four birthplace, three death-place, three father) each contain exactly two symmetrical reference facts. The state-framed baseline and injected prompts differ only in the supplied state field. Both evidence orders are tested, and two direct lookups per order establish context capability. The complete smoke comprises 80 independent calls with the same cached Qwen3-4B NF4 model, greedy decoding, a 32-token cap and KV caching explicitly disabled. No full original question or first-hop evidence reaches the model.

`src.experiment_v3` saves and validates the fixed cases before inference, refuses overwrite, and checks preservation of prior results. A pre-run name review must bind to the saved dataset hash. The direct calls also serve as minimal-lookup controls, and the state calls as framing controls; no extra duplicate calls are needed. Case eligibility requires exact direct answers for both entities in both orders. All state probes run for diagnosis, but only eligible cases enter primary outcome metrics.

```powershell
python -m unittest discover -s tests -v
python -m src.experiment_v3 prepare
# Inspect synthetic_cases.jsonl and save hash-bound name_review.json before inference.
$env:HF_HUB_OFFLINE='1'
python -m src.experiment_v3 run
```

These commands create a fresh run; the recorded `results/smoke_v3/` cannot be overwritten. See [the pre-run protocol](results/smoke_v3/protocol.md) for gate thresholds, name screening, outcome definitions and denominators. In this assay PROPAGATE means following an externally supplied state through provided facts; OVERRIDE_TO_GOLD means returning the other designated target and is not factual recovery. Neither result establishes that the intermediate error was spontaneously generated. The gate does not require a high propagation rate. Both orders are repeated observations of the same ten cases, not independent samples.

After the smoke, stop for human review. The 30–50-pair synthetic pilot and real-entity Track B are later stages, conditional on a valid setup and review. No SHARS/HalluSE integration is included.

Actual v3 Track A outcome: **40/40 direct lookups**, **20/20 baseline state answers**, and **20/20 injected state answers** were exact. All ten pairs passed; there were no evidence-order changes, state-frame failures, invalid outputs or refusals. The quantitative gate passes, with human review still required before scaling. See [full paired inspection](results/smoke_v3/inspection.md) and [reviewed interpretation](results/smoke_v3/diagnosis.md). This is controlled following of an externally set state, not evidence of spontaneous intermediate hallucination.

## Previous experiment: v2.1 natural-language prompt diagnosis

V2.1 reuses the exact five v2 candidates, model revision, NF4/BF16 adapter and greedy decoding. `src.experiment_v2_1` replaces operator wording with relation-specific questions, explicitly fixes the correct Oracle premise, and uses neutral continuation instructions for injection. Birth questions request a city/town; the death questions request a specific location so Lakshadweep is not incorrectly constrained to a city. The performer template uses "performed or recorded" to match the saved song evidence.

Outputs live exclusively in `results/smoke_v2_1/`. Existing v1/v2 artifacts are hash-checked for preservation, including the previous turn's format revalidation. The runner refuses any existing output directory and verifies the candidate file against the original v2 manifest. It runs five baseline, five Oracle and five independent donor calls, then injects only individual candidates passing all three exact gates. Fewer than three eligible candidates keeps propagation rates null and precludes propagation interpretation. Every run stops for human review; no scaling or SHARS integration is included.

Each record stores strict eligibility separately from downstream semantic labels, with per-field diagnoses for Step 1, Step 2 and the final answer. Explicit non-answers, copied input, invalid format, broader-compatible locations and mismatches are distinguished. `data/location_profiles_v2_1.json` contains a small evidence-linked containment map; no geographic containment is inferred from substring matching. Unmatched aliases/locations are provisional and require evidence review rather than being declared hallucinations. A correct city remains required for city-level eligibility even if the country is compatible. Syntax validation cannot establish that arbitrary prose is a valid entity or that an answer is true.

```powershell
$env:HF_HUB_OFFLINE='1'
python -m unittest discover -s tests -v
python -m src.experiment_v2_1
```

See the new inspection for exact prompts, raw responses, diagnoses and the paired comparison against saved v2 responses. The old prompts are not rerun. Prompt wording, explicit Oracle instructions and granularity guidance change together, so this small comparison cannot attribute any improvement to a single change.

Actual v2.1 result: baseline **0/5**, Oracle **1/5**, donor **1/5**, all-three eligibility **0/5**. No injection was run. Björk's Oracle birthplace and Gustaf Molander's donor birthplace improved to exact answers, but capability remains insufficient. Three outputs failed formatting, including two copied placeholders; no output was truncated. See [the reviewed diagnosis](results/smoke_v2_1/diagnosis.md) and [full inspection](results/smoke_v2_1/inspection.md). Ten provisional mismatches were confirmed against saved evidence in a separate hash-bound review log using `src.review_v2_1`; raw outputs remain unchanged. Work stops for human review.

## Previous experiment: v2 controlled composition

V1's semantic dependency gate failed. V2 explicitly assigns Step 1 to `r1(A)` and Step 2 to `r2(Step 1)`, using **Qwen/Qwen3-4B-Instruct-2507** through a local HF adapter. No original SHARS file is imported or modified by v2. No HalluSE, automatic rejection, or 0.6B fallback is used. Existing `results/smoke/` files are preserved byte-for-byte; v2 artifacts live in `results/smoke_v2/`.

The preparation command now defaults to v2 and only allows 3–5 examples. Candidates are explicitly compositional, exclude potentially multivalued relations and conflicting dataset objects, and include gold/donor triples, supporting sentences, and evidence-corroborated official aliases. Donors have identical r1/r2 and a biographical era anchor within 40 years. This heuristic does not prove geographic or historical plausibility; inspect the evidence. Recurrent intermediate entities are preferred before seeing model outputs to make this a knowledge-friendly capability pilot. This deliberately biased selection cannot estimate population performance.

V2 runs all baselines, then all oracle probes, then all donor probes. A pair is injected only if the model independently produces `B,C,C`, `C,C`, and `C'` respectively. Entity matching uses whole normalized names and saved aliases, never substrings. New unknown answers remain pending review rather than automatically becoming hallucinations. Use `src.review_v2` for explicit, output-hash-bound classifications; NEW_HALLUCINATION requires unsupportedness evidence and RECOVER records explicit/implicit mode. Raw generation logs remain immutable.

The primary metrics are PROPAGATE, RECOVER, NEW_HALLUCINATION, and REJECT_UNCERTAIN rates over all eligible injected trajectories, with INVALID_OUTPUT and pending counts reported separately. Zero eligible cases or pending classification reviews yield null rates; known category counts remain visible. Baseline/oracle/donor accuracies are eligibility diagnostics. A correct `C'` under an explicitly supplied false `B'` demonstrates controlled-state propagation, not spontaneous hallucination frequency.

### V2 execution

Use the existing Python environment; do not upgrade a working CUDA/PyTorch stack merely to run v2. Record package/GPU state before installation changes. The adapter uses the [official model's chat template](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507), greedy decoding, max_new_tokens=128, and thinking disabled.

```powershell
# First: one native load plus 8-token trivial generation, without an experiment.
python -m src.generation.local_hf_adapter --quantization native --cache-dir .cache/huggingface --output results/smoke_v2/load_native.json
# Only if native OOMs or lacks 1 GiB free headroom / uses CPU offload:
python -m pip install bitsandbytes
python -m src.generation.local_hf_adapter --quantization 4bit-nf4 --cache-dir .cache/huggingface --output results/smoke_v2/load_nf4.json
# Prepare only once the load test succeeds; use the successful JSON below.
python -m src.prepare --version v2 --n 5
python -m unittest discover -s tests -v
python -m src.experiment_v2 --load-test results/smoke_v2/load_nf4.json
```

For comfortable native inference, substitute `load_native.json` in the last command. NF4 first executes a CUDA quantization kernel, chooses BF16 only if supported, otherwise FP16, and logs dtype, device map, revision, and memory. Explicit `--quantization cpu-offload` is a last smoke-test fallback if NF4 compatibility cannot be resolved; never silently downgrade the model. Load-test errors and incomplete experiment failures are preserved. The CLI refuses to overwrite a prior trajectory file.

If standard downloading stalls, `python -m src.cache_model --source modelscope` can resume 1 MiB ranges from Qwen's official ModelScope mirror, verifying the completed files against Hugging Face's LFS SHA-256. Model/cache files are ignored by Git. This is optional transport recovery, not a change of model.

Inspect `results/smoke_v2/inspection.md`, `metrics.json`, and `gate.json`. At least three pairs must pass all pre-intervention gates and semantic inspection before the smoke gate can pass. The generated gate initially requires semantic review and always requires human review before scaling. This implementation intentionally accepts only 3–5 candidates; no 30–50 example v2 run is launched automatically. Failed gates are an identifiability/capability result, not evidence against propagation.

The sections below describe the preserved v1 experiment.

### Actual v2 smoke outcome

Qwen3-4B-Instruct-2507 (revision `cdbee75f17c01a7cc42f958dc650907174af0554`) ran in NF4/BF16 entirely on GPU. All three weight shards passed official SHA-256 checks. Native loading was tested once and automatically used CPU offload with insufficient free headroom, so NF4 was used. The actual experiment's peak reserved VRAM was approximately 3.29 GiB.

Five fixed candidates produced 15 baseline/oracle/donor probes. Each eligibility gate passed **0/5**; consequently **zero injected trajectories** were run and all mechanism rates are null. Parsed formatting did not imply semantic validity. Some responses were wrong entities, while Germany/Iceland answers were too coarse for the city targets and should not automatically be called false. The failed gate and detailed diagnosis are in [the v2 inspection](results/smoke_v2/inspection.md). Work stops here for human review, without scaling or adding SHARS.

Preparation was refined once before any model probes after detecting misleading support, state/city granularity ambiguity, and a donor too young at the work date. Both candidate lists and the refinement rationale are retained. No candidates were replaced after observing model outputs. Eleven unit tests and `pip check` passed; original smoke artifact hashes were preserved.

## Method

Question: does an incorrect intermediate fact propagate to the next reasoning step, and can correction interrupt it? Stage one compares natural generation, an injected parent-entity substitution, and **oracle correction** of that same injected fact. Oracle correction supplies the evidence-derived gold first step; it is not model resampling, automatic detection, or evidence of SHARS effectiveness. HalluSE scores remain null. No evidence or gold final answer is passed in prompts; oracle supplies only the first fact.

Source: [official 2WikiMultiHopQA repository](https://github.com/Alab-NII/2wikimultihop), April 7 2021 archive. `src.prepare` requires exactly two explicitly linked evidence triples terminating in the gold answer, valid supporting sentence references, and explicit intermediate/answer mentions. First-hop relations are restricted to father/mother to reduce multi-valued substitution ambiguity. Donors share the two relation types and have a different intermediate entity and final answer. This is a restricted genealogical pilot, not a representative dataset benchmark. Historical parentage and temporal plausibility still require inspection. Graph connectivity alone does not ensure the model uses that path; the smoke gate checks semantic dependency.

Forty examples are sampled without replacement with seed 42. Source SHA-256 and exclusions are retained in `data/pilot.manifest.json` and `data/flagged.jsonl`. Candidates are not automatically certified interventions. Do not confuse dataset preparation with completion of the 40-example experiment.

## SHARS inspection and reuse

Inspected commit: `b7fcf649d63d76dd57ec3242c14d7f1563ccac31`.

| Component | Original location | Integration |
|---|---|---|
| Model loading | `LLM.get_model`, `HFTransformer` | Imported read-only through local path |
| Generation and sampling | `LLM.complete`, `generation_configs` | Reused; T=.7, top-p=.8, top-k=20, max new tokens=192 |
| HalluSE | `uncertainty.SemanticUncertaintyEstimator`, `QADebertaEntailment` | Inspected; deferred until propagation is established |
| Rejection | `generator.is_prop_hallued`, `is_sentence_hallu` | Threshold plus optional entailment check; deferred |
| Resampling | `UncertaintyGenerator.generate`, `reset_cache` | Natural/following and decode policies; deferred |
| Logging | `main.py`, `utils.py`, WandB | New local JSONL logs avoid upstream runner's single-example break |

The upstream default system prompt prohibits reasoning, so this project uses its own two-step prompt through the reusable model interface. Original authors retain ownership of SHARS; no original implementation is copied here.

## Run

Python 3.11+, PyTorch compatible with your GPU, and the dependencies in `pyproject.toml` are required. From this directory, with a suitable Python environment:

```powershell
python -m pip install -e .
python -m src.download
python -m src.prepare --version v1 --n 40 --seed 42
python -m unittest discover -s tests
python -m src.run --shar-repo .. --n 3 --output results/smoke/trajectories.jsonl
python -m src.evaluate --input results/smoke/trajectories.jsonl --output results/smoke
```

This machine can reuse `../.venv/Scripts/python.exe` and the parent's HF/NLTK cache. Qwen3-0.6B is intentionally a small smoke-test model; lack of knowledge may make the proposed causal measurement uninformative. Run manifests record SHARS/model commits, data hash and sampling settings. Seeds match across conditions per sample; GPU execution may still be nondeterministic. Outputs are flushed after every trajectory and existing trajectory files cannot be overwritten. Raw outputs and prompts are preserved even if malformed.

## Semantic smoke gate and evaluation

Inspect all nine outputs against their evidence chains. Stop if Step 1/Step 2 does not track the intended dependency; do not launch the larger run. A full run requires a gate JSON with `passed: true`, reviewer and notes, model name, `dataset_sha256`, `trajectories_path`, and `trajectories_sha256`. Only create a passing gate after actual semantic inspection. The runner verifies hashes and the nine parsed records. This file is a recorded research decision, not a model judge.

```powershell
python -m src.run --shar-repo .. --n 40 --smoke-gate results/smoke/gate.json --output results/pilot/trajectories.jsonl
python -m src.evaluate --input results/pilot/trajectories.jsonl --output results/pilot
```

`manual_review.csv` contains full trajectories, evidence, and editable 0/1 labels. E1 means first-step factual error. E2 means downstream factual error; `propagation_consistent` separately records whether it follows the wrong intermediate fact. A true fact about the wrong person is not automatically a false statement: label factuality and relevance separately. This distinction is necessary for the spec's P(E2|not E1) to remain meaningful. Do not infer causation from entity overlap. Final correctness allows manually verified aliases; automatic exact matches only establish positives. All ambiguous cases stay null until reviewed. Replacement categories are REPAIR/AVOIDANCE/NEW_ERROR/SAME_ERROR/OTHER; oracle replacements are REPAIR by construction and do not measure model repair ability.

After editing a **copy** of the review CSV, use `--labels reviewed.csv` with `src.evaluate`. Missing labels are excluded rather than treated as correct; the summary reports denominators. PG compares E1=true/false within natural baseline only. IE uses matched injected/oracle pairs with both E2 labels. Never pool intervention arms to estimate natural PG. Rates from incompletely labeled data may be biased. The plot marks unavailable rates N/A. CSV, JSON metrics, PNG, and side-by-side case studies are generated; a stopped 3-example smoke run has only three case studies rather than inventing five. No significance claims are supported by this small pilot.

## Preliminary findings

See `results/smoke/inspection.md` for the actual execution outcome and the decision whether scaling is scientifically justified.
