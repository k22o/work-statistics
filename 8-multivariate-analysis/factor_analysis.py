#-*- coding:utf-8 -*-
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
from sklearn.decomposition import FactorAnalysis as FA

# 因子分析を実行する
def factor_analysis():

    # 好まれているコーヒー商品のデータ
    # http://mo161.soci.ous.ac.jp/@d/DoDStat/cannedcf/cannedcf_st01J.xml
    columns = ["wantbuy", "bought", "tasty", "buynear", "design"]
    data = [[94,288,131,206,82], [86,209,153,165,56], [67,277,120,191,30],
        [64,168,131,153,37], [60,180,112,131,64], [56,209,112,157,26],
        [56,183,120,127,22], [52,224,108,142,19], [49,116,157,101,11],
        [49,251,105,165,30], [45,191,120,127,19], [45,194,108,131,15],
        [37,150,97,138,22], [37,127,94,101,15]]        
    df = pd.DataFrame(data=data, columns=columns)

    # データを正規化する
    df_normalize = (df - df.mean()) / df.std()

    # 解析する
    factor_num = 2
    transformer = FA(factor_num, max_iter=1000, rotation='varimax')
    ## データ数×因子数のデータに変換する
    df_transformed = transformer.fit_transform(df_normalize)

    return df, transformer, df_transformed


# 因子負荷量を表示する
def print_factor_loading(columns, transformer):
    factor_loading = transformer.components_ # 因子負荷量を取得
    df = pd.DataFrame(factor_loading, index=["factor1", "factor2"], columns=[columns])

    # 共通性と独自性を計算する
    communality = df.loc["factor1"]**2 + df.loc["factor2"]**2
    df.loc["coomunality"] = communality
    df.loc["unique"] = 1-communality

    print(df)


# 2次元平面に図示する
def plot_analized_data(df_transformed):

    plt.axhline(0, ls="--", c="#777777")
    plt.axvline(0, ls="--", c="#777777")
    plt.scatter(df_transformed[:,0], df_transformed[:,1])
    for x, y, label in zip(df_transformed[:,0], df_transformed[:,1], df.index):
        plt.annotate(label, xy = (x, y))

    plt.xlabel("factor1")
    plt.ylabel("factor2")

    plt.show()

#######################################################

df, transformer, df_transformed = factor_analysis()
print_factor_loading(df.columns, transformer)
plot_analized_data(df_transformed)