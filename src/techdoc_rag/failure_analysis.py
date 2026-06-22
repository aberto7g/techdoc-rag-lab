from __future__ import annotations


def categorize_failure(row: dict) -> str:
    if row["retrieval_hit"] == 0:
        return "retrieval_miss"
    if row["answer_f1"] == 0:
        return "generation_failure"
    if row["answer_em"] == 0 and row["answer_f1"] < 0.5:
        return "partial_answer"
    return "success"


def build_failure_report(rows: list[dict]) -> dict:
    counts: dict[str, int] = {}
    cases: dict[str, list[dict]] = {}

    for row in rows:
        category = categorize_failure(row)
        counts[category] = counts.get(category, 0) + 1
        cases.setdefault(category, []).append(
            {
                "question_id": row["question_id"],
                "question": row["question"],
                "gold_answer": row["gold_answer"],
                "predicted_answer": row["predicted_answer"],
                "retrieved_doc_ids": row["retrieved_doc_ids"],
                "gold_doc_ids": row["gold_doc_ids"],
            }
        )

    return {"counts": counts, "cases": cases}

