import numpy as np
import matplotlib.pyplot as plt

DATA_SIZE = 50


def ar_p(params):
    data = np.zeros(DATA_SIZE)
    noise = np.random.normal(0, 1, DATA_SIZE)

    for i in range(len(params), DATA_SIZE):
        for j in range(len(params)):
            data[i] += params[j] * data[i-1-j]
        data[i] += noise[i-1-j]

    return data

def plot_ar_1():
    plt.subplot(2,2,1)
    plt.plot(ar_p([-0.6]))
    plt.subplot(2,2,2)
    plt.plot(ar_p([0]))
    plt.subplot(2,2,3)
    plt.plot(ar_p([0.4]))
    plt.subplot(2,2,4)
    plt.plot(ar_p([0.9]))
    plt.show()


def plot_ar_p():    
    plt.subplot(2,2,1)
    plt.plot(ar_p([0.2]))
    plt.subplot(2,2,2)
    plt.plot(ar_p([0.1, 0.9]))
    plt.subplot(2,2,3)
    plt.plot(ar_p([0.9, 0.1]))
    plt.subplot(2,2,4)
    plt.plot(ar_p([0.5, -0.5, 0.5]))
    plt.show()

#plot_ar_1()
plot_ar_p()

