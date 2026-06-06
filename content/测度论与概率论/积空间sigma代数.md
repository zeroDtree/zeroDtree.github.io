---
title: 积空间sigma代数
---

## 前置

- [[测度论与概率论/measurable-mapping]]

## 定义

- 设$T$为指标集，$\{(E_t,\mathcal{E}_t)| t \in T\}$为一族可测空间, 令 $\prod_{t \in T} E_t$ 为这族空间的积空间，$\pi_t: \prod_{t \in T} E_t \to E_t$为投影映射。称使得所有投影映射 $\pi_t$ 都可测的最小 $\sigma$-代数 $\bigotimes_{t \in T} \mathcal{E}_t:=\sigma(\bigcup_{t \in T} \sigma(\pi_t)):=\sigma(\bigcup_{t \in T} \pi^{-1}(\mathcal{E}_t))$ 为积空间 $\prod_{t \in T} E_t$ 上的 乘积$\sigma$-代数（当所有 $E_t = E, \mathcal{E}_t = \mathcal{E}$ 时，简记为 $\mathcal{E}^{\otimes T}$）。

## 性质

1. **积 $\sigma$-代数的泛性质（universal property）。**
   设 $(\Omega, \mathcal{F})$ 为可测空间，$Y: \Omega \to \prod_{t \in T} E_t$ 为一个映射。
   则 $Y$ 是 $\mathcal{F} \big/ \big(\bigotimes_{t \in T} \mathcal{E}_t \big)$-可测的，当且仅当对所有的 $t \in T$，复合映射 $\pi_t \circ Y: \Omega \to E_t$ 都是 $\mathcal{F}/ \mathcal{E}_t$-可测的。

## 性质 1 的证明

### 必要性（$\Rightarrow$）

**已知**：$Y: \Omega \to \prod_{t \in T} E_t$ 是 $\mathcal{F} \big/ \big(\bigotimes_{t \in T} \mathcal{E}_t \big)$-可测的。

根据乘积 $\sigma$-代数的定义，对任意固定的 $t \in T$，坐标投影映射 $\pi_t: \prod_{s \in T} E_s \to E_t$ 是 $\big(\bigotimes_{s \in T} \mathcal{E}_s\big) \big/ \mathcal{E}_t$-可测的。

因为两个可测映射的复合映射仍为可测映射，所以复合映射：

$$\pi_t \circ Y: \Omega \to E_t$$

是 $\mathcal{F}/ \mathcal{E}_t$-可测的。

### 充分性（$\Leftarrow$）

**已知**：对所有的 $t \in T$，复合映射 $\pi_t \circ Y: \Omega \to E_t$ 都是 $\mathcal{F}/ \mathcal{E}_t$-可测的。

令 $\mathcal{C}$ 为定义中乘积 $\sigma$-代数的生成元集：

$$\mathcal{C} = \bigcup_{t \in T} \{ \pi_t^{-1}(B_t) \mid B_t \in \mathcal{E}_t \}$$

根据定义，$\bigotimes_{t \in T} \mathcal{E}_t = \sigma(\mathcal{C})$。要证明 $Y$ 可测，只需证明对任意 $A \in \mathcal{C}$，皆有 $Y^{-1}(A) \in \mathcal{F}$。

任取 $A \in \mathcal{C}$，则存在某个特定的 $t_0 \in T$ 以及 $B_{t_0} \in \mathcal{E}_{t_0}$，使得 $A = \pi_{t_0}^{-1}(B_{t_0})$。

考虑 $A$ 在 $Y$ 下的原像：

$$Y^{-1}(A) = Y^{-1}\left(\pi_{t_0}^{-1}(B_{t_0})\right) = (\pi_{t_0} \circ Y)^{-1}(B_{t_0})$$

由已知条件，$\pi_{t_0} \circ Y$ 是 $\mathcal{F}/ \mathcal{E}_{t_0}$-可测的。因为 $B_{t_0} \in \mathcal{E}_{t_0}$，所以其原像必属于 $\mathcal{F}$：

$$Y^{-1}(A) = (\pi_{t_0} \circ Y)^{-1}(B_{t_0}) \in \mathcal{F}$$

由于 $Y^{-1}(\mathcal{C}) \subset \mathcal{F}$，由 $\sigma$-代数原像的性质，其生成的 $\sigma$-代数同样满足包含关系：

$$Y^{-1}\left(\bigotimes_{t \in T} \mathcal{E}_t\right) = Y^{-1}(\sigma(\mathcal{C})) = \sigma(Y^{-1}(\mathcal{C})) \subset \mathcal{F}$$

即 $Y$ 是 $\mathcal{F} \big/ \big(\bigotimes_{t \in T} \mathcal{E}_t \big)$-可测的。 $\blacksquare$
