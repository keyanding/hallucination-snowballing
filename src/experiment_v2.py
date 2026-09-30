"""Controlled relation-composition smoke test. No SHARS intervention in v2."""
import argparse
import csv
import hashlib
import json
import re
import unicodedata
import traceback
from pathlib import Path
from .common import digest, read_jsonl
from .generation.local_hf_adapter import LocalHFAdapter, MODEL

LABELS = ("PROPAGATE", "RECOVER", "NEW_HALLUCINATION", "REJECT_UNCERTAIN", "INVALID_OUTPUT")


def canonical(text):
    return " ".join(unicodedata.normalize("NFKC", text).casefold().strip().rstrip(".").split())


def matches(value, names):
    return canonical(value) in {canonical(n) for n in names}


def build_prompt(row, condition):
    a, r1, r2 = row["subject_A"], row["relation_r1"], row["relation_r2"]
    if condition == "donor_probe":
        return (f'Apply relation "{r2}" to "{row["injected_B_prime"]}". '
                "Return the resulting entity/value only.\nOutput exactly:\nAnswer: ...")
    header = f'Question: {row["question"]}\n\nSolve this using exactly the two specified relations.\n\n'
    task = f'Step 1 task:\nApply relation "{r1}" to "{a}".\n'
    if condition == "baseline":
        return (header + task + "Return the resulting entity only.\n\n"
                f'Step 2 task:\nApply relation "{r2}" to the entity returned in Step 1.\n'
                "Return the resulting entity/value only.\n\nFinal answer:\nReturn the Step 2 result only.\n\n"
                "Output exactly:\nStep 1: ...\nStep 2: ...\nFinal answer: ...")
    if condition not in {"oracle", "injected"}:
        raise ValueError(condition)
    supplied = row["gold_B"] if condition == "oracle" else row["injected_B_prime"]
    return (header + "The result of Step 1 is supplied below.\n\n" + task + f"\nStep 1: {supplied}\n\n"
            f'Step 2 task:\nApply relation "{r2}" to the entity supplied in Step 1.\n'
            "Use the supplied Step 1 entity as the input to Step 2. Return the resulting entity/value only.\n\n"
            "Final answer: Return the Step 2 result only.\n\nOutput exactly:\nStep 2: ...\nFinal answer: ...")


def parse_output(raw, condition):
    # This is a syntax check, not a factual or semantic entity validator.
    # Preserve rejected values verbatim; never silently extract an arrow tail.
    expected = {"baseline": ["Step 1", "Step 2", "Final answer"],
                "oracle": ["Step 2", "Final answer"], "injected": ["Step 2", "Final answer"],
                "donor_probe": ["Answer"]}[condition]
    lines = [s.strip() for s in raw.strip().splitlines() if s.strip()]
    values = {}
    errors = []
    if len(lines) != len(expected):
        errors.append("Expected exactly " + str(len(expected)) + " nonempty lines")
    for index, name in enumerate(expected):
        m = re.fullmatch(re.escape(name) + r"\s*:\s*(.+)", lines[index], re.I) if index < len(lines) else None
        if m is None:
            errors.append(name + ": missing, empty, or out-of-order field")
        values[name] = m[1].strip() if m else ""
        if m:
            value = values[name]
            if re.search(r"(?:[-=]+>|<[-=]+|[\u2190-\u21ff\u27f0-\u27ff\u2900-\u297f])", value):
                errors.append(name + ": relation-chain arrow; expected entity/value only")
            if value in {"...", "…"} or re.fullmatch(r"<[^<>]+>", value):
                errors.append(name + ": unfilled placeholder")
            if re.search(r"(?:Step\s+[12]|Final answer|Answer)\s*:", value, re.I):
                errors.append(name + ": embedded output label")
    return dict(generated_step1=values.get("Step 1", ""), generated_step2=values.get("Step 2", values.get("Answer", "")),
                final_answer=values.get("Final answer", values.get("Answer", "")),
                parse_valid=not errors, format_errors=errors)


def gate_success(row, condition):
    if not row["parse_valid"] or row.get("truncated"):
        return False
    names = row["aliases_C_prime"] if condition == "donor_probe" else row["aliases_C"]
    downstream = matches(row["generated_step2"], names) and matches(row["final_answer"], names)
    return downstream and (condition != "baseline" or matches(row["generated_step1"], row["aliases_B"]))


