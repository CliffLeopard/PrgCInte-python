import numpy as np
import scipy.stats as sc
import scipy.spatial.distance as dis


def get_sim(data, p1, p2):
    sim = []
    for item in data[p1]:
        if item in data[p2]:
            sim.append(item)
    return sim


# 得到两个数据向量
def get_vector(data, sim, person1, person2):
    vector1 = [data[person1][item] for item in sim]
    vector2 = [data[person2][item] for item in sim]
    return np.array(vector1), np.array(vector2)


# 欧几里得距离评价 (1/1+dx)
def sim_euclid(data, person1, person2):
    sim = get_sim(data, person1, person2)
    if len(sim) == 0:
        return 0
    (vector1, vector2) = get_vector(data, sim, person1, person2)
    dist = np.sqrt(np.sum(np.square(vector1 - vector2)))
    return 1 / (1 + dist)


# 余弦相似度距离评价
def sim_cosine(data, person1, person2):
    sim = get_sim(data, person1, person2)
    if len(sim) == 0:
        return 0
    (vector1, vector2) = get_vector(data, sim, person1, person2)
    distance = np.dot(vector1, vector2) / (np.linalg.norm(vector1) * (np.linalg.norm(vector2)))
    return distance


# 皮尔逊相关性评价
def sim_pearson(data, person1, person2):
    sim = get_sim(data, person1, person2)
    if len(sim) == 0:
        return 0
    (vector1, vector2) = get_vector(data, sim, person1, person2)
    # 使用numpy实现皮尔逊相关性评价
    distance = np.corrcoef(vector1, vector2)[0][1]
    # 使用scipy实现皮尔逊相关性评价
    # distance = sc.pearsonr(vector1, vector2)[0]
    return distance
