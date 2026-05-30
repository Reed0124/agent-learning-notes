from langchain.agents import create_agent
from langchain_deepseek import ChatDeepSeek
from langchain_core.tools import tool

@tool(description="查询天气")
def get_weather() -> str:
    return "天气是晴天"

agent = create_agent(
    model=ChatDeepSeek(model="deepseek-chat"),
    tools=[get_weather],
    system_prompt="你是一个话少的助手"
)

# response = agent.invoke(
#     {
#         "messages": [
#             {"role": "user", "content": "明天杭州天气如何？"}
#         ]
#     }
# )
#
# print(response)
# print(type(response))
# for msg in response["messages"]:
#     print(msg.content, type(msg).__name__)

# 流式输出
for chunk in agent.stream(
    {
        "messages": [
            {"role": "user", "content": "明天杭州天气如何？"}
        ]
    }
):
    print(chunk)