---
title: Lebesgue 积分（L积分）
---

本节恒设$(\Omega, \mathcal{F}, \mu)$为给定的测度空间，所有函数都是定义在$\Omega$上，广义实值函数。

本节的积分都表示$L$积分

两个广义实数相加有意义的意思为不会同为$+\infty$或同为$-\infty$。

## 前置

- [[测度论与概率论/almost-everywhere]]

## 非负简单可测函数的$L$积分

设$f=\sum_{i=1}^{n} a_i I_{A_i} \in S^+(\Omega, \mathcal{F})$, 称广义实数$\sum_{i=1}^{n} a_i \mu(A_i)$为$f$的**L积分**，记作$\int f d\mu$或$\mu(f)$。

$\int f d\mu$与$f$的表示形式无关。

设$f,g \in S^+(\Omega, \mathcal{F}), \lambda \in \mathbb{R}^*$，则

1. $\int \lambda f d\mu = \lambda \int f d\mu$
2. $\int (f+g) d\mu = \int f d\mu + \int g d\mu$
3. $f \leq g \implies \int f d\mu \leq \int g d\mu$

设$\{f,f_n,g_n,n\geq 1\} \subseteq S^+(\Omega, \mathcal{F})$，则

1. $f_n \uparrow f \wedge \lim\limits_{n\to\infty} f_n \geq f \implies \lim\limits_{n\to\infty} \int f_n d\mu \geq \int f d\mu$
2. $f_n \uparrow f, g_n \uparrow g, \lim\limits_{n\to\infty} f_n = \lim\limits_{n\to\infty} g_n \implies \lim\limits_{n\to\infty} \int f_n d\mu = \lim\limits_{n\to\infty} \int g_n d\mu$

## 非负可测函数的$L$积分

设$f\in \overline{\mathcal{L}}^+(\Omega, \mathcal{F})$，对任意满足$f_n \uparrow f$的$\{f_n, n\geq 1\} \subseteq S^+(\Omega, \mathcal{F})$，令

$$
\int f d\mu := \lim\limits_{n\to\infty} \int f_n d\mu
$$

知：$\int f d\mu$与$\{f_n\}$的选择无关。

设$f,g \in \overline{\mathcal{L}}^+(\Omega, \mathcal{F}), \lambda \in \mathbb{R}^*$，则

1. $\int \lambda f d\mu = \lambda \int f d\mu$
2. $\int (f+g) d\mu = \int f d\mu + \int g d\mu$
3. $f \leq g \implies \int f d\mu \leq \int g d\mu$

设$f \in \overline{\mathcal{L}}^+(\Omega, \mathcal{F})$，令$A_t=\{f \geq t\}$,则$\mu(A_t) \leq \frac{1}{t} \int f I_{A_t} d\mu \leq \frac{1}{t} \int f d\mu, \forall t \in \mathbb{R}^+$。

## 一般可测函数的$L$积分

设$f \in \overline{\mathcal{L}}(\Omega, \mathcal{F})$，若$f^+,f^-$至少有一个的积分不是$+\infty$，则称$f$的$L$积分存在(即，不出现$\infty-\infty$的无意义情况)，并规定$f$的积分为

$$
\int f d \mu := \int f^+ d \mu - \int f^- d \mu
$$

若$\int f$为实数(即，有限)，则称$f$可积（L可积）。

知：$f$可积$\iff |f|$可积。

## 复值可测函数的$L$积分

设$\mathbf{f}$为复值可测函数，若$Re\mathbf{f},Im\mathbf{f}$都可积，则称复值可测函数$\mathbf{f}$的L可积，并规定$\mathbf{f}$的积分为

$$
\int \mathbf{f} d \mu := \int Re\mathbf{f} d \mu + i \int Im\mathbf{f} d \mu
$$

$\mathbf{f}$可积 $\iff$ $Re\mathbf{f},Im\mathbf{f}$都可积$\iff |\mathbf{f}|$可积。

## 数学期望和方差

设$X$为概率空间$(\Omega, \mathcal{F}, P)$上的r.v., 若$X$关于$P$可积，则称$X$的数学期望存在，并且称$EX=\int_{\Omega} X dP$为$X$的**数学期望**。简称期望。

显然$EX$存在的充要条件是$E|X|<+\infty$。

