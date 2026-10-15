---
title: Hölder 不等式
tags:
  - 数学分析
  - 不等式
---

## 前置

- [[数学分析/实数次幂]]
- [[数学分析/derivate]]
- [[数学分析/complex-number]]
- [[测度论/L-integral]]

由实数幂的求导得到 Young 不等式，再经归一化得到 Hölder 不等式。有限和与积分用同一论证。

## 1. 共轭指数

设 $p,q>1$ 满足

$$
\frac{1}{p}+\frac{1}{q}=1.
$$

称 $p,q$ 为一对共轭指数。由此

$$
q=\frac{p}{p-1},\qquad
q-1=\frac{1}{p-1},\qquad
\frac{p}{q}=p-1.
$$

## 2. Young 不等式

设 $x,y\ge 0$，$p,q>1$ 为共轭指数。则

$$
xy\le\frac{x^p}{p}+\frac{y^q}{q}.
$$

等号成立当且仅当 $x^{p-1}=y$，等价地 $x^p=y^q$。

**证明.** 若 $y=0$，则 $xy=0\le x^p/p$，等号当且仅当 $x=0$，即 $x^{p-1}=y$。

设 $y>0$。固定 $y$，定义

$$
F(t)=\frac{t^p}{p}-ty+\frac{y^q}{q},\qquad t\ge 0.
$$

不等式即 $F(x)\ge 0$。对 $t>0$，

$$
F'(t)=t^{p-1}-y.
$$

映射 $t\mapsto t^{p-1}$ 在 $[0,\infty)$ 上严格递增，故 $F'(t)=0$ 有唯一解

$$
t_0=y^{1/(p-1)}=y^{q-1}.
$$

当 $0<t<t_0$ 时 $F'(t)<0$，当 $t>t_0$ 时 $F'(t)>0$。$F$ 在 $[0,t_0]$ 上递减、在 $[t_0,\infty)$ 上递增，最小值在 $t_0$ 取得。

由 $t_0^{p-1}=y$ 得

$$
t_0^p=y^{p/(p-1)}=y^q,\qquad
t_0 y=y^{1/(p-1)+1}=y^{p/(p-1)}=y^q.
$$

代入，

$$
\begin{aligned}
F(t_0)
&=\frac{t_0^p}{p}-t_0 y+\frac{y^q}{q}
=\frac{y^q}{p}-y^q+\frac{y^q}{q}
=y^q\left(\frac{1}{p}-1+\frac{1}{q}\right)
=0.
\end{aligned}
$$

因此对一切 $t\ge 0$ 有 $F(t)\ge 0$。最小值只在 $t_0$ 取得，故等号当且仅当 $x=t_0$，即 $x^{p-1}=y$。此时 $x^p=y^q$。

反之，若 $x^p=y^q$，则 $x=0$ 时必有 $y=0$；若 $x>0$，则 $y=x^{p/q}=x^{p-1}$。两种等号条件等价。

## 3. 有限和

设 $a_1,\ldots,a_n$ 与 $b_1,\ldots,b_n$ 为实数或复数，$p,q>1$ 为共轭指数。则

$$
\sum_{i=1}^{n}|a_i b_i|
\le
\left(\sum_{i=1}^{n}|a_i|^p\right)^{1/p}
\left(\sum_{i=1}^{n}|b_i|^q\right)^{1/q}.
$$

左边先对每一项取绝对值，再求和。

**证明.** 记

$$
A=\left(\sum_{i=1}^{n}|a_i|^p\right)^{1/p},\qquad
B=\left(\sum_{i=1}^{n}|b_i|^q\right)^{1/q}.
$$

若 $A=0$，则每个 $|a_i|^p=0$，故 $a_i=0$，左边为 $0$。$B=0$ 同样。以下设 $A>0$ 且 $B>0$，令

$$
x_i=\frac{|a_i|}{A},\qquad y_i=\frac{|b_i|}{B}.
$$

则

$$
\sum_{i=1}^{n}x_i^p
=\frac{1}{A^p}\sum_{i=1}^{n}|a_i|^p
=1,
$$

同理 $\sum_{i=1}^{n} y_i^q=1$。对每个 $i$ 应用 Young 不等式，

$$
x_i y_i\le\frac{x_i^p}{p}+\frac{y_i^q}{q}.
$$

求和得

$$
\begin{aligned}
\sum_{i=1}^{n}x_i y_i
&\le\frac{1}{p}\sum_{i=1}^{n}x_i^p+\frac{1}{q}\sum_{i=1}^{n}y_i^q
=\frac{1}{p}+\frac{1}{q}
=1.
\end{aligned}
$$

由 $x_i y_i=|a_i b_i|/(AB)$ 即得 $\sum_{i=1}^{n}|a_i b_i|\le AB$。

### 和的绝对值

对任意复数 $z,w$，$|z+w|\le|z|+|w|$。归纳得

$$
\left|\sum_{i=1}^{n}a_i b_i\right|
\le
\sum_{i=1}^{n}|a_i b_i|.
$$

再代入上一不等式，

$$
\left|\sum_{i=1}^{n}a_i b_i\right|
\le
\left(\sum_{i=1}^{n}|a_i|^p\right)^{1/p}
\left(\sum_{i=1}^{n}|b_i|^q\right)^{1/q}.
$$

## 4. 积分形式

设 $(X,\Sigma,\mu)$ 为测度空间，$f,g$ 可测，$p,q>1$ 为共轭指数，且

$$
\int |f|^p\,d\mu<\infty,\qquad
\int |g|^q\,d\mu<\infty.
$$

则

$$
\int |fg|\,d\mu
\le
\left(\int |f|^p\,d\mu\right)^{1/p}
\left(\int |g|^q\,d\mu\right)^{1/q}.
$$

**证明.** 记

$$
A=\left(\int |f|^p\,d\mu\right)^{1/p},\qquad
B=\left(\int |g|^q\,d\mu\right)^{1/q}.
$$

若 $A=0$ 或 $B=0$，则相应函数几乎处处为零，不等式成立。否则令 $u=|f|/A$、$v=|g|/B$，则

$$
\int u^p\,d\mu=1,\qquad \int v^q\,d\mu=1.
$$

逐点有 $uv\le u^p/p+v^q/q$。由积分的保序性与线性，

$$
\int uv\,d\mu
\le\frac{1}{p}\int u^p\,d\mu+\frac{1}{q}\int v^q\,d\mu
=1.
$$

代回 $u,v$ 得 $\int|fg|\,d\mu\le AB$。

证明用到积分的保序性、线性，以及非负可测函数积分为零则几乎处处为零。

## 5. 特例与等号

### Cauchy–Schwarz

取 $p=q=2$，有限和形式化为

$$
\sum_{i=1}^{n}|a_i b_i|
\le
\sqrt{\sum_{i=1}^{n}|a_i|^2}\,
\sqrt{\sum_{i=1}^{n}|b_i|^2}.
$$

### 等号

考虑 $\sum_{i=1}^{n}|a_i b_i|=AB$。

- 若 $A=0$ 或 $B=0$，两边都是 $0$，等号成立。
- 若 $A,B>0$，求和后等号成立当且仅当每个 $i$ 都使 Young 不等式取等号，即 $x_i^p=y_i^q$。换回原变量，

$$
\frac{|a_i|^p}{\sum_{j=1}^{n}|a_j|^p}
=
\frac{|b_i|^q}{\sum_{j=1}^{n}|b_j|^q}
\quad\text{对所有 }i.
$$

归一化之后，$|a_i|^p$ 与 $|b_i|^q$ 逐项相等。
