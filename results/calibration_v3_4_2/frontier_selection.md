# Development frontier selection

All cutoffs, the immediate-neighbor rule and the complexity tie-break were frozen before inference. At most two qualifiers are retained. No post-held-out retuning.

| Condition | C error | Gold median margin | Near boundary | FCA | LCA | Easier local support | Failed criteria | Selected |
|---|---|---|---|---|---|---|---|---|
| D1B0 | 3/8 (37.5%) | 1.7524 | 2/8 (25.0%) | 8/8 (100.0%) | 8/8 (100.0%) | none | boundary, median_margin, no_position_bias, local_trend | False |
| D1B1 | 3/8 (37.5%) | 0.9682 | 1/8 (12.5%) | 8/8 (100.0%) | 8/8 (100.0%) | D1B0 | boundary, no_position_bias | False |
| D1B2 | 3/8 (37.5%) | 0.5033 | 2/8 (25.0%) | 8/8 (100.0%) | 8/8 (100.0%) | D1B1 | boundary, no_position_bias | False |
| D2B0 | 2/8 (25.0%) | 0.8415 | 2/8 (25.0%) | 8/8 (100.0%) | 7/8 (87.5%) | D1B0 | boundary, no_position_bias | False |
| D2B1 | 2/8 (25.0%) | 0.7481 | 2/8 (25.0%) | 8/8 (100.0%) | 8/8 (100.0%) | D1B1, D2B0 | boundary, no_position_bias | False |
| D2B2 | 4/8 (50.0%) | 0.4275 | 1/8 (12.5%) | 8/8 (100.0%) | 8/8 (100.0%) | D1B2, D2B1 | boundary, no_position_bias | False |
| D3B0 | 3/8 (37.5%) | 1.2517 | 4/8 (50.0%) | 8/8 (100.0%) | 8/8 (100.0%) | D2B0 | no_position_bias | False |
| D3B1 | 4/8 (50.0%) | 0.7280 | 1/8 (12.5%) | 8/8 (100.0%) | 8/8 (100.0%) | D2B1, D3B0 | boundary, no_position_bias | False |
| D3B2 | 4/8 (50.0%) | 0.3887 | 1/8 (12.5%) | 8/8 (100.0%) | 8/8 (100.0%) | D2B2, D3B1 | boundary, no_position_bias | False |
| D4B0 | 3/8 (37.5%) | 1.2886 | 3/8 (37.5%) | 8/8 (100.0%) | 8/8 (100.0%) | none | no_position_bias, local_trend | False |
| D4B1 | 4/8 (50.0%) | -0.0602 | 2/8 (25.0%) | 8/8 (100.0%) | 8/8 (100.0%) | D3B1, D4B0 | boundary, no_position_bias | False |
| D4B2 | 3/8 (37.5%) | 0.1857 | 3/8 (37.5%) | 8/8 (100.0%) | 8/8 (100.0%) | D3B2 | no_position_bias | False |

Held-out results:

Not run: no development condition qualified. Twelve frozen held-out cases remain unqueried.
