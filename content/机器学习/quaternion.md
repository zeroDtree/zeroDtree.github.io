---
title: 四元数与旋转
---

- [1. 加法](#1-加法)
- [2. 乘法](#2-乘法)
- [3. 单位四元数（Unit Quaternion）](#3-单位四元数unit-quaternion)
- [4. 四元数与叉积](#4-四元数与叉积)
- [5. 四元数与旋转轴—角表示的对应关系](#5-四元数与旋转轴角表示的对应关系)
- [6. 用四元数旋转向量](#6-用四元数旋转向量)
- [7. 四元数旋转的组合](#7-四元数旋转的组合)


集合 $\mathbb{H} = \{a+bi+cj+dk \mid a,b,c,d \in \mathbb{R}\}$ 上定义加法和乘法：

### 1. 加法

四元数的加法与向量加法一致：

$$
(a_1+b_1i+c_1j+d_1k) + (a_2+b_2i+c_2j+d_2k) = (a_1+a_2) + (b_1+b_2)i + (c_1+c_2)j + (d_1+d_2)k
$$

知：$\mathbb{H}$关于上述加法构成一个交换群。

- 加法单位元：$0+0i+0j+0k$
- 加法逆元：$-a-bi-cj-dk$

### 2. 乘法

四元数的乘法定义为:

$$
\begin{align*}
&(a_1+b_1i+c_1j+d_1k) (a_2+b_2i+c_2j+d_2k) = \\
&\quad (a_1 a_2 - b_1 b_2 - c_1 c_2 - d_1 d_2) \\
&\quad + (a_1 b_2 + b_1 a_2 + c_1 d_2 - d_1 c_2)i \\
&\quad + (a_1 c_2 - b_1 d_2 + c_1 a_2 + d_1 b_2)j \\
&\quad + (a_1 d_2 + b_1 c_2 - c_1 b_2 + d_1 a_2)k.
\end{align*}
$$

乘法的记忆方法：$i^2=j^2=k^2=ijk=-1, -ij=ij=k, -kj=jk=i, -ik=ki=j$, 然后按数字的乘法法则拆开括号，得到上面的结果。

四元数乘法可用矩阵乘法表示：
我们可以用实矩阵表示四元数，从而把四元数乘法转化为矩阵乘法，而矩阵乘法已知满足结合律。

例如，将四元数 \( q = a + bi + cj + dk \) 表示为下面的实 \( 4\times4 \) 矩阵：

\[
M(q) =
\begin{pmatrix}
a & -b & -c & -d \\
b & a & -d & c \\
c & d & a & -b \\
d & -c & b & a
\end{pmatrix}
\]

可以验证：
\[
M(q_1 q_2) = M(q_1) M(q_2)
\]

于是四元数乘法满足结合律。

也于是四元数乘法对加法满足分配律。

乘法的单位元为$1+0i+0j+0k$

乘法逆元为$\frac{a}{a^2+b^2+c^2+d^2}-\frac{b}{a^2+b^2+c^2+d^2}i-\frac{c}{a^2+b^2+c^2+d^2}j-\frac{d}{a^2+b^2+c^2+d^2}k$

$$
(0+i+0j+0K) (0+0i+j+0K) = (0+0i+0j+1k)
$$

$$
(0+0i+j+0k) (0+i+0j+0k) = (0+0i+0j-1k)
$$

因此乘法不具有交换律

综上，$<\mathbb{H},+,\times>$构成一个非交换除环。

### 3. 单位四元数（Unit Quaternion）

若四元数  
$$
q = a + bi + cj + dk
$$  
满足
$$
a^2 + b^2 + c^2 + d^2 = 1,
$$
则称 $q$ 为**单位四元数**。

单位四元数在旋转表示中起核心作用。

### 4. 四元数与叉积

$q:=(a+\mathbf{v})=(a+v_1i+v_2j+v_3k)$

$$
(a_1+\mathbf{v}_1)(a_2 + \mathbf{v}_2) = ((a_1a_2-\mathbf{v}_1 \mathbf{v}_2) + (a_1\mathbf{v}_2 + a_2\mathbf{v}_1 + \mathbf{v}_1 \times \mathbf{v}_2))
$$

$$
\begin{align*}
& (a+\mathbf{b})(0+\mathbf{v})(a-\mathbf{b}) \\
& = (-\mathbf{b}\mathbf{v} + (a\mathbf{v} + \mathbf{b} \times \mathbf{v}))(a-\mathbf{b})\\
& =0 + (\mathbf{-b}\mathbf{v})(\mathbf{-b}) + a^2\mathbf{v} + a\mathbf{b}\times \mathbf{v} + a\mathbf{v}\times (-\mathbf{b}) + (\mathbf{b}\times \mathbf{v}) \times (-\mathbf{b})\\
&=0 + (\mathbf{b}\mathbf{v})(\mathbf{b}) + a^2\mathbf{v} + 2a\mathbf{b}\times \mathbf{v} + (\mathbf{b}\times \mathbf{v}) \times (-\mathbf{b})\\
& = 0 + (\mathbf{b}\mathbf{v})\mathbf{b} + a^2\mathbf{v} + 2a\mathbf{b}\times \mathbf{v} + \mathbf{b}\times (\mathbf{b}\times \mathbf{v})\\
& = 0 + (\mathbf{b}\mathbf{v})\mathbf{b} + a^2\mathbf{v} + 2a\mathbf{b}\times \mathbf{v} + \mathbf{b}(\mathbf{v}\mathbf{b}) - \mathbf{v} (\mathbf{b}\mathbf{b})\\
&= 0 + 2(\mathbf{b}\mathbf{v})\mathbf{b} + a^2\mathbf{v} + 2a\mathbf{b}\times \mathbf{v}  - \mathbf{v} (\mathbf{b}\mathbf{b})\\
\end{align*}
$$

### 5. 四元数与旋转轴—角表示的对应关系

任意三维空间的旋转可由一个**单位向量**（旋转轴）

$$
\boldsymbol{n} = (n_x, n_y, n_z), \quad \|\boldsymbol{n}\| = 1
$$

和一个**旋转角度** $\theta$ 表示。

与之对应的单位四元数为：

$$
q = \cos\frac{\theta}{2} + (n_x i + n_y j + n_z k)\sin\frac{\theta}{2}:=(\cos\frac{\theta}{2} + \mathbf{n}\sin\frac{\theta}{2})
$$

### 6. 用四元数旋转向量

将三维向量 $\mathbf{v} = (x, y, z)$ 看作“纯虚四元数”：

$$
v = 0 + xi + yj + zk
$$

根据：$(a+\mathbf{b})(0+\mathbf{v})(a-\mathbf{b})=0 + 2(\mathbf{b}\mathbf{v})\mathbf{b} + a^2\mathbf{v} + 2a\mathbf{b}\times \mathbf{v}  - \mathbf{v} (\mathbf{b}\mathbf{b})$

$$
\begin{align*}
q\mathbf{v}q^{-1} &= 0 + 2 \sin^2\frac{\theta}{2}(\mathbf{n}\mathbf{v})\mathbf{n} + (\cos^2 \frac{\theta}{2} - \sin^2 \frac{\theta}{2})(\mathbf{v}) + 2 \cos \frac{\theta}{2} \sin \frac{\theta}{2} (\mathbf{n} \times \mathbf{v})\\
&= 0 + \cos \theta \mathbf{v} + \sin \theta (\mathbf{n} \times \mathbf{v}) + (1-\cos \theta) (\mathbf{v}\mathbf{n})\mathbf{n}
\end{align*}
$$

注意到上式与Rodrigues公式一致。因此四元数乘法$qvq^{-1}$取虚部即可得到旋转后的向量。

若要用单位四元数 $q = a + bi + cj + dk$ 表示的旋转作用在 $\mathbf{v}$ 上，则旋转后的向量为：

$$
v' = q \, v \, q^{-1}
$$

其中：

- $q^{-1} = a - bi - cj - dk$，因为 $q$ 是单位四元数；
- $v'$的实部为0，虚部为旋转后的向量。

注意$(-q)v(-q)^{-1}=q v q^{-1}$, 因此单位四元数两次覆盖了$SO(3)$

### 7. 四元数旋转的组合

若有两个旋转：

- $q_1$ 表示第一次旋转；
- $q_2$ 表示第二次旋转；

则它们的**复合旋转**由四元数乘法给出：

$$
q_{\text{合}} = q_2 q_1
$$

注意顺序：先应用 $q_1$，再应用 $q_2$。
