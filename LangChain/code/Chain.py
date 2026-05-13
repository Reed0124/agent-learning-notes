from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_deepseek import ChatDeepSeek

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个助手"),
        MessagesPlaceholder(variable_name="history"),
        ("human", "我是谁")
    ]
)

history_data = [
    ("human", "我是Reed")
]

llm = ChatDeepSeek(model="deepseek-v4-flash")

chain = chat_prompt_template | llm
print(chain.invoke({"history": history_data}).content)

for chunk in chain.stream({"history": history_data}):
    print(chunk.content, end="", flush=True)