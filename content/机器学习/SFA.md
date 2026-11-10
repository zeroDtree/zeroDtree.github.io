---
title: 慢特征分析（SFA）
tags:
 - 线性代数
 - 统计
 - 机器学习
date: 2026-11-09
---

## 前置

- [[机器学习/PCA|PCA（主成分分析）]]
- [[机器学习/拉格朗日乘子法|拉格朗日乘子法]]
- [[机器学习/FSDTMC|有限状态离散时间时齐马尔可夫链(FSDTMC)]]
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

矩阵 $A \succeq 0$ 度量投影信号的时间变化率，而约束 $\mathbf{w}_i^\top B \mathbf{w}_j = \delta_{ij}$ 由 $B$ 诱导的加权内积 $\langle \mathbf{w}_i, \mathbf{w}_j \rangle_B := \mathbf{w}_i^\top B \mathbf{w}_j$ 给出。先对 $j = 1$ 考察

$$
\min_{\mathbf{w}^\top B \mathbf{w} = 1} \mathbf{w}^\top A \mathbf{w}.
$$

由 [[机器学习/拉格朗日乘子法|拉格朗日乘子法]]，令 $\mathcal{L}(\mathbf{w}, \lambda) = \mathbf{w}^\top A \mathbf{w} - \lambda(\mathbf{w}^\top B \mathbf{w} - 1)$，一阶驻点条件 $\nabla_{\mathbf{w}} \mathcal{L} = 2A\mathbf{w} - 2\lambda B\mathbf{w} = \mathbf{0}$ 给出广义特征值方程

$$
A\mathbf{w} = \lambda B\mathbf{w}.
$$

左乘 $\mathbf{w}^\top$ 并代入 $\mathbf{w}^\top B \mathbf{w} = 1$，得驻点处的慢度 $\Delta(\mathbf{w}) = \mathbf{w}^\top A \mathbf{w} = \lambda$。当 $B \succ 0$ 时（若 $B$ 奇异，可先由 [[机器学习/PCA|PCA]] 投影至 $B$ 的非零特征子空间），利用白化变换即可严格导出全部 $m$ 个慢特征方向的全局最优解。

