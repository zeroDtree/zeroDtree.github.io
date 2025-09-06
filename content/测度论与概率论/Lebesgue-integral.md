---
title: Lebesgue 积分（L积分）
---

本节恒设$(\Omega, \mathcal{F}, \mu)$为给定的测度空间，所有函数都是定义在$\Omega$上，广义实值函数。

## 前置

- [[测度论与概率论/measurable-func]]
- [[测度论与概率论/almost-everywhere]]

## 非负简单可测函数的L积分

设$f=\sum_{i=1}^{n} a_i I_{A_i} \in S^+(\Omega, \mathcal{F})$, 称广义实数$\sum_{i=1}^{n} a_i \mu(A_i)$为$f$的**L积分**，记作$\int f d\mu$或$\mu(f)$。

$\int f d\mu$与$f$的表示形式无关。

设$f,g \in S^+(\Omega, \mathcal{F}), \lambda \geq 0$，则

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

设$f,g \in \overline{\mathcal{L}}^+(\Omega, \mathcal{F}), \lambda \geq 0$，则

1. $\int \lambda f d\mu = \lambda \int f d\mu$
2. $\int (f+g) d\mu = \int f d\mu + \int g d\mu$
3. $f \leq g \implies \int f d\mu \leq \int g d\mu$

设$f \in \overline{\mathcal{L}}^+(\Omega, \mathcal{F})$，令$A_t=\{f \geq t\}$,则$\mu(A_t) \leq \frac{1}{t} \int f I_{A_t} d\mu \leq \frac{1}{t} \int f d\mu, \forall t > 0$。

## 一般可测函数的L积分

设$f \in \overline{\mathcal{L}}(\Omega, \mathcal{F})$，若$f^+,f^-$至少有一个的积分不是$+\infty$，则称$f$的$L$积分存在(即，不出现$\infty-\infty$的无意义情况)，并规定$f$的积分为

$$
\int f d \mu := \int f^+ d \mu - \int f^- d \mu
$$

若$\int f$为实数(即，有限)，则称$f$可积（L可积）。

知：$f$可积$\iff |f|$可积。

## 复值可测函数的L积分

设$\mathbf{f}$为复值可测函数，若$Re\mathbf{f},Im\mathbf{f}$都可积，则称复值可测函数$\mathbf{f}$的L可积，并规定$\mathbf{f}$的积分为

$$
\int \mathbf{f} d \mu := \int Re\mathbf{f} d \mu + i \int Im\mathbf{f} d \mu
$$

$\mathbf{f}$可积 $\iff$ $Re\mathbf{f},Im\mathbf{f}$都可积$\iff |\mathbf{f}|$可积。

## 数学期望和方差

设$X$为概率空间$(\Omega, \mathcal{F}, P)$上的r.v., 若$X$关于$P$可积，则称$X$的数学期望存在，并且称$EX=\int_{\Omega} X dP$为$X$的**数学期望**。简称期望。

显然$EX$存在的充要条件是$E|X|<+\infty$。

<!-- 若$p>0$,$|P|^p$关于$P$可积，则称$E|X|^p=\int_{\Omega} |X|^p dP$为$X$的**p阶矩**。特别地，当$p=2$时，称$EX^2<+\infty$时，称$Var(X)=E(X-EX)^2$为$X$的**方差**。 -->

## Lebesgue 积分的性质
