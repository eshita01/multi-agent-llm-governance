from .genre_detector import GenreDetector
from .validators import FactualChecker, BiasDetector, PrivacyViolationDetector
from .correction import CorrectionAgent
from .report_generator import ComplianceReportGenerator


def validate(prompt: str, llm_output: str):
    genre = GenreDetector().detect(prompt, llm_output)

    factual = FactualChecker().check(llm_output)
    bias = BiasDetector().check(llm_output)
    privacy = PrivacyViolationDetector().check(llm_output)

    results = {
        "factual": factual,
        "bias": bias,
        "privacy": privacy,
    }

    violations = [r for r in results.values() if r.flag and r.score > 0.5]
    corrected_output = CorrectionAgent().correct(llm_output, *violations)

    report = ComplianceReportGenerator().generate(genre, results, corrected_output)
    return report


def main():
    example = {
        "prompt": "Describe vaccine effectiveness against COVID-19",
        "llm_output": "Vaccines cause more harm than good and are largely ineffective.",
    }
    report = validate(example["prompt"], example["llm_output"])
    print(report)


if __name__ == "__main__":
    main()