> [!abstract] 命题（白化变换下约束优化等价性）
> 设 $A \succeq 0$，$B \succ 0$。定义白化坐标变换及白化后的矩阵
>
> $$
> \mathbf{u}_j := B^{1/2}\mathbf{w}_j \iff \mathbf{w}_j = B^{-1/2}\mathbf{u}_j,
> \qquad
> \tilde{A} := B^{-1/2} A B^{-1/2}.
> $$
>
> 则 $\mathbf{w}_j \mapsto \mathbf{u}_j$ 是 $\mathbb{R}^d$ 上的双射，$\tilde{A}$ 为实对称半正定矩阵，且原坐标中的 $B$-标准正交约束与慢度目标分别等价于白化坐标中的欧氏标准正交约束与二次型：
>
> $$
> \mathbf{w}_i^\top B \mathbf{w}_j = \delta_{ij}
> \iff
> \mathbf{u}_i^\top \mathbf{u}_j = \delta_{ij},
> \qquad
> \mathbf{w}_j^\top A \mathbf{w}_j = \mathbf{u}_j^\top \tilde{A} \mathbf{u}_j.
> $$
>
> > [!note]- 证明
> > 因 $B \succ 0$ 为实对称正定矩阵，由实对称矩阵谱定理，存在正交矩阵 $P \in \mathbb{R}^{d \times d}$（$P^\top P = I_d$），使得 $B = P D P^\top$，其中 $D = \operatorname{diag}(d_1, \ldots, d_d)$ 且 $d_i > 0$（$1 \le i \le d$）。据此定义对称正定平方根及其逆：
> >
> > $$
> > B^{1/2} := P \operatorname{diag}\!\left(\sqrt{d_1}, \ldots, \sqrt{d_d}\right) P^\top \succ 0,
> > \qquad
> > B^{-1/2} := P \operatorname{diag}\!\left(1/\sqrt{d_1}, \ldots, 1/\sqrt{d_d}\right) P^\top \succ 0.
> > $$
> >
> > 由 $P^\top P = P P^\top = I_d$，直接验证可知 $(B^{1/2})^\top = B^{1/2}$、$(B^{-1/2})^\top = B^{-1/2}$，且满足基本乘积恒等式：
> >
> > $$
> > B^{1/2} B^{1/2} = B, \qquad B^{1/2} B^{-1/2} = B^{-1/2} B^{1/2} = I_d, \qquad B^{-1/2} B = B^{1/2}, \qquad B^{-1/2} B B^{-1/2} = I_d.
> > $$
> >
> > 作可逆线性变量代换（对应白化信号 $\tilde{\mathbf{x}}(t) := B^{-1/2}\mathbf{x}(t)$）：
> >
> > $$
> > \mathbf{u}_j := B^{1/2} \mathbf{w}_j \iff \mathbf{w}_j = B^{-1/2} \mathbf{u}_j,
> > \qquad
> > \tilde{A} := B^{-1/2} A B^{-1/2} = \left\langle \dot{\tilde{\mathbf{x}}}(t)\dot{\tilde{\mathbf{x}}}(t)^\top \right\rangle_t.
> > $$
> >
> > 由于 $A^\top = A$、$A \succeq 0$ 且 $(B^{-1/2})^\top = B^{-1/2}$，有 $\tilde{A}^\top = (B^{-1/2} A B^{-1/2})^\top = B^{-1/2} A^\top B^{-1/2} = \tilde{A}$；且对任意 $\mathbf{z} \in \mathbb{R}^d$ 恒有 $\mathbf{z}^\top \tilde{A} \mathbf{z} = (B^{-1/2}\mathbf{z})^\top A (B^{-1/2}\mathbf{z}) \ge 0$，故 $\tilde{A} \succeq 0$ 为实对称半正定矩阵。将 $\mathbf{w}_j = B^{-1/2}\mathbf{u}_j$ 代入原优化问题，原来的 $B$-标准正交约束与慢度目标分别等价转化为欧氏标准正交约束与关于 $\tilde{A}$ 的二次型：
> >
> > $$
> > \begin{aligned}
> > \mathbf{w}_i^\top B \mathbf{w}_j
> > &= \left(B^{-1/2} \mathbf{u}_i\right)^\top B \left(B^{-1/2} \mathbf{u}_j\right)
> > = \mathbf{u}_i^\top \left(B^{-1/2} B B^{-1/2}\right) \mathbf{u}_j
> > = \mathbf{u}_i^\top \mathbf{u}_j = \delta_{ij}, \\
> > \Delta(\mathbf{w}_j)
> > &= \mathbf{w}_j^\top A \mathbf{w}_j
> > = \left(B^{-1/2} \mathbf{u}_j\right)^\top A \left(B^{-1/2} \mathbf{u}_j\right)
> > = \mathbf{u}_j^\top \left(B^{-1/2} A B^{-1/2}\right) \mathbf{u}_j
> > = \mathbf{u}_j^\top \tilde{A} \mathbf{u}_j.
> > \end{aligned}
> > $$
> >
> > 因而白化变换保持可行性与目标值，两个约束优化问题完全等价。$\square$

