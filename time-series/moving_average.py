import numpy as np
import matplotlib.pyplot as plt

DATA_SIZE = 50


def ma_p(params):
    data = np.zeros(DATA_SIZE)
    noise = np.random.normal(0, 1, DATA_SIZE)

    for i in range(len(params), DATA_SIZE):
        data[i] += noise[i]
        for j in range(len(params)):
            data[i] += params[j] * noise[i-1-j]

    return data

def plot_ma_1():
    plt.subplot(2,2,1)
    plt.plot(ma_p([-0.6]))
    plt.subplot(2,2,2)
    plt.plot(ma_p([0]))
    plt.subplot(2,2,3)
    plt.plot(ma_p([0.4]))
    plt.subplot(2,2,4)
    plt.plot(ma_p([0.9]))
    plt.show()


def plot_ma_p():    
    plt.subplot(2,2,1)
    plt.plot(ma_p([0.2]))
    plt.subplot(2,2,2)
    plt.plot(ma_p([0.1, 0.9]))
    plt.subplot(2,2,3)
    plt.plot(ma_p([0.9, 0.1]))
    plt.subplot(2,2,4)
    plt.plot(ma_p([0.5, -0.5, 0.5]))
    plt.show()

#plot_ma_1()
plot_ma_p()

