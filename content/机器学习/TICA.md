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

给定中心化时间序列 $\mathbf{x}(t)\in\mathbb{R}^d$ 与滞后 $\tau>0$，TICA 在单位方差与 $C_0$-正交约束下，依次寻找使投影信号滞后自相关最大的线性方向。该自相关是 $C_\tau^{\mathrm{sym}}$ 相对 $C_0$ 的广义 Rayleigh 商。

## 定义

沿用 [[机器学习/SFA#离散时间差分形式|SFA]] 的配对窗口 $T_\tau=\{t\in T:t+\tau\in T\}$，协方差取 $\mu_T$ 在 $T_\tau$ 上的归一化平均：

$$
C_0=\langle\mathbf{x}(t)\mathbf{x}(t)^\top\rangle_{t,\tau},\qquad
C_\tau=\langle\mathbf{x}(t)\mathbf{x}(t+\tau)^\top\rangle_{t,\tau},\qquad
C_\tau^{\mathrm{sym}}=\frac{C_\tau+C_\tau^\top}{2}.
$$

$C_0\succeq0$。$C_\tau$ 一般不对称，但反对称部分对 $\mathbf{w}^\top C_\tau\mathbf{w}$ 没有贡献，因此

$$
\rho_\tau(\mathbf{w})=\frac{\mathbf{w}^\top C_\tau^{\mathrm{sym}}\mathbf{w}}{\mathbf{w}^\top C_0\mathbf{w}}.
$$

设 $C_0\succ0$、$1\le m\le d$，TICA 依次取

$$
\mathbf{w}_j=\arg\max_{\substack{\mathbf{w}^\top C_0\mathbf{w}=1\\ \mathbf{w}_i^\top C_0\mathbf{w}=0,\ i<j}}\rho_\tau(\mathbf{w}),
\qquad
\lambda_j=\rho_\tau(\mathbf{w}_j).
$$

$W_m=[\mathbf{w}_1,\ldots,\mathbf{w}_m]$ 是方向矩阵，$\mathbf{z}(t)=W_m^\top\mathbf{x}(t)$ 是 $m$ 个成分。

## 与广义 Rayleigh 商的对应

$\rho_\tau$ 是 $A=C_\tau^{\mathrm{sym}}$、$B=C_0$ 的广义 Rayleigh 商。[[机器学习/广义Rayleigh商#变分刻画|逐次变分]] 表明 $\lambda_1\ge\cdots\ge\lambda_m$ 是 $C_\tau^{\mathrm{sym}}\mathbf{w}=\lambda C_0\mathbf{w}$ 的前 $m$ 个最大特征值，$\mathbf{w}_j$ 为对应的 $C_0$-标准正交特征向量；矩阵形式为

$$
\max_{W^\top C_0W=I_m}\operatorname{tr}\left(W^\top C_\tau^{\mathrm{sym}}W\right)=\sum_{j=1}^m\lambda_j
$$

等号在 $W=[\mathbf{w}_1,\ldots,\mathbf{w}_m]$ 处达到，最优子空间由这 $m$ 个特征向量张成。

白化为 $K_\tau=C_0^{-1/2}C_\tau^{\mathrm{sym}}C_0^{-1/2}$ 后，$\mathbf{q}_j$ 是 $K_\tau$ 对应 $\lambda_j$ 的单位特征向量，$\mathbf{w}_j=C_0^{-1/2}\mathbf{q}_j$，且 $\mathbf{w}_i^\top C_0\mathbf{w}_j=\delta_{ij}$。