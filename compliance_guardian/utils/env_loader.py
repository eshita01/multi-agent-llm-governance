"""Environment loader."""
from __future__ import annotations
import os
from typing import Optional
from dotenv import load_dotenv


def get_env(name: str, default: Optional[str] = None) -> Optional[str]:
    load_dotenv()
    return os.getenv(name, default)
