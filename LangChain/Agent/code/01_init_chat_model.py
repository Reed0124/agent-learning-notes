"""
01 模型初始化的方法
"""

# 调用Deepseek的模型
import os

from langchain.chat_models import init_chat_model
from langchain_deepseek import ChatDeepSeek

# 读取配置文件中的.env文件 (后续初始化模型的时候可以不加api和url参数，自动检测)
from dotenv import load_dotenv
load_dotenv(override=True)

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL")

# 创建Deepseek的模型
llm = ChatDeepSeek(
    model="deepseek-v4-flash",
    # api_key=DEEPSEEK_API_KEY,
    # api_base=DEEPSEEK_BASE_URL,
)

# langchain 1.0 提供了统一初始化模型的方法 init_chat_model
model = init_chat_model(
    model="deepseek-v4-flash", # 模型名称
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL,
    temperature=0.7, # 模型温度，范围0-1，默认0.7
)

response = model.invoke("巴威台风对苏州的影响如何")
print(response)