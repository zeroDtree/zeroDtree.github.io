---
title: svd
tags:
  - 线性代数
---

## Prerequisites

- [[线性代数/norm]]

设

$$
A\in\mathbb C^{m\times n},
\qquad
p:=\min\{m,n\},
\qquad
r:=\operatorname{rank}(A).
$$

记 $A^H$ 为共轭转置，$\mathcal R(A)$ 为像空间，$\mathcal N(A)$ 为核空间。对实矩阵，$A^H=A^T$，下文的酉矩阵相应退化为正交矩阵。

## 1. 奇异值分解

### 1.1. 完整 SVD

任意矩阵 $A\in\mathbb C^{m\times n}$ 都可以分解为

$$
\boxed{A=U\Sigma V^H,}
$$

其中

$$
U=[u_1\ \cdots\ u_m]\in\mathbb C^{m\times m},
\qquad
V=[v_1\ \cdots\ v_n]\in\mathbb C^{n\times n}
$$

都是酉矩阵，而 $\Sigma\in\mathbb R^{m\times n}$ 是矩形对角矩阵：

$$
\Sigma=
\begin{pmatrix}
\Sigma_r&0\\
0&0
\end{pmatrix},
\qquad
\Sigma_r=\operatorname{diag}(\sigma_1,\ldots,\sigma_r).
$$

若 $r>0$，正奇异值满足

$$
\sigma_1\ge\cdots\ge\sigma_r>0.
$$

若 $r<p$，则其余奇异值满足 $\sigma_{r+1}=\cdots=\sigma_p=0$。

$\sigma_1,\ldots,\sigma_p$ 称为 $A$ 的**奇异值**；$u_i$ 与 $v_i$ 分别称为左奇异向量与右奇异向量。

对每个 $1\le i\le r$，

$$
\boxed{Av_i=\sigma_i u_i,}
\qquad
\boxed{A^Hu_i=\sigma_i v_i.}
$$

其余奇异向量满足

$$
Av_j=0\quad(r<j\le n),
\qquad
A^Hu_i=0\quad(r<i\le m).
$$

### 1.2. 紧 SVD

只保留非零奇异值及对应的奇异向量，记

$$
U_r=[u_1\ \cdots\ u_r]\in\mathbb C^{m\times r},
\qquad
V_r=[v_1\ \cdots\ v_r]\in\mathbb C^{n\times r}.
$$

则

$$
\boxed{A=U_r\Sigma_rV_r^H.}
$$

这里

$$
U_r^HU_r=I_r,
\qquad
V_r^HV_r=I_r,
$$

但当 $r<m$ 或 $r<n$ 时，$U_r$、$V_r$ 本身不是方阵。

紧 SVD 也可以写成秩一矩阵之和：

$$
\boxed{A=\sum_{i=1}^r\sigma_i u_iv_i^H.}
$$

### 1.3. 截断 SVD

对 $0\le k\le r$，只保留前 $k$ 个奇异值，得到

$$
A_k
:=U_k\Sigma_kV_k^H
=\sum_{i=1}^k\sigma_i u_iv_i^H.
$$

其中 $\operatorname{rank}(A_k)=k$，并且 $A_r=A$、$A_0=0$。

## 2. 预备结论

### 2.1. $A^HA$ 与 $AA^H$ 半正定

$A^HA\in\mathbb C^{n\times n}$ 与 $AA^H\in\mathbb C^{m\times m}$ 都是 Hermitian 半正定矩阵。

> proof
>
> 首先，
>
> $$
> (A^HA)^H=A^HA,
> \qquad
> (AA^H)^H=AA^H,
> $$
>
> 所以二者都是 Hermitian 矩阵。对任意 $x\in\mathbb C^n$、$y\in\mathbb C^m$，
>
> $$
> x^HA^HAx=\|Ax\|_2^2\ge0,
> \qquad
> y^HAA^Hy=\|A^Hy\|_2^2\ge0.
> $$
>
> 因此二者都是半正定矩阵。

所以它们的特征值均为非负实数，并且都可以酉对角化。

