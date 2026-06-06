---
title: 与R相关的Borel集
---

## 1. Prerequisites

- [[测度论与概率论/class-of-sets]]
- [[点集拓扑/序拓扑]]

## 2. $\mathcal{B}(\mathbb{R})$的生成元

1. $\mathbb{R}$上的所有开集
2. $\mathbb{R}$上的所有闭集
3. $\mathbb{R}$上的$\{(-\infty,a]:a\in \mathbb{Q}\}$
4. $\mathbb{R}$上的$\{(-\infty,a):a\in \mathbb{Q}\}$
5. $\mathbb{R}$上的$\{(a,b]:a\lt b \wedge a,b \in \mathbb{Q}\}$
6. $\mathbb{R}$上的$\{[a,b]:a\lt b \wedge a,b \in \mathbb{Q}\}$
7. $\mathbb{R}$上的$\{[a,b):a\lt b \wedge a,b \in \mathbb{Q}\}$
8. $\mathbb{R}$上的$\{(a,b):a\lt b \wedge a,b \in \mathbb{Q}\}$

## 3. $\mathbb{R}^n$上的度量空间 与 积拓扑

$\mathbb{R}$上的绝对值可以作为度量函数，从而使得$\mathbb{R}$成为一个度量空间(拓扑空间)$(X, \tau)$,简记为$X$

$\mathbb{R}^n$上内积诱导范数，范数诱导度量，从而使得$\mathbb{R}^n$成为一个度量空间(拓扑空间)$(A, \tau_A)$,简记为$A$

$n$个$\mathbb{R}$可以制作一个积空间，从而使得$\mathbb{R}^n$成为一个拓扑空间$(B, \tau_B)$，简记为$B$

下面证明$A=B$，只需要证明$A$的基等于$B$的基。

下面把证明所有的开矩形构成的集合是$\mathbb{R}^n$的一个基。

只需要证明$\mathbb{R}^n$中的任意开集内的一点，都可以在这个开集中找到一个开矩形(易证开矩形是开集)，使得这个点在这个开矩形中。

对于$\mathbb{R}^n$中的任意开集$U$内的任意一点$x$，都可以找到一个包含$x$的开球$B(x,r) \subseteq U$, 而在这个开球内可以很容易的找到一个开矩形$R \subseteq B(x,r)$

因此，所有的开矩形构成的集合是$\mathbb{R}^n$的一个基。

又显然所有的开矩形构成的集合也是$B$的一个基。因此，$A$的基等于$B$的基。，因此$A=B$。

## 4. $\mathcal{B}(\mathbb{R}^n)$的生成元

1. $\mathbb{R}^n$中的所有开集
2. $\mathbb{R}^n$中的所有闭集
3. $\mathbb{R}^n$中的所有开矩形$\{(\mathbf{a}, \mathbf{b}): a,b  \in \mathbb{R} \wedge a_i < b_i, i=1,2,\ldots,n\}$，因为$\mathbb{R}^n$为第二可数空间。
4. $\mathbb{R}^n$中的所有有理开矩形$\{(\mathbf{a}, \mathbf{b}): \mathbf{a}, \mathbf{b} \in \mathbb{Q}^n \wedge a_i < b_i, i=1,2,\ldots,n\}$
5. $\{ (\mathbf{a}, \mathbf{b}] : \mathbf{a},\mathbf{b} \in \mathbb{Q}^n \wedge \mathbf{a} < \mathbf{b}\}$
6. $\{ [\mathbf{a}, \mathbf{b}): \mathbf{a},\mathbf{b} \in \mathbb{Q}^n \wedge \mathbf{a} < \mathbf{b}\}$
7. $\{ [\mathbf{a}, \mathbf{b}] : \mathbf{a},\mathbf{b} \in \mathbb{Q}^n \wedge \mathbf{a} < \mathbf{b}\}$
8. $\{ (-\infty, \mathbf{b}) : \mathbf{b} \in \mathbb{Q}^n\}$
9. $\{ (-\infty, \mathbf{b}] : \mathbf{b} \in \mathbb{Q}^n\}$
10. $\{ (\mathbf{a}, +\infty) : \mathbf{a} \in \mathbb{Q}^n\}$
11. $\{ [\mathbf{a}, +\infty) : \mathbf{a} \in \mathbb{Q}^n\}$

## 5. $\mathcal{B}(\overline{\mathbb{R}})$的生成元

这里$\overline{\mathbb{R}}$的拓扑是指序拓扑

1. $\overline{\mathbb{R}}$上的所有开集
2. $\overline{\mathbb{R}}$上的所有闭集
3. $\{[-\infty,a]:a \in \mathbb{Q}\}$
4. $\{[a,+\infty]:a \in \mathbb{Q}\}$
5. $\{[-\infty,a):a \in \mathbb{Q}\}$
6. $\{(a,+\infty]:a \in \mathbb{Q}\}$
7. $\{[-\infty,a):a \in \overline{\mathbb{R}}\}$
8. $\{[a,b]: a,b \in \overline{\mathbb{R}} \wedge a \lt b\}$
