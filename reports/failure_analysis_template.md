# 失败案例分析模板

## 实验设置

- 数据集：
- 检索器：
- 生成器：
- Top-k：
- Prompt 策略：

## 指标结果

- Retrieval hit@k：
- Answer EM：
- Answer F1：

## 错误分类

- `retrieval_miss`：正确来源文档没有被检索到
- `generation_failure`：正确文档已经检索到，但回答仍然错误
- `partial_answer`：答案只覆盖了一部分信息
- `missing_step`：答案遗漏了关键步骤
- `option_confusion`：把参数或选项用法混淆了
- `tool_confusion`：把相似工具或命令混淆了

## 代表性案例

### 案例 1

- 问题：
- 标准答案：
- 模型答案：
- 检索文档：
- 初步原因：
- 改进思路：

### 案例 2

- 问题：
- 标准答案：
- 模型答案：
- 检索文档：
- 初步原因：
- 改进思路：

## 下一轮实验建议

- 加入稠密检索或 reranker
- 优化 chunk 切分策略
- 尝试更强的引用约束 prompt
- 对比多个生成器在同一 benchmark 上的表现

