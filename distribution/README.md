# 分布
## 用語整理

| 名称 | 関数 | 特徴 |
| ---- | ---- | ---- |
| 確率密度関数(PDF)  | $f(x)$ | 連続型確率変数がある値をとる事象の確率密度を記述 |
| 累積分布関数(CDF)  | $F_x(a) = P(x\leq a) = \int^af(x)dx$ | 下側。微分はPDF |
| 生存関数(SF)  | $P(x>a) = \int_af(x)dx$ | 上側 |
| 確率質量関数(PMF)  | | 離散型確率変数にその値をとる確率を対応させる関数 |
|特性関数(CF)| $\phi_x(t) = E[e^{itx}] $ | 別ファイル参照|
|ハザード関数| $h(x) = \frac{f(x)}{1-F(x)}$ | 負の生存関数の微分に等しい。ある地点まで生きているものが直後に死ぬ確率 |
|確率母関数|$M_X(s) = E[s^{X}] = \int s^{x}f(x)dx $||
|積率母関数|$M_X(\theta) = E[e^{\theta X}] = \int e^{\theta x}f(x)dx $||


## 離散型
- 確率変数 $X$

### 二項分布 (binomial distribution)

$$ P(X=x) = {}_n C_x p^x(1-p)^{n-x} $$

- $X$ ~ $Bin(n, p)$
- ベルヌーイ試行が従う分布である。
- ある事象が発生する確率を $p$ 試行回数 $n$
- 再生性を有する -> $X + Y \sim Bin(n_1+n_2, p)$

### Poisson分布

$$ P(X=x) = e^{-\lambda} \frac{\lambda^x}{x!} $$

- $X \sim Po(\lambda)$
- 二項分布において、 $np = \lambda$ を一定にしつつ、 $n \rightarrow \infin $　として得られる
- すなわち、件数は多いが発生確率が低く、$np$が中程度の場合に見られる
- たとえば、単位時間当たりに客が平均 $\lambda$ で来る場合は、人数はpoisson分布で与えられる。
- 「単位時間内にx人が来る確率」
- 再生性を有する -> $X + Y \sim Po(\lambda_1 + \lambda_2)$


### 幾何分布 (geometric distribution)

$$ P(X=x) = p(1-p)^{x-1} $$

- $X \sim Ge(p)$
- ある事象が発生するまでの待ち時間を表すことが多い
- 「ある客が来てから、次にx時間後に客が来る確率」
- ベルヌーイ試行においては、初めて成功するまでの回数は幾何分布になる
- 無記憶性 $P(X=a+b|X>b) = P(X=a)$ を有する


## 連続確率分布
- 確率密度関数(PDF) を $f(x)$ とする

### 一様分布 (uniform distribution)

$$ 
f(x) = \begin{cases} 
{\frac{1}{b-a} (a < x < b)} \\
{0 (otherwise)}
\end{cases}
$$

- $X \sim U(a, b)$


### 正規分布 (normal distribution)

$$ f(x) = \frac{1}{\sqrt{2\pi}\sigma} exp(-\frac{(x-\mu)^2}{2\sigma^2})$$

- $X \sim N(\mu, \sigma^2)$
- 特に $N(0, 1)$ を標準正規分布という
- 再生性を有する -> $aX + bY + c \sim B(a\mu_1 + b\mu_2 + c, a^2\sigma_1^2 + b^2\sigma_2^2)$

### 指数分布 (exponential distribution)

$$ f(x) = \begin{cases} 
{\lambda e^{-\lambda x} (x > 0)} \\
{0 (otherwise)}
\end{cases}$$

- $X \sim Ex(\lambda)$
- ある事象が発生するまでの待ち時間を表すことが多い
- 無記憶性を有する
- 幾何分布の連続版
- PDFが「x時間後に次に客がくる確率」だとしたら、CDFは「x時間以内に客が来る確率」といえる

### beta分布
ここでは、第一種ベータ分布のみ記載する。

$$
f(x;\alpha,\beta) = \frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)} \\
B(\alpha, \beta) = \int_0^1 t^{\alpha-1}(1-t)^{\beta-1}dt
$$

