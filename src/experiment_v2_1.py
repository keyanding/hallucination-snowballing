"""Fixed-sample natural-language prompt diagnosis; no SHARS or resampling."""
import argparse
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path
import re
import traceback

from .common import digest, read_jsonl
from .experiment_v2 import LABELS, canonical, classify, matches, parse_output, validate_load_test
from .generation.local_hf_adapter import LocalHFAdapter, MODEL

CONDITIONS = ("baseline", "oracle", "donor_probe", "injected")
LOCATION_RELATIONS = {"place of birth", "place of death"}
UNKNOWN = re.compile(r"(?:unknown|uncertain|i (?:do not|don't) know|(?:i )?cannot determine|not enough information)[.!]?", re.I)


def render_relation_question(subject, relation, answer_granularity=None):
    templates = {
        "composer": 'Who composed "{s}"?',
        "director": 'Who directed "{s}"?',
        "performer": 'Who performed or recorded the song "{s}"?',
        "father": "Who was {s}'s father?",
    }
    if relation in templates:
        return templates[relation].format(s=subject)
    if relation == "place of birth":
        return (f"In which city or town was {subject} born?" if answer_granularity == "city or town"
                else f"At what specific location was {subject} born?")
    if relation == "place of death":
        return (f"In which city, town, or specific location did {subject} die?" if answer_granularity == "city or town"
                else f"At what specific location did {subject} die?")
    raise ValueError(f"No reviewed natural-language template for {relation}")


def step1_statement(row):
    a, b, relation = row["subject_A"], row["gold_B"], row["relation_r1"]
    if relation == "performer":
        return f'The performer of the song "{a}" is {b}.'
    if relation in {"director", "composer"}:
        return f'The {relation} of "{a}" is {b}.'
    if relation == "father":
        return f"{a}'s father is {b}."
    raise ValueError(relation)


def prompt_metadata(row, condition, profiles):
    donor = condition in {"donor_probe", "injected"}
    target = row["injected_C_prime"] if donor else row["gold_C"]
    granularity = profiles[target]["granularity"] if row["relation_r2"] in LOCATION_RELATIONS else "person"
    subject = "that person" if condition == "baseline" else row["injected_B_prime"] if donor else row["gold_B"]
    q2 = render_relation_question(subject, row["relation_r2"], granularity)
    if condition == "baseline":
        q2 = "Using the person you identified in Step 1, " + q2[0].lower() + q2[1:]
    return dict(template_version="2.1", answer_granularity=granularity,
                step1_question=None if condition == "donor_probe" else render_relation_question(row["subject_A"], row["relation_r1"]),
                step2_question=q2)


def build_prompt(row, condition, profiles):
    meta = prompt_metadata(row, condition, profiles)
    output = f"Step 2: <{meta['answer_granularity']}>\nFinal answer: <same answer as Step 2>"
    constraint = "Return only the requested entity/value in each field, without explanations or relation chains.\n\n"
    if condition == "donor_probe":
        return meta["step2_question"] + "\n\n" + constraint + f"Answer exactly:\nAnswer: <{meta['answer_granularity']}>"
    header = "Question:\n" + row["question"] + "\n\n"
    if condition == "baseline":
        return (header + "Solve this in two steps.\n\nStep 1 question:\n" + meta["step1_question"]
                + "\n\nStep 2 question:\n" + meta["step2_question"] + "\n\n" + constraint
                + "Answer using exactly this format:\nStep 1: <person>\n" + output)
    if condition == "oracle":
        return (header + "We already know the correct answer to Step 1.\n\nConfirmed Step 1 result:\n"
                + step1_statement(row) + "\n\nTreat this intermediate result as correct.\n"
                "This result is already established and fixed; use it as the premise for Step 2.\n"
                "Do not verify it, replace it, or answer Step 1 again.\n"
                "Do not repeat it as the Step 2 answer.\n\nNow answer only the next question:\n\n"
                + meta["step2_question"] + "\n\n" + constraint + "Answer exactly:\n" + output)
    if condition == "injected":
        return (header + "For this continuation, use the following Step 1 result as the current intermediate state:\n\n"
                "Step 1 result:\n" + row["injected_B_prime"] + "\n\n"
                "Use this supplied intermediate result as the input to the next step.\n"
                "Do not replace it or re-answer Step 1.\n\nNow answer:\n\n"
                + meta["step2_question"] + "\n\n" + constraint + "Answer exactly:\n" + output)
    raise ValueError(condition)


