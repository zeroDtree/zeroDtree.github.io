---
title: Matrix
tags:
  - 线性代数
---

- [1. Prerequisites](#1-prerequisites)
- [2. Matrix](#2-matrix)
- [3. Matrix Addition](#3-matrix-addition)
- [4. Scalar Multiplication](#4-scalar-multiplication)
- [5. Matrix Multiplication](#5-matrix-multiplication)
  - [5.1. Properties of Matrix Multiplication](#51-properties-of-matrix-multiplication)
    - [5.1.1. Associativity](#511-associativity)
    - [5.1.2. Distributivity](#512-distributivity)
    - [5.1.3. Square Matrix](#513-square-matrix)
- [6. Block Matrix Multiplication](#6-block-matrix-multiplication)
- [7. Matrix as a Linear Map](#7-matrix-as-a-linear-map)
- [8. Transpose](#8-transpose)
- [9. Orthogonal matrix](#9-orthogonal-matrix)
- [10. Conjugate](#10-conjugate)
- [11. Hermitian](#11-hermitian)
- [12. Trace](#12-trace)
- [13. Inner Product](#13-inner-product)
  - [13.1. 向量的标准内积](#131-向量的标准内积)
  - [13.2. 矩阵的 Frobenius 内积](#132-矩阵的-frobenius-内积)
- [14. Determinant](#14-determinant)
  - [14.1. Alternating multilinear map](#141-alternating-multilinear-map)
  - [14.2. Laplace expansion](#142-laplace-expansion)
- [15. Adjugate matrix](#15-adjugate-matrix)

## 1. Prerequisites

- [[抽象代数/向量空间]]
- [[抽象代数/群论(置换群)]]

Let $F$ be a field(e.g. $F=\mathbb{Q},F=\mathbb{R}$ or $F=\mathbb{C}$)

$0_{F}$ is the addtive unit element of $F$.

$1_{F}$ is the multiply unit element of $F$.

We will use $0$ and $1$ to denote $0_{F}$ and $1_{F}$ respectively if there is no confusion about the field $F$.

## 2. Matrix

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

## 3. Matrix Addition

Let $A = [a_{ij}]$ and $B = [b_{ij}]$ be two matrices of the same size. The sum of $A$ and $B$ is the matrix $C = [c_{ij}]$ defined by $c_{ij} = a_{ij} + b_{ij}$.

It is easy to see that $\langle F^{m \times n}, + \rangle$ is an commutative group.

## 4. Scalar Multiplication

Let $A = [a_{ij}]$ be a matrix and $c\in F$ be a scalar. The product of $A$ and $c$ is the matrix $C = [c_{ij}]$ defined by $c_{ij} = c a_{ij}$.

It is easy to see that $\langle F^{m \times n}, +, \cdot \rangle$ is a vector space over $F$.

## 5. Matrix Multiplication

Let $A = [a_{ij}]\in F^{m \times n}$ and $B = [b_{ij}]\in F^{n \times p}$ be two matrices. The product of $A$ and $B$ is the matrix $C = [c_{ij}]\in F^{m \times p}$ defined by $c_{ij} = \sum_{k=1}^n a_{ik} b_{kj}$.

### 5.1. Properties of Matrix Multiplication

#### 5.1.1. Associativity

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

#### 5.1.2. Distributivity

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

#### 5.1.3. Square Matrix

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

because all the units in a ring form a group under multiplication(this group is called the group of units of the ring), the group of units of $\langle F^{n \times n}, +, \cdot \rangle$ is denoted by $\langle \mathrm{GL}(n,F), \cdot \rangle$ or $\mathrm{GL}(n,F)$ or $\mathrm{GL}_n(F)$.

$\mathrm{GL}(n,F)$ is called the general linear group of degree $n$ over $F$.

## 6. Block Matrix Multiplication

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

## 7. Matrix as a Linear Map

设

$$
A=[v_1\ \cdots\ v_n]\in F^{m\times n},
\qquad
v_i\in F^m.
$$

对任意 $x=(x_1,\ldots,x_n)^T\in F^n$，矩阵乘法可以写成

$$
Ax=\sum_{i=1}^n x_iv_i.
$$

对任意 $x,y\in F^n$ 和 $a,b\in F$，矩阵乘法的分配律与数乘结合律给出

$$
A(ax+by)=aAx+bAy.
$$

因此矩阵 $A$ 定义了线性映射

$$
T_A:F^n\to F^m,
\qquad
T_A(x)=Ax.
$$

## 8. Transpose

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

## 9. Orthogonal matrix

Let $A \in F^{n \times n}$. $A$ is called an orthogonal matrix if $A^T A = I$. Equivalently, $A \in \mathrm{GL}(n,F)$ and $A^{-1} = A^T$.

## 10. Conjugate

**If $F$ is a subfield of** $\mathbb{C}$, the conjugate of $a\in F$ is $\overline{a}\in F$.

Let $A = [a_{ij}]\in F^{m \times n}$ be a matrix. The conjugate of $A$ is the matrix $\overline{A} = [\overline{a_{ij}}]\in F^{m \times n}$

- $A,B \in F^{m \times n}$, $\overline{A + B} = \overline{A} + \overline{B}$

- $A \in F^{m \times n}, B \in F^{n \times p}$, $\overline{A \cdot B} = \overline{A} \cdot \overline{B}$

## 11. Hermitian

设 $A=[a_{ij}]\in\mathbb C^{m\times n}$。$A$ 的**共轭转置**（conjugate transpose）为

$$
A^H:=\overline A^{\,T}=[\overline{a_{ji}}]\in\mathbb C^{n\times m}.
$$

将 $A$ 视为线性映射 $A:\mathbb C^n\to\mathbb C^m$。相对于两边的标准内积，$A^H$ 表示 $A$ 的**伴随映射**，即

$$
\langle Ax,y\rangle=\langle x,A^Hy\rangle,
\qquad
\forall x\in\mathbb C^n,\ y\in\mathbb C^m.
$$

> 这是因为标准内积满足 $\langle u,v\rangle=v^Hu$，所以
>
> $$
> \langle Ax,y\rangle
> =y^HAx
> =(A^Hy)^Hx
> =\langle x,A^Hy\rangle.
> $$

特别地，若 $A\in\mathbb C^{n\times n}$ 满足

$$
A^H=A,
$$

则称 $A$ 为 **Hermitian 矩阵**（厄米矩阵）。此时 $A$ 表示 $\mathbb C^n$ 上的自伴算子；反之，$\mathbb C^n$ 上的线性算子在标准正交基下是自伴的，当且仅当其矩阵是 Hermitian 矩阵。

## 12. Trace

Let $A = [a_{ij}]\in F^{n \times n}$ be a square matrix. The trace of $A$ is the sum of the diagonal elements of $A$, denoted by $\operatorname{tr}(A)$.

$$
\operatorname{tr}(A) = \sum_{i=1}^n a_{ii}
$$

**Properties of Trace**

- $\operatorname{tr}(A + B) = \operatorname{tr}(A) + \operatorname{tr}(B)$
- $\operatorname{tr}(cA) = c\operatorname{tr}(A)$
- $\operatorname{tr}(AB) = \operatorname{tr}(BA)$
- $\overline{\operatorname{tr}(A)} = \operatorname{tr}(\overline{A})$
- $\operatorname{tr}(A^T) = \operatorname{tr}(A)$
- 若 $A=[a_{ij}],B=[b_{ij}]\in\mathbb C^{m\times n}$，则 $\operatorname{tr}(A^HB)=\displaystyle\sum_{i=1}^m\sum_{j=1}^n\overline{a_{ij}}b_{ij}$

> proof : $\operatorname{tr}(AB) = \operatorname{tr}(BA)$
>
> $$
> \begin{aligned}
> \operatorname{tr}(AB) &= \sum_{i=1}^n (AB)_{ii} \\
> &= \sum_{i=1}^n \sum_{j=1}^n a_{ij} b_{ji} \\
> &= \sum_{j=1}^n \sum_{i=1}^n b_{ji} a_{ij} \\
> &= \operatorname{tr}(BA)
> \end{aligned}
> $$

## 13. Inner Product

本节统一采用“**第一变量线性、第二变量共轭线性**”的约定。

### 13.1. 向量的标准内积

对任意

$$
x=
\begin{pmatrix}
x_1\\
x_2\\
\vdots\\
x_n
\end{pmatrix},
\qquad
y=
\begin{pmatrix}
y_1\\
y_2\\
\vdots\\
y_n
\end{pmatrix}
\in\mathbb C^n,
$$

定义 $\mathbb C^n$ 上的**标准内积**为

$$
\boxed{
\langle x,y\rangle
=\sum_{i=1}^n x_i\overline{y_i}
=x^T\overline y
=y^Hx.
}
$$

其中 $y^H=\overline y^{\,T}$ 是 $y$ 的共轭转置。该定义满足内积的三条公理。

**共轭对称性：**

$$
\begin{aligned}
\overline{\langle y,x\rangle}
&=\overline{\sum_{i=1}^n y_i\overline{x_i}}\\
&=\sum_{i=1}^n\overline{y_i}x_i\\
&=\langle x,y\rangle.
\end{aligned}
$$

因此

$$
\langle x,y\rangle=\overline{\langle y,x\rangle}.
$$

**正定性：**

$$
\langle x,x\rangle
=\sum_{i=1}^n x_i\overline{x_i}
=\sum_{i=1}^n|x_i|^2
\ge0,
$$

并且

$$
\langle x,x\rangle=0
\iff x_1=\cdots=x_n=0
\iff x=0.
$$

**第一变量线性：** 对任意 $a,b\in\mathbb C$ 及 $x,w,z\in\mathbb C^n$，

$$
\begin{aligned}
\langle ax+bw,z\rangle
&=\sum_{i=1}^n(ax_i+bw_i)\overline{z_i}\\
&=a\langle x,z\rangle+b\langle w,z\rangle.
\end{aligned}
$$

结合共轭对称性，第二变量相应地满足共轭线性：

$$
\langle x,ay+bz\rangle
=\overline a\langle x,y\rangle
+\overline b\langle x,z\rangle.
$$

在 $\mathbb R^n$ 中，共轭不起作用，标准内积退化为通常的点积

$$
\langle x,y\rangle=x^Ty.
$$

### 13.2. 矩阵的 Frobenius 内积

矩阵空间 $\mathbb C^{m\times n}$ 也是复向量空间。对 $A=[a_{ij}]$、$B=[b_{ij}]\in\mathbb C^{m\times n}$，定义

$$
\boxed{
\langle A,B\rangle_F
:=\operatorname{tr}(B^HA)
=\operatorname{tr}(AB^H)
=\sum_{i=1}^m\sum_{j=1}^n a_{ij}\overline{b_{ij}}.
}
$$

这一定义与向量标准内积采用相同的变量约定。

**共轭对称性：**

$$
\begin{aligned}
\overline{\langle B,A\rangle_F}
&=\overline{\operatorname{tr}(A^HB)}\\
&=\operatorname{tr}\big((A^HB)^H\big)\\
&=\operatorname{tr}(B^HA)\\
&=\langle A,B\rangle_F.
\end{aligned}
$$

**第一变量线性：**

$$
\begin{aligned}
\langle aA+bB,C\rangle_F
&=\operatorname{tr}\big(C^H(aA+bB)\big)\\
&=a\langle A,C\rangle_F+b\langle B,C\rangle_F.
\end{aligned}
$$

**第二变量共轭线性：**

$$
\begin{aligned}
\langle A,aB+bC\rangle_F
&=\operatorname{tr}\big((aB+bC)^HA\big)\\
&=\overline a\langle A,B\rangle_F
+\overline b\langle A,C\rangle_F.
\end{aligned}
$$

**正定性：**

$$
\begin{aligned}
\langle A,A\rangle_F
&=\operatorname{tr}(A^HA)\\
&=\sum_{i=1}^m\sum_{j=1}^n|a_{ij}|^2\\
&\ge0,
\end{aligned}
$$

且等号成立当且仅当 $A=0$。该内积诱导 Frobenius 范数：

$$
\|A\|_F=\sqrt{\langle A,A\rangle_F}.
$$

## 14. Determinant

### 14.1. Alternating multilinear map

let $\langle F, V \rangle$ be a vector space over $F$. A map $f: V^n \to F$ is called an alternating multilinear map if:

- multilinear: $f$ is linear in each variable
- alternating: $f(v_1, \cdots, v_i, \cdots, v_j, \cdots, v_n) = -f(v_1, \cdots, v_j, \cdots, v_i, \cdots, v_n)$ for any $v_i, v_j \in V$

Let $A = [a_{ij}]\in F^{n \times n}$ be a square matrix. The determinant of $A$ is the scalar $\operatorname{det}(A)$ defined by:

$$
|A| := \operatorname{det}(A) = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma) \prod_{i=1}^n a_{i, \sigma(i)}
$$

or equivalently,

$$
|A| = \sum_{j_1,j_2,\cdots,j_n \in [n]} \tau(j_1,j_2,\cdots,j_n) \prod_{i=1}^n a_{i,j_i}
$$

where $S_n$ is the symmetric group of degree $n$, $\operatorname{sgn}(\sigma)$ is the sign of the permutation $\sigma$, and $a_{i, \sigma(i)}$ is the element of $A$ at the $i$-th row and $\sigma(i)$-th column.

$$
\operatorname{sgn}(\sigma) = \begin{cases}
1_{F} & \text{if } \sigma \text{ is an even permutation} \\
-1_{F} & \text{if } \sigma \text{ is an odd permutation}
\end{cases}
$$

$\tau(j_1,j_2,\cdots,j_n)$ is the number of inverse pairs of the sequence $(j_1,j_2,\cdots,j_n)$.

It is not difficult to see that:

$$
\operatorname{sgn}(\sigma) = (-1)^{\tau(j_1,j_2,\cdots,j_n)}
$$

- Determinant is a multilinear map for each row of $A$
- Determinant does not change under transposition, i.e. $\operatorname{det}(A) = \operatorname{det}(A^T)$
- Determinant is a multilinear map for each column of $A$
- Determinant is an alternating multilinear map for both each row of $A$ and each column of $A$
- $\operatorname{det}(A) = \sum_{j_1,j_2,\cdots,j_n \in [n]} (-1)^{\tau(i_1,i_2,\cdots,i_n) + \tau(j_1,j_2,\cdots,j_n) } \prod_{k=1}^n a_{i_k,j_k}$

### 14.2. Laplace expansion

$I = {i_1, i_2, \cdots, i_k}$
$I' = [n] \setminus I$

$J = {j_1, j_2, \cdots, j_k}$
$J' = [n] \setminus J$

$\sum(X):= \sum_{x \in X} x$

$A_{I,J}$ is the submatrix of $A$ obtained by deleting the $i$-th $\in I'$ row and $j$-th $\in J'$ column.

$$
\operatorname{det}(A) = \sum_{J \subseteq [n] \wedge |J| = k} (-1)^{\sum(I) + \sum(J)} \operatorname{det}(A_{I,J}) \operatorname{det}(A_{I',J'})
$$

- $\operatorname{det}(AB) = \operatorname{det}(A) \operatorname{det}(B)$

## 15. Adjugate matrix

$A_{ij}$ is the submatrix of $A$ obtained by deleting the $i$-th row and $j$-th column.

Let $A = [a_{ij}]\in F^{n \times n}$ be a square matrix. The adjugate of $A$ is the matrix $A^{\text{\#}}:=\operatorname{adj}(A) = [a^{\text{\#}}_{ij}]\in F^{n \times n}$ defined by $a^{\text{\#}}_{ij} = (-1)^{i+j} \operatorname{det}(A_{ji})$.

$$
A A^{\text{\#}} = A^{\text{\#}} A = \operatorname{det}(A) I
$$

> proof
>
> $$
> \begin{aligned}
> (A A^{\text{\#}})_{ij} &= \sum_{k=1}^n a_{ik} a^{\text{\#}}_{kj} \\
> &= \sum_{k=1}^n a_{ik} (-1)^{k+j} \operatorname{det}(A_{jk}) \\
> &= \operatorname{det}(A) \delta_{ij}
> \end{aligned}
> $$

- $A$ is invertible if and only if $\operatorname{det}(A) \not= 0$
- if $A$ is invertible, then $A^{-1} = \frac{1_F}{\operatorname{det}(A)} A^{\text{\#}}$
