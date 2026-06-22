from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

from techdoc_rag.types import Document, Question


def load_jsonl(path: str | Path) -> list[dict]:
    records: list[dict] = []
    with Path(path).open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))
    return records


def save_json(path: str | Path, payload: dict) -> None:
    with Path(path).open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)


def save_jsonl(path: str | Path, rows: Iterable[dict]) -> None:
    with Path(path).open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def load_documents(path: str | Path) -> list[Document]:
    return [
        Document(
            doc_id=row["doc_id"],
            title=row.get("title", ""),
            text=row["text"],
            source=row.get("source", ""),
            domain=row.get("domain", ""),
        )
        for row in load_jsonl(path)
    ]


def load_questions(path: str | Path) -> list[Question]:
    return [
        Question(
            question_id=row["question_id"],
            question=row["question"],
            gold_answer=row["gold_answer"],
            gold_doc_ids=list(row.get("gold_doc_ids", [])),
        )
        for row in load_jsonl(path)
    ]
