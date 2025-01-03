# モデル

## 一般線形モデル (general liner model; GLM)

$$\boldsymbol{y} = X\boldsymbol{\beta} + \boldsymbol{\epsilon}$$

- $\boldsymbol{\beta}$ は回帰係数、 $\boldsymbol{\epsilon}$ は残差を表しており、線形回帰分析はこれに当たる。
- ANOVAやt検定などにも含まれる考え方。
- 一般線形モデルでは、残差Eが正規分布に従うという仮定の下、最小二乗法によってEを最小化するようにしている (線形回帰では、最小二乗法も最尤法も辿り着く先は一緒)。

## 一般化線形モデル (generalized liner model; GLM)

一般線形モデルで仮定していた、残差の正規分布性を取り払い、任意の確率分布で表現できるようにしたもの。

Yが指数型分布族の確率分布に従うとする。指数型分布族は、BinやPo, N, ガンマなどの分布を含む。

$$
f(y;\theta,\phi) = exp[\frac{y\theta-b(\theta)}{a(\phi)}-c(y,\phi)]
$$

このようなYの期待値 $\pi$ のなめらかな変換 $g$ (リンク関数と呼ぶ) をもちいて、以下のような回帰で表される。

$$
g(\pi) = \alpha + \boldsymbol{\beta}^T \boldsymbol{x}
$$
