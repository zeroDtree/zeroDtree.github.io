---
title: 复数
---

## Prerequisites

- [[数学分析/real-number]]
- [[数学分析/向量空间]]

## 定义

$\mathcal{D} = \mathbb{R} \times \mathbb{R}$

定义$\mathcal{D}$上的加法和乘法：

$(a,b) + (c,d) = (a+c,b+d)$

$(a,b) \times (c,d) = (ac-bd,ad+bc)$

容易验证$\mathcal{D}$关于上述加法满足如下性质

- 加法交换律
- 加法结合律
- 加法单位元
- 加法逆元

容易验证$\mathcal{D}$关于上述乘法满足如下性质

- 乘法交换律
- 乘法结合律
- 乘法单位元
- 乘法逆元, 若$(a,b) \neq (0,0)$,则其乘法逆元为$\left(\frac{a}{a^2+b^2},\frac{-b}{a^2+b^2}\right)$

容易验证乘法对加法满足分配律

因此$\mathcal{D}$关于上述加法和乘法构成一个域, 称为复数域, 记作$\mathbb{C}$

将复数$(a,b)$记作$a+bi$

## 内积

$\mathbb{C}$可被看作向量空间$\langle \mathbb{C}, \mathbb{C} \rangle$

定义$f(a, b) = a \overline{b}$, 易知$f$是$\mathbb{C}$上的内积

内积诱导范数，范数诱导度量。qq

且内积$f$诱导的度量空间与$R^2$上的度量空间同胚。

## 共轭

定义复数$z=a+bi$的共轭为$\overline{z}=a-bi$

容易验证共轭满足如下性质

- $\overline{z_1+z_2}=\overline{z_1}+\overline{z_2}$
- $\overline{z_1z_2}=\overline{z_1}\overline{z_2}$
- $\overline{\overline{z}}=z$
- $z\overline{z}=|z|^2$
