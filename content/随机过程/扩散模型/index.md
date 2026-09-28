---
title: 扩散模型
aliases:
  - /随机过程/diffusion/扩散分类
  - /机器学习/diffusion/扩散分类
  - /随机过程/diffusion/离散分布的连续时间扩散
  - /机器学习/diffusion/离散分布的连续时间扩散
---

## 前置

- [[随机过程/基础/随机过程]]
- [[随机过程/生成模型/生成模型导论]]

## 概率设置

设：

- $(\Omega,\mathcal F,\mathbb P)$ 为概率空间；
- $(E,\mathcal E)$ 为标准 Borel 状态空间；
- $\mathbb T$ 为以 $0$ 为起点、以 $T$ 为终点的全序时间集；
- $X=(X_t)_{t\in\mathbb T}$ 为取值于 $E$ 的随机过程。

记 $P_t=\mathbb P\circ X_t^{-1}$ 为 $X_t$ 的边缘分布。扩散生成模型构造一条从数据分布到易采样参考分布的概率路径：

$$
P_0=P_{\mathrm{data}},
\qquad
P_T\approx\Pi.
$$

称

$$
q:E\times\mathcal E\to[0,1]
$$

为 $(E,\mathcal E)$ 上的**概率核**，若：

1. 对每个固定的 $A\in\mathcal E$，映射 $x\mapsto q(x,A)$ 是 $\mathcal E$-可测的；
2. 对每个固定的 $x\in E$，映射 $A\mapsto q(x,A)$ 是 $(E,\mathcal E)$ 上的概率测度。

这里第二个输入是可测集合，而不是“终点状态”；若核有密度或质量函数，才常把它简写成 $q(y\mid x)$。

因为 $E$ 是标准 Borel 空间，对任意 $s<t$ 都存在正则条件概率核

$$
q_{t\mid s}(x,A)
:=\mathbb P(X_t\in A\mid X_s=x),
$$

以及

$$
q^\leftarrow_{s\mid t}(y,A)
:=\mathbb P(X_s\in A\mid X_t=y).
$$

二者分别只在 $P_s$-几乎处处与 $P_t$-几乎处处意义下唯一，并满足边缘一致性

$$
P_t(A)=\int_E q_{t\mid s}(x,A)\,P_s(\mathrm dx),
\qquad
P_s(A)=\int_E q^\leftarrow_{s\mid t}(y,A)\,P_t(\mathrm dy).
$$

仅仅对每一对 $s<t$ 选取二时条件核，并**不能**自动得到一个 Markov family。要称其为 Markov 转移族，还需选取彼此相容的版本，使 Chapman--Kolmogorov 方程

$$
q_{t\mid r}(x,A)
=\int_E q_{t\mid s}(y,A)\,q_{s\mid r}(x,\mathrm dy),
\qquad r<s<t,
$$

在适当意义下成立；对具体过程还需假设

$$
\mathbb P(X_t\in A\mid \sigma(X_u:u\le s))
=q_{t\mid s}(X_s,A).
$$

## 四象限

按状态空间和时间集的离散、连续性质，本文体系对应如下：

- **离散状态、离散时间**：[[随机过程/扩散模型/离散状态/离散时间扩散]]，即 D3PM。
- **离散状态、连续时间**：本体系目前没有可完整迁移的实质源内容，暂不展开，也不建立空笔记。
- **连续状态、离散时间**：[[随机过程/扩散模型/连续状态/离散时间扩散]]，以 DDPM 为主。
- **连续状态、连续时间**：[[随机过程/扩散模型/连续状态/连续时间扩散]]，以 Score-SDE 与 probability-flow ODE 为主。

跨象限反复使用的结论分别放在：

- **线性理论**：[[随机过程/扩散模型/线性高斯扩散]]
- **训练理论**：[[随机过程/扩散模型/分数匹配]]
- **条件生成**：[[随机过程/扩散模型/条件扩散]]
- **设计空间**：[[随机过程/扩散模型/EDM]]
- **工程约定**：[[随机过程/扩散模型/实现约定]]
