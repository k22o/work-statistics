#-*- coding:utf-8 -*-

import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

# 正規分布 ave: 平均 std: 標準偏差
def normal(ave, std):
    x_min = ave - std * 10
    x_max = ave + std * 10
    x = np.linspace(x_min, x_max, 1000)
    y = stats.norm.pdf(x, ave, std)
    return (x, y)

def exponential(n, lam):
    x = np.linspace(0.01, n, 1000)
    y = lam * np.exp(-1*lam*x)
    return (x, y)

if __name__ == "__main__":

    plt.subplot(2, 2, 1)
    x, y = normal(5, 10)
    plt.plot(x, y)
    plt.title("normal distribution")

    plt.subplot(2, 2, 2)
    for lam in [0.5, 1, 2]:
        x, y = exponential(5, lam)
        plt.plot(x, y, label=lam)
    plt.title("exponential distribution")
    plt.legend()

    plt.show()
