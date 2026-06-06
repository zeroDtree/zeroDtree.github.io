---
title: derivative
---

## Prerequisites

- [[抽象代数/向量空间]]

## Multivariate complex vector-valued functions

- Complex vector space: $<\mathbb{C}, \mathbb{C}^n>$

Complex vector space can define inner product, which can induce norm, which can induce metric, which can induce topology.

- Multivariate complex-valued function $f: \mathbb{C}^n \rightarrow \mathbb{C}$

- Multivariate complex vector-valued function $f: \mathbb{C}^n \rightarrow \mathbb{C}^m$

**adherent point** Let $X$ be a topological space, $E$ be a subset of $X$, $x$ be a point of $X$. If every neighborhood $N_x$ of $x$ has $N_x \cap E \neq \emptyset$, then $x$ is called an adherent point of $E$. Equivalently, $x \in \overline{E}$ ($\overline{E}$ is the closure of $E$).

**limit point** Let $X$ be a topological space, $E$ be a subset of $X$, $x$ be a point of $X$. If every neighborhood $N_x$ of $x$ has $N_x \cap E \backslash \{x\} \neq \emptyset$, then $x$ is called a limit point of $E$.

limit point is also an adherent point.

## Derivative

**Differentiability at a point** Let $X$ be a subset of $\mathbb{C}^n$, and let $x_0 \in X$ be an element of $X$ which is also a limit point of $X$. Let $f: X \rightarrow \mathbb{C}^m$ be a function. Let $L$ be a linear transformation from $\mathbb{C}^n$ to $\mathbb{C}^m$. We say that $f$ is **differentiable at** $x_0$ on $X$ with **derivative** $L$ and write $f'(x_0) := L$ if

$$
\lim_{x \to x_0, x \in X \setminus \{x_0\}} \frac{d(f(x), f(x_0) + L(x - x_0))}{d(x, x_0)} = 0
$$

**Uniqueness of derivatives** Let $E$ be a subset of $\mathbb{C}^n$, $f: E \rightarrow \mathbb{C}^m$ be a function, $x_0 \in E$ be an interior point of $E$, and let $L_1: \mathbb{C}^n \rightarrow \mathbb{C}^m$ and $L_2: \mathbb{C}^n \rightarrow \mathbb{C}^m$ be linear transformations. Suppose that $f$ is differentiable at $x_0$ with derivative $L_1$, and also differentiable at $x_0$ with derivative $L_2$. Then $L_1 = L_2$.

> proof:
> because $L_1 \not= L_2$, so there exists $v \in \mathbb{C}^n \wedge v \not= 0$, s.t. $L_1(v) \not= L_2(v)$.
> $R_1(t) := f(x_0 + tv) - f(x_0) - L_1(tv)$.
> $R_2(t) := f(x_0 + tv) - f(x_0) - L_2(tv)$.
> $t(L_1(v) + L_2(v)) = L_1(tv) - L_2(tv) = R_2(t) - R_1(t)$.
> $\frac{||(L_1(v) - L_2(v))||}{||v||} = \frac{||t(L_1(v) - L_2(v))||}{||tv||} = \frac{||R_2(t) - R_1(t)||}{||tv||} \leq \frac{||R_2(t)||}{||tv||} + \frac{||R_1(t)||}{||tv||}$.
> so $L_1(v) - L_2(v) = 0$, contradiction.
