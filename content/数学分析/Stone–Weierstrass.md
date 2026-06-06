---
title: Stone–Weierstrass定理
---

## 前置

- [[数学分析/函数序列]]

## 定义

设$F=\mathbb{R}$或$\mathbb{C}$

设 $K$ 是一个紧 Hausdorff 空间。考虑$F$值连续函数空间 $\mathscr{C}(K, F)$，其范数为 $\|f\| = \sup_{x \in K} |f(x)|$。

- **（代数，Algebra）** 一个子集 $\mathcal{A} \subset \mathscr{C}(K, F)$ 被称为一个 **代数**，如果它对加法、标量乘法（$F$中的数）和乘法封闭：
  - 若 $f, g \in \mathcal{A}$，则 $f + g \in \mathcal{A}$。
  - 若 $f \in \mathcal{A}, c \in \mathbb{C}$，则 $c f \in \mathcal{A}$。
  - 若 $f, g \in \mathcal{A}$，则 $fg \in \mathcal{A}$。

- **（分离点，Separates points）** 我们说代数 $\mathcal{A}$ **分离点**，如果对于任意两个不同的点 $x, y \in K$，存在一个函数 $f \in \mathcal{A}$ 使得 $f(x) \neq f(y)$。

  > 如果 $K$ 不是 Hausdorff 的，那么存在两个不同的点 $x \neq y$，但它们不可能被开集分开（即它们“黏在一起”）。此时，**任何连续函数 $f$ 都必须满足 $f(x) = f(y)$**（因为连续函数不能分离非 Hausdorff 点）。

- **（包含常数函数，Contains constants）** 我们说 $\mathcal{A}$ 包含常数函数，如果对于每个$F$中的常数 $c \in F$，函数 $c$（即对所有 $x \in K$ 有 $f(x) = c$）属于 $\mathcal{A}$。

  > 在 Stone–Weierstrass 的标准陈述中，只要 $\mathcal{A}$ 包含非零常数函数（通常是 $f(x)=1$）即可，结合代数的标量乘法性质，所有的常数函数自然都在其中。

- **（复共轭封闭，Closed under complex conjugation）** 我们说 $\mathcal{A}$ 对$F$共轭封闭，如果对于每个 $f \in \mathcal{A}$，其$F$共轭函数 $\overline{f}$（定义为 $\overline{f}(x) = \overline{f(x)}$）也属于 $\mathcal{A}$。

  > 这是复值情况下强加的一个重要条件。对于实值情况（$\mathscr{C}(K, \mathbb{R})$），这个条件自动满足（因为 $\overline{f} = f$）。

- **（一致闭包，Uniform closure）** 一个代数 $\mathcal{A}$ 的 **一致闭包** $\overline{\mathcal{A}}$ 是包含 $\mathcal{A}$ 的最小一致闭集（即度量空间 $\mathscr{C}(K, F)$ 下的闭包）。

## Weierstrass 逼近定理

**定理陈述：**
设 $f \in \mathscr{C}([0, 1], \mathbb{R})$，则对于任意 $\epsilon > 0$，存在多项式 $P(x)$ 使得：

$$\sup_{x \in [0, 1]} |f(x) - P(x)| < \epsilon$$

### 构造 Bernstein 多项式

对于定义在 $[0, 1]$ 上的函数 $f$，我们定义第 $n$ 阶 Bernstein 多项式为：

$$B_n(f; x) = \sum_{k=0}^n f\left(\frac{k}{n}\right) \binom{n}{k} x^k (1-x)^{n-k}$$

为了简化符号，令 $p_{n,k}(x) = \binom{n}{k} x^k (1-x)^{n-k}$。这些项本质上是二项分布 $B(n, x)$ 的概率质量函数，因此它们满足：

1. $\sum_{k=0}^n p_{n,k}(x) = (x + (1-x))^n = 1$
2. $\sum_{k=0}^n \frac{k}{n} p_{n,k}(x) = x$
3. $\sum_{k=0}^n \left(\frac{k}{n} - x\right)^2 p_{n,k}(x) = \frac{x(1-x)}{n}$