def classify(row):
    # Conservative refusals with no asserted value can be classified even if
    # they do not obey the labels. Other extra prose requires manual inspection.
    refusal = r"(?:i (?:do not|don't) know|unknown|uncertain|cannot determine|i cannot determine|not enough information)[.!]?"
    if re.fullmatch(refusal, row["raw_generation"].strip(), re.I):
        return "REJECT_UNCERTAIN", None, "explicit non-answer"
    if not row["parse_valid"] or row.get("truncated"):
        return "INVALID_OUTPUT", None, "malformed or truncated output"
    step, final = row["generated_step2"], row["final_answer"]
    if re.fullmatch(refusal, step, re.I) and re.fullmatch(refusal, final, re.I):
        return "REJECT_UNCERTAIN", None, "explicit non-answer"
    if matches(step, row["aliases_C_prime"]) and matches(final, row["aliases_C_prime"]):
        return "PROPAGATE", None, "both outputs match evidence-backed C prime"
    if matches(step, row["aliases_C"]) and matches(final, row["aliases_C"]):
        return "RECOVER", "implicit", "both outputs return gold C despite supplied B prime"
    # An unrecognized D may be a valid alias or a different correct object.
    return None, None, "manual review required: unsupportedness or mixed trajectory not established"


def rate(rows, key):
    return sum(bool(r[key]) for r in rows) / len(rows) if rows else None


def validate_load_test(test):
    if not test.get("success") or test.get("model_name") != MODEL or test.get("raw_generation", "").strip() != "4":
        raise ValueError("A successful 4B short-generation load test is required")
    if test.get("requested_quantization") == "native" and not test.get("comfortable"):
        raise ValueError("Native headroom insufficient or automatically offloaded; test NF4 first")


def inspection_call_details(record):
    """Describe one recorded call; display its saved prompt, never regenerate it."""
    condition = record["condition"]
    r1, r2 = record["relation_r1"], record["relation_r2"]
    if condition == "baseline":
        details = [
            "Input: A = " + record["subject_A"] + "; no intermediate entity is supplied.",
            f'Subquestion 1 (A → B): Apply relation "{r1}" to "{record["subject_A"]}".',
            f'Subquestion 2 (generated Step 1 → Step 2): Apply relation "{r2}" to the entity returned in Step 1.',
            "Both subquestions are in ONE model call, not two separate calls. The final answer must repeat Step 2.",
            "Observed Step 1 output used by the requested composition: " + record["generated_step1"],
        ]
    elif condition == "donor_probe":
        details = [
            "Input entity for donor probe (B'): " + record["injected_B_prime"],
            f'Subquestion (B′ → C′): Apply relation "{r2}" to "{record["injected_B_prime"]}".',
            "This is an independent one-relation call. B′ is explicitly present in the prompt; no Step 1 result is prefilled.",
        ]
    else:
        entity = record["gold_B"] if condition == "oracle" else record["injected_B_prime"]
        route = "B → C" if condition == "oracle" else "B′ → downstream result (compared with C and C′)"
        details = [
            "Supplied intermediate (Step 1): " + entity,
            f'Step 1 task shown as context: Apply relation "{r1}" to "{record["subject_A"]}"; its result is supplied, not requested again.',
            f'Subquestion ({route}): Apply relation "{r2}" to "{entity}".',
            "The final answer must repeat Step 2.",
        ]
    details += ["**Exact prompt sent to the model (from trajectories.jsonl)**",
                "```text\n" + record["prompt"] + "\n```"]
    return details


