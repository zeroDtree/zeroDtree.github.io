---
title: Kabsch-algorithm
---

# Kabsch-algorithm

Kabsch-algorithm 是一种用于计算两个几何体(点集)之间的最佳对齐的算法。

## 目标

两个集合体 $P,Q \in \mathbb{R}^{N \times 3}$，找到一个$SE(3)$变换使得，$P$和$Q$的距离最小。

默认所有向量都为列向量

$$
\min_{R,t} l(R, t) = \sum_{i=1}^{N} \| p_i - (Rq_i + t) \|^2 = (p_i - (Rq_i+ t) )^T(p_i - (Rq_i+ t) ), t \in \mathbb{R}^3, R \in SO(3)
$$

$$
\begin{align*}
l &= \sum_{i=1}^{N} \|p_i\|^2 + \| (Rq_i + t) \|^2 - 2p_i^T(Rq_i + t) \\
&= \sum_{i=1}^{N} \|p_i\|^2 + \|Rq_i\|^2 + \|t\|^2 + 2t^T(Rq_i) - 2p_i^T(Rq_i + t) \\
& = \sum_{i=1}^{N} \|p_i\|^2 + \|Rq_i\|^2 + \|t\|^2 + 2t^T(Rq_i - 2p_i) - 2p_i^TRq_i\\
&= \sum_{i=1}^{N} \|p_i\|^2 + \sum_{i=1}^{N} \|Rq_i\|^2  + N\|t\|^2 + 2t^T \sum_{i=1}^{N} (Rq_i - 2p_i) - 2\sum_{i=1}^{N} p_i^TRq_i\\
\frac{\partial l}{\partial t} &= 2Nt + 2 \sum_{i=1}^{N} (Rq_i - 2p_i) = 0 \\
&\Rightarrow t = \frac{1}{N} \sum_{i=1}^{N} (p_i - R q_i)\\
& = \frac{1}{N} \sum_{i=1}^{N} p_i - \frac{1}{N} \sum_{i=1}^{N} R q_i\\
& = \frac{1}{N} \sum_{i=1}^{N} p_i - R \frac{1}{N} \sum_{i=1}^{N}  q_i\\
\end{align*}
$$

因此原问题可以先将两个点集的质心对齐，然后计算旋转矩阵。

$A = P - \frac{1}{N} \sum_{i=1}^{N} p_i$

$B = Q - \frac{1}{N} \sum_{i=1}^{N} q_i$

最小化目标转化为

$$
\min_{R} l(R) = \sum_{i=1}^{N} \| p_i' - R q_i' \|^2 \iff \min_{R} \|A - (RB^T)^T\|^2_F
$$

为了简化记号，

$$
\begin{align*}
\|A - (RB^T)^T\|^2_F  &= \|A - BR^T\|^2_F\\
& = Tr((A - BR^T)^T(A - BR^T))\\
&= Tr(A^TA - RB^TA - A^TBR^T + RB^TBR^T)\\
& = Tr(A^TA)  + Tr(B^TB) -2Tr(A^TBR^T)
\end{align*}
$$

因此原问题等价于最大化

$$
\max_{R} Tr(A^TBR^T) = \max_{R} Tr(RB^TA)
$$

$C := B^TA = USV^T$ (SVD分解)

$$
Tr(R C) = Tr(R USV^T) = Tr(V^T R U S)
$$

令 $M = V^T R U$，则有：

$$
\text{Tr}(RC) = \text{Tr}(MS)
$$

### 最大化迹的形式

- $M$ 仍然是正交矩阵，因为 $V^T R U$ 保持正交性。
- $S$ 是对角矩阵，奇异值为 $s_1, s_2, s_3$。

根据迹的性质：

$$
\text{Tr}(MS) = \sum_{i=1}^3 M_{ii} s_i
$$

此时，我们需要最大化 $M_{ii} s_i$ 的和。

### 利用性质取最大值

由于 $M$ 是正交矩阵，满足：

$$
-1 \le M_{ii} \le 1
$$

为了最大化 $ \text{Tr}(MS) $，我们需要 $M_{ii} = 1$。最优选择是使得：

$$
M = I \quad \Longrightarrow \quad V^T R U = I \quad \Longrightarrow \quad R = V U^T
$$

### 修正旋转矩阵的行列式

旋转矩阵必须满足 $\det(R) = 1$。然而 $\det(V U^T)$ 的行列式可能为 -1。为了修正这一点，引入一个校正矩阵 $F$：

$$
F = \operatorname{diag}(1, 1, \det(V U^T))
$$

这样可以确保：

$$
\det(V F U^T) = \det(V) \cdot \det(F) \cdot \det(U^T) = 1
$$

最终最优解为：

$$
R = V F U^T
$$