这三个等式本质上是对**二项式展开**的应用。我们从二项式定理开始：

$$(x + y)^n = \sum_{k=0}^n \binom{n}{k} x^k y^{n-k}$$

为了方便计算，我们令 $y = 1-x$，并记 $p_{n,k}(x) = \binom{n}{k} x^k (1-x)^{n-k}$。

---

#### 证明 $\sum_{k=0}^n p_{n,k}(x) = 1$

直接在二项式公式中代入 $y = 1-x$：

$$\sum_{k=0}^n p_{n,k}(x) = \sum_{k=0}^n \binom{n}{k} x^k (1-x)^{n-k} = (x + (1-x))^n = 1^n = 1$$

#### 证明 $\sum_{k=0}^n \frac{k}{n} p_{n,k}(x) = x$

我们需要求 $k$ 的一次加权和。利用恒等式 $k \binom{n}{k} = n \binom{n-1}{k-1}$：

$$\sum_{k=0}^n k \binom{n}{k} x^k (1-x)^{n-k} = \sum_{k=1}^n n \binom{n-1}{k-1} x^k (1-x)^{n-k}$$

（注意 $k=0$ 时项为 0，所以求和从 $1$ 开始）

提取公因子 $nx$：

$$= nx \sum_{k=1}^n \binom{n-1}{k-1} x^{k-1} (1-x)^{(n-1)-(k-1)}$$

令 $j = k-1$：

$$= nx \sum_{j=0}^{n-1} \binom{n-1}{j} x^j (1-x)^{(n-1)-j} = nx \cdot (x + (1-x))^{n-1} = nx \cdot 1 = nx$$

最后两边除以 $n$：

$$\sum_{k=0}^n \frac{k}{n} p_{n,k}(x) = \frac{1}{n} (nx) = x$$

#### 证明 $\sum_{k=0}^n \left(\frac{k}{n} - x\right)^2 p_{n,k}(x) = \frac{x(1-x)}{n}$

先展开平方项：

$$\left(\frac{k}{n} - x\right)^2 = \frac{k^2}{n^2} - 2x\frac{k}{n} + x^2$$

于是求和式变为：

$$\frac{1}{n^2} \sum k^2 p_{n,k} - 2x \sum \frac{k}{n} p_{n,k} + x^2 \sum p_{n,k}$$

利用前面的结果，后两项为 $-2x(x) + x^2(1) = -x^2$。现在只需计算 $\sum k^2 p_{n,k}$。
利用技巧 $k^2 = k(k-1) + k$：

$$\sum_{k=0}^n k(k-1) \binom{n}{k} x^k (1-x)^{n-k} = \sum_{k=2}^n n(n-1) \binom{n-2}{k-2} x^k (1-x)^{n-k}$$

提取 $n(n-1)x^2$：

$$= n(n-1)x^2 \sum_{j=0}^{n-2} \binom{n-2}{j} x^j (1-x)^{n-2-j} = n(n-1)x^2$$

所以：

$$\sum k^2 p_{n,k} = \sum (k(k-1) + k) p_{n,k} = n(n-1)x^2 + nx$$

代入总式：

$$\begin{aligned} \text{原式} &= \frac{n(n-1)x^2 + nx}{n^2} - x^2 \\ &= \frac{n^2x^2 - nx^2 + nx}{n^2} - x^2 \\ &= \left(x^2 - \frac{x^2}{n} + \frac{x}{n}\right) - x^2 \\ &= \frac{x - x^2}{n} = \frac{x(1-x)}{n} \end{aligned}$$

Q.E.D.

### 利用一致连续性

由于 $[0, 1]$ 是紧集，连续函数 $f$ 在其上**一致连续**。
即对于任意 $\epsilon > 0$，存在 $\delta > 0$，使得当 $|x - y| < \delta$ 时，有 $|f(x) - f(y)| < \frac{\epsilon}{2}$。
同时，由于 $f$ 连续，它在 $[0, 1]$ 上是有界的，设 $|f(x)| \le M$。

