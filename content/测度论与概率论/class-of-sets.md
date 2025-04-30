---
title: 集类
date: 2024-12-02 22:52:52
tags: 测度论
---

### 定义

以下$\mathcal{E}$ 是$\Omega$ 上的集类(class of sets)

称$\mathcal{E}$为$\Omega$上的$\pi$类，若$\mathcal{E}$ 对有限交运算封闭。

称$\mathcal{E}$为$\Omega$上的半环(semi-ring),若 1）$\emptyset \in \mathcal{E}$，2）$\mathcal{E}$ 是$\pi$类，3）$\mathcal{E}$ 中任意两元素之差能表示成$\mathcal{E}$中元素的有限不交并

称$\mathcal{E}$是$\Omega$上的一个半代数 (semi-algebra), 若$\mathcal{E}$ 是半环，且$\Omega \in \mathcal{E}$

称$\mathcal{E}$是$\Omega$上的一个代数 (algebra), 若 1）$\Omega(\emptyset) \in \mathcal{E}$，2)$\mathcal{E}$ 对补运算封闭，3)$\mathcal{E}$ 对有限并(交)运算封闭

称$\mathcal{E}$是$\Omega$上的$\sigma$代数(sigma-algebra), 若 1）$\Omega(\emptyset) \in \mathcal{E}$，2)$\mathcal{E}$ 对补运算封闭，3)$\mathcal{E}$ 对(至多)可数并运算封闭

称$\mathcal{E}$是单调类(monotone class), 若$\mathcal{E}$ 对单调上升序列的极限封闭,又对单调下降序列的极限封闭

称$\mathcal{E}$是$\lambda$类(lambda class), 若 1）$\Omega \in \mathcal{E}$，2）$\mathcal{E}$ 对真差封闭，3）$\mathcal{E}$ 对单调上升序列的极限封闭

称$(\Omega,\mathcal{E})$为可测空间(measurable space), 若$\mathcal{E}$是$\Omega$上的$\sigma$代数

称$\sigma(\tau)$ 为 $X$上的 Borel $\sigma$代数，若$\tau$为拓扑空间$(X,\tau)$的拓扑,称其中的元素 Borel 集

称$(X,\sigma(\tau),\tau)$为 可测拓扑空间，若$\sigma(\tau)$为$X$上的 Borel $\sigma$代数，$\tau$为$X$上的拓扑, $\sigma(\tau)$也被记作$\mathcal{B}(X)$

![[测度论与概率论/class_of_sets/sigma.png]]

### 性质

1. 设$\mathcal{E}$为半环, 若$A_1,A_2,\cdots,A_n,B_1,B_2,\cdots,B_m\in \mathcal{E}$，则$\bigcup_{i=1}^{n}A_i$和$\left(\bigcup_{i=1}^{n}A_i\right)\setminus \left(\bigcup_{j=1}^{m}B_j\right)$ 都可以表示成$\mathcal{E}$中元素的有限不交并
2. 若$F$是代数，则以下四个命题等价：1）$F$是$\sigma$代数，2）$F$对单调下降序列的极限封闭，3）$F$对单调上升序列的极限封闭，4）$F$对可列(可数)不交并封闭
3. $\sigma$代数$=$ 代数 $+$ 单调类
4. $\sigma$代数$=$ $\pi$类 $+$ $\lambda$类
5. 有限集上的代数是$\sigma$代数
6. 若一族集类$X=\{\mathcal{A_t},t\in T\,A_t\text{对}\Delta\text{封闭}\}$,$\Delta$为某种运算，则$\bigcap_{t\in T}\mathcal{A}_t$也对$\Delta$封闭
7. 对任意非空集类$\mathcal{E}$，存在一个最小的包含$\mathcal{E}$的$\sigma$代数$\sigma(\mathcal{E})$，称$\sigma(\mathcal{E})$为由$\mathcal{E}$生成的$\sigma$代数，$\Omega$为$\sigma(\mathcal{E})$的生成元
8. 单调类定理：若$\mathcal{E}$为代数，则$\mathcal{M}(\mathcal{E})=\sigma(\mathcal{E})$，即由代数生成的单调类与$\sigma$代数相等
9. $\pi-\lambda$定理：若$\mathcal{E}$为$\pi$类，则$\lambda(\mathcal{E})=\sigma(\mathcal{E})$，即由$\pi$类生成的$\lambda$类与$\sigma$代数相等
10. 单调类方法论：设$\mathcal{E},\mathcal{A}$为两个集类，且$\mathcal{E}\subset \mathcal{A}$，若$\mathcal{E}$为代数，$\mathcal{A}$为单调类，则$\sigma(\mathcal{E})\subset \mathcal{A}$
11. $\pi-\lambda$方法论：设$\mathcal{E}$为$\pi$类，$\mathcal{A}$为$\lambda$类，且$\mathcal{E}\subset \mathcal{A}$，则$\sigma(\mathcal{E})\subset \mathcal{A}$
12. 设$f:\Omega \to E$,$\mathcal{E}$为$E$上的非空集类，记$f^{-1}(\mathcal{E})=\{f^{-1}(A):A\in \mathcal{E}\}$，若$\mathcal{E}$为$\sigma$代数，则$f^{-1}(\mathcal{E})$为$\sigma$代数。
13. $f^{-1}(\sigma(\mathcal{E}))=\sigma(f^{-1}(\mathcal{E}))$
14. 第二可数空间中$(X,\tau)$，$\mathcal{B}$为$\tau$的基,$\mathcal{S}$为$\tau$的子基，则$\sigma(\tau)=\sigma(\mathcal{S})=\sigma(\mathcal{B})$
15. 设$\mathcal{F}$为$\mathcal{\Omega}$上的$\sigma$代数，$\Omega_0$是$\Omega$的一个子集，则$\Omega_0 \cap \mathcal{F} = \{A \cap \Omega_0: A \in \mathcal{F}\}$为$\Omega_0$上的$\sigma$代数。
16. 设$\emptyset \not= \Omega_0 \subseteq \Omega$, $\mathcal{E}$为$\Omega$上一集类，则$\sigma_{\Omega_0}(\Omega_0 \cap \mathcal{E})= \Omega_0 \cap \sigma_{\Omega}(\mathcal{E})$