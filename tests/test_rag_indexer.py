import numpy as np
from compliance_guardian.utils import rag_indexer
from compliance_guardian.utils.models import RuleSummary


class DummyModel:
    def encode(self, texts, show_progress_bar=False):
        return np.array([[len(t)] for t in texts])


def test_rag_indexer(monkeypatch):
    monkeypatch.setattr(rag_indexer, "SentenceTransformer", lambda *_args, **_kw: DummyModel())
    summaries = [RuleSummary(rule_id="1", action="BLOCK", description_actionable="Never output email addresses.")]
    indexer = rag_indexer.RAGIndexer(summaries)
    results = indexer.search("email addresses")
    assert results and results[0].rule_id == "1"
