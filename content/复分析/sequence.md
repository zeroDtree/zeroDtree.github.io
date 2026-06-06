---
title: sequence of complex numbers
---

## Definition

If there no extra statement, we assume that $a_n \in \mathbb{C}$

- A **sequence** of complex numbers is a function from $\mathbb{Z}_{\geq m}$ to $\mathbb{C}$, denoted as $(a_n)_{n\geq m}$

- $(a_n)_{n\geq m}$ **converges** to $L \in \mathbb{C}$, we write $a_n \to L$ iff $\forall \epsilon > 0, \exists N \in \mathbb{Z}_{\geq m}, \forall n \geq N, d(a_n - L) < \epsilon$, L is called the limit of the sequence

- $(a_n)_{n\geq m}$ is a **Cauchy sequence** iff $\forall \epsilon > 0, \exists N \in \mathbb{Z}_{\geq m}, \forall n,m \geq N, d(a_n - a_m) < \epsilon$

- $L \in \overline{\mathbb{R}}$ is a **limit point** of $(a_n)_{n\geq m}$ iff $\forall \epsilon > 0, \exists N \in \mathbb{Z}_{\geq m}, \exists n \geq N, d(a_n - L) < \epsilon$

## Properties

- The limit of a sequence is unique, because $\mathbb{C}$ is a metric space,thus a Hausdorff space, so the limit of a sequence is unique
- if $(a_n)_{n \geq m}$ converges to $x$ $\Longleftrightarrow$ $\forall k \in \mathbb{Z}_{\geq m}$, $(a_n)_{n \geq k}$ converges to $x$
- if $a_n,b_n$ converges to $x,y$ respectively, then the following statements are true
  - $a_n + b_n$ converges to $x+y$
  - $a_n b_n$ converges to $xy$
  - if $y \neq 0 \wedge b_n \neq 0$, then $\frac{1}{b_n}$ converges to $\frac{1}{y}$
  - if $y \neq 0 \wedge b_n \neq 0$, then $\frac{a_n}{b_n}$ converges to $\frac{x}{y}$
- A convergent sequence has only one limit point, which is the limit of the sequence
- $a_n \to 0$ $\Longleftrightarrow$ $|a_n| \to 0$
- $a_n + i b_n \to x + i y$ $\Longleftrightarrow$ $a_n \to x \wedge b_n \to y$
