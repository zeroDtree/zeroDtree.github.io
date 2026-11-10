---
title: 时间滞后独立成分分析（TICA）
tags:
 - 线性代数
 - 统计
 - 机器学习
date: 2026-11-10
---

## 前置

- [[机器学习/SFA|慢特征分析（SFA）]]

## 目标

给定中心化时间序列 $\mathbf{x}(t) \in \mathbb{R}^d$ 与滞后 $\tau > 0$，在单位方差与 $C_0$-正交约束下，依次寻找使投影信号滞后自相关最大的线性方向。

## 设定

时间平均 $\langle \cdot \rangle_t$ 与概率测度 $\mu_T$ 沿用 [[机器学习/SFA|慢特征分析（SFA）]]。给定滞后 $\tau > 0$，滞后量只在 $t$ 与 $t+\tau$ 同时属于 $T$ 时有定义。记

$$
T_\tau := \{ t \in T : t+\tau \in T \},
$$

并设 $\mu_T(T_\tau) > 0$。滞后平均是 $\mu_T$ 在 $T_\tau$ 上的归一化限制：

$$
\langle f(t) \rangle_{t,\tau}
:=
\frac{1}{\mu_T(T_\tau)}
\int_{T_\tau} f(t)\,\mu_T(\mathrm{d}t).
$$

下文的 $C_0$、$C_\tau$ 与差分协方差都使用这一平均，左右端点来自同一批配对。过程二阶平稳且平均改为关于平稳分布的期望时，端点效应消失，该平均与全时段平均给出同一二阶矩。

设 $\mathbf{x}$ 在配对窗口上已中心化，且各分量平方可积：

$$
\langle \mathbf{x}(t) \rangle_{t,\tau} = \mathbf{0},
\qquad
\mathbf{x}(t),\, \mathbf{x}(t+\tau) \in L^2(T_\tau, \mu_{T_\tau}; \mathbb{R}^d).
$$

## 滞后协方差

定义零滞后协方差、滞后协方差、右端协方差及其对称部分：

$$
\begin{aligned}
C_0
&:=
\left\langle \mathbf{x}(t)\mathbf{x}(t)^\top \right\rangle_{t,\tau},
\\
C_\tau
&:=
\left\langle \mathbf{x}(t)\mathbf{x}(t+\tau)^\top \right\rangle_{t,\tau},
\\
C_{\tau\tau}
&:=
\left\langle \mathbf{x}(t+\tau)\mathbf{x}(t+\tau)^\top \right\rangle_{t,\tau},
\\
C_\tau^{\mathrm{sym}}
&:=
\frac{1}{2}\left( C_\tau + C_\tau^\top \right).
\end{aligned}
$$

$C_0$ 与 $C_{\tau\tau}$ 实对称半正定。$C_\tau$ 一般不对称：$C_\tau^\top = \langle \mathbf{x}(t+\tau)\mathbf{x}(t)^\top \rangle_{t,\tau}$ 把时间方向反过来。称二阶平稳，若 $C_{\tau\tau} = C_0$。

> [!abstract] 命题（二次型只依赖对称部分）
> 对任意 $\mathbf{w} \in \mathbb{R}^d$ 与任意 $M \in \mathbb{R}^{d \times d}$，
>
> $$
> \mathbf{w}^\top M \mathbf{w} = \mathbf{w}^\top M^\top \mathbf{w} = \mathbf{w}^\top \frac{M + M^\top}{2}\, \mathbf{w}.
> $$
>
> 特别地，$\mathbf{w}^\top C_\tau \mathbf{w} = \mathbf{w}^\top C_\tau^{\mathrm{sym}} \mathbf{w}$。
>
> > [!note]- 证明
> > $\mathbf{w}^\top M \mathbf{w}$ 是标量，等于自身的转置：
> >
> > $$
> > \mathbf{w}^\top M \mathbf{w} = \left( \mathbf{w}^\top M \mathbf{w} \right)^\top = \mathbf{w}^\top M^\top \mathbf{w}.
> > $$
> >
> > 两式取算术平均即得对称部分的二次型。将 $M$ 换为 $C_\tau$ 得到后一式。$\square$

单个实值投影的滞后乘积平均因此不区分 $C_\tau$ 与 $C_\tau^{\mathrm{sym}}$。反对称部分 $\frac{1}{2}(C_\tau - C_\tau^\top)$ 对一切实二次型贡献为零；它进入非对称的向量传播，见后文可逆性。

## 自相关与优化问题

对线性投影 $y(t) = \mathbf{w}^\top \mathbf{x}(t)$，在 $\mathbf{w}^\top C_0 \mathbf{w} > 0$ 时定义滞后自相关

$$
\rho_\tau(\mathbf{w})
:=
\frac{\langle y(t)\, y(t+\tau) \rangle_{t,\tau}}{\langle y(t)^2 \rangle_{t,\tau}}
=
\frac{\mathbf{w}^\top C_\tau^{\mathrm{sym}} \mathbf{w}}{\mathbf{w}^\top C_0 \mathbf{w}}.
$$

这是 $C_\tau^{\mathrm{sym}}$ 相对 $C_0$ 的广义 Rayleigh 商。

