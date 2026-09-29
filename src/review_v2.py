"""Apply explicit evidence-backed classification reviews without changing raw logs."""
import argparse
import hashlib
import json
from pathlib import Path
from .common import digest, read_jsonl, write_jsonl
from .experiment_v2 import LABELS, export_results


def apply_reviews(records, reviews):
    indexed = {r["id"]: r for r in records if r["condition"] == "injected"}
    for review in reviews:
        row = indexed[review["id"]]
        if review["raw_sha256"] != hashlib.sha256(row["raw_generation"].encode("utf-8")).hexdigest():
            raise ValueError("Review does not match raw generation")
        if review["label"] not in LABELS or not review.get("reviewer") or not review.get("rationale"):
            raise ValueError("Review requires a valid label, reviewer, and rationale")
        if review["label"] == "NEW_HALLUCINATION" and not review.get("unsupportedness_evidence"):
            raise ValueError("Different strings alone do not establish a new hallucination")
        if review["label"] == "RECOVER" and review.get("recovery_mode") not in {"explicit", "implicit"}:
            raise ValueError("Recovery review requires explicit/implicit mode")
        row.update(trajectory_label=review["label"], recovery_mode=review.get("recovery_mode"),
                   classification_reason=review["rationale"], review=review)
    return records


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--run-dir", default="results/smoke_v2")
    p.add_argument("--data", default="data/candidates_v2.jsonl")
    p.add_argument("--reviews", required=True, help="JSONL: id, raw_sha256, label, reviewer, rationale; optional recovery_mode/unsupportedness_evidence")
    args = p.parse_args()
    root = Path(args.run_dir)
    manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    if digest(args.data) != manifest["candidates_sha256"]:
        raise ValueError("Candidate data changed since the run")
    records = apply_reviews(read_jsonl(root / "trajectories.jsonl"), read_jsonl(args.reviews))
    write_jsonl(root / "reviewed_trajectories.jsonl", records)
    export_results(root, read_jsonl(args.data), records, manifest)
