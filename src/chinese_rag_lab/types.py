from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Document:
    doc_id: str
    title: str
    text: str
    source: str = ""
    domain: str = ""


@dataclass(slots=True)
class Question:
    question_id: str
    question: str
    gold_answer: str
    gold_doc_ids: list[str]


@dataclass(slots=True)
class RetrievedDocument:
    doc: Document
    score: float


@dataclass(slots=True)
class Prediction:
    question_id: str
    question: str
    predicted_answer: str
    retrieved_doc_ids: list[str]
    top_context: str