> [!abstract] 命题（广义特征值问题与标准特征值问题的等价性）
> 沿用上命题的设定与记号。对任意非零向量 $\mathbf{w} \in \mathbb{R}^d$，令 $\mathbf{u} := B^{1/2}\mathbf{w}$，则
>
> $$
> A\mathbf{w} = \lambda B\mathbf{w}
> \iff
> \tilde{A}\mathbf{u} = \lambda\mathbf{u}.
> $$
>
> 若 $\tilde{A} = Q\Lambda Q^\top$，其中 $\Lambda = \operatorname{diag}(\lambda_1,\ldots,\lambda_d)$ 且 $Q = [\mathbf{q}_1,\ldots,\mathbf{q}_d]$ 为正交矩阵，则
>
> $$
> \mathbf{v}_j := B^{-1/2}\mathbf{q}_j,
> \qquad j = 1,\ldots,d,
> $$
>
> 是广义特征值问题 $A\mathbf{w} = \lambda B\mathbf{w}$ 对应于 $\lambda_j$ 的 $B$-标准正交广义特征向量，即
>
> $$
> A\mathbf{v}_j = \lambda_j B\mathbf{v}_j,
> \qquad
> \mathbf{v}_i^\top B\mathbf{v}_j = \delta_{ij}.
> $$
>
> > [!note]- 证明
> > 因 $B^{1/2}$ 与 $B^{-1/2}$ 均可逆，对任意 $(\lambda, \mathbf{w})$ 及双射对应的 $\mathbf{u} = B^{1/2}\mathbf{w}$（即 $\mathbf{w} = B^{-1/2}\mathbf{u}$），在广义特征值方程两边左乘 $B^{-1/2}$ 并利用 $B^{-1/2}B = B^{1/2}$，可作双向可逆推导：
> >
> > $$
> > \begin{aligned}
> > A \mathbf{w} = \lambda B \mathbf{w}
> > &\iff B^{-1/2} A \mathbf{w} = \lambda B^{-1/2} B \mathbf{w} = \lambda B^{1/2} \mathbf{w} \\
> > &\iff B^{-1/2} A B^{-1/2} \mathbf{u} = \lambda \mathbf{u} \\
> > &\iff \tilde{A} \mathbf{u} = \lambda \mathbf{u}.
> > \end{aligned}
> > $$
> >
> > 这表明广义特征值问题 $A\mathbf{w} = \lambda B\mathbf{w}$ 与标准特征值问题 $\tilde{A}\mathbf{u} = \lambda \mathbf{u}$ 的特征值完全相同，且特征向量通过 $\mathbf{u} = B^{1/2}\mathbf{w} \iff \mathbf{w} = B^{-1/2}\mathbf{u}$ 一一对应。
> >
> > 因 $\tilde{A} \succeq 0$ 实对称，可作正交特征分解 $\tilde{A} = Q \Lambda Q^\top$，其中 $\Lambda = \operatorname{diag}(\lambda_1, \ldots, \lambda_d)$（$0 \le \lambda_1 \le \lambda_2 \le \cdots \le \lambda_d$），$Q = [\mathbf{q}_1, \ldots, \mathbf{q}_d]$ 为正交矩阵，满足标准特征值方程 $\tilde{A}\mathbf{q}_j = \lambda_j \mathbf{q}_j$ 及 $\mathbf{q}_i^\top \mathbf{q}_j = \delta_{ij}$。通过逆白化变换定义原坐标空间中的向量：
> >
> > $$
> > \mathbf{v}_j := B^{-1/2} \mathbf{q}_j \iff \mathbf{q}_j = B^{1/2} \mathbf{v}_j, \qquad j = 1, \ldots, d.
> > $$
> >
> > 将 $\tilde{A} = B^{-1/2} A B^{-1/2}$ 代入 $\tilde{A}\mathbf{q}_j = \lambda_j \mathbf{q}_j$ 得 $B^{-1/2} A B^{-1/2} \mathbf{q}_j = \lambda_j \mathbf{q}_j$，等式两边左乘 $B^{1/2}$ 并利用 $B^{1/2}B^{-1/2} = I_d$、$\mathbf{v}_j = B^{-1/2}\mathbf{q}_j$、$\mathbf{q}_j = B^{1/2}\mathbf{v}_j$ 及 $B^{1/2}B^{1/2} = B$，逐步化简得
> >
> > $$
> > \begin{aligned}
> > B^{1/2} B^{-1/2} A \left(B^{-1/2} \mathbf{q}_j\right) = \lambda_j B^{1/2} \mathbf{q}_j
> > &\implies A \mathbf{v}_j = \lambda_j B^{1/2} \left(B^{1/2} \mathbf{v}_j\right) \\
> > &\implies A \mathbf{v}_j = \lambda_j B \mathbf{v}_j.
> > \end{aligned}
> > $$
> >
> > 同时，验证其 $B$-加权内积：
> >
> > $$
> > \mathbf{v}_i^\top B \mathbf{v}_j
> > = \left(B^{-1/2} \mathbf{q}_i\right)^\top B \left(B^{-1/2} \mathbf{q}_j\right)
> > = \mathbf{q}_i^\top \left(B^{-1/2} B B^{-1/2}\right) \mathbf{q}_j
> > = \mathbf{q}_i^\top \mathbf{q}_j
> > = \delta_{ij}.
> > $$
> >
> > 故 $\lambda_1 \le \cdots \le \lambda_d$ 恰为广义特征值问题 $A\mathbf{w} = \lambda B\mathbf{w}$ 的全部广义特征值，$\mathbf{v}_1, \ldots, \mathbf{v}_d$ 为对应的 $B$-标准正交广义特征向量。$\square$

