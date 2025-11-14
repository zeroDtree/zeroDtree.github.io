---
title: svd
---

All matrix is belong to $\mathbb{R}^{m \times n}$ if not specified.

## 1. Preliminaries

$B = A^TA \in \mathbb{R}^{n \times n}$ is a symmetric matrix, so it is diagonalizable, and the eigenvalues are non-negative.

$C = AA^T \in \mathbb{R}^{m \times m}$ is also a symmetric matrix, so it is diagonalizable, and the eigenvalues are non-negative.

$B = V \Lambda_B V^T, V \in \mathbb{R}^{n \times n}$

$C = U \Lambda_C U^T, U \in \mathbb{R}^{m \times m}$

#### 1.1. proposition

$B$ and $C$ have the same non-zero eigenvalues with the same multiplicity(geometric multiplicity).

> proof
>
> $$
> B v = A^T A v= \lambda v \Longrightarrow\\
> C Av = A A^T A v = \lambda A v
> $$
>
> if $\lambda$ is an eigenvalue of $B$, then it is also an eigenvalue of $C$.
> similarly,
>
> $$
> C v = A A^T v = \lambda v \Longrightarrow\\
> B A^T v = A^T A A^T v = \lambda A^T v
> $$
>
> if $\lambda$ is an eigenvalue of $C$, then it is also an eigenvalue of $B$.
> so $B$ and $C$ have the same eigenvalues.
> we analyze the geometric multiplicity of the non-zero eigenvalues.
>
> $$
> v \in Ker(A^T A - \lambda I) \Longleftrightarrow B v = A^T A v = \lambda v \Longrightarrow
> $$
>
> $$
> C Av = A A^T A v = \lambda A v \Longleftrightarrow Av \in Ker(A A^T - \lambda I)
> $$
>
> consider the linear map:
>
> $$
> f: Ker(A^T A - \lambda I) \to Ker(A A^T - \lambda I)\\
> f(v) = Av
> $$
>
> if $f(v)=Av=\lambda v=0$, because $\lambda \neq 0$, so $v=0$.
> so $f$ is injective.
> for any $w \in Ker(A A^T - \lambda I)$, there exists $v=(1/\lambda)A^T w \in Ker(A^T A - \lambda I)$ such that $f(v)=A (1/\lambda)A^T w = (1/\lambda)A A^T w = (1/\lambda) \lambda w = w$.
> so $f$ is surjective.
> so $f$ is an isomorphism.
> Therefore, $B$ and $C$ have the same non-zero eigenvalues with the same geometric multiplicity.

#### 1.2. proposition

$$
Ker(A) = Ker(A^T A)
$$

> proof
>
> $$
> x \in Ker(A) \Longleftrightarrow A x = 0 \implies A^T A x = 0 \Longleftrightarrow x \in Ker(A^T A)
> $$
>
> $$
> x \in Ker(A^T A) \Longleftrightarrow A^T A x = 0 \implies x^T A^T A x = 0 \implies A x = 0 \Longleftrightarrow x \in Ker(A)
> $$
>
> Therefore, $Ker(A) = Ker(A^T A)$.

## 2. SVD

$$
A = U \Sigma V^T
$$

$V = (v_1, v_2, \cdots, v_n)$

$U = (u_1, u_2, \cdots, u_m)$

$U = (u_1, u_2, \cdots, u_m) := ((1/\sqrt{\lambda_1}) A v_1, (1/\sqrt{\lambda_2}) A v_2, \cdots, (1/\sqrt{\lambda_r}) A v_r, u_{r+1}, \cdots, u_m)$

$\Sigma 
= \begin{bmatrix}
diag(\sqrt{\lambda_1}, \sqrt{\lambda_2}, \cdots, \sqrt{\lambda_r}),&0\\
0,&0
\end{bmatrix}$

$\lambda_i$ is the eigenvalue of $B$ and $C$. $\lambda_i \geq \lambda_{i+1}$

$v_i$ is the eigenvector of $B=A^TA$, and $(v_i)_{i=r+1}^{n}$ belongs to $Ker(A^T A)$

$u_i$ is the eigenvector of $C=AA^T$

$$
\begin{aligned}
U \Sigma V^T &= \sum_{i=1}^r \sqrt{\lambda_i} u_i v_i^T\\
&= \sum_{i=1}^r \sqrt{\lambda_i} ((1/\sqrt{\lambda_i}) A v_i) v_i^T\\
&= \sum_{i=1}^r A v_i v_i^T\\
&= A \sum_{i=1}^r v_i v_i^T\\
\end{aligned}
$$

It is need to prove that $A \sum_{i=1}^r v_i v_i^T = A$

$$
\forall x=(x_1, x_2, \cdots, x_n)^T \in \mathbb{R}^n, x = \sum_{i=1}^{n} \alpha_i v_i
$$

$$v_i^T x = v_i^T \sum_{i=1}^{n} \alpha_i v_i = \alpha_i$$

$$
x = \sum_{i=1}^{n} \alpha_i v_i = \sum_{i=1}^{n} (v_i^T x) v_i
$$

$$
\begin{aligned}
\forall x, A \sum_{i=1}^r v_i v_i^T x = A \sum_{i=1}^r v_i v_i^T x + A \sum_{i=r+1}^{n} v_i v_i^T x = A x \implies A \sum_{i=1}^r v_i v_i^T = A\\
\end{aligned}
$$

Therefore, $A = U \Sigma V^T = \sum_{i=1}^r \sqrt{\lambda_i} u_i v_i^T$

let $\sigma_i = \sqrt{\lambda_i}$, then $A = \sum_{i=1}^r \sigma_i u_i v_i^T$
