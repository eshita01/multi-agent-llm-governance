"""Pydantic models for compliance rules."""
from __future__ import annotations
from typing import Dict, List, Optional, Literal
from pydantic import BaseModel


class Activation(BaseModel):
    regexes: Optional[List[str]] = None
    keywords_any: Optional[List[str]] = None
    keywords_all: Optional[List[str]] = None
    domains: Optional[List[str]] = None


class Rule(BaseModel):
    rule_id: str
    action: Literal["BLOCK", "WARN", "LOG"]
    description_actionable: str
    legal_reference: Optional[str] = None
    clause_mapping: Optional[Dict[str, str]] = None
    suggestion: Optional[str] = None
    llm_instruction: Optional[str] = None
    activation: Activation
    applicable_contexts: List[Literal["pre-prompt", "plan", "output"]]


class RuleSummary(BaseModel):
    rule_id: str
    action: Literal["BLOCK", "WARN", "LOG"]
    description_actionable: str