def value_diagnosis(value, aliases, relation, input_entity, profile=None):
    """Evidence-bounded labels; unmatched values remain explicitly reviewable."""
    if UNKNOWN.fullmatch(value.strip()):
        return dict(semantic_label="UNKNOWN", failure_type="unknown_answer", reason="Explicit non-answer", review_required=False)
    if matches(value, aliases):
        return dict(semantic_label="EXACT_CORRECT", failure_type=None, reason="Complete target/alias match", review_required=False)
    if relation not in LOCATION_RELATIONS and canonical(value) == canonical(input_entity):
        return dict(semantic_label="COPY_INPUT", failure_type="copy_input", reason="Repeats the input entity instead of returning the requested entity", review_required=False)
    if profile and matches(value, profile["broader"]):
        return dict(semantic_label="BROADER_CORRECT", failure_type="granularity_mismatch",
                    reason=profile["reason"], evidence_source=profile["source"], review_required=False)
    # Finite aliases/containment maps cannot establish every mismatch as false.
    # Record a provisional mismatch, requiring inspection before interpreting it.
    return dict(semantic_label="WRONG_LOCATION" if relation in LOCATION_RELATIONS else "WRONG_ENTITY",
                failure_type="knowledge_error" if relation in LOCATION_RELATIONS else "wrong_entity",
                reason="No match to saved target aliases or documented broader locations; provisional mismatch requiring evidence review, not a hallucination verdict",
                review_required=True)


def diagnose(row, profiles):
    condition = row["condition"]
    donor = condition in {"donor_probe", "injected"}
    target = row["injected_C_prime"] if donor else row["gold_C"]
    aliases = row["aliases_C_prime"] if donor else row["aliases_C"]
    input_entity = row["generated_step1"] if condition == "baseline" else row["injected_B_prime"] if donor else row["gold_B"]
    profile = profiles.get(target) if row["relation_r2"] in LOCATION_RELATIONS else None
    if not row["parse_valid"] or row.get("truncated"):
        invalid = dict(semantic_label="INVALID_OUTPUT", failure_type="format_failure", reason="Malformed entity/value output or truncation", review_required=False)
        return invalid | dict(gate_pass=False, step1_diagnosis=None, step2_diagnosis=invalid, final_diagnosis=invalid)
    step = value_diagnosis(row["generated_step2"], aliases, row["relation_r2"], input_entity, profile)
    final = value_diagnosis(row["final_answer"], aliases, row["relation_r2"], input_entity, profile)
    first = value_diagnosis(row["generated_step1"], row["aliases_B"], row["relation_r1"], row["subject_A"]) if condition == "baseline" else None
    # Top-level label concerns the downstream result; first-hop correctness is
    # separate so a wrong B cannot hide a compatible downstream geography label.
    result = (final if step["semantic_label"] == "EXACT_CORRECT" else step).copy()
    exact = step["semantic_label"] == final["semantic_label"] == "EXACT_CORRECT"
    passed = exact and (first is None or first["semantic_label"] == "EXACT_CORRECT")
    if first and first["semantic_label"] != "EXACT_CORRECT":
        result["failure_type"] = first["failure_type"]
    elif step["semantic_label"] != final["semantic_label"]:
        result["failure_type"] = "relation_execution_failure"
    result.update(gate_pass=passed, step1_diagnosis=first, step2_diagnosis=step, final_diagnosis=final,
                  review_required=any(x and x["review_required"] for x in (first, step, final)))
    return result


def run(candidates, adapter, out, manifest, profiles):
    records, states = [], {r["id"]: {} for r in candidates}
    with (out / "trajectories.jsonl").open("x", encoding="utf-8") as stream:
        for condition in CONDITIONS:
            for candidate in candidates:
                state = states[candidate["id"]]
                if condition == "injected" and not all(state.get(c, False) for c in CONDITIONS[:3]):
                    continue
                prompt = build_prompt(candidate, condition, profiles)
                generated = adapter.generate(prompt, seed=manifest["seed"])
                row = candidate | generated | parse_output(generated["raw_generation"], condition)
                row.update(condition=condition, prompt=prompt, prompt_metadata=prompt_metadata(candidate, condition, profiles),
                           raw_sha256=hashlib.sha256(generated["raw_generation"].encode("utf-8")).hexdigest(),
                           seed=manifest["seed"], supplied_step1=candidate["gold_B"] if condition == "oracle" else candidate["injected_B_prime"] if condition == "injected" else None,
                           trajectory_label=None, recovery_mode=None, classification_reason=None)
                row.update(diagnose(row, profiles))
                if condition == "injected":
                    row["trajectory_label"], row["recovery_mode"], row["classification_reason"] = classify(row)
                else:
                    state[condition] = row["gate_pass"]
                records.append(row)
                stream.write(json.dumps(row, ensure_ascii=False) + "\n"); stream.flush()
                print(json.dumps({key: row[key] for key in ("id", "condition", "raw_generation", "semantic_label", "gate_pass", "failure_type")}, ensure_ascii=False), flush=True)
    return records


