# -*- coding:utf-8 -*-
# ギブスサンプリング法
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt;


# 必要な分布の分布はわからないが、
# 各変数の周辺分布はわかるような場合にGibbsSamplingを利用する

# ここでは、共分散cov, 分散1, 平均(0, 0)の2次元確率密度関数を求めたいものとする
# この場合、周辺分布は1次元確率密度関数となる
# 参照：https://research.miidas.jp/2019/12/mcmc%E5%85%A5%E9%96%80-gibbs-sampling/

def gibbs(N):
    cov = -0.5
    x1_arr = []
    x2_arr = []
    x1 = 0.0
    x2 = 0.0
    for i in range(N):
        x1 = np.random.normal(cov*x2, 1) # 周辺分布は平均cov*0.2の正規分布になる
        x2 = np.random.normal(cov*x1, 1) # 周辺分布は平均cov*0.2の正規分布
        x1_arr.append(x1)
        x2_arr.append(x2)
    return np.array(x1_arr), np.array(x2_arr)


def main():

    x1_arr, x2_arr = gibbs(2000)

    plt.scatter(x1_arr[1000:], x2_arr[1000:])
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()

if __name__ == '__main__':
    main()