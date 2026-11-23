---
title: Rayleigh 商
tags:
  - 线性代数
  - 最优化
  - 机器学习
date: 2026-11-22
---

## 前置

- [[机器学习/广义特征值|广义特征值问题（GEP）]]

## 定义

设 $A,B\in\mathbb{R}^{d\times d}$ 实对称。对使 $\mathbf{w}^\top B\mathbf{w}\ne0$ 的非零 $\mathbf{w}$，定义 Rayleigh 商

$$
\rho(\mathbf{w})
=\frac{\mathbf{w}^\top A\mathbf{w}}{\mathbf{w}^\top B\mathbf{w}}.
$$

$B\succ0$ 时，所有非零 $\mathbf{w}$ 都满足分母为正；$B$ 半正定但奇异时，$\ker B$ 中的方向不在定义域内。$B=I$ 时退化为普通 Rayleigh 商。

## 变分刻画

设 $\lambda_1\le\cdots\le\lambda_d$ 为 $(A,B)$ 的广义特征值，$\mathbf{v}_j$ 为对应的 $B$-标准正交特征向量，即 $\mathbf{v}_i^\top B\mathbf{v}_j=\delta_{ij}$。取 $B=SS^\top$，并令

$$
\tilde A=S^{-1}AS^{-\top}=Q\Lambda Q^\top,
$$

其中 $Q$ 正交，$\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_d)$；记 $Q=[\mathbf{q}_1,\ldots,\mathbf{q}_d]$，则 $\mathbf{v}_j=S^{-\top}\mathbf{q}_j$。

> [!abstract] 命题（单个方向的极值）
> 设 $A$ 实对称，$B\succ0$。对任意非零 $\mathbf{w}$，
>
> $$
> \lambda_1\le\rho(\mathbf{w})\le\lambda_d.
> $$
>
> 下界在 $\lambda_1$ 的特征子空间中达到，上界在 $\lambda_d$ 的特征子空间中达到。
>
> > [!note]- 证明
> > 令 $\mathbf{u}=S^\top\mathbf{w}$，$\mathbf{z}=Q^\top\mathbf{u}$，则 $\mathbf{u}=Q\mathbf{z}$。由 $B=SS^\top$，
> >
> > $$
> > \mathbf{w}^\top B\mathbf{w}
> > =\mathbf{w}^\top SS^\top\mathbf{w}
> > =\mathbf{u}^\top\mathbf{u}
> > =\mathbf{z}^\top Q^\top Q\mathbf{z}
> > =\mathbf{z}^\top\mathbf{z}
> > =\sum_i z_i^2.
> > $$
> >
> > 由 $A=S\tilde A S^\top$ 与 $\tilde A=Q\Lambda Q^\top$，
> >
> > $$
> > \begin{aligned}
> > \mathbf{w}^\top A\mathbf{w}
> > &=\mathbf{w}^\top S\tilde A S^\top\mathbf{w}
> > =\mathbf{u}^\top\tilde A\mathbf{u}\\
> > &=\mathbf{z}^\top Q^\top\tilde A Q\mathbf{z}
> > =\mathbf{z}^\top\Lambda\mathbf{z}
> > =\sum_i\lambda_i z_i^2.
> > \end{aligned}
> > $$
> >
> > 因此
> >
> > $$
> > \rho(\mathbf{w})
> > =\frac{\mathbf{w}^\top A\mathbf{w}}{\mathbf{w}^\top B\mathbf{w}}
> > =\frac{\mathbf{z}^\top\Lambda\mathbf{z}}{\mathbf{z}^\top\mathbf{z}}
> > =\frac{\sum_i\lambda_i z_i^2}{\sum_i z_i^2}.
> > $$
> >
> > 这是 $\lambda_i$ 的加权平均，故位于 $[\lambda_1,\lambda_d]$。取 $\mathbf{z}=\pm\mathbf{e}_1$ 或 $\pm\mathbf{e}_d$ 即分别达到下界与上界；重根时对应特征子空间中的任意 $B$-单位向量都可取。$\square$

