---
title: 测度论
---

## 广义实值集函数(extended real-valued set function)

设$\mathcal{E}$为$\Omega$上的集类，则称$\mu:\mathcal{E}\to \overline{\mathbb{R}}$为广义实值集函数。

- 有限可加性：$\forall A_1,A_2,\cdots,A_n\in \mathcal{E} \wedge A_i\cap A_j=\emptyset, i\neq j$，则$\mu\left(\biguplus_{i=1}^{n}A_i\right)=\sum_{i=1}^{n}\mu(A_i)$
- 可列可加性：$\forall A_1,A_2,\cdots\in \mathcal{E} \wedge A_i\cap A_j=\emptyset, i\neq j$，则$\mu\left(\biguplus_{i=1}^{\infty}A_i\right)=\sum_{i=1}^{\infty}\mu(A_i)$
- 有限次可加性：$\forall A,A_1,A_2,\cdots,A_n\in \mathcal{E} \wedge A \subseteq \bigcup_{i=1}^{n}A_i$，则$\mu(A)\leq \sum_{i=1}^{n}\mu(A_i)$
- 可列次可加性：$\forall A,A_1,A_2,\cdots\in \mathcal{E} \wedge A \subseteq \bigcup_{i=1}^{\infty}A_i$，则$\mu(A)\leq \sum_{i=1}^{\infty}\mu(A_i)$
- $\mu$在$\emptyset$处连续: $A_n \downarrow \emptyset \Longrightarrow \mu(A_n) \downarrow \mu(\emptyset)$

## 有限可加测度

$\mathcal{E}$为$\Omega$上的集类，$\mu:\mathcal{E}\to \overline{\mathbb{R}}$，称$\mu$为有限可加测度，若$\mu$满足：

- 非负性：$\forall A\in \mathcal{E},\mu(A)\geq 0$
- 有限可加性
- 有研究价值：存在$A_0\in \mathcal{E}$，使得$\mu(A_0)<\infty$

#### 性质

1. 若$\emptyset \in \mathcal{E}$，则$\mu(\emptyset)=0$
2. 若$\mu$为半环$\mathcal{E}$上有限可加测度，则$A,B\in \mathcal{E} \wedge A\subseteq B \Longrightarrow \mu(A)\leq \mu(B)$
3. 若$\mu$为半环$\mathcal{E}$上有限可加测度，则$A,B\in \mathcal{E} \wedge A\subseteq B \wedge B\backslash A \in \mathcal{E} \wedge \mu(A)<\infty \Longrightarrow \mu(B-A)=\mu(B)-\mu(A)$
4. 若$\mu$为半环$\mathcal{E}$上有限可加测度，则$A,A_1,A_2,\cdots A_n \in \mathcal{E} \wedge A_i\cap A_j=\emptyset, i\neq j \wedge \biguplus_{i=1}^{n}A_i \subseteq A \Longrightarrow \sum_{i=1}^{n}\mu(A_i) \leq \mu(A)$
5. 若$\mu$为半环$\mathcal{E}$上有限可加测度，则$A,A_1,A_2,\cdots \in \mathcal{E} \wedge A_i\cap A_j=\emptyset, i\neq j \wedge \biguplus_{i=1}^{\infty}A_i \subseteq A \Longrightarrow \sum_{i=1}^{\infty}\mu(A_i) \leq \mu(A)$
6. 若$\mu$为半环$\mathcal{E}$上有限可加测度,则其具有有限次可加性

## 可列可加测度(简称测度)

$\mathcal{E}$为$\Omega$上的集类，$\mu:\mathcal{E}\to \overline{\mathbb{R}}$，称$\mu$为可列可加测度，若$\mu$满足：

- 非负性：$\forall A\in \mathcal{E},\mu(A)\geq 0$
- 可列可加性
- 有研究价值：存在$A_0\in \mathcal{E}$，使得$\mu(A_0)<\infty$

有限 : $\forall A\in \mathcal{E}, \mu(A)<\infty$
$\sigma$ 有限：$\forall A\in \mathcal{E}, \exists \{A_n\}_{n=1}^{\infty}\in \mathcal{E}, s.t. A \subseteq \cup_{n=1}^{\infty}A_n \wedge \mu(A_n)<\infty$

#### 性质

1. 若$\emptyset \in \mathcal{E}$，则$\mu(\emptyset)=0$
2. $\mu$为测度，若$\emptyset \in \mathcal{E}$，$\mu$为有限可加测度
3. 半环上的测度具有可列次可加性
4. 半环上的测度 向上(从下)连续，即$A_n \in \mathcal{E} \wedge A_n \uparrow \wedge \lim\limits_{n \to \infty} A_n \in \mathcal{E} \Longrightarrow \lim\limits_{n \to \infty} \mu(A_n) = \mu(\lim\limits_{n \to \infty} A_n)$
5. 半环上的测度 向下(从上)连续，即$A_n \in \mathcal{E} \wedge A_n \downarrow \wedge \lim\limits_{n \to \infty} A_n \in \mathcal{E} \wedge \exist n_0 \text{ s.t. } \mu(A_{n_0})<\infty \Longrightarrow \lim\limits_{n \to \infty} \mu(A_n) = \mu(\lim\limits_{n \to \infty} A_n)$
6. 设$\mu$为半环$\mathcal{E}$上的有限可加测度，则下列各条件等价
   - $\mu$为测度
   - $\mu$为具有可列次可加性
   - $A_1,A_2,\cdots \in \mathcal{E} \wedge \cup_{i=1}^{\infty}A_i \in \mathcal{E} \Longrightarrow \sum_{i=1}^{\infty}\mu(A_i) \leq \mu(\cup_{i=1}^{\infty}A_i)$
