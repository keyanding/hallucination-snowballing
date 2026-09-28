import argparse
import json
import re
import subprocess
from pathlib import Path
from .common import digest, read_jsonl
from .generation.shar_adapter import SharAdapter

CONDITIONS = ("baseline", "injected_error", "rejection")


def parse(raw, fixed=None):
    labels = list(re.finditer(r"(?im)^\s*(Step\s*1|Step\s*2|Final answer)\s*:\s*", raw))
    values = {}
    for i, match in enumerate(labels):
        key = re.sub(r"\s+", " ", match[1].lower())
        values[key] = raw[match.end():labels[i+1].start() if i+1 < len(labels) else len(raw)].strip()
    return {"generated_hop1": fixed if fixed is not None else values.get("step 1", ""),
            "generated_hop2": values.get("step 2", ""), "final_answer": values.get("final answer", ""),
            "parse_valid": len(labels) == (3 if fixed is None else 2)
                           and all(values.get(k) for k in (["step 1"] if fixed is None else []) + ["step 2", "final answer"])}


def prompt(row, fixed=None):
    base = f"Question: {row['question']}\n\nReason step by step using exactly two factual steps. "
    if fixed is None:
        return base + "Output exactly these labeled lines:\nStep 1: <first fact>\nStep 2: <dependent fact>\nFinal answer: <short answer>"
    return base + f"Continue the supplied reasoning. Output only Step 2 and Final answer with those labels.\n\nStep 1: {fixed}\n\nStep 2:"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--data", default="data/pilot.jsonl")
    p.add_argument("--output", default="results/smoke/trajectories.jsonl")
    p.add_argument("--shar-repo", required=True)
    p.add_argument("--model", default="qwen3-0.6b")
    p.add_argument("--n", type=int, default=3)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--smoke-gate")
    args = p.parse_args()
    if args.n != 3 and not 30 <= args.n <= 50:
        p.error("Use a 3-example smoke test or a 30–50 example pilot")
    if args.n > 3:
        if not args.smoke_gate:
            p.error("Full run requires --smoke-gate after semantic inspection")
        gate = json.loads(Path(args.smoke_gate).read_text(encoding="utf-8"))
        smoke = Path(gate["trajectories_path"])
        if not (gate.get("passed") is True and gate.get("reviewer") and gate.get("notes")
                and gate.get("dataset_sha256") == digest(args.data)
                and gate.get("trajectories_sha256") == digest(smoke)
                and gate.get("model") == args.model):
            p.error("Invalid, failed, or stale semantic smoke gate")
        rows = read_jsonl(smoke)
        if len(rows) != 9 or not all(r["parse_valid"] for r in rows):
            p.error("Smoke trajectories are incomplete or malformed")
    rows = read_jsonl(args.data)
    if len(rows) < args.n:
        p.error("Insufficient prepared examples")
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        p.error("Output already exists; use a new run directory")
    adapter = SharAdapter(args.shar_repo, args.model, args.seed)
    metadata = vars(args) | {"dataset_sha256": digest(args.data), "shar_commit": subprocess.check_output(
        ["git", "-C", args.shar_repo, "rev-parse", "HEAD"], text=True).strip(),
        "temperature": 0.7, "top_p": 0.8, "top_k": 20, "max_new_tokens": 192,
        "model_commit": getattr(adapter.model.model.config, "_commit_hash", None),
        "stage": "oracle_correction", "evidence_in_prompt": False}
    target.with_suffix(".manifest.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    with target.open("x", encoding="utf-8") as stream:
        for index, row in enumerate(rows[:args.n]):
            for condition in CONDITIONS:
                fixed = None if condition == "baseline" else row["injected_hop1"]
                intervention = {"rejected_segment": None, "resampled_segment": None,
                                "uncertainty_score": None, "rejection_score": None,
                                "intervention_method": None}
                if condition == "rejection":
                    intervention = adapter.reject_and_resample(row["question"], fixed, oracle_fact=row["hop1_gold"])
                    fixed = intervention["resampled_segment"]
                text = prompt(row, fixed)
                generated = adapter.generate(text, args.seed + index)
                result = row | generated | parse(generated["raw_generation"], fixed) | intervention
                result.update(condition=condition, prompt=text, gold_hop1=row["hop1_gold"], seed=args.seed+index)
                stream.write(json.dumps(result, ensure_ascii=False) + "\n")
                stream.flush()
                print(json.dumps({k: result[k] for k in ("id", "question", "condition", "generated_hop1", "raw_generation", "parse_valid")}, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
