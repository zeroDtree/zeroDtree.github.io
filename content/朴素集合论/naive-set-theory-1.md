---
title: 朴素集合论(一)
---

## 集合的定义

- 集合(set): a collection of objects. 不规定object是什么，默认之后使用到的东西都可以被看作object

- 元素(element): 一个集合中的一个object被称作这个集合的元素,

- 属于(belong to): 若obejct $a$ 是集合 $A$ 的元素，则记作 $a \in A$，否则记作 $a \notin A$

- 空集(empty set): 一个集合中没有元素，则称这个集合为空集，记作 $\emptyset$ (承认空集的存在性)

- 集合的包含(contain): 若集合 $A$ 的元素都是集合 $B$ 的元素，则称 $A$ 是 $B$ 的子集，记作 $A \subseteq B$。

- 集合的相等(equal): 若$A \subseteq B$且$B \subseteq A$，则称$A$和$B$相等，记作$A = B$。

- 真子集(proper subset): 若$A \subseteq B$且$A \neq B$，则称$A$是$B$的真子集，记作$A \subsetneq B$。

## 集合上的运算

默认下面这些运算的结果都是存在的

- 性质P：$B=\{x \in A \mid P(x) \text{ is true}\}$
- 交集(intersection): $A \cap B = \{ x \mid x \in A \wedge x \in B \}$
- 并集(union): $A \cup B = \{ x \mid x \in A \text{ or } x \in B \}$
- 差集(difference): $A - B = \{ x \mid x \in A \wedge x \notin B \}$，也记作$A \setminus B$
- 任意并(union of arbitrary set): $A = \bigcup_{i \in I} A_i = \{ x \mid \exists i \in I, x \in A_i \}$
- 任意交(intersection of arbitrary set): $A = \bigcap_{i \in I} A_i = \{ x \mid \forall i \in I, x \in A_i \}$
- 幂集(power set): $P(A) = \{ x \mid x \subseteq A \}$
- 有序对(ordered pair): $(a, b)=(c,d) \iff a=c \wedge b=d$
- 笛卡尔积(cartesian product): $A \times B = \{ (a, b) \mid a \in A \wedge b \in B \}$
- 对称差(symmetric difference): $A \oplus B = (A - B) \cup (B - A)$

#### 性质

1. 交的交换律：$A \cap B = B \cap A$
2. 交的结合律：$A \cap (B \cap C) = (A \cap B) \cap C$
3. 交的单位元(全集)：$A \cap U = A$，$U$为全集
4. 并的交换律：$A \cup B = B \cup A$
5. 并的结合律：$A \cup (B \cup C) = (A \cup B) \cup C$
6. 并的单位元(空集)：$A \cup \emptyset = A$
7. 并对交的分配律：$A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$
8. 交对并的分配律：$A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$
9. 并对任意交的分配律：$A \cup (\bigcap_{i \in I} A_i) = \bigcap_{i \in I} (A \cup A_i)$
10. 交对任意并的分配律：$A \cap (\bigcup_{i \in I} A_i) = \bigcup_{i \in I} (A \cap A_i)$
11. 任意并交任意并：$(\bigcup_{i \in I} A_i) \cap (\bigcup_{j \in J} B_j) = \bigcup_{i \in I, j \in J} (A_i \cap B_j)$
12. 任意交并任意交：$(\bigcap_{i \in I} A_i) \cup (\bigcap_{j \in J} B_j) = \bigcap_{i \in I, j \in J} (A_i \cup B_j)$
13. 德摩根律(对任意交)：$A-\bigcap_{i \in I} A_i = \bigcup_{i \in I} (A - A_i)$
14. 德摩根律(对任意并)：$A-\bigcup_{i \in I} A_i = \bigcap_{i \in I} (A - A_i)$

## 关系

