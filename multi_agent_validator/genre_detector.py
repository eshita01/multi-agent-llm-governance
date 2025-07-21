class GenreDetector:
    """Detect content domain of user prompts and LLM outputs."""

    def detect(self, prompt: str, llm_output: str) -> str:
        """Stub genre detection based on keywords."""
        text = f"{prompt} {llm_output}".lower()
        if any(word in text for word in ["medical", "vaccine", "health"]):
            return "healthcare"
        if any(word in text for word in ["financial", "stock", "investment"]):
            return "finance"
        return "general"
