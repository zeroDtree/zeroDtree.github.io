---
title: 乘积度量空间与积拓扑
---

## Prerequisites

- [[点集拓扑/度量空间]]

## 乘积度量空间

$\{(X_i,d_i): i=1,2,\cdots,n\}$ 为n个度量空间，$X = \prod_{i=1}^{n} X_i$，$d_i$ 为 $X_i$ 上的度量，则 $X$ 上的乘积度量定义为

$$
d(\mathbf{x},\mathbf{y}) = \sqrt{\sum_{i=1}^{n} d_i(x_i,y_i)^2}
$$

$(X,d)$ 称为 $X_i$ 的乘积度量空间

## 积拓扑

设 $\{(X_i,\tau_i): i=1,2,\cdots,n\}$ 为n个拓扑空间，则 $X$ 上的积拓扑定义为

$$
\tau = \{\prod_{i=1}^{n} U_i: U_i \subseteq X_i \text{ 是 } X_i \text{ 上的开集}\}
$$

$(X,\tau)$ 称为 $X_i$ 的积拓扑空间

若 $\mathcal{B}_i$ 为 $X_i$ 上的基，则 $X = \prod_{i=1}^{n} X_i$ 的积拓扑的基为

$$
\mathcal{B} = \{\prod_{i=1}^{n} B_i: B_i \subseteq \mathcal{B}_i\}
$$

## 乘积度量空间与积拓扑的等价性

证明积拓扑的基为乘积度量空间的基

度量空间的积拓扑的基为$\mathcal{B} = \{\prod_{i=1}^{n} B(x_i,r_i) : x_i \in X_i, r_i > 0\}$

乘积度量空间的基为$\mathcal{A} = \{B(\mathbf{x},r): \mathbf{x} \in X, r > 0\}$

> 证明积拓扑的基为乘积度量空间中的开集

任取$\mathcal{B}$ 中元素$U= \prod_{i=1}^{n} B(x_i,r_i)$，任取$\mathbf{y}= (y_1,y_2,\cdots,y_n) \in U$，则

$r_i - d(x_i,y_i) =: a_i \in (0, r_i)$

$a = min(a_1,a_2,\cdots,a_n)$

$\forall \mathbf{z} \in B(\mathbf{y},a)$

$d(x_i,z_i) \leq d(x_i,y_i) + d(y_i,z_i) \lt d(x_i,y_i) + a = r_i$

所以$\mathbf{z} \in \prod_{i=1}^{n} B(x_i,r_i) = U$，即$B(\mathbf{y},a) \subseteq U$

因此$\mathcal{B}$中的元素是乘积度量空间中的开集

> 证明积拓扑的基为乘积度量空间的基

只需要证明 $\mathcal{A}$ 中的任一元素能被 $\mathcal{B}$ 中的某些元素完美覆盖

任取$\mathcal{A}$ 中元素$V= B(\mathbf{x},r)$，任取$\mathbf{y}= (y_1,y_2,\cdots,y_n) \in V$

$b = r - d(\mathbf{x},\mathbf{y})$

$\forall \mathbf{z} \in B(\mathbf{y},b)$

$d(\mathbf{x},\mathbf{z}) \leq d(\mathbf{x},\mathbf{y}) + d(\mathbf{y},\mathbf{z}) \lt d(\mathbf{x},\mathbf{y}) + b = r$

$B(\mathbf{y},b) \subseteq V$

$c = \frac{b}{\sqrt{n}}$

$\forall \mathbf{p} \in \prod_{i=1}^{n} B(y_i,c)$

$d(\mathbf{y},\mathbf{p}) = \sqrt{\sum_{i=1}^{n} d(y_i,p_i)^2} \lt \sqrt{\sum_{i=1}^{n} c^2} = b$

因此$\prod_{i=1}^{n} B(y_i,c) \subseteq B(\mathbf{y},b) \subseteq V$

所以$\mathcal{A}$ 中的任一元素能被 $\mathcal{B}$ 中的某些元素完美覆盖

度量空间的积拓扑与乘积度量空间有一个共同的拓扑基，因此度量空间的积拓扑与乘积度量空间是相等的。
