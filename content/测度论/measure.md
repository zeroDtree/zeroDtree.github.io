---
title: 测度
---

## Prerequisites

- [[测度论/class-of-sets]]

## 广义实值集函数(extended real-valued set function)

### 定义

设$\mathcal{E}$为$\Omega$上的集类，则称$\mu:\mathcal{E}\to \overline{\mathbb{R}}$为广义实值集函数。

- 有限可加性：$\forall A_1,A_2,\cdots,A_n\in \mathcal{E} \wedge A_i\cap A_j=\emptyset, i\neq j$，则$\mu\left(\biguplus_{i=1}^{n}A_i\right)=\sum_{i=1}^{n}\mu(A_i)$
- 可列可加性：$\forall A_1,A_2,\cdots\in \mathcal{E} \wedge A_i\cap A_j=\emptyset, i\neq j$，则$\mu\left(\biguplus_{i=1}^{\infty}A_i\right)=\sum_{i=1}^{\infty}\mu(A_i)$
- 有限次可加性：$\forall A,A_1,A_2,\cdots,A_n\in \mathcal{E} \wedge A \subseteq \bigcup_{i=1}^{n}A_i$，则$\mu(A)\leq \sum_{i=1}^{n}\mu(A_i)$
- 可列次可加性：$\forall A,A_1,A_2,\cdots\in \mathcal{E} \wedge A \subseteq \bigcup_{i=1}^{\infty}A_i$，则$\mu(A)\leq \sum_{i=1}^{\infty}\mu(A_i)$
- $\mu$在$\emptyset$处连续: $A_n \downarrow \emptyset \Longrightarrow \mu(A_n) \downarrow \mu(\emptyset)$

## 有限可加测度

### 定义

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
7. 有限可加测度的容斥原理： $\mu(\bigcup_{i=1}^n A_i)=\sum_{k=1}^{n} (-1)^{k+1} \sum_{1\leq i_1 < \cdots < i_k \leq n} \mu(A_{i_1} \cap \cdots \cap A_{i_k})$

## 可列可加测度(简称测度)

### 定义

$\mathcal{E}$为$\Omega$上的集类，$\mu:\mathcal{E}\to \overline{\mathbb{R}}$，称$\mu$为可列可加测度，若$\mu$满足：

- 非负性：$\forall A\in \mathcal{E},\mu(A)\geq 0$
- 可列可加性
- 有研究价值：存在$A_0\in \mathcal{E}$，使得$\mu(A_0)<\infty$

有限 : $\forall A\in \mathcal{E}, \mu(A)<\infty$
$\sigma$ 有限（$\sigma$-有限，sigma有限）：$\forall A\in \mathcal{E}, \exists \{A_n\}_{n=1}^{\infty}\in \mathcal{E}, s.t. A \subseteq \cup_{n=1}^{\infty}A_n \wedge \mu(A_n)<\infty$

#### 性质

1. 若$\emptyset \in \mathcal{E}$，则$\mu(\emptyset)=0$
2. $\mu$为测度，若$\emptyset \in \mathcal{E}$，$\mu$为有限可加测度
3. 半环上的测度具有可列次可加性
4. 半环上的测度 向上(从下)连续，即$A_n \in \mathcal{E} \wedge A_n \uparrow \wedge \lim\limits_{n \to \infty} A_n \in \mathcal{E} \Longrightarrow \lim\limits_{n \to \infty} \mu(A_n) = \mu(\lim\limits_{n \to \infty} A_n)$
5. 半环上的测度 向下(从上)连续，即$A_n \in \mathcal{E} \wedge A_n \downarrow \wedge \lim\limits_{n \to \infty} A_n \in \mathcal{E} \wedge \exists n_0 \text{ s.t. } \mu(A_{n_0})<\infty \Longrightarrow \lim\limits_{n \to \infty} \mu(A_n) = \mu(\lim\limits_{n \to \infty} A_n)$
6. 设$\mu$为半环$\mathcal{E}$上的有限可加测度，则下列各条件等价
   - $\mu$为测度
   - $\mu$为具有可列次可加性
   - $A_1,A_2,\cdots \in \mathcal{E} \wedge \cup_{i=1}^{\infty}A_i \in \mathcal{E} \Longrightarrow \sum_{i=1}^{\infty}\mu(A_i) \leq \mu(\cup_{i=1}^{\infty}A_i)$
