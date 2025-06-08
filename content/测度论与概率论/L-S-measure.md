---
title: Lebesgue-Stieltjes测度
---

本节利用(Caratheodory)测度扩张定理构造$\mathbb{R}^d$上的Lebesgue-Stieltjes测度。

## 定义

设$F:\mathbb{R}^d \to \mathbb{R},\mathbf{e}:=(1,1,\cdots,1)\in \mathbb{R}^d,C(F):=\{x\in \mathbb{R}^d \mid F \text{在} x \text{处连续}\}$

$F$在点$\mathbf{x}$处连续，等价于$\forall \epsilon > 0, \exists \delta > 0, \forall \mathbf{y}, \mathbf{x} - \delta \mathbf{e} < \mathbf{y} < \mathbf{x}+\delta \mathbf{e},d(F(\mathbf{x}), \mathbf{y})<\epsilon$

称$F$在$\mathbf{x}$处**上连续**，若$\forall \epsilon > 0, \exists \delta > 0, \forall \mathbf{y}, \mathbf{x} < \mathbf{y} < \mathbf{x}+\delta \mathbf{e},d(F(\mathbf{x}), \mathbf{y})<\epsilon$

称$F$在$\mathbf{x}$处**下连续**，若$\forall \epsilon > 0, \exists \delta > 0, \forall \mathbf{y}, \mathbf{x} - \delta \mathbf{e} < \mathbf{y} < \mathbf{x},d(F(\mathbf{x}), \mathbf{y})<\epsilon$

称$F:\mathbb{R}^d \to \mathbb{R}$为**Lebesgue-Stieltjes函数**，若

- $F$ 处处上连续
- $F$ 在任意矩形$(\mathbf{a},\mathbf{b}]$上具有非负增量,即

  $$
  \Delta_{(\mathbf{a},\mathbf{b}]}F:=\sum_{\mathbf{c} \in \{0,1\}^d} (-1)^{\mathbf{c}^T \mathbf{c}} F(\mathbf{\mathbf{d_c}}) \geq 0
  $$

  where $d_i=a_i$ if $c_i=1$ and $d_i=b_i$ if $c_i=0$

$\mu_{F}:=\Delta_{(\mathbf{a},\mathbf{b}]}F$

$\mathcal{E}:=\{(\mathbf{a},\mathbf{b}] \mid \mathbf{a},\mathbf{b} \in \mathbb{R}^d\}$，$\mathcal{E}$是$\mathbb{R}^d$上的一个半环。

称$F$为分布函数(distribution function, d.f.)，若$F$是Lebesgue-Stieltjes函数。且还满足以下三个条件：

- $F$ 单调不减：$\mathbf{x}\leq\mathbf{y} \implies F(\mathbf{x}) \leq F(\mathbf{y})$
- $\forall i \in [d],F(x_1,\cdots,x_{i-1},-\infty,x_{i+1},\cdots,x_d):= \lim\limits_{x_i \to -\infty}(x_1, \cdots, x_{i-1},x_i,x_{i+1},\cdots,x_d)=0$
- $F(+\infty):=\lim\limits_{\mathbf{x} \to +\infty} F(\mathbf{x})=1$, 即$\forall \epsilon > 0, \exists M >0, s.t. \forall i \in [d], x_i > M, |F(\mathbf{x}) - 1| < \epsilon$

称$F$为准分布函数(quasi-distribution function, q.d.f.)，若存在 d.f. $G$, s.t. $F(\mathbf{x})=\sigma^2G(\mathbf{x})$，其中$\sigma^2>0$

## 性质

1. $\mu_{F}$是$\mathcal{E}$上的一个有限可加测度。

## 证明

1. $\mu_{F}$是$\mathcal{E}$上的一个有限可加测度。

只需证明有限可加性，即若$\mathbf{I}^{(i)}:=(\mathbf{a}^{(i)},\mathbf{b}^{(i)}],i\in [m]$两两不交，且$\bigcup_{i=1}^m \mathbf{I}^{(i)}:= \mathbf{I} = (\mathbf{a},\mathbf{b}] \in \mathcal{E}$，则

$$
\mu_{F}(\mathbf{I}) = \sum_{i=1}^m \mu_{F}(\mathbf{I}^{(i)})
$$

$m=2$ 时
$(\mathbf{a},\mathbf{b}]=\bigcup_{i=1}^2 (\mathbf{a}^{(i)},\mathbf{b}^{(i)}]$
不妨设包含$\mathbf{b}$的矩形为$\mathbf{I}^{(1)}=(\mathbf{a}^{(1)},\mathbf{b}^{(1)}]=\left((a^{(1)}_{1},a^{(1)}_{2},\cdots,a^{(1)}_{d}),(b_{1},b_{2},\cdots,b_{d})\right]$,

则$\mathbf{a}^{(1)}$一定不等于$\mathbf{a}$.
因此存在$k \in [d]$,使得$a_{k} < a^{(1)}_{k}:=c$

则$\mathbf{a}^{(1)}$一定等于$(a_1,\cdots,a_{k-1},c,a_{k+1},\cdots,a_{d})$, 即$\mathbf{I}^{(1)}=\left((a_1, a_2, \cdots, c,\cdots,a_{d}),\mathbf{b}\right]$, $\mathbf{I}^{(2)}=\left((a_1, a_2, \cdots, a_d), (b_1,b_2, \cdots, c, \cdots, b_d) \right]$
为什么呢？

这里先给一个显然的引理：
**Lemma 1**: 空间中任意两个点$\mathbf{a},\mathbf{b}$可以确定一个矩形$\mathbf{I}:=\left(\min(\mathbf{a},\mathbf{b}), \max(\mathbf{a},\mathbf{b}) \right]$,其中$\min$和$\max$都是**逐元素**取最小和最大。若$\mathbf{a},\mathbf{b}$都含于某个矩形$(\mathbf{c},\mathbf{d}]$，则$\mathbf{I} \subseteq (\mathbf{c},\mathbf{d}]$


易知：$\mathbf{I}^{(1)}\subseteq \left((a_1, a_2, \cdots, c,\cdots,a_{d}),\mathbf{b}\right]$

若$\left((a_1, a_2, \cdots, c,\cdots,a_{d}),\mathbf{b}\right]$中包含$\mathbf{I}^{(2)}$中的点$\mathbf{t}:=(t_1,t_2,\cdots,t_d)$。

知：$\forall i \in [d], a_i < t_i \leq b_i \wedge c < t_k$

知：$\mathbf{a} \in \mathbf{I}^{(2)}$

根据Lemma 1，有$(\mathbf{a},\mathbf{t}] \subseteq \mathbf{I}^{(2)}$