7. 设$\mathcal{E}$ 为代数，若$\mu:\mathcal{E}\to \mathbb{R}$具有非负性和有限可加性，则($\mu$在$\emptyset$处连续 $\Longrightarrow$ $\mu$为测度)

## 测度空间

若 $(\Omega, \mathcal{F})$可测空间，$\mu$为$\mathcal{F}$上测度，则称$(\Omega, \mathcal{F}, \mu)$为**测度空间**。

若$(\Omega, \mathcal{F}, \mu)$为测度空间，且$\mu(\Omega)=1$，则称$\mu$为概率测度,称$(\Omega, \mathcal{F}, \mu)$为**概率空间**。

称可测拓扑空间$(X, \mathcal{B}(X), \mathcal{T})$上的测度为**Borel测度**。

## 外测度

称$\mu^*:\mathcal{P}(\Omega)\to \overline{\mathbb{R}}$为外测度，若$\mu^*$满足：

- $\mu^*(\emptyset)=0$
- 单调性：$A\subseteq B \Longrightarrow \mu^*(A)\leq \mu^*(B)$
- 可列次可加性：$A_1,A_2,\cdots \in \mathcal{P}(\Omega) \Longrightarrow \mu^*(\bigcup_{i=1}^{\infty}A_i) \leq \sum_{i=1}^{\infty}\mu^*(A_i)$

### 外测度的性质

- 非负性：$\forall A\in \mathcal{P}(\Omega), \mu^*(A)\geq 0$
- 有限次可加性：$\forall A_1,A_2,\cdots,A_n\in \mathcal{P}(\Omega), \mu^*(\bigcup_{i=1}^{n}A_i) \leq \sum_{i=1}^{n}\mu^*(A_i)$

### 由外测度诱导的测度

设$\mu^*$为$\Omega$上的外测度，称$A \in \mathcal{P}(\Omega)$为$\mu^*$-可测，若
$$\forall B \in \mathcal{P}(\Omega), \mu^*(B) = \mu^*(B \cap A) + \mu^*(B \cap A^c)$$

因为外测度具有有限次可加性，所以上式等价于

$$\forall B \in \mathcal{P}(\Omega), \mu^*(B) \geq \mu^*(B \cap A) + \mu^*(B \cap A^c)$$

$\mathcal{U}_{\mu^*}$表示所有的$\mu^*$-可测集构成的集类，简称为$\mu^*$-可测集类。

$\mathcal{U}_{\mu^*}$具有如下性质

- $\emptyset \in \mathcal{U}_{\mu^*}$, $\Omega \in \mathcal{U}_{\mu^*}$
- $\mu^*(A)=0 \Longrightarrow \mathcal{P}(A) \subseteq \mathcal{U}_{\mu^*}$
- $A \in \mathcal{U}_{\mu^*} \Longrightarrow A^c \in \mathcal{U}_{\mu^*}$
- $\mathcal{U}_{\mu^*}$为$\Omega$上的$\sigma$-代数
- $\mu^*$限制到$\mathcal{U}_{\mu^*}$上为测度，称为由$\mu^*$诱导的测度，记为$\mu^*|_{\mathcal{U}_{\mu^*}}$

### 由半环上的测度诱导的外测度

设$\mu$为半环$\mathcal{E}$上的测度，对于任意的$A \in \mathcal{P}(\Omega)$，定义

$$\mu^*(A) = \inf \left\{ \sum_{i\in I} \mu(A_i) \mid I  \subseteq \mathbb{N}, A_i \in \mathcal{E}, A \subseteq \bigcup_{i\in I} A_i \right\}$$

$\mu^*$有如下性质

- $\mu^*$限制到$\mathcal{E}$与$\mu$一致
- $\mu^*$为$\Omega$上的外测度, 称之为由$\mu$诱导的外测度

设$\mu^*$为半环$\mathcal{E}$上的测度诱导的外测度，则$A \in \mathcal{U}_{\mu^*}$当且仅当

$$\forall B \in \mathcal{E}, \mu^*(B) = \mu^*(B \cap A) + \mu^*(B \cap A^c)$$

## 测度扩张定理

设$\mathcal{E}_1,\mathcal{E}_2$为$\Omega$上的集类，$\mathcal{E}_1 \subseteq \mathcal{E}_2$，$\mu_i$是$\mathcal{E}_i$上的测度或有限可加测度，若 $\forall A \in \mathcal{E}_1, \mu_1(A) = \mu_2(A)$，则称$\mu_2$是$\mu_1$的在$\mathcal{E}_2$**扩张**, $\mu_1$是$\mu_2$在$\mathcal{E}_1$的**限制**。

设$\mathcal{E}$为$\Omega$上的$\pi$类，$\mu_1,\mu_2$是$\mathcal{E}$上的两个有限测度。若($\mu_1(A)=\mu_2(A), \forall A \in \mathcal{E} \wedge \mu_1(\Omega)=\mu_2(\Omega)$)，则$\mu_1(A)=\mu_2(A), \forall A \in \sigma(\mathcal{E})$。

设$\mu$为半环$\mathcal{E}$上的测度，则

- $\mu$在$\sigma(\mathcal{E})$上的扩张必然存在，因为$\sigma(\mathcal{E})\subseteq \mathcal{U}_{\mu^*}$
- 若$\mu$还在$\mathcal{E}$上$\sigma$-有限,且$\Omega$可以表示成$\mathcal{E}$中元素的可列并，则$\mu$在$\sigma(\mathcal{E})$上的扩张唯一,且所得的测度在$\sigma(\mathcal{E})$上$\sigma$-有限
