"""make.fun news-image-20261125 entry.

Copies the bundled entry.png to $MAKEFUN_OUTPUT_DIR/entry.png
(or /output when the variable is unset).
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")

OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT / "entry.png")
print(f"Wrote {OUT / 'entry.png'}")
