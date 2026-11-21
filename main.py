#!/usr/bin/env python3
"""Entry point for the news-image-20261121 make.fun bounty.

Copies the pre-rendered entry.png (produced by draw.py) into
$MAKEFUN_OUTPUT_DIR/entry.png. Standard library only, deterministic.
"""
import os
import shutil
import sys
from pathlib import Path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    src = Path(__file__).resolve().parent / "entry.png"
    if not src.is_file():
        print("entry.png not found next to main.py", file=sys.stderr)
        return 1
    out = Path(out_dir) / "entry.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out)
    print("wrote", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
