from __future__ import annotations

from techdoc_rag.tokenize import simple_tokenize
from techdoc_rag.types import RetrievedDocument


class ExtractiveGenerator:
    """A deterministic baseline that extracts the most query-overlapping sentence."""

    def generate(self, question: str, retrieved_docs: list[RetrievedDocument]) -> str:
        if not retrieved_docs:
            return "未检索到相关文档。"

        question_tokens = set(simple_tokenize(question))
        best_sentence = ""
        best_overlap = -1

        for item in retrieved_docs:
            sentences = _split_sentences(item.doc.text)
            for sentence in sentences:
                overlap = len(question_tokens.intersection(simple_tokenize(sentence)))
                if overlap > best_overlap:
                    best_overlap = overlap
                    best_sentence = sentence

        if not best_sentence:
            return retrieved_docs[0].doc.text[:120]
        return best_sentence.strip()


def _split_sentences(text: str) -> list[str]:
    separators = "。！？；\n"
    current = []
    sentences: list[str] = []

    for char in text:
        current.append(char)
        if char in separators:
            sentence = "".join(current).strip()
            if sentence:
                sentences.append(sentence)
            current = []

    tail = "".join(current).strip()
    if tail:
        sentences.append(tail)

    return sentences
