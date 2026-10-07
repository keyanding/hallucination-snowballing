# Pre-inference design audit

| Intention | Feature | Observable check | Failure meaning |
|---|---|---|---|
| Diagnose all old cases | 20 × four families × two states |160 frozen calls|No cherry-picking|
| UNKNOWN interference | One-line matched factor |Exact prompt assertions|Contaminated factor|
| Prompt complexity | Specified full/minimal templates |Preserved mappings/states|Bundled surface contrast only|
| Remove entity | No entity in C |Template assertions|Entity confound|
| Tokenization balance |5200 audited candidates|Equal within-pair tokens and lengths|Construction asymmetry|
| Causal contrast |Supplied state only|40 literal pair diffs|Intervention confound|
| Fallback separate |10 disjoint controls|≥9/10 UNKNOWN|Fallback unreliable|
| Avoid answer options |Only mapping evidence|No candidate list|Option artifact|
| Order diagnosis |10 seeded cases × two states|≥19/20 unchanged mapped identity|Order limitation, not gate rescue|
| Model-size diagnosis |Only conditional and available|Availability frozen; same prompts|No inference about size without data|
| Prevent optimization |Frozen hashes and C1–C6|Pre/post verification|Adaptive optimization|
| Claim boundary |Minimal primitive only|Final diagnosis|No SHAR/mechanism claim|

Stage C never depends on Stage B pass/fail. Total 270 calls. Static audit is descriptive, not causal.
FULL_UNKNOWN uses the spec's new UNKNOWN wording; it is not a byte-identical v3.6.0 replay.
