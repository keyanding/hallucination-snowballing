# Smoke test: STOP — semantic dependency gate failed

Executed with cached Qwen3-0.6B, SHARS model wrapper, seed 42, three examples and three conditions (nine real generations). All nine outputs parse, but **none of the three natural trajectories establishes the required first-hop intermediate entity**. Do not scale this configuration to 40 examples. The failed decision is stored with data/output hashes in `gate.json`.

| Question | Intended dependency | Observed failure |
|---|---|---|
| Malcolm IV's father | Malcolm IV → mother Ada de Warenne → spouse Henry of Scotland | Baseline invents a father and then a birth year. Injected and oracle continuations name other fathers without resolving the mother's spouse. The question itself can also be answered directly, so this dataset graph is not a necessary reasoning route. |
| Prince David of Kakheti's father's death place | Prince David → father Teimuraz I → Astarabad | Baseline begins with a birth year, and all three final answers give years rather than locations. The injection changes the named person but does not preserve the target relation. |
| Walter Butler's paternal grandfather | Walter → father Edmund MacRichard Butler → father Sir Richard Butler | Baseline never identifies the father. Injected and oracle outputs repeat the supplied father as the grandfather rather than executing the second relation. |

The three supplied substitutions contradict the annotated parent relation and preserve its entity role. However, cross-family/time-period donors may be implausible for a knowledgeable model. Candidate preparation is therefore not a substitute for validating the intervention. Parent/spouse inference also has real-world exceptions and direct-answer shortcuts.

All nine final answers are incorrect against the supplied dataset answers after inspection (0/3 in each condition). This is a **smoke diagnostic**, not a meaningful intervention-effect estimate. E2 and propagation attribution remain unlabeled because the intended dependent step is missing or changed; absence of valid measurement must not be converted into an error rate of zero. Baseline factual claims beyond the provided evidence are not automatically judged. PG and IE are unavailable. No claim of weak/strong propagation or successful SHARS intervention follows from this run.

Oracle correction replaces the first fact with the dataset's gold fact and has REPAIR label by construction. It is not a model-generated repair. Even after correction, the observed continuation does not execute the target second relation.

## Next experimental revision

Exclude inference questions answerable via a direct relation (such as parent → spouse). Keep explicitly compositional questions, require the first step to name the requested intermediate entity and the second to resolve the requested relation, and validate a fresh three-example smoke run. A more knowledgeable instruction-following model may be needed. These are proposed revisions, not experiments executed after the stop condition. Original raw outputs are preserved without prompt-tuning away failures.

## Artifacts

- `trajectories.jsonl`: nine actual generations, prompts, fixed/replaced segments, counts and latency.
- `trajectories.manifest.json`: model/SHARS revisions and generation settings.
- `reviewed_labels.csv`: evidence-based final-answer review; ambiguous hop labels left blank.
- `manual_review.csv`: generated worksheet for further labeling.
- `summary.csv`, `metrics.json`, `downstream_error.png`: diagnostic exports; unknown rates marked unavailable.
- `case_studies.md`: all three examples side by side. Three cases are retained because no additional examples were run.
