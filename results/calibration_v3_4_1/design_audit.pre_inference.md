# v3.4.1 pre-inference design audit

| Design intention | Experimental feature | Observable check | Failure meaning |
|---|---|---|---|
| Find Qwen3-specific error surface | Four mechanisms, four levels, six dev cases each | 96 Channel-C choices | No empirical frontier |
| Preserve traceability | Four real directors with frozen distinct targets | 36/36 candidate universes covered | Cannot support future propagation |
| Avoid output-format confound | Exact token trie; EOS only at complete names | All four reachable; no other terminals | Measurement interface failed |
| Preserve natural-behavior visibility | Greedy free generation, 96 tokens | FSC, FCA, EFCA; raw output retained | Constrained external validity uncertain |
| Measure decision confidence | Teacher force same prompt and candidate tokens; EOS excluded | Sum, mean, gold margin, LCA; boundary <=0.5 nats/token | Preference insufficiently characterized |
| Avoid assuming old-model failure modes | Frozen Qwen3-4B revision, NF4/BF16 | All predeclared curves measured | Mechanisms may not transfer |
| Avoid overfitting calibration set | 24 dev films; 12 disjoint held-out films; entities may overlap | Every selected mechanism uses all 12 once | No held-out generalization |
| Preserve unique ground truth | Explicit deterministic catalog credit paths; other link types non-credit | 288 rendered paths resolve uniquely; independent human audit pending | No human-certified ambiguity clearance |
| Prevent position shortcuts | Dev positions 2/2/1/1, held-out 3/3/3/3; frozen order | Position-conditioned rates and preregistered bias rule | Candidate index confound |
| Keep scope to calibration | Only first-hop F/C/L | No downstream generation or propagation metrics | Scope violation |

## Preregistered policy

```json
{
  "near_boundary_nats_per_token": 0.5,
  "minimum_boundary_cases": 4,
  "dev_band": [
    0.2,
    0.4
  ],
  "heldout_band": [
    0.15,
    0.45
  ],
  "minimum_lca": 0.8,
  "minimum_heldout_free_coverage": 0.7,
  "position_bias": "At a level: selected position >=50%, with >=2 wrong selections there and wrong selection >=40% among cases whose gold is elsewhere. Any flagged dev level blocks family promotion.",
  "free_outset_stop": "More than 50% short parseable out-of-set free answers blocks promotion.",
  "tie_rule": "Lowest difficulty; nearest-band ties also use lowest difficulty.",
  "human_audit": "Independent human review is not available in this automated run. Gate requires a recorded human audit before authorization."
}
```

## Construction and audit limits

Catalog IDs and comparison links are experimental constructs, explicitly identified in every prompt. Film-director endpoints and shared attributes are sourced from the frozen dataset. M2 keeps candidates fixed and highlights era/genre similarity to one alternative; a 50-year era band is coarse. This tests attribute salience, not changing candidate proximity. M1/M3 overlap in relation/order manipulations; these are operational families, not independent causal mechanisms. Prior-version entities and some questions may recur; only dev/held-out target films are disjoint. No independent human audit has been claimed.

Every possible rendering is preserved in prompt_plan.json, including unexecuted held-out levels; access before inference is structural auditing, not model-based selection.
