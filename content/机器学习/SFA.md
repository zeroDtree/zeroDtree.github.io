---
title: 慢特征分析（SFA）
tags:
  - 线性代数
  - 统计
  - 机器学习
date: 2026-11-09
---

## 前置

- [[机器学习/Rayleigh商|Rayleigh 商]]
- [[数学/数学分析/平方可积|平方可积空间 L²]]

## 目标

给定时间序列 $\mathbf{x}(t) \in \mathbb{R}^d$，在单位方差与正交去相关约束下，依次寻找使投影信号时间导数均方值 $\langle \dot{y}(t)^2 \rangle_t$ 最小的线性方向。

## 设定

设时间指标集 $T \subset \mathbb{R}$ 配备 Borel $\sigma$-代数 $\mathcal{B}(T)$ 与概率测度 $\mu_T$（$\mu_T(T) = 1$）。对可测时间序列 $\mathbf{x} : T \to \mathbb{R}^d$ 及可积函数 $f \in L^1(T, \mu_T)$，定义时间平均为 $\mu_T$ 上的 Lebesgue 积分：

$$
\langle f(t) \rangle_t := \int_T f(t)\,\mu_T(\mathrm{d}t).
$$

两类特例：

- **连续时间区间**：$T = [t_0, t_1]$，$\mu_T = \frac{1}{\lambda(T)}\lambda|_T$（$\lambda$ 为 $\mathbb{R}$ 上的 Lebesgue 测度），$\langle f(t) \rangle_t = \frac{1}{t_1 - t_0} \int_{[t_0, t_1]} f(t)\,\lambda(\mathrm{d}t)$；
- **离散时间采样**：$T = \{t_1, \ldots, t_N\}$，$\mu_T = \frac{1}{N}\sum_{k=1}^N \delta_{t_k}$（归一化计数测度），$\langle f(t) \rangle_t = \frac{1}{N}\sum_{k=1}^N f(t_k)$。

对 $u, v \in L^2(T, \mu_T)$，时间平均 $\langle u(t)v(t) \rangle_t = \int_T u(t)v(t)\,\mu_T(\mathrm{d}t)$ 即为 $L^2(T, \mu_T)$ 上的内积。

设复合信号 $y_j(t) = g_j(\mathbf{x}(t))$ 关于 $t$ 几乎处处可微，且 $y_j, \dot{y}_j \in L^2(T, \mu_T)$。SFA 依次求解瞬时映射 $g_j : \mathbb{R}^d \to \mathbb{R}$（$j = 1, \ldots, m$）：

$$
\begin{aligned}
\min_{g_j} \quad & \Delta(y_j) := \left\langle \dot{y}_j(t)^2 \right\rangle_t \\
\text{s.t.} \quad & \langle y_j(t) \rangle_t = 0, \\
& \langle y_j(t)^2 \rangle_t = 1, \\
& \langle y_i(t) y_j(t) \rangle_t = 0, \qquad \forall\, i < j.
\end{aligned}
$$

## 线性SFA

设 $\mathbf{x}(t)$ 已中心化（$\langle \mathbf{x}(t) \rangle_t = \mathbf{0}$），各分量几乎处处可微且 $\mathbf{x}, \dot{\mathbf{x}} \in L^2(T, \mu_T; \mathbb{R}^d)$。取线性映射 $y_j(t) = \mathbf{w}_j^\top \mathbf{x}(t)$，则 $\dot{y}_j(t) = \mathbf{w}_j^\top \dot{\mathbf{x}}(t)$。定义时间导数协方差矩阵 $A$ 与瞬时协方差矩阵 $B$：

$$
A := \left\langle \dot{\mathbf{x}}(t)\dot{\mathbf{x}}(t)^\top \right\rangle_t = \int_T \dot{\mathbf{x}}(t)\dot{\mathbf{x}}(t)^\top\,\mu_T(\mathrm{d}t) \in \mathbb{R}^{d \times d},
\qquad
B := \left\langle \mathbf{x}(t)\mathbf{x}(t)^\top \right\rangle_t = \int_T \mathbf{x}(t)\mathbf{x}(t)^\top\,\mu_T(\mathrm{d}t) \in \mathbb{R}^{d \times d}.
$$

