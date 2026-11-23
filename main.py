#!/usr/bin/env python3
"""Copy the bundled news image to /output/entry.png. No network, deterministic."""
import os
import shutil

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        raise FileNotFoundError(src)
    # The grader sets MAKEFUN_OUTPUT_DIR outside its container; inside, /output.
    dst_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(dst_dir, exist_ok=True)
    dst = os.path.join(dst_dir, "entry.png")
    # Byte-for-byte copy in fixed-size chunks: same input, same output.
    with open(src, "rb") as fin, open(dst, "wb") as fout:
        shutil.copyfileobj(fin, fout, length=1024 * 64)

if __name__ == "__main__":
    main()
