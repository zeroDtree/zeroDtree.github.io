---
title: 向量范数与矩阵范数
tags:
  - 线性代数
---

> [!warning]
> 此内容由AI生成，尚未审查完。

## Prerequisites

-
- [[线性代数/diagonalization]]

若无特别说明，向量空间定义在 $\mathbb C$ 上，矩阵

$$
A=(a_{ij})\in\mathbb C^{m\times n}.
$$

记 $A^H$ 为 $A$ 的共轭转置；在实数情形下，$A^H=A^T$，酉矩阵相应退化为正交矩阵。

## 1. 向量范数

### 1.1. 定义

设 $V$ 是复向量空间。函数

$$
\|\cdot\|:V\to\mathbb R
$$

称为 $V$ 上的一个**范数**，如果对任意 $x,y\in V$ 和 $\alpha\in\mathbb C$ 都满足：

1. **正定性**

$$
\|x\|\ge 0,
\qquad
\|x\|=0\Longleftrightarrow x=0;
$$

2. **绝对齐次性**

$$
\|\alpha x\|=|\alpha|\,\|x\|;
$$

3. **三角不等式**

$$
\|x+y\|\le \|x\|+\|y\|.
$$

### 1.2. 向量 $p$-范数

对 $x=(x_1,\ldots,x_n)^T\in\mathbb C^n$ 和 $1\le p<\infty$，定义

$$
\boxed{
\|x\|_p
=
\left(\sum_{i=1}^n|x_i|^p\right)^{1/p}.
}
$$

当 $p=\infty$ 时，定义

$$
\boxed{
\|x\|_\infty=\max_{1\le i\le n}|x_i|.
}
$$

最常用的三个例子是

$$
\|x\|_1=\sum_{i=1}^n|x_i|,
\qquad
\|x\|_2=\sqrt{x^Hx},
\qquad
\|x\|_\infty=\max_i|x_i|.
$$

其中 $\|\cdot\|_2$ 是标准内积诱导的 Euclidean 范数。$p$-范数的三角不等式是 Minkowski 不等式。

若 $1\le p\le q\le\infty$，则有限维空间中的这些范数满足

$$
\boxed{
\|x\|_q
\le
\|x\|_p
\le
n^{\,1/p-1/q}\|x\|_q,
}
$$

其中约定 $1/\infty=0$。因此有限维空间中的所有 $p$-范数都等价。

## 2. 矩阵范数与诱导范数

### 2.1. 一般矩阵范数

将 $\mathbb C^{m\times n}$ 看作一个向量空间后，任何满足范数三条公理的函数都可以称为矩阵范数。

当矩阵乘法有定义时，若一族矩阵范数还满足

$$
\boxed{
\|AB\|\le \|A\|\,\|B\|,
}
$$

则称它具有**次乘性**。有些教材直接把次乘性列入“矩阵范数”的定义，因此使用某个矩阵范数前需要先确认约定。

### 2.2. 诱导 $p$-范数

矩阵 $A\in\mathbb C^{m\times n}$ 表示线性映射

$$
A:(\mathbb C^n,\|\cdot\|_p)\to(\mathbb C^m,\|\cdot\|_p).
$$

由向量 $p$-范数诱导的矩阵范数定义为

$$
\boxed{
\|A\|_p
:=
\sup_{x\ne0}\frac{\|Ax\|_p}{\|x\|_p}
=
\max_{\|x\|_p=1}\|Ax\|_p.
}
$$

这里可以写成最大值，是因为有限维空间的单位球面是紧集，而 $x\mapsto\|Ax\|_p$ 连续。诱导范数也称为**算子范数**或**从属范数**。

由定义立刻得到相容性：

$$
\boxed{
\|Ax\|_p\le \|A\|_p\|x\|_p.
}
$$

它确实是一个范数。例如，

$$
\begin{aligned}
\|A+B\|_p
&=\max_{\|x\|_p=1}\|(A+B)x\|_p\\
&\le
\max_{\|x\|_p=1}
\bigl(\|Ax\|_p+\|Bx\|_p\bigr)\\
&\le \|A\|_p+\|B\|_p.
\end{aligned}
$$

