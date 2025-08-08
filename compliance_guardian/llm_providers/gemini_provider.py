"""Gemini provider using google-generativeai SDK."""
from __future__ import annotations
from typing import Optional

from .base_provider import BaseProvider
from ..utils.env_loader import get_env


class GeminiProvider(BaseProvider):
    def __init__(self, api_key: Optional[str] = None) -> None:
        self.api_key = api_key or get_env("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("Gemini API key not provided")
        try:
            import google.generativeai as genai  # type: ignore
        except Exception as exc:  # pragma: no cover - optional dependency
            raise RuntimeError("google-generativeai package is required") from exc
        self._genai = genai
        self._genai.configure(api_key=self.api_key)

    def complete(self, system_prompt: str, user_prompt: str) -> str:
        model = self._genai.GenerativeModel("gemini-pro")
        response = model.generate_content([system_prompt, user_prompt])
        return getattr(response, "text", "")
