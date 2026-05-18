from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader
from langchain_chroma import Chroma


# 内存向量存储
# vector_store = InMemoryVectorStore(
#     embedding = DashScopeEmbeddings()
# )

# 轻量级数据库Chroma数据库存储
vector_store = Chroma(
    collection_name="test",
    embedding_function=DashScopeEmbeddings(),
    persist_directory="../../resources/db/" # 指定数据存放的文件夹
)

loader = CSVLoader(
    file_path = "../../resources/test.csv",
    encoding="utf-8",
    source_column="source"
)

my_list = loader.load()
# print(type(my_list), my_list[0], type(my_list[0]))

# 新增
vector_store.add_documents(
    documents = my_list, # 被添加的文档，类型为 list[Document]
    ids=["id" + str(i) for i in range(1, len(my_list)+1)]
)

# 删除
# vector_store.delete("id1")

# 查询 Return: List[Document]
result = vector_store.similarity_search("lice", k=3)

print(result)