绝对齐次性可直接由定义得到；若 $\|A\|_p=0$，则对每个标准基向量 $e_j$ 都有 $Ae_j=0$，所以 $A=0$，正定性也成立。

### 2.3. 次乘性

设 $A\in\mathbb C^{m\times n}$、$B\in\mathbb C^{n\times k}$。由相容性，

$$
\|ABx\|_p
\le
\|A\|_p\|Bx\|_p
\le
\|A\|_p\|B\|_p\|x\|_p.
$$

对所有 $\|x\|_p=1$ 的向量取最大值，得到

$$
\boxed{
\|AB\|_p\le \|A\|_p\|B\|_p.
}
$$

特别地，

$$
\|I_n\|_p=1.
$$

## 3. 常用诱导矩阵范数

### 3.1. 诱导 $1$-范数

诱导 $1$-范数等于绝对列和的最大值：

$$
\boxed{
\|A\|_1
=
\max_{1\le j\le n}\sum_{i=1}^m|a_{ij}|.
}
$$

事实上，对任意 $x\in\mathbb C^n$，

$$
\begin{aligned}
\|Ax\|_1
&=\sum_{i=1}^m
\left|\sum_{j=1}^n a_{ij}x_j\right|\\
&\le
\sum_{j=1}^n
\left(\sum_{i=1}^m|a_{ij}|\right)|x_j|\\
&\le
\left(
\max_j\sum_i|a_{ij}|
\right)\|x\|_1.
\end{aligned}
$$

反过来，取绝对列和最大的第 $j_0$ 列及标准基向量 $e_{j_0}$，便有

$$
\|Ae_{j_0}\|_1
=
\sum_{i=1}^m|a_{ij_0}|.
$$

所以这个上界可以取到。

### 3.2. 诱导 $\infty$-范数

诱导 $\infty$-范数等于绝对行和的最大值：

$$
\boxed{
\|A\|_\infty
=
\max_{1\le i\le m}\sum_{j=1}^n|a_{ij}|.
}
$$

一方面，

$$
\begin{aligned}
\|Ax\|_\infty
&=
\max_i\left|\sum_{j=1}^n a_{ij}x_j\right|\\
&\le
\max_i\sum_{j=1}^n|a_{ij}|\,|x_j|\\
&\le
\left(
\max_i\sum_j|a_{ij}|
\right)\|x\|_\infty.
\end{aligned}
$$

另一方面，设第 $i_0$ 行的绝对行和最大，并令

$$
x_j=
\begin{cases}
\overline{a_{i_0j}}/|a_{i_0j}|,&a_{i_0j}\ne0,\\
1,&a_{i_0j}=0.
\end{cases}
$$

则 $\|x\|_\infty=1$，而

$$
(Ax)_{i_0}
=
\sum_{j=1}^n|a_{i_0j}|,
$$

所以上界同样可以取到。

### 3.3. 诱导 $2$-范数：谱范数

诱导 $2$-范数称为矩阵的**谱范数**：

$$
\boxed{
\|A\|_2
=
\max_{x\ne0}\frac{\|Ax\|_2}{\|x\|_2}
=
\max_{\|x\|_2=1}\|Ax\|_2.
}
$$

由于 $A^HA$ 是 Hermitian 半正定矩阵，

$$
\|Ax\|_2^2=x^HA^HAx.
$$

对 $A^HA$ 使用谱定理和 Rayleigh 商可得

$$
\boxed{
\|A\|_2
=
\sqrt{\lambda_{\max}(A^HA)}.
}
$$

其中 $\lambda_{\max}(A^HA)$ 是 $A^HA$ 的最大特征值。特别地，

$$
\boxed{
\|A^H\|_2=\|A\|_2.
}
$$

也可以直接由 Euclidean 范数的对偶表示

$$
\|z\|_2
=
\max_{\|y\|_2=1}|y^Hz|
$$

得到最后一个等式。

### 3.4. 谱范数的酉不变性

设

$$
Q\in\mathbb C^{m\times m},
\qquad
W\in\mathbb C^{n\times n}
$$

都是酉矩阵。酉矩阵保持 Euclidean 范数，并且把单位球面双射到自身，所以

