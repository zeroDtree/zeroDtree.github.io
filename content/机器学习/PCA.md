---
title: PCA（主成分分析）
tags:
  - 线性代数
  - 统计
---

## 目标

在列正交约束下，将中心化后的数据投影到 $k$ 维子空间，使投影后的数据方差最大。

## 设定与样本方差

设数据矩阵 $X \in \mathbb{R}^{n \times p}$，其中 $n$ 是样本数，$p$ 是特征数。第 $i$ 个样本记为列向量 $\mathbf{x}_i \in \mathbb{R}^p$，$X$ 的第 $i$ 行为 $\mathbf{x}_i^T$：

$$
X = \begin{pmatrix}
\mathbf{x}_1^T \\
\vdots \\
\mathbf{x}_n^T
\end{pmatrix}.
$$

样本均值、中心化数据矩阵与样本协方差矩阵分别定义为

$$
\bar{\mathbf{x}} := \frac{1}{n} \sum_{i=1}^n \mathbf{x}_i,
\qquad
\tilde{X} := X - \mathbf{1}_n \bar{\mathbf{x}}^T,
\qquad
\Sigma := \frac{1}{n-1} \tilde{X}^T \tilde{X},
$$

其中 $\mathbf{1}_n \in \mathbb{R}^n$ 为全 $1$ 列向量。

由于 $\Sigma \in \mathbb{R}^{p \times p}$ 是实对称半正定矩阵，可作正交特征分解

$$
\Sigma = Q \Lambda Q^T,
\qquad
\Lambda = \operatorname{diag}(\lambda_1, \lambda_2, \ldots, \lambda_p),
$$

其中 $Q = [\mathbf{q}_1, \ldots, \mathbf{q}_p]$ 为正交矩阵，第 $i$ 列 $\mathbf{q}_i$ 是特征值 $\lambda_i$ 对应的单位特征向量，且特征值按降序排列：

$$
\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_p \ge 0.
$$

**命题。** 对任意单位向量 $\mathbf{w} \in \mathbb{R}^p$（$\|\mathbf{w}\|_2 = 1$），各样本在 $\mathbf{w}$ 方向上的投影 $X\mathbf{w} \in \mathbb{R}^n$ 的样本均值为 $\bar{\mathbf{x}}^T \mathbf{w}$，样本方差为

$$
s^2(\mathbf{w}) = \mathbf{w}^T \Sigma \mathbf{w}.
$$

> [!note]- 证明
> $X\mathbf{w}$ 的第 $i$ 个分量为 $(X\mathbf{w})_i = \mathbf{x}_i^T \mathbf{w}$，故投影后的样本均值为
>
> $$
> \frac{1}{n} \sum_{i=1}^n (X\mathbf{w})_i
> = \frac{1}{n} \sum_{i=1}^n \mathbf{x}_i^T \mathbf{w}
> = \bar{\mathbf{x}}^T \mathbf{w}.
> $$
>
> 代入样本方差定义，并利用 $\tilde{X} = X - \mathbf{1}_n \bar{\mathbf{x}}^T$，有
>
> $$
> \begin{aligned}
> s^2(\mathbf{w})
> &= \frac{1}{n-1} (X\mathbf{w} - \mathbf{1}_n \bar{\mathbf{x}}^T \mathbf{w})^T (X\mathbf{w} - \mathbf{1}_n \bar{\mathbf{x}}^T \mathbf{w}) \\
> &= \frac{1}{n-1} (\tilde{X}\mathbf{w})^T (\tilde{X}\mathbf{w}) \\
> &= \mathbf{w}^T \left( \frac{1}{n-1} \tilde{X}^T \tilde{X} \right) \mathbf{w} \\
> &= \mathbf{w}^T \Sigma \mathbf{w}. \quad \square
> \end{aligned}
> $$

## 主成分方向

**命题（第一主成分）。** 一维投影方差的最大值为

$$
\max_{\|\mathbf{w}\|_2 = 1} \mathbf{w}^T \Sigma \mathbf{w} = \lambda_1,
$$

在第一主成分方向 $\mathbf{w}_1 = \pm \mathbf{q}_1$ 处达到。若 $\lambda_1 > \lambda_2$，最大值当且仅当 $\mathbf{w} = \pm \mathbf{q}_1$ 时取到；若 $\lambda_1$ 有重根，则最大值在 $\lambda_1$ 对应的整个特征子空间中的任意单位向量上取到。

