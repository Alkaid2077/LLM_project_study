from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

llm = ChatOpenAI(
    model="deepseek-r1:1.5b",   # 改成你本地下载的模型名
    api_key="ollama",           # 占位符即可
    base_url="http://localhost:11434/v1"  # Ollama 的 OpenAI 兼容端点
)

resp = llm.invoke([HumanMessage(content="用一句话介绍温度是什么")])
print(resp.content)