> [!abstract] 零均值约束与二次型化简
> 由积分的线性性，零均值约束 $\langle y_j(t) \rangle_t = \mathbf{w}_j^\top \langle \mathbf{x}(t) \rangle_t = 0$ 自然满足；慢度目标函数与二阶矩约束分别化为关于 $\mathbf{w}$ 的二次型与双线性型：
>
> $$
> \Delta(y_j) = \left\langle \mathbf{w}_j^\top \dot{\mathbf{x}}(t)\dot{\mathbf{x}}(t)^\top \mathbf{w}_j \right\rangle_t = \mathbf{w}_j^\top A \mathbf{w}_j,
> \qquad
> \langle y_i(t) y_j(t) \rangle_t = \left\langle \mathbf{w}_i^\top \mathbf{x}(t)\mathbf{x}(t)^\top \mathbf{w}_j \right\rangle_t = \mathbf{w}_i^\top B \mathbf{w}_j.
> $$
>
> > [!note]- 推导
> > **1. 零均值约束自动满足：**
> > 记常向量 $\mathbf{w}_j = (w_{j,1}, \ldots, w_{j,d})^\top \in \mathbb{R}^d$，$\mathbf{x}(t) = (x_1(t), \ldots, x_d(t))^\top$，向量值函数的时间平均按分量定义为 $\langle \mathbf{x}(t) \rangle_t := (\langle x_1(t) \rangle_t, \ldots, \langle x_d(t) \rangle_t)^\top \in \mathbb{R}^d$。由 的齐次性与可加性（线性性），与时间 $t$ 无关的系数 $w_{j,k}$ 可提出积分号外：
> >
> > $$
> > \begin{aligned}
> > \langle y_j(t) \rangle_t
> > &= \int_T \left( \sum_{k=1}^d w_{j,k} x_k(t) \right) \mu_T(\mathrm{d}t) \\
> > &= \sum_{k=1}^d w_{j,k} \int_T x_k(t)\,\mu_T(\mathrm{d}t) \\
> > &= \sum_{k=1}^d w_{j,k} \langle x_k(t) \rangle_t \\
> > &= \mathbf{w}_j^\top \langle \mathbf{x}(t) \rangle_t.
> > \end{aligned}
> > $$
> >
> > 结合输入已中心化的假设 $\langle \mathbf{x}(t) \rangle_t = \mathbf{0}$（若原始序列均值 $\bar{\mathbf{x}} := \langle \mathbf{x}_{\mathrm{raw}}(t) \rangle_t \neq \mathbf{0}$，预先作平移 $\mathbf{x}(t) := \mathbf{x}_{\mathrm{raw}}(t) - \bar{\mathbf{x}}$ 即可），对任意 $\mathbf{w}_j \in \mathbb{R}^d$ 恒有
> >
> > $$
> > \langle y_j(t) \rangle_t = \mathbf{w}_j^\top \mathbf{0} = 0,
> > $$
> >
> > 故第一条约束 $\langle y_j(t) \rangle_t = 0$ 在优化问题中可消去。
> >
> > **2. 二阶矩与慢度目标化简：**
> > 注意到标量 $y_j(t) = \mathbf{w}_j^\top \mathbf{x}(t) = \mathbf{x}(t)^\top \mathbf{w}_j$，将乘积 $y_i(t) y_j(t)$ 按分量展开：
> >
> > $$
> > y_i(t) y_j(t) = \left( \sum_{k=1}^d w_{i,k} x_k(t) \right) \left( \sum_{\ell=1}^d x_\ell(t) w_{j,\ell} \right) = \sum_{k=1}^d \sum_{\ell=1}^d w_{i,k} w_{j,\ell} x_k(t) x_\ell(t).
> > $$
> >
> > 矩阵值函数的积分按元素定义，即矩阵 $B = \int_T \mathbf{x}(t)\mathbf{x}(t)^\top\,\mu_T(\mathrm{d}t)$ 的第 $(k,\ell)$ 元为 $B_{k\ell} = \int_T x_k(t) x_\ell(t)\,\mu_T(\mathrm{d}t) = \langle x_k(t) x_\ell(t) \rangle_t$。由 Lebesgue 积分的可加性与齐次性，将与 $t$ 无关的常系数 $w_{i,k} w_{j,\ell}$ 提出积分号并与有限求和交换顺序：
> >
> > $$
> > \begin{aligned}
> > \langle y_i(t) y_j(t) \rangle_t
> > &= \int_T \left( \sum_{k=1}^d \sum_{\ell=1}^d w_{i,k} w_{j,\ell} x_k(t) x_\ell(t) \right) \mu_T(\mathrm{d}t) \\
> > &= \sum_{k=1}^d \sum_{\ell=1}^d w_{i,k} w_{j,\ell} \int_T x_k(t) x_\ell(t)\,\mu_T(\mathrm{d}t) \\
> > &= \sum_{k=1}^d \sum_{\ell=1}^d w_{i,k} B_{k\ell} w_{j,\ell} \\
> > &= \mathbf{w}_i^\top B \mathbf{w}_j.
> > \end{aligned}
> > $$
> >
> > 同理，将 $\dot{y}_j(t) = \sum_{k=1}^d w_{j,k} \dot{x}_k(t)$ 展开并利用 $A_{k\ell} = \int_T \dot{x}_k(t) \dot{x}_\ell(t)\,\mu_T(\mathrm{d}t)$，有
> >
> > $$
> > \begin{aligned}
> > \Delta(y_j)
> > &= \int_T \left( \sum_{k=1}^d \sum_{\ell=1}^d w_{j,k} w_{j,\ell} \dot{x}_k(t) \dot{x}_\ell(t) \right) \mu_T(\mathrm{d}t) \\
> > &= \sum_{k=1}^d \sum_{\ell=1}^d w_{j,k} w_{j,\ell} \int_T \dot{x}_k(t) \dot{x}_\ell(t)\,\mu_T(\mathrm{d}t) \\
> > &= \sum_{k=1}^d \sum_{\ell=1}^d w_{j,k} A_{k\ell} w_{j,\ell} \\
> > &= \mathbf{w}_j^\top A \mathbf{w}_j. \quad \square
> > \end{aligned}
> > $$

