---
title: smooth-manifold
date: 2024-12-09 15:33:37
tags: 光滑流形
---

## 流形定义

称**拓扑空间**$M$为 $m$ 维（拓扑）**流形**(Manifold)，若$M$满足：

- Hausdorff：$M$ 是 Hausdorff 空间
- Second countable：$M$ 是第二可数空间
- Locally Euclidean：对任意 $x \in M$，都有 $x$ 的开邻域 $U_x$，同胚于 $\mathbb{R}^m$ 的某个开集

称$(U,\phi)$为 卡(chart) 或坐标邻域(Coordinate Neighborhood),若$U$是$M$的开集，$U'$是$\mathbb{R}^m$的开集，$\phi$是$U$到$U'$的同胚映射，注意，同胚映射是连续映射，而连续映射是定义在拓扑空间上的，因此这里的$U$和$U'$应看作**相对拓扑空间**。

Let $k$ be a nonnegative integer. A real-valued function $f: U \to \mathbb{R}$ is said to be $\mathcal{C}^k$ at $p \in U$ if its partial derivatives

$$
\frac{\partial^j f}{\partial x^{i_1} \cdots \partial x^{i_j}}
$$

of all orders $j \leq k$ exist and are continuous at $p$. The function $f: U \to \mathbb{R}$ is $\mathcal{C}^\infty$ at $p$ if it is $\mathcal{C}^k$ for all $k \geq 0$; in other words, its partial derivatives $\partial^j f/\partial x^{i_1} \cdots \partial x^{i_j}$ of all orders exist and are continuous at $p$. A vector-valued function $f: U \to \mathbb{R}^m$ is said to be $\mathcal{C}^k$ at $p$ if all of its component functions $f^1,\ldots,f^m$ are $\mathcal{C}^k$ at $p$. We say that $f: U \to \mathbb{R}^m$ is $\mathcal{C}^k$ on $U$ if it is $\mathcal{C}^k$ at every point in $U$. A similar definition holds for a $\mathcal{C}^\infty$ function on an open set $U$. We treat the terms $\mathcal{C}^\infty$ and smooth as synonymous.

称两个 chart $(U_{a},\phi_{a})$和$(U_{b},\phi_{b})$是$\mathcal{C}^r$**兼容的**(compatible,相容的)，若$U_a \cap U_b \not= \emptyset \longrightarrow \phi_{a}\circ \phi_{b}^{-1}:\phi_{b}(U_a \cap U_b) \to \phi_{a}(U_a \cap U_b) \in \mathcal{C}^r$

称$\mathcal{A}=\{(U_{i},\phi_{i})\mid i \in I\}$为$M$的图册(Atlas)，其中$(U_{i},\phi_{i})$为$m$维坐标邻域，若$M \subseteq \bigcup \mathcal{A}$，且$\mathcal{A}$中 charts 两两相容。若两两$\mathcal{C}^r$兼容，则称$\mathcal{A}$为$C^r$图册。

至此可以使用 atlas 来描述拓扑流形。
称拓扑空间$M$为 $m$ 维（拓扑）流形(Manifold)，若$M$满足：

- $M$ 是 Hausdorff 和 second countable 的拓扑空间
- $M$ 上存在$C^0$图册 $\mathcal{A}$

称$M$为微分流形(Differentiable Manifold)，若$M$满足：

- $M$ 是 Hausdorff 和 second countable 的拓扑空间
- $M$ 上存在 $C^r$ 图册

若$r=\infty$，则称$M$为光滑流形(Smooth Manifold)。

称$f:M \to \mathbb{R}^n$为点$p \in M$上的**可微**(Differentiable)，若存在 chart$(U,\phi)$，使得$p \in U$，且$f \circ \phi^{-1}:\phi(U) \to \mathbb{R}^n \in \mathcal{C}^r$，若$f$在$M$上处处可微，则称$f$为$M$上的**可微函数**(Differentiable Function)。若$r=\infty$，则称$f$为$M$上的**光滑函数**(Smooth Function)。

