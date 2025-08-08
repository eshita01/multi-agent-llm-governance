"""Generate summary rule files from full rules."""
from __future__ import annotations
import json
from pathlib import Path

RULES_DIR = Path(__file__).resolve().parents[1] / "rules"
SUMMARY_DIR = Path(__file__).resolve().parents[1] / "rules_summary"


def main() -> None:
    SUMMARY_DIR.mkdir(exist_ok=True)
    for path in RULES_DIR.glob("*.json"):
        data = json.loads(path.read_text())
        summaries = [
            {
                "rule_id": r["rule_id"],
                "action": r["action"],
                "description_actionable": r["description_actionable"],
            }
            for r in data
        ]
        out = SUMMARY_DIR / f"{path.stem}_summary.json"
        out.write_text(json.dumps(summaries, indent=2))


if __name__ == "__main__":
    main()
