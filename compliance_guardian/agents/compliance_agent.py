"""Compliance agent for checking text against rules."""
from __future__ import annotations
from typing import Dict, List, Optional

from ..utils.models import Rule, RuleSummary
from ..utils.rule_loader import load_rule_summaries, load_rules_by_ids
from ..utils.rag_indexer import RAGIndexer
from ..utils.predicates import matches_activation
from ..utils.risk_scorer import score


class ComplianceAgent:
    """Check text against rules and return violations."""

    def __init__(self, domains: List[str], dynamic_rules: Optional[List[Rule]] = None) -> None:
        self.domains = domains
        self.dynamic_rules: Dict[str, Rule] = {r.rule_id: r for r in (dynamic_rules or [])}
        summaries = load_rule_summaries(domains)
        for r in self.dynamic_rules.values():
            summaries.append(RuleSummary(rule_id=r.rule_id, action=r.action, description_actionable=r.description_actionable))
        self.indexer = RAGIndexer(summaries)

    def check(self, text: str, context: str) -> List[Rule]:
        summaries = self.indexer.search(text)
        rule_ids = [s.rule_id for s in summaries]
        rules = load_rules_by_ids(self.domains, rule_ids)
        rules.update({rid: r for rid, r in self.dynamic_rules.items() if rid in rule_ids})
        matched: List[Rule] = []
        for rid in rule_ids:
            rule = rules.get(rid)
            if not rule:
                continue
            if context not in rule.applicable_contexts:
                continue
            if matches_activation(text, self.domains, rule.activation):
                matched.append(rule)
        matched.sort(key=lambda r: score(r.action), reverse=True)
        return matched
