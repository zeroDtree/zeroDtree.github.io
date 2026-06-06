---
title: Lebesgue-Stieltjes测度
---

本节利用(Caratheodory)测度扩张定理构造$\mathbb{R}^d$上的Lebesgue-Stieltjes测度。

## Prerequisites

- [[测度论与概率论/measure]]

## 定义

设$F:\mathbb{R}^d \to \mathbb{R},\mathbf{e}:=(1,1,\cdots,1)\in \mathbb{R}^d,C(F):=\{x\in \mathbb{R}^d \mid F \text{在} x \text{处连续}\}$

$F$在点$\mathbf{x}$处连续，等价于$\forall \epsilon > 0, \exists \delta > 0, \forall \mathbf{y}, \mathbf{x} - \delta \mathbf{e} < \mathbf{y} < \mathbf{x}+\delta \mathbf{e},d(F(\mathbf{x}), \mathbf{y})<\epsilon$

- 称$F$在$\mathbf{x}$处**上连续**，若$\forall \epsilon > 0, \exists \delta > 0, \forall \mathbf{y}, \mathbf{x} < \mathbf{y} < \mathbf{x}+\delta \mathbf{e},d(F(\mathbf{x}), \mathbf{y})<\epsilon$

- 称$F$在$\mathbf{x}$处**下连续**，若$\forall \epsilon > 0, \exists \delta > 0, \forall \mathbf{y}, \mathbf{x} - \delta \mathbf{e} < \mathbf{y} < \mathbf{x},d(F(\mathbf{x}), \mathbf{y})<\epsilon$

- 称$F:\mathbb{R}^d \to \mathbb{R}$为**Lebesgue-Stieltjes函数**(**L-S函数**)，若

