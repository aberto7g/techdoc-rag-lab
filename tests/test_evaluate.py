from __future__ import annotations

import sys
import unittest
from pathlib import Path

SRC_PATH = Path(__file__).resolve().parent.parent / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))


from techdoc_rag.evaluate import exact_match, retrieval_hit_at_k, token_f1


class EvaluateTests(unittest.TestCase):
    def test_exact_match_ignores_spacing(self) -> None:
        self.assertEqual(exact_match("机器学习 与 数据挖掘", "机器学习与数据挖掘"), 1.0)

    def test_token_f1_is_positive_for_partial_overlap(self) -> None:
        score = token_f1("检索 和 生成", "检索 生成 评测")
        self.assertGreater(score, 0)
        self.assertLess(score, 1)

    def test_retrieval_hit(self) -> None:
        self.assertEqual(retrieval_hit_at_k(["doc-1", "doc-3"], ["doc-2", "doc-3"]), 1.0)