7. 设$\mathcal{E}$ 为代数，若$\mu:\mathcal{E}\to \mathbb{R}$具有非负性和有限可加性，则($\mu$在$\emptyset$处连续 $\Longrightarrow$ $\mu$为测度)

## 测度空间

### 定义

若 $(\Omega, \mathcal{F})$可测空间，$\mu$为$\mathcal{F}$上测度，则称$(\Omega, \mathcal{F}, \mu)$为**测度空间**。

若$(\Omega, \mathcal{F}, \mu)$为测度空间，且$\mu(\Omega)=1$，则称$\mu$为概率测度,称$(\Omega, \mathcal{F}, \mu)$为**概率空间**。

- 称可测拓扑空间$(X, \mathcal{B}(X), \mathcal{T})$上的测度为**Borel测度**。

### 性质

1. 设$(\Omega, \mathcal{E}, \mu)$为测度空间,$\{A_n\}_{n=1}^{\infty} \subseteq \mathcal{F}$，则
   1. $\mu\left(\underline{\lim}_{n \to \infty} A_n\right) \leq \underline{\lim}_{n \to \infty} \mu(A_n)$

## 外测度

- 称$\mu^*:\mathcal{P}(\Omega)\to \overline{\mathbb{R}}$为外测度，若$\mu^*$满足：
  - $\mu^*(\emptyset)=0$
  - 单调性：$A\subseteq B \Longrightarrow \mu^*(A)\leq \mu^*(B)$
  - 可列次可加性：$A_1,A_2,\cdots \in \mathcal{P}(\Omega) \Longrightarrow \mu^*(\bigcup_{i=1}^{\infty}A_i) \leq \sum_{i=1}^{\infty}\mu^*(A_i)$

设$\mu^*$为$\Omega$上的外测度，称$A \in \mathcal{P}(\Omega)$为$\mu^*$-可测，若
$$\forall B \in \mathcal{P}(\Omega), \mu^*(B) = \mu^*(B \cap A) + \mu^*(B \cap A^c)$$

因为外测度具有有限次可加性，所以上式等价于

$$\forall B \in \mathcal{P}(\Omega), \mu^*(B) \geq \mu^*(B \cap A) + \mu^*(B \cap A^c)$$

$\mathcal{U}_{\mu^*}$表示所有的$\mu^*$-可测集构成的集类，简称为$\mu^*$-可测集类。

### 外测度的性质

1. 非负性：$\forall A\in \mathcal{P}(\Omega), \mu^*(A)\geq 0$
2. 有限次可加性：$\forall A_1,A_2,\cdots,A_n\in \mathcal{P}(\Omega), \mu^*(\bigcup_{i=1}^{n}A_i) \leq \sum_{i=1}^{n}\mu^*(A_i)$
3. $\emptyset \in \mathcal{U}_{\mu^*}$, $\Omega \in \mathcal{U}_{\mu^*}$
4. $\mu^*(A)=0 \Longrightarrow \mathcal{P}(A) \subseteq \mathcal{U}_{\mu^*}$
5. $A \in \mathcal{U}_{\mu^*} \Longrightarrow A^c \in \mathcal{U}_{\mu^*}$
6. $\mathcal{U}_{\mu^*}$为$\Omega$上的$\sigma$-代数
7. $\mu^*$限制到$\mathcal{U}_{\mu^*}$上为测度，称为由$\mu^*$诱导的测度，记为$\mu^*|_{\mathcal{U}_{\mu^*}}$

### 由半环上的测度诱导的外测度

设$\mu$为半环$\mathcal{E}$上的测度，对于任意的$A \in \mathcal{P}(\Omega)$，定义