> [!abstract] 命题（齐次性：Rayleigh 商与单位方差约束等价）
> 设 $C_0 \succ 0$。则 $\rho_\tau$ 零次齐次：对任意 $c \neq 0$ 与 $\mathbf{w} \neq \mathbf{0}$，$\rho_\tau(c\mathbf{w}) = \rho_\tau(\mathbf{w})$，并且
>
> $$
> \max_{\mathbf{w} \neq \mathbf{0}} \rho_\tau(\mathbf{w}) = \max_{\mathbf{w}^\top C_0 \mathbf{w} = 1} \mathbf{w}^\top C_\tau^{\mathrm{sym}} \mathbf{w}.
> $$
>
> 两边的最优方向相同，相差一个非零倍数。若只知 $C_0 \succeq 0$，Rayleigh 商在 $\ker C_0$ 上无定义。可行集改为 $\{ \mathbf{w} : \mathbf{w}^\top C_0 \mathbf{w} > 0 \}$，或先由 [[机器学习/PCA|PCA]] 投影到 $C_0$ 的正特征子空间，再在该子空间上使用正定情形。
>
> > [!note]- 证明
> > 对 $c \neq 0$，
> >
> > $$
> > \rho_\tau(c\mathbf{w})
> > =
> > \frac{(c\mathbf{w})^\top C_\tau^{\mathrm{sym}} (c\mathbf{w})}{(c\mathbf{w})^\top C_0 (c\mathbf{w})}
> > =
> > \frac{c^2\, \mathbf{w}^\top C_\tau^{\mathrm{sym}} \mathbf{w}}{c^2\, \mathbf{w}^\top C_0 \mathbf{w}}
> > =
> > \rho_\tau(\mathbf{w}).
> > $$
> >
> > $C_0 \succ 0$ 时，任意 $\mathbf{w} \neq \mathbf{0}$ 满足 $\mathbf{w}^\top C_0 \mathbf{w} > 0$。取
> >
> > $$
> > \widetilde{\mathbf{w}}
> > :=
> > \frac{\mathbf{w}}{\sqrt{\mathbf{w}^\top C_0 \mathbf{w}}},
> > $$
> >
> > 则 $\widetilde{\mathbf{w}}^\top C_0 \widetilde{\mathbf{w}} = 1$，且
> >
> > $$
> > \widetilde{\mathbf{w}}^\top C_\tau^{\mathrm{sym}} \widetilde{\mathbf{w}}
> > = \rho_\tau(\widetilde{\mathbf{w}})
> > = \rho_\tau(\mathbf{w}).
> > $$
> >
> > 反过来，约束集中的每一点都是某个非零向量的缩放，目标值等于该向量的 Rayleigh 商。两边最大值相等，最优方向在非零缩放下对应。
> >
> > 若 $C_0 \succeq 0$ 且 $\mathbf{w} \in \ker C_0$，分母为零。$C_0$ 在其正特征子空间上的限制正定，前半部分在该子空间上适用。$\square$

线性 TICA 因此依次求解

$$
\begin{aligned}
\max_{\mathbf{w}_j \in \mathbb{R}^d} \quad & \mathbf{w}_j^\top C_\tau^{\mathrm{sym}} \mathbf{w}_j \\
\text{s.t.} \quad & \mathbf{w}_i^\top C_0 \mathbf{w}_j = \delta_{ij}, \qquad 1 \le i \le j.
\end{aligned}
$$

$i = j$ 时 $\mathbf{w}_j^\top C_0 \mathbf{w}_j = \langle y_j(t)^2 \rangle_{t,\tau} = 1$；$i < j$ 时 $\mathbf{w}_i^\top C_0 \mathbf{w}_j = \langle y_i(t) y_j(t) \rangle_{t,\tau} = 0$。正交由内积 $\langle \mathbf{u}, \mathbf{v} \rangle_{C_0} := \mathbf{u}^\top C_0 \mathbf{v}$ 给出，与 [[机器学习/SFA|SFA]] 中的 $B$-内积同一角色。取前 $m$ 个方向组成 $W_m = [\mathbf{w}_1, \ldots, \mathbf{w}_m]$，投影为 $\mathbf{z}(t) = W_m^\top \mathbf{x}(t)$。

## 广义特征值与白化求解

第一个方向是

$$
\max_{\mathbf{w}^\top C_0 \mathbf{w} = 1} \mathbf{w}^\top C_\tau^{\mathrm{sym}} \mathbf{w}.
$$

由 [[机器学习/拉格朗日乘子法|拉格朗日乘子法]]，令 $\mathcal{L}(\mathbf{w}, \lambda) = \mathbf{w}^\top C_\tau^{\mathrm{sym}} \mathbf{w} - \lambda(\mathbf{w}^\top C_0 \mathbf{w} - 1)$。两个矩阵都对称，驻点条件 $\nabla_{\mathbf{w}} \mathcal{L} = 2 C_\tau^{\mathrm{sym}} \mathbf{w} - 2\lambda C_0 \mathbf{w} = \mathbf{0}$ 给出

$$
C_\tau^{\mathrm{sym}} \mathbf{w} = \lambda C_0 \mathbf{w}.
$$

左乘 $\mathbf{w}^\top$ 并代入 $\mathbf{w}^\top C_0 \mathbf{w} = 1$，得 $\lambda = \mathbf{w}^\top C_\tau^{\mathrm{sym}} \mathbf{w} = \rho_\tau(\mathbf{w})$。$C_\tau^{\mathrm{sym}}$ 只保证对称，不保证半正定，广义特征值可以为负。目标是最大化自相关，故按特征值从大到小选取；[[机器学习/SFA|SFA]] 最小化导数二次型，取得的是最小特征值。

$C_0$ 奇异时，先用 [[机器学习/PCA|PCA]] 去掉 $\ker C_0$，再在正特征子空间上白化。以下三个命题设 $C_0 \succ 0$。