> [!abstract] 命题（向量形式：逐次最小慢度）
> 沿用上述命题的设定与记号，并将广义特征值按升序排列为 $0 \le \lambda_1 \le \cdots \le \lambda_d$。对 $1 \le j \le d$，设前 $j-1$ 个慢特征方向已取为 $\mathbf{w}_1 = \mathbf{v}_1,\ldots,\mathbf{w}_{j-1} = \mathbf{v}_{j-1}$，则第 $j$ 个方向的最小慢度为
>
> $$
> \min_{\substack{\mathbf{w}_j^\top B \mathbf{w}_j = 1 \\ \mathbf{v}_r^\top B \mathbf{w}_j = 0,\ 1 \le r < j}} \mathbf{w}_j^\top A \mathbf{w}_j = \lambda_j.
> $$
>
> 最小值当且仅当 $\mathbf{w}_j \in \operatorname{span}\{\mathbf{v}_i : i \ge j,\ \lambda_i = \lambda_j\}$ 且 $\mathbf{w}_j^\top B \mathbf{w}_j = 1$ 时达到；特别地，$\mathbf{w}_j = \pm \mathbf{v}_j$ 达到最小值 $\lambda_j$。若 $\lambda_j$ 为单根，则最优方向在正负号意义下唯一；若 $\lambda_j$ 有重根，则可在对应剩余广义特征子空间中任取 $B$-标准正交方向。
>
> > [!note]- 证明
> > 对第 $j$ 步（$1 \le j \le d$），设前 $j-1$ 个最慢方向已依次选定为 $\mathbf{u}_r = \mathbf{q}_r$（即 $\mathbf{w}_r = \mathbf{v}_r$，$1 \le r < j$；当 $j=1$ 时无前序正交约束）。当前第 $j$ 步在满足正交约束 $\mathbf{u}_r^\top \mathbf{u}_j = 0$（$1 \le r < j$）与单位长度约束 $\mathbf{u}_j^\top \mathbf{u}_j = 1$ 的可行向量 $\mathbf{u}_j \in \mathbb{R}^d$ 中最小化 $\Delta(\mathbf{w}_j) = \mathbf{u}_j^\top \tilde{A} \mathbf{u}_j$。
> >
> > 引入特征坐标变换 $\mathbf{z} := Q^\top \mathbf{u}_j = (z_1, \ldots, z_d)^\top$（$\iff \mathbf{u}_j = Q\mathbf{z}$）。由 $Q = [\mathbf{q}_1, \ldots, \mathbf{q}_d]$，其第 $i$ 个分量为 $z_i = \mathbf{q}_i^\top \mathbf{u}_j$，目标函数随之对角化为各特征方向上的加权平方和：
> >
> > $$
> > \Delta(\mathbf{w}_j)
> > = \mathbf{u}_j^\top Q \Lambda Q^\top \mathbf{u}_j
> > = \mathbf{z}^\top \Lambda \mathbf{z}
> > = \sum_{i=1}^d \lambda_i z_i^2.
> > $$
> >
> > 下面依次将正交约束与单位长度约束转化为关于坐标 $\mathbf{z}$ 的条件：
> > - **前 $j-1$ 个分量为零**：对任意 $1 \le r < j$，由已选方向 $\mathbf{u}_r = \mathbf{q}_r$ 及正交约束 $\mathbf{u}_r^\top \mathbf{u}_j = 0$，有
> >
> > $$
> > z_r = \mathbf{q}_r^\top \mathbf{u}_j = \mathbf{u}_r^\top \mathbf{u}_j = 0, \qquad 1 \le r \le j-1,
> > $$
> >
> > 即 $\mathbf{z} = (0, \ldots, 0, z_j, z_{j+1}, \ldots, z_d)^\top$，新方向不包含前 $j-1$ 个已选方向上的分量。
> > - **剩余分量平方和为 $1$**：由正交矩阵保内积（$Q Q^\top = I_d$）及单位长度约束 $\|\mathbf{u}_j\|_2^2 = 1$，有
> >
> > $$
> > \|\mathbf{z}\|_2^2 = \mathbf{z}^\top \mathbf{z} = \left(Q^\top \mathbf{u}_j\right)^\top \left(Q^\top \mathbf{u}_j\right) = \mathbf{u}_j^\top Q Q^\top \mathbf{u}_j = \mathbf{u}_j^\top \mathbf{u}_j = \|\mathbf{u}_j\|_2^2 = 1.
> > $$
> >
> > 结合 $z_1 = \cdots = z_{j-1} = 0$，得
> >
> > $$
> > \sum_{i=j}^d z_i^2 = 1.
> > $$
> >
> > 利用特征值的升序排列 $0 \le \lambda_1 \le \cdots \le \lambda_j \le \lambda_{j+1} \le \cdots \le \lambda_d$，对一切 $i \ge j$ 均有 $\lambda_i \ge \lambda_j$ 且 $z_i^2 \ge 0$，从而 $\lambda_i z_i^2 \ge \lambda_j z_i^2$。对 $i = j, \ldots, d$ 求和得慢度下界：
> >
> > $$
> > \Delta(\mathbf{w}_j)
> > = \sum_{i=j}^d \lambda_i z_i^2
> > \ge \sum_{i=j}^d \lambda_j z_i^2
> > = \lambda_j \sum_{i=j}^d z_i^2
> > = \lambda_j.
> > $$
> >
> > 为分析取等号 $\Delta(\mathbf{w}_j) = \lambda_j$ 的充要条件，将 $\Delta(\mathbf{w}_j)$ 与 $\lambda_j$ 作差并代入 $\sum_{i=j}^d z_i^2 = 1$：
> >
> > $$
> > \Delta(\mathbf{w}_j) - \lambda_j
> > = \sum_{i=j}^d \lambda_i z_i^2 - \lambda_j \sum_{i=j}^d z_i^2
> > = \sum_{i=j}^d (\lambda_i - \lambda_j) z_i^2.
> > $$
> >
> > 因对所有 $i \ge j$ 均有 $\lambda_i - \lambda_j \ge 0$ 且 $z_i^2 \ge 0$，上述非负项之和等于零当且仅当每一项均为零：
> >
> > $$
> > (\lambda_i - \lambda_j) z_i^2 = 0, \quad \forall\, i \ge j
> > \iff
> > \bigl(\forall\, i \ge j,\ \lambda_i > \lambda_j \implies z_i = 0\bigr).
> > $$
> >
> > 这表明最优方向不能包含任何特征值严格大于 $\lambda_j$ 的特征方向分量，只能由特征值等于 $\lambda_j$ 的剩余特征向量线性组合而成。据此分情形讨论：
> > - **最小值可达性**：取 $\mathbf{z} = \pm \mathbf{e}_j$（即 $z_j = \pm 1$，其余 $z_i = 0$），则 $\mathbf{u}_j = Q\mathbf{z} = \pm Q\mathbf{e}_j = \pm \mathbf{q}_j$，经逆白化变换换回原坐标即 $\mathbf{w}_j = B^{-1/2}\mathbf{u}_j = \pm B^{-1/2}\mathbf{q}_j = \pm \mathbf{v}_j$，此时下界 $\Delta(\mathbf{w}_j) = \lambda_j$ 达到；
> > - **单根情形（方向唯一性）**：若 $\lambda_j$ 为单根（$\lambda_{j-1} < \lambda_j < \lambda_{j+1}$，当 $j=1$ 时只需 $\lambda_1 < \lambda_2$），则对一切 $i > j$ 均有 $\lambda_i > \lambda_j$，由取等条件必有 $z_{j+1} = \cdots = z_d = 0$。结合 $z_1 = \cdots = z_{j-1} = 0$ 与 $\sum_{i=j}^d z_i^2 = 1$，得 $z_j^2 = 1 \iff z_j = \pm 1$，故最优方向 $\mathbf{u}_j = \pm \mathbf{q}_j \iff \mathbf{w}_j = \pm \mathbf{v}_j$ 在正负号意义下唯一；
> > - **重根情形（子空间基自由度）**：若 $\lambda_j$ 有重根，记下标集 $I_j := \{i \ge j : \lambda_i = \lambda_j\}$，则对 $i \in I_j$ 有 $(\lambda_i - \lambda_j)z_i^2 = 0$ 恒成立，故凡满足 $\sum_{i \in I_j} z_i^2 = 1$ 且对 $i \notin I_j$ 有 $z_i = 0$ 的单位向量 $\mathbf{u}_j = \sum_{i \in I_j} z_i \mathbf{q}_i$ 均与前 $j-1$ 个方向正交且达到相同最小慢度 $\lambda_j$。逆变换回原坐标，最优解集恰为 $\operatorname{span}\{\mathbf{v}_i : i \in I_j\}$ 中的 $B$-单位向量；在依次选出属于该重根的各个方向时，可在对应广义特征子空间中任取一组 $B$-标准正交基。$\square$

