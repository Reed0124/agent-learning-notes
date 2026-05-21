"""
知识库
"""
import hashlib
import os
import config_data as config


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
        self.chroma = None  # chroma数据库存储的实例
        self.spliter = None # 文本分割器实例

    def upload_by_str(self, data, filename):
        """将传入的字符串，进行向量化，存入向量数据库中"""
        pass


if __name__ == '__main__':
    # r = get_string_md5("我是楞啊")
    # r2 = get_string_md5("我是人啊")
    # r3 = get_string_md5("我是人啊")
    # print(r, r2, r3)

    # save_md5("0c39c82e86a5ac0ec6c9fef235d45eb5")
    # print(check_md5("0c39c82e86a5ac0ec6c9fef235d45eb5"))

    pass

