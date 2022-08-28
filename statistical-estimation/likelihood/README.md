# 尤度

## 尤度
ある確率変数 $\theta$ と $x$ について、ベイズ推定において以下の式が成り立つ。

$$p(x|\theta) = \frac {p(\theta|x)p(x)}{p(\theta)}$$

このとき、$p(x)$ を**事前分布(prior)**、$p(x|\theta)$ を**事後分布(posterior)**、$p(\theta|x)$ を**尤度(likelihood)** と呼ぶ。

## 最尤法
標本データから、母集団を形作るパラメータ $\theta$ を求めることが大きな課題である。これは、
ある関数 $L(\theta|x)$ を最大化する $\theta$ を求めることと言い換えることができる。これを、最尤推定 (maximum-likelihood estimation) と呼ぶ。

最尤推定で利用するデータは、実測値であり、これは、ある確率密度関数 $f$ の下で $f(x;\theta)$ と表すことができる。
故に、最尤推定とは、

$$\hat{\theta} = \argmax_{\theta} L(\theta|x) = \argmax_{\theta} f(x;\theta)$$

と表現できる。

$x_i$ が独立した事象であれば、我々は、以下の式で表現される尤度関数を最大化すればよい。
$$L(\theta) = \prod_i f(x_i;\theta)$$
あるいは、負の対数をとって、以下を最小化すると考えてもよい。
$$L(\theta) = - \sum_i \log(f(x_i;\theta))$$

最終的に、
$$\frac{\partial L}{\partial \theta} = 0$$
を満たす、$\theta$を求める。

## 最大事後確率(MAP)推定
やりたいことは、尤度の最大化である。ベイズの定理より、
$$p(\theta|x)p(x) = p(x|\theta)p(\theta)$$

事前分布の項は、$\theta$の関数ではないので、

$$ p(\theta|x) \propto p(x|\theta)p(\theta) $$
であり、
$\theta$ の事前分布をgとすれば、次を最大化する $\theta$ を考えればよい。

$$L(\theta) = f(x;\theta)g(\theta)$$