从而线性 SFA 化为约束二次规划：

$$
\begin{aligned}
\min_{\mathbf{w}_j \in \mathbb{R}^d} \quad & \Delta(\mathbf{w}_j) = \mathbf{w}_j^\top A \mathbf{w}_j \\
\text{s.t.} \quad & \mathbf{w}_i^\top B \mathbf{w}_j = \delta_{ij}, \qquad 1 \le i \le j,
\end{aligned}
$$

其中 $\delta_{ij}$ 为 Kronecker 记号：当 $i = j$ 时为 $\mathbf{w}_j^\top B \mathbf{w}_j = \langle y_j(t)^2 \rangle_t = 1$（单位方差），当 $i < j$ 时为 $\mathbf{w}_i^\top B \mathbf{w}_j = \langle y_i(t)y_j(t) \rangle_t = 0$（正交去相关）。

## 广义特征值与白化求解

线性 SFA 的约束二次规划可以交给 [[机器学习/Rayleigh商|Rayleigh 商]] 处理。对单个方向，约束优化

$$
\min_{\mathbf{w}^\top B\mathbf{w}=1}\mathbf{w}^\top A\mathbf{w}
$$

的驻点满足

$$
A\mathbf{w}=\lambda B\mathbf{w},
\qquad
\lambda=\frac{\mathbf{w}^\top A\mathbf{w}}{\mathbf{w}^\top B\mathbf{w}},
$$

