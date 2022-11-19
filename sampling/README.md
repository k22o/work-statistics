## Bootstrap法
サンプル $X = \{x_1, x_2, ..., x_n\}$ があり、これから 
$\hat{\theta}(X)$ という推定値を得ることを考える。  
ブートストラップ法は、 $X$ からn個の要素を非復元抽出して (リサンプリング)、
$X^* = \{x^*_1, x^*_2, ..., x^*_n\}$ というデータ (bootstrap標本) を得て、推定値 $\hat{\theta}(X^*)$ を計算できる。

これをB回繰り返し、$\hat{\theta}_i(X^*) (i=1,2,...B)$ から、ブートストラップ法によって以下のように推定値を求める。

- 推定値: $\bar{\hat{\theta}}^* = \frac{1}{B}\sum^B_{i=0} \hat{\theta}^*_i$
- 標準誤差のブートストラップ推定量: $s(X) = \sqrt{\frac{1}{B-1}\sum(\hat{\theta}^*_i -\bar{\hat{\theta}^*})^2}$
- バイアスのブートストラップ推定量: $bias = \bar{\hat{\theta}}^* - \hat{\theta}$

確率分布関数は、以下で求まる。
$Pr(\bar{X}\leq x) = \frac{1}{B}\{x \leq \bar{x}_i の個数\} $


## Jackknife法
サンプル $X = \{x_1, x_2, ..., x_n\}$ があり、これから 
$\hat{\theta}(X)$ という推定値を得ることを考える。  
このうち、$x_i$ を除いた $n-1$ 個のサンプルから、 $\hat{\theta}_i(X^*)$ を得る。これを$i=1,2,...,n$まで繰り返す。

- 推定値: $\bar{\hat{\theta}}^* = \frac{1}{n}\sum^n_{i=0} \hat{\theta}^*_j$
- 標準誤差のジャックナイフ推定量: $s(X) = \sqrt{\frac{n-1}{n}\sum(\hat{\theta}^*_j -\bar{\hat{\theta}^*})^2}$
- バイアスのジャックナイフ推定量: $bias = (n-1)(\bar{\hat{\theta}}^* - \hat{\theta})$
