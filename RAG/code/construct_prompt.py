"""
学习根据向量库检索结果，插入提示词模版，交给大模型处理
"""

from langchain_deepseek import ChatDeepSeek
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatDeepSeek(model="deepseek-v4-flash")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "以我提供的已知参考资料为主，简介的回答用户的问题，参考资料：{context}。"),
        ("user", "用户提问: {question}"),
    ]
)

vector_store = InMemoryVectorStore(
    embedding=DashScopeEmbeddings(model="text-embedding-v4")
)

# 准备向量库资料
# add_texts 传入一个list[str]
vector_store.add_texts(["减肥就是要少吃多练", "在减脂期间吃东西很重要，清淡少油控制卡路里摄入并运动起来", "跑步是很好的运动方式"])

# 检索向量库
result = vector_store.similarity_search("如何减肥", k=2)
# print(result)

reference_text = "["
for doc in result:
    reference_text += doc.page_content
reference_text += "]"
# print(reference_text)

# 打印提示词方法
def print_prompt(prompt):
    print(prompt.to_string())
    print("="*20)
    return prompt

chain = prompt | print_prompt | model | StrOutputParser()

response = chain.invoke({"question": "如何减肥", "context": reference_text})
print(response)
# print(type(response))