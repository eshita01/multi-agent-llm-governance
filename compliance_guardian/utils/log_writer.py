"""Simple JSONL log writer."""
from __future__ import annotations
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict


def write_log(entry: Dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    line = {"time": datetime.utcnow().isoformat(), **entry}
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(line) + "\n")
