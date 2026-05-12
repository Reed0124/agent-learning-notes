from langchain_deepseek import ChatDeepSeek
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# 初始化大模型
llm = ChatDeepSeek(
    model="deepseek-v4-flash",
)

messages = [
    SystemMessage(content="你是一个话少的助手"),
    HumanMessage(content="你是谁"),
    ("ai", "我是一个助手")
]

# print(llm.invoke(messages))

# 流式调用
# responses = llm.stream(messages)
# for chunk in responses:
#     print(chunk.content, flush=True, end="")

# ============================================================================

from langchain_community.embeddings import DashScopeEmbeddings

# 初始化文本嵌入模型
embed = DashScopeEmbeddings(model="text-embedding-v1")

# print(embed.embed_query("我喜欢你"))
# print(embed.embed_documents(["我喜欢你", "你喜欢我", "我们喜欢一起玩"]))
