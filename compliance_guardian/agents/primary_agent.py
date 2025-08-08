"""Primary agent responsible for content generation."""
from __future__ import annotations
from typing import List

from ..llm_providers.base_provider import BaseProvider


class PrimaryAgent:
    def __init__(self, provider: BaseProvider) -> None:
        self.provider = provider

    def generate(self, prompt: str, constraints: List[str]) -> str:
        system_prompt = "You are a helpful assistant."
        user_prompt = prompt
        if constraints:
            user_prompt += "\nConstraints:\n" + "\n".join(constraints)
        return self.provider.complete(system_prompt, user_prompt)
