"""
Helper utilities for banking client
"""
from typing import Any


def ensure_http_scheme(url: str) -> str:
    if url.startswith("http://") or url.startswith("https://"):
        return url
    return "http://" + url


def safe_get(d: dict, key: str, default: Any = None):
    return d.get(key, default)
