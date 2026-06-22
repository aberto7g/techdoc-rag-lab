# 技术文档数据集设计建议

## 推荐项目范围

第一阶段最好只做一个集中的技术文档子领域，不要一开始把很多工具混在一起。

比较适合起步的方向：

- Git 工作流
- Linux 命令行使用
- Docker 部署基础
- PyTorch 训练流程

最好的选择通常是：你愿意深入读、也愿意认真标注的那个方向。

## 建议的文档 schema

每个文档 chunk 最少建议保留：

- `doc_id`
- `title`
- `text`
- `source`
- `domain`

后面可以逐步扩展成：

- `section_path`
- `tool_name`
- `version`
- `task_type`

这些字段在后面做检索分析、过滤实验和错误归因时会非常有用。

## 建议的问题类型

问答样本至少覆盖 4 类：

- 概念题
- 步骤题
- 参数 / 选项题
- 故障排查题

例如：

- `git rebase` 主要解决什么问题？
- 递归搜索并显示行号时，`grep` 常用哪些选项？
- Docker 数据卷为什么有用？
- PyTorch 中 `DataLoader` 的作用是什么？

## 做结果分析时要问的问题

拿到实验结果以后，建议优先问自己这些问题：

- 是不是检索阶段就没找到正确 chunk？
- 检索到了正确 chunk，但回答阶段没抽出来？
- 答案是不是漏掉了关键步骤或关键约束？
- 模型是不是把相似命令或相似参数混淆了？

这些问题会直接决定你下一步该优化 retriever、generator 还是 prompt。

## 适合这个领域的错误标签

- `retrieval_miss`
- `generation_failure`
- `partial_answer`
- `missing_step`
- `option_confusion`
- `tool_confusion`

## 一个比较像样的公开版本规模

如果你想先做出一个足够能发 GitHub 的版本，比较合理的规模是：

- 50 到 100 个技术文档 chunk
- 30 到 50 条问答样本
- 2 到 3 个检索基线
- 1 份简洁但有代表性的错误分析报告

做到这个程度，再把 README 和实验记录写好，项目已经会很像一个认真准备过的申请项目。

