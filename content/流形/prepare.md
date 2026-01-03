---
title: 光滑流形预备
---

- [前置](#前置)
- [定义](#定义)
- [性质](#性质)

## 前置

- [[点集拓扑/拓扑空间]]
- [[点集拓扑/子空间]]
- [[点集拓扑/连续映射]]

## 定义

- If $\forall t \in T, X_t$ is a set, their disjoint union is the set $$\bigsqcup_{t \in T} X_t = \{(x,t) \mid x \in X_t, t \in T\}$$
- Given an indexed family of topological spaces $\forall t \in T, X_t$ is a topological space, we define the disjoint union topology on $\bigsqcup_{t \in T} X_t$ by declaring a subset of $\bigsqcup_{t \in T} X_t$ to be open if and only if its intersection with each $X_t$ is open in $X_t$.

## 性质

1. Let $X$ be a second-countable topological space. Every open cover of $X$ has a countable subcover.
2. CHARACTERISTIC P ROPERTY: If $\forall t \in T, (X_t,\tau_t)$ are topological spaces, a map $F: B \to \prod_{t \in T} X_t$ is continuous if and only if each of its component functions $F_t = \pi_t \circ F: B \to X_t$ is continuous.
3. The product topology is the unique topology on $\prod_{t \in T} X_t$ for which the characteristic property holds
4. Given any continuous maps $F_t: X_t \to Y_t$ for $t\in T$, the product map
   $\mathbf{F}: \prod_{t \in T} X_t \to \prod_{t \in T} Y_t$ is continuous, where $\mathbf{F}_t(x) = F_t(x_t)$ for all $x \in \prod_{t \in T} X_t$
5. If $S_t$ is a subspace of $X_t$ for $t \in T$, the product topology and the subspace topology on $\prod_{t \in T} S_t \subseteq \prod_{t \in T} X_t$ coincide.
6. For any $t \in T$ and any choices of points $a_j \in X_j$ for $j \neq i$, the map $x \mapsto (x_t, t \in T | x_i = x \wedge x_j = a_j )$ is a topological embedding of $X_i$ into the product space $\prod X_1$.
7. Any product of Hausdorff spaces is Hausdorff.
8. Countable product of first-countable spaces is first-countable.
9. Countable product of second-countable spaces is second-countable.
10. (Properties of the Disjoint Union Topology). Suppose $\forall t \in T, X_t$ is a topological space, and $\bigcup_{t \in T} X_t$ is endowed with the disjoint union topology.
11. CHARACTERISTIC P ROPERTY: If $Y$ is a topological space, a map $F: \bigsqcup_{t \in T} X_t \to Y$ is continuous if and only if $F \circ \iota_t: X_t \to Y$ is continuous for each $t \in T$. where $\iota_t: X_t \to \bigsqcup_{t \in T} X_t: x \mapsto (x,t)$
12. The disjoint union topology is the unique topology on $\bigsqcup_{t \in T} X_t$ for which the characteristic property holds.
13. A subset of $\bigsqcup_{t \in T} X_t$ is closed if and only if its intersection with each $X_t$ is closed.
