#-*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rd

if __name__ == "__main__":

    '''
    中心極限定理の実験。
    loop_arr内で指定した分だけ、標本平均を取る。
    すなわち、ループ数が増えるほど、正規分布に近くなる。
    具体的には、N(10, 10)にちかくなるハズ。
    '''

    lam = 10

    loop_arr = [50, 100, 300, 1000]
    
    for  plot_pos, loop_num in enumerate(loop_arr):
        average_arr = []
        for i in range(0, loop_num):
            x = rd.poisson(lam, 100)
            average_arr.append(np.average(x))

        plt.subplot(2, 2, plot_pos+1)
        plt.hist(average_arr, label=loop_num)

    plt.legend()
    plt.show()
