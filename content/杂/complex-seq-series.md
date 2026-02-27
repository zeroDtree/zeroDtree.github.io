---
title: sequence, series, function
---

## Prerequisites

- [[数学分析/metric-space]]
- [[点集拓扑/拓扑空间]]
-
- [[数学分析/series]]

## Definition

If there is no additional explanation and the sequence is not in a field, it is assumed that the sequence is in the metric space.
If there is an operation on a field, it is assumed that the sequence is in $\mathbb{C}$.

$\forall x \in X, \forall r>0, B(x, r):=\{y \in X: d(x, y) < r\}$ is called the **open neighborhood ball**(o.n.b.) of $x$.

$E \subseteq X$ is bounded if there exists $x \in X$ and $r>0$ such that $E \subseteq B(x, r)$.

Let $E$ be a nonempty subset of a metric space $X$, and let $S$ be the set of all real numbers of the form $d(p, q)$, with $p \in E$ and $q \in E$. The sup of $S$ is called the diameter of $E$.

## Properties

1. $\{p_n\}$ be a sequence in a metric space $X$

- $\{p_n\}$ converges to $p \in X$ if and only if every o.n.b. of $p$ contains $p_n$ for all but finitely many $n$.
- If $p \in X$, $p' \in X$, and if $\{p_n\}$ converges to $p$ and to $p'$, then $p' = p$.
- If $\{p_n\}$ converges, then $\{p_n\}$ is bounded.
- If $E \subseteq X$ and if $p$ is a limit point of $E$, then there is a sequence $\{p_n\}$ in $E$ such that $p = \lim_{n \to \infty} p_n$.

2. $\{a_n\}$ and $\{b_n\}$ are complex sequences, if $a_n,b_n$ converges to $x,y$ respectively, then the following statements are true:

- $a_n + b_n$ converges to $x+y$
- $a_n b_n$ converges to $xy$
- if $y \neq 0 \wedge b_n \neq 0$, then $\frac{1}{b_n}$ converges to $\frac{1}{y}$
- if $y \neq 0 \wedge b_n \neq 0$, then $\frac{a_n}{b_n}$ converges to $\frac{x}{y}$
- $a_n \to 0$ $\Longleftrightarrow$ $|a_n| \to 0$
- $a_n + i b_n \to x + i y$ $\Longleftrightarrow$ $a_n \to x \wedge b_n \to y$

3. Every bounded sequence in $\mathbb{R}^k$ contains a convergent subsequence.
4. The subsequential limits of a sequence $\{p_n\}$ in a metric space $X$ form a closed subset of $X$.
5. If $E$ is the closure of a set $E$ in a metric space $X$, then $\text{diam} \overline{E} = \text{diam} E$.
6. If $\{K_n\}$ is a sequence of compact sets in $X$ such that $K_n \supseteq K_{n+1}$ for all $n$, and if $\lim_{n \to \infty} \text{diam} K_n = 0$, then $\bigcap_{n=1}^{\infty} K_n$ consists of exactly one point.
7. Let $\{a_i\}$ be a complex sequence, $\sum a_n$ converges if and only if for every $\epsilon > 0$ there is an integer $N$ such that $\forall m,n, N < m\leq n $, $\sum_{n=m}^{n} |a_n| < \epsilon$. lf $\sum a_n$ converges, then $\lim_{n \to \infty }a_n$ = 0.
8. Let $f$ be monotonically increasing on $(a, b)$. Then $f(x+)$ and $f(x-)$ exist at every point of $x$ of $(a, b)$. More precisely, $\sup_{a<t<x} f(t) =f(x-) \leq f(x) \leq f(x+) = \inf_{x<t<b} f(t)$. Furthermore, if $a < x < y < b$, then $f(x+) \leq f(y-)$.
9. Let $f$ be monotonic on $(a, b)$. Then the set of points of $(a, b)$ at which $f$ is discontinuous is at most countable.
