# 中文技术文档 RAG 实验室

`Chinese TechDoc RAG Lab` 是一个面向中文计算机技术文档问答的 RAG 实验项目。这个仓库的目标不是做一个“能聊两句的 AI 页面”，而是做一个可以上传到 GitHub、能够体现研究潜力和工程能力的项目。

项目当前重点放在 4 件事上：

- 可复现实验
- 检索与回答分开评测
- 失败案例分析
- 从离线基线逐步演化到真实 LLM RAG 系统

## 项目定位

这个项目更适合这样介绍：

`一个面向中文计算机技术文档的 RAG 评测平台，包含基准构建、检索器对比和失败案例分析。`

相比“我做了一个问答机器人”，这种表述更强，因为它强调的是：

- 你会构建数据集
- 你会设计实验
- 你会分析系统表现
- 你会根据错误迭代改进

这类能力更接近导师会重视的研究训练潜力。

## 为什么选“计算机技术文档”这个方向

中文计算机技术文档非常适合做申请向项目，原因有几个：

- 和计算机专业直接相关
- 术语精确，适合检索和对齐评测
- 既有概念型问题，也有步骤型问题
- 比泛知识问答更容易构建高质量 benchmark

这个领域还能自然引出很多有价值的问题，比如：

- 为什么检索命中了，答案还是不完整？
- 不同 chunk 策略会不会影响命令行文档问答效果？
- 关键词检索和语义检索各自在什么问题上更强？
- 模型是否会把相似命令或参数混淆？

## 当前版本包含什么

当前仓库已经提供一套可直接运行的基线：

- 一个中文技术文档演示语料集
- 纯 Python 实现的 BM25 检索器
- 一个离线抽取式回答基线
- 回答质量与检索质量评测
- 启发式失败案例分类
- 一个实验运行脚本

这一版不依赖任何 API Key，可以直接在本地跑通。

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
|   |-- portfolio_roadmap.md
|   `-- tech_docs_dataset_plan.md
|-- scripts/
|   `-- run_experiment.py
|-- src/
|   `-- chinese_rag_lab/
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

### 1. 运行技术文档 demo 实验

```bash
python scripts/run_experiment.py --config configs/tech_docs_experiment.json
```

### 2. 运行测试

```bash
python -m unittest discover -s tests
```

### 3. 查看实验结果

实验结果会输出到：

```text
artifacts/tech_docs_demo_results.json
```

## 数据格式

### 文档样本格式

```json
{"doc_id":"doc-1","title":"...","text":"...","source":"...","domain":"..."}
```

### 问答样本格式

```json
{
  "question_id": "q-1",
  "question": "...",
  "gold_answer": "...",
  "gold_doc_ids": ["doc-1"]
}
```

## 技术文档 benchmark 应该怎么设计

一个更像样的技术文档问答 benchmark，不应该只有“查概念”这一种题。建议至少混合下面几类：

- 概念解释题
- 步骤执行题
- 参数或选项题
- 故障排查题
- 工具对比题

这样做的好处是，你后面分析系统错误时会更有内容，而不是只报一个准确率数字。

## 适合扩展的数据源方向

这个项目后续最好先专注一个小领域，不要一开始把所有技术文档混在一起。比较推荐：

- Git 工作流文档
- Linux 命令行文档
- Docker 与容器部署文档
- Python / PyTorch 中文文档
- 数据库运维与排错文档

只要你把一个小方向做深，质量往往比“什么都沾一点”更高。

## 推荐迭代路线

1. 把技术文档语料扩展到 50 到 100 篇
2. 构建 30 到 50 条带金标准引用的问答
3. 对比 BM25、稠密检索和混合检索
4. 加入 reranker，并分析它什么时候真正有帮助
5. 接入真实 LLM，并强制要求引用检索证据
6. 扩展评测指标，例如 recall@k、MRR、faithfulness 和错误类型统计

## 这个项目为什么适合放到 GitHub

因为它天然能持续迭代，并且每一次迭代都能留下很清楚的“研究痕迹”：

- benchmark 表格
- 检索对比实验
- prompt 变体
- 失败案例报告
- 配置化实验
- 测试与 CI

这比单纯上传一个“聊天网页”更像一个长期认真维护的技术项目。

## 版本里程碑建议

- `v0.1`：技术文档上的 BM25 + 抽取式基线
- `v0.2`：加入稠密检索与 reranking
- `v0.3`：加入带引用的真实 LLM 回答
- `v0.4`：加入自动化事实一致性评测和详细错误报告

## 适合作为简历描述的一句话

可以把这个项目写成：

`构建了一个面向中文计算机技术文档的 RAG 评测平台，完成技术文档数据集设计、BM25 检索基线实现、回答质量评测与失败案例分析。`

