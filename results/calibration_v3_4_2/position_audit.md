## Position and case diagnostics

The preregistered pooled POSITION_BIAS flag is **True**. D3B0, D4B2 meets all other development criteria but is not selected. No new threshold, candidate ordering, or model call was introduced in this presentation step.

| Candidate position | Times selected / 96 | Gold occurrences | Wrong selections | Wrong selections when gold elsewhere / 72 | Share of 38 errors |
|---|---|---|---|---|---|
| 1 | 54/96 | 24 | 34 | 34/72 | 89.5% |
| 2 | 9/96 | 24 | 0 | 0/72 | 0.0% |
| 3 | 5/96 | 24 | 0 | 0/72 | 0.0% |
| 4 | 28/96 | 24 | 4 | 4/72 | 10.5% |

Always-wrong base cases: dev-04, dev-07; these contribute 24/38 errors. The 96 decisions are repeated measurements on eight base cases, not 96 independent cases. Because candidate identities remain at fixed positions within each case, the position flag cannot distinguish index preference from candidate-identity or case effects. It is a conservative exclusion signal, not proof of a causal position effect. No candidate-order counterfactual was run.

The observed axis is partly ordered, not globally monotonic: depth ER/GM satisfy 6/9 and 7/9 adjacent comparisons, while branch ER/GM both satisfy 7/8. Margin support at selected-looking cells does not override the position exclusion. The held-out split remains unqueried.
