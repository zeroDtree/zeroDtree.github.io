---
title: auto-grad
---

- [1. Base Principle](#1-base-principle)
- [2. Useful Rules](#2-useful-rules)
  - [2.1. Differential](#21-differential)
  - [2.2. Trace](#22-trace)
- [3. Common differential calculations](#3-common-differential-calculations)
  - [3.1. MSE](#31-mse)
  - [3.2. Eigenvalue and Eigenvector](#32-eigenvalue-and-eigenvector)
    - [3.2.1. Eigenvalue](#321-eigenvalue)
    - [3.2.2. Eigenvector](#322-eigenvector)

## 1. Base Principle

$l = f(A),f:\mathbb{R}^{m \times n} \to \mathbb{R},f \in \mathcal{C}^1$

$$
\begin{align*}
\frac{\partial f}{\partial A} = \begin{bmatrix}
\frac{\partial f}{\partial A_{1,1}} & \frac{\partial f}{\partial A_{1,2}} & \cdots & \frac{\partial f}{\partial A_{1,n}} \\
\frac{\partial f}{\partial A_{2,1}} & \frac{\partial f}{\partial A_{2,2}} & \cdots & \frac{\partial f}{\partial A_{2,n}} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial f}{\partial A_{m,1}} & \frac{\partial f}{\partial A_{m,2}} & \cdots & \frac{\partial f}{\partial A_{m,n}}
\end{bmatrix}
\end{align*}
$$

$$
\begin{align*}
d l &= tr(d l)\\
&= tr(d f(A))\\
&= tr(\sum_{i,j} \frac{\partial f}{\partial A_{i,j}} d A_{i,j})\\
&= tr((\frac{\partial f}{\partial A})^T d A)
\end{align*}
$$

$\forall d A, dl = tr(B^T d A) \Longrightarrow \frac{\partial f}{\partial A} = B$

So all we need to do is to find a $B$ that satisfies $\forall d A, dl = tr(B^T d A)$.

## 2. Useful Rules

### 2.1. Differential

- Addition rule: $d(X \pm Y) = dX \pm dY$
- Product rule: $d(XY) = (dX)Y + XdY$
- Inverse: $dX^{-1} = -X^{-1}dXX^{-1}$
- Transpose: $d(X^T) = (dX)^T$
- Trace: $d\text{tr}(X) = \text{tr}(dX)$
- Determinant: $d|X| = \text{tr}(X^\# dX)$, where $X^\#$ is the adjugate matrix
- Hadamard product: $d(X \odot Y) = dX \odot Y + X \odot dY$
- Component-wise(element-wise) function: $d\sigma(X) = \sigma'(X) \odot dX$

### 2.2. Trace

- Scalar trace: $a = \text{tr}(a)$
- Transpose: $\text{tr}(A^T) = \text{tr}(A)$
- Linearity: $\text{tr}(aA + bB) = a\text{tr}(A) + b\text{tr}(B)$
- Cyclic property: $\text{tr}(AB) = \text{tr}(BA)$, where $A$ and $B^T$ are conformable. Both equal to $\sum_{i,j} A_{ij}B_{ji}$
- Cyclic property with Hadamard product: $\text{tr}(A^T(B \odot C)) = \text{tr}((A \odot B)^TC)$, where $A, B, C$ have the same dimensions. Both equal to $\sum_{i,j} A_{ij}B_{ij}C_{ij}$

## 3. Common differential calculations

- $n$ : dimension of output
- $\mathbf{\hat{y}}$ : predicted value
- $\mathbf{y}$ : target value

### 3.1. MSE

$\mathbf{\hat{y}} = W\mathbf{x} + \mathbf{b}$

$l = \sum_{i=1}^n (y_i - \hat{y}_i)^2 = (\mathbf{\hat{y}} - \mathbf{y})^T(\mathbf{\hat{y}}- \mathbf{y})$

let $\mathbf{t} = \mathbf{\hat{y}} - \mathbf{y}$,

$
dl = tr(dl) = tr(\mathbf{t}^T d\mathbf{t} + d\mathbf{t}^T \mathbf{t}) =  tr(\mathbf{t}^T d\mathbf{t}) + tr(d\mathbf{t}^T \mathbf{t}) = tr((2\mathbf{t})^T d\mathbf{t})
$

Thus.
$\frac{\partial l}{\partial \mathbf{t}} = 2\mathbf{t}$

$d \mathbf{t} = d(\mathbf{\hat{y}} - \mathbf{y}) = d\mathbf{\hat{y}}$

$\frac{\partial l}{\partial \mathbf{\hat{y}}} = 2\mathbf{t}$

$d \mathbf{\hat{y}} = d(W\mathbf{x} + \mathbf{b}) = dW\mathbf{x}$

$dl = tr((\frac{\partial l}{\mathbf{\partial \hat{y}}})^T dW \mathbf{x}) = tr(\mathbf{x} (\frac{\partial l}{\mathbf{\partial \hat{y}}})^T dW) = tr(((\frac{\partial l}{\mathbf{\partial \hat{y}}}) \mathbf{x}^T)^T dW)$

$\frac{\partial l}{\partial W} = (\frac{\partial l}{\mathbf{\partial \hat{y}}}) \mathbf{x}^T$ = $2\mathbf{t} \mathbf{x}^T$

### 3.2. Eigenvalue and Eigenvector

Suppose $A \in \text{Sym}_n(\mathbb{R})$, then $A$ can be decomposed as

$$
A = Q \Lambda Q^T
$$

$$
\Lambda = \text{diag}(\lambda_1, \lambda_2, \cdots, \lambda_n), \lambda_i \leq \lambda_{i+1}\\
Q=(\mathbf{q}_1, \mathbf{q}_2, \cdots, \mathbf{q}_n) \in \mathbf{O}_n(\mathbb{R}), \text{where } \mathbf{O}_n(\mathbb{R}) = \{\mathbf{M} \in \mathbb{R}^{n \times n} \mid \mathbf{M}^T\mathbf{M} = \mathbf{I}\}
$$

where $\lambda_i$ are the eigenvalues of $A$ and $Q$ is the eigenvector matrix.

#### 3.2.1. Eigenvalue

$$
\begin{align*}
\Lambda &= Q^T A Q\\
d\Lambda &= Q^T dA Q\\
dl &= tr(dl)\\
& =tr((\frac{\partial l}{\partial \Lambda})^T d\Lambda) \\
&= tr((\frac{\partial l}{\partial \Lambda})^T Q^T dA Q)\\
&= tr(Q (\frac{\partial l}{\partial \Lambda})^T Q^T dA)\\
&= tr((Q \frac{\partial l}{\partial \Lambda} Q^T)^T d A)
\end{align*}
$$

Thus,

$$
\frac{\partial l}{\partial A} = Q \frac{\partial l}{\partial \Lambda} Q^T
$$

#### 3.2.2. Eigenvector

$Q^T dQ + dQ^T Q = 0$, because $Q^T Q = \mathbf{I}$
Let $H = Q^T dQ$

$$
\begin{align*}
dA &=  dQ \Lambda Q^T + Q d\Lambda Q^T + Q \Lambda dQ^T\\
Q^T dA Q &= (Q^T dQ) \Lambda + d\Lambda +  \Lambda (dQ^TQ)\\
&= H \Lambda + d\Lambda +  \Lambda H\\
\end{align*}
$$

$$
\begin{align*}
(Q^T dA Q)_{ii} &= d \Lambda_{ii}\\
\forall i\not= j, (Q^T dA Q)_{ij} &= H_{ij}(\lambda_j - \lambda_i)\\
\forall i\not= j, H_{ij} &= \frac{1}{\lambda_j - \lambda_i} (Q^T dA Q)_{ij}\\
\forall i, H_{ii} &= 0\\
\end{align*}
$$

Let $F_{ij} = \begin{cases}
    \frac{1}{\lambda_j - \lambda_i} & \text{if } i\not= j\\
    0 & \text{if } i=j
\end{cases}$

$
H = F \odot (Q^T dA Q)
$

$$
\begin{align*}
tr(dl) &= tr(\frac{\partial l}{\partial Q}^T dQ)\\
&= tr(\frac{\partial l}{\partial Q}^T QH)\\
& = tr\left((Q^T \frac{\partial l}{\partial Q})^T (F \odot (Q^T dA Q))\right)\\
& = tr\left( \left((Q^T \frac{\partial l}{\partial Q}) \odot F\right)^T (Q^T dA Q) \right)\\
& = tr\left(Q\ \left( (Q^T\frac{\partial l}{\partial Q}) \odot F \right)^T Q^T d A\right)
\end{align*}
$$