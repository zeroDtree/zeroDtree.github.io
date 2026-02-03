---
title: 朴素集合论(二)
---

## 前置

- [[朴素集合论/naive-set-theory-1]]
- [[朴素集合论/初等数论]]

## 偏序

超限归纳法：$A$是良序集，$P$是$A$上的某种性质，若$\forall a \in A((\forall b < a(P(b)\text{ is True}))\rightarrow P(a)\text{ is True})$，则$P$对$A$成立

证明：$P(\min A)$空真。设$B=\{a \in A|P(a)\text{ is False}\}$，$B$非空，$B$有最小元$a$，由归纳假设可得，$P(a)$为真。与$a \in B$矛盾。

## 集合的势

- 势的比较: 若存在$A$到$B$的单射，则称$|A| \leq |B|$
- 等势: 若存在双射$f:A \to B$，则称$|A| = |B|$
- 可数集(countable set): 若$|A| = \mathbb{N}$，则称$A$是可数集
- 不可数集(uncountable set): 若$\mathbb{N} \leq |A| \wedge |A| \neq \mathbb{N}$，则称$A$是不可数集
- 至多可数集(at most countable set): 若$|A| \leq \mathbb{N}$，则称$A$是至多可数集

#### 性质

1. 若$|A| \leq |B| \wedge |B| \leq |C|$，则$|A| \leq |C|$
2. 若$|A| \leq |B| \wedge |B| \leq |A|$，则$|A| = |B|$
3. 至多可数个至多可数集的并仍是至多可数集
