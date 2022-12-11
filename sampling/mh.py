# -*- coding:utf-8 -*-
# メトロポリス・ヘイスティング法
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt;

# 事前分布として、N(2,4) を与える
def prior_pdf(x):
    return stats.norm.pdf(x, loc=2, scale=2)

# 尤度として、N(1,1) を考える
def likelyhood_pdf(x):
    return stats.norm.pdf(x, loc=-1, scale=1)

# 事後分布に比例する関数として、以下を与える
# 実際の事後分布は、積分結果が1になるように定数がつくが、ここでは無視
# そのため、「比例する」と表現した
def target_pdf(x):
    return prior_pdf(x) * likelyhood_pdf(x)

# MHの本丸
class Metropolis():
    def __init__(self, target_pdf):
        self.x = 1 # 初期値
        self.target = target_pdf

    # 提案分布から値を計算する
    # ここでは、N(x, 1)を提案分布とする
    def proposal(self, x):
        return np.random.normal(loc=x)

    # 1ステップ  
    def step(self):
        x0 = self.x
        x1 = self.proposal(self.x)

        p0 = self.target(x0)
        p1 = self.target(x1)

        a = min(p1 / (p0 + 1.0e-12), 1.0)
        
        if np.random.rand() < a:
            self.x = x1
        else:
            self.x = x0

        return self.x


model = Metropolis(target_pdf)
data = []

for i in range(5000):
    data.append(model.step())

plt.hist(data)
plt.show()
