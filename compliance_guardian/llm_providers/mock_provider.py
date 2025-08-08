"""Mock LLM provider for testing."""
from __future__ import annotations
from .base_provider import BaseProvider


class MockProvider(BaseProvider):
    def __init__(self, response: str) -> None:
        self.response = response

    def complete(self, system_prompt: str, user_prompt: str) -> str:  # pragma: no cover - trivial
        return self.response
