class CorrectionAgent:
    def correct(self, original_output: str, *violations) -> str:
        if not violations:
            return original_output
        # naive correction replacing flagged terms
        corrected = original_output.replace("ineffective", "effective")
        corrected = corrected.replace("harm", "benefit")
        return corrected
