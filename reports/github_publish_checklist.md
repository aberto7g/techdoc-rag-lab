# GitHub 发布检查清单

## 发布前建议检查

- README 是否已经改成你自己的项目介绍
- `pyproject.toml` 中作者名是否正确
- demo 数据里是否有不适合公开的内容
- 实验命令和测试命令是否还能正常运行
- `.gitignore` 是否已经忽略了 `artifacts/` 等本地产物

## 建议的首次提交内容

首次上传 GitHub 时，建议至少包含这些内容：

- `README.md`
- `LICENSE`
- `src/`
- `scripts/`
- `configs/`
- `data/tech_docs_demo/`
- `tests/`
- `reports/`

## Windows 下常用上传命令

如果你还没初始化仓库，可以在 `D:\RAG` 下执行：

```bash
git init
git add .
git commit -m "init: bootstrap chinese tech-doc rag lab"
```

然后在 GitHub 上创建一个空仓库，再执行：

```bash
git remote add origin <你的仓库地址>
git branch -M main
git push -u origin main
```

## 推荐仓库名称

- `chinese-techdoc-rag-lab`
- `techdoc-rag-benchmark`
- `cn-tech-rag-eval`

## 发布后第一批可以继续补的内容

- 项目架构图
- benchmark 结果表
- 更多真实技术文档样本
- 一轮错误分析报告
- GitHub Actions CI

