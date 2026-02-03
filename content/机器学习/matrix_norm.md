---
title: Matrix Norm
---

All matrix is belong to $ \mathbb{C}^{m \times n} $ if not specified.

## 1. Vector p norm

$$
\|x\|_p = \left( \sum_{i=1}^n |x_i|^p \right)^{1/p}
$$

## 2. Matrix p norm

$$
\|A\|_p = \max_{\|x\|_p = 1} \|Ax\|_p
$$

## 3. Frobenius norm

$$
\|A\|_F = \sqrt{\sum_{i=1}^n \sum_{j=1}^n |a_{ij}|^2} = \sqrt{tr(A^H A)} = \sqrt{tr(A A^H)}
$$

### Frobenius norm and singular value

$$
\|A\|_F = \sqrt{\sum_{i=1}^r \sigma_i^2}
$$

> proof
>
> $$
> \|A\|_F = \sqrt{tr(A^T A)} = \sqrt{tr(V \Sigma^2 V^T)} = \sqrt{tr(\Sigma^2)} = \sqrt{\sum_{i=1}^r \sigma_i^2}
> $$
>
> Q.E.D.

### Orthogonal matrix do not change the Frobenius norm

$$
\|A\|_F = \|J A \|_F = \| A K\|_F, \forall J, K \in \mathbb{R}^{m \times m} \text{ is orthogonal matrix}
$$

## 4. Spectral norm(Matrix 2 norm)

$$
\|A\|_2 = \max_{\|x\|_2 = 1} \|Ax\|_2 = \max_{x} \frac{\|Ax\|_F}{\|x\|_F}
$$

### Orthogonal matrix do not change the spectral norm

$$
\|A\|_2 = \|J A \|_2 = \| A K\|_2, \forall J, K \in \mathbb{R}^{m \times m} \text{ is orthogonal matrix}
$$

> proof
>
> $$
> \|A\|_2 = \max_{\|x\|_2 = 1} \|Ax\|_2 = \max_{x} \frac{\|Ax\|_F}{\|x\|_F} = \max_{x} \frac{\|J A x\|_F}{\|x\|_F} = \|J A \|_2
> $$
>
> similar, $\|A\|_2 = \| A K\|_2$
> Q.E.D.