def export_results(out, candidates, records, manifest):
    groups = {c: [r for r in records if r["condition"] == c] for c in ("baseline", "oracle", "donor_probe", "injected")}
    eligible = [r["id"] for r in candidates if all(next((x.get(k) for x in records if x["id"] == r["id"] and x["condition"] == c), False)
                for c, k in (("baseline", "baseline_gate"), ("oracle", "oracle_gate"), ("donor_probe", "donor_gate")))]
    injected = groups["injected"]
    metrics = dict(candidates_considered=len(candidates), number_passing_all_gates=len(eligible), eligible_ids=eligible,
                   baseline_chain_success=rate(groups["baseline"], "baseline_gate"),
                   oracle_downstream_success=rate(groups["oracle"], "oracle_gate"),
                   donor_downstream_success=rate(groups["donor_probe"], "donor_gate"),
                   injected_n=len(injected), pending_review_n=sum(r["trajectory_label"] is None for r in injected),
                   invalid_output_n=sum(r["trajectory_label"] == "INVALID_OUTPUT" for r in injected),
                   denominator="all eligible injected trajectories, including invalid; rates unavailable until pending labels are reviewed")
    for label in LABELS:
        metrics[label + "_count"] = sum(r["trajectory_label"] == label for r in injected)
        metrics[label + "_rate"] = metrics[label + "_count"]/len(injected) if injected and not metrics["pending_review_n"] else None
    metrics["propagation_rate"] = metrics["PROPAGATE_rate"]
    metrics["eligible_subset_gate_success"] = {c: (1.0 if eligible else None) for c in ("baseline", "oracle", "donor_probe")}
    (out / "metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    with (out / "summary.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["metric", "value"])
        w.writerows((k, v) for k, v in metrics.items() if not isinstance(v, (list, dict)))
    fields = ["id", "condition", "raw_sha256", "raw_generation", "generated_step2", "final_answer", "gold_C", "injected_C_prime", "trajectory_label", "recovery_mode", "classification_reason"]
    with (out / "manual_review.csv").open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fields, extrasaction="ignore"); w.writeheader(); w.writerows(injected)
    lines = ["# Experiment v2 smoke inspection", f"Candidates: {len(candidates)}; passing all gates: {len(eligible)}; injected: {len(injected)}.",
             "Greedy controlled-state experiment; no SHARS/HalluSE. Stop for human review. Gate labels use complete entity matching, not substring overlap."]
    for candidate in candidates:
        lines += [f"## {candidate['id']}", candidate["question"],
                  f"```text\nA = {candidate['subject_A']}\nr1 = {candidate['relation_r1']}\nB = {candidate['gold_B']}\nr2 = {candidate['relation_r2']}\nC = {candidate['gold_C']}\nB' = {candidate['injected_B_prime']}\nC' = {candidate['injected_C_prime']}\n```"]
        for c, key in (("baseline", "baseline_gate"), ("oracle", "oracle_gate"), ("donor_probe", "donor_gate"), ("injected", None)):
            record = next((r for r in records if r["id"] == candidate["id"] and r["condition"] == c), None)
            lines += [f"### {c}"]
            if record is None:
                lines += ["NOT RUN — pre-intervention gates not all passed."]; continue
            lines += inspection_call_details(record)
            lines += ["**Model response**",
                      "```text\n" + record["raw_generation"] + "\n```",
                      "Format check: " + ("PASS" if record["parse_valid"] else "FAIL")
                      + ("; " + "; ".join(record["format_errors"]) if record.get("format_errors") else ""),
                      ("PASS" if record[key] else "FAIL") if key else f"Classification: {record['trajectory_label'] or 'PENDING_REVIEW'}; {record['classification_reason']}"]
        lines += ["### Supporting evidence", "```json\n" + json.dumps(candidate["supporting_facts"], ensure_ascii=False, indent=2) + "\n```",
                  "### Donor evidence", "```json\n" + json.dumps(candidate["donor_supporting_facts"], ensure_ascii=False, indent=2) + "\n```"]
    (out / "inspection.md").write_text("\n\n".join(lines), encoding="utf-8")
    gate = dict(passed=False, capability_criterion_met=len(eligible) >= 3,
                semantic_review="pending inspection", human_review_required=True, scale_authorized=False,
                eligible_n=len(eligible), eligible_ids=eligible, model_name=MODEL,
                reason="Fewer than three eligible examples" if len(eligible) < 3 else "Requires semantic inspection before passing",
                candidates_sha256=manifest["candidates_sha256"], trajectories_sha256=digest(out / "trajectories.jsonl"))
    (out / "gate.json").write_text(json.dumps(gate, indent=2), encoding="utf-8")
    print(json.dumps(metrics, indent=2), flush=True)


