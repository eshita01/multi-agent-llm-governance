"""FastAPI interface for the compliance guardian."""
from __future__ import annotations
from fastapi import FastAPI
from pydantic import BaseModel

from ..agents.domain_user_extractor import extract
from ..agents.compliance_agent import ComplianceAgent
from ..agents.primary_agent import PrimaryAgent
from ..agents.output_validator import OutputValidator
from ..llm_providers.mock_provider import MockProvider

app = FastAPI()


class PromptIn(BaseModel):
    prompt: str


@app.post("/generate")
def generate(data: PromptIn) -> dict:
    domains, dynamic_rules = extract(data.prompt)
    agent = ComplianceAgent(domains, dynamic_rules)
    matches = agent.check(data.prompt, "pre-prompt")
    for rule in matches:
        if rule.action == "BLOCK":
            return {"status": "blocked", "rule_id": rule.rule_id}
    constraints = [r.llm_instruction or r.description_actionable for r in matches if r.action == "WARN"]
    provider = MockProvider("OK")
    generator = PrimaryAgent(provider)
    output = generator.generate(data.prompt, constraints)
    validator = OutputValidator(agent)
    post = validator.validate(output)
    for rule in post:
        if rule.action == "BLOCK":
            return {"status": "blocked", "rule_id": rule.rule_id}
    return {"status": "ok", "output": output}
