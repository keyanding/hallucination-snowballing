# v3.5.1 — Task-Role Framing and Erroneous-State Propagation

**Codex implementation specification · Revised v2 · Pilot · 2026-10-06**

## 0. Decision and research scope

**Research question:** Given an externally supplied erroneous intermediate state \(B'\), when does an LLM propagate the resulting downstream answer \(C'\), override it with the correct answer \(C\), or output something else? Does **task-role framing** of an identical conflicting evidence sentence change this behavior?

**Not studied:** spontaneous first-hop hallucination incidence; end-to-end natural hallucination snowballing; SHAR/HalluSE efficacy; internal attention or belief revision. The intervention is **externally injected B′**, not model-generated B′. Do not call the resulting PR a natural-hallucination propagation rate.

**Novelty relative to v3.2–v3.3:** isolate **task-role framing of identical contradictory evidence** through a matched label intervention, instead of merely adding/removing gold evidence. Include a manipulation check and explicit falsification outcomes; both arms remain logically relevant to the current question; do not claim an intervention on semantic relevance. Report any perceived-authority confound.

**Scope:** frozen 12-case pilot, six main cells per case = 72 main calls; small, predeclared auxiliary validity/format checks may add calls and must be tallied separately. No adaptive benchmark search and no automatic v3.5.2.

## 1. Causal estimand and precise claim

For each independent chain, gold \(A \xrightarrow{r_1} B \xrightarrow{r_2} C\) and mapped donor wrong chain \(B' \xrightarrow{r_2} C'\), with \(B\neq B'\) and \(C\neq C'\).