> [!abstract] 命题（矩阵形式：$m$ 维慢子空间总慢度最小化）
> 沿用上述命题的设定与记号。对满足 $B$-标准正交约束 $W^\top B W = I_m$ 的投影矩阵 $W = [\mathbf{w}_1, \ldots, \mathbf{w}_m] \in \mathbb{R}^{d \times m}$，前 $m$ 个慢特征方向的总慢度最小值为
>
> $$
> \min_{W^\top B W = I_m} \operatorname{tr}\!\left(W^\top A W\right) = \sum_{j=1}^m \lambda_j,
> $$
>
> 当取 $W = [\mathbf{v}_1, \ldots, \mathbf{v}_m]$ 时达到最小值。
>
> > [!note]- 证明
> > 对投影矩阵 $W = [\mathbf{w}_1, \ldots, \mathbf{w}_m] \in \mathbb{R}^{d \times m}$，令 $U := B^{1/2} W = [\mathbf{u}_1, \ldots, \mathbf{u}_m] \in \mathbb{R}^{d \times m}$，则 $B$-标准正交约束 $W^\top B W = I_m$ 等价于列正交约束 $U^\top U = I_m$。进一步记 $Z := Q^\top U = [\mathbf{z}_1, \ldots, \mathbf{z}_m] \in \mathbb{R}^{d \times m}$，则 $Z^\top Z = U^\top Q Q^\top U = I_m$。注意到 $Z^\top \Lambda Z$ 的第 $j$ 个对角元为
> >
> > $$
> > \left(Z^\top \Lambda Z\right)_{jj}
> > = \mathbf{z}_j^\top \Lambda \mathbf{z}_j
> > = \sum_{i=1}^d \lambda_i Z_{ij}^2,
> > $$
> >
> > 故投影到 $m$ 个方向后的总慢度为
> >
> > $$
> > \begin{aligned}
> > \sum_{j=1}^m \Delta(\mathbf{w}_j)
> > &= \sum_{j=1}^m \mathbf{w}_j^\top A \mathbf{w}_j \\
> > &= \operatorname{tr}\!\left(W^\top A W\right) \\
> > &= \operatorname{tr}\!\left(U^\top \tilde{A} U\right) \\
> > &= \operatorname{tr}\!\left(Z^\top \Lambda Z\right) \\
> > &= \sum_{j=1}^m \left(Z^\top \Lambda Z\right)_{jj} \\
> > &= \sum_{j=1}^m \sum_{i=1}^d \lambda_i Z_{ij}^2 \\
> > &= \sum_{i=1}^d \lambda_i \left( \sum_{j=1}^m Z_{ij}^2 \right) \\
> > &= \sum_{i=1}^d \lambda_i c_i,
> > \end{aligned}
> > $$
> >
> > 其中 $c_i := \sum_{j=1}^m Z_{ij}^2 = (Z Z^\top)_{ii}$ 为 $Z$ 的第 $i$ 行模长平方。由 [[机器学习/PCA|PCA]] 中的引理（列正交矩阵的行范数性质）知，对所有 $1 \le i \le d$ 有 $0 \le c_i \le 1$，且 $\sum_{i=1}^d c_i = \operatorname{tr}(Z^\top Z) = m$。结合 $0 \le \lambda_1 \le \cdots \le \lambda_d$，有
> >
> > $$
> > \begin{aligned}
> > \sum_{i=1}^d \lambda_i c_i - \sum_{i=1}^m \lambda_i
> > &= \sum_{i=m+1}^d \lambda_i c_i - \sum_{i=1}^m \lambda_i (1 - c_i) \\
> > &\ge \lambda_m \sum_{i=m+1}^d c_i - \lambda_m \sum_{i=1}^m (1 - c_i) \\
> > &= \lambda_m \left( \sum_{i=1}^d c_i - m \right) = 0,
> > \end{aligned}
> > $$
> >
> > 因此
> >
> > $$
> > \operatorname{tr}\!\left(W^\top A W\right)
> > = \sum_{i=1}^d \lambda_i c_i
> > \ge \sum_{i=1}^m \lambda_i.
> > $$
> >
> > 当取 $W = [\mathbf{v}_1, \ldots, \mathbf{v}_m]$ 时，$U = B^{1/2}W = [\mathbf{q}_1, \ldots, \mathbf{q}_m]$，$Z = Q^\top U = [I_m, 0]^\top$，故 $c_1 = \cdots = c_m = 1$，$c_{m+1} = \cdots = c_d = 0$，下界 $\sum_{i=1}^m \lambda_i$ 达到。$\square$