$$
\begin{aligned}
\|QAW\|_2
&=
\max_{\|x\|_2=1}\|QAWx\|_2\\
&=
\max_{\|x\|_2=1}\|AWx\|_2\\
&=
\max_{\|y\|_2=1}\|Ay\|_2\\
&=\|A\|_2.
\end{aligned}
$$

因此

$$
\boxed{
\|QAW\|_2=\|A\|_2.
}
$$

一般的诱导 $p$-范数在 $p\ne2$ 时并不具有任意酉变换下的不变性。

## 4. Frobenius 范数

### 4.1. 定义与等价表达式

Frobenius 范数定义为所有矩阵元素的平方和开根号：

$$
\boxed{
\|A\|_F
:=
\left(
\sum_{i=1}^m\sum_{j=1}^n|a_{ij}|^2
\right)^{1/2}.
}
$$

它有如下等价表达式：

$$
\boxed{
\|A\|_F^2
=
\operatorname{tr}(A^HA)
=
\operatorname{tr}(AA^H).
}
$$

矩阵空间上的 Frobenius 内积为

$$
\langle A,B\rangle_F
:=
\operatorname{tr}(B^HA)
=
\sum_{i=1}^m\sum_{j=1}^n
a_{ij}\overline{b_{ij}},
$$

而

$$
\|A\|_F=\sqrt{\langle A,A\rangle_F}.
$$

所以 Frobenius 范数就是把矩阵按元素视为 $mn$ 维向量时的 Euclidean 范数。

需要注意，Frobenius 范数虽然是矩阵空间内积诱导的范数，却不是向量 $2$-范数诱导的算子范数。例如，当 $n>1$ 时，

$$
\|I_n\|_F=\sqrt n,
\qquad
\|I_n\|_2=1.
$$

### 4.2. Frobenius 范数的酉不变性

仍设 $Q\in\mathbb C^{m\times m}$、$W\in\mathbb C^{n\times n}$ 为酉矩阵。利用 $Q^HQ=I_m$、$WW^H=I_n$ 以及迹的循环不变性，

$$
\begin{aligned}
\|QAW\|_F^2
&=
\operatorname{tr}\bigl((QAW)^H(QAW)\bigr)\\
&=
\operatorname{tr}(W^HA^HQ^HQAW)\\
&=
\operatorname{tr}(W^HA^HAW)\\
&=
\operatorname{tr}(A^HAWW^H)\\
&=
\operatorname{tr}(A^HA).
\end{aligned}
$$

因此

$$
\boxed{
\|QAW\|_F=\|A\|_F.
}
$$

### 4.3. 乘积估计

设 $A\in\mathbb C^{m\times n}$、$B\in\mathbb C^{n\times k}$，并把 $B$ 的列记为 $b_1,\ldots,b_k$。则

$$
\begin{aligned}
\|AB\|_F^2
&=
\sum_{j=1}^k\|Ab_j\|_2^2\\
&\le
\sum_{j=1}^k
\|A\|_2^2\|b_j\|_2^2\\
&=
\|A\|_2^2\|B\|_F^2.
\end{aligned}
$$

结合共轭转置可得另一侧的估计，故

$$
\boxed{
\|AB\|_F
\le
\min\bigl\{
\|A\|_2\|B\|_F,\,
\|A\|_F\|B\|_2
\bigr\}.
}
$$

又因为 $\|A\|_2\le\|A\|_F$，所以

$$
\boxed{
\|AB\|_F\le\|A\|_F\|B\|_F.
}
$$

因此 Frobenius 范数也具有次乘性。

## 5. 常用范数之间的关系

### 5.1. 谱范数与 Frobenius 范数

对任意 $x\in\mathbb C^n$，逐行使用 Cauchy–Schwarz 不等式可得

$$
\|Ax\|_2^2
\le
\left(
\sum_{i=1}^m\sum_{j=1}^n|a_{ij}|^2
\right)\|x\|_2^2
=
\|A\|_F^2\|x\|_2^2.
$$

因此

$$
\|A\|_2\le\|A\|_F.
$$

另一方面，若 $e_1,\ldots,e_n$ 是 $\mathbb C^n$ 的标准基，则

$$
\|A\|_F^2
=
\sum_{j=1}^n\|Ae_j\|_2^2
\le
n\|A\|_2^2.
$$

