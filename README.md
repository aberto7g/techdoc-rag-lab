# 技术文档 RAG 实验

这个仓库是我在做的一个 RAG 小实验，方向是中文计算机技术文档问答。现在这版先不追求复杂模型，主要把几件基础的事情做扎实：

- 技术文档数据怎么组织
- 检索和回答怎么分开评测
- 基线系统怎么尽量简单但可复现
- 出错以后怎么做失败案例分析

我之所以选“技术文档”这个方向，是因为这类数据既有明确术语，也有不少步骤型知识，很适合拿来观察 RAG 系统在检索、抽取和生成上的问题。相比泛知识问答，这个场景更容易做成一个能持续迭代的实验项目。

## 现在仓库里有什么

当前版本包含一套可以直接跑通的最小基线：

- 一个中文技术文档 demo 语料
- 一个纯 Python 实现的 BM25 检索器
- 一个离线抽取式回答基线
- 回答质量和检索质量评测
- 一个简单的失败案例分类逻辑
- 一个实验运行脚本

这一版不依赖 API Key，可以直接在本地运行。

## 仓库结构

```text
.
|-- configs/
|   `-- tech_docs_experiment.json
|-- data/
|   `-- tech_docs_demo/
|       |-- corpus.jsonl
|       `-- questions.jsonl
|-- reports/
|   |-- failure_analysis_template.md
|   |-- github_publish_checklist.md
|   |-- portfolio_roadmap.md
|   `-- tech_docs_dataset_plan.md
|-- scripts/
|   `-- run_experiment.py
|-- src/
|   `-- techdoc_rag/
|       |-- __init__.py
|       |-- evaluate.py
|       |-- failure_analysis.py
|       |-- generator.py
|       |-- io_utils.py
|       |-- pipeline.py
|       |-- retriever.py
|       |-- tokenize.py
|       `-- types.py
|-- tests/
|   |-- test_evaluate.py
|   `-- test_retriever.py
|-- .gitignore
|-- LICENSE
|-- pyproject.toml
`-- README.md
```

## 快速开始

### 运行 demo 实验

```bash
python scripts/run_experiment.py --config configs/tech_docs_experiment.json
```

### 运行测试

```bash
python -m unittest discover -s tests
```

### 查看输出结果

实验结果默认会写到：

```text
artifacts/tech_docs_demo_results.json
```

## 数据格式

### 文档样本

```json
{"doc_id":"doc-1","title":"...","text":"...","source":"...","domain":"..."}
```

### 问答样本

```json
{
  "question_id": "q-1",
  "question": "...",
  "gold_answer": "...",
  "gold_doc_ids": ["doc-1"]
}
```

## 我现在比较关心的问题

这个项目后面我会重点看几件事：

- 检索命中了，为什么答案还是不完整
- 不同 chunk 策略会不会影响技术文档问答效果
- 关键词检索和语义检索分别在哪些问题上更占优势
- 模型会不会把相似命令、相似参数或相似工具搞混

这些问题比单纯把系统跑起来更值得做。

## 后续准备怎么扩展

下一步我会先把 demo 数据扩成一个更像样的小 benchmark，优先考虑这些方向：

- Git 工作流文档
- Linux 命令行文档
- Docker 与容器相关文档
- Python / PyTorch 中文文档

比较现实的迭代顺序大概是：

1. 扩展语料和问答样本
2. 对比 BM25、稠密检索和混合检索
3. 加入 reranker
4. 接入真实 LLM，并要求回答引用检索证据
5. 补更多评测指标和错误分析

## 当前版本说明

这一版更像一个可运行的起点，而不是最终系统。代码和文档我都尽量写得直接一点，方便后面继续改，也方便回头看每一轮实验到底改了什么。