### 估计误差 $|f(x) - B_n(f; x)|$

利用 $\sum p_{n,k}(x) = 1$，我们可以写出：

$$|f(x) - B_n(f; x)| = \left| \sum_{k=0}^n (f(x) - f(k/n)) p_{n,k}(x) \right| \le \sum_{k=0}^n |f(x) - f(k/n)| p_{n,k}(x)$$

我们将求和索引 $k$ 分为两个集合：

- **集合 $A$**：满足 $|\frac{k}{n} - x| < \delta$ 的 $k$。
- **集合 $B$**：满足 $|\frac{k}{n} - x| \ge \delta$ 的 $k$。

#### 对于集合 $A$（邻域内）：

根据一致连续性，$|f(x) - f(k/n)| < \frac{\epsilon}{2}$。

$$\sum_{k \in A} |f(x) - f(k/n)| p_{n,k}(x) < \frac{\epsilon}{2} \sum_{k \in A} p_{n,k}(x) \le \frac{\epsilon}{2}$$

#### 对于集合 $B$（邻域外）：

此时 $|f(x) - f(k/n)| \le 2M$。根据定义，$|\frac{k}{n} - x| \ge \delta$ 等价于 $\frac{(k/n - x)^2}{\delta^2} \ge 1$。

$$\sum_{k \in B} |f(x) - f(k/n)| p_{n,k}(x) \le 2M \sum_{k \in B} p_{n,k}(x) \le \frac{2M}{\delta^2} \sum_{k \in B} \left(\frac{k}{n} - x\right)^2 p_{n,k}(x)$$

利用步骤 1 中的方差公式：

$$\frac{2M}{\delta^2} \sum_{k \in B} \dots \le \frac{2M}{\delta^2} \cdot \frac{x(1-x)}{n}$$

由于 $x(1-x)$ 在 $[0, 1]$ 上的最大值是 $1/4$，所以：

$$\text{误差}_B \le \frac{2M}{\delta^2} \cdot \frac{1}{4n} = \frac{M}{2n\delta^2}$$

### 完成证明

现在合并两部分误差：

$$|f(x) - B_n(f; x)| < \frac{\epsilon}{2} + \frac{M}{2n\delta^2}$$

只要我们选取足够大的 $n$（使得 $n > \frac{M}{\epsilon\delta^2}$），第二项也会小于 $\frac{\epsilon}{2}$。
从而对于所有的 $x \in [0, 1]$：

$$|f(x) - B_n(f; x)| < \epsilon$$

这意味着 Bernstein 多项式序列 $B_n(f; x)$ 一致收敛于 $f(x)$。

### 关于区间 $[a, b]$ 的说明

如果函数定义在一般的闭区间 $[a, b]$ 上，只需通过线性变换 $t = \frac{x-a}{b-a}$ 将其映射到 $[0, 1]$ 即可。这一变换不改变函数的连续性和多项式的性质。

**证毕。**

## 实值 Stone–Weierstrass 定理

### 利用 Weierstrass 逼近定理处理绝对值

我们需要证明：如果 $f \in \overline{\mathcal{A}_{\mathbb{R}}}$，那么 $|f| \in \overline{\mathcal{A}_{\mathbb{R}}}$。

1. 设 $f \in \overline{\mathcal{A}_{\mathbb{R}}}$，令 $M = \|f\|$。
2. 考虑实函数 $\phi(t) = |t|$，它在区间 $[-M, M]$ 上连续。
3. **调用 Weierstrass 逼近定理**：对于任意 $\epsilon > 0$，存在一个多项式 $P(t) = \sum_{k=0}^n c_k t^k$ 使得在 $[-M, M]$ 上 $|P(t) - |t|| < \epsilon$。
4. 由于 $\overline{\mathcal{A}_{\mathbb{R}}}$ 是一个代数且包含常数，因此 $P(f) = \sum c_k f^k$ 仍然属于 $\overline{\mathcal{A}_{\mathbb{R}}}$。
5. 这意味着我们可以用 $\overline{\mathcal{A}_{\mathbb{R}}}$ 中的元素一致逼近 $|f|$。由于 $\overline{\mathcal{A}_{\mathbb{R}}}$ 是闭的，故 $|f| \in \overline{\mathcal{A}_{\mathbb{R}}}$。

