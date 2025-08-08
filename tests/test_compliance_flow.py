import numpy as np
from compliance_guardian.utils import rag_indexer
from compliance_guardian import main


class DummyModel:
    def encode(self, texts, show_progress_bar=False):
        return np.array([[len(t)] for t in texts])


def test_compliance_block(monkeypatch):
    monkeypatch.setattr(rag_indexer, "SentenceTransformer", lambda *_args, **_kw: DummyModel())
    result = main.run("My email is test@example.com")
    assert result.startswith("BLOCK")
