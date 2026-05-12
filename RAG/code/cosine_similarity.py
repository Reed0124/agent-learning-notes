
# 计算两个向量的余弦相似度实现

import numpy

def get_dot(vec_a, vec_b):
    """
    计算两个向量的点积（两个相当同维度数字乘积之和）
    :param vec_a: 向量a
    :param vec_b: 向量b
    :return: 返回两个向量点积
    """
    if len(vec_a) != len(vec_b):
        raise ValueError("两个向量的维度不一致")

    dot_sum = 0
    for a, b in zip(vec_a, vec_b):
        dot_sum += a * b

    return dot_sum

def get_norm(vec_a):
    """
    计算单个向量的模长（对向量的每个数字求平方 再求和 再开根号）
    :param vec_a: 向量a
    :return: 返回单个向量模长
    """
    sum_square = 0
    for a in vec_a:
        sum_square += a ** 2

    return numpy.sqrt(sum_square)

def get_cosine_similarity(vec_a, vec_b):
    """
    计算两个向量的余弦相似度
    :param vec_a: 向量a
    :param vec_b: 向量b
    :return: 返回两个向量的余弦相似度
    """
    dot = get_dot(vec_a, vec_b)
    norm_a = get_norm(vec_a)
    norm_b = get_norm(vec_b)

    return dot / (norm_a * norm_b)

# 测试
if __name__ == '__main__':
    vec_a = [1, 2, 3]
    vec_b = [2, 3, 4]
    vec_c = [1, 2]
    vec_d = [2, 4]
    vec_e = [-1, -2]
    print(get_cosine_similarity(vec_a, vec_b))
    print(get_cosine_similarity(vec_c, vec_d))
    print(get_cosine_similarity(vec_c, vec_e))
    # print(get_cosine_similarity(vec_a, vec_c))


