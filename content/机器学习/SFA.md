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
-
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

> [!abstract] 命题（广义特征值求解与白化等价性）
> 设 $A \succeq 0$，$B \succ 0$。记广义特征值问题 $A \mathbf{w} = \lambda B \mathbf{w}$ 的特征值按升序排列为 $0 \le \lambda_1 \le \lambda_2 \le \cdots \le \lambda_d$，对应的 $B$-标准正交广义特征向量为 $\mathbf{v}_1, \ldots, \mathbf{v}_d$（$\mathbf{v}_i^\top B \mathbf{v}_j = \delta_{ij}$）。则线性 SFA 的第 $j$ 个最小慢度为 $\Delta(\mathbf{w}_j) = \lambda_j$，在 $\mathbf{w}_j = \pm \mathbf{v}_j$ 处达到；若 $\lambda_j$ 为单根，最优方向在正负号意义下唯一，若 $\lambda_j$ 有重根，则可在对应广义特征子空间中任取 $B$-标准正交基。此外，记 $W = [\mathbf{w}_1, \ldots, \mathbf{w}_m] \in \mathbb{R}^{d \times m}$，前 $m$ 个慢特征的总慢度满足
>
> $$
> \min_{W^\top B W = I_m} \operatorname{tr}\!\left(W^\top A W\right) = \sum_{j=1}^m \lambda_j,
> $$
>
> 当取 $W = [\mathbf{v}_1, \ldots, \mathbf{v}_m]$ 时达到最小值。
>
> > [!note]- 证明
> > **1. 白化坐标变换与优化问题等价性：**
> > 因 $B \succ 0$ 为实对称正定矩阵，可作正交特征分解 $B = P D P^\top$，其中 $P \in \mathbb{R}^{d \times d}$ 为正交矩阵，$D = \operatorname{diag}(d_1, \ldots, d_d)$ 且 $d_i > 0$（$1 \le i \le d$）。据此定义对称正定平方根及其逆：
> >
> > $$
> > B^{1/2} := P \operatorname{diag}\!\left(d_1^{1/2}, \ldots, d_d^{1/2}\right) P^\top \succ 0,
> > \qquad
> > B^{-1/2} := P \operatorname{diag}\!\left(d_1^{-1/2}, \ldots, d_d^{-1/2}\right) P^\top \succ 0,
> > $$
> >
> > 满足 $(B^{1/2})^\top = B^{1/2}$、$B^{1/2} B^{1/2} = B$ 及 $B^{-1/2} B B^{-1/2} = I_d$。作可逆线性变量代换（对应白化信号 $\tilde{\mathbf{x}}(t) := B^{-1/2}\mathbf{x}(t)$）：
> >
> > $$
> > \mathbf{u}_j := B^{1/2} \mathbf{w}_j \iff \mathbf{w}_j = B^{-1/2} \mathbf{u}_j,
> > \qquad
> > \tilde{A} := B^{-1/2} A B^{-1/2} = \left\langle \dot{\tilde{\mathbf{x}}}(t)\dot{\tilde{\mathbf{x}}}(t)^\top \right\rangle_t.
> > $$
> >
> > 由于 $A \succeq 0$ 且 $B^{-1/2}$ 对称，有 $\tilde{A}^\top = (B^{-1/2})^\top A^\top B^{-1/2} = \tilde{A}$，且对任意 $\mathbf{z} \in \mathbb{R}^d$ 恒有 $\mathbf{z}^\top \tilde{A} \mathbf{z} = (B^{-1/2}\mathbf{z})^\top A (B^{-1/2}\mathbf{z}) \ge 0$，故 $\tilde{A} \succeq 0$ 为实对称半正定矩阵。在此双射下，原问题的 $B$-标准正交约束与慢度目标分别等价转化为欧氏标准正交约束与关于 $\tilde{A}$ 的二次型：
> >
> > $$
> > \mathbf{w}_i^\top B \mathbf{w}_j = \mathbf{u}_i^\top B^{-1/2} B B^{-1/2} \mathbf{u}_j = \mathbf{u}_i^\top \mathbf{u}_j = \delta_{ij},
> > \qquad
> > \Delta(\mathbf{w}_j) = \mathbf{w}_j^\top A \mathbf{w}_j = \mathbf{u}_j^\top B^{-1/2} A B^{-1/2} \mathbf{u}_j = \mathbf{u}_j^\top \tilde{A} \mathbf{u}_j.
> > $$
> >
> > **2. 广义特征值问题与标准特征值问题的等价性：**
> > 因 $B^{-1/2}$ 可逆，对任意特征对 $(\lambda, \mathbf{w})$ 及对应的 $\mathbf{u} = B^{1/2}\mathbf{w}$，左乘 $B^{-1/2}$ 有
> >
> > $$
> > A \mathbf{w} = \lambda B \mathbf{w}
> > \iff B^{-1/2} A B^{-1/2} \left(B^{1/2} \mathbf{w}\right) = \lambda \left(B^{1/2} \mathbf{w}\right)
> > \iff \tilde{A} \mathbf{u} = \lambda \mathbf{u}.
> > $$
> >
> > 因 $\tilde{A} \succeq 0$ 实对称，可作正交特征分解 $\tilde{A} = Q \Lambda Q^\top$，其中 $\Lambda = \operatorname{diag}(\lambda_1, \ldots, \lambda_d)$（$0 \le \lambda_1 \le \lambda_2 \le \cdots \le \lambda_d$），$Q = [\mathbf{q}_1, \ldots, \mathbf{q}_d]$ 为正交矩阵（$\mathbf{q}_i^\top \mathbf{q}_j = \delta_{ij}$）。令 $\mathbf{v}_j := B^{-1/2} \mathbf{q}_j$（$1 \le j \le d$），则由上述等价性知 $A \mathbf{v}_j = \lambda_j B \mathbf{v}_j$，且
> >
> > $$
> > \mathbf{v}_i^\top B \mathbf{v}_j = \mathbf{q}_i^\top B^{-1/2} B B^{-1/2} \mathbf{q}_j = \mathbf{q}_i^\top \mathbf{q}_j = \delta_{ij},
> > $$
> >
> > 即 $\lambda_1 \le \cdots \le \lambda_d$ 恰为广义特征值问题 $A\mathbf{w} = \lambda B\mathbf{w}$ 的全部广义特征值，$\mathbf{v}_1, \ldots, \mathbf{v}_d$ 为对应的 $B$-标准正交广义特征向量。
> >
> > **3. 逐次最小化慢度与取等条件：**
> > 对第 $j$ 步（$1 \le j \le d$），设前 $j-1$ 个慢特征方向已依次取为 $\mathbf{u}_r = \mathbf{q}_r$（即 $\mathbf{w}_r = \mathbf{v}_r$，$1 \le r \le j-1$）。对任意满足正交与单位化约束 $\mathbf{u}_r^\top \mathbf{u}_j = 0$（$1 \le r < j$）且 $\|\mathbf{u}_j\|_2 = 1$ 的可行向量 $\mathbf{u}_j \in \mathbb{R}^d$，作正交坐标变换 $\mathbf{z} := Q^\top \mathbf{u}_j = (z_1, \ldots, z_d)^\top$。由 $Q$ 的正交性，对任意 $1 \le r \le j-1$ 有
> >
> > $$
> > z_r = \mathbf{q}_r^\top \mathbf{u}_j = \mathbf{u}_r^\top \mathbf{u}_j = 0,
> > $$
> >
> > 且模长满足 $\sum_{i=j}^d z_i^2 = \|\mathbf{z}\|_2^2 = \|\mathbf{u}_j\|_2^2 = 1$。代入慢度目标函数并利用特征值升序关系 $\lambda_j \le \lambda_{j+1} \le \cdots \le \lambda_d$，得
> >
> > $$
> > \Delta(\mathbf{w}_j)
> > = \mathbf{u}_j^\top Q \Lambda Q^\top \mathbf{u}_j
> > = \mathbf{z}^\top \Lambda \mathbf{z}
> > = \sum_{i=j}^d \lambda_i z_i^2
> > \ge \lambda_j \sum_{i=j}^d z_i^2
> > = \lambda_j.
> > $$
> >
> > 上式取等号当且仅当 $\sum_{i=j}^d (\lambda_i - \lambda_j) z_i^2 = 0$，即对所有满足 $\lambda_i > \lambda_j$ 的下标 $i \ge j$ 均有 $z_i = 0$：
> > - 当取 $\mathbf{z} = \pm \mathbf{e}_j$，即 $\mathbf{u}_j = \pm Q \mathbf{e}_j = \pm \mathbf{q}_j \iff \mathbf{w}_j = \pm B^{-1/2}\mathbf{q}_j = \pm \mathbf{v}_j$ 时，下界 $\lambda_j$ 达到；
> > - 若 $\lambda_j$ 为单根（$\lambda_{j-1} < \lambda_j < \lambda_{j+1}$，当 $j=1$ 时只需 $\lambda_1 < \lambda_2$），则对一切 $i > j$ 均有 $\lambda_i > \lambda_j$，故必有 $z_{j+1} = \cdots = z_d = 0$，结合 $\sum_{i=j}^d z_i^2 = 1$ 得 $z_j = \pm 1$，从而最优方向 $\mathbf{w}_j = \pm \mathbf{v}_j$ 在正负号意义下唯一；
> > - 若 $\lambda_j$ 有重根，则凡属于 $\lambda_j$ 对应的特征子空间且与前 $j-1$ 个已选方向正交的单位向量 $\mathbf{u}_j$ 均使等号成立，逆变换回原坐标即对应在 $\lambda_j$ 的广义特征子空间中任取 $B$-标准正交基。
> >
> > **4. $m$ 维子空间总慢度迹最小化：**
> > 对矩阵 $W = [\mathbf{w}_1, \ldots, \mathbf{w}_m] \in \mathbb{R}^{d \times m}$，令 $U := B^{1/2} W = [\mathbf{u}_1, \ldots, \mathbf{u}_m] \in \mathbb{R}^{d \times m}$，则约束 $W^\top B W = I_m$ 等价于列正交约束 $U^\top U = I_m$，总慢度化为 $\operatorname{tr}(W^\top A W) = \operatorname{tr}(U^\top \tilde{A} U)$。记 $Z := Q^\top U \in \mathbb{R}^{d \times m}$，则 $Z^\top Z = U^\top Q Q^\top U = I_m$。定义 $Z$ 的第 $i$ 行模长平方为
> >
> > $$
> > c_i := \sum_{j=1}^m Z_{ij}^2 = \left(Z Z^\top\right)_{ii}, \qquad i = 1, \ldots, d.
> > $$
> >
> > 由 [[机器学习/PCA|PCA]] 中的列正交矩阵引理，将 $Z$ 扩充为 $d \times d$ 正交矩阵可知对所有 $1 \le i \le d$ 有 $0 \le c_i \le 1$，且 $\sum_{i=1}^d c_i = \operatorname{tr}(Z^\top Z) = \operatorname{tr}(I_m) = m$。展开总慢度：
> >
> > $$
> > \operatorname{tr}\!\left(W^\top A W\right)
> > = \operatorname{tr}\!\left(U^\top Q \Lambda Q^\top U\right)
> > = \operatorname{tr}\!\left(Z^\top \Lambda Z\right)
> > = \sum_{j=1}^m \sum_{i=1}^d \lambda_i Z_{ij}^2
> > = \sum_{i=1}^d \lambda_i \left(\sum_{j=1}^m Z_{ij}^2\right)
> > = \sum_{i=1}^d \lambda_i c_i.
> > $$
> >
> > 结合 $0 \le c_i \le 1$、$\sum_{i=1}^d c_i = m$ 以及特征值升序关系 $\lambda_1 \le \cdots \le \lambda_m \le \lambda_{m+1} \le \cdots \le \lambda_d$，作差放缩得
> >
> > $$
> > \begin{aligned}
> > \operatorname{tr}\!\left(W^\top A W\right) - \sum_{i=1}^m \lambda_i
> > &= \sum_{i=1}^d \lambda_i c_i - \sum_{i=1}^m \lambda_i \\
> > &= \sum_{i=m+1}^d \lambda_i c_i - \sum_{i=1}^m \lambda_i (1 - c_i) \\
> > &\ge \lambda_m \sum_{i=m+1}^d c_i - \lambda_m \sum_{i=1}^m (1 - c_i) \\
> > &= \lambda_m \left( \sum_{i=1}^d c_i - m \right) = 0,
> > \end{aligned}
> > $$
> >
> > 故对任意满足 $W^\top B W = I_m$ 的 $W$ 恒有 $\operatorname{tr}(W^\top A W) \ge \sum_{j=1}^m \lambda_j$。当取 $W = [\mathbf{v}_1, \ldots, \mathbf{v}_m]$ 时，$U = B^{1/2}W = [\mathbf{q}_1, \ldots, \mathbf{q}_m]$，$Z = Q^\top U = [I_m, 0]^\top$，此时 $c_1 = \cdots = c_m = 1$ 且 $c_{m+1} = \cdots = c_d = 0$，达到最小值 $\sum_{j=1}^m \lambda_j$。$\square$

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
