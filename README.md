# 技术文档 RAG 实验

一个面向中文计算机技术文档问答的 RAG 实验仓库，当前重点是做可复现的基线、评测和失败案例分析。

English: A small RAG lab for Chinese technical documentation QA, focused on reproducible baselines, evaluation, and error analysis.

## Current Scope

- BM25 retrieval baseline
- extractive answer baseline
- retrieval and answer evaluation
- failure case tracking

## Data

- `data/tech_docs_demo/`: small demo set for quick runs
- `data/tech_docs_seed/`: seed set built from official technical docs

## Run

```bash
python scripts/run_experiment.py --config configs/tech_docs_experiment.json
python scripts/run_experiment.py --config configs/tech_docs_seed_experiment.json
python -m unittest discover -s tests
```

Artifacts are written to `artifacts/` by default.

## Data Format

Document:

```json
{"doc_id":"doc-1","title":"...","text":"...","source":"...","domain":"..."}
```

QA sample:

```json
{"question_id":"q-1","question":"...","gold_answer":"...","gold_doc_ids":["doc-1"]}
```