---
title: 复值可测函数的L积分
---

## 前置

- [[测度论与概率论/Lebesgue-integral]]

## 复值可测函数 $L$ 积分的性质

若 $\mathbf{f}, \mathbf{g}$ 为 $\Omega$ 上的复值可测可积函数，$\alpha = a + ib \in \mathbb{C}$ 为复常数，则其积分满足以下性质：

1. **线性性（Linearity）**：

$$\int (\mathbf{f} + \mathbf{g}) d\mu = \int \mathbf{f} d\mu + \int \mathbf{g} d\mu$$

2. **复齐次性（Complex Homogeneity）**：

$$\int \alpha \mathbf{f} d\mu = \alpha \int \mathbf{f} d\mu \quad (\forall \alpha \in \mathbb{C})$$

3. **几乎处处相等性（a.e. Equality）**：
   若 $\mathbf{f} = \mathbf{g} \quad \text{a.e.}$，则 $\int \mathbf{f} d\mu = \int \mathbf{g} d\mu$。
4. **模长三角不等式（Triangle Inequality for Integrals）**：

$$\left| \int \mathbf{f} d\mu \right| \le \int |\mathbf{f}| d\mu$$

5. **共轭不变性（Conjugate Invariance）**：

$$\int \overline{\mathbf{f}} d\mu = \overline{\int \mathbf{f} d\mu}$$

---

## 证明

### 线性性

**欲证**：$\int (\mathbf{f} + \mathbf{g}) d\mu = \int \mathbf{f} d\mu + \int \mathbf{g} d\mu$

**证明**：
设 $\mathbf{f} = u_1 + iv_1$ 且 $\mathbf{g} = u_2 + iv_2$。则有：

$$\mathbf{f} + \mathbf{g} = (u_1 + u_2) + i(v_1 + v_2)$$

根据复值积分的定义，将实部与虚部展开：

$$\int (\mathbf{f} + \mathbf{g}) d\mu = \int (u_1 + u_2) d\mu + i \int (v_1 + v_2) d\mu$$

利用实值 $L$ 积分的线性性质（性质 11 中的可加性），上式可拆分为：

$$
\begin{aligned}
\int (\mathbf{f} + \mathbf{g}) d\mu &= \left( \int u_1 d\mu + \int u_2 d\mu \right) + i \left( \int v_1 d\mu + \int v_2 d\mu \right) \
&= \left( \int u_1 d\mu + i \int v_1 d\mu \right) + \left( \int u_2 d\mu + i \int v_2 d\mu \right) \
&= \int \mathbf{f} d\mu + \int \mathbf{g} d\mu
\end{aligned}
$$

证毕。

### 复齐次性

**欲证**：$\int \alpha \mathbf{f} d\mu = \alpha \int \mathbf{f} d\mu \quad (\alpha = a+ib \in \mathbb{C})$

**证明**：
设 $\mathbf{f} = u + iv$，直接展开复数乘法 $\alpha \mathbf{f}$：

$$\alpha \mathbf{f} = (a+ib)(u+iv) = (au - bv) + i(bu + av)$$

根据复值积分定义：

$$\int \alpha \mathbf{f} d\mu = \int (au - bv) d\mu + i \int (bu + av) d\mu$$

利用实值 $L$ 积分的齐次性与线性性拆开积分：

$$\int \alpha \mathbf{f} d\mu = \left( a\int u d\mu - b\int v d\mu \right) + i \left( b\int u d\mu + a\int v d\mu \right)$$

对右侧进行代数重组，提取公因式 $a$ 和 $ib$：

$$
\begin{aligned}
&= a\left( \int u d\mu + i\int v d\mu \right) + ib\left( \int u d\mu + i\int v d\mu \right) \
&= (a + ib) \left( \int u d\mu + i\int v d\mu \right) \
&= \alpha \int \mathbf{f} d\mu
\end{aligned}
$$

