from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RULES_DIR = BASE_DIR / "rules"
RULES_SUMMARY_DIR = BASE_DIR / "rules_summary"
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
BM25_TOP_N = 25
EMBED_TOP_K = 8
