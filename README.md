# 技术文档 RAG 实验

我在这里做一个中文技术文档问答方向的 RAG 实验。

现在先保留一个比较简单的基线，方便后面继续往上加：

- BM25 检索
- 抽取式回答
- 检索 / 回答评测
- 失败案例记录

## 现在的数据

目前有两套小数据：

- `data/tech_docs_demo/`
  用来快速跑通流程。
- `data/tech_docs_seed/`
  用官方技术文档整理的一批 seed 样本，现在主要是 Git 和 grep。

## 目录

```text
.
|-- configs/
|-- data/
|-- reports/
|-- scripts/
|-- src/
|   `-- techdoc_rag/
|-- tests/
|-- .gitignore
|-- LICENSE
|-- pyproject.toml
`-- README.md
```

## 运行

跑 demo：

```bash
python scripts/run_experiment.py --config configs/tech_docs_experiment.json
```

跑 seed 数据：

```bash
python scripts/run_experiment.py --config configs/tech_docs_seed_experiment.json
```

跑测试：

```bash
python -m unittest discover -s tests
```

结果默认写到 `artifacts/`。

## 数据格式

文档：

```json
{"doc_id":"doc-1","title":"...","text":"...","source":"...","domain":"..."}
```

问答：

```json
{
  "question_id": "q-1",
  "question": "...",
  "gold_answer": "...",
  "gold_doc_ids": ["doc-1"]
}
```

## 后面准备做的事

1. 继续扩 Git / Linux 相关样本
2. 加稠密检索或者混合检索
3. 接一个带引用的生成模块
4. 把错误分类再细一点

