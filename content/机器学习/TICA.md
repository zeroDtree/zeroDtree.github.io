
## 2. 时间滞后独立成分分析（TICA）

设中心化时间序列为 $\mathbf{x}(t) \in \mathbb{R}^d$。给定滞后时间 $\tau > 0$，定义零滞后协方差矩阵 $C_0$、时间滞后协方差矩阵 $C_\tau$ 及其对称化矩阵 $C_\tau^{\mathrm{sym}}$：

$$
C_0 := \left\langle \mathbf{x}(t)\mathbf{x}(t)^\top \right\rangle_t = \int_T \mathbf{x}(t)\mathbf{x}(t)^\top\,\mu_T(\mathrm{d}t),
\qquad
C_\tau := \left\langle \mathbf{x}(t)\mathbf{x}(t+\tau)^\top \right\rangle_t = \int_T \mathbf{x}(t)\mathbf{x}(t+\tau)^\top\,\mu_T(\mathrm{d}t),
\qquad
C_\tau^{\mathrm{sym}} := \frac{1}{2}\left( C_\tau + C_\tau^\top \right).
$$

对线性投影 $y(t) = \mathbf{w}^\top \mathbf{x}(t)$，其滞后 $\tau$ 的自相关系数定义为

$$
\rho_\tau(\mathbf{w}) := \frac{\mathbf{w}^\top C_\tau^{\mathrm{sym}} \mathbf{w}}{\mathbf{w}^\top C_0 \mathbf{w}}.
$$

线性 TICA 在 $C_0$-正交与单位方差约束下依次最大化自相关：

$$
\begin{aligned}
\max_{\mathbf{w}_i} \quad & \mathbf{w}_i^\top C_\tau^{\mathrm{sym}} \mathbf{w}_i \\
\text{s.t.} \quad & \mathbf{w}_i^\top C_0 \mathbf{w}_j = \delta_{ij}, \qquad 1 \le j \le i.
\end{aligned}
$$

取前 $m$ 个方向组成投影矩阵 $W_m = [\mathbf{w}_1, \ldots, \mathbf{w}_m] \in \mathbb{R}^{d \times m}$，则 $m$ 维慢子空间投影定义为 $\mathbf{z}(t) = W_m^\top \mathbf{x}(t) \in \mathbb{R}^m$。