> [!note]- 证明
> 令 $\mathbf{z} := Q^T \mathbf{w}$。因为 $Q$ 是正交矩阵，所以 $\|\mathbf{z}\|_2 = \|\mathbf{w}\|_2 = 1$，即 $\sum_{i=1}^p z_i^2 = 1$。代入目标函数得
>
> $$
> \mathbf{w}^T \Sigma \mathbf{w}
> = \mathbf{w}^T Q \Lambda Q^T \mathbf{w}
> = \mathbf{z}^T \Lambda \mathbf{z}
> = \sum_{i=1}^p \lambda_i z_i^2
> \le \lambda_1 \sum_{i=1}^p z_i^2
> = \lambda_1.
> $$
>
> 当 $z_1 = \pm 1$ 且 $z_2 = \cdots = z_p = 0$，即 $\mathbf{z} = \pm \mathbf{e}_1$ 时上界达到，此时
>
> $$
> \mathbf{w} = Q \mathbf{z} = \pm Q \mathbf{e}_1 = \pm \mathbf{q}_1.
> $$
>
> 上述不等式取等号当且仅当对所有满足 $\lambda_i < \lambda_1$ 的下标 $i$ 都有 $z_i = 0$，这等价于 $\mathbf{w}$ 属于 $\lambda_1$ 的特征子空间。特别地，当 $\lambda_1 > \lambda_2$ 时，有 $z_2 = \cdots = z_p = 0$，故 $\mathbf{w} = \pm \mathbf{q}_1$。$\square$

**命题（第 $j$ 主成分）。** 对 $1 \le j \le p$，记前 $j-1$ 个主成分方向为 $\mathbf{w}_1 = \mathbf{q}_1, \ldots, \mathbf{w}_{j-1} = \mathbf{q}_{j-1}$。则在与 $\mathbf{w}_1, \ldots, \mathbf{w}_{j-1}$ 均正交的单位向量中，投影方差的最大值为

$$
\max_{\substack{\|\mathbf{w}\|_2 = 1 \\ \mathbf{w} \perp \mathbf{w}_1, \ldots, \mathbf{w}_{j-1}}} \mathbf{w}^T \Sigma \mathbf{w} = \lambda_j,
$$

在第 $j$ 主成分方向 $\mathbf{w}_j = \pm \mathbf{q}_j$ 处达到。

> [!note]- 证明
> 令 $\mathbf{z} := Q^T \mathbf{w}$。对任意 $1 \le r \le j-1$，由 $Q^T \mathbf{q}_r = \mathbf{e}_r$ 及正交矩阵保内积，有
>
> $$
> z_r = \mathbf{e}_r^T \mathbf{z} = (Q^T \mathbf{q}_r)^T (Q^T \mathbf{w}) = \mathbf{q}_r^T \mathbf{w} = 0.
> $$
>
> 于是 $z_1 = \cdots = z_{j-1} = 0$，且 $\sum_{i=j}^p z_i^2 = \|\mathbf{z}\|_2^2 = 1$。从而
>
> $$
> \mathbf{w}^T \Sigma \mathbf{w}
> = \sum_{i=j}^p \lambda_i z_i^2
> \le \lambda_j \sum_{i=j}^p z_i^2
> = \lambda_j.
> $$
>
> 当 $\mathbf{z} = \pm \mathbf{e}_j$，即 $\mathbf{w} = \pm Q \mathbf{e}_j = \pm \mathbf{q}_j$ 时达到最大值 $\lambda_j$。$\square$

## $k$ 维子空间投影

**引理。** 设 $Z \in \mathbb{R}^{p \times k}$ 满足列正交约束 $Z^T Z = I_k$，记其第 $i$ 行的模长平方为

$$
c_i := \sum_{j=1}^k Z_{ij}^2 = (Z Z^T)_{ii},
\qquad i = 1, \ldots, p.
$$

则对所有 $1 \le i \le p$ 有 $0 \le c_i \le 1$，且 $\sum_{i=1}^p c_i = k$。