> [!abstract] 命题（逐次变分）
> 设前 $j-1$ 个方向取为 $\mathbf{v}_1,\ldots,\mathbf{v}_{j-1}$。则
>
> $$
> \min_{\substack{\mathbf{w}^\top B\mathbf{w}=1\\ \mathbf{v}_r^\top B\mathbf{w}=0,\ r<j}}
> \mathbf{w}^\top A\mathbf{w}
> =\lambda_j.
> $$
>
> 等号当且仅当 $\mathbf{w}\in\operatorname{span}\{\mathbf{v}_i:i\ge j,\ \lambda_i=\lambda_j\}$ 且 $\|\mathbf{w}\|_B=1$。单根时 $\mathbf{w}=\pm\mathbf{v}_j$；重根时可在对应特征子空间中任取 $B$-标准正交基。
>
> > [!note]- 证明
> > 令 $\mathbf{u}=S^\top\mathbf{w}$，$\mathbf{z}=Q^\top\mathbf{u}$。约束 $\mathbf{w}^\top B\mathbf{w}=1$ 等价于 $\|\mathbf{z}\|_2=1$；又
> >
> > $$
> > \mathbf{v}_r^\top B\mathbf{w}
> > =\mathbf{q}_r^\top S^{-1}SS^\top S^{-\top}\mathbf{u}
> > =z_r,
> > $$
> >
> > 故前 $j-1$ 个约束等价于 $z_1=\cdots=z_{j-1}=0$。于是
> >
> > $$
> > \mathbf{w}^\top A\mathbf{w}
> > =\sum_{i=j}^d\lambda_i z_i^2
> > \ge\lambda_j\sum_{i=j}^d z_i^2
> > =\lambda_j.
> > $$
> >
> > 等号当且仅当对所有 $\lambda_i>\lambda_j$ 的 $i$ 有 $z_i=0$，即 $\mathbf{w}\in\operatorname{span}\{\mathbf{v}_i:i\ge j,\ \lambda_i=\lambda_j\}$。这里“剩余”是指前 $j-1$ 个方向已被约束排除，只保留 $i\ge j$ 的部分；单根时只剩 $\mathbf{v}_j$。$\mathbf{z}=\pm\mathbf{e}_j$ 达到下界，对应 $\mathbf{w}=\pm\mathbf{v}_j$。$\square$

## 矩阵形式

> [!abstract] 定理（矩阵形式的最小值）
> 设 $A$ 实对称，$B\succ0$，$1\le m\le d$。则
>
> $$
> \min_{W^\top BW=I_m}\operatorname{tr}(W^\top AW)=\sum_{j=1}^m\lambda_j.
> $$
>
> 最小值在 $W=[\mathbf{v}_1,\ldots,\mathbf{v}_m]$ 处达到。
>
> > [!note]- 证明
> > 令 $U=S^\top W$，$Z=Q^\top U$。由 $W^\top BW=I_m$ 与 $B=SS^\top$，
> >
> > $$
> > U^\top U
> > =W^\top SS^\top W
> > =W^\top BW
> > =I_m.
> > $$
> >
> > 又因 $Q$ 正交，
> >
> > $$
> > Z^\top Z
> > =U^\top QQ^\top U
> > =U^\top U
> > =I_m.
> > $$
> >
> > 记 $c_i=\sum_{j=1}^m Z_{ij}^2$。因为 $Z^\top Z=I_m$，$Z$ 的 $m$ 个列向量标准正交，可将其补全为 $d\times d$ 正交矩阵 $\widetilde Z=[Z,Z_\perp]$。补全后每一行的平方和为 $1$，而前 $m$ 项的平方和正是 $c_i$，所以
> >
> > $$
> > 0\le c_i\le1.
> > $$
> >
> > 另一方面，
> >
> > $$
> > \sum_i c_i
> > =\sum_{i=1}^d\sum_{j=1}^m Z_{ij}^2
> > =\operatorname{tr}(Z^\top Z)
> > =\operatorname{tr}(I_m)
> > =m.
> > $$
> >
> > 由 $A=S\tilde A S^\top$ 与 $\tilde A=Q\Lambda Q^\top$，
> >
> > $$
> > \begin{aligned}
> > W^\top AW
> > &=W^\top S\tilde A S^\top W
> > =U^\top\tilde A U\\
> > &=U^\top Q\Lambda Q^\top U
> > =Z^\top\Lambda Z,
> > \end{aligned}
> > $$
> >
> > 因为 $W^\top AW=Z^\top\Lambda Z$，两者迹相等。由 $\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_d)$，
> >
> > $$
> > \begin{aligned}
> > \operatorname{tr}(Z^\top\Lambda Z)
> > &=\sum_{j=1}^m (Z^\top\Lambda Z)_{jj}\\
> > &=\sum_{j=1}^m\sum_{i=1}^d Z_{ij}\lambda_i Z_{ij}\\
> > &=\sum_{i=1}^d\lambda_i\sum_{j=1}^m Z_{ij}^2\\
> > &=\sum_{i=1}^d\lambda_i c_i.
> > \end{aligned}
> > $$
> >
> > 故 $\operatorname{tr}(W^\top AW)=\sum_{i=1}^d\lambda_i c_i$。
> >
> > 因 $\lambda_1\le\cdots\le\lambda_d$，
> >
> > $$
> > \begin{aligned}
> > \sum_i\lambda_i c_i-\sum_{i=1}^m\lambda_i
> > &=\sum_{i=1}^m\lambda_i(c_i-1)+\sum_{i=m+1}^d\lambda_i c_i\\
> > &\ge\lambda_m\sum_{i=1}^m(c_i-1)+\lambda_m\sum_{i=m+1}^d c_i\\
> > &=\lambda_m\left(\sum_i c_i-m\right)=0.
> > \end{aligned}
> > $$
> >
> > 不等号逐项得到：当 $i\le m$ 时，$c_i-1\le0$ 且 $\lambda_i\le\lambda_m$，乘以非正数后不等号反向，故 $\lambda_i(c_i-1)\ge\lambda_m(c_i-1)$；当 $i>m$ 时，$c_i\ge0$ 且 $\lambda_i\ge\lambda_m$，故 $\lambda_i c_i\ge\lambda_m c_i$。两段求和即得。故下界为 $\sum_{j=1}^m\lambda_j$。
> >
> > 取 $W=[\mathbf{v}_1,\ldots,\mathbf{v}_m]$。由 $\mathbf{v}_j=S^{-\top}\mathbf{q}_j$，
> >
> > $$
> > Z=Q^\top S^\top W
> > =Q^\top S^\top S^{-\top}[\mathbf{q}_1,\ldots,\mathbf{q}_m]
> > =[\mathbf{e}_1,\ldots,\mathbf{e}_m],
> > $$
> >
> > 故 $c_1=\cdots=c_m=1$，$c_{m+1}=\cdots=c_d=0$。于是
> >
> > $$
> > \operatorname{tr}(W^\top AW)
> > =\sum_{i=1}^m\lambda_i,
> > $$
> >
> > 且 $W^\top BW=I_m$，所以下界达到。$\square$

