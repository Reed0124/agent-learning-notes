"""
name: StrOutputParser()
function: 将AIMessage对象（model invoke后的结果）拆解为简单字符串
"""
from http.client import responses

from langchain_core.output_parsers import StrOutputParser
from langchain_deepseek import ChatDeepSeek
from langchain_core.prompts import PromptTemplate

model = ChatDeepSeek(model="deepseek-v4-flash")
prompt_template = PromptTemplate.from_template("我姓{name}，性别{gender}，帮我起一个英文名字")

parser = StrOutputParser()
chain = prompt_template | model | parser | model | parser
response = chain.invoke ({"name": "李", "gender": "男"})
print(response)
print(type(response))