> [!abstract] 命题（白化变换）
> 设 $C_0 \succ 0$。定义
>
> $$
> \mathbf{u} := C_0^{1/2} \mathbf{w}
> \iff
> \mathbf{w} = C_0^{-1/2} \mathbf{u},
> \qquad
> K_\tau := C_0^{-1/2} C_\tau^{\mathrm{sym}} C_0^{-1/2}.
> $$
>
> 则 $\mathbf{w} \mapsto \mathbf{u}$ 是 $\mathbb{R}^d$ 上的双射，$K_\tau$ 实对称，且
>
> $$
> \mathbf{w}_i^\top C_0 \mathbf{w}_j = \delta_{ij} \iff \mathbf{u}_i^\top \mathbf{u}_j = \delta_{ij},
> \qquad
> \mathbf{w}^\top C_\tau^{\mathrm{sym}} \mathbf{w} = \mathbf{u}^\top K_\tau \mathbf{u}.
> $$
>
> $K_\tau$ 不必半正定。
>
> > [!note]- 证明
> > $C_0 \succ 0$ 实对称。由 [[机器学习/SFA|SFA]] 白化命题中的谱分解，存在对称正定平方根 $C_0^{1/2}$ 及其对称正定逆 $C_0^{-1/2}$，满足 $C_0^{1/2} C_0^{1/2} = C_0$、$C_0^{1/2} C_0^{-1/2} = I_d$ 与 $C_0^{-1/2} C_0 C_0^{-1/2} = I_d$。代入 $\mathbf{w}_j = C_0^{-1/2} \mathbf{u}_j$：
> >
> > $$
> > \begin{aligned}
> > \mathbf{w}_i^\top C_0 \mathbf{w}_j
> > &= \mathbf{u}_i^\top \left( C_0^{-1/2} C_0 C_0^{-1/2} \right) \mathbf{u}_j
> > = \mathbf{u}_i^\top \mathbf{u}_j, \\
> > \mathbf{w}^\top C_\tau^{\mathrm{sym}} \mathbf{w}
> > &= \mathbf{u}^\top \left( C_0^{-1/2} C_\tau^{\mathrm{sym}} C_0^{-1/2} \right) \mathbf{u}
> > = \mathbf{u}^\top K_\tau \mathbf{u}.
> > \end{aligned}
> > $$
> >
> > $C_0^{-1/2}$ 与 $C_\tau^{\mathrm{sym}}$ 都对称，故 $K_\tau^\top = K_\tau$。$\mathbf{z}^\top K_\tau \mathbf{z}$ 的符号与 $C_\tau^{\mathrm{sym}}$ 在 $\mathbf{w} = C_0^{-1/2} \mathbf{z}$ 上的二次型相同，可正可负。$\square$

> [!abstract] 命题（对称谱给出全部广义特征向量）
> 沿用上一命题的记号。实对称矩阵 $K_\tau$ 有正交特征分解 $K_\tau = Q \Lambda Q^\top$，其中 $Q = [\mathbf{q}_1, \ldots, \mathbf{q}_d]$，$Q^\top Q = I_d$，$\Lambda = \operatorname{diag}(\lambda_1, \ldots, \lambda_d)$，并按 $\lambda_1 \ge \cdots \ge \lambda_d$ 排列。令 $\mathbf{v}_j := C_0^{-1/2} \mathbf{q}_j$。则
>
> $$
> C_\tau^{\mathrm{sym}} \mathbf{v}_j = \lambda_j C_0 \mathbf{v}_j,
> \qquad
> \mathbf{v}_i^\top C_0 \mathbf{v}_j = \delta_{ij},
> \qquad
> \mathbf{v}_j^\top C_\tau^{\mathrm{sym}} \mathbf{v}_j = \lambda_j.
> $$
>
> > [!note]- 证明
> > 由 $K_\tau \mathbf{q}_j = \lambda_j \mathbf{q}_j$ 与 $\mathbf{q}_j = C_0^{1/2} \mathbf{v}_j$，
> >
> > $$
> > C_0^{-1/2} C_\tau^{\mathrm{sym}} C_0^{-1/2} C_0^{1/2} \mathbf{v}_j
> > = \lambda_j C_0^{1/2} \mathbf{v}_j.
> > $$
> >
> > 左乘 $C_0^{1/2}$，并用 $C_0^{1/2} C_0^{-1/2} = I_d$ 与 $C_0^{1/2} C_0^{1/2} = C_0$，得 $C_\tau^{\mathrm{sym}} \mathbf{v}_j = \lambda_j C_0 \mathbf{v}_j$。白化命题已给出 $\mathbf{v}_i^\top C_0 \mathbf{v}_j = \mathbf{q}_i^\top \mathbf{q}_j = \delta_{ij}$。再左乘 $\mathbf{v}_j^\top$ 得二次型等于 $\lambda_j$。$\square$

