from __future__ import annotations

import re


_TOKEN_PATTERN = re.compile(r"[\u4e00-\u9fff]|[A-Za-z0-9_]+")


def simple_tokenize(text: str) -> list[str]:
    """Tokenize Chinese text with a simple character-and-word strategy."""
    return _TOKEN_PATTERN.findall(text.lower())


def normalize_text(text: str) -> str:
    return "".join(simple_tokenize(text))

