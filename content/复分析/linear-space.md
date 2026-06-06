---
title: linear space
---

## 函数空间

$X \subseteq \mathbb{C}:= F, V = \{f: X \to \mathbb{C}\}$

- 在$V$上定义加法
  $$
  (f+g)(x) = f(x) + g(x)
  $$

易得$\langle V, + \rangle$是一个交换群

- 在$V$上定义数乘
  $$
  (\lambda f)(x) = \lambda f(x)
  $$

易得

- $(a + b)f = af + bf$
- $a(f + g) = af + ag$
- $(ab)f = a(bf)$
- $1f = f$

所以$\langle F, V \rangle$是一个线性空间

## k阶可导的函数空间

$X \subseteq \mathbb{R}, U_k = \{f: X \to \mathbb{R} \mid f \text{ is differentiable at least k times}\}$

易得$U_k$是$V$的子空间

## 函数空间上的求导(算子)

$D: U_k \to U_{k-1}, (Df)(x) = f'(x)$

有

- $D(f+g) = Df + Dg$
- $D(\lambda f) = \lambda Df$

所以求导算子$D$是线性映射

线性映射复合线性映射仍是线性映射

因此

$$
D^k = D \circ D \circ \cdots \circ D
$$

是线性映射

线性映射的线性组合仍是线性映射,因此

$$
\sum_{i=0}^k \lambda_i D^i
$$

是线性映射

## 多元函数

$X \subseteq \mathbb{C}^n, V = \{f: X \to \mathbb{C}\}$

- 在$V$上定义加法
  $$
  (f+g)(x) = f(x) + g(x)
  $$

易得$\langle V, + \rangle$是一个交换群

- 在$V$上定义数乘
  $$
  (\lambda f)(x) = \lambda f(x)
  $$

易得

- $(a + b)f = af + bf$
- $a(f + g) = af + ag$
- $(ab)f = a(bf)$
- $1f = f$

所以$\langle F, V \rangle$是一个线性空间
