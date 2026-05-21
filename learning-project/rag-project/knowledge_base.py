"""
知识库
"""
import hashlib
import os
import config_data as config
from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from datetime import datetime


def check_md5(md5_str: str):
    """检查传入的md5字符串是否已有"""
    if not os.path.exists(config.md5_path):  # 检查文件是否存在
        open(config.md5_path, 'w', encoding='utf-8').close()  # w模式自动创建文件
        return False
    else:
        with open(config.md5_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip() == md5_str:
                    return True
        return False


def save_md5(md5_str: str):
    """将传入的md5字符串保存到文件中"""
    with open(config.md5_path, 'a', encoding='utf-8') as f:
        f.write(md5_str + '\n')


def get_string_md5(input_str: str, encoding='utf-8'):
    """将传入的字符串转换为md5字符串"""
    str_bytes = input_str.encode(encoding)
    return hashlib.md5(str_bytes).hexdigest() # 返回md5的16进制字符串


class KnowledgeBaseService(object):
    """
    知识库服务
    """
    def __init__(self):
        os.makedirs(config.persist_directory, exist_ok=True) # 创建数据库存储目录, 如果已存在则不创建

        # chroma数据库存储的实例
        self.chroma = Chroma(
            collection_name=config.collection_name,
            embedding_function=DashScopeEmbeddings(model="text-embedding-v4"),
            persist_directory=config.persist_directory
        )

        # 文本分割器实例
        self.spliter = RecursiveCharacterTextSplitter(
            chunk_size=config.chunk_size, # 块大小
            chunk_overlap=config.chunk_overlap, # 块重叠
            separators=config.separators, # 自然段落分隔符
            length_function=len
        )

    def upload_by_str(self, data: str, filename):
        """
        将传入的字符串进行向量化，存入向量数据库中

        :param data: 待写入向量库的字符串
        :param filename: 文件名称，作为元数据 source 字段记录来源
        """
        # 获取传入字符串的md5
        md5_hex = get_string_md5(data)

        if check_md5(md5_hex):
            return "已存在于向量库"

        if len(data) > config.chunk_size:
            knowledge_chunks: list[str] = self.spliter.split_text(data)
        else:
            knowledge_chunks = [data]

        # 元数据, Document对象的metadata属性
        metadata = {
            "source": filename,
            "create_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), # 2025-01-01 00:00:00
            "operator": "Reed"
        }

        # 加载到向量库中
        self.chroma.add_texts(
            knowledge_chunks,
            metadatas=[metadata for _ in knowledge_chunks]
        )

        save_md5(md5_hex)
        return "内容载入向量库成功"




if __name__ == '__main__':
    # 测试md5
    # r = get_string_md5("我是楞啊")
    # r2 = get_string_md5("我是人啊")
    # r3 = get_string_md5("我是人啊")
    # print(r, r2, r3)
    # save_md5("0c39c82e86a5ac0ec6c9fef235d45eb5")
    # print(check_md5("0c39c82e86a5ac0ec6c9fef235d45eb5"))

    # 测试向量库
    kbs = KnowledgeBaseService()
    r = kbs.upload_by_str("我是一个测试字符串", "test.txt")
    print(r)



    pass