$$\mu^*(A) = \inf \left\{ \sum_{i\in I} \mu(A_i) \mid I  \subseteq \mathbb{N}, A_i \in \mathcal{E}, A \subseteq \bigcup_{i\in I} A_i \right\}$$

$\mu^*$有如下性质

- $\mu^*$限制到$\mathcal{E}$与$\mu$一致
- $\mu^*$为$\Omega$上的外测度, 称之为由$\mu$诱导的外测度

设$\mu^*$为半环$\mathcal{E}$上的测度诱导的外测度，则$A \in \mathcal{U}_{\mu^*}$当且仅当

$$\forall B \in \mathcal{E}, \mu^*(B) = \mu^*(B \cap A) + \mu^*(B \cap A^c)$$

## 测度扩张定理

### 定义

设$\mathcal{E}_1,\mathcal{E}_2$为$\Omega$上的集类，$\mathcal{E}_1 \subseteq \mathcal{E}_2$，$\mu_i$是$\mathcal{E}_i$上的测度或有限可加测度，若 $\forall A \in \mathcal{E}_1, \mu_1(A) = \mu_2(A)$，则称$\mu_2$是$\mu_1$的在$\mathcal{E}_2$**扩张**, $\mu_1$是$\mu_2$在$\mathcal{E}_1$的**限制**。

### 性质

1. 设$\mu$为半环$\mathcal{E}$上的测度，则$\sigma(\mathcal{E})\subseteq \mathcal{U}_{\mu^*}$
2. 设$\mathcal{E}$为$\Omega$上的$\pi$类，$\mu_1,\mu_2$是$\mathcal{E}$上的两个有限测度。若($\mu_1(A)=\mu_2(A), \forall A \in \mathcal{E} \wedge \mu_1(\Omega)=\mu_2(\Omega)$)，则$\mu_1(A)=\mu_2(A), \forall A \in \sigma(\mathcal{E})$。

3. 设$\mu$为半环$\mathcal{E}$上的测度，则
   1. $\mu$在$\sigma(\mathcal{E})$上的扩张必然存在，因为$\sigma(\mathcal{E})\subseteq \mathcal{U}_{\mu^*}$
   2. 若$\mu$还在$\mathcal{E}$上$\sigma$-有限,且$\Omega$可以表示成$\mathcal{E}$中元素的可列并，则$\mu$在$\sigma(\mathcal{E})$上的扩张唯一,且所得的测度在$\sigma(\mathcal{E})$上$\sigma$-有限

## 测度完备化

### 定义

设$(\Omega, \mathcal{F}, \mu)$为测度空间.

零测集：称$A$ 为 零测集，若$A \in \mathcal{F} \wedge \mu(A)=0$
可略集: 称$A$ 为 可略集，若 $\exists \text{零测集}B \text{ s.t. } A \subseteq B$，所有的可略集构成的集类记为$\mathcal{N}_{\mu}$

- 称$(\Omega, F, \mu)$为完备测度空间，若$\mathcal{N}_{\mu} \subseteq F$

设$(\Omega, \mathcal{F}_1, \mu_1)$和$(\Omega, \mathcal{F}_2, \mu_2)$为两个测度空间，称$(\Omega, \mathcal{F}_2, \mu_2)$是$(\Omega, \mathcal{F}_1, \mu_1)$的**完备化**，若

- (1) $(\Omega, \mathcal{F}_2, \mu_2)$ 为完备测度空间
- (2) $\mathcal{F}_1 \subseteq \mathcal{F}_2$
- (3) $\mu_2|_{\mathcal{F}_1} = \mu_1$, 即$\mu_2$是$\mu_1$的扩张

