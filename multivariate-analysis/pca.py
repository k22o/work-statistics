#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

# 対応分析を実行する
def pca_exec():

    iris = load_iris()
    data = iris.data
    # features = iris.feature_names
    labels = iris.target
    labels_set = set(labels)

    transformer = PCA(n_components=2)
    pca_result = transformer.fit_transform(data)

    # 固有ベクトル
    vec = transformer.components_
    print(vec)
    # 固有値
    print(transformer.singular_values_)
    # 寄与率
    print(transformer.explained_variance_ratio_)
    # 主成分負荷量
    loading = np.zeros((2, np.size(vec,1)))
    loading[0,:] = np.sqrt(transformer.singular_values_[0]) * vec[0,:]
    loading[1,:] = np.sqrt(transformer.singular_values_[1]) * vec[1,:]
    print(loading)

    # 描画
    plt.subplot(1,2,1)
    markers = ['o', 'x', '+']
    for i, label in enumerate(labels_set):
        target_data = pca_result[labels==label, :]
        plt.scatter(target_data[:,0], target_data[:,1], marker=markers[i])
    plt.xlabel("dim1")
    plt.ylabel("dim2")

    plt.subplot(1,2,2)
    colors = ['red', 'blue', 'green', 'black']
    for i in range(len(vec[0])):
        plt.quiver(0, 0, vec[0,i], vec[1,i], angles='xy', scale_units='xy', scale=1, color=colors[i])
        plt.scatter(vec[0,i], vec[1,i], c=colors[i])
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.xlabel("dim1")
    plt.ylabel("dim2")
    plt.show()

#############################################

pca_exec()
