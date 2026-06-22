from __future__ import annotations

from chinese_rag_lab.generator import ExtractiveGenerator
from chinese_rag_lab.retriever import BM25Retriever
from chinese_rag_lab.types import Prediction, Question


class RAGPipeline:
    def __init__(self, retriever: BM25Retriever, generator: ExtractiveGenerator, top_k: int = 3) -> None:
        self.retriever = retriever
        self.generator = generator
        self.top_k = top_k

    def predict(self, question: Question) -> Prediction:
        retrieved = self.retriever.retrieve(question.question, top_k=self.top_k)
        predicted_answer = self.generator.generate(question.question, retrieved)
        top_context = retrieved[0].doc.text if retrieved else ""
        return Prediction(
            question_id=question.question_id,
            question=question.question,
            predicted_answer=predicted_answer,
            retrieved_doc_ids=[item.doc.doc_id for item in retrieved],
            top_context=top_context,
        )

