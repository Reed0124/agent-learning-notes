import os, hashlib
from logger_handler import logger
def get_file_md5_hex(file_path: str):
    """
    获取文件的MD5的16进制字符串
    :param file_path: 文件路径
    :return: MD5的16进制字符串
    """
    if not os.path.exists(file_path):
        logger.error(f"[MD5计算] 文件 {file_path} 不存在")
        return None

    if not os.path.isfile(file_path):
        logger.error(f"[MD5计算] {file_path} 不是一个文件")
        return None

    md5_obj = hashlib.md5()

    chunk_size = 4096  # 文件4kb分片

    try:
        with open(file_path, "rb") as f: # 二进制打开文件
            while chunk := f.read(chunk_size):
                md5_obj.update(chunk)
            return md5_obj.hexdigest()

    except Exception as e:
        logger.error(f"[MD5计算] 文件 {file_path} 读取错误 {str(e)}")
        return None


def listdir_with_allowed_type():
    """
    返回文件夹内的文件列表（允许的文件后缀）
    :return:
    """
    pass

def pdf_loader():
    pass

def txt_loader():
    pass