称**连续映射**$f:M \to N$在点$p \in M$上**可微**，若存在 $M$上的 chart$(U,\phi)$ 和$N$上的 chart$(V,\psi)$，使得$p \in U$，$f(p) \in V$，且$\psi \circ f \circ \phi^{-1}:\phi(f^{-1}[V] \cap U) \to \psi(V)$在$p$点可微，若$f$在$M$上处处可微，则称$f$为$M$上的**可微映射**(Differentiable Map)。若$r=\infty$，则称$f$为$M$上的**光滑映射**(Smooth Map)。

注意: 光滑映射这里要求$f$为连续映射，是为了确保$f^{-1}[V]$是$M$中的开集.

称双射$F$为**微分同胚**(Diffeomorphism)，若$F:M \to N$是$\mathcal{C}^r$映射，且$F^{−1}$也是$\mathcal{C}^r$映射。光滑流形中默认$r=\infty$。

**图册语言描述的流形 等价于 Local Euclidean 描述的流形**

只需证明 chart 的$\mathcal{C}^0$兼容性。因为连续映射复合连续映射为连续映射，所以$\phi_a \circ \phi_b^{-1}:\phi_b(U_a \cap U_b) \to \phi_a(U_a \cap U_b)$为$\mathbb{R}^m$中的同胚映射，因此$\phi_a \circ \phi_b^{-1} \in \mathcal{C}^0$的。

$\mathcal{C}^r$ map $F : N \to M$ is **locally invertible** or a **local diffeomorphism** at $p \in N$ if $p$ has a open neighborhood $U$ on which $F| U : U \to F(U)$ is a diffeomorphism.

注意：$\mathcal{C}^r$映射并没有要求$F$为双射，locally invertible(local diffeomorphism)要求$F$在局部是双射，且$F^{-1}$在局部是$\mathcal{C}^r$映射。

后文中若没有额外说明，则默认$r=\infty$。

## 性质

1. 如果两个 chart $(V,\psi)$ 和 $(W,\sigma)$ 都与某个 atlas $\{(U_\alpha, \phi_\alpha)\}$ 相容，那么它们彼此也相容。
2. 存在一个包含 atlas $\mathcal{A}$的极大 atlas$\mathcal{A}'$
3. 设$f:M\to \mathbb{R}^n$，$M$为光滑流形，则以下三个命题等价
   (a) $f$是光滑函数
   (b) 光滑流形上存在一个图册$\mathcal{A}$,使得对于其中的每一个 chart$(U,\phi)$，都有$f \circ \phi^{-1}:\phi(U) \to \mathbb{R}^n \in \mathcal{C}^\infty$
   (c) 光滑流形上的(极大图册中的)每一个 chart $(U,\phi)$，都有$f \circ \phi^{-1}:\phi(U) \to \mathbb{R}^n \in \mathcal{C}^\infty$
4. 设$(U_a,\phi_a)$和$(U_b,\phi_b)$是$M$上的两个 chart，$U_a \cap U_b$为$M$中的开集，$\phi_a(U_a \cap U_b)$和$\phi_b(U_a \cap U_b)$为$\mathbb{R}^m$中的开集。因为连续映射在子空间上也是连续映射，$U_a \cap U_b$是$U_a$和$U_b$中的相对开集，因此$\phi_a(U_a \cap U_b)$和$\phi_b(U_a \cap U_b)$分别为$\phi_a(U_a)$和$\phi_b(U_b)$中的相对开集，又因为$\phi(U_a),\phi(U_b)$是$\mathbb{R}^m$中的开集，开子空间中的开集为原空间中开集。
5. Suppose $F: N \to M$ is $C^\infty$ at $p \in N$. If $(U,\phi)$ is any chart (in maximal atlas) about $p$ in $N$ and $(V,\psi)$ is any chart about $F(p)$ in $M$, then $\psi \circ F \circ \phi^{-1}$ is $C^\infty$ at $\phi(p)$.即光滑映射与 chart 的选择无关
6. If $F: N \to M$ and $G: M \to P$ are $C^\infty$ maps of manifolds, then the composite $G \circ F: N \to P$ is $C^\infty$.
7. Let $N$ and $M$ be smooth manifolds, and $F : N \to M$ a continuous map. The following are equivalent:
   (i) The map $F : N \to M$ is $\mathcal{C}^\infty$.
   (ii) There are atlases $\mathfrak{U}$ for $N$ and $\mathfrak{V}$ for $M$ such that for every chart $(U,\phi)$ in $\mathfrak{U}$ and $(V,\psi)$ in $\mathfrak{V}$, the map $\psi \circ F \circ \phi^{-1} : \phi(U \cap F^{-1}(V)) \to \mathbb{R}^m$ is $\mathcal{C}^\infty$.
   (iii) For every chart(in maximal atlas) $(U,\phi)$ on $N$ and $(V,\psi)$ on $M$, the map $\psi \circ F \circ \phi^{-1} : \phi(U \cap F^{-1}(V)) \to \mathbb{R}^m$ is $\mathcal{C}^\infty$.
