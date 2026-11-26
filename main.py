"""make.fun news-image-20261125 entry.

Copies the bundled entry.png to $MAKEFUN_OUTPUT_DIR/entry.png
(or /output when the variable is unset), then verifies the copy
byte-for-byte so a truncated write fails loudly instead of
silently shipping a broken image.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    src = HERE / "entry.png"
    if not src.is_file():
        print(f"missing bundled image: {src}", file=sys.stderr)
        return 1
    OUT.mkdir(parents=True, exist_ok=True)
    dst = OUT / "entry.png"
    shutil.copyfile(src, dst)
    if sha256(src) != sha256(dst):
        print(f"copy mismatch, refusing to ship: {dst}", file=sys.stderr)
        return 1
    print(f"Wrote {dst} ({dst.stat().st_size} bytes, sha256 verified)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
