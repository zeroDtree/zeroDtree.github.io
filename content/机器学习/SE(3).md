---
title: SE(3)
---

## Invariance and Equivariance

### Invariance

Let $A=\{f\mid \text{ f is a function from X to X}\}$ be a set of functions.

$g:X\to Y$ is invariant under $A$ if $g(x)=g(f(x))$ for all $f\in A$ and $x\in X$, denoted as $g\in \text{A-Invariant}$.

### Equivariance

Let $A=\{f\mid \text{ f is a function from X to X}\}$ be a set of functions.

$g:X\to X$ is equivariant under $A$ if $g(f(x))=f(g(x))$ for all $f\in A$ and $x\in X$, denoted as $g\in \text{A-Equivariant}$.

## Group in $\mathbb{R}^3$

- $GL(3) = \{M \in \mathbb{R}^{3 \times 3} \mid M \text{ is invertible}\}$
- $O(3) = \{M \in \mathbb{R}^{3 \times 3} \mid MM^T = M^T M = I\}$
- $SO(3) = \{M \in \mathbb{R}^{3 \times 3} \mid MM^T = M^T M = I \wedge \det(M) = 1\}$

> $SO(3) < O(3) < GL(3)$

- $SE(3) = \{f \mid f(x) = Rx + t \wedge R \in SO(3) \wedge t \in \mathbb{R}^3\}$

> $SO(3) < SE(3)$

### SE(3)-Equivariance

- A function $g$ is SE(3)-equivariant if and only if for any $f \in SE(3)$,
  $g \circ f(x) = f \circ g(x)$

> **Property**: The composition of two SE(3)-equivariant functions is also SE(3)-equivariant.

### Common SO(3)-Invariant functions

#### Norm in $\mathbb{R}^n$

$$
f(x) = \|x\| = \langle x, x \rangle = (x^T U^T)(U x) = x^T x
$$
