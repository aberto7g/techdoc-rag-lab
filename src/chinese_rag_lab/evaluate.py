from __future__ import annotations

from chinese_rag_lab.tokenize import normalize_text, simple_tokenize
from chinese_rag_lab.types import Prediction, Question


def exact_match(prediction: str, gold: str) -> float:
    return float(normalize_text(prediction) == normalize_text(gold))


def token_f1(prediction: str, gold: str) -> float:
    pred_tokens = simple_tokenize(prediction)
    gold_tokens = simple_tokenize(gold)
    if not pred_tokens or not gold_tokens:
        return 0.0

    pred_counts: dict[str, int] = {}
    gold_counts: dict[str, int] = {}
    for token in pred_tokens:
        pred_counts[token] = pred_counts.get(token, 0) + 1
    for token in gold_tokens:
        gold_counts[token] = gold_counts.get(token, 0) + 1

    overlap = 0
    for token, pred_count in pred_counts.items():
        overlap += min(pred_count, gold_counts.get(token, 0))

    if overlap == 0:
        return 0.0

    precision = overlap / len(pred_tokens)
    recall = overlap / len(gold_tokens)
    return 2 * precision * recall / (precision + recall)


def retrieval_hit_at_k(predicted_doc_ids: list[str], gold_doc_ids: list[str]) -> float:
    return float(bool(set(predicted_doc_ids).intersection(gold_doc_ids)))


def evaluate_predictions(predictions: list[Prediction], questions: list[Question]) -> dict:
    question_lookup = {question.question_id: question for question in questions}
    rows: list[dict] = []

    for prediction in predictions:
        question = question_lookup[prediction.question_id]
        em = exact_match(prediction.predicted_answer, question.gold_answer)
        f1 = token_f1(prediction.predicted_answer, question.gold_answer)
        hit = retrieval_hit_at_k(prediction.retrieved_doc_ids, question.gold_doc_ids)
        rows.append(
            {
                "question_id": prediction.question_id,
                "question": prediction.question,
                "gold_answer": question.gold_answer,
                "predicted_answer": prediction.predicted_answer,
                "retrieved_doc_ids": prediction.retrieved_doc_ids,
                "gold_doc_ids": question.gold_doc_ids,
                "answer_em": em,
                "answer_f1": f1,
                "retrieval_hit": hit,
            }
        )

    count = max(len(rows), 1)
    summary = {
        "answer_em": sum(row["answer_em"] for row in rows) / count,
        "answer_f1": sum(row["answer_f1"] for row in rows) / count,
        "retrieval_hit": sum(row["retrieval_hit"] for row in rows) / count,
        "count": len(rows),
    }
    return {"summary": summary, "rows": rows}

