from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from techdoc_rag.evaluate import evaluate_predictions
from techdoc_rag.failure_analysis import build_failure_report
from techdoc_rag.generator import ExtractiveGenerator
from techdoc_rag.io_utils import load_documents, load_questions, save_json
from techdoc_rag.pipeline import RAGPipeline
from techdoc_rag.retriever import BM25Retriever


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a baseline Chinese RAG experiment.")
    parser.add_argument("--config", required=True, help="Path to the experiment config JSON file.")
    args = parser.parse_args()

    config_path = Path(args.config)
    with config_path.open("r", encoding="utf-8") as handle:
        config = json.load(handle)

    corpus_path = PROJECT_ROOT / config["corpus_path"]
    questions_path = PROJECT_ROOT / config["questions_path"]
    output_path = PROJECT_ROOT / config["output_path"]

    documents = load_documents(corpus_path)
    questions = load_questions(questions_path)

    retriever = BM25Retriever(documents)
    generator = ExtractiveGenerator()
    pipeline = RAGPipeline(retriever=retriever, generator=generator, top_k=config.get("top_k", 3))

    predictions = [pipeline.predict(question) for question in questions]
    evaluation = evaluate_predictions(predictions, questions)
    failure_report = build_failure_report(evaluation["rows"])

    output_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "config": config,
        "summary": evaluation["summary"],
        "rows": evaluation["rows"],
        "failure_report": failure_report,
    }
    save_json(output_path, payload)

    print("Experiment complete.")
    print(json.dumps(evaluation["summary"], ensure_ascii=False, indent=2))
    print(f"Saved results to: {output_path}")


if __name__ == "__main__":
    main()
