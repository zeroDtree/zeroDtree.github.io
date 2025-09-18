---
title: 相对拓扑
---

## Prerequisites

- [[测度论与概率论/拓扑空间]]

## 定义

$(X,\tau)$为拓扑空间，称$(X_0,X_0 \cap \tau)$为相对拓扑(relative topology, 又称子空间)，简记为$X_0$

#### 性质

1. 子空间$X_0$中的开集为$X$中的开集 $\Leftrightarrow$ $X_0$为$X$中的开集
2. 子空间$X_0$中的闭集为$X$中的闭集 $\Leftrightarrow$ $X_0$为$X$中的闭集
3. 若$F$为$X$中的闭集，则$F \cap X_0$为$X_0$中的闭集
4. 第一可数空间的子空间都为第一可数空间
5. 第二可数空间的子空间都为第二可数空间
6. $T_1$空间的子空间为$T_1$空间
7. $T_2$(Hausdorff)空间的子空间为$T_2$空间
8. 若$K$为$X$中的紧集，$X_0$为$X$的闭子空间，则$K \cap X_0$为$X_0$中的紧集
9. $X_0\subseteq X$,$f:X \to Y$连续，则$f:X_0 \to f(X_0)$也连续,这里的连续是将$X_0$和$f(X_0)$看作$X$和$Y$的子空间
10. 在子空间中紧与在原空间中紧是等价的。
11. Let $X$ be a topological space and let $S$ be a subspace of $X$.
    - **CHARACTERISTIC PROPERTY:** If $Y$ is a topological space, a map $F\colon Y\to S$ is continuous if and only if the composition $\iota_S\circ F\colon Y\to X$ is continuous, where $\iota_S\colon S\to X$ is the inclusion map (the restriction of the identity map of $X$ to $S$).
    - The subspace topology is the unique topology on $S$ for which
      the characteristic property holds.
    - The inclusion map $\iota_S\colon S\to X$ is a topological embedding.
12. - **Continuity Is Local**： Continuity is a local property, in the following sense:
      if $F\colon X\to Y$ is a map between topological spaces such that every point $p\in X$ has a open neighborhood $U$ on which the restriction $F|_U$ is continuous, then $F$ is continuous.
13. **Gluing Lemma for Continuous Maps**
    Let $X$ and $Y$ be topological spaces, and suppose one of the following conditions holds:

    - $B_1,\dots,B_n$ are finitely many closed subsets of $X$ whose union is $X$.
    - $\{B_i\}_{i\in A}$ is a collection of open subsets of $X$ whose union is $X$.

    Suppose that for all $i$ we are given continuous maps $F_i\colon B_i\to Y$ that agree on overlaps:$F_i|_{B_i\cap B_j}=F_j|_{B_i\cap B_j}.$
    Then there exists a unique continuous map $F\colon X\to Y$ whose restriction to each $B_i$ is equal to $F_i$.