设$(\Omega, \mathcal{F}, \mu)$为测度空间
$\overline{\mathcal{F}} := \{A \cup N \mid A \in \mathcal{F}, N \in \mathcal{N}_{\mu}\},\overline{\mu}(A \cup N) := \mu(A)$
$\mathcal{F}^{\Delta}:= \{A \Delta N: A \in \mathcal{F}, N \in \mathcal{N}_{\mu}\}$, $\mu_{\Delta}(A \Delta N) := \mu(A)$
$\mathcal{F}^* := \{ A \in \Omega \mid \exists A_1,A_2 \in \mathcal{F}, s.t. A_1 \subseteq A \subseteq A_2 \wedge  \mu(A_1)=\mu(A_2) \}$, $\mu^* (A) := \mu(A_1)$
可以验证$\overline{\mu},\mu^{\Delta},\mu^*$都是良定义的。

### 性质

1. 设$\mu^*$为$\Omega$上的任一外测度，$\mathcal{U}_{\mu^*}$为$\mu^*$-可测集类，则$(\Omega, \mathcal{U}_{\mu^*}, \mu^*|_{\mathcal{U}_{\mu^*}})$为完备测度空间.

2. 以下五个命题成立
   - (1) $\overline{\mathcal{F}}$为$\sigma$-代数
   - (2) $\overline{\mathcal{F}} = \sigma(\mathcal{F}\cup \mathcal{N}_{\mu})$
   - (3) $\overline{\mu}$为$\overline{\mathcal{F}}$上的测度
   - (4) $\overline{\mu}$是完备测度
   - (5) $(\Omega, \overline{\mathcal{F}}, \overline{\mu})$为$(\Omega, \mathcal{F}, \mu)$的最小的完备化测度空间。
3. $\overline{\mathcal{F}} = \mathcal{F}^{\Delta} = \mathcal{F}^*$
4. $\overline{\mu} = \mu^{\Delta}=\mu^*$
5. $(\Omega, \mathcal{U}_{\mu^*},\mu^*)$是$(\Omega, \mathcal{F}, \mu)$的完备化.
6. 设$\Omega, \mathcal{F},\mu$为$\sigma$-有限测度空间，$\mu^*$为$\mu$诱导的外测度，$\mathcal{U}_{\mu^*}$为$\mu^*$-可测集类，则$(\forall A \in \mathcal{U}_{\mu^*},\exists B \in \mathcal{F}, \text{s.t. } A \subseteq B \wedge \mu^*(B\setminus A)=0)$
7. 设$\Omega,\mathcal{F},\mu$为$\sigma$-有限测度空间，则:
   1. $\mathcal{U}_{\mu^*}=\overline{\mathcal{F}}$
   2. $\mu^*|_{\mathcal{U}_{\mu^*}}=\overline{\mu}$

## Examples

### 计数测度

设 $\Omega$ 为任意集合。在 $(\Omega,\mathcal{P}(\Omega))$ 上定义

$$
\#(A)=
\begin{cases}
|A|, & A\text{ 为有限集},\\
+\infty, & A\text{ 为无限集},
\end{cases}
\qquad A\subseteq\Omega.
$$

称 $\#$ 为 $\Omega$ 上的**计数测度**（counting measure）。若
$\{A_n\}_{n\geqslant1}\subseteq\mathcal{P}(\Omega)$ 两两不交，则对每个
$N\geqslant1$，

$$
\#\left(\biguplus_{n=1}^N A_n\right)
=\sum_{n=1}^N\#(A_n).
$$

事实上，若其中某个 $A_n$ 无限，则等式两端均为 $+\infty$；否则这就是
有限个两两不交的有限集的基数公式。

下面验证测度公理：

1. **非负性与空集**：显然 $\#(A)\in[0,+\infty]$，且
   $\#(\emptyset)=0$。
2. **可列可加性**：记 $A=\biguplus_{n=1}^{\infty}A_n$。
   - 若某个 $A_k$ 为无限集，则 $A$ 也是无限集，等式两端均为
     $+\infty$。
   - 若每个 $A_n$ 都是有限集，则

     $$
     \#(A)
     =\lim_{N\to\infty}
       \#\left(\biguplus_{n=1}^N A_n\right)
     =\lim_{N\to\infty}\sum_{n=1}^N\#(A_n)
     =\sum_{n=1}^{\infty}\#(A_n).
     $$

     第一处等号可直接由基数验证：若 $A$ 有限，则只有有限多个
     $A_n$ 非空，有限并最终稳定；若 $A$ 无限，则有限并的基数趋于
     $+\infty$。

