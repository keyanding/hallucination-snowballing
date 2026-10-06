# Diagnosis

Same fact, same semantic relevance, different task-role heading; perceived authority not independently isolated.

1. State manipulation: S0 propagated 9/12; C0 followed gold 9/12. Independent capability checks passed: True. Gates: {'complete': True, 'capability': True, 'C0': False, 'S0': True, 'framing_format': True}.

2. Identical correct evidence under different headings: paired ΔOR={'count': 0, 'denominator': 12, 'rate': 0.0}; ΔPR={'count': 0, 'denominator': 12, 'rate': 0.0}. Framing heuristic met: False. Evidence dominance: True; wrong-state dominance: False.

3. Literal prompt diffs in prompt_diff_audit.md change only the dossier heading. Fact text, source tag, statement location, blank-line spacing, downstream record order and injected state are held fixed. Heading length and perceived authority/freshness are not separately manipulated or isolated.

4. Exact Cp→C cases: []; C→Cp cases: []. All transitions, including other outputs, appear in metrics.json.

5. Wrong supporting evidence: W-CURRENT PR=12/12; S0 PR=9/12; G-CURRENT PR=0/12. This content-control contrast is distinct from the heading-only pair.

6. Reverse direction: C-WCURRENT induced wrong 12/12; paired C0 gold→wrong flips {'count': 9, 'denominator': 12, 'rate': 0.75}. Symmetry is not assumed.

7. Every category and denominator is shown below; valid-parse-only rates are in metrics.json.

| Condition | Cp | C | Other | Unknown | Invalid | Valid parses |
|---|---|---|---|---|---|---|
| S0 | 9/12 | 3/12 | 0/12 | 0/12 | 0/12 | 12/12 |
| G-CURRENT | 0/12 | 12/12 | 0/12 | 0/12 | 0/12 | 12/12 |
| G-BACKGROUND | 0/12 | 12/12 | 0/12 | 0/12 | 0/12 | 12/12 |
| W-CURRENT | 12/12 | 0/12 | 0/12 | 0/12 | 0/12 | 12/12 |
| C0 | 2/12 | 9/12 | 0/12 | 1/12 | 0/12 | 11/12 |
| C-WCURRENT | 12/12 | 0/12 | 0/12 | 0/12 | 0/12 | 12/12 |


8. These responses can establish behavioral sensitivity to supplied state, evidence and these role headings when validity gates pass. They do not identify internal attention, beliefs, or a specific computational mechanism.

9. The intervention is an externally injected erroneous state with explicit source-backed downstream mappings. PR measures propagation under this prompt intervention; it is not spontaneous hallucination incidence or natural end-to-end snowballing.

10. STOP this label pilot. No qualifying task-role signal was obtained. Do not search new labels or orderings inside this experiment; any redesigned intervention needs external design review and a separate preregistration.

Final recommendation: **STOP_INVALID**. With 12 cases, absence of discordance is not proof of equivalence, and the null cannot falsify logical relevance or authority effects generally.

## Interpretation gate

**STOP_INVALID: C0 accuracy is 9/12, below the frozen 10/12 minimum.** S0 PR is 9/12 and passes its 8/12 minimum. All 16 independent auxiliary checks passed, but this does not rescue the failed main state-adherence control. No cases were replaced and no prompts or thresholds were revised.

Both framing arms returned C in 12/12 cases (ΔOR=0/12; ΔPR=0/12; 12 unchanged-C pairs; 0 strict discordances). This is a descriptive output pattern, not a clean mechanistic task-role test. The `evidence_dominance` flag records those counts only. No evidence for these headings as a moderator was obtained.

The failed C0 cases were:

```json
[
  {
    "case_id": "v351-04",
    "gold": "Rēzekne",
    "supplied": "Fridrikh Ermler",
    "raw": "Unknown",
    "outcome": "UNKNOWN"
  },
  {
    "case_id": "v351-03",
    "gold": "Rēzekne",
    "supplied": "Fridrikh Ermler",
    "raw": "Düsseldorf",
    "outcome": "INDUCED_WRONG"
  },
  {
    "case_id": "v351-10",
    "gold": "Xi'an",
    "supplied": "Feng Xiaoning",
    "raw": "Düsseldorf",
    "outcome": "INDUCED_WRONG"
  }
]
```

No framing confirmation or new label search is recommended from this run. If a new design is externally approved, its prerequisite would be an independently validated state-adherence assay; that is not an additional experiment in this pilot.
