"""Map rule actions to risk scores."""
from __future__ import annotations
from typing import Dict

SCORES: Dict[str, int] = {"BLOCK": 3, "WARN": 2, "LOG": 1}


def score(action: str) -> int:
    return SCORES.get(action.upper(), 0)