- 关系(relation): 若$R\subseteq A\times B$，则称$R$为从$A$到$B$的关系,若$A=B$，则称$R$为$A$上的关系
- 自反性(reflexive): 若$R$是$A$上的关系，且$\forall a \in A, (a, a) \in R$，则称$R$是自反的
- 对称性(symmetric): 若$R$是$A$上的关系，且$\forall a, b \in A, (a, b) \in R \implies (b, a) \in R$，则称$R$是对称的
- 传递性(transitive): 若$R$是$A$上的关系，且$\forall a, b, c \in A, (a, b) \in R \wedge (b, c) \in R \implies (a, c) \in R$，则称$R$是传递的
- 等价关系(equivalence relation): 若$R$是$A$上的关系，且$R$是自反的、对称的、传递的，则称$R$是等价关系
- 偏序关系(partial order relation): 若$R$是$A$上的关系，且$R$是反自反的、反对称的、传递的，则称$R$是偏序关系
- 全序关系(total order relation): 若$R$是$A$上的偏序关系，且$\forall a, b \in A, a \neq b \implies (a, b) \in R \vee (b, a) \in R$，则称$R$是全序关系
- 映射(mapping or function): 若$f\subseteq A\times B \wedge \forall a \in A, \exists ! b \in B, (a, b) \in f$，($\exists !$表示存在且唯一),则称$f$是$A$到$B$的映射
- 单射(injection): 若$f$是$A$到$B$的映射，且$(\forall a, b \in A, f(a)=f(b) \implies a=b)$，则称$f$是单射，记作$f: A \hookrightarrow B$
- 满射(surjection): 若$f$是$A$到$B$的映射，且$(\forall b \in B, \exists a \in A, f(a)=b)$，则称$f$是满射，记作$f: A \twoheadrightarrow B$
- 双射(bijection): 若$f$是$A$到$B$的映射，且$f$是单射和满射，则称$f$是双射，记作$f: A \leftrightarrow B$
- 逆映射(inverse mapping): 若$f$是$A$到$B$的双射，若$B=\{(b,a) \mid (a,b) \in f\}$为$B$到$A$的映射，则称$f$可逆，称$B$为$f$的逆映射，记作$f^{-1}$
- 映射的像(image): 若$f$是$A$到$B$的映射，$A_1$是$A$的子集，则称$f[A_1] = \{ b \in B \mid \exists a \in A_1, f(a)=b \}$为$A_1$在$f$下的像
- 逆像(inverse image): 若$f$是$A$到$B$的映射，$B_1$是$B$的子集，则称$f^{-1}[B_1] = \{ a \in A \mid \exists b \in B_1, f(a)=b \}$为$B_1$在$f$下的逆像
- 划分(partition): 若$\forall A,B \in \mathcal{A}, (A \neq B \implies A \cap B = \emptyset) \wedge \bigcup_{A \in \mathcal{A}} A = U$，则称$\mathcal{A}$是$U$的划分
- 等价类(equivalence class): 若$R$是$A$上的等价关系，$a \in A$，则称$a$在$R$下的等价类为$[a] = \{ b \in A \mid (a, b) \in R \}$
- 映射复合(mapping composition): 若$f:A \to B$，$g:B \to C$，则称$g \circ f=\{\langle a, c \rangle \mid \exists b \in B, \langle a, b \rangle \in f \wedge \langle b, c \rangle \in g \}$为$f$和$g$的复合
- 多重集(multiset): 称$f:A \to \mathbb{N^+}$为多重集，若$f(a)$表示$a$在多重集中的出现次数
- 最大元：若$(A, \leq)$是全序集，$a \in A$，若$\forall b \in A, b \leq a$，则称$a$为$A$的最大元
- 极大元：若$(A,\leq)$为偏序集，$a \in A$, 若((若$a$和$b$是可比较的) $\implies b \leq a$)
- 良序集：称$A$为良序集，若$A$是全序集，且$A$的每个非空子集都有最小元

#### 性质

1. 集合$A$上的等价关系$R$所确定的所有等价类的集合$A/R = \{ [a] \mid a \in A \}$ 是$A$的划分
2. 集合$A$上的划分$\mathcal{A}$可以确定一个等价关系$R = \{ (a, b) \mid \exists A \in \mathcal{A}, a, b \in A \}$
3. $f^{-1}[\bigcap_{i \in I} A_i] = \bigcap_{i \in I} f^{-1}[A_i]$
4. $f^{-1}[\bigcup_{i \in I} A_i] = \bigcup_{i \in I} f^{-1}[A_i]$
5. $f^{-1}[A-B] = f^{-1}[A] - f^{-1}[B]$
6. $f[\bigcap_{i \in I} A_i] \subseteq \bigcap_{i \in I} f[A_i]$，若$f$是单射则$f[\bigcap_{i \in I} A_i] = \bigcap_{i \in I} f[A_i]$
7. $f[\bigcup_{i \in I} A_i] = \bigcup_{i \in I} f[A_i]$
8. $f^{-1}[f[A]] \supseteq A$,若$f$是单射，则$f^{-1}[f[A]] = A$
9. $f[f^{-1}[A]] \subseteq A$,若$f$是满射，则$f[f^{-1}[A]] = A$
10. 若$f:A \to B$可逆等价于$f^{-1}$为单射和满射
11. 若$f:A \to B$是单射，则$f|_A:A \to f[A]$是双射
12. 复合映射有结合律：$(f \circ g) \circ h = f \circ (g \circ h)$
13. 单射复合单射是单射
14. 满射复合满射是满射
15. 双射复合双射是双射
16. 若$f_i:A_i \to B_i$是双射,且$\forall i,A_i \cap A_j = \emptyset$，则$f=\bigcup_{i \in I} f_i: \bigcup_{i \in I} A_i \to \bigcup_{i \in I} B_i$是双射
17. 若$f:A \to B$是双射，则$f[A] = B \wedge f^{-1}[B] = A$
18. 若$f:A\to B$可逆，则$f^{-1} \circ f = id_A = \{(a,a)|a \in A\} \wedge f \circ f^{-1} = id_B = \{(b,b)|b \in B\}$
