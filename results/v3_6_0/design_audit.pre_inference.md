# Pre-inference design audit

| Intention | Feature | Observable check | Failure meaning |
|---|---|---|---|
| Eliminate world knowledge | Opaque, disjoint IDs | 420 unique IDs; no real entities | Shortcut contamination |
| State-dependent answer | Two explicit mappings | C0/W0 gates | No state dependence |
| Isolate intervention | State-only diff | 60 exact pair assertions | Confounded contrast |
| Mapping capability | Direct lookups | A ≥38/40 | Capability failure |
| Prevent option primacy | No answer list | Prompt audit | Option artifact |
| Record order | Reversed mapping lines | E ≥19/20 unchanged | Order artifact |
| Mapping use | Swapped outcomes | D ≥19/20 | Mapping shortcut |
| Absent state | Uniform UNKNOWN rule | F ≥18/20 | Guessing |
| Entity identity | Only replace entity ID | H ≥19/20 unchanged | Entity artifact |
| No post-hoc rescue | Frozen A–H, G1–G5 and hashes | Verify before/after inference | Adaptive overfit |
| Claim boundary | Phase I only | Final diagnosis | Unsupported mechanism claim |

Calibration 160, main 80 conditional, maximum 240. G requires 159/160. No auxiliary calls.
Frozen UNKNOWN instruction: If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