- **Propagation:** response exactly resolves to \(C'\) after injection of \(B'\).
- **Override:** response exactly resolves to \(C\) despite injection of \(B'\).
- **Other:** any other known answer, uncertainty/refusal, invalid/multiple/truncated. Never force these to PR/OR.

Primary paired contrast (among identical \(B'\) and identical evidence payloads):

\[
\Delta OR_i = \mathbf{1}\{Y_i(B', E_g,\text{current})=C\} - \mathbf{1}\{Y_i(B', E_g,\text{background})=C\}.
\]

Across 12 cases, report mean paired difference with numerator/denominator, full 2×2 transition table, and **both** PR and OR. This is a **task-role label effect** on observable responses, not a semantic relevance effect. Both arms provide the same logically relevant evidence. Even with identical source tags, role labels may convey different perceived authority; report this as a limitation.

A secondary symmetric contrast checks how a false first-hop relation \(E_w: A\to B'\) affects an initially correct \(B\).

## 2. Fixed model/harness

- Continue pinned **Qwen3-4B-Instruct-2507**, 4-bit NF4, BF16 compute, same tokenizer/chat-template and inference stack as v3.4.4.
- New independent chat per call; temperature = 0 / greedy, deterministic; seed and environment recorded. Use the existing exact decoding conventions and avoid hidden reuse of previous conversational context.
- No explicit ranked candidate list or constrained candidate trie for the **main** downstream answer. Give a short natural question and instruction to output only one answer; preserve raw text.
- Choose a generous fixed generation cap using *pre-run independent format smoke*, without tuning it on the 12 cases. Prefer the prior validated free-generation cap; log any truncations.
- Retain automatic graph consistency checking, exact provenance of downstream mappings, hashes of all prompts, model details, and full raw outputs.
- Per run, record whether the two relation lookups use provided context rather than relying on unrelated memorized film facts. Synthetic \(A\) and explicitly declared graph facts are permissible; real entity-to-city mappings remain frozen and source backed.

## 3. Cases and sampling

Freeze **12 independent base cases** before inference. Prefer new anonymous A identifiers and 12 frozen, distinct correct/donor B,B′ pairs from previously audited source mappings. A real named B and B′ each have a distinct, verified \(r_2\) outcome. Within each case, choose one relation \(r_2\) (e.g. place of birth) that is natural to ask; do **not** mix city/country answer granularities or ambiguous parent relations. Explicitly include the mapping statements \(B\to C\), \(B'\to C'\) in a common downstream evidence block.

No case can enter primary analysis unless pre-run **mechanical** validation confirms uniqueness, distinct C/C′, lack of ambiguous aliases, and natural response can be parsed. No replacing low-accuracy cases based on main outcomes. Declare sampling seed and source hashes. Avoid using v3.4.4 outputs to cherry-pick easy/hard identity combinations.

## 4. What is held constant?

Within a case, main outcome prompts share the exact:

- original query A and downstream question r2;
- gold and donor identities B and B′;
- identical r2 mapping statements for both B and B′;
- injected state string, when that arm injects the same state;
- first-hop evidence payload (when both compared conditions contain it), including identical content, source label, timestamp, token sequence, and factual correctness;
- no answer candidate list; identical instruction and decoder.

Only the **contextual role framing** of a pre-existing evidence sentence differs in the framing pair. For this comparison, preserve evidence *location, order, and spacing* as far as possible; change only a short matched role label/paragraph, and audit literal diffs. Do not use "ignore this", "authoritative", "verified truth", "ground truth", or "you must obey" in only one arm: those change instruction strength/trust rather than just a task-role label. Role tags must not alter evidence availability or omit any block from context.

## 5. Six preregistered main conditions per case

**Naming migration from original draft (for traceability only):** `G-REL → G-CURRENT`, `G-INC → G-BACKGROUND`, `W-REL → W-CURRENT`, `C-WREL → C-WCURRENT`. Use **only the new IDs** in runtime artifacts. This revision was made before running v3.5.1; the original conceptual label "relevance" was too broad.


| ID | Injected intermediate state | Additional A→B-type evidence | Context role | Main purpose |
|---|---|---|---|---|
| S0 | Wrong B′ | No conflicting first-hop evidence | Baseline | Test ordinary B′→C′ propagation with downstream mappings available |
| G-CURRENT | Wrong B′ | Correct \(E_g: A\to B\) | Current-task dossier | Primary current-task framing arm |
| G-BACKGROUND | Wrong B′ | Identical correct \(E_g: A\to B\) | Background/history dossier | Primary background framing arm |
| W-CURRENT | Wrong B′ | Wrong \(E_w: A\to B'\) | Current-task dossier | Support-wrong control |
| C0 | Correct B | No first-hop evidence | Baseline | Check correct B→C pathway |
| C-WCURRENT | Correct B | Wrong \(E_w: A\to B'\) | Current-task dossier | Reverse-direction counterfactual |

**Total: 12×6=72 main prompts**. Task-role framing experiment's primary pair is G-CURRENT vs G-BACKGROUND. H0–H4 correspond to the older planned controls but **do not** silently add a seventh condition. A both-claims conflict/order experiment can be a future study, not part of this pilot. If a second independent order rotation is necessary to control an identified ordering confound, preregister as a **separate extension** with its own budget; do not claim it is included in 72.

**Important design limitation:** Both G-CURRENT and G-BACKGROUND contain the same statement explicitly naming the queried A. **Their logical relevance is identical.** Only a contextual role heading changes. This manipulation may also shift the perceived authority or freshness of the evidence, even if its factual source label is kept identical. The identifiable intervention is therefore **label/framing**, not logical relevance and not trust independently. Do not relabel the arms as relevant/irrelevant in code, plots, or conclusions.

## 6. Concrete reference example — include in generated test fixtures

This is an **illustrative synthetic task** (anonymous film and fictional first-hop association). It is **not** an assertion about a real film. Use frozen, source-audited second-hop facts when implementing actual cases. The example deliberately preserves the *same* potentially overriding evidence in G-CURRENT and G-BACKGROUND.

**Query target:** `Film T64218`; \(r_1\) = credited director; \(r_2\) = place of birth.

**Gold chain:** `Film T64218 → Helmut Käutner → Düsseldorf`.

**Donor wrong chain:** `Film T64218 → Rolf Schübel → Stuttgart`.

The real-world biographical associations must be rechecked against the repo's frozen evidence before using these literal people/cities in a run; if they are not verifiable, substitute another preaudited pair. Gold first-hop link to the fictional film is defined solely by the task's synthetic graph.

**Common downstream evidence block, included verbatim in EVERY main arm:**

```text
Reference notes (source: project record set):
Helmut Käutner's place of birth is Düsseldorf.
Rolf Schübel's place of birth is Stuttgart.
```

**Shared current-task prompt for all arms (only slot texts vary):**

```text
Task: The current question concerns Film T64218.

[DOWNSTREAM_REFERENCE_NOTES]

[OPTIONAL_CONTEXT_BLOCK]

Working intermediate state supplied by the previous step:
[CURRENT_STATE]

Question: Based on the supplied context, what is the place of birth of the credited director of Film T64218?
Output only the city name.
```

**S0:**

```text
[OPTIONAL_CONTEXT_BLOCK] = (none)
[CURRENT_STATE] = Rolf Schübel
```

Expected *diagnostic* outcome if the wrong state is followed: Stuttgart (C′). Not a guaranteed prediction.

**G-CURRENT (current-task framed correct evidence):**

```text
Current-task dossier (source: project record set):
Film T64218 has credited director Helmut Käutner.

[CURRENT_STATE] = Rolf Schübel
```

**G-BACKGROUND (background framed correct evidence):**

```text
Background/history dossier (source: project record set):
Film T64218 has credited director Helmut Käutner.

[CURRENT_STATE] = Rolf Schübel
```

**Literal fact in G-CURRENT and G-BACKGROUND is identical, equally logically relevant, and occupies the same position.** Only dossier role heading differs. Keep the parenthetical `source: project record set` identical. A difference estimates the effect of that heading, potentially including its authority/freshness connotations. If the system prompt supplies additional hints tied to either role, remove those hints or apply them symmetrically.

**W-CURRENT:**

```text
Current-task dossier (source: project record set):
Film T64218 has credited director Rolf Schübel.

[CURRENT_STATE] = Rolf Schübel
```

**C0:**

```text
[OPTIONAL_CONTEXT_BLOCK] = (none)
[CURRENT_STATE] = Helmut Käutner
```

**C-WCURRENT:**

```text
Current-task dossier (source: project record set):
Film T64218 has credited director Rolf Schübel.

[CURRENT_STATE] = Helmut Käutner
```

**Classification for this example:**

- `Düsseldorf` => OVERRIDE_TO_GOLD if B′ supplied; GOLD_FOLLOW if B supplied.
- `Stuttgart` => PROPAGATE_WRONG if B′ supplied; INDUCED_WRONG if B supplied.
- any other city/name => OTHER_ANSWER.
- refusal/unknown => UNKNOWN.
- multiple answers, malformed text, truncation => INVALID (with separate subtype).

**Interpretation:** If G-CURRENT elicits Düsseldorf but G-BACKGROUND elicits Stuttgart *with all else fixed*, it supports **task-role label sensitivity** (possibly including implied authority/freshness), not evidence of differing logical relevance or internally repaired beliefs. If both give Düsseldorf, correct evidence overrides in both labels. If both give Stuttgart, supplied wrong state persists in both labels. All three are meaningful outcomes.

## 7. Required manipulation checks and independent capability gates

Before running primary 72 prompts, use independent sample(s) or preselected calibration-only controls, not primary responses, to verify:

1. **Direct r2 lookup:** given only `B→C` evidence and question for B, output C; repeat for B′→C′. Failure means downstream mapping not accessible; stop and inspect.
2. **State adherence sanity:** C0 should usually produce C; S0 should often produce C′. Do not conditionally remove cases that fail S0 after outcome observation; report failed manipulation coverage separately. Preregister an aggregate stop criterion: if C0 accuracy < 10/12 **or** S0 PR < 8/12, interpret the pilot as failed manipulation, not as a clean task-role effect test. All 72 may be collected before gate evaluation; do not expand adaptively.
3. **Framing check:** independent design audit confirms `Current-task dossier` vs `Background/history dossier` changes only the heading, not its factual sentence, source tag, location, or downstream evidence. Optional *blinded* human ratings may separately record perceived task role and perceived trust/authority; never treat them as proof of isolated logical relevance. A null G-CURRENT/G-BACKGROUND contrast means no detected effect of these two particular headings in this pilot.
4. **Record-order control:** keep r2 records and task frame fixed; no candidate list. Log record order hash. A separate exploratory record-order perturbation is optional *only after* completing/reporting the frozen pilot, not silently mixed into main 72.
5. **No leakage:** each call fresh; identical main model settings and output parser; first-hop error supplied explicitly, not presented as the model's own previous answer.

## 8. Main outcomes and estimands

**Identification boundary:** In the primary pair the evidence remains logically applicable to the current question in both arms. The causal contrast identifies the effect of the specific role headings under this prompt, *not* pure semantic relevance. Different perceived priority, recency, or credibility may mediate the heading effect. Preserve this caveat in `diagnosis.md`, charts, abstract, and README.


For each cell report counts **with all 12 cases as denominator** and a second analysis among valid parses only:

- `PR = #PROPAGATE_WRONG / 12` for conditions injecting B′.
- `OR = #OVERRIDE_TO_GOLD / 12` for conditions injecting B′.
- `OTHER`, `UNKNOWN`, `INVALID` each reported independently.
- correct-state degradation in C-WCURRENT vs C0: `#INDUCED_WRONG/12` and `#GOLD_FOLLOW/12`.
- Primary `ΔOR = OR(G-CURRENT) – OR(G-BACKGROUND)` (paired). Secondary `ΔPR` analog.
- Paired transition table G-BACKGROUND→G-CURRENT: [C′→C, C→C′, unchanged C, unchanged C′, transitions involving other].
- Show 12 case-level raw triples (state, contextual role, output) and per-case contrast.

Descriptive uncertainty: paired sign/binomial interval over discordant case pairs **if** enough discordances; report exact numerator and denominator, no unwarranted significance. With 12 cases, avoid overstated statistical power. Candidate scores/mean log probabilities are optional diagnostics and **not** calibrated choice probabilities.

## 9. Predeclared falsification logic

- **Task-role framing hypothesis supported descriptively:** at least 4/12 cases give a more gold-aligned outcome in G-CURRENT than G-BACKGROUND, with reverse switches at most 1/12; distinguish this heuristic from inferential significance. Also require manipulation and capability checks.
- **No resolved task-role label effect:** outputs mainly identical under G-CURRENT/G-BACKGROUND, or switches symmetric/mixed. Report as null/inconclusive at pilot scale, not "logical relevance does not matter".
- **Wrong-state dominance:** G-CURRENT and G-BACKGROUND both mainly C′ despite accessible correct evidence.
- **Evidence dominance:** G-CURRENT and G-BACKGROUND both mainly C; this shows correct context can override supplied state, not that task-role headings matter.
- **Format/capability failure:** high invalids or missing C0/S0 separation; no mechanistic conclusions.
- **Reverse asymmetry:** C-WCURRENT vs C0 may reveal whether wrong evidence changes correct initial states; do not assume symmetry.

A null result would limit the usefulness of these particular task-role headings as moderators; it cannot falsify the impact of logical evidence relevance, evidence authority, or evidence-state competition more generally. Findings do not show *why* a particular internal computational path was taken.

## 10. Stop / continuation conditions

- Fail mechanical graph uniqueness, mapping provenance, same-evidence audit, or inference reproducibility: stop **before** main inference.
- Independent r2 capability validation fails: stop and diagnose, no new dataset hunting inside v3.5.1.
- After fixed main 72: if C0 <10/12 or S0 PR <8/12, mark manipulation failure and stop mechanistic interpretation.
- If G-CURRENT vs G-BACKGROUND is near-null or mixed, **do not** invent more label variants to obtain a positive result. Summarize and redirect to a better-identified intervention only after external design review.
- If contrast is nontrivial, plan a separately preregistered independent confirmation experiment; **do not automatically run it**.
- Independently of outcome, do not silently revise definitions/thresholds; write every deviation and its timing.

## 11. Inputs, scripts, deterministic outputs

Prefer adding a clean module rather than editing v3.4.4 outputs. Create:

```text
experiments/v3_5_1/
  build_cases.py
  validate_cases.py
  render_prompts.py
  run_pilot.py
  analyze.py
```

and deliver:

```text
results/v3_5_1/
  README.md
  pre_registration.md
  design_audit.md
  cases.json
  model_manifest.json
  prompt_plan.json
  prompt_diff_audit.md
  capability_checks.jsonl
  outputs.jsonl
  parsed_outcomes.jsonl
  metrics.json
  inspection.md
  diagnosis.md
  gate.json
  CHANGELOG.md
```

`cases.json` must freeze each A/B/B′/C/C′, relation r1/r2, citations/source ids for r2 claims, synonyms, case IDs, generation seeds. `prompt_plan.json` must include hashes plus every textual condition before execution. Save raw responses and exact template metadata; never overwrite previous experimental versions.

## 12. Audit table (before and after experiment)

Add a dedicated audit result stating: **"Same fact, same semantic relevance, different task-role heading; perceived authority not independently isolated."** Any output describing G-BACKGROUND as factually irrelevant is an automatic interpretation-audit failure.


Include and complete this table **before inference**, then append achieved/failed outcomes after execution.

| Design intention | Feature | Observable check | Failure meaning |
|---|---|---|---|
| Study propagation not initiation | Inject same B′, ask r2 downstream question | S0 PR, downstream C′ trace | No reliable propagation assay |
| Verify gold path | Paired C0 and r2 oracle | C0 accuracy and direct r2 lookup | Capability not established |
| Isolate task-role framing | Identical E_g text; matched current/background role tags | Literal prompt diff, G-CURRENT vs G-BACKGROUND | Role label may alter perceived trust/recency; cannot infer semantic relevance |
| Separate evidence correctness from task-role heading | G-CURRENT, G-BACKGROUND, W-CURRENT | PR/OR by arm | Cannot isolate content vs role |
| Check reverse-direction influence | C0 vs C-WCURRENT | Correct→wrong flips | Unjustified symmetric narrative |
| Avoid option primacy | No enumerated candidate list | Prompt audit | Earlier artifact recurs |
| Avoid record-order confound | Fixed downstream/name-record ordering | Prompt hashes | Change reflects evidence order |
| Keep results interpretable | Fixed categories, separate invalids | Raw output and classification agreement | Mislabelled propagation |
| Preserve inference limits | 12 paired cases, no cherry-picking | Full case table; no adaptive rerun | Inflated claim |
| Stop at informative boundary | Frozen gates and 72 calls | Gate + changelog | Aimless calibration iteration |

## 13. Required diagnosis.md answers

1. Did S0 and C0 demonstrate the intended state manipulation and downstream retrieval?
2. Did identical correct evidence affect output differently when framed as current-task vs background history?
3. Were any observed differences attributable to changed evidence text, source authority, order, or formatting? Show prompt diffs.
4. Which cases flip C′→C in G-CURRENT but not G-BACKGROUND, and which show the opposite?
5. How does wrong supporting evidence W-CURRENT compare with S0 and G-CURRENT?
6. Does wrong evidence reverse an initially correct B in C-WCURRENT?
7. What proportions were C, C′, other, unknown, invalid under every cell?
8. Are results only behaviorally consistent with evidence-state competition, or can a more specific interpretation be justified?
9. What claim can be made about **externally injected** erroneous states, and what claim cannot be made about spontaneous hallucinations?
10. Which one independently testable hypothesis, if any, merits follow-up? Explicitly recommend **stop** if pilot produces no new information.

## 14. Deliverable acceptance criteria

- **Terminology audit:** `G-CURRENT`/`G-BACKGROUND` everywhere in execution artifacts; do not claim "relevance varied" or "irrelevant evidence". Both evidence statements explicitly concern current A.
- In `pre_registration.md`, define the estimand as "response difference under current-task vs background dossier label with identical relevant fact." Distinguish the label effect from logical relevance and perceived authority.


- All 12×6 frozen calls (or a documented early structural halt) present; exact denominators and raw outputs.
- No downstream experiment is incorrectly described as free-form spontaneous first-hop hallucination.
- Explicit sample prompt demonstrating G-CURRENT vs G-BACKGROUND included in `inspection.md`.
- Pilot includes a **design intention → feature → observable check → failure meaning** mapping, with post-run audit.
- Repo CHANGELOG explains what changed and why; gate.json is machine-readable; stop condition evaluated.
- Final recommendation is one of: `STOP_INVALID`, `STOP_UNINFORMATIVE`, `PILOT_SIGNAL_CONFIRM_SEPARATELY`.
