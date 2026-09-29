"""V2 local HF inference; independent of the original SHARS implementation."""
import argparse
import json
import time
import traceback
from pathlib import Path

MODEL = "Qwen/Qwen3-4B-Instruct-2507"


class LocalHFAdapter:
    def __init__(self, quantization="native", cache_dir=None, revision=None):
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
        self.torch = torch
        self.requested_quantization = quantization
        self.quantization = quantization
        self.compute_dtype = "auto"
        args = dict(device_map="auto", trust_remote_code=True, cache_dir=cache_dir, revision=revision)
        if torch.cuda.is_available():
            torch.cuda.reset_peak_memory_stats()
        if quantization == "4bit-nf4":
            import bitsandbytes as bnb
            # A real CUDA quantize/dequantize check, not merely an import check.
            x = torch.randn(128, device="cuda", dtype=torch.float16)
            packed, state = bnb.functional.quantize_4bit(x, quant_type="nf4")
            bnb.functional.dequantize_4bit(packed, state)
            dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
            self.compute_dtype = str(dtype)
            args["quantization_config"] = BitsAndBytesConfig(load_in_4bit=True,
                bnb_4bit_quant_type="nf4", bnb_4bit_compute_dtype=dtype, bnb_4bit_use_double_quant=True)
        else:
            args["torch_dtype"] = "auto"
            if quantization == "cpu-offload":
                args["max_memory"] = {0: "5GiB", "cpu": "20GiB"}
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL, cache_dir=cache_dir, revision=revision, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(MODEL, **args).eval()
        self.device_map = {k: str(v) for k, v in getattr(self.model, "hf_device_map", {}).items()}
        self.offload = any(v in {"cpu", "disk"} for v in self.device_map.values())
        if quantization == "native" and self.offload:
            self.quantization = "cpu-offload"
        if self.compute_dtype == "auto":
            self.compute_dtype = str(self.model.dtype)
        self.revision = getattr(self.model.config, "_commit_hash", None)

    def memory(self):
        tc = self.torch
        if not tc.cuda.is_available():
            return {}
        free, total = tc.cuda.mem_get_info()
        return dict(peak_allocated_bytes=tc.cuda.max_memory_allocated(),
                    peak_reserved_bytes=tc.cuda.max_memory_reserved(), free_bytes=free, total_bytes=total)

    def generate(self, prompt, seed=None, max_new_tokens=128):
        tc = self.torch
        tc.manual_seed(42 if seed is None else seed)
        formatted = self.tokenizer.apply_chat_template([{"role": "user", "content": prompt}],
            tokenize=False, add_generation_prompt=True, enable_thinking=False)
        inputs = self.tokenizer(formatted, return_tensors="pt").to(self.model.device)
        if tc.cuda.is_available():
            tc.cuda.synchronize()
        start = time.perf_counter()
        with tc.inference_mode():
            output = self.model.generate(**inputs, do_sample=False, temperature=None, top_p=None,
                top_k=None, max_new_tokens=max_new_tokens, pad_token_id=self.tokenizer.eos_token_id)
        if tc.cuda.is_available():
            tc.cuda.synchronize()
        new = output[0, inputs.input_ids.shape[1]:]
        return dict(raw_generation=self.tokenizer.decode(new, skip_special_tokens=True),
                    input_tokens=inputs.input_ids.shape[1], output_tokens=new.numel(),
                    latency_seconds=time.perf_counter()-start, model_name=MODEL,
                    quantization=self.quantization, compute_dtype=self.compute_dtype,
                    truncated=bool(new.numel() >= max_new_tokens and new[-1].item() != self.tokenizer.eos_token_id))


def load_test():
    p = argparse.ArgumentParser()
    p.add_argument("--quantization", choices=["native", "4bit-nf4", "cpu-offload"], default="native")
    p.add_argument("--cache-dir")
    p.add_argument("--output", required=True)
    args = p.parse_args()
    target = Path(args.output)
    if target.exists():
        p.error("Load test already recorded; do not repeat a failed configuration")
    target.parent.mkdir(parents=True, exist_ok=True)
    result = dict(requested_quantization=args.quantization, model_name=MODEL)
    try:
        adapter = LocalHFAdapter(args.quantization, args.cache_dir)
        result.update(adapter.generate("What is 2 + 2? Return only the number.", max_new_tokens=8))
        result.update(adapter.memory(), device_map=adapter.device_map, revision=adapter.revision,
                      cpu_offload=adapter.offload, success=True)
        result["comfortable"] = (not adapter.offload and result.get("free_bytes", 0) >= 1024**3)
    except Exception:
        result.update(success=False, comfortable=False, error=traceback.format_exc())
        import torch
        if torch.cuda.is_available():
            result.update(peak_allocated_bytes=torch.cuda.max_memory_allocated(),
                          peak_reserved_bytes=torch.cuda.max_memory_reserved())
    target.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2), flush=True)


if __name__ == "__main__":
    load_test()