因此

$$
\#\left(\biguplus_{n=1}^{\infty}A_n\right)
=\sum_{n=1}^{\infty}\#(A_n),
$$

即 $\#$ 是 $(\Omega,\mathcal{P}(\Omega))$ 上的测度。它具有以下性质：

- $\#(\{\omega\})=1$，$\omega\in\Omega$；
- $\#$ 是有限测度当且仅当 $\Omega$ 有限；
- $\#$ 是 $\sigma$-有限测度当且仅当 $\Omega$ 至多可数。

  **证明** 若 $\Omega$ 至多可数，则可将它写成至多可数个单点集之并，而每个
  单点集的计数测度均为 $1$，故 $\#$ 是 $\sigma$-有限测度。

  反之，若 $\#$ 是 $\sigma$-有限测度，则存在
  $\{E_n\}_{n\geqslant1}\subseteq\mathcal{P}(\Omega)$，使得

  $$
  \Omega=\bigcup_{n=1}^{\infty}E_n,
  \qquad \#(E_n)<\infty.
  $$

  因此每个 $E_n$ 都是有限集，而有限集的可列并至多可数，所以 $\Omega$
  至多可数。$\square$

若 $\Omega$ 是非空有限集，则归一化后的计数测度

$$
P(A)=\frac{\#(A)}{\#(\Omega)}
$$

是 $\Omega$ 上的均匀概率测度。

### 集中在子集上的计数测度

设 $(\Omega,\mathcal{F})$ 为可测空间，$E\in\mathcal{F}$。对任意
$A\in\mathcal{F}$，定义

$$
\nu_E(A):=\#(A\cap E).
$$

称 $\nu_E$ 为**集中在 $E$ 上的计数测度**。它确实是测度：首先
$\nu_E(A)\geqslant0$ 且 $\nu_E(\emptyset)=0$；其次，若
$\{A_n\}_{n\geqslant1}\subseteq\mathcal{F}$ 两两不交，则
$\{A_n\cap E\}_{n\geqslant1}$ 也两两不交，所以

$$
\begin{aligned}
\nu_E\left(\biguplus_{n=1}^{\infty}A_n\right)
&=\#\left(
  \left(\biguplus_{n=1}^{\infty}A_n\right)\cap E
  \right)\\
&=\#\left(\biguplus_{n=1}^{\infty}(A_n\cap E)\right)\\
&=\sum_{n=1}^{\infty}\#(A_n\cap E)\\
&=\sum_{n=1}^{\infty}\nu_E(A_n).
\end{aligned}
$$

此外，

$$
\nu_E(\Omega\setminus E)=0,
$$

即 $\nu_E$ 的全部质量都集中在 $E$ 上。它还具有以下性质：

1. $\nu_E(\Omega)=\#(E)$，故 $\nu_E$ 是有限测度当且仅当 $E$ 是
   有限集；它是概率测度当且仅当 $E$ 是单点集。
2. 若 $\mathcal{F}$ 包含 $\Omega$ 的所有单点集，则
   $\nu_E$ 是 $\sigma$-有限测度当且仅当 $E$ 至多可数。

   事实上，若 $E=\{\omega_n:n\in I\}$ 至多可数，则

   $$
   \Omega=(\Omega\setminus E)\cup\bigcup_{n\in I}\{\omega_n\},
   $$

   且等号右侧各集合的 $\nu_E$-测度均有限。反之，若
   $\Omega=\bigcup_{n=1}^{\infty}B_n$ 且 $\nu_E(B_n)<\infty$，则
   每个 $B_n\cap E$ 都是有限集，而

   $$
   E=\bigcup_{n=1}^{\infty}(B_n\cap E)
   $$

   至多可数。

