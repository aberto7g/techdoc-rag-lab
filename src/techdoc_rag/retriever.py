from __future__ import annotations

import math
from collections import Counter, defaultdict

from techdoc_rag.tokenize import simple_tokenize
from techdoc_rag.types import Document, RetrievedDocument


class BM25Retriever:
    def __init__(self, documents: list[Document], k1: float = 1.5, b: float = 0.75) -> None:
        self.documents = documents
        self.k1 = k1
        self.b = b
        self.doc_freqs: dict[str, int] = defaultdict(int)
        self.term_freqs: list[Counter[str]] = []
        self.doc_lengths: list[int] = []

        for document in documents:
            tokens = simple_tokenize(f"{document.title} {document.text}")
            counts = Counter(tokens)
            self.term_freqs.append(counts)
            self.doc_lengths.append(sum(counts.values()))
            for token in counts:
                self.doc_freqs[token] += 1

        self.avg_doc_length = sum(self.doc_lengths) / max(len(self.doc_lengths), 1)

    def retrieve(self, query: str, top_k: int = 3) -> list[RetrievedDocument]:
        query_tokens = simple_tokenize(query)
        scored: list[RetrievedDocument] = []

        for index, document in enumerate(self.documents):
            score = self._score_document(query_tokens, index)
            scored.append(RetrievedDocument(doc=document, score=score))

        scored.sort(key=lambda item: item.score, reverse=True)
        return scored[:top_k]

    def _score_document(self, query_tokens: list[str], index: int) -> float:
        score = 0.0
        term_freq = self.term_freqs[index]
        doc_length = self.doc_lengths[index]

        for token in query_tokens:
            if token not in term_freq:
                continue

            df = self.doc_freqs.get(token, 0)
            idf = math.log(1 + (len(self.documents) - df + 0.5) / (df + 0.5))
            freq = term_freq[token]
            denom = freq + self.k1 * (1 - self.b + self.b * doc_length / max(self.avg_doc_length, 1))
            score += idf * (freq * (self.k1 + 1)) / max(denom, 1e-9)

        return score
