# Pre-inference design audit

| Intention | Feature | Check | Failure meaning |
|---|---|---|---|
| Add upstream mapping | Explicit A→B and symmetric alternative | New U gates; P shell tested separately | Stage/shell brittleness |
| Upstream capability | Balanced symmetric tables | A/B/E and G1/G2 | Lookup instability |
| Isolate intervention | Only recorded state changes | P literal diffs | Confounded propagation |
| Prevent recomputation | No upstream evidence in P | Prompt audit | Override possible |
| Actual modular chain | Forward actual normalized U-GOLD | Source-linked pipeline log | Repaired-state artifact |
| Avoid world knowledge | Fresh opaque IDs |7800-tokenizer audit;360 fresh IDs|Shortcut|
| No fallback interference | No UNKNOWN instruction |Template checks|Fallback brittleness|
| No candidate options | Mapping tables only |Exact prompt audit|Option artifact|
| Integrated diagnostic separate |20 seeded cases|Readiness outside G1–G7|Internal-use overclaim|
| Order diagnostic separate |10 seeded cases|Unchanged and correct≥19/20|Order limitation|
| No adaptive tuning |Frozen rules,subsets,templates|Hash verification|Post-hoc rescue|
| Phase I boundary |No next phase|Final diagnosis|Natural snowballing/SHAR overclaim|

Maximum340 calls including optional20-call order diagnostic. Dynamic pipeline templates and builder freeze before inference; actual prompts follow actual upstream strings and are hashed when built. Malformed upstream skips are recorded, never repaired.