> [!abstract] 命题（逐次最大自相关）
> 沿用上述记号，特征值按降序 $\lambda_1 \ge \cdots \ge \lambda_d$。对 $1 \le j \le d$，若前 $j-1$ 个方向已取为 $\mathbf{w}_r = \mathbf{v}_r$（$1 \le r < j$），则
>
> $$
> \max_{\substack{\mathbf{w}^\top C_0 \mathbf{w} = 1 \\ \mathbf{v}_r^\top C_0 \mathbf{w} = 0,\, 1 \le r < j}}
> \mathbf{w}^\top C_\tau^{\mathrm{sym}} \mathbf{w}
> = \lambda_j.
> $$
>
> 最大值当且仅当 $\mathbf{w}$ 属于 $\operatorname{span}\{ \mathbf{v}_i : i \ge j,\ \lambda_i = \lambda_j \}$ 且 $\mathbf{w}^\top C_0 \mathbf{w} = 1$ 时达到。单根时最优方向在正负号意义下为 $\pm \mathbf{v}_j$；重根时，在该特征值余下的广义特征子空间中任取 $C_0$-标准正交方向。
>
> > [!note]- 证明
> > 白化把约束变成 $\mathbf{u}_r^\top \mathbf{u} = 0$（$r < j$）与 $\mathbf{u}^\top \mathbf{u} = 1$，目标变成 $\mathbf{u}^\top K_\tau \mathbf{u}$。令 $\mathbf{z} := Q^\top \mathbf{u}$。则
> >
> > $$
> > \mathbf{u}^\top K_\tau \mathbf{u}
> > = \mathbf{z}^\top \Lambda \mathbf{z}
> > = \sum_{i=1}^d \lambda_i z_i^2,
> > $$
> >
> > 并且 $z_r = \mathbf{q}_r^\top \mathbf{u} = 0$（$r < j$），$\sum_{i \ge j} z_i^2 = 1$。降序意味着 $i \ge j \Rightarrow \lambda_i \le \lambda_j$，故
> >
> > $$
> > \sum_{i \ge j} \lambda_i z_i^2
> > \le \lambda_j \sum_{i \ge j} z_i^2
> > = \lambda_j.
> > $$
> >
> > 差分等于 $\sum_{i \ge j} (\lambda_i - \lambda_j) z_i^2$。每一项 $\lambda_i - \lambda_j \le 0$，和为零当且仅当 $\lambda_i < \lambda_j$ 时 $z_i = 0$。因此 $\mathbf{u}$ 只含那些特征值等于 $\lambda_j$、下标不小于 $j$ 的特征向量。取 $\mathbf{z} = \pm \mathbf{e}_j$ 得 $\mathbf{u} = \pm \mathbf{q}_j$，即 $\mathbf{w} = \pm \mathbf{v}_j$，最大值 $\lambda_j$ 达到。单根时只剩 $z_j = \pm 1$。重根时，该特征值余下特征子空间中的任一单位向量都达到同一最大值；依次选取时可以任取一组欧氏标准正交基，逆白化后即为一组 $C_0$-标准正交基。$\square$

> [!abstract] 命题（矩阵形式：前 $m$ 个方向的总自相关）
> 沿用上述记号。对满足 $W^\top C_0 W = I_m$ 的 $W \in \mathbb{R}^{d \times m}$，
>
> $$
> \max_{W^\top C_0 W = I_m}
> \operatorname{tr}\!\left( W^\top C_\tau^{\mathrm{sym}} W \right)
> = \sum_{j=1}^m \lambda_j,
> $$
>
> 当 $W = [\mathbf{v}_1, \ldots, \mathbf{v}_m]$ 时达到。
>
> > [!note]- 证明
> > 令 $U := C_0^{1/2} W$。约束 $W^\top C_0 W = I_m$ 等价于 $U^\top U = I_m$。再令 $Z := Q^\top U$，则 $Z^\top Z = I_m$，并且
> >
> > $$
> > \begin{aligned}
> > \operatorname{tr}\!\left( W^\top C_\tau^{\mathrm{sym}} W \right)
> > &= \operatorname{tr}\!\left( U^\top K_\tau U \right)
> > = \operatorname{tr}\!\left( Z^\top \Lambda Z \right)
> > = \sum_{i=1}^d \lambda_i c_i,
> > \end{aligned}
> > $$
> >
> > 其中 $c_i := \sum_{j=1}^m Z_{ij}^2$。由 [[机器学习/PCA|PCA]] 中的引理（列正交矩阵的行范数性质），$0 \le c_i \le 1$ 且 $\sum_{i=1}^d c_i = m$。按降序 $\lambda_1 \ge \cdots \ge \lambda_d$，
> >
> > $$
> > \begin{aligned}
> > \sum_{i=1}^d \lambda_i c_i - \sum_{i=1}^m \lambda_i
> > &= \sum_{i=m+1}^d \lambda_i c_i - \sum_{i=1}^m \lambda_i (1 - c_i) \\
> > &\le \lambda_m \sum_{i=m+1}^d c_i - \lambda_m \sum_{i=1}^m (1 - c_i) \\
> > &= \lambda_m \left( \sum_{i=1}^d c_i - m \right)
> > = 0.
> > \end{aligned}
> > $$
> >
> > 不等号用到 $i > m$ 时 $\lambda_i \le \lambda_m$、$c_i \ge 0$，以及 $i \le m$ 时 $\lambda_i \ge \lambda_m$、$1 - c_i \ge 0$。这两处都不要求 $\lambda_i \ge 0$。故迹不超过 $\sum_{j=1}^m \lambda_j$。取 $W = [\mathbf{v}_1, \ldots, \mathbf{v}_m]$ 时，$U = [\mathbf{q}_1, \ldots, \mathbf{q}_m]$，$Z = [I_m,\, 0]^\top$，于是 $c_1 = \cdots = c_m = 1$，其余 $c_i = 0$，上界达到。$\square$

$\lambda_i < 0$ 表示对应投影在滞后 $\tau$ 上反相关。比较定理不把这些方向排除在外；只是它们不会被选进前 $m$ 个最大特征值，除非更大的特征值不足 $m$ 个。

## 与离散时间 SFA 的关系

[[机器学习/SFA|SFA]] 的离散形式用滞后差分代替时间导数。在同一滞后平均下，记 $y(t) = \mathbf{w}^\top \mathbf{x}(t)$ 与 $\Delta \mathbf{x}_\tau(t) := \mathbf{x}(t+\tau) - \mathbf{x}(t)$，

