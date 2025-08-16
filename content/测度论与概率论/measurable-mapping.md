---
title: 可测映射与随机变量
---

## Prerequisites

- [[测度论与概率论/class-of-sets]]

## 定义

- 可测映射：设$f:\Omega \rightarrow E$，其中$(\Omega, \mathcal{F})$和$(E,\mathcal{E})$是可测空间, 若$\mathcal{E}$中的元素在$f$下的逆像都是$\mathcal{F}$中的元素，则称$f$为可测映射。记作$f\in \mathcal{F}/\mathcal{E}$。
- Borel可测映射：若可测映射的$\Omega$和$E$为拓扑空间，且$\mathcal{F}=\mathcal{B}(\Omega)$, $\mathcal{E}=\mathcal{B}(E)$，则称$f$为Borel可测映射。
- 通过定义域构造$\sigma$代数： $\{(E_t, \mathcal{E_t}), t\in T\}$是一族可测空间,且诸$f_t:\Omega \to E_t$, $\sigma(f_t, t \in T)$:= $\sigma(\bigcup_{t\in T} \sigma(f_t))= \sigma(\bigcup_{t\in T} f_t^{-1}(\mathcal{E}_t))$ 是$\Omega$上使得每个$f_t$可测的最小$\sigma$-代数。
- 通过值域构造$\sigma$代数：$\mathcal{E}=\{A \subseteq E: g^{-1}(A)\in \mathcal{F}\}$是$E$上使得$g$可测的最大$\sigma$-代数。$\mathcal{E}=\bigcap_{t\in T}\{A \subseteq E: g^{-1}_t(A)\in \mathcal{F}\}$是E上使得每个$g_t$可测的最大$\sigma$-代数。

## 性质

- 若$f\in \mathcal{F}_1/\mathcal{E}, \mathcal{F}_1 \subseteq {F}_2$, 则$f\in \mathcal{F}_2/\mathcal{E}$
- 可测映射的复合仍为可测映射
- 连续映射可测
- 若$(\Omega, \mathcal{F})$和$(E,\mathcal{E})$为可测空间, 且$\sigma(\mathcal{C})=\mathcal{E}$，则$f\in \mathcal{F}/\mathcal{E} \Leftrightarrow f^{-1}(\mathcal{C}) \subseteq \mathcal{F}$
- 设$(\Omega, \mathcal{F}),(E,\mathcal{E})$为可测空间，$f:\Omega \to E$, $T$是任意非空指集，若$\forall t \in T, (S_t,\mathcal{S}_t)$是可测空间,且$\phi_t:E \to S_t$是可测映射，且$\mathcal{E}=\sigma(\phi_t, t\in T)$,则$f\in \mathcal{F}/\mathcal{E} \Leftrightarrow \forall t \in T, \phi_t \circ f \in \mathcal{F}/\mathcal{S}_t$
