---
title: Zorn's Lemma (佐恩引理)
---

## 前置

- [[朴素集合论/naive-set-theory-1]]

## 定义

- **链(chain)**: 称$A\subseteq P$为链，若将偏序集$P$上的偏序关系限制到$A$上为全序关系。
- **真上界(proper upper bound)**: 称$b \in P$为$A\subseteq P$的真上界，若 $b$为$A$的上界，且$b \notin A$。
- $\forall A \subseteq P, \forall x \in A, A_x:=\{y < x \mid y \in A\}$, 即$A_x$为$A$中所有小于$x$的元素组成的集合。称$A_x$为$A$在$x$处的**切片**.

## 佐恩引理

设$P$为一个偏序集，($P$的任链都有上界 $\implies$ $P$有极大元。)

### 证明

若$P$为空集，则$P$的子集只有$\emptyset$，因此只有空链。因为$P$为空，空链不存在上界。因此佐恩引理为空真。

若$P$为非空集，则$P$的所有链组成的集合$\mathcal{C}$非空，因为任取一个元素$a \in P$, 知$\{a\}$为链。

假设$P$没有极大元，则$P$中的链都存在真上界。首先根据条件，$\forall C \in \mathcal{C}$都存在上界$u_C$, 又因为假设$P$没有极大元，即存在$a_C \in P$, 使得$a_C > u_C$。$a_C$即为$C$的一个真上界。

因此可以定义一个映射$u: \mathcal{C} \to P$，$u(C) = a_C$。即$u$将每个链映射到它的一个真上界。

称链$C$为好链(u-好链，u-good chain, u-gc, u-g.c.)，若$C$满足以下两个条件：

- $C$为良序集
- $\forall x \in C, x = u(C_x)$

注意到：空集是好链。$\{u(\emptyset)\}$是好链。

**命题**：任意两个好链$C, C'$, $(C\not=C' \implies C_x = C' \vee C = C'_x)$

假设$C \not= C'$。那么不妨设$C \not\subseteq C'$，即$C \setminus C' \not= \emptyset$。

知$C \setminus C'$为良序集合，设其最小元为$x_1$

知$C_{x_1} \subseteq C'$。假设$C_{x_1} \subsetneq C'$, 否则命题自然成立。

$C' \setminus C_{x_1} \not= \emptyset$, 且$C' \setminus C_{x_1}$为良序集合，设其最小元为$x_2$。

知$C'_{x_2} \subseteq C_{x_1}$，

只能有$C'_{x_2} \subsetneq C_{x_1}$, 否则$x_2=u(C'_{x_2})=u(C_{x_1})=x_1 \notin C'$, 与$x_2 \in C' \setminus C_{x_1}$矛盾。

设良序集$C_{x_1} \setminus C'_{x_2}$的最小元为$x_3$

知$C_{x_3} \subseteq C'_{x_2}$

整理一下，现在有

$$
\begin{align*}
C_{x_3} \subseteq C'_{x_2} \subseteq C_{x_1} &\subseteq C \\
& \subseteq C'
\end{align*}
$$

$$
\begin{align*}
&x_3 \in C_{x_1}, x_2 \in C', x_1 \in C \\
&x_3 \notin C'_{x_2}, x_2 \notin C_{x_1}, x_1 \notin C'
\end{align*}
$$

知$x_3 < x_1$

任取$x \in C'_{x_2}$，知$x < x_2$.

$x,x_3$都属于$C'$, 因此，要么$x < x_3$ 要么 $x \geq x_3$， 而后者意味着$x_3 \leq x < x_2$,从而$x_3 \in C'_{x_2}$, 与$x_3 \notin C'_{x_2}$矛盾。

$x,x_3$都属于$C$，因此$x \in C_{x_3}$, 所以$C'_{x_2} \subseteq C_{x_3}$。

因此$C_{x_3} = C'_{x_2}$.

因此$x_3 = u(C_{x_3}) = u(C'_{x_2}) = x_2 \notin C_{x_1}$, 与$x_3 \in C_{x_1}$矛盾。

因此命题得证。

**现在接着证明佐恩引理。**

设所有好链组成的集合族为$\mathcal{G}$

知$G:=\bigcup \mathcal{G}$为良序集

知$\forall x \in G, u(G_x)=x$

因此$G$为好链。

知$G':=G \cup \{u(G)\}$为好链。因此$G' \in \mathcal{G}$, $G'\subseteq G$，与$G \subsetneq G'$矛盾。

因此佐恩引理得证。
