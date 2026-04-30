---
title: 线性代数的结论
---

本文的向量空间的域默认都为$\mathbb{R}$

## 定义

- n阶方阵上的定义内积$\langle A,B\rangle := tr(A^TB)$
- $skew(A):=(A-A^T)/2$
- $sym(A):=(A+A^T)/2$

## 性质

1. 对称矩阵对反对称矩阵正交。
2. 方阵$M$在反对称矩阵空间的正交投影为$skew(M)$
3. 方阵$M$在对称矩阵空间的投影为$sym(M)$
4. 在实数域（$\mathbb{R}$）上，$W W^T \mathbf{x} = \mathbf{0} \Longleftrightarrow W^T \mathbf{x} = \mathbf{0}$。
5. 设$H$为实对称半正定矩阵，则$H \mathbf{v} = \mathbf{0} \iff \mathbf{v}^T H \mathbf{v} = 0$
