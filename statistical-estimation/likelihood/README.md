## 事前準備

ある確率変数 $\theta$ と $x$ について、ベイズ推定において以下の式が成り立つ。

$$p(\theta|x) = \frac {p(x|\theta)p(\theta)}{p(x)}$$

このとき、 $p(\theta)$ を**事前分布(prior)**、 $p(\theta|x)$ を**事後分布(posterior)**、 $p(x|\theta)$ を**尤度(likelihood)** と呼ぶ。

すなわち、「事前にある分布が想定されていて」、「何らかの実験結果があって」、「それをつきあわせたことで事後分布が得られる」ということである。

## 最尤法

尤度を最大化する方法で、最尤推定 (maximum-likelihood estimation) とも呼ぶ。

最尤推定で利用するデータは、実測値から求まる $p(x|\theta)$ であり、これは、ある確率密度関数 $f$ の下で $f(x;\theta)$ と表すことができる。
故に、最尤推定とは、

$$\hat{\theta} = \argmax_{\theta} L(\theta) = \argmax_{\theta} f(x;\theta)$$

と表現できる。

$x_i$ が独立した事象であれば、我々は、以下の式で表現される尤度関数を最大化すればよい。
$$L(\theta) = \prod_i f(x_i;\theta)$$
あるいは、負の対数をとって、以下を最小化すると考えてもよい。
$$L(\theta) = - \sum_i \log(f(x_i;\theta))$$

最終的に、
$$\frac{\partial L}{\partial \theta} = 0$$
を満たす、 $\theta$ を求める。

## 最大事後確率(MAP)推定

やりたいことは、事後確率    の最大化である。ベイズの定理より、
$$p(\theta|x)p(x) = p(x|\theta)p(\theta)$$

事前分布の項は、 $\theta$ の関数ではないので、
$$p(\theta|x) \propto p(x|\theta)p(\theta)$$
であり、 $\theta$ の事前分布を $g$ とすれば、次を最大化する $\theta$ を考えればよい。

$$
L(\theta) = f(x;\theta)g(\theta)
$$

これを最大化する $\theta$ を求めればよい。

## ベイズ推定

MAP推定では、事後分布を最大にする $\theta$ 、すなわちモードを求めたが、ベイズ推定では、期待値を求める。すなわち、

$$
\hat{\theta} = \int_{\theta \in \Theta} \theta p(\theta|x)dx
$$

## 数値計算による推定

解析的に求められない場合、以下のようなアルゴリズムを用いて、数値計算によって推定量を求める。

- ニュートン法
- 勾配降下法
- EMアルゴリズム
- モンテカルロ法
