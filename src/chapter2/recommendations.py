from similarity import sim_pearson


# 选出与person喜好最相同的n个人 (属于人的匹配)
def top_matches(data, person="Tony", n=5, similarity=sim_pearson):
    scores = [(similarity(data, person, other), other) for other in data if other != person]
    scores.sort()
    scores.reverse()
    return scores[0:n]


# 根据用户的协作过滤
# 根据评论者相似度作为权重，推荐电影
def get_recommendations(data, person, similarity=sim_pearson):
    totals = {}
    sim_sums = {}
    for other in data:
        if other == person:
            continue
        sim = similarity(data, person, other)

        # 忽略评价值为零或小于零的情况
        if sim < 0:
            continue
        for item in data[other]:
            if item not in data[person] or data[person][item] == 0:
                # 相似度*评价值
                totals.setdefault(item, 0)
                totals[item] += data[other][item] * sim
                # 相似度之和
                sim_sums.setdefault(item, 0)
                sim_sums[item] += sim
    # 建立一个归一化的列表
    rankings = [(total / sim_sums[item], item) for (item, total) in totals.items()]
    rankings.sort()
    rankings.reverse()
    return rankings


# 商品的匹配,我们找出相似的电影的时候。将商品和人兑换位置
def transform_profs(data):
    result = {}
    for person in data:
        for item in data[person]:
            result.setdefault(item, {})
            result[item][person] = data[person][item]

    return result


# 基于物品的协作过滤
# 构造物品比较数据集
def calculate_similar_items(data, n=10):
    result = {}
    items = transform_profs(data)
    for item in items:
        scores = top_matches(items, item, n=n, similarity=sim_pearson)
        result[item] = scores
    return result


# 基于物品的协作型过滤获得推荐电影
def get_recommended_items(data, similar_items, user):
    user_ratings = data[user]
    scores = {}
    total_sim = {}
    for (item, rating) in user_ratings.items:
        for (similarity, item2) in similar_items[item]:
            # 如果该用户已经对当前电影进行过评价，则跳过
            if item2 in user_ratings:
                continue

            # 评价值与相似度的加权和
            scores.setdefault(item2, 0)
            scores[item2] += similarity * rating

            # 全部相似度之和
            total_sim.setdefault(item2, 0)
            total_sim[item2] += similarity
    rankings = [(score / total_sim[item], item) for item, score in scores.items()]
    rankings.reverse()
    return rankings
