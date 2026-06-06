---
title: Rn与代数与格
---

## 前置

- [[抽象代数/代数]]
- [[抽象代数/格]]
- [[数学分析/有限维赋范线性空间]]

---

## $\mathbb{R}^n$ 在逐点乘法下是一个 Banach 代数

### 代数结构的定义与验证

设 $x, y \in \mathbb{R}^n$。我们定义 $\mathbb{R}^n$ 上的逐点乘法（或称分量乘法）为：$$x \cdot y = (x_1 y_1, x_2 y_2, \dots, x_n y_n)$$显然，对任意 $x, y \in \mathbb{R}^n$，其乘积 $x \cdot y \in \mathbb{R}^n$ 依然成立（对乘法封闭）。验证代数公理：结合律：$$((x \cdot y) \cdot z)_i = (x_i y_i) z_i = x_i (y_i z_i) = (x \cdot (y \cdot z))_i$$分配律：$$(x \cdot (y + z))_i = x_i (y_i + z_i) = x_i y_i + x_i z_i = (x \cdot y + x \cdot z)_i$$（同理可证左分配律）与标量乘法相容（设 $c \in \mathbb{R}$）：$$(c(x \cdot y))_i = c(x_i y_i) = (c x_i) y_i = ((cx) \cdot y)_i$$$$(c(x \cdot y))_i = x_i (c y_i) = (x \cdot (cy))_i$$额外性质：由于实数乘法交换，它是一个交换代数。此外，若引入单位元 $1 = (1, 1, \dots, 1)$，则有 $1 \cdot x = x \cdot 1 = x$，它还是一个含幺代数。

### 赋范代数验证

并为所有的范数都能满足次可乘性：例如$$\|x\|_{bad} = 100|x_1| + 0.01|x_2|$$就不满足次可乘性。

下面证明$\ell^p$范数与$\ell^\infty$范数满足次可乘性

#### 一般 $\ell^p$ 范数的证明

对于任意 $p \ge 1$，定义 $\ell^p$ 范数为 $\|x\|_p = \left( \sum_{i=1}^n |x_i|^p \right)^{1/p}$。考察乘积的范数的 $p$ 次方：$$\|x \cdot y\|_p^p = \sum_{i=1}^n |x_i y_i|^p = \sum_{i=1}^n |x_i|^p |y_i|^p$$对于每一个分量 $|y_i|^p$，它显然不可能超过全体分量的 $p$ 次方和。也就是说：$$\text{对任意 } i, \quad |y_i|^p \le \sum_{j=1}^n |y_j|^p = \|y\|_p^p$$将这个放大关系代入到求和式中：$$\sum_{i=1}^n |x_i|^p |y_i|^p \le \sum_{i=1}^n |x_i|^p \cdot \|y\|_p^p$$因为 $\|y\|_p^p$ 是一个与求和指标 $i$ 无关的常数，可以把它提到求和号外面：$$\sum_{i=1}^n |x_i|^p \cdot \|y\|_p^p = \|y\|_p^p \left( \sum_{i=1}^n |x_i|^p \right) = \|y\|_p^p \cdot \|x\|_p^p$$两边同时开 $p$ 次方根（因为 $p \ge 1$ 且所有项非负，开方保持不等号方向）：$$\|x \cdot y\|_p \le \|x\|_p \|y\|_p$$

Q.E.D.

#### $\ell^\infty$ 范数（上确界范数）的证明

$\|x\|_\infty = \max_{1 \le i \le n} |x_i|$。$$\|x \cdot y\|_\infty = \max_{1 \le i \le n} |x_i y_i| = \max_{1 \le i \le n} (|x_i| \cdot |y_i|)$$由于对任意 $i$，都有 $|x_i| \le \max_j |x_j| = \|x\|_\infty$ 且 $|y_i| \le \max_j |y_j| = \|y\|_\infty$，因此：$$|x_i| \cdot |y_i| \le \|x\|_\infty \cdot \|y\|_\infty$$取最大值后，次可乘性依然成立：$$\|x \cdot y\|_\infty \le \|x\|_\infty \|y\|_\infty$$因此，$(\mathbb{R}^n, \|\cdot\|_\infty)$ 是一个赋范代数。

Q.E.D.

因此，$(\mathbb{R}^n, \|\cdot\|_p)$ 和 $(\mathbb{R}^n, \|\cdot\|_\infty)$ 都是赋范代数。

---

### 范数所诱导的度量的完备性验证

有限维赋范线性空间必然是完备的（即一定是 Banach 空间）。

## $\mathbb{R}^n$ 是一个Banach 格

首先，将 $\mathbb{R}^n$ 视为实向量空间，并赋予**逐点序**（即分量序）：

$$
x \le y \iff x_i \le y_i \quad \text{对每个 } i = 1, \dots, n
$$

在这个偏序下，对任意 $x, y \in \mathbb{R}^n$：

- **上确界** 是**逐点取 $\max$**：
  $$
  x \vee y = (\max(x_1, y_1), \dots, \max(x_n, y_n))
  $$
- **下确界** 是**逐点取 $\min$**：
  $$
  x \wedge y = (\min(x_1, y_1), \dots, \min(x_n, y_n))
  $$

显然这两个运算的结果仍在 $\mathbb{R}^n$ 中，所以 $\mathbb{R}^n$ 是一个格。

- **加法平移不变性**：若 $x \le y$，则对任意 $z$，$(x+z)_i = x_i + z_i \le y_i + z_i = (y+z)_i$，故 $x+z \le y+z$。
- **正标量乘法不变性**：若 $x \le y$ 且 $c \ge 0$，则 $cx_i \le cy_i$，故 $cx \le cy$。

在向量格中，绝对值被定义为：

$$
|x| = x \vee (-x)
$$

在 $\mathbb{R}^n$ 的逐点序下，这正好是逐点取绝对值：

$$
(|x|)_i = |x_i|
$$

这正是我们熟悉的绝对值函数。

因此，$\mathbb{R}^n$ 是一个向量格（Riesz 空间）。

$\mathbb{R}^n$ 是一个 Banach 格

$$
\text{若 } |x| \le |y|, \quad \text{则 } \|x\| \le \|y\|
$$

这里 $|x| \le |y|$ 的意思是**逐点** $|x_i| \le |y_i|$ 对所有 $i$ 成立。

常见范数的验证：

- **$\ell^1$ 范数**：
  $\|x\|_1 = \sum_i |x_i| \le \sum_i |y_i| = \|y\|_1$

- **$\ell^\infty$ 范数**：
  $\|x\|_\infty = \max_i |x_i| \le \max_i |y_i| = \|y\|_\infty$

- **$\ell^p$ 范数**（$p \ge 1$）：
  $\|x\|_p = \big(\sum_i |x_i|^p\big)^{1/p} \le \big(\sum_i |y_i|^p\big)^{1/p} = \|y\|_p$
  （因为每个分量 $|x_i|^p \le |y_i|^p$）

由于 $\mathbb{R}^n$ 是有限维的，在这些范数下都是完备的，因此它是一个 Banach 格。