### 格（Lattice）性质与局部线性逼近

有了绝对值，我们就可以构造“最大值”和“最小值”函数：

$$\max(f, g) = \frac{f+g+|f-g|}{2}, \quad \min(f, g) = \frac{f+g-|f-g|}{2}$$

这说明 $\overline{\mathcal{A}_{\mathbb{R}}}$ 对 $\max$ 和 $\min$ 运算封闭。

#### 局部两点插值

对于任意 $x_1, x_2 \in K$ 及任意实数 $a, b$，由于 $\mathcal{A}_{\mathbb{R}}$ 分离点且含常数，我们可以构造 $h \in \mathcal{A}_{\mathbb{R}}$ 使得 $h(x_1) = a$ 且 $h(x_2) = b$。

> **构造法**：取 $g \in \mathcal{A}_{\mathbb{R}}$ 使得 $g(x_1) \neq g(x_2)$，令 $h(x) = a \frac{g(x)-g(x_2)}{g(x_1)-g(x_2)} + b \frac{g(x)-g(x_1)}{g(x_2)-g(x_1)}$。

#### 从点到全局的逼近

设 $f \in \mathscr{C}(K, \mathbb{R})$ 及 $\epsilon > 0$：

- **固定 $x$，逼近 $y$**：对于每个 $x \in K$，对每一个 $y \in K$，存在 $h_{x,y} \in \mathcal{A}_{\mathbb{R}}$ 使得 $h_{x,y}(x) = f(x)$ 且 $h_{x,y}(y) = f(y)$。
- 由于连续性，存在 $y$ 的邻域 $U_y$ 使得在 $U_y$ 内 $h_{x,y}(z) > f(z) - \epsilon$。
- 利用 $K$ 的**紧致性**，有限个这样的 $h_{x,y}$ 的 $\max$（记作 $H_x$）满足：$H_x(x) = f(x)$ 且对所有 $z \in K$ 有 $H_x(z) > f(z) - \epsilon$。
- 同理，对 $H_x$ 在 $x$ 附近取 $\min$。存在 $x$ 的邻域 $V_x$ 使得在 $V_x$ 内 $H_x(z) < f(z) + \epsilon$。
- 再次利用紧致性，有限个 $H_x$ 的 $\min$（记作 $H$）将满足：对所有 $z \in K$，

$$f(z) - \epsilon < H(z) < f(z) + \epsilon$$

### 总结

由于 $H$ 是通过有限次 $\max$ 和 $\min$ 运算得到的，且每次运算的对象都在 $\overline{\mathcal{A}_{\mathbb{R}}}$ 中，因此 $H \in \overline{\mathcal{A}_{\mathbb{R}}}$。

Q.E.D.

## 复值 Stone–Weierstrass 定理

**定理 (Stone–Weierstrass, 复值版本)**：
设 $K$ 是一个紧致 Hausdorff 空间，且 $\mathcal{A} \subset \mathscr{C}(K, \mathbb{C})$ 是一个代数。
如果 $\mathcal{A}$ 满足以下条件：

1.  **分离点**：对于任意 $x \neq y \in K$，存在 $f \in \mathcal{A}$ 使得 $f(x) \neq f(y)$。
2.  **包含常数函数**：$1 \in \mathcal{A}$（即常函数1属于 $\mathcal{A}$）。
3.  **复共轭封闭**：若 $f \in \mathcal{A}$，则 $\overline{f} \in \mathcal{A}$。

那么 $\mathcal{A}$ 在 $\mathscr{C}(K, \mathbb{C})$ 中 **一致稠密**，即 $\overline{\mathcal{A}} = \mathscr{C}(K, \mathbb{C})$。

### 构造实代数部分