证毕。

### 共轭不变性

**欲证**：$\int \overline{\mathbf{f}} d\mu = \overline{\int \mathbf{f} d\mu}$

**证明**：
设 $\mathbf{f} = u + iv$，则 $\overline{\mathbf{f}} = u - iv$。根据定义：

$$\int \overline{\mathbf{f}} d\mu = \int u d\mu + i \int (-v) d\mu$$

利用实值积分的齐次性把 $-1$ 提出来：

$$\int \overline{\mathbf{f}} d\mu = \int u d\mu - i \int v d\mu = \overline{\int u d\mu + i \int v d\mu} = \overline{\int \mathbf{f} d\mu}$$

证毕。

### 几乎处处相等性

**欲证**：若 $\mathbf{f} = \mathbf{g} \quad \text{a.e.}$，则 $\int \mathbf{f} d\mu = \int \mathbf{g} d\mu$

**证明**：
因为 $\mathbf{f} = \mathbf{g} \quad \text{a.e.}$，这意味着：

$$\text{Re}\,\mathbf{f} = \text{Re}\,\mathbf{g} \quad \text{a.e.} \quad \text{且} \quad \text{Im}\,\mathbf{f} = \text{Im}\,\mathbf{g} \quad \text{a.e.}$$

因此

$$\int \text{Re}\,\mathbf{f} d\mu = \int \text{Re}\,\mathbf{g} d\mu \quad \text{且} \quad \int \text{Im}\,\mathbf{f} d\mu = \int \text{Im}\,\mathbf{g} d\mu$$

代入复值积分定义式，两积分必然相等。
证毕。

### 模长三角不等式

<!-- #! TODO (待证：e的定义与性质) -->

**欲证**：$\left| \int \mathbf{f} d\mu \right| \le \int |\mathbf{f}| d\mu$

**证明**：
设复数积分值 $z = \int \mathbf{f} d\mu \in \mathbb{C}$。

- 若 $z = 0$，则左式 $|0| = 0$。由于 $|\mathbf{f}| \ge 0$，其积分非负，不等式 $0 \le \int |\mathbf{f}| d\mu$ 显然成立。
- 若 $z \neq 0$，我们可以将 $z$ 写为极坐标形式：$z = |z|e^{i\theta}$，其中 $\theta \in [0, 2\pi)$。

由此可得：

$$|z| = z \cdot e^{-i\theta} = e^{-i\theta} \int \mathbf{f} d\mu$$

利用上面刚刚证明的复齐次性，将复常数 $e^{-i\theta}$ 移入积分号内部：

$$|z| = \int \left( e^{-i\theta} \mathbf{f} \right) d\mu$$

注意：因为 $|z|$ 是一个**纯实数**，所以它的值必然等于它自身的实部。因此：

$$|z| = \text{Re} \left( \int e^{-i\theta} \mathbf{f} d\mu \right)$$

根据复值积分定义，积分的实部等于实部的积分：

$$|z| = \int \text{Re} \left( e^{-i\theta} \mathbf{f} \right) d\mu$$

对任何复数 $w$，显然有 $\text{Re}(w) \le |w|$。因此对被积函数有：

$$\text{Re} \left( e^{-i\theta} \mathbf{f} \right) \le \left| e^{-i\theta} \mathbf{f} \right| = \left|e^{-i\theta}\right| \cdot |\mathbf{f}| = 1 \cdot |\mathbf{f}| = |\mathbf{f}|$$

由于上述不等式处处成立，利用实值 $L$ 积分的单调性：

$$|z| = \int \text{Re} \left( e^{-i\theta} \mathbf{f} \right) d\mu \le \int |\mathbf{f}| d\mu$$

将 $z = \int \mathbf{f} d\mu$ 代回，最终得到：

$$\left| \int \mathbf{f} d\mu \right| \le \int |\mathbf{f}| d\mu$$

Q.E.D.
