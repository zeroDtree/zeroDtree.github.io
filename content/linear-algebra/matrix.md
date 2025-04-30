---
title: Matrix
---

- [1. Matrix](#1-matrix)
- [2. Matrix Addition](#2-matrix-addition)
- [3. Scalar Multiplication](#3-scalar-multiplication)
- [4. Matrix Multiplication](#4-matrix-multiplication)
	- [4.1. Properties of Matrix Multiplication](#41-properties-of-matrix-multiplication)
		- [4.1.1. Associativity](#411-associativity)
		- [4.1.2. Distributivity](#412-distributivity)
		- [4.1.3. Square Matrix](#413-square-matrix)
- [5. Transpose](#5-transpose)
- [6. Conjugate](#6-conjugate)
- [7. Hermitian](#7-hermitian)
- [8. Block Matrix Multiplication](#8-block-matrix-multiplication)
- [9. Trace](#9-trace)
- [10. Inner Product](#10-inner-product)
- [11. Determinant](#11-determinant)
	- [11.1. Alternating multilinear map](#111-alternating-multilinear-map)
	- [11.2. Laplace expansion](#112-laplace-expansion)
- [12. Adjugate matrix](#12-adjugate-matrix)

Let $F$ be a field(e.g. $F=\mathbb{Q},F=\mathbb{R}$ or $F=\mathbb{C}$)

$0_{F}$ is the addtive unit element of $F$.

$1_{F}$ is the multiply unit element of $F$.

We will use $0$ and $1$ to denote $0_{F}$ and $1_{F}$ respectively if there is no confusion about the field $F$.

## 1. Matrix

A matrix is a rectangular array of elements from a field $F$.

$$
A = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}
$$

The element $a_{ij}$ is called the $(i,j)$-th entry of $A$.

$F^{m \times n}$ is the set of all $m \times n$ matrices with entries in $F$.

## 2. Matrix Addition

Let $A = [a_{ij}]$ and $B = [b_{ij}]$ be two matrices of the same size. The sum of $A$ and $B$ is the matrix $C = [c_{ij}]$ defined by $c_{ij} = a_{ij} + b_{ij}$.

It is easy to see that $\langle F^{m \times n}, + \rangle$ is an commutative group.

## 3. Scalar Multiplication

Let $A = [a_{ij}]$ be a matrix and $c\in F$ be a scalar. The product of $A$ and $c$ is the matrix $C = [c_{ij}]$ defined by $c_{ij} = c a_{ij}$.

It is easy to see that $\langle F^{m \times n}, +, \cdot \rangle$ is a vector space over $F$.

## 4. Matrix Multiplication

Let $A = [a_{ij}]\in F^{m \times n}$ and $B = [b_{ij}]\in F^{n \times p}$ be two matrices. The product of $A$ and $B$ is the matrix $C = [c_{ij}]\in F^{m \times p}$ defined by $c_{ij} = \sum_{k=1}^n a_{ik} b_{kj}$.

### 4.1. Properties of Matrix Multiplication

#### 4.1.1. Associativity

Let $A = [a_{ij}]\in F^{m \times n}$, $B = [b_{ij}]\in F^{n \times p}$, $C = [c_{ij}]\in F^{p \times q}$ be three matrices.

$$
(AB)C = A(BC)
$$

> proof
>
> $$
> \begin{aligned}
> ((AB)C)_{ij} &= \sum_{k=1}^p (AB)_{ik} c_{kj} \\
> & = \sum_{k=1}^p (\sum_{l=1}^n a_{il} b_{lk}) c_{kj} \\
> & = \sum_{k=1}^p \sum_{l=1}^n a_{il} b_{lk} c_{kj} \\
> \end{aligned}
> $$
>
> $$
> \begin{aligned}
> A(BC)_{ij} &= \sum_{l=1}^n a_{il} (BC)_{lj} \\
> & = \sum_{l=1}^n a_{il} \sum_{k=1}^p b_{lk} c_{kj} \\
> & = \sum_{l=1}^n \sum_{k=1}^p a_{il} b_{lk} c_{kj} \\
> & = \sum_{k=1}^p \sum_{l=1}^n a_{il} b_{lk} c_{kj} \\
> & = ((AB)C)_{ij}
> \end{aligned}
> $$

#### 4.1.2. Distributivity

$$
A(B + C) = AB + AC
$$

> proof
>
> $$
> \begin{aligned}
> (A(B + C))_{ij} &= \sum_{k=1}^n a_{ik} (B + C)_{kj} \\
> & = \sum_{k=1}^n a_{ik} (b_{kj} + c_{kj}) \\
> & = \sum_{k=1}^n a_{ik} b_{kj} + \sum_{k=1}^n a_{ik} c_{kj} \\
> & = (AB)_{ij} + (AC)_{ij} \\
> & = (AB + AC)_{ij}
> \end{aligned}
> $$

#### 4.1.3. Square Matrix

A matrix $A$ is called a square matrix if $m = n$.

**Identity Matrix**

The $n \times n$ identity matrix $I_n$ is the matrix with $1_{F}$ on the diagonal and $0_{F}$ elsewhere.

$$
I_n = \begin{bmatrix}
1_{F} & 0_{F} & \cdots & 0_{F} \\
0_{F} & 1_{F} & \cdots & 0_{F} \\
\vdots & \vdots & \ddots & \vdots \\
0_{F} & 0_{F} & \cdots & 1_{F}
\end{bmatrix}
$$

$I$ is the identity element of $\langle F^{n \times n}, \cdot \rangle$.

$$
AI = IA = A
$$

> proof
>
> $$
> \begin{aligned}
> (AI)_{ij} &= \sum_{k=1}^n a_{ik} (I)_{kj} \\
> & = \sum_{k=1}^n a_{ik} \delta_{kj} \\
> & = a_{ij}
> \end{aligned}
> $$
>
> similar, we have $IA = A$.

$\langle F^{n \times n}, +, \cdot \rangle$ is a ring with identity.

because all the units in a ring form a group under multiplication(this group is called the group of units of the ring), the group of units of $\langle F^{n \times n}, +, \cdot \rangle$ is denoted by $\langle GL(n,F), \cdot \rangle$ or $GL(n,F)$ or $GL_n(F)$.

$GL(n,F)$ is called the general linear group of degree $n$ over $F$.

## 5. Transpose

Let $A = [a_{ij}]\in F^{m \times n}$ be a matrix. The transpose of $A$ is the matrix $A^T = [a_{ji}]\in F^{n \times m}$ defined by $a_{ji} = a_{ij}$.

$A \in F^{m \times n}, B \in F^{n \times p}$, we have:
$(AB)^T = B^T A^T$

> proof
>
> $$
> \begin{aligned}
> (AB)^T_{ij} &= (AB)_{ji} \\
> &= \sum_{k=1}^n a_{jk} b_{ki} \\
> &= \sum_{k=1}^n (A^T)_{kj} (B^T)_{ik} \\
> &= (B^T A^T)_{ij}
> \end{aligned}
> $$

## 6. Conjugate

**If $F$ is a subfield of** $\mathbb{C}$, the conjugate of $a\in F$ is $\overline{a}\in F$.

Let $A = [a_{ij}]\in F^{m \times n}$ be a matrix. The conjugate of $A$ is the matrix $\overline{A} = [\overline{a_{ij}}]\in F^{m \times n}$

- $A,B \in F^{m \times n}$, $\overline{A + B} = \overline{A} + \overline{B}$

- $A \in F^{m \times n}, B \in F^{n \times p}$, $\overline{A \cdot B} = \overline{A} \cdot \overline{B}$

## 7. Hermitian

**If $F$ is a subfield of** $\mathbb{C}$

Let $A = [a_{ij}]\in F^{m \times n}$ be a matrix. The Hermitian of $A$ is the matrix $A^H = [\overline{a_{ji}}]\in F^{n \times m}$ defined by $a_{ji} = \overline{a_{ij}}$.

## 8. Block Matrix Multiplication

let $A$ be a $m \times n$ matrix, $B$ be a $n \times p$ matrix, divide $A$ and $B$ into blocks:

$$
A = \begin{bmatrix}
A_{11} & A_{12} & \cdots & A_{1s} \\
A_{21} & A_{22} & \cdots & A_{2s} \\
\vdots & \vdots & \ddots & \vdots \\
A_{r1} & A_{r2} & \cdots & A_{rs}
\end{bmatrix}, \quad
B = \begin{bmatrix}
B_{11} & B_{12} & \cdots & B_{1t} \\
B_{21} & B_{22} & \cdots & B_{2t} \\
\vdots & \vdots & \ddots & \vdots \\
B_{s1} & B_{s2} & \cdots & B_{st}
\end{bmatrix}
$$

where $A_{ij}$ is a $m_i \times n_j$ matrix, $B_{jk}$ is a $n_j \times p_k$ matrix, and satisfies:

- $\sum_{i=1}^r m_i = m$
- $\sum_{j=1}^s n_j = n$
- $\sum_{k=1}^t p_k = p$

then $C = AB$ can be represented as:

$$
C = \begin{bmatrix}
C_{11} & C_{12} & \cdots & C_{1t} \\
C_{21} & C_{22} & \cdots & C_{2t} \\
\vdots & \vdots & \ddots & \vdots \\
C_{r1} & C_{r2} & \cdots & C_{rt}
\end{bmatrix}
$$

where $C_{ik} = \sum_{j=1}^s A_{ij}B_{jk}$, and $C_{ik}$ is a $m_i \times p_k$ matrix.

## 9. Trace

Let $A = [a_{ij}]\in F^{n \times n}$ be a square matrix. The trace of $A$ is the sum of the diagonal elements of $A$, denoted by $tr(A)$.

$$
tr(A) = \sum_{i=1}^n a_{ii}
$$

**Properties of Trace**

- $tr(A + B) = tr(A) + tr(B)$
- $tr(cA) = ctr(A)$
- $tr(AB) = tr(BA)$
- $\overline{tr(A)} = tr(\overline{A})$
- $tr(A^T) = tr(A)$

> proof : $tr(AB) = tr(BA)$
>
> $$
> \begin{aligned}
> tr(AB) &= \sum_{i=1}^n (AB)_{ii} \\
> &= \sum_{i=1}^n \sum_{j=1}^n a_{ij} b_{ji} \\
> &= \sum_{j=1}^n \sum_{i=1}^n b_{ji} a_{ij} \\
> &= tr(BA)
> \end{aligned}
> $$

## 10. Inner Product

Recall that $\langle F^{m \times n}, +, \cdot \rangle$ is a vector space over $F$.

**If $F$ is a subfield of** $\mathbb{C}$, we can define an inner product on $F^{m \times n}$ as follows:

$$
\langle A, B \rangle = tr(A^H B)
$$

It is easy to verify that $\langle A, B \rangle$ satisfies the following properties:

- conjugate symmetry: $\langle A, B \rangle = \overline{\langle B, A \rangle}$
- right linearity: $\langle A, bB + cC \rangle = b\langle A, B \rangle + c\langle A, C \rangle$
- positive-definiteness: $\langle A, A \rangle \geq 0$, $\langle A, A \rangle = 0$ if and only if $A = 0$

> proof: $\langle A, B \rangle = \overline{\langle B, A \rangle}$
>
> $$
> \begin{aligned}
> \langle A, B \rangle &= tr(A^H B) \\
> &= \overline{\overline{tr(A^H B)}} \\
> &= \overline{tr(A^T \overline{B})} \\
> &= \overline{tr(B^H A)} \\
> &= \overline{\langle B, A \rangle}
> \end{aligned}
> $$

> proof: $\langle A, bB + cC \rangle = b\langle A, B \rangle + c\langle A, C \rangle$
>
> $$
> \begin{aligned}
> \langle A, bB + cC \rangle &= tr(A^H (bB + cC)) \\
> &= tr(bB^H A + cC^H A) \\
> &= btr(B^H A) + ctr(C^H A) \\
> &= b\langle A, B \rangle + c\langle A, C \rangle
> \end{aligned}
> $$

> proof: $\langle A, A \rangle \geq 0$
>
> $$
> \begin{aligned}
> \langle A, A \rangle &= tr(A^H A) \\
> &= \sum_{i=1}^n \sum_{j=1}^n a_{ij} \overline{a_{ij}} \\
> &= \sum_{i=1}^n |a_{ii}|^2 \\
> &\geq 0
> \end{aligned}
> $$
>
> It is easy to see that $\langle A, A \rangle = 0$ if and only if $A = 0$.

## 11. Determinant

### 11.1. Alternating multilinear map

let $\langle F, V \rangle$ be a vector space over $F$. A map $f: V^n \to F$ is called an alternating multilinear map if:

- multilinear: $f$ is linear in each variable
- alternating: $f(v_1, \cdots, v_i, \cdots, v_j, \cdots, v_n) = -f(v_1, \cdots, v_j, \cdots, v_i, \cdots, v_n)$ for any $v_i, v_j \in V$

Let $A = [a_{ij}]\in F^{n \times n}$ be a square matrix. The determinant of $A$ is the scalar $\det(A)$ defined by:

$$
|A| := \det(A) = \sum_{\sigma \in S_n} \text{sgn}(\sigma) \prod_{i=1}^n a_{i, \sigma(i)}
$$

or equivalently,

$$
|A| = \sum_{j_1,j_2,\cdots,j_n \in [n]} \tau(j_1,j_2,\cdots,j_n) \prod_{i=1}^n a_{i,j_i}
$$

where $S_n$ is the symmetric group of degree $n$, $\text{sgn}(\sigma)$ is the sign of the permutation $\sigma$, and $a_{i, \sigma(i)}$ is the element of $A$ at the $i$-th row and $\sigma(i)$-th column.

$$
\text{sgn}(\sigma) = \begin{cases}
1_{F} & \text{if } \sigma \text{ is an even permutation} \\
-1_{F} & \text{if } \sigma \text{ is an odd permutation}
\end{cases}
$$

$\tau(j_1,j_2,\cdots,j_n)$ is the number of inverse pairs of the sequence $(j_1,j_2,\cdots,j_n)$.

It is not difficult to see that:

$$
\text{sgn}(\sigma) = (-1)^{\tau(j_1,j_2,\cdots,j_n)}
$$

- Determinant is a multilinear map for each row of $A$
- Determinant does not change under transposition, i.e. $\det(A) = \det(A^T)$
- Determinant is a multilinear map for each column of $A$
- Determinant is an alternating multilinear map for both each row of $A$ and each column of $A$
- $\det(A) = \sum_{j_1,j_2,\cdots,j_n \in [n]} (-1)^{\tau(i_1,i_2,\cdots,i_n) + \tau(j_1,j_2,\cdots,j_n) } \prod_{k=1}^n a_{i_k,j_k}$

### 11.2. Laplace expansion

$I = {i_1, i_2, \cdots, i_k}$
$I' = [n] \setminus I$

$J = {j_1, j_2, \cdots, j_k}$
$J' = [n] \setminus J$

$\sum(X):= \sum_{x \in X} x$

$A_{I,J}$ is the submatrix of $A$ obtained by deleting the $i$-th $\in I'$ row and $j$-th $\in J'$ column.

$$
\det(A) = \sum_{J \subseteq [n] \wedge |J| = k} (-1)^{\sum(I) + \sum(J)} \det(A_{I,J}) \det(A_{I',J'})
$$

- $\det(AB) = \det(A) \det(B)$

## 12. Adjugate matrix

$A_{ij}$ is the submatrix of $A$ obtained by deleting the $i$-th row and $j$-th column.

Let $A = [a_{ij}]\in F^{n \times n}$ be a square matrix. The adjugate of $A$ is the matrix $A^{\#}:=adj(A) = [a^{\#}_{ij}]\in F^{n \times n}$ defined by $a^{\#}_{ij} = (-1)^{i+j} \det(A_{ji})$.

$$
A A^{\#} = A^{\#} A = \det(A) I
$$

> proof
>
> $$
> \begin{aligned}
> (A A^{\#})_{ij} &= \sum_{k=1}^n a_{ik} a^{\#}_{kj} \\
> &= \sum_{k=1}^n a_{ik} (-1)^{k+j} \det(A_{jk}) \\
> &= \det(A) \delta_{ij}
> \end{aligned}
> $$

- $A$ is invertible if and only if $\det(A) \not= 0$
- if $A$ is invertible, then $A^{-1} = \frac{1_F}{\det(A)} A^{\#}$