8. If $(U, \phi )$ is a chart on a manifold $M$ of dimension $n$, then the coordinate map $\phi : U \to \phi (U) \subset \mathbb{R}^n$ is a diffeomorphism.
9. Let $U$ be an open subset of a manifold $M$ of dimension $n$. If $F : U \to F(U) \subset \mathbb{R}^n$ is a diffeomorphism onto an open subset of $\mathbb{R}^n$, then $(U, F)$ is a chart in the differentiable structure of $M$.
10. Theorem (Inverse function theorem for manifolds). Let $F : N \to M$ be a $\mathcal{C}^\infty$ map between two manifolds of the same dimension, and $p \in N$. Suppose for some charts $(U,\phi)=(U,x^1,\cdots,x^n)$ about $p$ in $N$ and $(V,\psi)=(V,y^1,\cdots,y^n)$ about $F(p)$ in $M$, $F(U) \subset V$. Set $F^i=y^i \circ F$. Then $F$ is locally invertible at $p$ if and only if its Jacobian determinant $\det[\partial F^i/\partial x^j(p)]$ is nonzero.

## Example

#### 流形

- $M=\{(x,x^2)\mid x \in \mathbb{R}\}$ 是一维流形

Hausdorff:M 是 $\mathbb{R}^2$ 的子空间，$\mathbb{R}^2$ 是 Hausdorff 空间，Hausdorff 空间的子空间是 Hausdorff 空间，因此 M 是 Hausdorff 空间。
Second countable:M 是 $\mathbb{R}^2$ 的子空间，$\mathbb{R}^2$ 是第二可数空间，第二可数空间的子空间是第二可数空间，因此 M 是第二可数空间。
Locally Euclidean: $\phi:M \to \mathbb{R}^2,\phi(x,x^2)=x$,是同胚映射，连续函数在子空间仍是连续函数，因此$\{(U_x,\phi)\mid x \in \mathbb{R}\}$是 $M$上的 $\mathcal{C}^0$的图册

- $M=\{(x,y)\mid x^2+y^2<r,x \in \mathbb{R},y \in \mathbb{R},r \in \mathbb{R}\}$ 是二维流形

Hausdorff 和 Second countable:继承自$\mathbb{R}^2$
Locally Euclidean: $\phi:M \to \mathbb{R}^2,\phi(x,y)=(x,y)$,是同胚映射，因此$\{(U_x,\phi)\mid x \in \mathbb{R}\}$是 $M$上的 $\mathcal{C}^0$的图册

易得$\mathbb{R}^n$中的开集都是局部欧几里得空间，特别地，$\mathbb{R}^n$也是$\mathbb{R}^n$的子空间，因此$\mathbb{R}^n$也是局部欧几里得空间。即$\mathbb{R}^n$及其子空间都是流形，atlas 取 $\{(U,\mathbb{1}_U)\}$。

因为恒等映射是光滑映射，所以$\mathbb{R}^n$中的开集是光滑流形。

#### 光滑映射

- 恒等映射$I:R^n \to R^n \in \mathcal{C}^\infty$, 特别地，恒等映射为连续映射