$$
\Delta_\tau(\mathbf{w})
:=
\left\langle \bigl( y(t+\tau) - y(t) \bigr)^2 \right\rangle_{t,\tau},
\qquad
A_\tau
:=
\left\langle \Delta \mathbf{x}_\tau(t)\, \Delta \mathbf{x}_\tau(t)^\top \right\rangle_{t,\tau}
\succeq 0.
$$

于是 $\Delta_\tau(\mathbf{w}) = \mathbf{w}^\top A_\tau \mathbf{w}$。离散 SFA 在 $W^\top C_0 W = I_m$ 下最小化总差分，广义特征值记为 $\mu$。这里的 $C_0$ 与 SFA 笔记中的 $B$ 是同一瞬时协方差在同一窗口上的两种记号。

> [!abstract] 命题（差分协方差与滞后协方差）
>
> $$
> A_\tau = C_{\tau\tau} + C_0 - 2 C_\tau^{\mathrm{sym}}.
> $$
>
> 若二阶平稳（$C_{\tau\tau} = C_0$），则 $A_\tau = 2(C_0 - C_\tau^{\mathrm{sym}})$。此时 $\mathbf{w}^\top C_0 \mathbf{w} = 1$ 已经推出 $\mathbf{w}^\top C_{\tau\tau} \mathbf{w} = 1$，并且
>
> $$
> \Delta_\tau(\mathbf{w}) = 2\bigl(1 - \rho_\tau(\mathbf{w})\bigr).
> $$
>
> 广义特征值问题 $A_\tau \mathbf{w} = \mu C_0 \mathbf{w}$ 与 $C_\tau^{\mathrm{sym}} \mathbf{w} = \lambda C_0 \mathbf{w}$ 的特征向量相同，特征值满足 $\mu = 2(1 - \lambda)$。最小化 $\mu$ 与最大化 $\lambda$ 选出同一组方向，排序相反。在该平稳性下 $\lambda \in [-1, 1]$，$\mu \in [0, 4]$。
>
> > [!note]- 证明
> > 展开差分外积：
> >
> > $$
> > \begin{aligned}
> > A_\tau
> > &= \left\langle
> > \bigl(\mathbf{x}(t+\tau) - \mathbf{x}(t)\bigr)
> > \bigl(\mathbf{x}(t+\tau) - \mathbf{x}(t)\bigr)^\top
> > \right\rangle_{t,\tau} \\
> > &= C_{\tau\tau} + C_0 - C_\tau - C_\tau^\top \\
> > &= C_{\tau\tau} + C_0 - 2 C_\tau^{\mathrm{sym}}.
> > \end{aligned}
> > $$
> >
> > $C_{\tau\tau} = C_0$ 时得到 $A_\tau = 2(C_0 - C_\tau^{\mathrm{sym}})$。对 $\mathbf{w}^\top C_0 \mathbf{w} = 1$，平稳性给出 $\mathbf{w}^\top C_{\tau\tau} \mathbf{w} = 1$，故
> >
> > $$
> > \Delta_\tau(\mathbf{w})
> > = 1 + 1 - 2\, \mathbf{w}^\top C_\tau^{\mathrm{sym}} \mathbf{w}
> > = 2\bigl(1 - \rho_\tau(\mathbf{w})\bigr).
> > $$
> >
> > 将 $A_\tau = 2(C_0 - C_\tau^{\mathrm{sym}})$ 代入 $A_\tau \mathbf{w} = \mu C_0 \mathbf{w}$：
> >
> > $$
> > 2(C_0 - C_\tau^{\mathrm{sym}}) \mathbf{w} = \mu C_0 \mathbf{w}
> > \iff
> > C_\tau^{\mathrm{sym}} \mathbf{w}
> > = \left(1 - \frac{\mu}{2}\right) C_0 \mathbf{w}.
> > $$
> >
> > 与 TICA 的特征值方程对照，$\lambda = 1 - \mu/2$，即 $\mu = 2(1 - \lambda)$。约束 $\mathbf{w}^\top C_0 \mathbf{w} = 1$ 与 $A_\tau \succeq 0$ 给出 $\mu = \mathbf{w}^\top A_\tau \mathbf{w} \ge 0$。由 $L^2(T_\tau)$ 上的柯西不等式，
> >
> > $$
> > \bigl| \langle y(t)\, y(t+\tau) \rangle_{t,\tau} \bigr|
> > \le
> > \sqrt{ \langle y(t)^2 \rangle_{t,\tau} \, \langle y(t+\tau)^2 \rangle_{t,\tau} }
> > = 1,
> > $$
> >
> > 故 $\lambda \in [-1, 1]$，从而 $\mu = 2(1 - \lambda) \in [0, 4]$。两个目标在同一约束集上只差正仿射变换 $\mu = 2(1 - \lambda)$，最小 $\mu$ 与最大 $\lambda$ 的特征向量一致，排序相反。$\square$

没有二阶平稳时，

$$
\Delta_\tau(\mathbf{w})
= \mathbf{w}^\top C_{\tau\tau} \mathbf{w} + \mathbf{w}^\top C_0 \mathbf{w} - 2\, \mathbf{w}^\top C_\tau^{\mathrm{sym}} \mathbf{w}.
$$

单位 $C_0$-方差并不推出未来方差为 $1$，两个广义特征值问题也不再只差平移。

