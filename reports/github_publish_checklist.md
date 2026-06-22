# GitHub 发布检查清单

这个文件主要是给我自己发仓库之前过一遍，免得传上去以后才发现细节没收好。

## 发布前检查

- README 里的表述是不是已经改成当前版本对应的内容
- `pyproject.toml` 里的作者信息是不是对的
- demo 数据里有没有不适合公开的内容
- 实验命令和测试命令还能不能跑
- `.gitignore` 有没有忽略 `artifacts/` 这类本地产物

## 首次提交建议包含的内容

- `README.md`
- `LICENSE`
- `src/`
- `scripts/`
- `configs/`
- `data/tech_docs_demo/`
- `tests/`
- `reports/`

## 常用发布命令

如果本地还没初始化仓库，可以在 `D:\RAG` 下执行：

```bash
git init
git add .
git commit -m "init: bootstrap chinese tech-doc rag lab"
```

创建远端仓库后再执行：

```bash
git remote add origin <repo-url>
git branch -M main
git push -u origin main
```

## 后面还可以继续补的东西

- 项目结构图
- benchmark 结果表
- 更多真实技术文档样本
- 一轮完整的错误分析报告
- GitHub Actions CI

