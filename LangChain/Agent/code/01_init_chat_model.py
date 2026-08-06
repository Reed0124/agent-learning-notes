"""
01 模型的初始化以及调用

模型的调用方法
1、invoke(): 阻塞式，一次性返回完整的结果
2、stream(): 阻塞式，流式输出，实时返回每个token
3、batch(): 阻塞式，批量处理多个输入
以及它们的异步版本
4、ainvoke()
5、astream()
6、abatch()

"""

# 调用Deepseek的模型
import os

from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_deepseek import ChatDeepSeek
from rich import print as rprint

# 读取配置文件中的.env文件 (后续初始化模型的时候可以不加api和url参数，自动检测)
from dotenv import load_dotenv
load_dotenv(override=True)

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL")

model = ChatDeepSeek(
    model="deepseek-v4-flash",
    # api_key=DEEPSEEK_API_KEY,
    # api_base=DEEPSEEK_BASE_URL,
    extra_body={
        # "thinking": {"type": "disabled"},
        "enable_search": True

    }

)

# model = init_chat_model(
#     model="deepseek-v4-flash", # 模型名称
#     api_key=DEEPSEEK_API_KEY,
#     base_url=DEEPSEEK_BASE_URL,
#     temperature=0.7, # 模型温度，范围0-1，默认0.7
#
#     # extra_body={
#     #     # "thinking": {"type": "disabled"},
#     #     "enable_search": True
#     #
#     # }
# )

# 调用模型
# 1、入参字符串
# response1 = model.invoke("巴威台风对苏州的影响如何")

# 2、字典列表 (多轮对话场景)
messages = [
    {"role": "system", "content": "你是一个话少的助手"},
    {"role": "user", "content": "2026年有两位华人获得了菲尔兹奖是谁"},
    # {"role": "assistant", "content": "好的，正在查找"}
]
response2 = model.invoke(messages)
rprint(response2)

# 3、消息对象列表
# message_list = [
#     SystemMessage(content="你是一个话少的助手"),
#     HumanMessage(content="巴威台风对苏州的影响如何"),
#     # AIMessage(content="好的，正在查找")
# ]
# response3 = model.invoke(message_list)
# print(response3.content)
# print(response3.content_blocks)