> [!note]- 证明
> 非负性 $c_i \ge 0$ 显然。因为 $Z$ 的 $k$ 个列向量标准正交，可将 $Z$ 扩充为正交矩阵 $\tilde{Z} = [Z, Z_\perp] \in \mathbb{R}^{p \times p}$。正交矩阵的每一行也是单位向量，故对任意 $1 \le i \le p$，
>
> $$
> c_i = \sum_{j=1}^k Z_{ij}^2 \le \sum_{j=1}^p \tilde{Z}_{ij}^2 = 1.
> $$
>
> 对 $i = 1, \ldots, p$ 求和得
>
> $$
> \sum_{i=1}^p c_i = \sum_{i=1}^p \sum_{j=1}^k Z_{ij}^2 = \operatorname{tr}(Z^T Z) = \operatorname{tr}(I_k) = k. \quad \square
> $$

**定理（$k$ 维主子空间投影）。** 对满足列正交约束 $W^T W = I_k$ 的投影矩阵 $W = [\mathbf{w}_1, \ldots, \mathbf{w}_k] \in \mathbb{R}^{p \times k}$，投影后的总方差最大值为

$$
\max_{W^T W = I_k} \operatorname{tr}(W^T \Sigma W) = \sum_{i=1}^k \lambda_i,
$$

当取 $W = [\mathbf{q}_1, \ldots, \mathbf{q}_k]$ 时达到最大值。此时中心化数据在 $k$ 维主子空间上的投影坐标为 $\tilde{X} W \in \mathbb{R}^{n \times k}$。

> [!note]- 证明
> 记 $Z := Q^T W = [\mathbf{z}_1, \ldots, \mathbf{z}_k] \in \mathbb{R}^{p \times k}$，则 $Z^T Z = W^T Q Q^T W = I_k$。注意到 $Z^T \Lambda Z$ 的第 $j$ 个对角元为
>
> $$
> (Z^T \Lambda Z)_{jj}
> = \mathbf{z}_j^T \Lambda \mathbf{z}_j
> = \sum_{i=1}^p \lambda_i Z_{ij}^2,
> $$
>
> 故投影到 $k$ 个正交方向后的总方差为
>
> $$
> \begin{aligned}
> \sum_{j=1}^k s^2(\mathbf{w}_j)
> &= \sum_{j=1}^k \mathbf{w}_j^T \Sigma \mathbf{w}_j \\
> &= \operatorname{tr}(W^T \Sigma W) \\
> &= \operatorname{tr}(Z^T \Lambda Z) \\
> &= \sum_{j=1}^k (Z^T \Lambda Z)_{jj} \\
> &= \sum_{j=1}^k \sum_{i=1}^p \lambda_i Z_{ij}^2 \\
> &= \sum_{i=1}^p \lambda_i \left( \sum_{j=1}^k Z_{ij}^2 \right) \\
> &= \sum_{i=1}^p \lambda_i c_i,
> \end{aligned}
> $$
>
> 其中 $c_i := \sum_{j=1}^k Z_{ij}^2$。由上引理知 $0 \le c_i \le 1$ 且 $\sum_{i=1}^p c_i = k$。结合 $\lambda_1 \ge \cdots \ge \lambda_p \ge 0$，有
>
> $$
> \begin{aligned}
> \sum_{i=1}^k \lambda_i - \sum_{i=1}^p \lambda_i c_i
> &= \sum_{i=1}^k \lambda_i (1 - c_i) - \sum_{i=k+1}^p \lambda_i c_i \\
> &\ge \lambda_k \sum_{i=1}^k (1 - c_i) - \lambda_k \sum_{i=k+1}^p c_i \\
> &= \lambda_k \left( k - \sum_{i=1}^p c_i \right) = 0,
> \end{aligned}
> $$
>
> 因此
>
> $$
> \operatorname{tr}(W^T \Sigma W)
> = \sum_{i=1}^p \lambda_i c_i
> \le \sum_{i=1}^k \lambda_i.
> $$
>
> 当取 $W = [\mathbf{q}_1, \ldots, \mathbf{q}_k]$ 时，$Z = Q^T W = [I_k, 0]^T$，故 $c_1 = \cdots = c_k = 1$，$c_{k+1} = \cdots = c_p = 0$，上界 $\sum_{i=1}^k \lambda_i$ 达到。$\square$

此外，由于 $\Sigma = \frac{1}{n-1}\tilde{X}^T \tilde{X}$，$\Sigma$ 的正交特征向量 $\mathbf{q}_1, \ldots, \mathbf{q}_p$ 就是中心化数据矩阵 $\tilde{X}$ 的右奇异向量。