> [!abstract] 命题（矩阵形式的最大值）
> 设 $A$ 实对称，$B\succ0$，$1\le m\le d$。则
>
> $$
> \max_{W^\top BW=I_m}\operatorname{tr}(W^\top AW)=\sum_{i=d-m+1}^d\lambda_i.
> $$
>
> 最大值在 $W=[\mathbf{v}_{d-m+1},\ldots,\mathbf{v}_d]$ 处达到。
>
> > [!note]- 证明
> > 对 $-A$ 用最小值定理。$-A$ 的广义特征值按升序为
> >
> > $$
> > -\lambda_d\le\cdots\le-\lambda_1,
> > $$
> >
> > 对应的特征向量为 $\mathbf{v}_d,\ldots,\mathbf{v}_1$。因此
> >
> > $$
> > \min_{W^\top BW=I_m}\operatorname{tr}(W^\top(-A)W)
> > =\sum_{j=1}^m(-\lambda_{d-j+1})
> > =-\sum_{i=d-m+1}^d\lambda_i.
> > $$
> >
> > 又 $\operatorname{tr}(W^\top(-A)W)=-\operatorname{tr}(W^\top AW)$，故
> >
> > $$
> > \max_{W^\top BW=I_m}\operatorname{tr}(W^\top AW)
> > =\sum_{i=d-m+1}^d\lambda_i.
> > $$
> >
> > 最小值定理中，$-A$ 的最小值在 $W=[\mathbf{v}_d,\ldots,\mathbf{v}_{d-m+1}]$ 处达到；它与 $[\mathbf{v}_{d-m+1},\ldots,\mathbf{v}_d]$ 只差列的顺序，因此最大值也在后者处达到。$\square$

## 逐次变分与矩阵形式的关系

逐次变分和矩阵形式不是同一个优化问题，但在最优值和最优子空间上等价。

逐次变分给出

$$
\lambda_j
=\min_{\substack{\mathbf{w}^\top B\mathbf{w}=1\\ \mathbf{v}_r^\top B\mathbf{w}=0,\ r<j}}
\mathbf{w}^\top A\mathbf{w},
$$

而矩阵形式给出

$$
\min_{W^\top BW=I_m}\operatorname{tr}(W^\top AW)
=\sum_{j=1}^m\lambda_j.
$$

两者最优值相同；逐次变分得到的 $W=[\mathbf{v}_1,\ldots,\mathbf{v}_m]$ 是矩阵形式的一个最优解。