- $X \sim Be(\alpha, \beta)$
- 事前分布を $Be(\alpha, \beta)$ とする。尤度が二項分布 $Bin(a, b)$ 
 に従うとき、事後分布は、$Be(\alpha + a, \beta + b)$ に従う。
- ベイズ統計において、二項分布を尤度とした、共役事前分布として用いられることが多い。
- $Be(1,1)$ は一様分布に相当する。

### Gamma分布

$$
f(x;a,b) = \frac{1}{\Gamma(a)b^a} x^{a-1}e^{-\frac{x}{b}} \\
\Gamma(a) = \int_0^{\infin} x^{a-1}e^{-x}dx
$$

- $X \sim Ga(a, b)$
- $Ga(1,b)$ は、$Ex(1/b)$ に等しい
- ベイズ統計において、ポアソン分布を尤度とした、共役事前分布として用いられることが多い。


## 期待値と分散のまとめ
| 分布 | 期待値 | 分散 |
| ---- | ---- | ---- |
| 二項分布  | $np$ | $np(1-p)$ |
| Poisson分布 | $\lambda$ | $\lambda$ |
| 幾何分布  | $\frac{1}{p}$ | $\frac{1-p}{p^2}$ |
| 正規分布 | $\mu$ | $\sigma^2$ |
| 指数分布  | $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$ |
| beta分布  | $\frac{\alpha}{\alpha + \beta}$ | $\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$ |

(注) 連続型確率変数の場合、最頻値は確率密度関数の極値に相当する。

## 備考
### 無記憶性
以下の性質を無記憶性と呼ぶ。前までのことに依存せずに次の事象がおきることを表す。例えば、 $P(X)$ に指数分布の値を入れれば、これがなりたつことがわかる。

$$P(X=a+b|X>b) = P(X=a)$$


### 再生性
ある確率変数 $X_1 \sim F_1$, $X_2 \sim F_2$ について、 $X_1 + X_2$ も同じ種類の分布 $F$ に従うとき、再生性があるという。

たとえば、正規分布 $N(\mu_1, \sigma_1^2)$ と $N(\mu_2, \sigma_2^2)$ を仮定する。これらを足し合わせたデータは、 $N(\mu_1+\mu_2, \sigma_1^2+\sigma_2^2)$ の分布に従う。


### 特性関数の求め方
以下をRiemann–Stieltjes積分という。

$$\int_a^b fdg = \int_a^b f(x)dg(x)$$

特性関数は以下の通りである。

$$\phi_X(t) = E[e^{itx}] = \int_{-\infin}^{-\infin} e^{itx} dF_X(x)$$

$\frac{dF_X(x)}{dx} = f(x)$ であるので、

$$
\phi_X(t) = \int_{-\infin}^{-\infin} e^{itx} f_X(x)dx
$$

## 多変量正規分布
確率変数 $\boldsymbol{X} = (X_1, X_2, ...,X_n)^T$ について、
以下のように多変量正規分布 $N(\boldsymbol{\mu}, \Sigma)$ を規定できる。

$$
f(\boldsymbol{x}) = \frac{1}{\sqrt{(2\pi)^n}\sqrt{det\Sigma}} exp(-\frac{1}{2}(\boldsymbol{x}-\boldsymbol{\mu})^T\Sigma^{-1}(\boldsymbol{x}-\boldsymbol{\mu})) \\
$$

ただし、 $\boldsymbol{\mu} = (\mu_1, \mu_2, ..., \mu_n)^T$ , $\Sigma(i,i) = \sigma_i^2$, $\Sigma(i,k) = \rho_{ij} \sigma_i\sigma_j$

とする。

このとき、周辺分布は、 $X_i \sim N(\mu_i, \sigma_i)$ である。
この確率密度関数を $f(x_i)$ とおけば、
また、条件付き分布 $P(\boldsymbol{X}|X_i=x_i)$ は、確率密度関数 $f(\boldsymbol{x}) / f(x_i)$ から求めることができる。 

特に、2変数の場合は、

$$
\begin{aligned}
E[X_2 | X_1 = x_1] &= \mu_2 + \rho \frac{\sigma_2}{\sigma_1} (x_1 - \mu_1) \\
V[X_2 | X_1 = x_1] &= \sigma_2^2 (1-\rho^2)
\end{aligned}
$$