### 2.2. 核空间

有

$$
\boxed{\mathcal N(A^HA)=\mathcal N(A),}
\qquad
\boxed{\mathcal N(AA^H)=\mathcal N(A^H).}
$$

> proof
>
> 以第一个等式为例，若 $Ax=0$，则显然 $A^HAx=0$；反过来，若 $A^HAx=0$，则
>
> $$
> 0=x^HA^HAx=\|Ax\|_2^2,
> $$
>
> 所以 $Ax=0$。第二个等式同理。

由秩–零度定理可得

$$
\operatorname{rank}(A^HA)
=\operatorname{rank}(A)
=\operatorname{rank}(AA^H)
=r.
$$

此外，

$$
\boxed{\mathcal R(A)^\perp=\mathcal N(A^H),}
\qquad
\boxed{\mathcal R(A^H)^\perp=\mathcal N(A).}
$$

> proof
>
> 例如，$y\in\mathcal R(A)^\perp$ 当且仅当 $y^HAx=0$ 对所有 $x\in\mathbb C^n$ 成立，也就是 $A^Hy=0$。另一个等式同理。

### 2.3. 非零特征值

$A^HA$ 与 $AA^H$ 具有相同的非零特征值，并且重数相同。

> proof
>
> 设 $\lambda>0$，分别记相应的特征空间为
>
> $$
> E_\lambda(A^HA)
> \quad\text{和}\quad
> E_\lambda(AA^H).
> $$
>
> 映射
>
> $$
> T:E_\lambda(A^HA)\to E_\lambda(AA^H),
> \qquad
> T(v)=Av
> $$
>
> 是同构，其逆映射为
>
> $$
> T^{-1}(u)=\frac1\lambda A^Hu.
> $$
>
> 事实上，若 $A^HAv=\lambda v$，则
>
> $$
> AA^H(Av)=A(A^HAv)=\lambda Av,
> $$
>
> 并且 $Av\ne0$，否则 $\lambda v=A^HAv=0$ 将推出 $v=0$。类似地，若 $AA^Hu=\lambda u$，则
>
> $$
> A^HA(A^Hu)=A^H(AA^Hu)=\lambda A^Hu.
> $$
>
> 最后，
>
> $$
> \frac1\lambda A^H(Av)=v,
> \qquad
> A\left(\frac1\lambda A^Hu\right)=u.
> $$
>
> 因此两个特征空间同构。由于 $A^HA$ 与 $AA^H$ 都可对角化，非零特征值的几何重数等于代数重数，结论成立。

## 3. SVD 的存在性证明