对 $A^H$ 使用同样的结论，并利用

$$
\|A^H\|_F=\|A\|_F,
\qquad
\|A^H\|_2=\|A\|_2,
$$

还可得到 $\|A\|_F\le\sqrt m\,\|A\|_2$。综上，

$$
\boxed{
\|A\|_2
\le
\|A\|_F
\le
\sqrt{\min\{m,n\}}\,\|A\|_2.
}
$$

### 5.2. $1$-范数、$\infty$-范数与谱范数

对任意 $x\in\mathbb C^n$，

$$
\begin{aligned}
\|Ax\|_2^2
&=
\sum_i
\left|\sum_j a_{ij}x_j\right|^2\\
&\le
\sum_i
\left(\sum_j|a_{ij}|\right)
\left(\sum_j|a_{ij}|\,|x_j|^2\right)\\
&\le
\|A\|_\infty
\sum_j
\left(\sum_i|a_{ij}|\right)|x_j|^2\\
&\le
\|A\|_\infty\|A\|_1\|x\|_2^2.
\end{aligned}
$$

所以

$$
\boxed{
\|A\|_2
\le
\sqrt{\|A\|_1\|A\|_\infty}.
}
$$

### 5.3. 谱范数与谱半径

“谱范数”和“谱半径”是两个不同的概念。对方阵 $A\in\mathbb C^{n\times n}$，谱半径定义为

$$
\rho(A):=\max_{\lambda\in\sigma(A)}|\lambda|.
$$

若 $Av=\lambda v$ 且 $v\ne0$，则对任意诱导范数都有

$$
|\lambda|\,\|v\|
=
\|Av\|
\le
\|A\|\,\|v\|,
$$

因此

$$
\boxed{
\rho(A)\le\|A\|.
}
$$

特别地，$\rho(A)\le\|A\|_2$，但一般不取等号。例如

$$
N=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix}
$$

满足 $\rho(N)=0$，而 $\|N\|_2=1$。

## 6. 算例

令

$$
A=
\begin{pmatrix}
1&-2\\
3&4
\end{pmatrix}.
$$

由绝对列和、绝对行和以及元素平方和可得

$$
\|A\|_1=6,
\qquad
\|A\|_\infty=7,
\qquad
\|A\|_F=\sqrt{30}.
$$

又因为

$$
A^HA
=
\begin{pmatrix}
10&10\\
10&20
\end{pmatrix}
$$

的最大特征值为 $15+5\sqrt5$，所以

$$
\|A\|_2=\sqrt{15+5\sqrt5}.
$$

这个例子表明，同一个矩阵在不同范数下通常具有不同的大小。

## 7. 与奇异值的关系

学完 [[线性代数/svd]] 后，上面的两个范数还可以写成更直观的形式。若 $A\ne0$ 且

$$
\sigma_1\ge\cdots\ge\sigma_r>0
$$

是 $A$ 的正奇异值，$r=\operatorname{rank}(A)$，则

$$
\boxed{
\|A\|_2=\sigma_1,
\qquad
\|A\|_F
=
\left(\sum_{i=1}^r\sigma_i^2\right)^{1/2}.
}
$$

于是前面的范数关系可以加强为

$$
\boxed{
\|A\|_2
\le
\|A\|_F
\le
\sqrt r\,\|A\|_2.
}
$$

当 $A=0$ 时，上式相应地理解为 $\|A\|_2=\|A\|_F=0$。前六节不依赖 SVD，因此可以作为构造 SVD 时的前置知识。

## 8. 总结

- $\|x\|_p$ 衡量向量的大小；$\|A\|_p$ 表示由同一个向量 $p$-范数诱导的算子范数。
- $\|A\|_1$ 是最大绝对列和，$\|A\|_\infty$ 是最大绝对行和。
- $\|A\|_2=\sqrt{\lambda_{\max}(A^HA)}$，它也称为谱范数。
- $\|A\|_F^2=\operatorname{tr}(A^HA)$；Frobenius 范数不是诱导 $2$-范数。
- 诱导范数和 Frobenius 范数都具有次乘性；谱范数与 Frobenius 范数都具有酉不变性。