设 $\mathcal{A}_{\mathbb{R}}$ 是 $\mathcal{A}$ 中所有**实值函数**构成的集合：

$$\mathcal{A}_{\mathbb{R}} = \{ f \in \mathcal{A} \mid f(x) \in \mathbb{R}, \forall x \in K \}$$

我们需要证明 $\mathcal{A}_{\mathbb{R}}$ 满足实值 Stone–Weierstrass 定理的所有条件：

- **是一个代数**：
  由于 $\mathcal{A}$ 是 $\mathbb{C}$ 上的代数，且两个实值函数的加法、实标量乘法、乘法结果仍为实值函数，故 $\mathcal{A}_{\mathbb{R}}$ 是 $\mathbb{R}$ 上的代数。
- **包含常数函数**：
  已知 $1 \in \mathcal{A}$。由于 $1$ 是实值的，故 $1 \in \mathcal{A}_{\mathbb{R}}$。
- **分离点**：
  这是最关键的一步。对于任意 $x, y \in K$ 且 $x \neq y$，由已知条件存在 $f \in \mathcal{A}$ 使得 $f(x) \neq f(y)$。
  令 $f = u + iv$，其中 $u, v$ 分别是 $f$ 的实部和虚部：

$$u = \frac{f + \overline{f}}{2}, \quad v = \frac{f - \overline{f}}{2i}$$

由于 $\mathcal{A}$ 对**复共轭封闭**（$\overline{f} \in \mathcal{A}$）且对标量乘法封闭，所以 $u \in \mathcal{A}$ 且 $v \in \mathcal{A}$。又因为 $u, v$ 显然是实值的，故 **$u, v \in \mathcal{A}_{\mathbb{R}}$**。
因为 $f(x) \neq f(y)$，则必须有 $u(x) \neq u(y)$ 或 $v(x) \neq v(y)$。
这说明实代数 $\mathcal{A}_{\mathbb{R}}$ 同样能够分离点。

### 应用实值定理

根据**实值 Stone–Weierstrass 定理**，$\mathcal{A}_{\mathbb{R}}$ 在实连续函数空间 $\mathscr{C}(K, \mathbb{R})$ 中是一致稠密的。
即：

$$\overline{\mathcal{A}_{\mathbb{R}}} = \mathscr{C}(K, \mathbb{R})$$

### 完成复值逼近

现在考虑任意复值连续函数 $g \in \mathscr{C}(K, \mathbb{C})$。
我们可以将其分解为实部和虚部：

$$g(x) = u(x) + i v(x)$$

其中 $u, v \in \mathscr{C}(K, \mathbb{R})$。

对于任意 $\epsilon > 0$：

1. 由于 $\overline{\mathcal{A}_{\mathbb{R}}} = \mathscr{C}(K, \mathbb{R})$，存在 $u_{\mathcal{A}} \in \mathcal{A}_{\mathbb{R}}$ 使得 $\|u - u_{\mathcal{A}}\| < \frac{\epsilon}{2}$。
2. 同理，存在 $v_{\mathcal{A}} \in \mathcal{A}_{\mathbb{R}}$ 使得 $\|v - v_{\mathcal{A}}\| < \frac{\epsilon}{2}$。

构造函数 $g_{\mathcal{A}} = u_{\mathcal{A}} + i v_{\mathcal{A}}$。
由于 $u_{\mathcal{A}}, v_{\mathcal{A}} \in \mathcal{A}_{\mathbb{R}} \subset \mathcal{A}$，且 $\mathcal{A}$ 是 $\mathbb{C}$ 上的代数，故 **$g_{\mathcal{A}} \in \mathcal{A}$**。

计算误差：

$$\|g - g_{\mathcal{A}}\| = \|(u - u_{\mathcal{A}}) + i(v - v_{\mathcal{A}})\| \le \|u - u_{\mathcal{A}}\| + \|v - v_{\mathcal{A}}\| < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$$

这证明了 $\mathcal{A}$ 在 $\mathscr{C}(K, \mathbb{C})$ 中一致稠密。

Q.E.D.
