# Hallucination snowballing pilot

Standalone research project staged inside the existing checkout. Original SHARS source files are not modified or copied. Move this directory elsewhere and supply `--shar-repo` to keep running it independently.

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
python -m src.prepare --n 40 --seed 42
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
