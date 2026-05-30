# Agent
##  Agent 与 Chain 关系
Chain = 固定流程的流水线<br>
Agent = 会思考、会决策、会自己选工具的智能体<br>
Agent 内部 包含并使用 很多 Chain<br>

## ReAct （Reasoning + Action）
Reasoning → Action → 拿到结果 → 再次 Reasoning → 再次 Action … 直到出最终答案<br>

## middleware<br>
````
1、Agent执行前 @before_agent
2、Agent执行后 @after_agent
3、model执行前 @before_model
4、model执行后 @after_model
5、model执行中 @wrap_model_call
6、工具执行中 @wrap_tool_call
````
