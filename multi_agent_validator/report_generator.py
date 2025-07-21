from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class ComplianceReport:
    domain: str
    results: Dict[str, Any]
    corrected_output: str

class ComplianceReportGenerator:
    def generate(self, domain: str, results: Dict[str, Any], corrected_output: str) -> ComplianceReport:
        return ComplianceReport(domain=domain, results=results, corrected_output=corrected_output)
