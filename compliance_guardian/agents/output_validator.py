"""Validate final outputs against rules."""
from __future__ import annotations
from typing import List

from .compliance_agent import ComplianceAgent
from ..utils.models import Rule


class OutputValidator:
    def __init__(self, agent: ComplianceAgent) -> None:
        self.agent = agent

    def validate(self, output: str) -> List[Rule]:
        return self.agent.check(output, "output")