<!-- 若$p>0$,$|P|^p$关于$P$可积，则称$E|X|^p=\int_{\Omega} |X|^p dP$为$X$的**p阶矩**。特别地，当$p=2$时，称$EX^2<+\infty$时，称$Var(X)=E(X-EX)^2$为$X$的**方差**。 -->

（因为设$f，g \in \overline{\mathcal{L}}(\Omega, \mathcal{F})$，且$f=g$ a.e., 则$\int f d\mu = \int g d\mu$.）当仅涉及积分问题时， a.e. 相等的函数可以不加区别，从而被积函数可以是 a.e. 可测的广义实值函数.

设 $f$ 是 a.e. 可测的广义实值函数， $A \in \mathcal{F}$， 若 $\int fI_A d\mu$ 的积分存在(相应地，可积)，则称 $f$ 在 $A$ 上的积分存在(相应地，可积)，且规定 $f$ 在 $A$ 上的积分为$\int_{A} f d\mu$。

## Lebesgue 积分的性质

1. 非负可测函数的L积分存在
2. 设$f \in \overline{\mathcal{L}}(\Omega, \mathcal{F})$，则$|f|$的积分存在，并且$|\int f d\mu| \leq \int |f| d\mu$
3. 设$f，g \in \overline{\mathcal{L}}^+(\Omega, \mathcal{F})$，且$f=g$ a.e., 则$\int f d\mu = \int g d\mu$
4. 设$f，g \in \overline{\mathcal{L}}(\Omega, \mathcal{F})$，且$f=g$ a.e., 则$f,g$中其中一个积存存在，另一个积分也存在，并且$\int f d\mu = \int g d\mu$.
5. 设 $f \in \overline{\mathcal{L}}(\Omega, \mathcal{F})$ ， $A$ 为零测集，则 $\int_{A} f d\mu = 0$.
6. 设 $f \in \overline{\mathcal{L}}(\Omega, \mathcal{F})$ 的积分存在，则
7. $f$可积 $\implies$ $|f|<+\infty$ a.e.
8. $\int |f| d\mu =0 \implies f=0$ a.e.
9. $(\forall A \in \mathcal{F}, \int_{A} f d\mu \geq 0) \implies f \geq 0$ a.e.
10. 设$f,g$为广义实值函数，且$f+g$有定义，则$(f+g)^+\leq f^+ + g^+, (f+g)^- \leq f^- + g^-$
11. 设$f,g \in \overline{\mathcal{L}}(\Omega, \mathcal{F})$ 的积分都存在，则
    - （齐次性 homogeneity）$\int c f d\mu = c \int f d\mu, \forall c \in \mathbb{R}$
    - （线性性 linearity）若$\int f d\mu + \int g d\mu$有意义， 则 $f+g$ a.e. 有定义，且$f+g$的积分存在，且$\int (f+g) d\mu = \int f d\mu + \int g d\mu$
    - （单调性 monotonicity）若$f \leq g$ a.e.，则$\int f d\mu \leq \int g d\mu$
12. $\int 1 d\mu = \mu(\Omega)$
13. 若实值函数$f$能表示成$f=\sum_{i=1}^{\infty} a_i I_{A_i}$的形式，其中$a_i \in \mathbb{R}$，$\{A_i, i\geq 1\} \subsetneq \mathcal{F}$为$\Omega$的一个划分，那么称$f$为初等函数。有以下三个结论
    - $f$是可测函数
    - 若$f$的积分存在，则$\int f d\mu = \sum_{i=1}^{\infty} a_i \mu(A_i)$
    - $f$可积 等价于 $\sum_{i=1}^{\infty} |a_i| \mu(A_i) < +\infty$
14. 设$f$为a.e. 有限的广义实值可测函数，且$\mu$为有限测度，则以下三条等价
    - $f$可积
    - $\sum_{i=1}^{\infty} n \mu(n \leq |f| < n+1) < +\infty$
    - $\sum_{i=1}^{\infty} \mu(|f| \geq n) < +\infty$
15. 若设$f \in \overline{\mathcal{L}}(\Omega, \mathcal{F})$ 的积分存在，且恒非负（或恒非正），$c \in \overline{\mathbb{R}}$,则$cf$积分存在，且$\int cf=c\int f$
16. $A \in \mathcal{F}, \int I_A=\mu(A)$
