#!/usr/bin/env python3
"""Sync board bills-of-materials from the BeeHive hardware repo's Kitspace config.

The BeeHive PCB repo (github.com/BeeHive-org/BeeHive) ships a `kitspace.yaml`
manifest listing each board project and the path to its `1-click-bom.csv`. This
script fetches that manifest and every referenced BOM CSV and vendors them into
data/kitspace/, so the docs build stays offline and reproducible:

    data/kitspace/manifest.yaml        # a copy of the repo's kitspace.yaml
    data/kitspace/bom/<project>.csv    # one BOM per project

Run it occasionally (or when the hardware changes) with `uv run poe sync`, then
commit the result. build_ingredients.py reads this vendored cache to render the
Bill of materials on each board's page; if the cache is absent it simply skips
BOMs, so `gen` never needs the network.
"""

from __future__ import annotations

import sys
import urllib.error
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = ROOT / "data" / "kitspace"
BOM_DIR = CACHE_DIR / "bom"

REPO = "BeeHive-org/BeeHive"
BRANCH = "master"
RAW = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}"
MANIFEST_URL = f"{RAW}/kitspace.yaml"


def fetch(url: str) -> bytes | None:
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            return resp.read()
    except urllib.error.HTTPError as e:
        print(f"  ! {e.code} fetching {url}", file=sys.stderr)
    except (urllib.error.URLError, TimeoutError) as e:
        print(f"  ! failed fetching {url}: {e}", file=sys.stderr)
    return None


def main() -> None:
    print(f"Fetching manifest: {MANIFEST_URL}")
    raw = fetch(MANIFEST_URL)
    if raw is None:
        sys.exit("error: could not fetch kitspace.yaml (offline?)")

    manifest = yaml.safe_load(raw) or {}
    projects = manifest.get("multi", {})
    if not projects:
        sys.exit("error: kitspace.yaml has no `multi:` projects")

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    BOM_DIR.mkdir(parents=True, exist_ok=True)
    (CACHE_DIR / "manifest.yaml").write_bytes(raw)

    ok = 0
    for key, proj in projects.items():
        bom_path = proj.get("bom")
        if not bom_path:
            continue
        data = fetch(f"{RAW}/{bom_path}")
        if data is None:
            continue
        (BOM_DIR / f"{key}.csv").write_bytes(data)
        ok += 1
        print(f"  ✓ {key}  ({bom_path})")

    print(f"Synced manifest + {ok}/{len(projects)} BOMs into {CACHE_DIR.relative_to(ROOT)}.")


if __name__ == "__main__":
    main()
