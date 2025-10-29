# RAG Project 1 - My Version

本项目基于原作者的 note/ 版本修改而来：[原作者仓库](https://github.com/lichuachua/llms-project/tree/main/LangChain_RAG/llms-2/)。

在此基础上，我做了以下改动：

## 改动内容

**功能相关**：

- 更改检索文件为 *Google Prompt Guidance*
- 更新为 Ollama 本地部署大模型支持
- 增加 API 请求大模型的轻量方法
- 增加两个 *test.py* 文件，方便测试 API 请求和 Ollama 部署

**环境与依赖**：

- 检查并更新所有依赖版本
- 新增 *requirements.txt* 存储必要依赖

**代码与文档**：

- 对 *indexer.py* 增加更多注释
- 重构代码结构，便于维护
- 增加详细注释和文档

## 使用方法

### 环境准备

```bash
pip install -r requirements.txt
```

### 前置准备

#### 使用 API 模式

前往 [阿里云百炼平台](https://modelstudio.console.alibabacloud.com/?tab=api#/api/?type=model&url=2712195) 注册并申请 API Key。

#### 使用本地 Ollama 模式

1. 前往 [Ollama 官网](https://ollama.com/download) 下载并安装 Ollama。
2. 拉取所需模型，例如：

```bash
ollama pull deepseek-r1:1.5b
```

### 运行示例

> 以下示例展示了如何分别运行 API 模式和 Ollama 本地模式的测试与实战脚本。请根据你选择的模式运行对应的文件。

```bash
# 生成向量库
python indexer.py #本项目已生成向量库，因此也可以不运行此条

# 测试 API 请求
python test/test_LLM_api.py

# API 结合 RAG 实战
python rag_api_ver.py

# 测试 Ollama 部署
python test/test_LLM_ollama.py

# Ollama 本地化部署大模型 结合 RAG 实战
python rag_ollama_ver.py
