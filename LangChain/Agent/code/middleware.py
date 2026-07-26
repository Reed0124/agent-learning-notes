from langchain.agents import AgentState, create_agent
from langchain.agents.middleware import before_agent, after_agent, before_model, after_model, wrap_model_call, \
    wrap_tool_call
from langchain.chat_models import init_chat_model
from langchain_core.tools import tool
from langchain_deepseek import ChatDeepSeek
from langgraph.runtime import Runtime

from rich import print as rprint


@tool(description="查询天气,传入城市名称字符串")
def get_weather(city: str) -> str:
    return "天气是晴天"

"""
1、Agent执行前 @before_agent
2、Agent执行后 @after_agent
3、model执行前 @before_model
4、model执行后 @after_model
5、model执行中 @wrap_model_call
6、工具执行中 @wrap_tool_call
"""

@before_agent
def log_before_agent(state: AgentState, runtime: Runtime) -> None:
    print(f"[before_agent], 附带{len(state["messages"])}条消息")

@after_agent
def log_after_agent(state: AgentState, runtime: Runtime) -> None:
    print(f"[after_agent], 附带{len(state['messages'])}条消息")

@before_model
def log_before_model(state: AgentState, runtime: Runtime) -> None:
    print(f"[before_model], 附带{len(state['messages'])}条消息")

@after_model
def log_after_model(state: AgentState, runtime: Runtime) -> None:
    print(f"[after_model], 附带{len(state['messages'])}条消息")

@wrap_model_call
def model_call_hook(request, handler):
    print("[wrap_model_call]")
    return handler(request)

@wrap_tool_call
def monitor_tool(request, handler):
    print(f"[wrap_tool_call], 使用了{request.tool_call["name"]}")
    print(f"[wrap_tool_call], 工具执行参数{request.tool_call["args"]}")
    return handler(request)

agent = create_agent(
    model=init_chat_model(model="deepseek-v4-flash"),
    tools=[get_weather],
    middleware=[log_before_agent, log_after_agent, log_before_model, log_after_model, model_call_hook, monitor_tool],
    system_prompt="你是一个话少的助手"
)

response = agent.invoke(
    {
        "messages": [
            {"role": "user", "content": "明天杭州天气如何？"}
        ]
    }
)

rprint(response)