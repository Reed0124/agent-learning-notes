"""
RunnablePassthrough && as_retriever()

function: 将向量检索入Chain

"""
from langchain_core.documents import Document
from langchain_core.runnables import RunnablePassthrough
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

# 准备向量库资料 add_texts 传入一个list[str]
vector_store.add_texts(["减肥就是要少吃多练", "在减脂期间吃东西很重要，清淡少油控制卡路里摄入并运动起来", "跑步是很好的运动方式"])

# 返回一个Runnable接口对象
retriever = vector_store.as_retriever(search_kwargs={"k": 2})

"""
retriever:
    Input: 用户的提问    type: str
    Return: 向量库的检索结果    type: List[Document]

prompt:
    Input: 用户的提问 + 向量库的检索结果    type: dict
    Return: 完整的提示词    type: PromptValue
"""

def format_func(doc_list: list[Document]):
    if not doc_list:
        return "无参考资料"

    formatted_str = "["
    for doc in doc_list:
        formatted_str += doc.page_content
    formatted_str += "]"

    return formatted_str

# 打印提示词方法
def print_prompt(prompt):
    print(prompt.to_string())
    print("="*20)
    return prompt

chain = {
    "question": RunnablePassthrough(),
    "context": retriever | format_func } | prompt | print_prompt | model | StrOutputParser()

response = chain.invoke("如何减肥")
print(response)