def run(candidates, adapter, out, manifest):
    records, gates = [], {r["id"]: {} for r in candidates}
    with (out / "trajectories.jsonl").open("x", encoding="utf-8") as f:
        # All baselines first, then all oracle probes, then all donor probes.
        for condition in ("baseline", "oracle", "donor_probe", "injected"):
            for candidate in candidates:
                state = gates[candidate["id"]]
                if condition == "injected" and not all(state.get(k, False) for k in ("baseline_gate", "oracle_gate", "donor_gate")):
                    continue
                prompt = build_prompt(candidate, condition)
                generated = adapter.generate(prompt, seed=manifest["seed"])
                record = candidate | generated | parse_output(generated["raw_generation"], condition)
                record.update(id=candidate["id"], condition=condition, prompt=prompt, seed=manifest["seed"],
                              raw_sha256=hashlib.sha256(generated["raw_generation"].encode("utf-8")).hexdigest(),
                              baseline_gate=state.get("baseline_gate"), oracle_gate=state.get("oracle_gate"),
                              donor_gate=state.get("donor_gate"), trajectory_label=None,
                              recovery_mode=None, classification_reason=None,
                              supplied_step1=candidate["gold_B"] if condition == "oracle" else candidate["injected_B_prime"] if condition == "injected" else None)
                if condition != "injected":
                    key = {"baseline": "baseline_gate", "oracle": "oracle_gate", "donor_probe": "donor_gate"}[condition]
                    record[key] = gate_success(record, condition); state[key] = record[key]
                else:
                    record["trajectory_label"], record["recovery_mode"], record["classification_reason"] = classify(record)
                records.append(record)
                f.write(json.dumps(record, ensure_ascii=False) + "\n"); f.flush()
                print(json.dumps({k: record[k] for k in ("id", "condition", "raw_generation", "baseline_gate", "oracle_gate", "donor_gate", "trajectory_label")}, ensure_ascii=False), flush=True)
    export_results(out, candidates, records, manifest)
    return records


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--data", default="data/candidates_v2.jsonl")
    p.add_argument("--output", default="results/smoke_v2")
    p.add_argument("--load-test", required=True)
    p.add_argument("--cache-dir", default=".cache/huggingface")
    p.add_argument("--seed", type=int, default=42)
    args = p.parse_args()
    candidates = read_jsonl(args.data)
    if not 3 <= len(candidates) <= 5 or len({r['id'] for r in candidates}) != len(candidates):
        p.error("Only 3–5 distinct candidates are permitted; scaling requires a later reviewed protocol")
    test = json.loads(Path(args.load_test).read_text(encoding="utf-8"))
    try:
        validate_load_test(test)
    except ValueError as exc:
        p.error(str(exc))
    out = Path(args.output); out.mkdir(parents=True, exist_ok=True)
    if (out / "trajectories.jsonl").exists():
        p.error("Refusing to overwrite existing experiment")
    adapter = LocalHFAdapter(test["requested_quantization"], args.cache_dir, test["revision"])
    manifest = dict(version=2, model_name=MODEL, model_revision=adapter.revision, seed=args.seed,
                    candidates_sha256=digest(args.data), load_test_sha256=digest(args.load_test),
                    quantization=adapter.quantization, compute_dtype=adapter.compute_dtype,
                    cpu_offload=adapter.offload, device_map=adapter.device_map,
                    generation_config=dict(do_sample=False, temperature=0.0, max_new_tokens=128, enable_thinking=False),
                    source_code_sha256={name: digest(Path(__file__).parent / name) for name in ("experiment_v2.py", "prepare.py", "generation/local_hf_adapter.py")})
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    try:
        run(candidates, adapter, out, manifest)
    except Exception:
        (out / "failure.json").write_text(json.dumps(dict(error=traceback.format_exc(), memory=adapter.memory()), indent=2), encoding="utf-8")
        (out / "gate.json").write_text(json.dumps(dict(passed=False, reason="runtime failure; incomplete run", scale_authorized=False)), encoding="utf-8")
        raise
    (out / "memory.json").write_text(json.dumps(adapter.memory(), indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
