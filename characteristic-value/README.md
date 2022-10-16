# 定義
- 期待値: $E[X]$
- 分散: $V[X] = E[X-E[X]]$
- 共分散: $Cov[X,Y] = E[(X-E[X])(Y-E[Y])]$
- 相関係数: $\rho[X,Y] = \frac{Cov[X,Y]}{\sqrt{V[X]V[Y]}}$
- 偏相関係数: $\rho[X,Y|Z] = \frac{\rho[X,Y] - \rho[X,Z]\rho[Y,Z]}{\sqrt{(1-\rho[X,Z])^2(1-\rho[Y,Z]^2)}}$


## 期待値や分散の変換法則
- $V[X] = E[X^2] - (E[X])^2$
- $Cov[X,Y] = E[X]E[Y] - E[XY]$   
- $E[aX+bY+c] = aE[X]+bE[Y]+c$
- $V[aX+b] = a^2V[X]$
- $V[X\pm Y] = V[X] + V[Y] \pm 2cov[X,Y]$ 

## その他の特性値
期待値を $\mu$, 標準偏差を $\sigma$ とする。
- 変動係数: $\sigma/\mu$
- 歪度: $\frac{E[(X-\mu)^3]}{\sigma^3}$
- 尖度: $\frac{E[(X-\mu)^4]}{\sigma^4}$

## 確率母関数・積率母関数と特性値
確率母関数 $G_1(s) = E[s^x]$ について、
- $G_1^\prime(1) = E[X] $

積率母関数 $G_2(\theta) = E[e^{\theta x}]$ について、
- $G_2^\prime(0) = E[X] $

というように、微分した値が特性値に関連している。
1階微分までの結果から平均、2階微分までの結果から分散などが求まる。

## 不偏推定量と一致推定量
### 不偏推定量

$E(\bar{X}) = \mu$ や $E(s^2) = \sigma^2$ は、推定値(標本値)の平均が、真なる値 (母集団) に一致している。
一般に、推定値$T$、真値$\theta$について、 $E(T) = \theta$ を満たす場合、 $T$ を $\theta$ の不偏推定量と呼ぶ。<br>
不偏推定量の中で最も分散が小さいものを、最小分散不偏推定量 (minimum variance unbiased estimator) と呼ぶ

$$\hat{T} = \argmin_T V[(T-\theta)^2]$$

### 一致推定量
n数を増やした場合に、真値を正しく予測できるような推定量を、一致推定量と呼ぶ。すなわち、真値 $\theta$, 予測値 $\hat{\theta}_n$ に対して以下が成り立つ。
(「一致推定量は真値に確率収束する」)

$$
\forall \epsilon, \lim_{n \rightarrow \infin} P(|\hat{\theta_n} - \theta | < \epsilon) = 1
$$

一致性の証明は確率収束することを示す必要があり、chevichef不等式を用いることが多い。