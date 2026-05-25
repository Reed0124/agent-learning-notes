from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个助手"),
        MessagesPlaceholder(variable_name="history"),
        ("human", "我是谁")
    ]
)

history_message = [
    ("human", "我是Reed")
]

prompt_text = prompt.invoke({"history": history_message}).to_string()

print(prompt_text)