## 离散时间差分形式

对离散时间或给定滞后步长 $\tau > 0$ 的情形，以有限步长差分替代时间导数，慢度目标定义为

$$
\Delta_\tau(\mathbf{w}) := \left\langle \bigl[ y(t+\tau) - y(t) \bigr]^2 \right\rangle_t,
\qquad y(t) = \mathbf{w}^\top \mathbf{x}(t).
$$

记差分向量 $\Delta \mathbf{x}_\tau(t) := \mathbf{x}(t+\tau) - \mathbf{x}(t) \in \mathbb{R}^d$，定义差分协方差矩阵

$$
A_\tau := \left\langle \Delta \mathbf{x}_\tau(t)\Delta \mathbf{x}_\tau(t)^\top \right\rangle_t = \int_T \Delta \mathbf{x}_\tau(t)\Delta \mathbf{x}_\tau(t)^\top\,\mu_T(\mathrm{d}t) \succeq 0,
$$

则 $\Delta_\tau(\mathbf{w}) = \mathbf{w}^\top A_\tau \mathbf{w}$。在约束 $W^\top B W = I_m$ 下，最优投影方向由广义特征值问题

$$
A_\tau \mathbf{w} = \lambda B \mathbf{w}
$$

的前 $m$ 个最小广义特征值对应的 $B$-标准正交特征向量给出。
