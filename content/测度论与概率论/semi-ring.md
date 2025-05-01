---
title: semi-ring (in measure theory)
---

称集类$\mathcal{E}$为半环，若

- $\emptyset \in \mathcal{E}$
- 若$A,B \in \mathcal{E}$，则$A \cap B \in \mathcal{E}$
- 若$A,B \in \mathcal{E}$，则$A \setminus B = \bigcup_{i=1}^n C_i$，其中$C_i \in \mathcal{E}$

#### 有限个半环的笛卡尔积(Cartesian product, or direct product)是半环

$\mathcal{E}_i$为$\Omega_i$上的半环，则$\mathcal{S} = \mathcal{E}_1 \times \mathcal{E}_2 \times \cdots \times \mathcal{E}_n$为半环.

证明：

$$
\begin{aligned}
\mathcal{S} = \left\{ \prod_{i=1}^n A_i \mid A_i \in \mathcal{E}_i \right\}
\end{aligned}
$$

(1) $\emptyset \in \mathcal{S}$
显然
(2) 若$A,B \in \mathcal{S}$，则$A \cap B \in \mathcal{S}$

$A = \prod_{i=1}^n A_i$
$B = \prod_{i=1}^n B_i$

$A \cap B = \prod_{i=1}^n A_i \cap B_i \in \mathcal{S}$

(3) $A,B\in \mathcal{S}$,则$A \setminus B = \bigcup_{i=1}^n C_i$，其中$C_i \in \mathcal{S}$

$A = \prod_{i=1}^n A_i$
$B = \prod_{i=1}^n B_i$
设$A_i\setminus B_i = \biguplus_{j=1}^{m_i} D_{ij}$

$$
\begin{aligned}
A \setminus B &= A \cap B^c \\
&= \prod_{i=1}^n A_i \cap \left( \prod_{i=1}^n B_i \right)^c \\
&= \prod_{i=1}^n A_i \cap \bigcup_{j=1}^{n} \left( \prod_{i < j} \Omega_i \times B_j^c \times \prod_{i > j} \Omega_i \right) \\
&= \bigcup_{j=1}^{n} \left( \prod_{i < j} A_i \times (A_j \setminus B_j) \times \prod_{i > j} A_i \right)\\
&= \bigcup_{j=1}^{n} \left( \prod_{i < j} (A_i \cap B_i) \times (A_j \setminus B_j) \times \prod_{i > j} A_i \right)\\
& = \bigcup_{j=1}^{n} \left( \prod_{i < j} (A_i \cap B_i) \times (\biguplus_{k=1}^{m_j} D_{jk}) \times \prod_{i > j} A_i \right)\\
&= \bigcup_{j=1}^{n} \biguplus_{k=1}^{m_j} \left( \prod_{i < j} (A_i \cap B_i) \times (D_{jk}) \times \prod_{i > j} A_i \right)\\
& = \biguplus_{j=1}^{n} \biguplus_{k=1}^{m_j} \left( \prod_{i < j} (A_i \cap B_i) \times (D_{jk}) \times \prod_{i > j} A_i \right)\\
\end{aligned}
$$

#### 半环实例

$\mathcal{E} = \{[a, b) \mid a, b \in \mathbb{R}\}$ 是半环

证明：

(1) $\emptyset \in \mathcal{E}$

$\emptyset = [a, a) \in \mathcal{E}$

(2) 若$A,B \in \mathcal{E}$，则$A \cap B \in \mathcal{E}$

$A = [a, b)$
$B = [c, d)$

$A \cap B = [a, b) \cap [c, d) = [\max(a, c), \min(b, d))$

(3) $A,B\in \mathcal{E}$,则$A \setminus B = \bigcup_{i=1}^n C_i$，其中$C_i \in \mathcal{E}$

$A = [a, b)$
$B = [c, d)$

$B^c = (-\infty, c) \cup [d, \infty)$

$$
\begin{aligned}
A \setminus B &= A \cap B^c \\
&= [a, b) \cap \left( (-\infty, c) \cup [d, \infty) \right) \\
& = [a, \min(b,c)) \cup [\max(a,d), b)
\end{aligned}
$$

所以$\{[a, b) \mid a, b \in \mathbb{R}\}$ 是半环
