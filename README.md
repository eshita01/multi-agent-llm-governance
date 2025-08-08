# Dynamic Compliance Guardian

This repository provides a CPU-friendly compliance layer for LLM agents. Rules are loaded dynamically and matched using a hybrid BM25 and embedding retrieval pipeline. The system can block, warn, or log interactions based on predefined rules.

## Usage

Run a compliance check from the CLI:

```bash
python -m compliance_guardian.main --prompt "Scrape article titles from example.com"
```

## Tests

```bash
pytest -q
```
