# 分布
## 用語整理

| 名称 | 関数 | 特徴 |
| ---- | ---- | ---- |
| 確率密度関数(PDF)  | $f(x)$ | 連続型確率変数がある値をとる事象の確率密度を記述 |
| 累積分布関数(CDF)  | $$ F_x(a) = P(x\leq a) = \int^af(x)dx$$ | 下側。微分はPDF |
| 生存関数(SF)  | $$P(x>a) = \int_af(x)dx$$ | 上側 |
| 確率質量関数(PMF)  | | 離散型確率変数にその値をとる確率を対応させる関数 |
|特性関数(CF)| $$ \phi_x(t) = E[e^{itx}] $$ | 別ファイル参照|
|確率母関数|$$ M_X(s) = E[s^{X}] = \int s^{x}f(x)dx $$||
|積率母関数|$$ M_X(\theta) = E[e^{\theta X}] = \int e^{\theta x}f(x)dx $$||


## 離散型
- 確率変数 $X$

### 二項分布 (binomial distribution)
$$ P(X=x) = {}_n C_x p^x(1-p)^{n-x} $$
- $X$ ~ $B(n, p)$
- ベルヌーイ試行が従う分布である。
- ある事象が発生する確率を$p$ 試行回数$n$
- 再生性を有する -> X + Y ~ $B(n_1+n_2, p)$

### Poisson分布
$$ P(X=x) = e^{-\lambda} \frac{\lambda^x}{x!} $$
- $X$ ~ $Po(\lambda)$
- 二項分布において、$np = \lambda$ を一定にしつつ、$n \rightarrow \infin $　として得られる
- すなわち、件数は多いが発生確率が低く、$np$が中程度の場合に見られる
- たとえば、単位時間当たりに客が平均$\lambda$で来る場合は、人数はpoisson分布で与えられる。
- 「単位時間内にx人が来る確率」
- 再生性を有する -> X + Y ~ $Po(\lambda_1 + \lambda_2)$


### 幾何分布 (geometric distribution)
$$ P(X=x) = p(1-p)^{x-1} $$
- $X$ ~ $Ge(p)$
- ある事象が発生するまでの待ち時間を表すことが多い
- 「ある客が来てから、次にx時間後に客が来る確率」
- ベルヌーイ試行においては、初めて成功するまでの回数は幾何分布になる
- 無記憶性 $P(X=a+b|X>b) = P(X=a)$を有する


## 連続確率分布
- 確率密度関数(PDF) を $f(x)$ とする
- $P(x<a)$ = $\int_0^af(x)dx$ を(累積)分布関数(CDF) と呼ぶ
- $P(x>=a)$ を生存関数(SF) と呼ぶ

### 一様分布 (uniform distribution)
$$ f(x) = \begin{cases} 
{\frac{1}{b-a} (a < x < b)} \\
{0 (otherwise)}
\end{cases}$$
- - $X$ ~ $U(a, b)$


### 正規分布 (normal distribution)
$$ f(x) = \frac{1}{\sqrt{2\pi}\sigma} exp(-\frac{(x-\mu)^2}{2\sigma^2})$$
- $X$ ~ $N(\mu, \sigma^2)$
- 特に $N(0, 1)$ を標準正規分布という
- 再生性を有する -> aX + bY + c ~ $B(a\mu_1 + b\mu_2 + c, a^2\sigma_1^2 + b^2\sigma_2^2)$

### 指数分布 (exponential distribution)
$$ f(x) = \begin{cases} 
{\lambda e^{-\lambda x} (x > 0)} \\
{0 (otherwise)}
\end{cases}$$
- $X$ ~ $Ex(\lambda)$
- ある事象が発生するまでの待ち時間を表すことが多い
- 無記憶性を有する
- 幾何分布の連続版
- PDFが「x時間後に次に客がくる確率」だとしたら、CDFは「x時間以内に客が来る確率」といえる


## 期待値と分散のまとめ
| 分布 | 期待値 | 分散 |
| ---- | ---- | ---- |
| 二項分布  | $np$ | $np(1-p)$ |
| Poisson分布 | $\lambda$ | $\lambda$ |
| 幾何分布  | $\frac{1}{p}$ | $\frac{1-p}{p^2}$ |
| 正規分布 | $\mu$ | $\sigma^2$ |
| 指数分布  | $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$ |


## 備考
### 無記憶性
以下の性質を無記憶性と呼ぶ。前までのことに依存せずに次の事象がおきることを表す。例えば、P(X)に指数分布の値を入れれば、これがなりたつことがわかる。
$$P(X=a+b|X>b) = P(X=a)$$


### 再生性
ある確率変数 $X_1 \sim F_1$, $X_2 \sim F_2$ について、$X_1 + X_2$ も同じ種類の分布 $F$ に従うとき、再生性があるという。

たとえば、正規分布 $N(\mu_1, \sigma_1^2)$ と $N(\mu_2, \sigma_2^2)$ を仮定する。これらを足し合わせたデータは、$N(\mu_1+\mu_2, \sigma_1^2+\sigma_2^2)$ の分布に従う。


### 特性関数の求め方
以下をRiemann–Stieltjes積分という。
$$\int_a^b fdg = \int_a^b f(x)dg(x)$$

特性関数は以下の通りである。
$$\phi_X(t) = E[e^{itx}] = \int_{-\infin}^{-\infin} e^{itx} dF_X(x)$$

$\frac{dF_X(x)}{dx} = f(x)$ であるので、
$$
\phi_X(t) = \int_{-\infin}^{-\infin} e^{itx} f_X(x)dx
$$
