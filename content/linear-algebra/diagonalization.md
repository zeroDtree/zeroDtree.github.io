---
title: Diagonalization
---

## Prerequisites

- [[linear-algebra/matrix]]

## 1. Diagonalization

$A \in F^{n \times n}$ is a matrix.

$A$ is diagonalizable if there exists an invertible matrix $P$ and a diagonal matrix $D$ such that $A = PDP^{-1}$.

$P=(v_1, v_2, \cdots, v_n) \in F^{n \times n}$

$D = diag(\lambda_1, \lambda_2, \cdots, \lambda_n) \in F^{n \times n}$

$$
A = PDP^{-1} \Longleftrightarrow AP = PD \Longleftrightarrow \forall i \in [n], A v_i = \lambda_i v_i
$$

If $\exists v\not=0$ s.t. $A v = \lambda v$, then $\lambda$ is an eigenvalue of $A$ and $v$ is an eigenvector of $A$ corresponding to $\lambda$.

if $v\not=0$, we have $Av=\lambda v \Longleftrightarrow (A-\lambda I)v=0 \Longleftrightarrow v\in Ker(A-\lambda I)$

$Ker(A-\lambda I)$ is the eigenspace of $A$ corresponding to $\lambda$.

## 2. Characteristic polynomial

$\exists v\not=0, v \in \text{Ker}(A-\lambda I) \Longleftrightarrow \exists v\not=0, (A-\lambda I)v=0 \Longleftrightarrow \det(A-\lambda I) = 0$

$\det(A-\lambda I)$ is a polynomial of $\lambda$ with degree $n$, called the characteristic polynomial of $A$.

The roots of the characteristic polynomial are the eigenvalues of $A$.

If $F$ is algebraically closed, then $A$ will have $n$ eigenvalues in $F$. (Maybe with multiplicity)

Let $d_i = dim(Ker(A-\lambda_i I))$. If $\sum_{i=1}^n d_i = n$, then $A$ is diagonalizable.

## 3. Real symmetric matrix

If $A \in \mathbb{R}^{n \times n}$ is a real symmetric matrix, then $A$ is diagonalizable. Moreover, $A=PDP^T$ where $D$ is a diagonal matrix and $P$ is an orthogonal matrix.
