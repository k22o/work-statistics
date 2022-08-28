#-*- coding:utf-8 -*-

import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

# 二項分布 n:試行回数, p:確率
def binomial(n, p):
    x = np.arange(n)
    y = stats.binom.pmf(x, n, p) #確率分布
    return (x, y)

def poisson(n, lam):
    x = np.arange(n)
    y = stats.poisson.pmf(x, lam)
    return (x, y)

def geometric(n, p):
    x = np.arange(n)
    y = stats.geom.pmf(x, p)
    return (x, y)


if __name__ == "__main__":

    plt.subplot(2, 2, 1)
    for p in [0.1, 0.5, 0.8]:
        x, y = binomial(30, p)
        plt.plot(x, y, marker='o', label=p)
    plt.title("binomial distribution")
    plt.legend()

    plt.subplot(2, 2, 2)
    for lam in [3, 5, 10]:
        x, y = poisson(40, lam)
        plt.plot(x, y, marker='o', label=lam)
    plt.title("poisson distribution")
    plt.legend()

    plt.subplot(2, 2, 3)
    for p in [0.1, 0.3, 0.7]:
        x, y = geometric(20, p)
        plt.plot(x, y, marker='o', label=p)
    plt.title("geometric distribution")
    plt.legend()

    plt.show()
