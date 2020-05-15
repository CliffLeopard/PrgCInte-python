from math import sqrt


# 欧几里得距离评价 (1/1+dx)
def sim_euclid(data, person1, person2):
    # 得到shared_items的列表
    si = get_sim(data, person1, person2)

    # 如果两者没有共同之处，则返回0
    if len(si) == 0:
        return 0

    # 计算所有差值的平方和
    sum_of_squares = sum(
        pow(data[person1][item] - data[person2][item], 2) for item in si.keys()
    )

    return 1 / (1 + sqrt(sum_of_squares))


# 余弦相似度
def sim_cosine(data, p1, p2):
    sim = get_sim(data, p1, p2)
    n = len(sim)
    if n == 0:
        return 0


# 皮尔逊相关性评价
def sim_pearson(data, p1, p2):
    # 找到两者都评价过的电影，存储在sim中
    sim = get_sim(data, p1, p2)
    n = len(sim)
    # 如果两者没有看过相同的电影。这里原文里返回1，我觉得是不合适的。应该返回0
    if n == 0:
        return 0

    # 分别计算都评价过的电影的评分总和
    sum1 = sum(data[p1][item] for item in sim)
    sum2 = sum(data[p2][item] for item in sim)

    # 分别计算都评价过的电影的评分的平方和（这里显然限制评分只能为正数）
    sum1_sq = sum(pow(data[p1][item], 2) for item in sim)
    sum2_sq = sum(pow(data[p2][item], 2) for item in sim)

    # 都评价过的电影的 评分的乘积之和
    p_sum = sum(data[p1][item] * data[p2][item] for item in sim)

    # 计算皮尔逊相关度评价值
    num = p_sum - (sum1 * sum2 / n)
    den = sqrt((sum1_sq - pow(sum1, 2) / n) * (sum2_sq - pow(sum2, 2) / n))
    if den == 0:
        return 0
    return num / den


# jaccard 相似度系数
def sim_jaccard(data, p1, p2):
    # 找到两者都评价过的电影，存储在sim中
    sim = get_sim(data, p1, p2)
    n = len(sim)
    len_total = len(data[p1]) + len(data[p2]) - n
    if len_total == 0:
        return 0
    return n / len_total


# 曼哈顿距离算法
def manhattan_distance(data, p1, p2):
    sim = get_sim(data, p1, p2)
    n = len(sim)
    if n == 0:
        return 1
    sum_of_distance = sum(
        abs(data[p1][item] - data[p2][item]) for item in sim.keys()
    )
    return 1 / (1 + sum_of_distance)


def sim_tanimoto(data, p1, p2):
    sim = get_sim(data, p1, p2)
    n = len(sim)
    if n == 0:
        return 1


def get_sim(data, p1, p2):
    sim = {}
    for item in data[p1]:
        if item in data[p2]:
            sim[item] = 1
    return sim
