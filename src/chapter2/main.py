from math import sqrt
from data import critics
import similarity as sim
import numpy_sim as nsim
from recommendations import top_matches
from recommendations import get_recommendations
from recommendations import transform_profs

# 欧几里得距离评价
euclid1 = sim.sim_euclid(critics, 'Lisa Rose', 'Gene Seymour')
euclid2 = nsim.sim_euclid(critics, 'Lisa Rose', 'Gene Seymour')
print("欧几里得距离评价:")
print(euclid1)
print(euclid2)

# 皮尔逊相关度评价
pearson1 = sim.sim_pearson(critics, 'Lisa Rose', 'Gene Seymour')
pearson2 = nsim.sim_pearson(critics, 'Lisa Rose', 'Gene Seymour')
print("皮尔逊相关度评价:")
print(pearson1)
print(pearson2)

# 余弦相似度评价
cosine1 = nsim.sim_cosine(critics, 'Lisa Rose', 'Gene Seymour')
print("余弦相似度评价:")
print(cosine1)

# jaccard相似度评价: 这个例子说明了jaccard在此场景下的不精确性，虽然二者所评价的电影集合都相同，但是评分不同的差异被忽略了。
jaccard1 = sim.sim_jaccard(critics, 'Lisa Rose', 'Gene Seymour')
print("jaccard相似度评价:")
print(jaccard1)

# 基于商品的评价
movie_pearson = top_matches(transform_profs(critics), 'Superman Returns', similarity=sim.sim_pearson, n=5)
print(movie_pearson)