> [!abstract] 命题（小滞后与连续时间 SFA）
> 设 $C_0 \succ 0$，二阶平稳，且 $\dot{\mathbf{x}} \in L^2(T, \mu_T; \mathbb{R}^d)$。再设差分商在滞后窗口的 $L^2$ 中收敛到该导数：$\tau \to 0$ 时，各分量满足
>
> $$
> \left\|
> \frac{x_i(t+\tau) - x_i(t)}{\tau} - \dot{x}_i(t)
> \right\|_{L^2(T_\tau)}
> \to 0.
> $$
>
> 记 $A := \langle \dot{\mathbf{x}}(t) \dot{\mathbf{x}}(t)^\top \rangle_t$ 为连续时间 SFA 的导数协方差。则 $A_\tau = \tau^2 A + o(\tau^2)$，并且在紧集 $\{ \mathbf{w} : \mathbf{w}^\top C_0 \mathbf{w} = 1 \}$ 上一致地有
>
> $$
> \rho_\tau(\mathbf{w})
> = 1 - \frac{\tau^2}{2}\, \mathbf{w}^\top A \mathbf{w} + o(\tau^2).
> $$
>
> 因此 $\tau \to 0$ 时，TICA 最大自相关方向的任一极限点都是连续时间 SFA 的最小导数方向。若另有 $A \mathbf{w} = \mu C_0 \mathbf{w}$ 且 $\mathbf{w}^\top C_0 \mathbf{w} = 1$，则该方向上 $\rho_\tau(\mathbf{w}) = 1 - \tau^2 \mu / 2 + o(\tau^2)$。
>
> > [!note]- 证明
> > 记差分商 $\mathbf{d}_\tau(t) := (\mathbf{x}(t+\tau) - \mathbf{x}(t))/\tau$，余项 $\mathbf{r}_\tau := \mathbf{d}_\tau - \dot{\mathbf{x}}$。假设给出各分量的 $L^2(T_\tau)$ 范数趋于 $0$，故 $\langle \mathbf{r}_\tau \mathbf{r}_\tau^\top \rangle_{t,\tau} \to 0$。交叉项的元素满足
> >
> > $$
> > \bigl| \langle r_{\tau,a}(t)\, \dot{x}_b(t) \rangle_{t,\tau} \bigr|
> > \le
> > \| r_{\tau,a} \|_{L^2(T_\tau)}
> > \,
> > \| \dot{x}_b \|_{L^2(T_\tau)},
> > $$
> >
> > 从而 $\langle \mathbf{d}_\tau \mathbf{d}_\tau^\top \rangle_{t,\tau}$ 收敛到滞后窗口上的 $\langle \dot{\mathbf{x}} \dot{\mathbf{x}}^\top \rangle_{t,\tau}$。$\dot{\mathbf{x}} \in L^2(T)$ 时，宽度为 $\tau$ 的端点层对全时段积分的贡献是 $o(1)$，窗口平均与全时段平均 $A$ 之差趋于 $0$。因此 $A_\tau = \langle (\tau \mathbf{d}_\tau)(\tau \mathbf{d}_\tau)^\top \rangle_{t,\tau} = \tau^2 A + o(\tau^2)$。
> >
> > 二阶平稳给出 $2(C_0 - C_\tau^{\mathrm{sym}}) = A_\tau$，所以 $C_\tau^{\mathrm{sym}} = C_0 - (\tau^2 / 2) A + o(\tau^2)$。$C_0 \succ 0$ 使约束集紧，其上 $\|\mathbf{w}\|_2$ 有界，矩阵的 $o(\tau^2)$ 对二次型一致。代入 $\mathbf{w}^\top C_0 \mathbf{w} = 1$ 得到 $\rho_\tau$ 的展开。
> >
> > 记 $\varepsilon_\tau(\mathbf{w}) := \mathbf{w}^\top (A_\tau / \tau^2 - A) \mathbf{w}$，则 $\varepsilon_\tau$ 在约束集上一致趋于 $0$，并且最大化 $\rho_\tau$ 等价于最小化 $\mathbf{w}^\top A \mathbf{w} + \varepsilon_\tau(\mathbf{w})$。设 $\mathbf{w}_\tau$ 是一个最大自相关方向，$\mathbf{w}_\ast$ 是它的极限点。对任意可行 $\mathbf{w}$，
> >
> > $$
> > \mathbf{w}_\tau^\top A \mathbf{w}_\tau + \varepsilon_\tau(\mathbf{w}_\tau)
> > \le \mathbf{w}^\top A \mathbf{w} + \varepsilon_\tau(\mathbf{w}).
> > $$
> >
> > 令 $\tau \to 0$，得到 $\mathbf{w}_\ast^\top A \mathbf{w}_\ast \le \mathbf{w}^\top A \mathbf{w}$。故 $\mathbf{w}_\ast$ 达到连续时间 SFA 的最小导数二次型。最后一式是把 $A \mathbf{w} = \mu C_0 \mathbf{w}$ 代入同一个展开。$\square$

布朗运动的增量满足 $\langle (B_{t+\tau} - B_t)^2 \rangle = \tau$，差分协方差是 $O(\tau)$ 而不是 $O(\tau^2)$，轨道在 $L^2$ 意义下不可微。滞后形式的 $A_\tau$ 仍有定义，连续时间导数形式的 SFA 不适用，上面的 $\tau^2$ 展开不成立。

## 传播算子与时间尺度

设 $(X_t)$ 平稳，边际为 $\mu$，坐标函数属于 $L^2(\mu)$，且上文的时间平均等于关于 $\mu$ 的期望。滞后传播算子作用在观测上：

$$
(\mathcal{P}_\tau f)(x)
:=
\mathbb{E}\bigl[ f(X_{t+\tau}) \mid X_t = x \bigr],
$$

在该条件期望确定 $L^2(\mu)$ 上一个压缩算子的意义下。于是

$$
\mathbb{E}\bigl[ f(X_t)\, g(X_{t+\tau}) \bigr]
= \langle f, \mathcal{P}_\tau g \rangle_{L^2(\mu)}.
$$

