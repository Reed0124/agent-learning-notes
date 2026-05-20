"""
知识库
"""

import os


def check_md5():
    """
    检查传入的md5字符串是否已经被处理过了
    """
    pass

def save_md5():
    """
    将传入的md5字符串，记录到文件中保存
    """
    pass

def get_string_md5():
    """
    获取传入的字符串转换为md5字符串
    """
    pass


class KnowledgeBaseService(object):
    """
    知识库服务
    """
    def __init__(self):
        self.chroma = None  # chroma数据库存储的实例
        self.spliter = None # 文本分割器实例

    def upload_by_str(self, data, filename):
        """将传入的字符串，进行向量化，存入向量数据库中"""
        pass



