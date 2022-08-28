#-*- coding:utf-8 -*-

import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

# t分布
def tdist(k):
    x = np.linspace(-10, 10, 100)
    y = stats.t.pdf(x, k)
    return (x, y)

def chi2(k):
    x = np.linspace(0, 20, 400)
    y = stats.chi2.pdf(x, k)
    return (x, y)

def fdist(k1, k2):
    x = np.linspace(-20, 20, 400)
    y = stats.chi2.pdf(x, k1, k2)
    return (x, y)


if __name__ == "__main__":

    plt.subplot(2, 2, 1)
    for k in [5, 20, 100]:
        x, y = tdist(k)
        plt.plot(x, y, label=k)
    plt.title("t distribution")
    plt.legend()

    plt.subplot(2, 2, 2)
    for k in [2, 5, 10]:
        x, y = chi2(k)
        plt.plot(x, y, label=k)
    plt.title("chi2 distribution")
    plt.legend()

    plt.subplot(2, 2, 3)
    x, y = fdist(5, 10)
    plt.plot(x, y)
    plt.title("F distribution")
    plt.legend()

    plt.show()