- $F$ 处处上连续
- $F$ 在任意矩形$(\mathbf{a},\mathbf{b}]$上具有非负增量,即

  $$
  \Delta_{(\mathbf{a},\mathbf{b}]}F:=\sum_{\mathbf{\epsilon} \in \{0,1\}^d} (-1)^{\#(\mathbf{\epsilon}=0)} F(\mathbf{\mathbf{\mathbf{a} + \epsilon(\mathbf{b} - \mathbf{a})}}) \geq 0
  $$

  $\#(\mathbf{\epsilon}=0)$表示$\mathbf{\epsilon}$中$0$的个数。

$\mu_{F}:=\Delta_{(\mathbf{a},\mathbf{b}]}F$

$\mathcal{E}:=\{(\mathbf{a},\mathbf{b}] \mid \mathbf{a},\mathbf{b} \in \mathbb{R}^d\}$，$\mathcal{E}$是$\mathbb{R}^d$上的一个半环。

- 称$F$为分布函数(distribution function, d.f.)，若$F$是Lebesgue-Stieltjes函数(L-S函数)。且还满足以下三个条件：

- $F$ 单调不减：$\mathbf{x}\leq\mathbf{y} \implies F(\mathbf{x}) \leq F(\mathbf{y})$
- $\forall i \in [d],F(x_1,\cdots,x_{i-1},-\infty,x_{i+1},\cdots,x_d):= \lim\limits_{x_i \to -\infty}(x_1, \cdots, x_{i-1},x_i,x_{i+1},\cdots,x_d)=0$
- $F(+\infty):=\lim\limits_{\mathbf{x} \to +\infty} F(\mathbf{x})=1$, 即$\forall \epsilon > 0, \exists M >0, s.t. \forall i \in [d], x_i > M, |F(\mathbf{x}) - 1| < \epsilon$

- 称$F$为准分布函数(quasi-distribution function, q.d.f.)，若存在 d.f. $G$, s.t. $F(\mathbf{x})=\sigma^2G(\mathbf{x})$，其中$\sigma^2>0$

设$\mu$为$\mathcal{B}(\mathbb{R}^d)$上的一个$\sigma$-有限测度，称$\mu$为Lebesgue-Stieltjes测度,若对于$\mathbb{R}^d$上的任意有限区间(矩形)$I$，都有$\mu(I)<+\infty$.

$\mu(\mathbf{I})$可简记为$\mu \mathbf{I}$,例如$\mu((\mathbf{a},\mathbf{b}])= \mu(\mathbf{a},\mathbf{b}]$

设$\mu$是$(\mathbb{R}^d, \mathcal{B}(\mathbb{R}^d))$上的一个有限测度，$A\in \mathcal{B}(\mathbb{R}^d),a\in \mathbb{R}^d, I \subseteq \mathbb{R}^d$为区间,定义如下三个概念：

- 若$\mu(\partial A)=0$,则称$A$为$\mu$连续集
- 若$I$为$\mu$连续集，则称$I$为$\mu$连续区间
- 若$(-\infty, \mathbf{a}]$为连续区间，则称$\mathbf{a}$为$\mu$连续点，$\mu$连续点的全体记作$C({\mu})$

$F_i:=F\left(\underbrace{+\infty,+\infty,..., +\infty }_{i-1},  x_i, \underbrace{+\infty,+\infty,..., +\infty }_{d-i}\right)$,可以得知$F_i$为$\mathbb{R}$上的q.d.f., 且$\mu_{F_i} = \mu_{F} \circ \pi_{i}^{-1}$

## 性质

1. $\mu_{F}$是$\mathcal{E}$上的一个有限可加测度。
2. 上连续函数的(实系数)线性组合为上连续函数。
3. $\mu_{F}$在$\mathcal{E}$上的具有可列次可加性。
4. $\mu_{F}$在$\mathcal{E}$上的测度
5. $\mu_{F}$可以唯一地扩张成$\mathcal{B}(\mathbb{R}^d)$上的$\sigma$-有限测度。称$\mu_{F}$为$F$诱导的Lebesgue-Stieltjes测度。
6. 设$\mu$为$\mathcal{B}(\mathbb{R}^d)$上的一个L-S 测度，则存在$\mathbb{R}^d$上的L-S函数$F$(但不唯一)，使得由$F$诱导的测度恰好为$\mu$,i.e. $\mu_{F}=\mu$.
7. $\mathcal{B}(\mathbb{R}^d)$上的有限测度与$\mathbb{R}^d$上的q.d.f. 之间依 $\mu_{F}((\mathbf{a}, \mathbf{b}]=\Delta_{(\mathbf{a}, \mathbf{b}]}F$ 一一对应。
8. 用$\mu_{F}$表示q.d.f. $F$诱导的L-S测度，则$\mu_{F}(-\infty, \mathbf{x}]=F(\mathbf{x})$
9. 若区间$I$的每个顶点都是$\mu$连续点，则$I$为$\mu$连续区间。因为$\bigcup_{\epsilon \in \{0,1\}^d} \partial (-\infty, \mathbf{a} + \epsilon(\mathbf{b}-\mathbf{a}) ] \supseteq  \partial (\mathbf{a}, \mathbf{b}]$.
10. 设$F$是$\mathbb{R}^d$上的q.d.f. ,$\mu_{F}$是$F$诱导的$(\mathbb{R}, \mathcal{B}(\mathbb{R}^d))$上的有限测度，$\mathbf{x} \in \mathbb{R}^d$， 则$x\in C(F) \iff x\in C(\mu_{F})$
11. 设$F$是$\mathbb{R}^d$上的q.d.f.，$\mathbf{x}=(x_1,x_2,\cdots,x_d)$，若诸$x_i$都为$F_i$的连续点，则$\mathbf{x}$为$F$的连续点。

## 证明

### 1.

$\mu_{F}$是$\mathcal{E}$上的一个有限可加测度。

只需证明有限可加性，即若$\mathbf{I}^{(i)}:=(\mathbf{a}^{(i)},\mathbf{b}^{(i)}],i\in [m]$两两不交，且$\bigcup_{i=1}^m \mathbf{I}^{(i)}:= \mathbf{I} = (\mathbf{a},\mathbf{b}] \in \mathcal{E}$，则

$$
\mu_{F}(\mathbf{I}) = \sum_{i=1}^m \mu_{F}(\mathbf{I}^{(i)})
$$

$m=2$ 时
$(\mathbf{a},\mathbf{b}]=\bigcup_{i=1}^2 (\mathbf{a}^{(i)},\mathbf{b}^{(i)}]$
不妨设包含$\mathbf{b}$的矩形为$\mathbf{I}^{(1)}=(\mathbf{a}^{(1)},\mathbf{b}^{(1)}]=\left((a^{(1)}_{1},a^{(1)}_{2},\cdots,a^{(1)}_{d}),(b_{1},b_{2},\cdots,b_{d})\right]$,

则$\mathbf{a}^{(1)}$一定不等于$\mathbf{a}$.
因此存在$k \in [d]$,使得$a_{k} < a^{(1)}_{k}:=c$

则$\mathbf{a}^{(1)}$一定等于$(a_1,\cdots,a_{k-1},c,a_{k+1},\cdots,a_{d})$, 即$\mathbf{I}^{(1)}=\left((a_1, a_2, \cdots, c,\cdots,a_{d}),\mathbf{b}\right]$, $\mathbf{I}^{(2)}=\left(\mathbf{a}, (b_1,b_2, \cdots, c, \cdots, b_d) \right]$
为什么呢？

这里先给一个显然的引理：
**Lemma 1**: 空间中任意两个点$\mathbf{a},\mathbf{b}$可以确定一个矩形$\mathbf{I}:=\left(\min(\mathbf{a},\mathbf{b}), \max(\mathbf{a},\mathbf{b}) \right]$,其中$\min$和$\max$都是**逐元素**取最小和最大。若$\mathbf{a},\mathbf{b}$都属于某个矩形$(\mathbf{c},\mathbf{d}]$，则$\mathbf{I} \subseteq (\mathbf{c},\mathbf{d}]$. 更一般地， $(\mathbf{a}^{(i)})_{i=1}^n$可以确定一个矩形$\mathbf{I}:=(\min_i(\mathbf{a}^{(i)}),\max_i(\mathbf{a}^{(i)}))]$, 若每个$\mathbf{a}^{(i)}$都属于某个矩形$(\mathbf{c},\mathbf{d}]$, 则$\mathbf{I} \subseteq (\mathbf{c},\mathbf{d}]$

易知：$\mathbf{I}^{(1)}\subseteq \left((a_1, a_2, \cdots, c,\cdots,a_{d}),\mathbf{b}\right]$

若$\left((a_1, a_2, \cdots, c,\cdots,a_{d}),\mathbf{b}\right]$中包含$\mathbf{I}^{(2)}$中的点$\mathbf{t}:=(t_1,t_2,\cdots,t_d)$。

知：$\forall i \in [d], a_i < t_i \leq b_i \wedge c < t_k$

知：$\mathbf{a} \in \mathbf{I}^{(2)}$

根据Lemma 1，有$\mathbf{x}:=(b_1, b_2,\cdots, b_{k-1},t_k, b_{k+1},\cdots, b_{d}) \in \mathbf{I}^{(2)}$

又知，$\mathbf{x} \in \mathbf{I}^{(1)}$

与$\mathbf{I}^{(1)} \cap \mathbf{I}^{(2)} = \emptyset$矛盾。

不难证明$\mu_{F}$在$m=2$时的有限可加性。

设$m=k-1$是$\mu_{F}$在$\mathcal{E}$上具有有限可加性。
要证$m=k$时，$\mu_{F}$在$\mathcal{E}$上也具有有限可加性。

这里需要再给一个引理
**Lemma 2**: 若一个矩形$(\mathbf{a},\mathbf{b}]$可以被$m\geq 2$个两两不交的矩形$\mathbf{I}^{(i)}:=(\mathbf{a}^{(i)},\mathbf{b}^{(i)}],i\in [m]$覆盖，则存在矩形$U,V$,$U \cap V = \emptyset \wedge U \cup V = (\mathbf{a},\mathbf{b}]$,且$U$和$V$中都分别包含至少一个矩形$(\mathbf{a}^{(i)},\mathbf{b}^{(i)}]$

Lemma 2的证明如下：
还是设包含$\mathbf{b}$的矩形为$\mathbf{I}^{(1)}=(\mathbf{a}^{(1)},\mathbf{b}^{(1)}]$
则$\mathbf{I}^{(1)} \subseteq (\mathbf{y}_j, \mathbf{b}]:=\mathbf{J}^{(j)}, \forall j \in [d]$, 其中$\mathbf{y}_j$为将$\mathbf{a}$的第$j$个分量替换为$\mathbf{a}^{(1)}$的第$j$个分量得到的。
另任取一个不同于$\mathbf{I}^{(1)}$的矩形，不妨为$\mathbf{I}^{(2)}=(\mathbf{a}^{(2)},\mathbf{b}^{(2)}]$，则一定存在$l$，使得$\mathbf{I}^{(2)} \subseteq \mathbf{J}^{(l)}$, 否则$\mathbf{I}^{(2)}$与$\mathbf{I}^{(1)}$的交集将不为空。
Q.E.D.

根据Lemma 2, 存在矩形$U,V$,$U \cap V = \emptyset \wedge U \cup V = (\mathbf{a},\mathbf{b}]$,且$U$和$V$中都分别包含至少一个矩形$(\mathbf{a}^{(i)},\mathbf{b}^{(i)}]$, 不妨设$U$中包含$\mathbf{I}^{(1)}$，$V$中包含$\mathbf{I}^{(2)}$

$$
\begin{align}
  \mu_{F}(\mathbf{I}) &=  \mu_{F}(\mathbf{I} \cap (U \cup V))\\
  &= \mu_{F}(\mathbf{I} \cap U) + \mu_{F}(\mathbf{I} \cap V)\\
  &=\mu_{F}(\bigcup_{i=1}^m \mathbf{I}^{(i)} \cap U) + \mu_{F}(\bigcup_{i=1}^m \mathbf{I}^{(i)} \cap V)\\
  &=\mu_{F}(\bigcup_{i=1,i\not=2}^m \mathbf{I}^{(i)} \cap U) + \mu_{F}(\bigcup_{i=2}^m \mathbf{I}^{(i)} \cap V)\\
  &= \sum_{i=1,i\not=2}^m \mu_{F}(\mathbf{I}^{(i)} \cap U) + \sum_{i=2}^m \mu_{F}(\mathbf{I}^{(i)} \cap V)\\
  & = \sum_{i=1}^m \mu_{F}(\mathbf{I}^{(i)})
\end{align}
$$

Q.E.D.

### 2.

从L-S 测度到 L-S 函数：设$\mu$为$\mathcal{B}(\mathbb{R}^d)$上的一个L-S 测度，则存在$\mathbb{R}^d$上的L-S函数$F$(但不唯一)，使得由$F$诱导的测度恰好为$\mu$,i.e. $\mu_{F}=\mu$.

定义$F:= (-1)^{\#(\mathbf{x}<\mathbf{c})}\mu\left((\min(\mathbf{x},\mathbf{c}),\max(\mathbf{x},\mathbf{c})]\right)$,其中$\min$和$\max$都是逐元素取最小和最大。#表示$\mathbf{x}<\mathbf{c}$的元素(分量)个数。

$$
\Delta_{(\mathbf{a},\mathbf{b}]} F = \sum_{\epsilon \in \{0,1\}^d}(-1)^{\#(\epsilon=0)} F(\mathbf{x^{\epsilon}}), \mathbf{x^{\epsilon}}=\mathbf{a}+\epsilon(\mathbf{b}-\mathbf{a})
$$

证明：

下面只证明$F$有非负增量，即$\Delta_{(\mathbf{a},\mathbf{b}]} F \geq 0$。

将$\mu((\min(\mathbf{x}, \mathbf{y}),\max(\mathbf{x}, \mathbf{y})])$简记为$\mu\{\mathbf{x}, \mathbf{y}\}$

我们只需证明如下等式(后文称下式为**L-S测度幂分解公式**)：

$$
\begin{align}
\mu((\mathbf{a},\mathbf{b}])=\sum_{\epsilon \in \{0,1\}^d}(-1)^{\#(\epsilon=0)} (-1)^{\#(\mathbf{x}^{\epsilon}<\mathbf{c})}\mu\{\mathbf{a}+\epsilon(\mathbf{b}-\mathbf{a}),\mathbf{c}\}
\end{align}
$$

首先对于$\mathcal{B}(\mathbb{R})$上的测度，容易验证上式成立。示意图如下，$\pm$的部分被抵消掉。
![[测度论与概率论/images/mu_a_b.png]]

对与$d$维情况，我们需要先发现如下事实：一个$\mathcal{B}(\mathbb{R}^d)$上的测度，固定其中$d-1$个分量，则以剩下的一个分量为变量的函数为$\mathcal{B}(\mathbb{R})$上的测度。形式化地，若$\mu$为$\mathcal{B}(\mathbb{R}^d)$上的测度，则$\mu^{(i)}_{\mathbf{a},\mathbf{b}}((x,y]):=\mu(((a_1, a_2, \cdots, a_{i-1}, x, a_{i+1}, \cdots, a_d),(b_1, b_2, \cdots, b_{i-1}, y, b_{i+1}, \cdots, b_d)])$为$\mathcal{B}(\mathbb{R})$上的测度。

然后对$1,2,3,\cdots,d$维依次累计使用一维的L-S测度幂分解公式，即可得到$d$维的L-S测度幂分解公式。

### 3.

$\mathcal{E}:=\{(\mathbf{a},\mathbf{b}] \mid \mathbf{a},\mathbf{b} \in \mathbb{R}^d\}$，$\mathcal{E}$是$\mathbb{R}^d$上的一个半环。其中的元素被称作矩形。
若$\mathbf{I}^{(i)}:=(\mathbf{a}^{(i)},\mathbf{b}^{(i)}],i\in [m]$两两不交，且$\bigcup_{i=1}^m \mathbf{I}^{(i)}:= \mathbf{I} = (\mathbf{a},\mathbf{b}] \in \mathcal{E}$

$\forall k \in [d], D_k:=\{c \mid \exists i \text{ s.t. } c = b^{(i)}_k\}$

谬论：存在$k \in [d]$，使得$\exists c_k \in D_k$, 使得超平面$x_k=c_k$将$\mathbf{I}^{(i)}$分成两组，且两组集合中没有矩形跨越这个超平面。

反例如下：

![[测度论与概率论/images/rect_example.png]]
