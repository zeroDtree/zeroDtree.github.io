---
title: holant problem
tags:
  - 计算理论
---

- [1. 定义](#1-定义)
- [2. 结论](#2-结论)
- [proof](#proof)

## 1. 定义

- signature(local constraint function): A map $f:A\to B$ is a signature if (($\exists n \in \mathbb{N}, q\in \mathbb{Z}^+$ s.t. $A=[q]^n$) and ($\exists$ a commutative semiring $R$ s.t. $B=R$)). The set of signatures is denoted by $\mathcal{F}$
- symmetric signature: A signature $f:[q]^n\to R$ is symmetric if $f$ is invariant under permutation of the variables
- signature grid: A signature grid $\Omega = (G,\pi)$ over $\mathcal{F}$ consists of a graph $G = (V, E )$ and a mapping $\pi$ that assigns to each vertex $v \in V$ an $f_v \in \mathcal{F}$ and a linear order(total order) of the incident edges at $v$.The arity of $f$ is equal to the degree at $v$, and the incident edges at $v$ are associated with the input variables of $f_v$.
- planar signature grid: A planar signature grid is a signature grid such that its underlying graph is planar and for some planar embedding, for every vertex $v$, the linear order of the incident edges at $v$ agrees with the clockwise cyclic order of the incident edges at $v$ in the embedding starting with some particular edge.
- bipartite signature grid: For signature sets $F$ and $G$, a bipartite signature grid over $(F|G)$ is a signature grid $\Omega = (H,\pi)$ over $F\cup G$, where $H=(V,E)$ is a bipartite graph with bipartition $V=(V_1,V_2)$ such that $\pi(V_1)\subseteq F$ and $\pi(V_2)\subseteq G$.
- Holant problem $Holant_q(\mathcal{F})$:
  - input: A signature grid $\Omega = (G=(V,E),\pi)$ over $\mathcal{F}$
  - output: $Holant_q(\Omega;\mathcal{F}) = \sum_{\sigma:E \to [q]} \prod_{v\in V} f_v(\sigma |_{E(v)})$, where $E(v)$ is the set of edges incident to $v$
- tractable: polynomial-time computable
- #P is the set of functions $f : \{0,1\}^* \to \mathbb{N}$ such that there exists a polynomial $p : \mathbb{N} \to \mathbb{N}$ and a polynomial-time deterministic Turing machine $V$, called the verifier, such that for every $x \in \{0,1\}^*$, $f(x) = |\{y \in \{0,1\}^{p(|x|)} : V(x,y) = 1\}|$ (In other words, $f(x)$ equals the size of the set containing all of the polynomial-size certificates).

## 2. 结论

- $CSP_q^d(\mathcal{F}) \equiv_T Holant_q(\mathcal{EQ}_d|\mathcal{F})=Holant_q(\mathcal{EQ}_d \cup \mathcal{F})$
- Let $\mathcal{F}$ be a set of signatures over a domain of size $q$. If there exists an $\mathcal{F}$-gate with signature $f$, then $\text{Holant}_q(\mathcal{F}, f) \leq_T \text{Holant}_q(\mathcal{F})$.

- Let $\mathcal{F}$ and $\mathcal{G}$ be sets of complex-valued signatures over a domain of size $q$. Suppose $\Omega$ is a bipartite signature grid over $(\mathcal{F} \mid \mathcal{G})$. If $T \in \text{GL}_q(\mathbb{C})$, then $\text{Holant}_q(\Omega; \mathcal{F} \mid \mathcal{G}) = \text{Holant}_q(\Omega'; \mathcal{F}T \mid T^{-1}\mathcal{G}),$ where $\Omega'$ is the corresponding signature grid over $(\mathcal{F}T \mid T^{-1}\mathcal{G})$.

## proof

### 记号与基变换

设 $G=(U,V,E)$ 是有限无向二分图。对每个顶点 $w\in U\cup V$，固定关联边集 $E(w)$ 的一个次序，并记 $d_w=|E(w)|$。左、右两侧顶点分别赋予复值签名

$$
f_u:[q]^{d_u}\to\mathbb C\quad (u\in U),
\qquad
g_v:[q]^{d_v}\to\mathbb C\quad (v\in V).
$$

若 $\sigma:E\to[q]$ 是边赋值，则 $\sigma|_{E(w)}$ 表示按照上述固定次序排列的局部赋值元组。对应的 Holant 值为

$$
\operatorname{Holant}_q(G;\mathcal F\mid\mathcal G)
=
\sum_{\sigma\in[q]^E}
\prod_{u\in U}f_u\bigl(\sigma|_{E(u)}\bigr)
\prod_{v\in V}g_v\bigl(\sigma|_{E(v)}\bigr),
$$

其中 $\mathcal F=\{f_u\}_{u\in U}$，$\mathcal G=\{g_v\}_{v\in V}$。

取任意 $T\in\operatorname{GL}_q(\mathbb C)$。对 $u\in U$，定义 $f'_u=f_uT^{\otimes d_u}$，即

$$
f'_u(x_1,\ldots,x_{d_u})
=
\sum_{y_1,\ldots,y_{d_u}\in[q]}
f_u(y_1,\ldots,y_{d_u})
\prod_{i=1}^{d_u}T_{y_i,x_i}.
$$

对 $v\in V$，定义 $g'_v=(T^{-1})^{\otimes d_v}g_v$，即

$$
g'_v(x_1,\ldots,x_{d_v})
=
\sum_{z_1,\ldots,z_{d_v}\in[q]}
g_v(z_1,\ldots,z_{d_v})
\prod_{j=1}^{d_v}(T^{-1})_{x_j,z_j}.
$$

分别记 $\mathcal F T=\{f'_u\}_{u\in U}$ 和
$T^{-1}\mathcal G=\{g'_v\}_{v\in V}$。左右两侧采用相反的变换方向，正是为了使每条边上的 $T$ 与 $T^{-1}$ 在张量收缩时相消。

### 定理

**Valiant 全息变换定理（二分 Holant 形式）。** 对任意上述二分签名网格和任意 $T\in\operatorname{GL}_q(\mathbb C)$，都有

$$
\operatorname{Holant}_q(G;\mathcal F\mid\mathcal G)
=
\operatorname{Holant}_q(G;\mathcal F T\mid T^{-1}\mathcal G).
$$

### 证明

记

$$
Z'
=
\operatorname{Holant}_q(G;\mathcal F T\mid T^{-1}\mathcal G).
$$

对任意变换后的边赋值 $\sigma'\in[q]^E$，将各顶点内部的求和变量分别拼接为全局赋值 $\sigma,\tau\in[q]^E$，可得

$$
\prod_{u\in U}f'_u\bigl(\sigma'|_{E(u)}\bigr)
=
\sum_{\sigma\in[q]^E}
\left(\prod_{u\in U}f_u\bigl(\sigma|_{E(u)}\bigr)\right)
\left(\prod_{e\in E}T_{\sigma(e),\sigma'(e)}\right),
$$

以及

$$
\prod_{v\in V}g'_v\bigl(\sigma'|_{E(v)}\bigr)
=
\sum_{\tau\in[q]^E}
\left(\prod_{v\in V}g_v\bigl(\tau|_{E(v)}\bigr)\right)
\left(\prod_{e\in E}(T^{-1})_{\sigma'(e),\tau(e)}\right).
$$

将二式代入 $Z'$。由于所有集合均有限，可以交换求和次序，于是

$$
\begin{aligned}
Z'
&=
\sum_{\sigma\in[q]^E}\sum_{\tau\in[q]^E}
\left(\prod_{u\in U}f_u\bigl(\sigma|_{E(u)}\bigr)\right)
\left(\prod_{v\in V}g_v\bigl(\tau|_{E(v)}\bigr)\right)\\
&\qquad\cdot
\sum_{\sigma'\in[q]^E}
\prod_{e\in E}
T_{\sigma(e),\sigma'(e)}
(T^{-1})_{\sigma'(e),\tau(e)}.
\end{aligned}
$$

内层被积项在不同边之间没有共享变量，而 $[q]^E$ 是各边状态空间的笛卡尔积，因此

$$
\begin{aligned}
&\sum_{\sigma'\in[q]^E}
\prod_{e\in E}
T_{\sigma(e),\sigma'(e)}
(T^{-1})_{\sigma'(e),\tau(e)}\\
&\quad=
\prod_{e\in E}
\sum_{k\in[q]}T_{\sigma(e),k}(T^{-1})_{k,\tau(e)}\\
&\quad=
\prod_{e\in E}(TT^{-1})_{\sigma(e),\tau(e)}
=
\prod_{e\in E}\delta_{\sigma(e),\tau(e)},
\end{aligned}
$$

其中 $\delta$ 是 Kronecker delta。最后一个乘积当且仅当 $\sigma=\tau$ 时等于 $1$，否则等于 $0$。所以对 $\tau$ 的求和坍缩为唯一可能的赋值 $\tau=\sigma$：

$$
\begin{aligned}
Z'
&=
\sum_{\sigma\in[q]^E}
\prod_{u\in U}f_u\bigl(\sigma|_{E(u)}\bigr)
\prod_{v\in V}g_v\bigl(\sigma|_{E(v)}\bigr)\\
&=
\operatorname{Holant}_q(G;\mathcal F\mid\mathcal G).
\end{aligned}
$$

故定理成立。

### 因子化恒等式

下面详细说明证明中的按边因子化。设

$$
E=\{e_1,e_2,\ldots,e_m\},\qquad m=|E|,
$$

并定义

$$
A(e,k)=T_{\sigma(e),k}(T^{-1})_{k,\tau(e)}.
$$

全局赋值 $\sigma':E\to[q]$ 可以等价地写成向量

$$
\sigma'=(k_1,k_2,\ldots,k_m),\qquad k_i=\sigma'(e_i)\in[q].
$$

由于 $\sigma'$ 遍历 $[q]^E$，向量 $(k_1,\ldots,k_m)$ 恰好遍历笛卡尔积 $[q]^m$。因此证明中的内层求和可以写成多重求和：

$$
\begin{aligned}
\mathrm{LHS}
&=
\sum_{\sigma'\in[q]^E}\prod_{e\in E}A\bigl(e,\sigma'(e)\bigr)\\
&=
\sum_{k_1=1}^q\sum_{k_2=1}^q\cdots\sum_{k_m=1}^q
\prod_{i=1}^m A(e_i,k_i).
\end{aligned}
$$

每个因子 $A(e_i,k_i)$ 只依赖对应的变量 $k_i$，与其余求和变量无关。利用有限次乘法分配律，可以逐层将无关因子移出求和号：

$$
\begin{aligned}
\mathrm{LHS}
&=
\sum_{k_1=1}^q A(e_1,k_1)
\left[
\sum_{k_2=1}^q A(e_2,k_2)
\left[
\cdots
\left[
\sum_{k_m=1}^q A(e_m,k_m)
\right]
\cdots
\right]
\right]\\
&=
\left(\sum_{k_1=1}^q A(e_1,k_1)\right)
\left(\sum_{k_2=1}^q A(e_2,k_2)\right)
\cdots
\left(\sum_{k_m=1}^q A(e_m,k_m)\right)\\
&=
\prod_{e\in E}\left(\sum_{k\in[q]}A(e,k)\right).
\end{aligned}
$$

所以，这一步并不是对任意求和与乘积进行交换；它成立的关键是求和域 $[q]^E$ 是各边状态空间的笛卡尔积，并且每个因子只依赖一条边上的求和变量。
