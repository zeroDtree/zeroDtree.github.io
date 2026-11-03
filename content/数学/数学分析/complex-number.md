---
title: 复数构造
tags:
  - 数学分析
---

## 前置

- [[数学分析/实数构造/实数]]

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

## 共轭

定义复数$z=a+bi$的共轭为$\overline{z}=a-bi$

容易验证共轭满足如下性质

- $\overline{z_1+z_2}=\overline{z_1}+\overline{z_2}$
- $\overline{z_1z_2}=\overline{z_1}\overline{z_2}$
- $\overline{\overline{z}}=z$
- $z\overline{z}=a^2+b^2$，记 $|z|^2=a^2+b^2$
