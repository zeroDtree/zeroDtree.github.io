---
title: 拓展实数域上的点集收敛
---

## 前置

- [[数学分析/real-number]]

#### 定义

$\overline{\mathbb{R}}=\mathbb{R} \cup \{-\infty, +\infty\}$

$\mathbb{Z}_{\geq m} = \{n \in \mathbb{Z} \mid n \geq m\}$

以下若没有额外说明，则默认$a_n \in \overline{\mathbb{R}}$

**序列(数列)**：称$(a_n)_{n\geq m}$为数列，其中$a_n$为数列的项，$m\in \mathbb{Z}$

**收敛**：称数列$a_n$收敛于$L \in \overline{\mathbb{R}}$,简记为$a_n \to L$,若$a_n$满足以下两个条件

- 对于任意$l < L$, 存在$N \in \mathbb{Z}_{\geq m}$使得对于任意$n \geq N$, $a_n > l$
- 对于任意$u > L$, 存在$N \in \mathbb{Z}_{\geq m}$使得对于任意$n \geq N$, $a_n < u$

**极限**：称$L$为数列$a_n$的极限，若$a_n$收敛于$L$,记作$lim_{n \to \infty} a_n = L$

**极限点**：称$L \in \overline{\mathbb{R}}$是数列$a_n$的极限点，若$a_n$满足以下两个条件

- 对于任意$l < L$, 存在$N \in \mathbb{Z}_{\geq m}$使得对于任意$n \geq N$, $a_n > l$
- 对于任意$u > L$, 存在$N \in \mathbb{Z}_{\geq m}$使得对于任意$n \geq N$, $a_n < u$

**上极限**：$L^+= \mathop{lim sup}\limits_{n \to \infty} a_n = inf_{n\geq m} sup_{k\geq n} a_k$

**下极限**：$L^-= \mathop{lim inf}\limits_{n \to \infty} a_n = sup_{n\geq m} \mathop{inf}\limits_{k\geq n} a_k$

**柯西列**：称数列$a_n$为柯西列，若对于任意$\epsilon > 0$, 存在$N \in \mathbb{Z}_{\geq m}$使得对于任意$n,m \geq N$, $|a_n - a_m| < \epsilon$

#### 性质

- 收敛数列的极限唯一
- 若$(a_n)_{n \geq m}$收敛于$x$,则对于任意$k \in \mathbb{Z}_{\geq m}$,$(a_n)_{n \geq k}$也收敛于$x$
- 若$a_n,b_n$分别收敛于$x,y$,$a_n \geq b_n$,则$x \geq y$
- 若$a_n,b_n$分别收敛于$x,y$,且$x,y \in \mathbb{R}$,则
  - $a_n + b_n$收敛于$x+y$
  - $a_n b_n$收敛于$xy$
  - 若$y \neq 0 \wedge b_n \neq 0$,则$\frac{1}{b_n}$收敛于$\frac{1}{y}$
  - 若$y \neq 0 \wedge b_n \neq 0$,则$\frac{a_n}{b_n}$收敛于$\frac{x}{y}$
- $lim_{n \to \infty} max(a_n,b_n) = max(lim_{n \to \infty} a_n, lim_{n \to \infty} b_n)$
- $lim_{n \to \infty} min(a_n,b_n) = min(lim_{n \to \infty} a_n, lim_{n \to \infty} b_n)$
- 若$y<sup(a_n)$,则存在$n \in \mathbb{Z}_{\geq m}$，使得$y<a_n$
- 单调数列必有极限，其极限为其上确界
- 收敛数列只有一个极限点，即这个数列的极限
- 若$L+<x$,则存在$N \in \mathbb{Z}_{\geq m}$，使得对于任意$n \geq N$,都有$a_n<x$
- 若$L^->x$,则存在$N \in \mathbb{Z}_{\geq m}$，使得对于任意$n \geq N$,都有$a_n>x$
- 若$y<L^+$,则存在$n \in \mathbb{Z}_{\geq m}$，使得$y<a_n$
- 若$y>L^-$,则存在$n \in \mathbb{Z}_{\geq m}$，使得$a_n<y$
- $inf(a_n) \leq L^- \leq L^+ \leq sup(a_n)$
- $L^+$和$L^-$是数列的极限点
- if c is a limit point of a sequence, then $L^- \leq c \leq L^+$
- $L^+=L^-=c \Longleftrightarrow lim_{n \to \infty} a_n = c$
- $a_n \leq b_n \Longrightarrow sup(a_n) \leq sup(b_n) \wedge inf(a_n) \leq inf(b_n) \wedge limsup(a_n) \leq limsup(b_n) \wedge liminf(a_n) \leq liminf(b_n)$
- 若$a_n \leq b_n \leq c_n$,且$a_n,c_n$收敛于$x$,则$b_n$收敛于$x$
- 若$x \in \mathbb{R}$，则$a_n$收敛于$x \Longleftrightarrow \forall \epsilon > 0, \exists N \in \mathbb{Z}_{\geq m}, \forall n \geq N, |a_n - x| < \epsilon$
- $a_n \to 0$ $\Longleftrightarrow$ $|a_n| \to 0$
- 实数域的完备性：若$a_n \in \mathbb{R}$, 则$a_n$是 cauchy 列 $\Longleftrightarrow$ $a_n$收敛于$\mathbb{R}$中的某个数
