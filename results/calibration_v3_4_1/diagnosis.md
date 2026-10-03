# v3.4.1 diagnosis

This is calibration of one frozen Qwen3-4B NF4/BF16 model and a constructed catalog task, not a propagation experiment or a general research conclusion.

1. **Which families cause errors?** ['M1', 'M4']

2. **Which do not?** ['M2', 'M3']

3. **Gradual frontier or capability cliff?** Neither is established. M1 has an isolated D2 error that disappears at D3. M4 has errors at D0 and D3 but none at D1/D2. This is a sparse, non-monotonic pattern, not a demonstrated gradual frontier or a near-random cliff.

4. **Which pairs meet the target?** The error-rate band alone contains M4/D3 (2/6). M4/D3 nevertheless has 0/6 cases inside the preregistered absolute gold-margin threshold of 0.5 nats/token (required 4/6); its median gold margin is 2.4502. Its two wrong-answer margins are -0.5065 and -0.5553. No threshold was relaxed after observing these values, and no pair qualifies provisionally.

5. **Held-out confirmation?** Not run: no provisional frontier. The twelve frozen cases remain unqueried.

6. **Does free generation support constrained choice?** FSC={'count': 96, 'denominator': 96, 'rate': 1.0}; FCA={'count': 96, 'denominator': 96, 'rate': 1.0}; EFCA={'count': 96, 'denominator': 96, 'rate': 1.0}; truncated=0. Formatting failures are separate from semantic choices.

7. **Does likelihood support constrained choice?** LCA={'count': 96, 'denominator': 96, 'rate': 1.0}; gold margin distributions and boundary fractions are in metrics.json. Mean-normalized likelihood is diagnostic, never a substitute for C.

8. **Ambiguity, position bias, or formatting?** Every rendered credit path resolves uniquely in the programmatic audit. Independent human review remains pending. Flagged families: []. Position rates do not establish causal position sensitivity without order swaps; no swaps were run.

9. **What should be frozen for v3.5?** No stable confirmed frontier. No v3.5 launch or construction recommendation is authorized by this run.

# Frontier selection

Lowest in-band difficulty; nearest out-of-band level is diagnostic only. No post-output tuning.

| Mechanism | D0 | D1 | D2 | D3 | Selected/diagnostic | Status |
|---|---|---|---|---|---|---|
| M1 | 0/6 | 0/6 | 1/6 | 0/6 | D2 | NO_STABLE_FRONTIER_FOUND: NO_STABLE_FRONTIER_FOUND, INSUFFICIENT_LIKELIHOOD_BOUNDARY_SIGNAL |
| M2 | 0/6 | 0/6 | 0/6 | 0/6 | D0 | NO_STABLE_FRONTIER_FOUND: NO_STABLE_FRONTIER_FOUND, INSUFFICIENT_LIKELIHOOD_BOUNDARY_SIGNAL |
| M3 | 0/6 | 0/6 | 0/6 | 0/6 | D0 | NO_STABLE_FRONTIER_FOUND: NO_STABLE_FRONTIER_FOUND, INSUFFICIENT_LIKELIHOOD_BOUNDARY_SIGNAL |
| M4 | 1/6 | 0/6 | 0/6 | 2/6 | D3 | REJECTED: INSUFFICIENT_LIKELIHOOD_BOUNDARY_SIGNAL |

## Limits

Six development cases per family give a coarse error grid (only 2/6 lies inside 20–40%). This design may remain too easy; that is a valid negative calibration outcome. Catalog conventions explicitly disambiguate relations, and composition is index traversal rather than unrestricted factual reasoning. M2 highlights shared attributes for one alternative, uses broad 50-year bands, and does not change the candidate set. Entities can recur across splits; only target film questions are disjoint. Do not redesign or retune using held-out answers. Future evaluation must exclude all 36 films.

The three channels agree on all four wrong selections as well as the correct ones (96/96 agreement). This supports a semantic-selection interpretation within this task, not a claim that constrained and free decoding are generally equivalent. The 100% free-format result cannot be attributed solely to the 96-token cap because the prompt construction also differs from v3.4. Candidate plausibility is domain-level: age/country/era are not uniformly matched for all alternatives, especially older films; this can make some distractors weak.
