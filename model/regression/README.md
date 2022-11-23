# 線形回帰

## 重回帰
### 決定係数
決定係数は、$1-\frac{S_E^2}{S_T^2}$ で表される ($S_E^2$ : 残差平方和, $S_T^2$ : 総平方和)

自由度調整済み決定係数は、各平方和を自由度で割ったものである。
すなわち、データ数$n$ かつ 説明変数 $d$ の場合は、
$1-\frac{S_E^2/(n-d-1)}{S_T^2/(n-1)}$ で記述される。

### 正則化項
- リッジ回帰: L2正則化項を加えて、推定量の分散を小さくする
- Lasso回帰: L1正則化項を加えて計算。いくつかの説明変数は0となり、スパース化される
- Elastic Net: L1とL2の正則化項を、重みα:1-αで加える。


## ロジスティック回帰
ある事象 $Y\in\{0,1\}$ について、 $Y \sim Bin(1,p)$ とし、説明変数を $x_i(i=1,2, ...,n)$ とする。このとき、期待値  $\pi=E[Y]$ を以下をロジスティック回帰モデルと呼ぶ。

$$
\begin{aligned}
\log \frac{\pi}{1-\pi} &= \alpha + \boldsymbol{\beta^T} \boldsymbol{x} \\
\pi &= \frac{1}{1+ e^{-(\alpha +\boldsymbol{\beta^T} \boldsymbol{x})}}
\end{aligned}
$$

実際には、複数のデータ $(\boldsymbol{x_j},y_j)$ を用いて $\beta$ を推定する。

## プロビットモデル
ある事象 $Y\in\{0,1\}$ について、 $Y \sim Bin(1,p)$ とし、説明変数を $x_i(i=1,2, ...,n)$ とする。
標準正規分布の累積分布関数 $\Phi$ をもちいて、期待値 $\pi$ 以下のように表現したモデルをプロビットモデルと呼ぶ。

$$
\begin{aligned}
\pi &= \Phi(\alpha + \boldsymbol{\beta}^T\boldsymbol{x})\\
\Phi(x) &= \int_{-\infin}^x \frac{1}{\sqrt{2\pi}}e^{-y^2/2}dy
\end{aligned}
$$

## ポアソン回帰モデル
$Y \sim Po(\pi)$ とする。この $Y$ を説明変数を $x_i(i=1,2, ...,n)$ を用いて回帰する統計モデルをポアソン回帰モデル(対数線形モデル)と呼ぶ。

$$
\log{\pi} = \alpha + \boldsymbol{\beta}^T \boldsymbol{x}
$$

