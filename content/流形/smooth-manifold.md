---
title: smooth manifold（光滑流形）
---

## 前置

- [[点集拓扑/拓扑空间]]
- [[点集拓扑/子空间]]

## 定义

- A topological space $M$ is called an **$m$-dimensional manifold** if $M$ satisfies the following:

  - Hausdorff: $M$ is a Hausdorff space
  - Second countable: $M$ is a second countable space
  - Locally Euclidean: For any $x \in M$, there is an open neighborhood $U_x$ of $x$ that is homeomorphic to some open set in $\mathbb{R}^m$.

- We call $(U,\phi)$ a **coordinate chart, or chart**, if $U$ is an open set of $M$, $U'$ is an open set of $\mathbb{R}^m$, and $\phi$ is a homeomorphism from $U$ to $U'$. (Note that homeomorphisms are continuous mappings, and continuous mappings are defined on topological spaces, so $U$ and $U'$ here should be considered relative topological spaces.) $U$ is called the **coordinate domain or coordinate neighborhood**. If $\phi(p)=0$, then the chart is said to be **centered at p.**
  If, in addition, $\phi(U)$ is an open ball in $\mathbb{R}^n$, then $U$ is called a **coordinate ball**; if $\phi(U)$ is an open cube, $U$ is a **coordinate cube**. The map $\phi$ is called a **(local) coordinate map**, and the component functions $x_1, \ldots, x_n$ of $\phi$, defined by $\phi(p) = (x_1(p), \ldots, x_n(p))$, are called **local coordinates on $U$**. We sometimes write things such as “$(U,\phi)$ is a chart containing $p$” as shorthand for “$(U,\phi)$ is a chart whose domain $U$ contains $p$.” If we wish to emphasize the coordinate functions $x_1, \ldots, x_n$ instead of the coordinate map $\phi$, we sometimes denote the chart by $(U,( x_1, \ldots, x_n))$ or $(U, (x_i))$.

## 性质

1. Every topological manifold has a countable basis of precompact coordinate balls.
