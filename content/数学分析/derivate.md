---
title: derivative
tags:
  - 数学分析
---

## 1. Prerequisites

- [[数学分析/无穷小]]

## 2. Definitions

- Real vector space: $<\mathbb{R}, \mathbb{R}^n>$
- Multivariate real-valued function $f: \mathbb{R}^n \rightarrow \mathbb{R}$
- Multivariate real vector-valued function $f: \mathbb{R}^n \rightarrow \mathbb{R}^m$
- **Differentiability at a point** Let $X$ be a subset of $\mathbb{R}^n$, and let $x_0 \in X$ be an element of $X$ which is also a limit point of $X$. Let $f: X \rightarrow \mathbb{R}^m$ be a function. Let $L$ be a linear transformation from $\mathbb{R}^n$ to $\mathbb{R}^m$. We say that $f$ is **differentiable at** $x_0$ on $X$ with **derivative** $L$ and write $f'(x_0) := L$ if
  $$
  \lim_{x \to x_0, x \in X \setminus \{x_0\}} \frac{d(f(x), f(x_0) + L(x - x_0))}{d(x, x_0)} = 0
  $$
  > Equivalently, in the little-o of [[数学分析/无穷小]],
  >
  > $$
  > d\big(f(x), f(x_0) + L(x - x_0)\big) = o\big(d(x, x_0)\big) \quad (x \to x_0,\ x \in X \setminus \{x_0\}),
  > $$
  >
  > that is,
  >
  > $$
  > \forall \varepsilon > 0,\ \exists \delta > 0,\ \text{s.t.}\ \forall x \in X,\ 0 < d(x, x_0) < \delta \implies d\big(f(x), f(x_0) + L(x - x_0)\big) \le \varepsilon\, d(x, x_0).
  > $$
  **Uniqueness of derivatives** Let $E$ be a subset of $\mathbb{R}^n$, $f: E \rightarrow \mathbb{R}^m$ be a function, $x_0 \in E$ be an interior point of $E$, and let $L_1: \mathbb{R}^n \rightarrow \mathbb{R}^m$ and $L_2: \mathbb{R}^n \rightarrow \mathbb{R}^m$ be linear transformations. Suppose that $f$ is differentiable at $x_0$ with derivative $L_1$, and also differentiable at $x_0$ with derivative $L_2$. Then $L_1 = L_2$.
    > proof:
    > because $L_1 \not= L_2$, so there exists $v \in \mathbb{R}^n \wedge v \not= 0$, s.t. $L_1(v) \not= L_2(v)$.
    > $R_1(t) := f(x_0 + tv) - f(x_0) - L_1(tv)$.
    > $R_2(t) := f(x_0 + tv) - f(x_0) - L_2(tv)$.
    > $t(L_1(v) - L_2(v)) = L_1(tv) - L_2(tv) = R_2(t) - R_1(t)$.
    > $\frac{||(L_1(v) - L_2(v))||}{||v||} = \frac{||t(L_1(v) - L_2(v))||}{||tv||} = \frac{||R_2(t) - R_1(t)||}{||tv||} \leq \frac{||R_2(t)||}{||tv||} + \frac{||R_1(t)||}{||tv||}$.
    > so $L_1(v) - L_2(v) = 0$, contradiction.

- 梯度：设 $X \subseteq \mathbb{R}^n$，$f: X \rightarrow \mathbb{R}$ 是一个定义在 $X$ 上的实值函数（标量场）。若 $f$ 在内点 $x_0 \in X$ 处可微，存在唯一的线性变换 $L: \mathbb{R}^n \rightarrow \mathbb{R}$（即 $f'(x_0)$）。由于 $L$ 是从 $\mathbb{R}^n$ 到 $\mathbb{R}$ 的线性映射，根据里斯表示定理 (Riesz Representation Theorem)，在给定内积 $\langle \cdot, \cdot \rangle$ 的欧几里得空间中，必然存在唯一的向量 $v \in \mathbb{R}^n$，使得对于任意 $h \in \mathbb{R}^n$，都有：$$L(h) = \langle v, h \rangle$$这个唯一的向量 $v$ 就称为 $f$ 在 $x_0$ 处的梯度，记作 $\nabla f(x_0)$ 或 $\text{grad } f(x_0)$。

