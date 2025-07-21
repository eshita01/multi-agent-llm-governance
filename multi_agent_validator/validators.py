from dataclasses import dataclass

@dataclass
class ValidationResult:
    flag: bool
    score: float
    rationale: str

class FactualChecker:
    def check(self, text: str) -> ValidationResult:
        # Simple heuristic example
        flag = "ineffective" in text.lower()
        score = 0.9 if flag else 0.0
        rationale = "Contains claims that vaccines are ineffective." if flag else "Looks factual."
        return ValidationResult(flag, score, rationale)

class BiasDetector:
    def check(self, text: str) -> ValidationResult:
        flag = "left" in text.lower() or "right" in text.lower()
        score = 0.6 if flag else 0.0
        rationale = "Contains political leaning." if flag else "No bias detected."
        return ValidationResult(flag, score, rationale)

class PrivacyViolationDetector:
    def check(self, text: str) -> ValidationResult:
        flag = "@" in text
        score = 0.8 if flag else 0.0
        rationale = "Possible email detected." if flag else "No PII found."
        return ValidationResult(flag, score, rationale)
