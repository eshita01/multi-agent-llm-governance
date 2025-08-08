"""Activation predicate checks for rules."""
from __future__ import annotations
import re
from typing import List

from .models import Activation


def matches_activation(text: str, domains: List[str], activation: Activation) -> bool:
    """Return True if rule activation predicates match given text/domains."""
    t = text.lower()
    if activation.domains and not any(d in activation.domains for d in domains):
        return False
    if activation.regexes:
        if not any(re.search(p, text, re.IGNORECASE) for p in activation.regexes):
            return False
    if activation.keywords_all:
        if not all(k.lower() in t for k in activation.keywords_all):
            return False
    if activation.keywords_any:
        if not any(k.lower() in t for k in activation.keywords_any):
            return False
    return True
