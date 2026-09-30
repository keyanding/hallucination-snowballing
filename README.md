# Hallucination snowballing pilot

Standalone research project staged inside the existing checkout. Original SHARS source files are not modified or copied. Move this directory elsewhere and supply `--shar-repo` to keep running it independently.

## Current experiment: v2.1 natural-language prompt diagnosis

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
