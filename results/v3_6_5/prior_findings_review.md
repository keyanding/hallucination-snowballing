# Prior Findings Review

References: docs/validated_findings.md and docs/validated_findings.json.

| Finding / Component | Ledger status | Treatment in this experiment | Rationale |
|---|---|---|---|
| F01 | ACTIVE_WARNING | AVOIDED | Whole-output eligibility and independent confirmation; no denominator substitution. |
| F02 | ACTIVE_WARNING | AVOIDED | Synthetic explicit records avoid closed-book knowledge and birthplace granularity. |
| F03 | FROZEN_REUSE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F04 | FROZEN_REUSE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F05 | ACTIVE_WARNING | AVOIDED | No supporting prose that asserts a competing answer; exactly one gold path. |
| F06 | ACTIVE_WARNING | AVOIDED | No UNKNOWN instruction or fallback shell. |
| F07 | ACTIVE_WARNING | AVOIDED | No Recorded intermediate result shell or downstream inference. |
| F08 | FROZEN_REUSE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F09 | FROZEN_REUSE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F10 | FROZEN_REUSE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F11 | FROZEN_REUSE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F12 | FROZEN_REUSE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F13 | INCONCLUSIVE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F14 | ACTIVE_WARNING | AVOIDED | Keep historical N cap96, no sweep; truncated responses cannot be strict-valid. |
| F15 | ACTIVE_WARNING | AVOIDED | No answer options or numbered candidate list; records are relational evidence. |
| F16 | ACTIVE_WARNING | INTENTIONALLY_RETESTED | Eight seeded complete name-record cyclic permutations; non-gating regardless of development pass. |
| F17 | ACTIVE_WARNING | AVOIDED | Only unconstrained greedy generation, no likelihood or constrained channel. |
| F18 | INCONCLUSIVE | TARGETED | Replicate historical HARD/N5/24 on fresh graphs, then independent confirmation if development passes. |
| F19 | ACTIVE_WARNING | INTENTIONALLY_RETESTED | Fixed development4/24 and confirmation3/24 traceable wrong yield; no error-selected cases. |
| F20 | INCONCLUSIVE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F21 | INCONCLUSIVE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F22 | OPEN_QUESTION | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F23 | OPEN_QUESTION | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F24 | INCONCLUSIVE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F25 | INCONCLUSIVE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F26 | FROZEN_REUSE | OVERRIDDEN | Use exact v3.4.4 person-name parser, not later state parser; preserve raw text and no extraction. |
| F27 | FROZEN_REUSE | OVERRIDDEN | Same pinned greedy stack; cap96 matches historical N, explicitly differs from cap16 symbolic components. |
| C01 | FROZEN_REUSE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| C02 | FROZEN_REUSE | NOT_RELEVANT | Do not run direct A-to-B shell; reuse historical D4B2 catalog graph task. |
| C03 | FROZEN_REUSE | NOT_RELEVANT | No opaque-state ID task; retain historical T/R graph ID family and real-name candidates. |
| C04 | FROZEN_REUSE | OVERRIDDEN | Person-name parser is unchanged v3.4.4 implementation; later STATE normalization does not apply. |
| C05 | FROZEN_REUSE | OVERRIDDEN | Same model stack but cap96; historical HARD/N budget and new fixed validity/yield gates. |
| C06 | FROZEN_REUSE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| C07 | FROZEN_REUSE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