取坐标函数，$(C_\tau)_{ij} = \langle x_i, \mathcal{P}_\tau x_j \rangle_{L^2(\mu)}$。

> [!abstract] 命题（坐标子空间上的 Galerkin 条件）
> 设 $C_0$ 在所讨论的子空间上可逆。$\mathbf{w}$ 与 $\lambda$ 满足 $C_\tau \mathbf{w} = \lambda C_0 \mathbf{w}$，当且仅当残差 $\mathcal{P}_\tau(\mathbf{w}^\top \mathbf{x}) - \lambda\, \mathbf{w}^\top \mathbf{x}$ 与每一个坐标函数在 $L^2(\mu)$ 中正交。可逆动力学下 $C_\tau$ 对称，该条件就是 $C_\tau^{\mathrm{sym}} \mathbf{w} = \lambda C_0 \mathbf{w}$，从而 TICA 的特征值是 $\mathcal{P}_\tau$ 在坐标张成子空间上的 Galerkin 谱，不是 $\mathcal{P}_\tau$ 在整个 $L^2(\mu)$ 上的谱。二者相同，当且仅当相应特征函数落在这个子空间里。
>
> > [!note]- 证明
> > 残差与 $x_i$ 正交写作
> >
> > $$
> > \langle x_i, \mathcal{P}_\tau(\mathbf{w}^\top \mathbf{x}) \rangle_{L^2(\mu)}
> > = \lambda\, \langle x_i, \mathbf{w}^\top \mathbf{x} \rangle_{L^2(\mu)},
> > \qquad i = 1, \ldots, d.
> > $$
> >
> > 左边是 $(C_\tau \mathbf{w})_i$，右边是 $\lambda (C_0 \mathbf{w})_i$。可逆时 $C_\tau = C_\tau^\top$，对称部分不再改变方程，该事实的验证见下一节。这个条件只要求残差正交于 $d$ 个坐标函数。特征函数若不在它们的张成中，就不满足全空间的方程 $\mathcal{P}_\tau f = \lambda f$。$\square$

把输入从原始坐标换成距离、二面角或其它可测映射 $\boldsymbol{\varphi}(X_t) \in \mathbb{R}^d$，优化形式不变：$C_0$ 与 $C_\tau$ 改为 $\boldsymbol{\varphi}$ 的二阶矩，试探子空间改为 $\operatorname{span}\{\varphi_1, \ldots, \varphi_d\}$。

可逆连续时间马尔可夫过程的传播算子构成自伴半群时，非平凡特征值形如 $\lambda_i(\tau) = e^{-\kappa_i \tau}$，$\kappa_i > 0$。若计算得到的 $\lambda_i(\tau) \in (0, 1]$，定义隐含时间尺度

$$
t_i(\tau) := -\frac{\tau}{\ln \lambda_i(\tau)}.
$$

半群情形下 $t_i = 1/\kappa_i$，与 $\tau$ 无关。$\lambda_i \le 0$ 时对数没有定义：负特征值表示滞后 $\tau$ 上的反相关，不对应正的指数衰减时间。有限状态转移矩阵的谱决定分布收敛的速率，见 [[机器学习/FSDTMC|有限状态离散时间时齐马尔可夫链]]。分子动力学里常用 TICA 先把构象压到少数坐标，再离散化这些坐标来估计转移矩阵 [@perezhernandez2013identification]。这样得到的是所选特征子空间上的变分近似。

## 可逆性与对称化

细致平衡是指平稳分布 $\mu$ 与滞后转移核满足

$$
\mu(\mathrm{d}x)\, p_\tau(\mathrm{d}y \mid x)
= \mu(\mathrm{d}y)\, p_\tau(\mathrm{d}x \mid y).
$$

此时 $\mathcal{P}_\tau$ 在 $L^2(\mu)$ 上自伴，$\langle f, \mathcal{P}_\tau g \rangle_{L^2(\mu)} = \langle \mathcal{P}_\tau f, g \rangle_{L^2(\mu)}$。对坐标函数，

$$
\mathbb{E}\bigl[ x_i(t)\, x_j(t+\tau) \bigr]
= \mathbb{E}\bigl[ x_j(t)\, x_i(t+\tau) \bigr],
$$

即 $C_\tau = C_\tau^\top$。总体量不必再对称化。有限样本的 $C_\tau$ 仍可以带数值上的反对称部分，对称化把它去掉。

不论是否可逆，实二次型都只看见 $C_\tau^{\mathrm{sym}}$。不可逆时 $\mathcal{P}_\tau$ 不自伴，$C_\tau \mathbf{w} = \lambda C_0 \mathbf{w}$ 可以出现复特征值，特征向量也不再构成 $C_0$-正交基。改解 $C_\tau^{\mathrm{sym}} \mathbf{w} = \lambda C_0 \mathbf{w}$，是对自伴部分 $(\mathcal{P}_\tau + \mathcal{P}_\tau^\ast)/2$ 做 Galerkin 投影。反对称部分 $\frac{1}{2}(C_\tau - C_\tau^\top)$ 里的概率环流不进入这个谱。

保留整块 $C_\tau$ 的一种做法是 VAMP [@wu2020variational]。在 $C_0$ 与 $C_{\tau\tau}$ 可逆时定义

$$
\bar{K}_\tau := C_0^{-1/2} C_\tau C_{\tau\tau}^{-1/2}.
$$

VAMP-2 在 $m$ 维线性子空间上最大化 $\bar{K}_\tau$ 前 $m$ 个奇异值的平方和，最优子空间由这些奇异值的左右奇异向量张成。二阶平稳且细致平衡时 $C_{\tau\tau} = C_0$ 且 $C_\tau$ 对称，于是 $\bar{K}_\tau = K_\tau$ 本身对称，奇异值分解退回 TICA 的正交特征分解。

