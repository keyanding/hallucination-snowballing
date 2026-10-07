# v3.6.2 pre-registration

40 fresh base cases × four K levels × C0/W0 =320 main calls. Twelve seeded cases × three K24 positions × C0/W0 =72 secondary calls. Total392. All main and diagnostic renderings frozen before any inference. No extra capability/smoke calls. Main calls shuffle seed362; diagnostics seed364; generation seed42; greedy cap16; fresh chat, use_cache=False, no constrained decoding. Same pinned Qwen3/NF4/BF16 stack and exact minimal K0 template as v3.6.1.

## Cases, nesting and position
Candidates: STATE/OUTCOME_[A-Z][0-9]{2},5200 IDs. Exclude old IDs case-insensitively across all v3.6.0 and v3.6.1 cases. Choose each role's smallest available tokenizer-length bucket, deterministic seed362, no model-output input. All2080 selected IDs are globally unique; each case has52 unique suffixes, equal character/token counts within state and outcome roles. Relevant state/outcome suffix characters do not overlap; each distractor state/outcome pair also has disjoint suffix characters.
Each case has24 distractors. All smaller blocks are exact order-preserving subsets of larger blocks, differing only by inserted irrelevant lines. Relevant pair adjacency/order remains fixed. Positive-K bands are beginning14, middle13, end13 across cases, same band across K per case. K0 only has two positions, so three-band placement is inapplicable there; gold-first20/wrong-first20. Beginning positions1/2; middle K/2+1,K/2+2; end K+1,K+2. This balances relative region, not absolute distance; added text also changes distance to the query, so no internal mechanism is isolated.
Secondary selection seed363: sample2 per gold-first/wrong-first cell in each main band (12 total). At K24 place the same pair at beginning/middle/end, holding all distractor content and relative order fixed. All72 calls execute even where24 prompts duplicate primary K24; report exact-repeat consistency, do not reuse outputs. No diagnostic result changes the main gate.

## Parser and statistics
Normalization only NFC, strip outer whitespace, remove one final period. No case folding/extraction. Exact gold=C, paired alternative=Cp, UNKNOWN literal, one other well-formed OUTCOME_[A-Z][0-9]{2}=OTHER; any explanation/multiple output or truncation=INVALID. OTHER may be a distractor outcome: record it separately, but count in off-target O. Model-generated invalid output does not mean parser implementation failed.
For each K: A_C/40,A_W/40,S/40,U/80,O/80, separate categories by C0/W0. Wilson95% intervals for A_C,A_W,S. Unit40 paired cases. Delta_C/Delta_W/Delta_S are integer count differences /40 vs K0. Report exact per-arm5×5 transitions, correct→incorrect and incorrect→correct, paired both-correct→not-both-correct and reverse, including all case IDs. No significance testing required. No pooling hides C0/W0.
On baseline regression collect the prespecified outputs but stop context-size interpretation. Missing required calls or structural/runtime/parser-code faults yield infrastructure failure. Secondary accuracy failures do not change the main gate. No reruns, case replacements, caps or thresholds adapted after inference.

## User-approved decision amendment, frozen before inference

INFRASTRUCTURE_FAILURE is restricted to real structural/runtime/parser implementation faults: bad prompt/render/hash validation, missing calls, model exceptions or parser malfunction. Model-generated OTHER/INVALID is not by itself infrastructure failure.
Priority: INFRASTRUCTURE_FAILURE → BASE_ASSAY_REGRESSION → CONTEXT_SENSITIVE_ASSAY → ROBUST_CONTEXT_ASSAY.
If K0 C0<39/40, W0<39/40 or paired S<39/40, classify BASE_ASSAY_REGRESSION and stop context-size interpretation.
With valid K0, CONTEXT_SENSITIVE_ASSAY holds if any original sensitive criterion is met, or if monotonic collapse holds, or OTHER+INVALID>2/320 with healthy infrastructure/parser. Report off-target counts separately at each K.
Monotonic collapse means S(K0)≥S(K4)≥S(K12)≥S(K24), at least two strict decreases, and S(K0)−S(K24)≥4/40. Use exact integer paired-success counts.
All remaining structurally valid outcomes are ROBUST_CONTEXT_ASSAY. No post-inference threshold changes.

## Claim boundary
Robustness licenses only reliable symbolic mapping under up to24 irrelevant records in this setting. Sensitivity is an observed controlled context effect, not hallucination snowballing or an internal explanation. Diagnose position with the secondary subset; do not generalize it to all40 cases. No upstream A→B layer, entities, conflicting evidence, natural hallucinations, SHAR/HalluSE or automatic next phase.
