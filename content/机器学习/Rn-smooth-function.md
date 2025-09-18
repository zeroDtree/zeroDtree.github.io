---
title: Smooth functions on Euclidean space
---

## Definition

Let $k$ be a nonnegative integer. $U\subseteq \mathbb{R}^n$ is an open set. A real-valued function $f: U \to \mathbb{R}$ is said to be $\mathcal{C}^k$ at $\mathbf{p} \in U$ if its partial derivatives

$$
	\frac{\partial^j f}{\partial x^{i_1} \cdots \partial x^{i_j}}(\mathbf{p})
$$

of all orders $j \leq k$ exist and are continuous at $\mathbf{p}$. The function $f: U \to \mathbb{R}$ is $\mathcal{C}^\infty$ at $\mathbf{p}$ if it is $\mathcal{C}^k$ for all $k \geq 0$;

A vector-valued function $f: U \to \mathbb{R}^m$ is said to be $\mathcal{C}^k$ at $\mathbf{p}$ if all of its component functions $f^1,\ldots,f^m$ are $\mathcal{C}^k$ at $\mathbf{p}$.

We say that $f: U \to \mathbb{R}^m$ is $\mathcal{C}^k$ on $U$ if it is $\mathcal{C}^k$ at every point in $U$. A similar definition holds for a $\mathcal{C}^\infty$ function on an open set $U$. We treat the terms $\mathcal{C}^\infty$ and smooth as synonymous.

A neighborhood of a point in $\mathbb{R}^n$ is an open set containing the point. The function $f$ is real-analytic at $\mathbf{p}$ if in some neighborhood of $\mathbf{p}$ it is equal to its Taylor series at $\mathbf{p}$:

$$
\begin{align*}
f(\mathbf{x}) = f(\mathbf{p}) &+ \sum_i \frac{\partial f}{\partial x^i}(\mathbf{p})(x^i - p^i) \\
&+ \frac{1}{2!} \sum_{i,j} \frac{\partial^2 f}{\partial x^i \partial x^j}(\mathbf{p})(x^i - p^i)(x^j - p^j) \\
&+ \cdots + \frac{1}{k!} \sum_{i_1, \ldots, i_k} \frac{\partial^k f}{\partial x^{i_1} \cdots \partial x^{i_k}}(\mathbf{p})(x^{i_1} - p^{i_1}) \cdots (x^{i_k} - p^{i_k}) + \cdots
\end{align*}
$$

i.e. If $S_k$ represents symmetric group of $[k]$, then:

$$
f(\mathbf{x}) = \sum_{k=0}^{\infty} \sum_{i_1i_2\cdots i_k \in S_k} \frac{1}{k!} \frac{\partial^k f}{\partial x^{i_1} \cdots \partial x^{i_k}}(\mathbf{p})(x^{i_1} - p^{i_1}) \cdots (x^{i_k} - p^{i_k})
$$

## Properties

1. A real-analytic function is necessarily $C^{\infty}$ , because a convergent power series can be differentiated term by term in its region of convergence
