---
title: Cholesky 分解
tags:
  - 线性代数
  - 矩阵分解
date: 2026-11-22
---

Cholesky 分解把实对称正定矩阵写成 $A=LL^\top$，其中 $L$ 为下三角矩阵、对角元为正。

## 定理

> [!abstract] 定理（Cholesky 分解）
> 设 $A\in\mathbb{R}^{n\times n}$ 实对称正定。则存在唯一的下三角矩阵 $L$，其对角元均为正，使得
>
> $$
> A=LL^\top.
> $$
>
> > [!note]- 证明
> > **存在性**
> >
> > 对 $n$ 归纳。$n=1$ 时 $A=[a]$，由正定性
> >
> > $$
> > a=\mathbf{e}_1^\top A\mathbf{e}_1>0,
> > $$
> >
> > 取 $L=[\sqrt{a}]$ 即可。
> >
> > 设结论对 $n-1$ 阶实对称正定矩阵成立。将 $A$ 分块为
> >
> > $$
> > A=\begin{bmatrix}
> > a & \mathbf{b}^\top\\
> > \mathbf{b} & C
> > \end{bmatrix},
> > $$
> >
> > 其中 $a>0$，$\mathbf{b}\in\mathbb{R}^{n-1}$，$C$ 为 $n-1$ 阶对称矩阵。令
> >
> > $$
> > S=C-\frac{\mathbf{b}\mathbf{b}^\top}{a}.
> > $$
> >
> > 对任意非零 $\mathbf{y}\in\mathbb{R}^{n-1}$，取
> >
> > $$
> > \mathbf{x}=\begin{bmatrix}
> > -\frac{\mathbf{b}^\top\mathbf{y}}{a}\\
> > \mathbf{y}
> > \end{bmatrix}\ne\mathbf{0}.
> > $$
> >
> > 先计算 $A\mathbf{x}$：
> >
> > $$
> > \begin{aligned}
> > A\mathbf{x}
> > &=\begin{bmatrix}
> > a & \mathbf{b}^\top\\
> > \mathbf{b} & C
> > \end{bmatrix}
> > \begin{bmatrix}
> > -\frac{\mathbf{b}^\top\mathbf{y}}{a}\\
> > \mathbf{y}
> > \end{bmatrix}\\
> > &=\begin{bmatrix}
> > a\left(-\frac{\mathbf{b}^\top\mathbf{y}}{a}\right)+\mathbf{b}^\top\mathbf{y}\\
> > \mathbf{b}\left(-\frac{\mathbf{b}^\top\mathbf{y}}{a}\right)+C\mathbf{y}
> > \end{bmatrix}
> > =\begin{bmatrix}
> > 0\\
> > \left(C-\frac{\mathbf{b}\mathbf{b}^\top}{a}\right)\mathbf{y}
> > \end{bmatrix}.
> > \end{aligned}
> > $$
> >
> > 于是
> >
> > $$
> > \begin{aligned}
> > \mathbf{x}^\top A\mathbf{x}
> > &=\begin{bmatrix}
> > -\frac{\mathbf{b}^\top\mathbf{y}}{a} & \mathbf{y}^\top
> > \end{bmatrix}
> > \begin{bmatrix}
> > 0\\
> > S\mathbf{y}
> > \end{bmatrix}
> > =\mathbf{y}^\top S\mathbf{y}.
> > \end{aligned}
> > $$
> >
> > 由 $A$ 正定，$\mathbf{x}^\top A\mathbf{x}>0$，故 $\mathbf{y}^\top S\mathbf{y}>0$。$C$ 与 $\mathbf{b}\mathbf{b}^\top$ 均对称，因此 $S$ 对称；所以 $S$ 正定。由归纳假设，存在对角元为正的下三角矩阵 $L_2$，使 $S=L_2L_2^\top$。令
> >
> > $$
> > L=\begin{bmatrix}
> > \sqrt{a} & \mathbf{0}^\top\\
> > \frac{\mathbf{b}}{\sqrt{a}} & L_2
> > \end{bmatrix},
> > $$
> >
> > 则
> >
> > $$
> > LL^\top=
> > \begin{bmatrix}
> > a & \mathbf{b}^\top\\
> > \mathbf{b} & \frac{\mathbf{b}\mathbf{b}^\top}{a}+L_2L_2^\top
> > \end{bmatrix}
> > =
> > \begin{bmatrix}
> > a & \mathbf{b}^\top\\
> > \mathbf{b} & C
> > \end{bmatrix}
> > =A.
> > $$
> >
> > 且 $L$ 为下三角矩阵，对角元 $\sqrt{a}$ 与 $L_2$ 的对角元均为正。
> >
> > **唯一性**
> >
> > 设 $L_1,L_2$ 都是对角元为正的下三角矩阵，且
> >
> > $$
> > A=L_1L_1^\top=L_2L_2^\top.
> > $$
> >
> > 两者对角元为正，因此均可逆。左乘 $L_2^{-1}$、右乘 $L_2^{-\top}$，得
> >
> > $$
> > L_2^{-1}L_1L_1^\top L_2^{-\top}=I.
> > $$
> >
> > 令 $Q=L_2^{-1}L_1$，则 $QQ^\top=I$。可逆下三角矩阵的逆仍为下三角，下三角矩阵的乘积仍为下三角，故 $Q$ 为下三角矩阵；$QQ^\top=I$ 又说明 $Q$ 为正交矩阵，即 $Q^\top=Q^{-1}$。
> >
> > 于是 $Q^\top=Q^{-1}$ 下三角，从而 $Q=(Q^\top)^\top$ 为上三角。$Q$ 同时是下三角与上三角矩阵，故只能是对角矩阵。设 $Q=\operatorname{diag}(q_{11},\ldots,q_{nn})$，由 $QQ^\top=I$ 得 $q_{ii}^2=1$。
> >
> > 另一方面，$L_2^{-1}$ 仍为下三角矩阵，且对角元为 $\frac{1}{(L_2)_{ii}}$；下三角矩阵乘积的对角元等于对角元之积，因此
> >
> > $$
> > q_{ii}=\frac{(L_1)_{ii}}{(L_2)_{ii}}>0,
> > $$
> >
> > 故 $q_{ii}=1$，即 $Q=I$。于是 $L_2^{-1}L_1=I$，从而 $L_1=L_2$。$\square$