## 滞后时间

$\tau$ 是输入参数，不由广义特征值问题解出。

$\tau$ 过小：各模态的 $\lambda_i(\tau)$ 都靠近 $1$，$\ln \lambda_i$ 的相对误差被放大，$t_i(\tau)$ 对 $C_\tau$ 的采样误差敏感。小滞后展开同时说明，此时 TICA 退回局部导数，快噪声与慢变量在自相关上尚未分开。

$\tau$ 过大：慢模态衰减到与采样噪声同量级，配对数减少，离散样本中为 $N-k$，$C_\tau$ 的方差变大。$\lambda_i$ 接近 $0$ 时 $t_i$ 同样不稳定。

检查方法是画出 $t_i(\tau)$ 随 $\tau$ 的变化。可逆半群的总体时间尺度不依赖 $\tau$，平台表示估计进入了与该分辨率相容的区间。平台不是模型正确的充分条件：采样不足、记忆未衰减，或慢特征函数不在所选子空间中，都可以产生一段平坦的曲线。

## 算法

设离散样本 $\mathbf{x}_1, \ldots, \mathbf{x}_N \in \mathbb{R}^d$，滞后为整数步 $k \in \{1, \ldots, N-1\}$，记 $n := N - k$。先减去全轨迹均值 $\bar{\mathbf{x}} = \frac{1}{N}\sum_{t=1}^{N} \mathbf{x}_t$。配对窗口的左右均值仍可能因端点不同而不相等；二者不相等时二阶平稳不成立，差分恒等式必须保留 $C_{\tau\tau}$。

1. 用同一批配对估计

$$
C_0 = \frac{1}{n} \sum_{t=1}^{n} \mathbf{x}_t \mathbf{x}_t^\top,
\qquad
C_\tau = \frac{1}{n} \sum_{t=1}^{n} \mathbf{x}_t \mathbf{x}_{t+k}^\top,
\qquad
C_\tau^{\mathrm{sym}} = \frac{1}{2}\bigl( C_\tau + C_\tau^\top \bigr).
$$

2. $C_0$ 奇异或病态时，用 [[机器学习/PCA|PCA]] 保留大于阈值的特征值，把 $\mathbf{x}_t$、$C_0$ 与 $C_\tau^{\mathrm{sym}}$ 换成该子空间中的坐标。

3. 计算 $K_\tau = C_0^{-1/2} C_\tau^{\mathrm{sym}} C_0^{-1/2}$，作正交特征分解 $K_\tau = Q \Lambda Q^\top$，按 $\lambda_1 \ge \cdots \ge \lambda_d$ 排列。

4. 取前 $m$ 列 $Q_m$，令 $W_m = C_0^{-1/2} Q_m$。则 $W_m^\top C_0 W_m = I_m$，投影为 $\mathbf{z}_t = W_m^\top \mathbf{x}_t$。对 $\lambda_i \in (0, 1]$，隐含时间尺度为 $t_i = -k \Delta t / \ln \lambda_i$，其中 $\Delta t$ 为采样间隔，$\tau = k \Delta t$。

## 与 PCA、SFA 的对照

三种线性投影都是对称矩阵的二次型极值，差别在于被优化的矩阵和约束诱导的内积。

PCA 在 $\mathbf{w}^\top \mathbf{w} = 1$ 下最大化 $\mathbf{w}^\top C_0 \mathbf{w}$，取 $C_0$ 的最大特征值。它只看同一时刻的方差，大方差方向可以是快噪声。

连续时间 SFA 在 $\mathbf{w}^\top B \mathbf{w} = 1$ 下最小化 $\mathbf{w}^\top A \mathbf{w}$，取导数协方差的最小广义特征值。离散形式把 $A$ 换成 $A_\tau$。二阶平稳且 $B$ 与 $A_\tau$ 使用同一滞后窗口时，这些方向与 TICA 相同，特征值关系为 $\mu = 2(1 - \lambda)$。

TICA 在 $\mathbf{w}^\top C_0 \mathbf{w} = 1$ 下最大化 $\mathbf{w}^\top C_\tau^{\mathrm{sym}} \mathbf{w}$，取最大广义特征值。它显式依赖 $\tau$：同一条序列在不同滞后上可以选出不同方向。样本只在离散时刻取值时，滞后乘积不需要估计时间导数。

## 注记

特征向量的正负号不改变二次型。单根时 $\mathbf{w}$ 与 $-\mathbf{w}$ 是同一方向。重根时，逐次最大自相关命题只确定重根子空间，其中的 $C_0$-标准正交基可以旋转。

非平稳序列不满足 $C_{\tau\tau} = C_0$。全局减去一个常数均值也不能恢复这个等式。Rayleigh 商仍可计算，但 $\lambda \in [-1, 1]$ 与 $\mu = 2(1 - \lambda)$ 都不再成立，隐含时间尺度的指数解释也失去半群依据。

TICA 这个名字来自用时间滞后相关分离独立信源 [@molgedey1994separation]，不是极大化非高斯性或极小化互信息的独立成分分析。本文的目标是滞后自相关，用它提取慢线性坐标 [@perezhernandez2013identification]。

## 文献

Molgedey 与 Schuster 用时间滞后相关分离独立信号 [@molgedey1994separation]。Pérez-Hernández 等把这一广义特征值问题用于分子动力学中的慢序参量，并由此构造马尔可夫模型 [@perezhernandez2013identification]。非可逆情形的奇异值形式见 Wu 与 Noé 的 VAMP [@wu2020variational]。