> proof
>
> 由谱定理，存在 $\mathbb C^n$ 的一组标准正交基 $v_1,\ldots,v_n$，使得
>
> $$
> A^HAv_i=
> \begin{cases}
> \lambda_i v_i,&1\le i\le r,\\
> 0,&r<i\le n,
> \end{cases}
> $$
>
> 其中
>
> $$
> \lambda_1\ge\cdots\ge\lambda_r>0.
> $$
>
> 定义
>
> $$
> \sigma_i:=\sqrt{\lambda_i},
> \qquad
> u_i:=\frac1{\sigma_i}Av_i,
> \qquad
> 1\le i\le r.
> $$
>
> ### 3.1. $u_1,\ldots,u_r$ 标准正交
>
> 对 $1\le i,j\le r$，
>
> $$
> \begin{aligned}
> u_i^Hu_j
> &=\frac1{\sigma_i\sigma_j}v_i^HA^HAv_j\\
> &=\frac{\sigma_j^2}{\sigma_i\sigma_j}v_i^Hv_j\\
> &=\delta_{ij}.
> \end{aligned}
> $$
>
> 因此 $u_1,\ldots,u_r$ 标准正交。它们都属于 $\mathcal R(A)$，且数量恰好等于 $\dim\mathcal R(A)=r$，所以
>
> $$
> \mathcal R(A)=\operatorname{span}\{u_1,\ldots,u_r\}.
> $$
>
> ### 3.2. 左右奇异向量的关系
>
> 根据定义，
>
> $$
> Av_i=\sigma_i u_i.
> $$
>
> 同时，
>
> $$
> A^Hu_i
> =\frac1{\sigma_i}A^HAv_i
> =\frac{\lambda_i}{\sigma_i}v_i
> =\sigma_i v_i.
> $$
>
> 因而 $u_i$ 也是 $AA^H$ 对应于特征值 $\sigma_i^2$ 的特征向量：
>
> $$
> AA^Hu_i=\sigma_i^2u_i.
> $$
>
> ### 3.3. 补全标准正交基
>
> 由
>
> $$
> \mathcal R(A)^\perp=\mathcal N(A^H)
> $$
>
> 可选取 $\mathcal N(A^H)$ 的一组标准正交基 $u_{r+1},\ldots,u_m$。于是
>
> $$
> U=[u_1\ \cdots\ u_m]
> $$
>
> 是酉矩阵。另一方面，第 2.2 节给出
>
> $$
> \mathcal N(A)=\mathcal N(A^HA)
> =\operatorname{span}\{v_{r+1},\ldots,v_n\},
> $$
>
> 所以 $V=[v_1\ \cdots\ v_n]$ 也是酉矩阵。
>
> 对任意 $x\in\mathbb C^n$，
>
> $$
> x=\sum_{i=1}^n(v_i^Hx)v_i,
> $$
>
> 并且 $Av_i=0$ 对 $i>r$ 成立。因此
>
> $$
> Ax
> =\sum_{i=1}^r\sigma_i(v_i^Hx)u_i
> =U\Sigma V^Hx.
> $$
>
> 这对一切 $x$ 都成立，故
>
> $$
> \boxed{A=U\Sigma V^H.}
> $$
>
> 当 $A=0$ 时，取 $\Sigma=0$，并任取两个相应尺寸的酉矩阵 $U,V$ 即可。
>
> Q.E.D.

## 4. 四个基本子空间

SVD 给出了四个基本子空间的标准正交基：

$$
\boxed{
\begin{aligned}
\mathcal R(A)
&=\operatorname{span}\{u_1,\ldots,u_r\},\\
\mathcal N(A^H)
&=\operatorname{span}\{u_{r+1},\ldots,u_m\},\\
\mathcal R(A^H)
&=\operatorname{span}\{v_1,\ldots,v_r\},\\
\mathcal N(A)
&=\operatorname{span}\{v_{r+1},\ldots,v_n\}.
\end{aligned}
}
$$

因此

$$
\mathbb C^m
=\mathcal R(A)\mathbin{\oplus^\perp}\mathcal N(A^H),
\qquad
\mathbb C^n
=\mathcal R(A^H)\mathbin{\oplus^\perp}\mathcal N(A).
$$

对应的正交投影分别为

$$
U_rU_r^H=P_{\mathcal R(A)},
\qquad
V_rV_r^H=P_{\mathcal R(A^H)}.
$$

若

$$
x=\sum_{i=1}^n\alpha_i v_i,
$$

则

$$
Ax=\sum_{i=1}^r\sigma_i\alpha_i u_i.
$$

也就是说，$\mathcal N(A)$ 中的分量被映为零，而 $\mathcal R(A^H)$ 中沿 $v_i$ 的分量被缩放 $\sigma_i$ 倍并映到 $u_i$ 方向。

## 5. 谱分解与基本性质

由 $A=U\Sigma V^H$ 可得

$$
\boxed{A^HA=V\Sigma^H\Sigma V^H,}
\qquad
\boxed{AA^H=U\Sigma\Sigma^HU^H.}
$$

其中

$$
\Sigma^H\Sigma
=\operatorname{diag}(\sigma_1^2,\ldots,\sigma_r^2,0,\ldots,0)
\in\mathbb R^{n\times n},
$$

$$
\Sigma\Sigma^H
=\operatorname{diag}(\sigma_1^2,\ldots,\sigma_r^2,0,\ldots,0)
\in\mathbb R^{m\times m}.
$$

因此：

