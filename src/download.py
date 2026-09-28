"""Download the official April 2021 dataset archive and extract only dev.json."""
import argparse
import urllib.request
import zipfile
from pathlib import Path


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--directory", default="data")
    args = p.parse_args()
    root = Path(args.directory)
    root.mkdir(parents=True, exist_ok=True)
    archive = root / "source.zip"
    if not archive.exists():
        urllib.request.urlretrieve("https://www.dropbox.com/s/ms2m13252h6xubs/data_ids_april7.zip?dl=1", archive)
    with zipfile.ZipFile(archive) as z:
        (root / "dev.json").write_bytes(z.read("dev.json"))
