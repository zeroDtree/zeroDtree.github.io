---
title: Lebesgue 测度
---

## Preliminary

- [[测度论与概率论/L-S-measure]]

## Definitions

Define $d$-ary function $F:\mathbb{R}^d \to \mathbb{R}, F(x_1, x_2,\cdots ,x_d):=x_1x_2\cdots x_d$

It is easy to see that $F$ is an L-S function, which is called Lebesgue function, abbreviated as L function. The L-S measure induced by the $d$-dimensional L function on $\mathcal{B}(\mathbb{R}^d)$ is called Lebesgue measure on $\mathcal{B}(\mathbb{R}^d)$, abbreviated as $L$ measure, denoted as $\lambda$, thus $(\mathbb{R}^d,\mathcal{B}(\mathbb{R}^d),\lambda)$ is a measure space.

$\lambda^*$ is the outer measure in measure extension from semi-ring to sigma algebra.

Let $(\mathbb{R}^d, \overline{\mathcal{B}(\mathbb{R}^d)}, \overline{\lambda})$ be the completion of $(\mathbb{R}^d, \mathcal{B}(\mathbb{R}^d), \lambda)$. $\overline{\mathcal{B}(\mathbb{R}^d)}=\sigma(\mathcal{B}(\mathbb{R}^d)\cup \mathcal{N}_{\lambda})$ is called Lebesgue measurable set, abbreviated as L measurable set.

$A\subseteq \mathbb{R}^d,y \in \mathbb{R}^d, A + y:= \{a + y: a \in A\}$
$A\subseteq \mathbb{R}^d, -A:= \{ -a: a \in A\}$

## Properties

1. $x \in A \iff x+y \in A+y$
2. $x-y \not\in A \iff x \not\in A+y$
3. $x\in A \iff -x \in -A$
4. $x \not\in A \iff -x \not\in -A$
5. $A \cap (B + y) = (A - y) \cap B + y$
6. $A^c + y =  (A + y)^c$
7. $\lambda^*(A+y) = \lambda^*(A)$
8. $\lambda^*(A) = \lambda^*(-A)$
9. $x\in - (A^c) \iff x \in (-A)^c$
10. L measure is invariant under translation, i.e. $\forall A \subseteq \mathbb{R}^d, x\in \mathbb{R}^d$, ($A$ is L measurable $\iff$ $A + y$ is L measurable), and $\lambda(A + y) = \lambda(A)$
11. L measure is invariant under reflection, i.e. $\forall A \subseteq \mathbb{R}^d$, ($A$ is L measurable $\iff$ $-A$ is L measurable)
12. $\exists A \subseteq \mathbb{R}$, s.t. $A$ is not L measurable. For example, Vitali set.
