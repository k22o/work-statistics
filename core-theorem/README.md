# 主要定理

## ベイズの定理 (Bayes' theorem)
- P(B): 事前分布
- P(B|A): 事後分布
- P(A|B): 尤度
$$ P(B|A) = \frac{P(A|B)P(B)}{P(A)}$$

すなわち、
$$ P(B|A) \propto P(A|B)P(B) $$



## 中心極限定理 (central limit theorem)
確率変数$X_i$が、互いに独立かつ、平均 $\mu$ 分散 $\sigma^2$ の分布から生じるとき、その数が大きくなるに従い、標本平均$\bar{X}$ の分布は $N(\mu, \sigma^2/n)$ に近づく。

## 大数法則 (law of large numbers)
中心極限定理にて、nを大きくするほど、標本平均は $\mu$ に近づく。しかし、実数列の場合とは異なり、「確率収束をする」ということを定めた定理。
具体的には、中心極限定理と同様の前提において、
$$ \lim_{n \rightarrow \infin} P(|\bar{X}-\mu| \leq \epsilon) = 1, ^\forall \epsilon>0 $$
$$ \lim_{n \rightarrow \infin} P(|\bar{X}-\mu| > \epsilon) = 0, ^\forall \epsilon>0 $$

## Chebyshev's inequality
$X$が、平均 $\mu$、分散 $\sigma^2$ の分布に従うとき、任意の実数 $k$ について、以下の不等式 (チェビシェフ不等式) が成り立つ。
$$P(|X < \mu| \geq k\sigma) \leq \frac{1}{k^2}$$
これは、ざっくりとした確率を求めることや、各種確率論の証明に用いられる。


### 備考：確率収束
確率変数列 $X_i$ が値 $\alpha$ に収束するとは、以下で表される。
$$ \lim_{n \rightarrow \infin} P(|X_n-\alpha| > \epsilon) = 0, ^\forall \epsilon>0 $$
