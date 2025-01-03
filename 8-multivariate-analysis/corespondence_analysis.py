#-*- coding:utf-8 -*-
import mca
import pandas as pd
import matplotlib.pyplot as plt

# 対応分析を実行する
def mca_analysis():

    # データは、統計検定準1級より一部修正して引用
    data = dict(
        tv = [94, 106, 133, 186, 157, 203],
        radio = [2, 3, 2, 3, 6, 7],
        paper = [15, 41, 53, 55, 67, 69],
        book = [4, 2, 6, 3, 1, 4],
        web = [23, 64, 73, 56, 24, 15]
    )

    index = ["10's", "20's", "30's", "40's", "50's", "60's"]

    df = pd.DataFrame(data=data, index=index)
    return df, mca.MCA(df, benzecri=False)

## factorをプロットする
def factor_score(df, mca_result):

    rows = mca_result.fs_r(N=2) # 第二成分までの因子スコア
    cols = mca_result.fs_c(N=2)

    plt.axhline(0, ls="--", c="#777777")
    plt.axvline(0, ls="--", c="#777777")

    plt.scatter(rows[:,0], rows[:,1], c='b',marker='x')
    for x, y, label in zip(rows[:,0],rows[:,1], df.index):
        plt.annotate(label, xy = (x, y))

    plt.scatter(cols[:,0], cols[:,1], c='r',marker='o')
    for x, y, label in zip(cols[:,0], cols[:,1], df.columns):
        plt.annotate(label, xy = (x, y))

    plt.xlabel("factor1")
    plt.ylabel("factor2")
    plt.show()

#############################################

df, mca_result = mca_analysis()

print("クロス集計表")
print(df)
print("行(年代ごと)の結果")
print(mca_result.fs_r(N=2))
print("列(媒体ごと)の結果")
print(mca_result.fs_c(N=2))

factor_score(df, mca_result)