- 方向导数：设 $u$ 为单位向量（$\|u\|=1$），$f$ 在 $x_0$ 处沿方向 $u$ 的方向导数定义为：$$D_u f(x_0) = \lim_{t \to 0} \frac{f(x_0 + tu) - f(x_0)}{t}$$将全微分公式代入上式（令 $h = tu$）：$$D_u f(x_0) = \lim_{t \to 0} \frac{f(x_0) + L(tu) + o(\|tu\|) - f(x_0)}{t}$$由于 $L$ 是线性变换，$L(tu) = t L(u)$，且 $\|tu\| = |t|\|u\| = |t|$：$$D_u f(x_0) = \lim_{t \to 0} \frac{t L(u) + o(t)}{t} = L(u)$$

## 3. Properties

**可微蕴含连续.** 设 $X\subseteq\mathbb{R}^n$，$x_0\in X$ 是 $X$ 的极限点，$f:X\to\mathbb{R}^m$ 在 $x_0$ 可微。则 $f$ 在 $x_0$ 连续。

> proof
>
> 由可微定义，存在线性映射 $L:\mathbb{R}^n\to\mathbb{R}^m$，使得
>
> $$
> f(x)=f(x_0)+L(x-x_0)+r(x),
> $$
>
> 其中
>
> $$
> d(r(x),0)=o\big(d(x,x_0)\big)\quad(x\to x_0,\ x\in X\setminus\{x_0\}).
> $$
>
> 因此 $r(x)\to 0$。
>
> 再证 $L(h)\to 0$（$h\to 0$）。设 $e_1,\ldots,e_n$ 为 $\mathbb{R}^n$ 的标准基，$h=\sum_{i=1}^n h_i e_i$。欧氏距离满足 $d(h,0)^2=\sum_{k=1}^n h_k^2$，故 $h_i^2\le d(h,0)^2$。记 $a=|h_i|$，$b=d(h,0)$，则 $a,b\ge 0$ 且 $a^2\le b^2$。若 $a>b$，则 $a-b>0$、$a+b>0$，从而 $a^2-b^2=(a-b)(a+b)>0$。因此 $a\le b$，即 $|h_i|\le d(h,0)$。并且
>
> $$
> L(h)=\sum_{i=1}^n h_i L(e_i).
> $$
>
> 三角不等式与绝对齐性给出
>
> $$
> d(L(h),0)\le\sum_{i=1}^n |h_i|\,d(L(e_i),0)\le d(h,0)\sum_{i=1}^n d(L(e_i),0).
> $$
>
> 右端在 $h\to 0$ 时趋于 $0$，所以 $L(x-x_0)\to 0$。于是
>
> $$
> d(f(x),f(x_0))\le d(L(x-x_0),0)+d(r(x),0)\to 0.
> $$
>
> 故
>
> $$
> \boxed{\lim_{\substack{x\to x_0\\ x\in X}}f(x)=f(x_0).}
> $$

1. Let $F$ be a field, $\langle F, F^n \rangle=:F^n$, $f: F^n \rightarrow F^m$ be a linear mapping. Then $\exists L \in F^{m \times n}$, s.t. $f(x) = Lx$. Furthermore, $L$ is unique. <span id="1"></span>
2. 设 $f,g:[a,b]\to\mathbb{R}$ 在 $x\in[a,b]$ 可微。则 $f+g$ 与 $fg$ 在 $x$ 可微。若 $g(x)\neq 0$，则 $f/g$ 在 $x$ 可微。并且
   1. $(f+g)'(x) = f'(x) + g'(x)$
   2. $(fg)'(x) = f'(x)g(x) + f(x)g'(x)$
   3. $\left(\frac{f}{g}\right)'(x) = \frac{g(x)f'(x) - g'(x)f(x)}{g(x)^2}$
3. Let $f: \mathbb{R}^n \rightarrow \mathbb{R}^m$ be a function, and $f$ is differentiable at $x_0$ on $X$. $g: \mathbb{R}^m \rightarrow \mathbb{R}^k$ be a function, and $g$ is differentiable at $f(x_0)$ on $f(X)$. Then $g \circ f$ is differentiable at $x_0$ on $X$, and $(g \circ f)'(x_0) = g'(f(x_0)) \circ f'(x_0)$. <span id="3"></span>
4. 梯度方向是方向导数最大的方向。

