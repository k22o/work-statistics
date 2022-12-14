# 時系列データ
## 時系列データの特性値と定常性
### 特性値
$(Y_1, Y_2, ..., Y_t,...,Y_T)$ からなる時系列データに対して、観測時刻 $t$ について特性値が定義される
- 平均 $\mu_t = E[Y_t]$
- 分散 $\sigma_t^2 = V[Y_t]$
- 自己共分散 $Cov[Y_t, Y_{t-k}] = E[(Y_t-E[Y_t])(Y_{t-k}-E[Y_{t-k}])]$
- 自己相関係数 $\rho[Y_t, Y_{t-k}] = Cov[Y_t, Y_{t-k}]/\sigma_t \sigma_{t-k}$

上記のような自己共分散・自己相関係数を、「時刻tにおけるh次の...」と呼ぶ。

### 共分散定常過程/弱定常過程(covariance/week stationary process)
平均と分散が有限で、平均も自己共分散も時刻 $t$ に依存せず、自己共分散がラグ $k$ にのみ依存する系列。
すなわち、
- $E[Y_t] = \mu$ (時刻に非依存、有限値) 
- $Cov[Y_t, Y_{t-k}] = \gamma_{|k|}$ (時刻に非依存でラグにのみ依存、有限) 

### 強定常過程(strong stationary process)
任意の $h_i (i=1,2,...,n)$ について、系列{ $Y_t,Y_{t-k_1}, ...Y_{t-k_n}$} がラグにのみ依存する場合を強定常状態と呼ぶ。

### Noise
共分散定常で、 $\mu=0$, $\gamma_{|k|} = \sigma^2\delta(k)$ (k=0以外では値が0) の場合をホワイトノイズと呼ぶ。    
単に、ノイズが正規分布 $N(\mu, \sigma^2)$ に従う場合にはガウスノイズと呼ぶ。    
両者を満たす場合を、白色ガウスノイズと呼ぶ。

## 時系列モデリング
### 自己回帰過程 (Auto Regression)
$\epsilon_t \sim N(0,\sigma^2)$ とする。
1次の自己回帰過程 AR(1)は、以下で記述される。
(ここでは簡単のため、定数項は省略した。)

$$
\begin{aligned} 
Y_t &= \alpha Y_{t-1} + \epsilon_t \\
&= \alpha^t Y_0 + \sum_i \alpha^{t-i}\epsilon_i
\end{aligned} 
$$

p次の自己回帰過程 AR(p)は、以下の通りとなる。

$$
\begin{aligned} 
Y_t &= c + \alpha_1 Y_{t-1} \alpha_2 Y_{t-2} +... + \alpha_p Y_{t-p}  + \epsilon_t \\
&=c + \sum_{i=1}^p \alpha_i Y_{t-i} + \epsilon_t
\end{aligned} 
$$

### 移動平均過程 (Moving Average)
$\epsilon_t \sim N(0,\sigma^2)$ として、1次の移動平均過程 MA(1)は以下で記述される。

$$
Y_t = \mu + \epsilon_t + \beta \epsilon_{t-1}
$$

q次の移動平均過程 MA(q)は、以下の通りとなる。

$$
\begin{aligned} 
Y_t &= \mu + \epsilon_t + \beta_1 \epsilon_{t-1} + \beta_2 \epsilon_{t-2} + ... + \beta_q \epsilon_{t-q} \\
&= \mu + \epsilon_t + \sum_{j=1}^q \beta_j \epsilon_{t-j}
\end{aligned} 
$$

### ARMA/ARIMAモデル
ARモデルとMAモデルを混合したものが、ARMAモデルである。
$(p,q)$ 次のARMAモデルが以下の通りである。

$$
Y_t = c + \sum_{i=1}^p \alpha_i Y_{t-i} + \epsilon_t + \sum_{j=1}^q \beta_j \epsilon_{t-j}
$$

また、階差 $\Delta Y_t = Y_t - Y_{t-1}$ が定常となるようにモデリングする場合もある。このときには、ARIMAモデルが利用される。これはARMAモデルの$Y_t$ を $\Delta Y_t$ に置き換えただけである。

$(p,1,q)$ 次のARIMAモデルが以下の通りである。

$$
\Delta Y_t = c + \sum_{i=1}^p \alpha_i \Delta Y_{t-i} + \epsilon_t + \sum_{j=1}^q \beta_j \epsilon_{t-j}
$$

## モデルの決定
### 自己相関係数による決定
自己相関係数は、ラグ $k$ ごとに計算される。横軸を $k$ 、縦軸を自己相関としたグラフをコレログラムと呼ぶ。MA(1), MA(2) 過程では、 $k \geq 2 or3$ にて自己相関が0になる。もとの時系列データのコレログラムがこのような性質を有する場合、MA(1)やMA(2)が適する。

### 偏自己相関係数による決定
$Y_t - Y_{t-1}$ の自己相関、すなわち残差の自己相関を偏自己相関と呼ぶ。 $AR(p)$ では、p次以上の偏自己相関は0であるが、MAやARMAでは $k$ が増えるにつれてゆっくりと減衰する。これをもとに、モデルをきめることができる。

### まとめ

|自己相関 |　偏自己相関 | モデル |
| --- | --- | --- |
|$k\geq2$ で0 | ゆっくり減衰 | MA(1) |
|$k\geq3$ で0 | ゆっくり減衰 | MA(2) |
|ゆっくり減衰 | $k\geq2$ で0 | AR(1) | 
|ゆっくり減衰 | $k\geq3$ で0 | AR(2) | 
|ゆっくり減衰 | ゆっくり減衰 | ARMA(1,1) | 

## 検定
### Durbin-Watson検定 (DW-test)
回帰モデルの誤差項 $\epsilon_t$ がホワイトノイズではない場合、すなわち自己相関 $\gamma \neq 0 $ の場合 は、最小二乗法によるパラメータ推定ではなく、最尤法などが好ましいとされている。
誤差項が自己相関を有するか調べる検定をDW検定と呼ぶ。

誤差項に自己相関がある場合、以下の式において、 $\rho \neq 0$ である。

$$
\epsilon_t = \rho \epsilon_{t-1} + (誤差項)
$$

DW統計量は以下で定義される

$$
\begin{aligned} 
DW &= \frac{\sum_{t=2}^T (\epsilon_t-\epsilon_{t-1})}{\sum_{t=1}^T \epsilon_t^2} \\
&= 2 - 2\gamma
\end{aligned} 
$$

よって、以下が成り立つ ($\rho=0$ は $\gamma=0$ と同義)。

|| $\rho>0$ かどうか| $\rho<0$ かどうか|
|---|---|---|
|受容| $\rho=0$ すなわち $DW=2$ | $\rho=2$ すなわち $DW=0$ | 
|棄却| $\rho>0$ すなわち $DW<2$ | $\rho<0$ すなわち $4-DW<2$ |