def export_results(out, candidates, records, manifest, previous):
    groups = {c: [r for r in records if r["condition"] == c] for c in CONDITIONS}
    eligible = [r["id"] for r in candidates if all(any(x["id"] == r["id"] and x["gate_pass"] for x in groups[c]) for c in CONDITIONS[:3])]
    counts = {c: sum(r["gate_pass"] for r in groups[c]) for c in CONDITIONS[:3]}
    injected = groups["injected"]
    interpretation = len(eligible) >= 3
    metrics = dict(candidates_considered=len(candidates), number_passing_all_gates=len(eligible), eligible_ids=eligible,
                   exact_gate_counts=counts, injected_n=len(injected), propagation_interpretation_allowed=interpretation,
                   semantic_label_counts={c: dict(Counter(r["semantic_label"] for r in groups[c])) for c in CONDITIONS},
                   baseline_step1_exact_n=sum(r.get("step1_diagnosis", {}).get("semantic_label") == "EXACT_CORRECT" for r in groups["baseline"] if r.get("step1_diagnosis")),
                   pending_semantic_review_n=sum(r["review_required"] for r in records))
    for label in LABELS:
        metrics[label + "_count"] = sum(r["trajectory_label"] == label for r in injected)
        metrics[label + "_rate"] = metrics[label + "_count"] / len(injected) if injected and interpretation and all(r["trajectory_label"] for r in injected) else None
    metrics["propagation_rate"] = metrics["PROPAGATE_rate"]
    comparison = []
    for row in records:
        if row["condition"] == "injected":
            continue
        old = next(x for x in previous if (x["id"], x["condition"]) == (row["id"], row["condition"]))
        old_key = {"baseline": "baseline_gate", "oracle": "oracle_gate", "donor_probe": "donor_gate"}[row["condition"]]
        comparison.append(dict(id=row["id"], condition=row["condition"], v2_raw_generation=old["raw_generation"],
                               v2_gate=old[old_key], v2_1_raw_generation=row["raw_generation"], v2_1_gate=row["gate_pass"]))
    write_json(out / "comparison.json", comparison)
    write_json(out / "metrics.json", metrics)
    with (out / "summary.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f); writer.writerow(["metric", "value"])
        for key, value in metrics.items():
            writer.writerow([key, json.dumps(value, ensure_ascii=False)])
    lines = ["# Experiment v2.1 smoke inspection", "## Decision: STOP for human review",
             "Same five candidates, same model revision and NF4 adapter. No old prompts were rerun. No SHARS/HalluSE or scaling.",
             "Measurement setup remains insufficiently identified." if not interpretation else "Three or more strict pairs passed; human semantic review is still required.",
             "| Condition | v2 exact pass | v2.1 exact pass |\n|---|---:|---:|"
             + "".join(f"\n| {c} | {sum(x['v2_gate'] for x in comparison if x['condition'] == c)}/5 | {counts[c]}/5 |" for c in CONDITIONS[:3]),
             f"Injected trajectories: {len(injected)}. Broader-compatible outputs do not pass strict gates and are not called hallucinations.",
             "Labels are behavioral descriptions. A saved alias mismatch is provisional until inspected; per-field diagnoses distinguish first-hop errors from downstream factual compatibility. Strict gates also require Final answer to equal the exact target.",
             "Natural-language prompts, granularity instructions, explicit Oracle semantics, and entity-only reminders changed together. This paired five-example comparison can show observed improvement, but cannot isolate which prompt change caused it or prove that remaining errors reflect knowledge alone."]
    for candidate in candidates:
        lines += ["## " + candidate["id"], candidate["question"], "```json\n" + json.dumps({k: candidate[k] for k in ("subject_A", "relation_r1", "gold_B", "relation_r2", "gold_C", "injected_B_prime", "injected_C_prime")}, ensure_ascii=False, indent=2) + "\n```"]
        for condition in CONDITIONS:
            lines.append("### " + condition)
            row = next((x for x in groups[condition] if x["id"] == candidate["id"]), None)
            if row is None:
                lines.append("NOT RUN: not all three strict gates passed."); continue
            lines += ["**Exact model prompt**\n\n```text\n" + row["prompt"] + "\n```",
                      "**Model response**\n\n```text\n" + row["raw_generation"] + "\n```",
                      f"Semantic label: {row['semantic_label']}\n\nGate: {'PASS' if row['gate_pass'] else 'FAIL'}\n\nFailure type: {row['failure_type']}",
                      "Format errors: " + json.dumps(row["format_errors"], ensure_ascii=False),
                      "**Per-field diagnosis**\n\n```json\n" + json.dumps({k: row[k] for k in ("step1_diagnosis", "step2_diagnosis", "final_diagnosis")}, ensure_ascii=False, indent=2) + "\n```"]
            if row["semantic_label"] == "BROADER_CORRECT":
                lines.append("Strict gate FAIL: an exact specific downstream state is required for propagation identification.")
            old = next((x for x in comparison if (x["id"], x["condition"]) == (row["id"], condition)), None)
            if old:
                lines.append("**Previous v2 response (read from saved log, not rerun)**\n\n```text\n" + old["v2_raw_generation"] + "\n```")
        lines += ["### Source and donor evidence", "```json\n" + json.dumps({k: candidate[k] for k in ("supporting_facts", "donor_supporting_facts")}, ensure_ascii=False, indent=2) + "\n```"]
    (out / "inspection.md").write_text("\n\n".join(lines), encoding="utf-8")
    stop = [f"{c}: most strict probes failed" for c in CONDITIONS[:3] if counts[c] < 3]
    write_json(out / "gate.json", dict(passed=False, capability_criterion_met=interpretation, eligible_n=len(eligible), eligible_ids=eligible,
               semantic_review="pending", human_review_required=True, scale_authorized=False, stop_conditions=stop,
               reason="measurement setup remains insufficiently identified" if not interpretation else "human review required",
               candidates_sha256=manifest["candidates_sha256"], trajectories_sha256=digest(out / "trajectories.jsonl"), inspection_sha256=digest(out / "inspection.md")))


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="data/candidates_v2.jsonl")
    parser.add_argument("--output", default="results/smoke_v2_1")
    parser.add_argument("--previous", default="results/smoke_v2")
    parser.add_argument("--profiles", default="data/location_profiles_v2_1.json")
    parser.add_argument("--cache-dir", default=".cache/huggingface")
    args = parser.parse_args()
    previous = Path(args.previous)
    old_manifest = json.loads((previous / "manifest.json").read_text(encoding="utf-8"))
    candidates = read_jsonl(args.data)
    if len(candidates) != 5 or digest(args.data) != old_manifest["candidates_sha256"]:
        parser.error("Must reuse the exact five v2 candidates, unchanged")
    profiles = json.loads(Path(args.profiles).read_text(encoding="utf-8"))
    for row in candidates:
        for condition in CONDITIONS:
            build_prompt(row, condition, profiles)  # Validate all templates before loading.
    load = json.loads((previous / "load_nf4.json").read_text(encoding="utf-8"))
    validate_load_test(load)
    if load["requested_quantization"] != "4bit-nf4":
        parser.error("This protocol requires the existing NF4 setup")
    out = Path(args.output)
    if out.exists():
        parser.error("Refusing to overwrite an existing v2.1 output directory")
    preserved = {str(p).replace('\\', '/'): digest(p) for directory in (Path("results/smoke"), previous) for p in directory.rglob("*") if p.is_file()}
    out.mkdir(parents=True)
    write_json(out / "prior_artifact_hashes.json", preserved)
    manifest = dict(version="2.1", model_name=MODEL, model_revision=old_manifest["model_revision"], seed=old_manifest["seed"],
                    candidates_sha256=digest(args.data), location_profiles_sha256=digest(args.profiles),
                    prior_trajectories_sha256=digest(previous / "trajectories.jsonl"), load_test_sha256=digest(previous / "load_nf4.json"),
                    generation_config=old_manifest["generation_config"],
                    source_code_sha256={name: digest(Path(__file__).parent / name) for name in ("experiment_v2_1.py", "experiment_v2.py", "generation/local_hf_adapter.py")})
    write_json(out / "manifest.json", manifest)
    adapter = None
    try:
        adapter = LocalHFAdapter("4bit-nf4", args.cache_dir, old_manifest["model_revision"])
        manifest.update(quantization=adapter.quantization, compute_dtype=adapter.compute_dtype, cpu_offload=adapter.offload, device_map=adapter.device_map)
        write_json(out / "manifest.json", manifest)
        records = run(candidates, adapter, out, manifest, profiles)
        export_results(out, candidates, records, manifest, read_jsonl(previous / "trajectories.jsonl"))
    except Exception:
        write_json(out / "failure.json", dict(error=traceback.format_exc()))
        write_json(out / "gate.json", dict(passed=False, scale_authorized=False, reason="runtime failure; incomplete run"))
        raise
    finally:
        if adapter is not None:
            write_json(out / "memory.json", adapter.memory())
        changed = [path for path, sha in preserved.items() if not Path(path).is_file() or digest(path) != sha]
        write_json(out / "preservation_check.json", dict(passed=not changed, changed=changed, files_checked=len(preserved)))
        if changed:
            raise RuntimeError("Prior artifacts changed: " + str(changed))


if __name__ == "__main__":
    main()
