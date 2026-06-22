from __future__ import annotations

import sys
import unittest
from pathlib import Path

SRC_PATH = Path(__file__).resolve().parent.parent / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from techdoc_rag.retriever import BM25Retriever
from techdoc_rag.types import Document


class RetrieverTests(unittest.TestCase):
    def test_bm25_prefers_relevant_document(self) -> None:
        documents = [
            Document(doc_id="a", title="RAG系统", text="RAG系统包含检索和生成模块。"),
            Document(doc_id="b", title="数据库", text="数据库关注事务和索引。"),
        ]
        retriever = BM25Retriever(documents)
        results = retriever.retrieve("RAG系统有哪些模块", top_k=1)
        self.assertEqual(results[0].doc.doc_id, "a")
