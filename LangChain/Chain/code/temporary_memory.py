"""
name: RunnableWithMessageHistory
function: 将一个chain转换为带有历史记录功能的chain(内存临时存储)
Args: chain

name: InMemoryChatMessageHistory
function: 生成对话实例，一般一个session_id对应一个实例
"""

from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_deepseek import ChatDeepSeek
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

model = ChatDeepSeek(model="deepseek-v4-flash")

# prompt = PromptTemplate.from_template(
#     "你需要根据会话历史回应用户问题。对话历史: {chat_history}, 用户提问: {input}, 请回答"
# )

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你需要根据会话历史简短的回应用户问题。"),
        MessagesPlaceholder("chat_history"),
        ("user", "用户提问: {input}, 请回答")
    ]
)


base_chain = prompt | model | StrOutputParser()

store = {}  # key: session_id, value: InMemoryChatMessageHistory

def get_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


chain = RunnableWithMessageHistory(
    base_chain,      # 需要转换的chain
    get_history,     # 获取指定session的InMemoryChatMessageHistory对象
    input_messages_key="input",  # 输入消息的key
    history_messages_key="chat_history"  # 历史记录的key
)

if __name__ == "__main__":
    session_config = {
        "configurable": {
            "session_id": "user_01"
        }
    }
    print(chain.invoke({"input": "你好,我叫Reed"}, session_config))
    print(chain.invoke({"input": "我是谁"}, session_config))



