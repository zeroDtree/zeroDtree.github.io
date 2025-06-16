---
title: 非负级数
---

## 前置

- [[数学分析/converge]]

## 约定

- $\mathbb{R}^+ = \{x \in \mathbb{R} \mid x \gt 0\}$
- $\mathbb{R}^* = \{x \in \mathbb{R} \mid x \geq 0\}$
- $\overline{\mathbb{R}}^+ = \mathbb{R}^+ \cup \{+\infty\}$
- $\overline{\mathbb{R}}^* = \mathbb{R}^* \cup \{+\infty\}$
- $\overline{\mathbb{R}}=\mathbb{R} \cup \{-\infty, +\infty\}$

## 有限级数(有限求和)

$a_i \in \mathbb{R}$

$n<m \Longrightarrow\sum_{i=m}^n {a_i} = 0$

$\sum_{i=m}^m {a_i}=a_m$

$\sum_{i=m}^{n+1} {a_i}=\sum_{i=m}^n {a_i}+a_{n+1}$

有数学归纳法可得，对于每一个$n \in \mathbb{Z}_{\geq m}$，$\sum_{i=m}^n {a_i}$ 被唯一定义。

**有限集上求和**: $X$ 是有限集，$f: X \to \mathbb{R}$ 是函数，$g:\{i\in \mathbb{Z}|1\lt i \lt n\} \to X$ 是双射, $f$ 在 $X$ 上的求和$\sum_{x \in X} f(x)=\sum_{i=1}^n f(g(i))$

通过数学归纳法可证明：(Finite summations are well-defined) Let $X$ be a finite set with $n$ elements (where $n \in \mathbb{N}$), let $f : X \to \mathbb{R}$ be a function, and let $g : \{i \in \mathbb{N} : 1 \leq i \leq n\} \to X$ and $h : \{i \in \mathbb{N} : 1 \leq i \leq n\} \to X$ be bijections. Then we have $\sum_{i=1}^n f(g(i)) = \sum_{i=1}^n f(h(i))$

因此，有限集上求和是良定义的。

#### 性质

1. $\sum_{i=m}^n {a_i} + \sum_{i=n+1}^{p} {a_i} = \sum_{i=m}^{p} {a_i}$ for $m \leq n < p$
2. $\sum_{i=m}^{n} a_i = \sum_{j=m+k}^{n+k} a_{j-k}$
3. $\sum_{i=m}^{n} a_i + b_i = \sum_{i=m}^{n} a_i + \sum_{i=m}^{n} b_i$
4. $\sum_{i=m}^{n} ca_i = c \sum_{i=m}^{n} a_i$
5. $|\sum_{i=m}^{n} a_i| \leq \sum_{i=m}^{n} |a_i|$
6. $a_i \leq b_i  \Longrightarrow \sum_{i=m}^{n} a_i \leq \sum_{i=m}^{n} b_i$

## 正项(非负)无穷级数

规定(对于正项级数求和只需要定义下面这些运算就可以了)：

- $x \in \mathbb{R}, y = +\infty, x+y = y+x = +\infty$
- $x = +\infty, y = \infty, x+y = y+x = +\infty$
- $x \in \mathbb{R} \wedge x \gt 0, y = \infty, xy = yx = \infty$
- $x = \infty, y = \infty, xy = yx = \infty$
- $x =0， y = \infty, xy = yx = 0$

若没有额外说明，则以下默认$a_i,b_i \in \overline{\mathbb{R}}^*$

$\sum_{i=m}^{m} {a_i} = a_m$

$\sum_{i=m}^{n+1} {a_i} = \sum_{i=m}^n {a_i} + a_{n+1}$

$\sum_{i=m}^{n} {a_i} < \sum_{i=m}^{n+1} {a_i}$, 所以数列$(\sum_{i=m}^{n} {a_i})_{n \geq m}$ 是单调递增的,因此极限存在。

$\sum_{i=m}^{\infty} {a_i} = \lim_{n \to \infty} \sum_{i=m}^{n} {a_i}$

有穷(有限)正项级数$S = \sum_{i=m}^{n} {a_i}$ 可看作无穷正项级数的一种特例，即令数列$a_n$ 在$i \geq n$时恒为 0。

可数集上求和：$X$ 是可数集，$f:X \to \overline{\mathbb{R}}^*$ 是函数，$g:\mathbb{Z}_{\geq m} \to X$ 是双射, $f$ 在 $X$ 上的求和$\sum_{x \in X} f(x)=\sum_{i=m}^{\infty} f(g(i))$, 有正项级数的性质可得，以上定义的可数集上求和是良定义的。

#### 性质

1. $\forall a,b,c,d \in \overline{\mathbb{R}}^*, a\leq b \wedge c\leq d \Longrightarrow a+c\leq b+d$
2. (Zero test) Let $n=m$ an be a convergent(收敛到$\mathbb{R}$中的某个数) series of real numbers. Then we must have $\lim_{n \to \infty} a_n = 0$.
3. 若存在$n_0 \in \mathbb{Z}_{\geq m}$使得$a_{n_0}=+\infty$,则$\sum_{i=m}^{\infty} a_i = +\infty$,特别地,若$n_0<n$, 则$\sum_{i=m}^{n}=+\infty$
4. 若$a_n \to L,c \in \overline{\mathbb{R}}^*$,则$ca_n \to cL$
5. $\sum_{i=m}^{\infty} ca_i = c \sum_{i=m}^{\infty} a_i$
6. $\forall a_i \leq b_i \Longrightarrow \sum_{i=m}^{n} a_i \leq \sum_{i=m}^{n} b_i$
7. $\forall a_i \leq b_i \Longrightarrow \sum_{i=m}^{\infty} a_i \leq \sum_{i=m}^{\infty} b_i$
8. $\sum_{i=m}^{\infty} a_i + \sum_{i=m}^{\infty} b_i = \sum_{i=m}^{\infty} (a_i + b_i)$
9. $\forall k \in \mathbb{N},\sum_{i=m}^{\infty} a_i = \sum_{i=m}^{m+k-1} a_i + \sum_{i=m+k}^{\infty} a_i$
10. $\sum_{i=m}^{\infty} = \sum_{i=m+k}^{\infty} a_{i-k}$
11. 若$f:\mathbb{Z}_{\geq m} \to \mathbb{Z}_{\geq m}$为双射，则$\sum_{i=m}^{\infty} a_i = \sum_{i=m}^{\infty} a_{f(i)}$
12. $\lim\limits_{n_2 \to \infty} \sum_{i=m_1}^{n} \sum_{j=m_2}^{n_2} f(i,j) = \sum_{i=m_1}^{n} \lim\limits_{n_2 \to \infty} \sum_{j=m_2}^{n_2} f(i,j)$
13. 正项级数的 Fubini 定理：$\sum_{i=m_1}^{\infty} \sum_{j=m_2}^{\infty} f(i,j) = \sum_{j=m_2}^{\infty} \sum_{i=m_1}^{\infty} f(i,j)=\sum_{(i,j) \in \mathbb{Z}_{\geq m_1} \times \mathbb{Z}_{\geq m_2}} f(i,j)=\sum_{(j,i) \in \mathbb{Z}_{\geq m_2} \times \mathbb{Z}_{\geq m_1}} f(j,i)$
