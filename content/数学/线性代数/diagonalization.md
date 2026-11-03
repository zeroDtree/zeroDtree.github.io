---
title: Diagonalization
tags:
  - 线性代数
---

## Prerequisites

- [[线性代数/rank]]

## 1. Diagonalization

$A \in F^{n \times n}$ is a matrix.

$A$ is diagonalizable if there exists an invertible matrix $P$ and a diagonal matrix $D$ such that $A = PDP^{-1}$.

$P = [v_1\ \cdots\ v_n] \in F^{n \times n}$, where $v_i \in F^n$ for every $i \in [n]$.

$D = \operatorname{diag}(\lambda_1, \lambda_2, \cdots, \lambda_n) \in F^{n \times n}$

$$
A = PDP^{-1} \Longleftrightarrow AP = PD \Longleftrightarrow \forall i \in [n], A v_i = \lambda_i v_i
$$

If $\exists v \neq 0$ s.t. $A v = \lambda v$, then $\lambda$ is an eigenvalue of $A$ and $v$ is an eigenvector of $A$ corresponding to $\lambda$.

For every $v \in F^n$, we have $Av=\lambda v \Longleftrightarrow (A-\lambda I)v=0 \Longleftrightarrow v\in \ker(A-\lambda I)$.

$\ker(A-\lambda I)$ is the eigenspace of $A$ corresponding to $\lambda$.

## 2. Characteristic polynomial

$\exists v \neq 0, v \in \ker(A-\lambda I) \Longleftrightarrow \exists v \neq 0, (A-\lambda I)v=0 \Longleftrightarrow \operatorname{det}(\lambda I-A) = 0$

$\operatorname{det}(\lambda I-A)$ is a polynomial of $\lambda$ with degree $n$, called the characteristic polynomial of $A$.

The roots of the characteristic polynomial are the eigenvalues of $A$.

Let $\lambda_1,\ldots,\lambda_k$ be the distinct eigenvalues of $A$, and let $d_i = \dim\ker(A-\lambda_i I)$ be the geometric multiplicity of $\lambda_i$. Then $A$ is diagonalizable if and only if $\sum_{i=1}^k d_i = n$.

## 3. Real symmetric matrix

By the spectral theorem, every real symmetric matrix $A \in \mathbb{R}^{n \times n}$ is orthogonally diagonalizable: there exist an orthogonal matrix $P$ and a real diagonal matrix $D$ such that $A = PDP^T$.