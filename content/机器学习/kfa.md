---
tags:
  - 线性代数
  - 统计
---

# Kronecker-factored Approximate

- [Kronecker-factored Approximate](#kronecker-factored-approximate)
  - [1. 约定](#1-约定)
  - [2. 目标](#2-目标)
  - [3. Kronecker](#3-kronecker)
    - [3.1. Definition](#31-definition)
    - [3.2. Properties](#32-properties)
  - [4. Useful formula](#4-useful-formula)

## 1. 约定

默认所有向量都是列向量

## 2. 目标

求$F^{-1}v$

Fisher 信息阵$F = E\left[\frac{\partial L}{\partial \theta}(\frac{\partial L}{\partial \theta})^T\right]$

把神经网络的每个权重矩阵逐列向量化，然后按一个确定的顺序排列这些向量，得到一个长向量$\theta$。对于$y = Wx + b$, 令$g = \frac{\partial L}{\partial y}$，把 $x$ 和 $I$ 在后文中用$a$表示，$\theta_i$ 表示按前述顺序排列的第 $i$ 个权重矩阵的向量化表示。在独立性近似与块对角近似下：

$$
E\left[\frac{\partial L}{\partial \theta_i}\cdot \frac{\partial L}{\partial \theta_i}^T\right] \approx E[a_ia_i^T] \otimes E[g_ig_i^T] =: A_i \otimes G_i \tag{未证明}
$$

$$
\begin{align*}
F &\approx diag(A_1\otimes G_1, A_2 \otimes G_2, \ldots, A_n \otimes G_n) \tag{未证明}\\
&=
\begin{pmatrix}
    A_1 \otimes G_1, &0,&0,&\cdots,&0\\
    0, &A_2 \otimes G_2, &0, &\cdots, &0\\
    0, &0, &A_3 \otimes G_3, &\cdots, &0\\
    \vdots, &\vdots, &\vdots, &\ddots, &\vdots\\
    0, &0, &0, &\cdots, &A_n \otimes G_n
\end{pmatrix}
\end{align*}
$$

> [!abstract] 命题（K-FAC 块对角近似下的逆矩阵向量积）
> 记第 $i$ 层的 Fisher 对角块近似为 $F_i := A_i \otimes G_i$，其中 $A_i = E[a_i a_i^T]$，$G_i = E[g_i g_i^T]$。对向量 $v_i = vec(V_i)$，有
>
> $$
> F_i^{-1} \cdot v_i = vec\!\left(G_i^{-1} V_i A_i^{-1}\right) = vec\!\left(E[g_i \cdot g_i^T]^{-1} V_i E[a_i \cdot a_i^T]^{-1}\right).
> $$
>
> > [!note]- 证明
> > 对于 $y = Wx + b$，令 $g = \frac{\partial L}{\partial y}$，有
> >
> > $$
> > \frac{\partial L}{\partial W} = \frac{\partial L}{\partial y} \cdot x^T,
> > \qquad
> > \frac{\partial L}{\partial b} = \frac{\partial L}{\partial y} \cdot I.
> > $$
> >
> > 把 $x$ 和 $I$ 统一记为 $a$，则全参数 Fisher 信息阵分块写为
> >
> > $$
> > F =
> > \begin{matrix}
> > E[\frac{\partial L}{\partial \theta} \cdot \frac{\partial L}{\partial \theta}^T]
> > \end{matrix} =
> > \begin{bmatrix}
> >     E[\frac{\partial L}{\partial \theta_1} \cdot \frac{\partial L}{\partial \theta_1}^T]
> >     E[\frac{\partial L}{\partial \theta_1} \cdot \frac{\partial L}{\partial \theta_2}^T]\cdots & E[\frac{\partial L}{\partial \theta_1} \cdot \frac{\partial L}{\partial \theta_n}^T]\\
> >     E[\frac{\partial L}{\partial \theta_2} \cdot \frac{\partial L}{\partial \theta_1}^T]  E[\frac{\partial L}{\partial \theta_2} \cdot \frac{\partial L}{\partial \theta_2}^T]  \cdots & E[\frac{\partial L}{\partial \theta_2} \cdot \frac{\partial L}{\partial \theta_n}^T] \\
> >     \vdots &\vdots\\
> >     E[\frac{\partial L}{\partial \theta_n} \cdot \frac{\partial L}{\partial \theta_1}^T]  E[\frac{\partial L}{\partial \theta_n} \cdot \frac{\partial L}{\partial \theta_2}^T]  \cdots & E[\frac{\partial L}{\partial \theta_n} \cdot \frac{\partial L}{\partial \theta_n}^T]
> > \end{bmatrix}.
> > $$
> >
> > 对第 $i$ 个对角块，利用向量化与 Kronecker 积性质 $vec(g_i a_i^T) = a_i \otimes g_i$ 及 $(A \otimes B)(C \otimes D) = (AC) \otimes (BD)$：
> >
> > $$
> > \begin{align*}
> > E\left[\frac{\partial L}{\partial \theta_i}\cdot \frac{\partial L}{\partial \theta_i}^T\right] &=
> > E[vec(g_i \cdot a_i^T)vec(g_i \cdot a_i^T)^T] \\
> > &= E[(a_i \otimes g_i)(a_i^T \otimes g_i^T)] \\
> > &= E[(a_ia_i^T)\otimes(g_ig_i^T)].
> > \end{align*}
> > $$
> >
> > 在近似 $F_i = A_i \otimes G_i$ 下，由于 $A_i$ 和 $G_i$ 都是对称矩阵，对称矩阵的逆矩阵仍为对称矩阵。结合 $(A_i \otimes G_i)^{-1} = A_i^{-1} \otimes G_i^{-1}$ 与 $(A \otimes B)vec(X) = vec(BXA^T)$，得
> >
> > $$
> > \begin{align*}
> > F_i^{-1}\cdot v_i &= (A_i^{-1}\otimes G_i^{-1})vec(V_i)\\
> > &= vec(G_i^{-1}V_i(A_i^{-1})^T)\\
> > &= vec(G_i^{-1}V_iA_i^{-1})\\
> > &= vec(E[g_i \cdot g_i^T]^{-1}V_iE[a_i \cdot a_i^T]^{-1}). \quad \square
> > \end{align*}
> > $$

## 3. Kronecker

### 3.1. Definition

$$
A\otimes B= \begin{pmatrix}
a_{11}B & a_{12}B & \cdots & a_{1n}B \\
a_{21}B & a_{22}B & \cdots & a_{2n}B \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1}B & a_{m2}B & \cdots & a_{mn}B
\end{pmatrix}
$$

### 3.2. Properties

$$
vec(uv^T) = v \otimes u
$$

$$
(A \otimes B)^T = (A^T \otimes B^T)
$$

$$
(A \otimes B)(A^T \otimes B^T) = AA^T \otimes BB^T
$$

$$
(A \otimes B)^{-1} = A^{-1} \otimes B^{-1}
$$

$$
(A \otimes B)vec(X) = vec(BXA^T)
$$

## 4. Useful formula

$$
(A+bc^T)^{-1} = A^{-1} + \frac{A^{-1}bc^TA^{-1}}{1-c^TA^{-1}b}
$$

$$
(A+bc^T)^{-1}d= A^{-1}d + \frac{A^{-1}bc^TA^{-1}d}{1-c^TA^{-1}b}
$$

$$
\begin{align*}
(F - \frac{\partial L}{\partial \theta} \frac{\partial L}{\partial \theta}^T)^{-1}d &=
F^{-1}d + \frac{F^{-1}\frac{\partial L}{\partial \theta} \frac{\partial L}{\partial \theta}^TF^{-1}d}{1-\frac{\partial L}{\partial \theta}^TF^{-1}\frac{\partial L}{\partial \theta}}\\
&= F^{-1}d + (\frac{\frac{\partial L}{\partial \theta}^TF^{-1}d}{1-\frac{\partial L}{\partial \theta}^TF^{-1}\frac{\partial L}{\partial \theta}})F^{-1}\frac{\partial L}{\partial \theta}\\
&= F^{-1}d + (\frac{\frac{\partial L}{\partial \theta}^T(F^{-1}d)}{1-\frac{\partial L}{\partial \theta}^T(F^{-1}\frac{\partial L}{\partial \theta})})(F^{-1}\frac{\partial L}{\partial \theta})\\
\end{align*}
$$
