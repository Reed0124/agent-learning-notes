"""
name: RunnableLambda()
function: 将自定义的函数转换为能在chain中通过管道执行的函数
"""

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import PromptTemplate
from langchain_deepseek import ChatDeepSeek


my_func = RunnableLambda(lambda ai_msg: {"eng_name": ai_msg.content}) # 将自定义函数转换为 RunnableLambda对象（可在链中通过管道执行）
# lambda ai_msg: {"name": ai_msg.content} 相当于如下
# def 匿名函数(ai_msg):
#     return {"name": ai_msg.content}

model = ChatDeepSeek(model="deepseek-v4-flash")

first_prompt = PromptTemplate.from_template("我姓{name}，性别{gender}，帮我起一个英文名字，仅回复我名字")
second_prompt = PromptTemplate.from_template("姓名是{eng_name}，请帮我解释这个名字的含义")

chain = first_prompt | model | my_func | second_prompt | model | StrOutputParser()
print(chain.invoke({"name": "李", "gender": "男"}))