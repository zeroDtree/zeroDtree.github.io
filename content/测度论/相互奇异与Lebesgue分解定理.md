---
tags:
  - 测度论
---

## 前置

- [[测度论/绝对连续与Radon-Nikodým定理]]

## 定义

- **定义 8.26** 设 $\nu, \varphi$ 都是 $\mathcal{F}$ 上的符号测度，称 $\nu$ 与 $\varphi$ 相互奇异 (mutually singular)，记作 $\nu \perp \varphi$，如果 $\exists N \in \mathcal{F}$，s.t.

$$\vert{}\nu\vert{}(N) = 0, \quad \vert{}\varphi\vert{}(N^c) = 0.$$

## 性质

1. 绝对连续 $\pm$ 绝对连续 $=$ 绝对连续
   设 $\nu_1, \nu_2, \mu,\nu_1 \pm \nu_2$ 为符号测度
   $$\text{若 } \nu_1 \ll \mu \text{ 且 } \nu_2 \ll \mu \text{，则 } (\nu_1 \pm \nu_2) \ll \mu$$
1. 奇异 $\pm$ 奇异 $=$ 奇异
   设 $\nu_1, \nu_2, \mu, \nu_1 \pm \nu_2$ 为符号测度。
   $$\text{若 } \nu_1 \perp \mu \text{ 且 } \nu_2 \perp \mu \text{，则 } (\nu_1 \pm \nu_2) \perp \mu$$
1. 绝对连续性的局部遗传性 (Local Heredity of Absolute Continuity)：设 $\mu$ 为测度，$\nu$ 为符号测度。若 $\nu \ll \mu$，则对于任意可测子集 $E \in \mathcal{F}$，限制测度依然满足绝对连续性，即：
   $$\nu\vert{}_E \ll \mu\vert{}_E$$
1. 相互奇异性的局部遗传性 (Local Heredity of Mutual Singularity)：设 $\nu, \varphi$ 为符号测度。若 $\nu \perp \varphi$，则对于任意可测子集 $E \in \mathcal{F}$，限制测度依然保持相互奇异，即：
   $$\nu\vert{}_E \perp \varphi\vert{}_E$$
1. 设 $\nu$ 是 $\mathcal{F}$ 上的符号测度，则 $\nu^+ \perp \nu^-$。
1. $\nu \perp \varphi \iff \exists N \in \mathcal{F}$，s.t. $\vert{}\nu\vert{}(N) = 0$，且 $\varphi(A \cap N^c) = 0$，$A \in \mathcal{F}$.
1. 若 $\nu \ll \varphi$，且 $\nu \perp \varphi$，则 $\nu \equiv 0$。
1. **定理 8.28** 若 $\mu$ 为 $\mathcal{F}$ 上的 $\sigma$-有限测度，$\nu$ 为 $\mathcal{F}$ 上的 $\sigma$-有限符号测度，则存在两个 $\sigma$-有限符号测度 $\nu_{ac}$ 和 $\nu_s$，使得
   $$\nu = \nu_{ac} + \nu_s$$且
   $$\nu_{ac} \ll \mu, \quad \nu_s \perp \mu,$$
   并且这种分解是唯一的，称此分解式为 $\nu$ 的 **Lebesgue 分解**，$\nu_{ac}$ 称为 $\nu$ 的绝对连续部分，$\nu_s$ 称为 $\nu$ 的奇异部分。
