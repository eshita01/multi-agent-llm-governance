"""Utilities for loading rules and summaries."""
from __future__ import annotations
import json
from typing import Dict, Iterable, List

from ..config import RULES_DIR, RULES_SUMMARY_DIR
from .models import Rule, RuleSummary


def load_rule_summaries(domains: Iterable[str]) -> List[RuleSummary]:
    """Load summary rules for given domains."""
    summaries: List[RuleSummary] = []
    for domain in domains:
        path = RULES_SUMMARY_DIR / f"{domain}_summary.json"
        if path.exists():
            data = json.loads(path.read_text())
            summaries.extend(RuleSummary.model_validate(r) for r in data)
    return summaries


def load_rules_by_ids(domains: Iterable[str], rule_ids: Iterable[str]) -> Dict[str, Rule]:
    """Load full rule definitions for the provided rule IDs."""
    result: Dict[str, Rule] = {}
    target_ids = set(rule_ids)
    for domain in domains:
        path = RULES_DIR / f"{domain}.json"
        if not path.exists():
            continue
        data = json.loads(path.read_text())
        for entry in data:
            if entry.get("rule_id") in target_ids:
                result[entry["rule_id"]] = Rule.model_validate(entry)
    return result
