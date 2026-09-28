"""Read-only local SHARS import. Stage one uses an explicit oracle correction."""
import os
import sys
import time
from pathlib import Path


class SharAdapter:
    def __init__(self, repo, model="qwen3-0.6b", seed=42):
        repo = Path(repo).resolve()
        if not (repo / "LLM.py").is_file():
            raise ValueError("--shar-repo must contain the original LLM.py")
        os.environ.setdefault("NLTK_DATA", str(repo / ".cache/nltk_data"))
        os.environ.setdefault("HF_HOME", str(repo / ".cache/huggingface"))
        os.environ.setdefault("WANDB_MODE", "offline")
        sys.path.insert(0, str(repo))
        import torch
        import LLM
        self.torch = torch
        self.model = LLM.get_model(model, "cuda" if torch.cuda.is_available() else "cpu")
        self.seed = seed

    def generate(self, prompt, seed=None):
        self.torch.manual_seed(self.seed if seed is None else seed)
        formatted = self.model.format_messages(user_prompt=prompt, thinking=False)
        inputs, _ = self.model.tokenize(formatted)
        start = time.perf_counter()
        with self.torch.inference_mode():
            raw, tokens = self.model.complete(user_prompt=prompt, thinking=False,
                return_tokens=True, max_new_tokens=192, temperature=0.7, top_p=0.8, top_k=20)
        return {"raw_generation": raw, "input_tokens": inputs.shape[1],
                "output_tokens": tokens.numel(), "latency_seconds": time.perf_counter() - start}

    def score_segment(self, segment, context):
        # No proxy score presented as HalluSE. Enable only in a later validated phase.
        return None

    def reject_and_resample(self, context, segment, *, oracle_fact):
        return {"rejected_segment": segment, "resampled_segment": oracle_fact,
                "intervention_method": "oracle_correction", "uncertainty_score": None,
                "rejection_score": None, "replacement_origin": "dataset_evidence"}
