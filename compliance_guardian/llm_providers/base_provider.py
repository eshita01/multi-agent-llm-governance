"""Base interface for LLM providers."""
from __future__ import annotations
from abc import ABC, abstractmethod


class BaseProvider(ABC):
    @abstractmethod
    def complete(self, system_prompt: str, user_prompt: str) -> str:
        """Return completion text."""

    def adjudicate_violation(self, text: str, rule_summary: str) -> bool:
        """Optional step to let an LLM decide if a rule was violated."""
        return True
