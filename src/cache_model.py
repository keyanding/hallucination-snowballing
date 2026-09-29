"""Fallback for proxies that stall full multi-GB downloads; SHA-256 verified."""
import argparse
import hashlib
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import threading
from pathlib import Path
import requests
from .generation.local_hf_adapter import MODEL


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--cache-dir", default=".cache/huggingface")
    p.add_argument("--source", choices=["huggingface", "modelscope"], default="huggingface")
    p.add_argument("--workers", type=int, default=16)
    args = p.parse_args()
    response = requests.get(f"https://huggingface.co/api/models/{MODEL}?blobs=true", timeout=30)
    response.raise_for_status()
    meta = response.json()
    revision = meta["sha"]
    root = Path(args.cache_dir) / ("models--" + MODEL.replace("/", "--"))
    snapshot = root / "snapshots" / revision
    snapshot.mkdir(parents=True, exist_ok=True)
    files = [s for s in meta["siblings"] if s["rfilename"].endswith(".safetensors")]
    def download(entry):
        name = entry["rfilename"]
        target = snapshot / name
        expected = entry["lfs"]["sha256"]
        size = entry["lfs"]["size"]
        partial = target.with_suffix(".part")
        if target.exists():
            with target.open("rb") as existing:
                if hashlib.file_digest(existing, "sha256").hexdigest() == expected:
                    return
        chunk_dir = root / "range_chunks" / name
        chunk_dir.mkdir(parents=True, exist_ok=True)
        block_size = 1024**2
        url = (f"https://huggingface.co/{MODEL}/resolve/main/{name}" if args.source == "huggingface"
               else f"https://modelscope.cn/models/{MODEL}/resolve/master/{name}")
        # Resolve the official CDN once; keep signed URLs in memory only.
        with requests.get(url, headers={"Range": "bytes=0-0"}, stream=True, timeout=(10, 20)) as probe:
            probe.raise_for_status()
            download_url = probe.url
        local = threading.local()
        def block(start):
                end = min(start + block_size, size) - 1
                chunk = chunk_dir / str(start)
                if chunk.exists() and chunk.stat().st_size == end-start+1:
                    return
                if not hasattr(local, "session"):
                    local.session = requests.Session()
                for attempt in range(3):
                    try:
                        with local.session.get(download_url, headers={"Range": f"bytes={start}-{end}"},
                                               stream=True, timeout=(10, 20)) as r:
                            r.raise_for_status()
                            if r.status_code != 206 or r.headers.get("Content-Range") != f"bytes {start}-{end}/{size}":
                                raise RuntimeError(f"Invalid range response for {name} at {start}")
                            content = r.content
                            if len(content) != end-start+1:
                                raise RuntimeError("Incomplete range")
                        break
                    except requests.RequestException:
                        if attempt == 2:
                            raise
                        time.sleep(1)
                chunk.write_bytes(content)
        starts = range(0, size, block_size)
        with ThreadPoolExecutor(max_workers=args.workers) as workers:
            jobs = [workers.submit(block, start) for start in starts]
            failures = []
            for count, job in enumerate(as_completed(jobs), 1):
                try:
                    job.result()
                except Exception as exc:
                    failures.append(type(exc).__name__)
                if count % 64 == 0 or count == len(jobs):
                    print(f"{name}: {count}/{len(jobs)} verified-range blocks", flush=True)
            if failures:
                raise RuntimeError(f"{name}: {len(failures)} blocks failed ({set(failures)}); rerun to resume")
        with partial.open("wb") as f:
            for start in starts:
                f.write((chunk_dir / str(start)).read_bytes())
        with partial.open("rb") as f:
            actual = hashlib.file_digest(f, "sha256").hexdigest()
        if actual != expected:
            raise RuntimeError(f"SHA-256 mismatch: {name}")
        partial.replace(target)
        print(f"Verified {name}: {actual}", flush=True)
    with ThreadPoolExecutor(max_workers=3) as executor:
        list(executor.map(download, files))
    (root / "refs").mkdir(exist_ok=True)
    (root / "refs/main").write_text(revision, encoding="utf-8")
    print(json.dumps({"revision": revision, "verified_shards": len(files)}), flush=True)


if __name__ == "__main__":
    main()
