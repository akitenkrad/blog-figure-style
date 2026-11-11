from __future__ import annotations

import os
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"

sys.path.insert(0, str(SRC))
os.environ.setdefault(
    "MPLCONFIGDIR",
    str(ROOT / ".matplotlib-cache"),
)
