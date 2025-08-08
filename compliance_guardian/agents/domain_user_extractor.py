"""Simple heuristic domain detection and user rule extraction."""
from __future__ import annotations
from typing import List, Tuple

from ..utils.models import Rule


def extract(prompt: str) -> Tuple[List[str], List[Rule]]:
    """Detect domains from prompt. Returns list of domains and dynamic rules."""
    text = prompt.lower()
    domains: List[str] = []
    if any(k in text for k in ["scrape", "scraping"]):
        domains.append("scraping")
    if any(k in text for k in ["stock", "finance", "investment"]):
        domains.append("finance")
    if any(k in text for k in ["medical", "symptom", "diagnose"]):
        domains.append("medical")
    if "generic" not in domains:
        domains.append("generic")
    return domains, []
