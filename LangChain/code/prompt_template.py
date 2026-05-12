from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_deepseek import ChatDeepSeek

# zero-shot的通用提示词模版
prompt = PromptTemplate.from_template(
    "我的名字是{name}，我喜欢学{language}"
)

# prompt_text = prompt_template.format(name="Reed", language="Python")
# print(prompt_text)

llm = ChatDeepSeek(
    model="deepseek-v4-flash",
)

# chain = prompt | llm
# print(chain.invoke({"name": "Reed", "language": "Python"}))


# few-shot的提示词模版

examples = [
    {"input": "Reed", "output": "Python"},
    {"input": "James", "output": "Java"},
    {"input": "Lucy", "output": "C++"},
]

few_shot_prompt = FewShotPromptTemplate(
    example_prompt = prompt,
    examples = examples,
    prefix = "请从以下的例子中选择最匹配的答案",
    suffix = "Alice喜欢学{language}",
    input_variables = ["language"],

)