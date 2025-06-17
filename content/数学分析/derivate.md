---
title: derivative
---

## Prerequisites

- [[抽象代数/向量空间]]
- [[数学分析/funct-limit]]

## Definitions

- real vector space: $<\mathbb{R}, \mathbb{R}^n>$

real vector space can define inner product, which can induce norm, which can induce metric, which can induce topology.

- Multivariate real-valued function $f: \mathbb{R}^n \rightarrow \mathbb{R}$

- Multivariate real vector-valued function $f: \mathbb{R}^n \rightarrow \mathbb{R}^m$

- **Differentiability at a point** Let $X$ be a subset of $\mathbb{R}^n$, and let $x_0 \in X$ be an element of $X$ which is also a limit point of $X$. Let $f: X \rightarrow \mathbb{R}^m$ be a function. Let $L$ be a linear transformation from $\mathbb{R}^n$ to $\mathbb{R}^m$. We say that $f$ is **differentiable at** $x_0$ on $X$ with **derivative** $L$ and write $f'(x_0) := L$ if

  $$
  \lim_{x \to x_0, x \in X \setminus \{x_0\}} \frac{d(f(x), f(x_0) + L(x - x_0))}{d(x, x_0)} = 0
  $$

**Uniqueness of derivatives** Let $E$ be a subset of $\mathbb{R}^n$, $f: E \rightarrow \mathbb{R}^m$ be a function, $x_0 \in E$ be an interior point of $E$, and let $L_1: \mathbb{R}^n \rightarrow \mathbb{R}^m$ and $L_2: \mathbb{R}^n \rightarrow \mathbb{R}^m$ be linear transformations. Suppose that $f$ is differentiable at $x_0$ with derivative $L_1$, and also differentiable at $x_0$ with derivative $L_2$. Then $L_1 = L_2$.

> proof:
> because $L_1 \not= L_2$, so there exists $v \in \mathbb{R}^n \wedge v \not= 0$, s.t. $L_1(v) \not= L_2(v)$.
> $R_1(t) := f(x_0 + tv) - f(x_0) - L_1(tv)$.
> $R_2(t) := f(x_0 + tv) - f(x_0) - L_2(tv)$.
> $t(L_1(v) + L_2(v)) = L_1(tv) - L_2(tv) = R_2(t) - R_1(t)$.
> $\frac{||(L_1(v) - L_2(v))||}{||v||} = \frac{||t(L_1(v) - L_2(v))||}{||tv||} = \frac{||R_2(t) - R_1(t)||}{||tv||} \leq \frac{||R_2(t)||}{||tv||} + \frac{||R_1(t)||}{||tv||}$.
> so $L_1(v) - L_2(v) = 0$, contradiction.

## Properties

1. Suppose $f$ and $g$ are defined on $[a, b]$ and are differentiable at a point $x \in [a, b]$. Then $f+g$, $f \cdot g$, and $\frac{f}{g}$ are differentiable at $x$, and
   1. $(f+g)'(x) = f'(x) + g'(x)$
   2. $(fg)'(x) = f'(x)g(x) + f(x)g'(x)$
   3. $\left(\frac{f}{g}\right)'(x) = \frac{g(x)f'(x) - g'(x)f(x)}{g^2(x)}$
2. Let $f: \mathbb{R}^n \rightarrow \mathbb{R}^m$ be a function, and $f$ is differentiable at $x_0$ on $X$. $g: \mathbb{R}^m \rightarrow \mathbb{R}^k$ be a function, and $g$ is differentiable at $f(x_0)$ on $f(X)$. Then $g \circ f$ is differentiable at $x_0$ on $X$, and $(g \circ f)'(x_0) = g'(f(x_0)) \circ f'(x_0)$.