# from langchain_community.embeddings import DashScopeEmbeddings
# import config_data as config
# model = DashScopeEmbeddings(model=config.embedding_model_name)
# print(model)


from langchain_community.embeddings import DashScopeEmbeddings
import config_data as config
import os

print("检查环境变量:")
print(f"DASHSCOPE_API_KEY 已设置: {'是' if os.getenv('DASHSCOPE_API_KEY') else '否'}")
print()

model = DashScopeEmbeddings(model=config.embedding_model_name)
print(f"Model 实例: {model}")
print()

try:
    result = model.embed_query("你好")
    print(f"嵌入成功! 向量维度: {len(result)}")
    print(f"前5个值: {result[:5]}")
except Exception as e:
    print(f"嵌入失败: {type(e).__name__}: {e}")