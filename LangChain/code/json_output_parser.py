"""
name: JsonOutputParser
function: 第一个提示词交给大模型处理后，将结果传入第二个提示词模版，因为模版的入参是dict格式的，需要JsonOutputParser处理，
    将AIMessage对象解析成JSON格式
Args: AIMessage(content必须为JSON格式)
Returns: dict
"""


from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_deepseek import ChatDeepSeek
from langchain_core.prompts import PromptTemplate

# 创建解析器
str_parser = StrOutputParser()
json_parser = JsonOutputParser()

# 创建模型
model = ChatDeepSeek(model="deepseek-v4-flash")

# 创建提示词模版
first_prompt = PromptTemplate.from_template("我姓{name}，性别{gender}，帮我起一个英文名字，仅回复我名字，并封装为JSON格式返回给我，key为eng_name，value是你起的名字，请严格遵守格式要求")

second_prompt = PromptTemplate.from_template("姓名是{eng_name}，请帮我解释这个名字的含义")

chain = first_prompt | model | json_parser | second_prompt | model | str_parser
# response = chain.invoke({"name": "李", "gender": "男"})
# print(response)
# print(type(response))

# 流式输出
for chunk in chain.stream({"name": "李", "gender": "男"}):
    print(chunk, end="", flush=True)