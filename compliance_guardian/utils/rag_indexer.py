"""Hybrid BM25 + optional embedding retriever."""
from __future__ import annotations
from typing import Sequence, List
import numpy as np
from rank_bm25 import BM25Okapi

try:  # pragma: no cover - optional dependency
    from sentence_transformers import SentenceTransformer  # type: ignore
except Exception:  # pragma: no cover
    SentenceTransformer = None  # type: ignore

from ..config import EMBED_MODEL, BM25_TOP_N, EMBED_TOP_K
from .models import RuleSummary


class RAGIndexer:
    """Retrieve relevant rule summaries for a given query."""

    def __init__(self, summaries: Sequence[RuleSummary]) -> None:
        self.summaries = list(summaries)
        corpus = [s.description_actionable for s in self.summaries]
        tokenized = [doc.lower().split() for doc in corpus]
        self.bm25 = BM25Okapi(tokenized)
        if SentenceTransformer is not None:
            self.model = SentenceTransformer(EMBED_MODEL)
            self.embeddings = self.model.encode(corpus, show_progress_bar=False)
        else:
            self.model = None
            self.embeddings = np.zeros((len(corpus), 1))

    def search(self, query: str) -> List[RuleSummary]:
        tokens = query.lower().split()
        bm25_scores = self.bm25.get_scores(tokens)
        top_idx = np.argsort(bm25_scores)[::-1][:BM25_TOP_N]
        if len(top_idx) == 0:
            return []
        if self.model is not None:
            query_vec = self.model.encode([query], show_progress_bar=False)[0]
            cand_vecs = self.embeddings[top_idx]
            sims = cand_vecs @ query_vec
            ranked = np.argsort(sims)[::-1][:EMBED_TOP_K]
        else:
            ranked = np.arange(len(top_idx))[:EMBED_TOP_K]
        return [self.summaries[top_idx[i]] for i in ranked]
