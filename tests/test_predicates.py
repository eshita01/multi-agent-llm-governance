from compliance_guardian.utils.models import Activation
from compliance_guardian.utils.predicates import matches_activation


def test_keywords_and_regex():
    act1 = Activation(keywords_any=["robots.txt"])
    assert matches_activation("Respect robots.txt rules", ["scraping"], act1)
    act2 = Activation(regexes=["\\d{3}"])
    assert matches_activation("123", ["generic"], act2)
    assert not matches_activation("abc", ["generic"], act2)
