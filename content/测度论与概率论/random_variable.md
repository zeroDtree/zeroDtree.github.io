---
title: 随机变量-像测度与概率分布
---

## 前置

[[测度论与概率论/measurable-func]]

## 定义

- 设$f:(\Omega, \mathcal{F}, P) \to (E, \mathcal{E}))$为可测映射，令$\mu \circ f^{-1}(B)=\mu (f^{-1}(B)),B\in\mathcal{E}$，则$\mu \circ f^{-1}$是$(E, \mathcal{E})$上的测度，从而$(E, \mathcal{E},\mu \circ f^{-1})$为一新的测度空间。称$\mu \circ f^{-1}$为$\mu$在$f$下的**像测度**(image measure). 称$P$在$X$下的像测度$P_X:=P\circ X$为$X$的概率分布.若$\mu$是概率测度，则$\mu \circ f^{-1}$也是概率测度。
- 设$(\Omega, \mathcal{F}, P)$为概率空间，$E$为度量空间，若$X$是从$(\Omega, \mathcal{F}, P)$到$(E, \mathcal{B}(E))$的可测映射，则称$X$为从$(\Omega, \mathcal{F}, P)$到$E$的**随机元**(random element)。当$(E, \mathcal{B}(E))=(\mathbb{R}, \mathcal{B}(\mathbb{R}))$时，称$X$为**随机变量**(random variable, r.v.)。
- 设$X$为一随机变量，$F(x):=P_X((-\infty, x])=:P(X\leq x)$，易知$F$满足d.f.的定义，称$F$为$X$的**分布函数**，记作$X \sim F$
- 当$(E,\mathcal{E})=(\mathbb{R}^n, \mathcal{B}(\mathbb{R}^n))$时，称$\mathbb{R}^n$值随机元为**随机向量**(random vector, R.V.)。用常用黑体$\mathbf{X}$表示。
- 当$(E,\mathcal{E})=(\mathbb{C}, \mathcal{B}(\mathbb{C}))$时，称$\mathbb{C}$值随机元为**复值随机变量**(complex random variable, c.r.v.)。用常用黑体$\mathbf{X}$表示。

## 性质

1. 设$L:\mathbb{R}^n\to \mathbb{R}^n$为可逆线性变换，$\lambda$是$\mathbb{R}^n$上的$L$测度与，则$\lambda \circ L = |\det L| \lambda$。
2. $\mathbf{X}$为R.V. $\iff$ 诸分量$X_i$为r.v.
3. 设$F(x)$为d.f., 则存在某个概率空间$(\Omega, \mathcal{F}, P)$上的r.v. $X$使得$X \sim F$。
4. 设$F(\mathbf{x})$为d维d.f., 则存在某个概率空间$(\Omega, \mathcal{F}, P)$上的R.V. $\mathbf{X}$使得$\mathbf{X} \sim F$。
5. $\mathbf{X}$为c.r.v. $\iff$ 诸分量实部$Re X$与虚部$Im X$都为r.v.
