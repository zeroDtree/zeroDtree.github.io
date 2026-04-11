- [n阶向量微分方程](#n阶向量微分方程)
- [$n$阶线性向量微分方程](#n阶线性向量微分方程)
- [$n$阶齐次线性向量微分方程](#n阶齐次线性向量微分方程)
- [$n$阶齐次常系数线性向量微分方程](#n阶齐次常系数线性向量微分方程)
  - [举例](#举例)

## n阶向量微分方程

设 $\mathbf{y}(t) = [y_1(t), y_2(t), ..., y_n(t)]^T$

一个n阶向量微分方程的典型形式为：

$$
\frac{d^n \mathbf{y}}{dt^n} = \mathbf{F}(t, \mathbf{y}, \frac{d\mathbf{y}}{dt}, \frac{d^2\mathbf{y}}{dt^2}, ..., \frac{d^{n-1}\mathbf{y}}{dt^{n-1}})
$$

其中 $\mathbf{F}$ 是一个向量值函数，它依赖于$t$ 和 $\mathbf{y}$ 的各阶导数。

## $n$阶线性向量微分方程

一个 $n$ 阶线性向量微分方程通常可以写成如下的形式：

$$
\frac{d^n \mathbf{y}}{dt^n} + a_{n-1}(t) \frac{d^{n-1} \mathbf{y}}{dt^{n-1}} + \cdots + a_1(t) \frac{d\mathbf{y}}{dt} + a_0(t) \mathbf{y} = \mathbf{g}(t)
$$

其中：

- $t\in \mathbb{C}$
- $\mathbf{y}(t)\in \mathbb{C}^m$
- $a_i(t)\in \mathbb{C}^{m\times m}$
- $\mathbf{g}(t)\in \mathbb{C}^m$

## $n$阶齐次线性向量微分方程

一个 $n$ 阶齐次线性向量微分方程可以表示为：

$$
\frac{d^n \mathbf{y}}{dt^n} + a_{n-1}(t) \frac{d^{n-1} \mathbf{y}}{dt^{n-1}} + \cdots + a_1(t) \frac{d\mathbf{y}}{dt} + a_0(t) \mathbf{y} = 0
$$

## $n$阶齐次常系数线性向量微分方程

$$
\frac{d^n \mathbf{y}}{dt^n} + A_{n-1} \frac{d^{n-1} \mathbf{y}}{dt^{n-1}} + \cdots + A_1 \frac{d\mathbf{y}}{dt} + A_0 \mathbf{y} = 0
$$

假设解的形式为：

$$
\mathbf{y}(t) = e^{\lambda t} \mathbf{v}
$$

其中，$\lambda$ 是特征值，$\mathbf{v}$ 是特征向量。代入方程后得到特征方程：

$$
\begin{align*}
(\lambda^n e^{\lambda t} I + A_{n-1} \lambda^{n-1} e^{\lambda t} I + \cdots + A_1 \lambda e^{\lambda t} I + A_0 e^{\lambda t} I) \mathbf{v} &= 0 \\
(\lambda^n I + A_{n-1} \lambda^{n-1} + \cdots + A_1 \lambda + A_0) \mathbf{v} &= 0
\end{align*}
$$

所有满足特征方程的 $\lambda$ 和 $\mathbf{v}$ 都可以确定一个解$\mathbf{y}(t) = e^{\lambda t} \mathbf{v}$。因为齐次微分方程的解空间是线性算子的核空间，所以所有解构成一个向量空间。

因此只要找到这个向量空间的一组基，就可以得到齐次微分方程的通解。

### 举例

$q\in \mathbb{C}^m, D\in \text{Sym}_m(\mathbb{R}),t\in \mathbb{R}$

$$
\frac{d^2 \mathbf{q}}{dt^2} = -D \mathbf{q}
$$

移项表示为标准形式：

$$
\frac{d^2 \mathbf{q}}{dt^2} + D \mathbf{q} = 0
$$

设$\mathbf{q}(t) = e^{\lambda t} \mathbf{v}$

特征方程为：

$$
(\lambda^2 I + D) \mathbf{v} = 0
$$




即$D\mathbf{v} = -\lambda^2 \mathbf{v}$

表明$-\lambda^2$是$D$的特征值，$\mathbf{v}$是$D$的特征向量。

因为$D$是实对称矩阵，所以$D$可以对角化，即存在正交矩阵$P$，使得$D = P \Lambda P^T$，其中$\Lambda$是对角矩阵，对角线上的元素为$D$的特征值。$\Lambda = \text{diag}(\lambda_1, \lambda_2, ..., \lambda_m) \in \mathbb{R}^{m\times m}$,且$\lambda_1 \leq \lambda_2 \leq ... \leq \lambda_m$, $P=[\mathbf{p}_1, \mathbf{p}_2, ..., \mathbf{p}_m] \in \mathbf{O}_m(\mathbb{R})$

因此，方程的解为：

$$
\mathbf{q}(t) = c_1 e^{\sqrt{-\lambda_1} t} \mathbf{p}_1 + c_2 e^{\sqrt{-\lambda_2} t} \mathbf{p}_2 + ... + c_m e^{\sqrt{-\lambda_m} t} \mathbf{p}_m
$$