差别在于矩阵形式只确定最优子空间，不唯一确定各列。若 $W$ 最优，则对任意正交矩阵 $Q\in\mathbb{R}^{m\times m}$，$\widetilde W=WQ$ 仍满足约束，且迹不变：

$$
\widetilde W^\top B\widetilde W=I_m,
\qquad
\operatorname{tr}(\widetilde W^\top A\widetilde W)
=\operatorname{tr}(W^\top AW).
$$

所以矩阵形式允许最优子空间内的正交混合甚至列交换；逐次变分额外要求方向按 $\lambda_1\le\cdots\le\lambda_m$ 嵌套排列。若只关心总目标值或最优子空间，两者等价；若要得到有序的第 $1$、第 $2$、……个慢特征方向，应使用逐次变分，或在得到最优子空间后再对角化 $W^\top AW$。


## 约束优化视角

约束二次规划也会导出同一特征值方程。

> [!abstract] 命题（约束二次规划与 Rayleigh 商）
> 设 $A$ 实对称，$B\succ0$。约束问题
>
> $$
> \min_{\mathbf{w}}\ \mathbf{w}^\top A\mathbf{w}
> \quad\text{s.t.}\quad \mathbf{w}^\top B\mathbf{w}=1
> $$
>
> 的驻点与广义特征向量等价：$\mathbf{w}$ 是约束问题的驻点，当且仅当存在 $\lambda$ 使 $A\mathbf{w}=\lambda B\mathbf{w}$ 且 $\mathbf{w}^\top B\mathbf{w}=1$；此时 $\lambda=\rho(\mathbf{w})$。等价地，$\rho$ 的驻点也正好是这些广义特征向量。
>
> > [!note]- 证明
> > 令 $\mathcal{L}=\mathbf{w}^\top A\mathbf{w}-\lambda(\mathbf{w}^\top B\mathbf{w}-1)$。由 $A,B$ 对称，
> >
> > $$
> > \nabla_{\mathbf{w}}\mathcal{L}=2A\mathbf{w}-2\lambda B\mathbf{w}.
> > $$
> >
> > 驻点条件给出 $A\mathbf{w}=\lambda B\mathbf{w}$；左乘 $\mathbf{w}^\top$ 并代入约束得 $\lambda=\rho(\mathbf{w})$。反之，若 $A\mathbf{w}=\lambda B\mathbf{w}$ 且 $\mathbf{w}^\top B\mathbf{w}=1$，则 $\nabla_{\mathbf{w}}\mathcal{L}=0$，所以它也是约束驻点。
> >
> > 另一方面，用 [[机器学习/矩阵微分演算|矩阵微分演算]] 中的标量微分计算 $\rho$。由 $A,B$ 对称，
> >
> > $$
> > d(\mathbf{w}^\top A\mathbf{w})=2\mathbf{w}^\top A\,d\mathbf{w},
> > \qquad
> > d(\mathbf{w}^\top B\mathbf{w})=2\mathbf{w}^\top B\,d\mathbf{w}.
> > $$
> >
> > 由商法则，
> >
> > $$
> > \begin{aligned}
> > d\rho
> > &=\frac{d(\mathbf{w}^\top A\mathbf{w})}{\mathbf{w}^\top B\mathbf{w}}
> > -\frac{(\mathbf{w}^\top A\mathbf{w})\,d(\mathbf{w}^\top B\mathbf{w})}{(\mathbf{w}^\top B\mathbf{w})^2}\\
> > &=\frac{2}{\mathbf{w}^\top B\mathbf{w}}
> > \left(\mathbf{w}^\top A-\rho(\mathbf{w})\mathbf{w}^\top B\right)d\mathbf{w}\\
> > &=\frac{2}{\mathbf{w}^\top B\mathbf{w}}
> > \left(A\mathbf{w}-\rho(\mathbf{w})B\mathbf{w}\right)^\top d\mathbf{w}.
> > \end{aligned}
> > $$
> >
> > 对照 $dl=(\nabla l)^\top d\mathbf{w}$，得
> >
> > $$
> > \nabla\rho(\mathbf{w})
> > =\frac{2}{\mathbf{w}^\top B\mathbf{w}}\left(A\mathbf{w}-\rho(\mathbf{w})B\mathbf{w}\right).
> > $$
> >
> > 故 $\nabla\rho(\mathbf{w})=\mathbf{0}$ 与 $A\mathbf{w}=\rho(\mathbf{w})B\mathbf{w}$ 等价。$\square$
