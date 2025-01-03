# 基本原則

## 特性値

### 基礎的な特性値の定義

- 期待値: $E[X]$
- 分散: $V[X] = E[X-E[X]]$
- 共分散: $Cov[X,Y] = E[(X-E[X])(Y-E[Y])]$
- 相関係数: $\rho[X,Y] = \frac{Cov[X,Y]}{\sqrt{V[X]V[Y]}}$
- 偏相関係数: $\rho[X,Y|Z] = \frac{\rho[X,Y] - \rho[X,Z]\rho[Y,Z]}{\sqrt{(1-\rho[X,Z])^2(1-\rho[Y,Z]^2)}}$

### 期待値や分散の変換法則

- $V[X] = E[X^2] - (E[X])^2$
- $Cov[X,Y] = E[X]E[Y] - E[XY]$   
- $E[aX+bY+c] = aE[X]+bE[Y]+c$
- $V[aX+b] = a^2V[X]$
- $V[X\pm Y] = V[X] + V[Y] \pm 2cov[X,Y]$ 

### その他の特性値

期待値を $\mu$, 標準偏差を $\sigma$ とする。
- 変動係数: $\sigma/\mu$
- 歪度: $\frac{E[(X-\mu)^3]}{\sigma^3}$: 左右対称のとき0、右に裾が長いと正、左に裾が長いと負。
- 尖度: $\frac{E[(X-\mu)^4]}{\sigma^4}$: 正規分布のとき3、それより急峻だと正。

### 確率母関数・積率母関数と特性値

確率母関数 $G_1(s) = E[s^x]$ について、

- $G_1^\prime(1) = E[X] $

積率母関数 $G_2(\theta) = E[e^{\theta x}]$ について、

- $G_2^\prime(0) = E[X] $

というように、微分した値が特性値に関連している。
1階微分までの結果から平均、2階微分までの結果から分散などが求まる。

## 不偏推定量と一致推定量

### 不偏推定量

$E(\bar{X}) = \mu$ や $E(s^2) = \sigma^2$ は、推定値(標本値)の平均が、真なる値 (母集団) に一致している。
一般に、推定値 $\hat{\theta}$ 、真値 $\theta$ について、 $E(\theta) = \theta$ を満たす場合、 $\theta$ を $\theta$ の不偏推定量と呼ぶ。<br>

### 一致推定量

n数を増やした場合に、真値を正しく予測できるような推定量を、一致推定量と呼ぶ。すなわち、真値 $\theta$, 予測値 $\hat{\theta}_n$ に対して以下が成り立つ。
(「一致推定量は真値に確率収束する」)

$$
\forall \epsilon, \lim_{n \rightarrow \infin} P(|\hat{\theta_n} - \theta | < \epsilon) = 1
$$

一致性の証明は確率収束することを示す必要があり、chevichef不等式を用いることが多い。

### バイアス・バリアンス分解

一般に、推定量 $\hat{\theta}$ について、 $b(\hat{\theta}) = E(\hat{\theta}) - \theta$ をバイアスと呼ぶ。    
この定義からわかるように、不偏推定量はバイアスが0となるような推定量である。ここで、

$$
E[(\hat{\theta}-\theta)^2] = (E[\hat{\theta}] - \theta)^2 + V[\hat{\theta}]
$$

であり、平均二乗誤差は、バイアスとバリアンスに分解できる。  
バイアスを0に保ちつつ、分散を最小にする推定量を、最小分散不偏推定量 (minimum variance unbiased estimator) と呼ぶ。

## 主要定理

### ベイズの定理 (Bayes' theorem)

- P(B): 事前分布
- P(B|A): 事後分布
- P(A|B): 尤度

$$ P(B|A) = \frac{P(A|B)P(B)}{P(A)}$$

すなわち、

$$P(B|A) \propto P(A|B)P(B)$$

### 中心極限定理 (central limit theorem)

確率変数 $X_i$ が、互いに独立かつ、平均 $\mu$ 分散 $\sigma^2$ の分布から生じるとき、その数が大きくなるに従い、標本平均 $\bar{X}$ の分布は $N(\mu, \sigma^2/n)$ に近づく。

### 大数法則 (law of large numbers)

中心極限定理にて、nを大きくするほど、標本平均は $\mu$ に近づく。しかし、実数列の場合とは異なり、「確率収束をする」ということを定めた定理。
具体的には、中心極限定理と同様の前提において、

$$ \lim_{n \rightarrow \infin} P(|\bar{X}-\mu| \leq \epsilon) = 1, ^\forall \epsilon>0 $$

$$ \lim_{n \rightarrow \infin} P(|\bar{X}-\mu| > \epsilon) = 0, ^\forall \epsilon>0 $$

## Chebyshev's inequality

$X$ が、平均 $\mu$、分散 $\sigma^2$ の分布に従うとき、任意の実数 $k$ について、以下の不等式 (チェビシェフ不等式) が成り立つ。

$$P(|X < \mu| \geq k\sigma) \leq \frac{1}{k^2}$$

これは、ざっくりとした確率を求めることや、各種確率論の証明に用いられる。

#### 備考：確率収束

確率変数列 $X_i$ が値 $\alpha$ に収束するとは、以下で表される。

$$ \lim_{n \rightarrow \infin} P(|X_n-\alpha| > \epsilon) = 0, ^\forall \epsilon>0 $$