这是 [[机器学习/Rayleigh商#约束优化视角|约束优化视角]] 的直接结论。

对 $m$ 个方向，[[机器学习/Rayleigh商#变分刻画|变分刻画]] 中的矩阵形式定理给出

$$
\min_{W^\top BW=I_m}\operatorname{tr}(W^\top AW)=\sum_{j=1}^m\lambda_j,
$$

且最小值在 $W=[\mathbf{v}_1,\ldots,\mathbf{v}_m]$ 处达到，其中 $\lambda_1\le\cdots\le\lambda_d$ 是 $(A,B)$ 的广义特征值，$\mathbf{v}_j$ 为对应的 $B$-标准正交特征向量。

逐次变分形式同理：第 $j$ 个方向在前 $j-1$ 个方向确定后，取剩余特征子空间中最小的 $\lambda_j$；重根时可在对应特征子空间中任取一组 $B$-标准正交基。

当 $B\succ0$ 时，取 $B=SS^\top$（例如对称平方根 $S=B^{1/2}$），令

$$
\tilde A=S^{-1}AS^{-\top}.
$$

则 $\tilde A$ 实对称半正定，且

$$
A\mathbf{w}=\lambda B\mathbf{w}
\iff
\tilde A\mathbf{u}=\lambda\mathbf{u},
\qquad
\mathbf{u}=S^\top\mathbf{w}.
$$

证明见 [[广义特征值#白化与标准特征值问题|白化与标准特征值问题]]。若 $\tilde A=Q\Lambda Q^\top$，则

$$
\mathbf{v}_j=S^{-\top}\mathbf{q}_j
$$

给出原问题的 $B$-标准正交特征向量；实际计算时对 $\tilde A$ 做对称特征分解，再回代即可。

SFA 中 $A\succeq0$，所以全部 $\lambda_j\ge0$，慢度就是对应的广义特征值。若 $B$ 奇异，可在 $\operatorname{range}(B)$ 上求解；压缩的限制与注意事项见 [[广义特征值#谱性质与退化情形|谱性质与退化情形]]。

## 离散时间差分形式

对离散时间或给定滞后步长 $\tau > 0$ 的情形，以有限步长差分替代时间导数。$\mathbf{x}(t+\tau)$ 只在 $t$ 与 $t+\tau$ 同时属于 $T$ 时有定义，故时间平均取在配对窗口上。记

$$
T_\tau := \{\, t \in T : t+\tau \in T \,\},
\qquad
\mu_{T_\tau} := \frac{1}{\mu_T(T_\tau)}\,\mu_T|_{T_\tau},
$$

并设 $\mu_T(T_\tau) > 0$。对可积函数 $f$，定义滞后平均

$$
\langle f(t) \rangle_{t,\tau}
:= \int_{T_\tau} f(t)\,\mu_{T_\tau}(\mathrm{d}t)
= \frac{1}{\mu_T(T_\tau)} \int_{T_\tau} f(t)\,\mu_T(\mathrm{d}t).
$$

设 $\mathbf{x}$ 在 $T_\tau$ 上已中心化，且 $\mathbf{x}(t), \mathbf{x}(t+\tau) \in L^2(T_\tau, \mu_{T_\tau}; \mathbb{R}^d)$。取 $y(t) = \mathbf{w}^\top \mathbf{x}(t)$，定义差分 $\Delta \mathbf{x}_\tau(t) := \mathbf{x}(t+\tau) - \mathbf{x}(t)$ 及

$$
A_\tau := \left\langle \Delta \mathbf{x}_\tau(t)\Delta \mathbf{x}_\tau(t)^\top \right\rangle_{t,\tau} \succeq 0,
\qquad
B := \left\langle \mathbf{x}(t)\mathbf{x}(t)^\top \right\rangle_{t,\tau} \succeq 0.
$$

$B$ 与 §线性SFA 的瞬时协方差相同，只是平均窗口换成 $T_\tau$；平稳时二者一致。于是

$$
\begin{aligned}
\Delta_\tau(\mathbf{w})
&:= \left\langle \bigl[ y(t+\tau) - y(t) \bigr]^2 \right\rangle_{t,\tau} \\
&= \left\langle \bigl[ \mathbf{w}^\top \bigl( \mathbf{x}(t+\tau) - \mathbf{x}(t) \bigr) \bigr]^2 \right\rangle_{t,\tau} \\
&= \left\langle \mathbf{w}^\top \Delta \mathbf{x}_\tau(t) \Delta \mathbf{x}_\tau(t)^\top \mathbf{w} \right\rangle_{t,\tau} \\
&= \mathbf{w}^\top \left\langle \Delta \mathbf{x}_\tau(t) \Delta \mathbf{x}_\tau(t)^\top \right\rangle_{t,\tau} \mathbf{w} \\
&= \mathbf{w}^\top A_\tau \mathbf{w}.
\end{aligned}
$$

约束仍为 $W^\top B W = I_m$。这已化为 §线性SFA 的约束二次规划。
