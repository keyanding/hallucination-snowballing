# Counterbalanced frontier diagnostics

These are the six deliberately selected cases, not a replacement clean development split. First summarize four orders per case, then aggregate six cases equally. The four rotations are not four new independent cases.

## MID: D3B0

| Case | Error fraction across orders | Median gold margin | Near-boundary fraction | ISR | Classification |
|---|---:|---:|---:|---:|---|
| dev-04 | 0.50 | -0.1129 | 0.75 | 0.50 | POSITION_1_LOCKED |
| dev-07 | 0.25 | 1.1241 | 0.50 | 0.75 | UNSTABLE_OTHER |
| dev-05 | 0.25 | 0.1614 | 0.75 | 0.75 | UNSTABLE_OTHER |
| dev-01 | 0.50 | -0.0483 | 1.00 | 0.50 | POSITION_1_LOCKED |
| dev-06 | 0.25 | 2.2875 | 0.00 | 0.75 | UNSTABLE_OTHER |
| dev-08 | 0.00 | 2.5235 | 0.00 | 1.00 | GOLD_STABLE |

Equal-case mean error=29.2%; median of six case median margins=0.6427; equal-case mean NBF=50.0%; mean ISR=0.708. Heuristic frontier-like=True.

PSR: position 1: 13/24 (54.2%); position 2: 3/24 (12.5%); position 3: 3/24 (12.5%); position 4: 5/24 (20.8%).

## HARD: D4B2

| Case | Error fraction across orders | Median gold margin | Near-boundary fraction | ISR | Classification |
|---|---:|---:|---:|---:|---|
| dev-04 | 0.75 | -1.7795 | 0.00 | 0.25 | POSITION_1_LOCKED |
| dev-07 | 0.50 | 0.0610 | 0.00 | 0.50 | POSITION_1_LOCKED |
| dev-05 | 1.00 | -2.2653 | 0.25 | 0.50 | POSITION_1_LOCKED |
| dev-01 | 0.75 | -3.2635 | 0.25 | 0.25 | POSITION_1_LOCKED |
| dev-06 | 0.00 | 3.7435 | 0.00 | 1.00 | GOLD_STABLE |
| dev-08 | 0.00 | 1.4031 | 0.00 | 1.00 | GOLD_STABLE |

Equal-case mean error=50.0%; median of six case median margins=-0.8592; equal-case mean NBF=8.3%; mean ISR=0.583. Heuristic frontier-like=False.

PSR: position 1: 16/24 (66.7%); position 2: 2/24 (8.3%); position 3: 3/24 (12.5%); position 4: 3/24 (12.5%).

No clean route is supported. Resolve answer-option order sensitivity before any propagation study. No automatic v3.5 authorization.
