import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from multi_agent_validator.main import validate


def test_validate():
    report = validate(
        "Describe vaccine effectiveness against COVID-19",
        "Vaccines cause more harm than good and are largely ineffective."
    )
    assert report.domain == "healthcare"
    assert report.corrected_output != ""
