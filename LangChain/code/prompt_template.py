from langchain_core.prompts import PromptTemplate
from langchain_deepseek import ChatDeepSeek

# zero-shot的PromptTemplate
prompt_template = PromptTemplate.from_template(
    "我的名字是{name}，我喜欢学{language}"
)

# prompt_text = prompt_template.format(name="Reed", language="Python")

# print(prompt_text)

llm = ChatDeepSeek(
    model="deepseek-v4-flash",
)

chain = prompt_template | llm

print(chain.invoke({"name": "Reed", "language": "Python"}))