"""CLI entry point for compliance guardian."""
from __future__ import annotations
import argparse
from typing import List

from .agents.domain_user_extractor import extract
from .agents.compliance_agent import ComplianceAgent
from .agents.primary_agent import PrimaryAgent
from .agents.output_validator import OutputValidator
from .llm_providers.gemini_provider import GeminiProvider
from .llm_providers.mock_provider import MockProvider


def run(prompt: str, provider_name: str = "mock", api_key: str | None = None) -> str:
    provider = GeminiProvider(api_key=api_key) if provider_name == "gemini" else MockProvider("OK")
    domains, dynamic_rules = extract(prompt)
    comp_agent = ComplianceAgent(domains, dynamic_rules)
    matches = comp_agent.check(prompt, "pre-prompt")
    for rule in matches:
        if rule.action == "BLOCK":
            return f"BLOCK: {rule.rule_id} - {rule.description_actionable}"
    constraints: List[str] = [r.llm_instruction or r.description_actionable for r in matches if r.action == "WARN"]
    generator = PrimaryAgent(provider)
    output = generator.generate(prompt, constraints)
    validator = OutputValidator(comp_agent)
    post_matches = validator.validate(output)
    for rule in post_matches:
        if rule.action == "BLOCK":
            return f"BLOCK: {rule.rule_id} - {rule.description_actionable}"
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description="Dynamic Compliance Guardian")
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--provider", default="mock")
    parser.add_argument("--api-key", dest="api_key")
    args = parser.parse_args()
    result = run(args.prompt, args.provider, args.api_key)
    print(result)


if __name__ == "__main__":  # pragma: no cover
    main()