3. 若 $E=\{\omega_n:n\in I\}$ 至多可数且各点两两不同，则

   $$
   \nu_E=\sum_{n\in I}\delta_{\omega_n}.
   $$

集中计数测度可视为计数测度在 $E$ 上的限制，再将其扩充为
$\Omega$ 上、在 $\Omega\setminus E$ 处取零的测度。

### Dirac 测度

设 $(\Omega,\mathcal{F})$ 为可测空间，固定 $\omega_0\in\Omega$。定义

$$
\delta_{\omega_0}(A)
=I_A(\omega_0)
=
\begin{cases}
1, & \omega_0\in A,\\
0, & \omega_0\notin A,
\end{cases}
\qquad A\in\mathcal{F}.
$$

称 $\delta_{\omega_0}$ 为集中在 $\omega_0$ 处的 **Dirac 测度**。对于任意两两不交的
$\{A_n\}_{n\geqslant1}\subseteq\mathcal{F}$，有

$$
\omega_0\in\biguplus_{n=1}^{\infty}A_n
\quad\Longleftrightarrow\quad
\text{存在唯一的 }k\geqslant1\text{ 使 }\omega_0\in A_k.
$$

若不存在这样的 $k$，则下式两端均为 $0$；若存在，则两端均为
$1$。因此

$$
\delta_{\omega_0}\left(\biguplus_{n=1}^{\infty}A_n\right)
=\sum_{n=1}^{\infty}\delta_{\omega_0}(A_n).
$$

此外，$\delta_{\omega_0}(A)\geqslant0$、
$\delta_{\omega_0}(\emptyset)=0$，并且
$\delta_{\omega_0}(\Omega)=1$。所以 $\delta_{\omega_0}$ 不仅是测度，
还是概率测度。

Dirac 测度也可看作集中在单点集上的计数测度：

$$
\delta_{\omega_0}(A)=\#(A\cap\{\omega_0\}).
$$

更一般地，若 $\{\omega_n:n\in I\}$ 至多可数、各点两两不同，且对每个
$n\in I$ 都有 $\{\omega_n\}\in\mathcal{F}$，并且
$p_n\geqslant0$、$\sum_{n\in I}p_n=1$，则

$$
P=\sum_{n\in I}p_n\delta_{\omega_n}
$$

是离散概率测度。事实上，对任意 $A\in\mathcal{F}$，

$$
P(A)
=\sum_{n\in I}p_n\delta_{\omega_n}(A)
=\sum_{\{n\in I:\,\omega_n\in A\}}p_n.
$$

因此 $P(A)\geqslant0$、$P(\emptyset)=0$，并且

$$
P(\Omega)=\sum_{n\in I}p_n=1.
$$

再设 $\{A_k\}_{k\geqslant1}\subseteq\mathcal{F}$ 两两不交。对每个
$n\in I$，至多有一个 $A_k$ 包含 $\omega_n$，故

$$
\delta_{\omega_n}\left(\biguplus_{k=1}^{\infty}A_k\right)
=\sum_{k=1}^{\infty}\delta_{\omega_n}(A_k).
$$

由于所有项均非负，可以交换两个求和的次序，从而

$$
\begin{aligned}
P\left(\biguplus_{k=1}^{\infty}A_k\right)
&=\sum_{n\in I}p_n
  \delta_{\omega_n}\left(\biguplus_{k=1}^{\infty}A_k\right)\\
&=\sum_{n\in I}\sum_{k=1}^{\infty}
  p_n\delta_{\omega_n}(A_k)\\
&=\sum_{k=1}^{\infty}\sum_{n\in I}
  p_n\delta_{\omega_n}(A_k)\\
&=\sum_{k=1}^{\infty}P(A_k).
\end{aligned}
$$

所以 $P$ 具有可列可加性；结合 $P(\Omega)=1$，可知 $P$ 是概率测度。
最后，由各 $\omega_n$ 两两不同，

$$
P(\{\omega_n\})
=\sum_{m\in I}p_m\delta_{\omega_m}(\{\omega_n\})
=p_n.
\qquad\square
$$
