import argparse
import json
import random
from pathlib import Path

from huggingface_hub import hf_hub_download

from tinker_hw.utils.io import write_jsonl

DEFAULT_REPO_ID = "cdleong/piglatin-mt"
TRAIN_FILE = "piglatin-mt-train.json"
DEV_FILE = "piglatin-mt-dev.json"


def _load_records(path: str) -> list[dict]:
    # Try normal JSON first (list/dict). If it fails, fall back to JSONL.
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        if isinstance(data, dict) and "data" in data and isinstance(data["data"], list):
            return data["data"]
        if isinstance(data, dict):
            # Some datasets wrap differently; try values if it looks like a dict of records
            # but avoid doing something surprising.
            raise ValueError(
                f"Unexpected JSON dict structure keys={list(data.keys())[:10]}")
    except json.JSONDecodeError:
        rows = []
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                rows.append(json.loads(line))
        return rows


def _extract_pair(r: dict) -> tuple[str, str]:
    # Handle both flat and nested formats.
    if "translation" in r and isinstance(r["translation"], dict):
        t = r["translation"]
        eng = t.get("eng") or t.get("en") or t.get("english")
        pig = t.get("engyay") or t.get("piglatin") or t.get("pig")
    else:
        eng = r.get("eng") or r.get("en") or r.get("english")
        pig = r.get("engyay") or r.get("piglatin") or r.get("pig")
    if not eng or not pig:
        raise KeyError(
            f"Could not find eng/pig fields in record keys={list(r.keys())}")
    return eng, pig


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-id", default=DEFAULT_REPO_ID,
                    help="HF dataset repo id, e.g. cdleong/piglatin-mt")
    ap.add_argument("--sample-n", type=int, default=300)
    ap.add_argument("--full-n", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--out-sample", default="data/piglatin/sample.jsonl")
    ap.add_argument("--out-full", default="data/piglatin/full/piglatin.jsonl")
    args = ap.parse_args()

    train_path = hf_hub_download(
        repo_id=args.repo_id, filename=TRAIN_FILE, repo_type="dataset")
    dev_path = hf_hub_download(
        repo_id=args.repo_id, filename=DEV_FILE, repo_type="dataset")

    rows = _load_records(train_path)

    rng = random.Random(args.seed)
    rng.shuffle(rows)

    def row_to_io(r):
        eng, pig = _extract_pair(r)
        return {
            "input": f"Translate this to Pig Latin:\n{eng}",
            "output": pig,
        }

    sample_rows = [row_to_io(r) for r in rows[: min(args.sample_n, len(rows))]]
    full_rows = [row_to_io(r) for r in rows[: min(args.full_n, len(rows))]]

    write_jsonl(Path(args.out_sample), sample_rows)
    write_jsonl(Path(args.out_full), full_rows)

    print(f"Downloaded: {TRAIN_FILE} -> {train_path}")
    print(f"Downloaded: {DEV_FILE}   -> {dev_path}")
    print(f"Wrote sample: {args.out_sample} rows={len(sample_rows)}")
    print(f"Wrote full:   {args.out_full} rows={len(full_rows)}")


if __name__ == "__main__":
    main()
