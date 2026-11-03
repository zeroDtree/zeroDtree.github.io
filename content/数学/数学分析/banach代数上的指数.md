---
date: 2026-10-29
title: Banach代数上的指数
tags:
 - 数学分析
---

## 前置

- [[数学分析/banach代数上的级数]]

设 $A$ 是实或复含幺 Banach 代数，且 $\|1\|=1$。$e^a$ 按 [[数学分析/banach代数上的级数|指数级数]] 定义。

**引理（二项式展开）.** 设 $a,b\in A$ 且 $ab=ba$。则对任意整数 $n\geq 0$，

$$
(a+b)^n=\sum_{k=0}^{n}C_n^k\,a^kb^{n-k}.
$$

> proof
>
> $ab=ba$ 时，$a$、$b$ 与单位元生成的含幺子环是交换环。 的定理 (9) 用在这个子环上。

**引理（加法公式）.** 设 $a,b\in A$ 且 $ab=ba$。则 $e^{a+b}=e^ae^b$。

> proof
>
> 记 $s_N(x)=\sum_{n=0}^{N}x^n/n!$。由二项式展开，
>
> $$
> \frac{(a+b)^n}{n!}=\sum_{k=0}^{n}\frac{C_n^k}{n!}\,a^kb^{n-k}.
> $$
>
> $C_n^k=\dfrac{n!}{k!(n-k)!}$，故 $\dfrac{C_n^k}{n!}=\dfrac{1}{k!(n-k)!}$。因此
>
> $$
> \frac{(a+b)^n}{n!}=\sum_{k=0}^{n}\frac{a^k}{k!}\frac{b^{n-k}}{(n-k)!},
> $$
>
> 故
>
> $$
> s_N(a+b)=\sum_{k+m\leq N}\frac{a^k}{k!}\frac{b^m}{m!},
> \qquad
> s_N(a)s_N(b)=\sum_{k\leq N,\,m\leq N}\frac{a^k}{k!}\frac{b^m}{m!}.
> $$
>
> 二者之差只含 $k\leq N$、$m\leq N$ 且 $k+m>N$ 的项。取 $N=2M$。这些项或者 $k\geq M+1$，或者 $m\geq M+1$。两类的范数之和大于等于差的范数。由 [[数学分析/banach代数上的级数|幂]] 的估计 $\|a^n\|\leq\|a\|^n$，
>
> $$
> \begin{aligned}
> \|s_N(a)s_N(b)-s_N(a+b)\|
> &\leq
> \left(\sum_{k\geq M+1}\frac{\|a\|^k}{k!}\right)\sum_{m\geq 0}\frac{\|b\|^m}{m!}\\
> &\quad+
> \left(\sum_{m\geq M+1}\frac{\|b\|^m}{m!}\right)\sum_{k\geq 0}\frac{\|a\|^k}{k!}.
> \end{aligned}
> $$
>
> 实指数级数收敛，见 [[数学分析/一些标准的级数|指数级数]]，故 $M\to\infty$ 时右端趋于 $0$。由定义 $s_N(a+b)\to e^{a+b}$。由 [[数学分析/banach代数上的级数|乘法连续性]]，$s_N(a)s_N(b)\to e^ae^b$。因此 $e^{a+b}=e^ae^b$。
