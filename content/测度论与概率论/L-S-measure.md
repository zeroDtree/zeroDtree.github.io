---
title: Lebesgue-Stieltjes测度
---

本节利用(Caratheodory)测度扩张定理构造$\mathbb{R}$上的Lebesgue-Stieltjes测度。

## 定义

设$F:\mathbb{R}^d \to \mathbb{R},\mathbf{e}:=(1,1,\cdots,1)\in \mathbb{R}^d,C(F):=\{x\in \mathbb{R}^d \mid F \text{在} x \text{处连续}\}$

$F$在点$\mathbf{x}$处连续，等价于$\forall \epsilon > 0, \exist \delta > 0, \forall \mathbf{y}, \mathbf{x} - \delta \mathbf{e} < \mathbf{y} < \mathbf{x}+\delta \mathbf{e},d(F(\mathbf{x}), \mathbf{y})<\epsilon$

称$F$在$\mathbf{x}$处**上连续**，若$\forall \epsilon > 0, \exist \delta > 0, \forall \mathbf{y}, \mathbf{x} < \mathbf{y} < \mathbf{x}+\delta \mathbf{e},d(F(\mathbf{x}), \mathbf{y})<\epsilon$

称$F$在$\mathbf{x}$处**下连续**，若$\forall \epsilon > 0, \exist \delta > 0, \forall \mathbf{y}, \mathbf{x} - \delta \mathbf{e} < \mathbf{y} < \mathbf{x},d(F(\mathbf{x}), \mathbf{y})<\epsilon$

称$F:\mathbb{R}^d \to \mathbb{R}$为**Lebesgue-Stieltjes函数**，若

- $F$ 处处上连续
- $F$ 在任意矩形$(\mathbf{a},\mathbf{b}]$上具有非负增量,即

  $$
  \Delta_{(\mathbf{a},\mathbf{b}]}F:=\sum_{\mathbf{c} \in \{0,1\}^d} (-1)^{\mathbf{c}^T \mathbf{c}} F(\mathbf{\mathbf{d_c}}) \geq 0
  $$

  where $d_i=a_i$ if $c_i=1$ and $d_i=b_i$ if $c_i=0$

$\mu_{F}:=\Delta_{(\mathbf{a},\mathbf{b}]}F$

## 性质

$\mathcal{E}:=\{(a,b] \mid a,b \in \mathbb{R}^d\}$，易得$\mathcal{E}$是$\mathbb{R}^d$上的一个半环。

$\mu_{F}$是$\mathcal{E}$上的一个有限可加测度。

### 矩形

符合约定

- Vector is denoted as bold letter, e.g. $\bold{a}$, $a_i$ means the $i$th element of $\mathbf{a}$.
- $[d]:=\{1,2,\cdots,d\}$

两个点$\mathbf{a},\mathbf{b} \in \mathbb{R}^d$，可以确定一个矩形$[\mathbf{a},\mathbf{b}]$，
矩形的所有顶点构成的集合$D =\left\{(c_1,c_2,\cdots,c_d) \mid c_i \in \{a_i,b_i\},i\in [d] \right\}$

设$I$为至多可数集，$\bigcup_{i \in I} [\mathbf{a}^i,\mathbf{b}^i] \supseteq [\mathbf{a},\mathbf{b}]$，且这些小矩形$[\mathbf{a}^i,\mathbf{b}^i]$只可能在边界处相交.

小矩形$[\mathbf{a}^i,\mathbf{b}^i]$的所有顶点构成的集合为$D_i = \left\{(c_1,c_2,\cdots,c_d) \mid c_j \in \{a^i_j,b^i_j\},j\in [d]\right\}$

对于$\mathbb{R}^d$中任意一点$\mathbf{c}$,都可以定义一个函数$f_{\mathbf{c}}:{I} \to \{0,1\}$，

$$
f_{\mathbf{c}}(i):=
\begin{cases}
1, & \text{if } \mathbf{c} \in D_i \\
0, & \text{otherwise}
\end{cases}
$$

$S_{\mathbf{c}} := \sum_{i \in I} f_{\mathbf{c}}(i)$

$\forall \mathbf{c}, \forall i, S_{\mathbf{c}}(i) < +\infty$,因为每个点至多属于$C^{d}_{2d}$个小矩形的顶点。

命题：$\forall i \in [d], \forall \mathbf{c} \in D_i$, if $\mathbf{c} \not\in D$, then $S_{\mathbf{c}} \equiv 0 (\text{mod} 2)$
