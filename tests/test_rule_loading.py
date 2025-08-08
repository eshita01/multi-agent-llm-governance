from compliance_guardian.utils.rule_loader import load_rule_summaries, load_rules_by_ids


def test_load_rules():
    summaries = load_rule_summaries(["generic"])
    assert summaries and summaries[0].rule_id == "GEN001"
    rules = load_rules_by_ids(["generic"], ["GEN001"])
    assert "GEN001" in rules
    assert rules["GEN001"].description_actionable.startswith("Never output email")