- $\sigma_i^2$ 是 $A^HA$ 与 $AA^H$ 的非零特征值；
- $\operatorname{rank}(A)$ 等于正奇异值的个数；
- 若 $A$ 是方阵，则

$$
|\det A|=\prod_{i=1}^n\sigma_i.
$$

## 6. 范数与条件数

### 6.1. 谱范数

$$
\boxed{\|A\|_2=\sigma_1}
$$

> proof
>
> 对任意 $x\in\mathbb C^n$，写成
>
> $$
> x=\sum_{i=1}^n\alpha_i v_i.
> $$
>
> 则
>
> $$
> \|Ax\|_2^2
> =\sum_{i=1}^r\sigma_i^2|\alpha_i|^2
> \le\sigma_1^2\sum_{i=1}^n|\alpha_i|^2
> =\sigma_1^2\|x\|_2^2.
> $$
>
> 当 $x=v_1$ 时取等号；当 $A=0$ 时两边均为零。

### 6.2. Frobenius 范数

$$
\boxed{\|A\|_F=\left(\sum_{i=1}^r\sigma_i^2\right)^{1/2}.}
$$

> proof
>
> $$
> \begin{aligned}
> \|A\|_F^2
> &=\operatorname{tr}(A^HA)\\
> &=\operatorname{tr}(\Sigma^H\Sigma)\\
> &=\sum_{i=1}^r\sigma_i^2.
> \end{aligned}
> $$

### 6.3. 酉不变性

若 $Q\in\mathbb C^{m\times m}$、$W\in\mathbb C^{n\times n}$ 都是酉矩阵，则

$$
\boxed{
\|QAW\|_2=\|A\|_2,
\qquad
\|QAW\|_F=\|A\|_F.
}
$$

> proof
>
> 由
>
> $$
> QAW=(QU)\Sigma(W^HV)^H
> $$
>
> 可知右侧也是一个 SVD，所以 $QAW$ 与 $A$ 具有相同的奇异值。再由前两节的结论即得所证。

### 6.4. 2-范数条件数

当 $r=p$ 时，定义

$$
\boxed{\kappa_2(A)=\frac{\sigma_1}{\sigma_p}.}
$$

若 $r<p$，则存在零奇异值，约定

$$
\kappa_2(A)=+\infty.
$$

特别地，对可逆方阵 $A\in\mathbb C^{n\times n}$，

$$
\kappa_2(A)=\|A\|_2\|A^{-1}\|_2
=\frac{\sigma_1}{\sigma_n}.
$$

## 7. 唯一性与非唯一性

设 $A^HA$ 的特征值按降序排列。对 $1\le i\le p$，奇异值由下式唯一确定：

$$
\sigma_i=\sqrt{\lambda_i(A^HA)},
$$

所以按降序排列后的奇异值及其重数是唯一的，但奇异向量一般不唯一。

- 若正奇异值 $\sigma_i$ 是单重的，则对应的 $u_i,v_i$ 在共同乘以一个模为 $1$ 的标量后仍表示同一项；实数情形下，这就是同时改变二者的符号。
- 若某个正奇异值重复出现，可以在对应的左右奇异子空间内同时施加任意酉基变换。
- 与零奇异值对应的向量只需分别构成 $\mathcal N(A^H)$ 与 $\mathcal N(A)$ 的标准正交基，因此通常也不唯一。

所以，唯一的是奇异值和相应的奇异子空间，而不是某一组具体的 $U$ 与 $V$。

## 8. 总结

- 任意复矩阵都存在完整 SVD $A=U\Sigma V^H$；
- 正奇异值是 $A^HA$（或 $AA^H$）正特征值的平方根；
- 紧 SVD 为 $A=U_r\Sigma_rV_r^H=\sum_{i=1}^r\sigma_i u_iv_i^H$；
- 左右奇异向量分别给出四个基本子空间的标准正交基；
- $\|A\|_2=\sigma_1$，$\|A\|_F^2=\sum_i\sigma_i^2$；
- 奇异值唯一，奇异向量在相位、重根子空间及零空间中不唯一。
