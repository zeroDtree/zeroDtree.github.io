---
title: Stieltjes积分
---

## 1. 前置

- [[测度论与概率论/三大积分收敛定理]]

## 2. 定义

### 2.1. L-S 积分

设 $F$ 是 $\mathbb{R}^d$ 上的 L-S 函数，$\mu_F$ 是由 $F$ 诱导的 L-S 测度，$g$ 是 Borel 可测函数，若

$$(\text{L-S}) \int_{\mathbb{R}^d} g(\boldsymbol{x}) \mathrm{d} F(\boldsymbol{x}) := \int_{\mathbb{R}^d} g(\boldsymbol{x}) \mathrm{d} \mu_F(\boldsymbol{x})$$

存在，则称之为 $g$ 关于 $F$ 的 Lebesgue-Stieltjes 积分，简称 **L-S 积分**。

- 若取 $F(\boldsymbol{x}) = x_1 x_2 \cdots x_d$，则 $\mu_F = \lambda$ 为 $\mathcal{B}(\mathbb{R}^d)$ 上的 L 测度，

$$(\text{L}) \int_{\mathbb{R}^d} g(\boldsymbol{x}) \mathrm{d} \boldsymbol{x} := \int_{\mathbb{R}^d} g(\boldsymbol{x}) \mathrm{d} \lambda(\boldsymbol{x})$$

就是 $g$ 的狭义 L 积分。

- 当 $d=1, a, b \in \mathbb{R}, a < b$ 时，通常将 $(\text{L-S}) \displaystyle \int_{(a, b]} g(x) \mathrm{d} \mu_F(x)$ 写成 $\displaystyle \int_a^b g(x) \mathrm{d} F(x)$。
- 当 $d=1, a, b \in \mathbb{R}, a < b$ 时，通常将 $(\text{L}) \displaystyle \int_{(a, b]} g(x) \mathrm{d} x$ 写成 $\displaystyle \int_a^b g(x) \mathrm{d} x$。因为单点集的 L 测度为 0，所以还可以把 $\displaystyle \int_a^b g(x) \mathrm{d} x$ 理解为 $\displaystyle \int_{[a, b]} g(x) \mathrm{d} x, \int_{[a, b)} g(x) \mathrm{d} x$ 或 $\displaystyle \int_{(a, b)} g(x) \mathrm{d} x$。

### 2.2. R-S 积分

本段恒设 $g:(\mathbf{a}, \mathbf{b}] \to \mathbb{R}$ 为有界函数，$F:(\mathbf{a}, \mathbf{b}] \to \mathbb{R}$为Lebesgue-Stieltjes函数（L-S函数）。

- 矩形：$(\mathbf{a},\mathbf{b}], a_i \leq b_i$
- 分割：称$$\mathbb{P}=\{J |,J \subseteq I\, \text{and } J \text{ is a rectangle}\}$$为$I$的分割，若$\biguplus_{J \in \mathbb{P}} J = I$,且 $\mathbb{P}$ 是有限集。
- $m_J(g):=\inf_{x \in J} g(x)$
- $M_J(g):=\sup_{x \in J} g(x)$
- Riemann-Stieltjes 下和: $l(g, F, \mathbb{P}):=\sum_{J \in \mathbb{P}} m_J(g) \Delta F(J)$
- Riemann-Stieltjes 上和: $u(g, F, \mathbb{P}):=\sum_{J \in \mathbb{P}} M_J(g) \Delta F(J)$
- 分割的加细：若对于 $\mathbb{P}_2$ 中的每一个矩形 $J' \in \mathbb{P}_2$，都存在 $\mathbb{P}_1$ 中的一个矩形 $J \in \mathbb{P}_1$，使得 $J' \subseteq J$，则称 $\mathbb{P}_2$ 是 $\mathbb{P}_1$ 的一个加细。

总可以构造两个分割的公共加细，$\mathbb{P} = \{J_1 \cap J_2 \mid J_1 \in \mathbb{P}_1, J_2 \in \mathbb{P}_2\}$。

**引理**
(i) $l(g, F; \mathbb{P}) \leqslant u(g, F; \mathbb{P})$;
(ii) 设 $\mathbb{P}_1$ 和 $\mathbb{P}_2$ 都是 $(\mathbf{a}, \mathbf{b}]$ 的分割, 若 $\mathbb{P}_2$ 是 $\mathbb{P}_1$ 的一个**加细**, 则
$$l(g, F, \mathbb{P}_1) \leqslant l(g, F, \mathbb{P}_2), \quad u(g, F, \mathbb{P}_1) \geqslant u(g, F, \mathbb{P}_2);$$
(iii) 对 $(\mathbf{a}, \mathbf{b}]$ 的任何两个分割 $\mathbb{P}_1$ 和 $\mathbb{P}_2$, 总有 $l(g, F, \mathbb{P}_1) \leqslant u(g, F, \mathbb{P}_2)$.

- 分别称
  $$\underline{\int_\mathbf{a}^\mathbf{b}} g(x) \mathrm{d} F(x) = \sup \{ l(g, F, \mathbb{P}) : \mathbb{P} \in \mathcal{P} \},$$

  $$\overline{\int_\mathbf{a}^\mathbf{b}} g(x) \mathrm{d} F(x) = \inf \{ u(g, F, \mathbb{P}) : \mathbb{P} \in \mathcal{P} \}$$

  为 $g$ 在 $(\mathbf{a}, \mathbf{b}]$ 上关于 $F$ 的 Riemann-Stieltjes 下积分与 Riemann-Stieltjes 上积分.

  显然, $\underline{\int_\mathbf{a}^\mathbf{b}} g(x) \mathrm{d} F(x) \leqslant \overline{\int_\mathbf{a}^\mathbf{b}} g(x) \mathrm{d} F(x)$,

- 若进一步有
  $$\underline{\int_\mathbf{a}^\mathbf{b}} g(x) \mathrm{d} F(x) = \overline{\int_\mathbf{a}^\mathbf{b}} g(x) \mathrm{d} F(x),$$
  则称 $g$ 在 $(\mathbf{a}, \mathbf{b}]$ 上关于 $F$ Riemann-Stieltjes 可积，简称 **R-S 可积**，并称此共同值为 $g$ 在 $(\mathbf{a}, \mathbf{b}]$ 上关于 $F$ 的 **R-S 积分**，记为 $(\text{R-S}) \int_\mathbf{a}^\mathbf{b} g(x) \mathrm{d} F(x)$, 其中 $g$ 称为**被积函数** (integrand), $F$ 称为**积分函数** (integrator).

## 反常R-积分

### 7.4.3 反常 R-S 积分

当 $g$ 在 $\mathbb{R}^d$ 上 L 可积时,

$$(\mathrm{L}) \int_{\mathbb{R}^d} g(x) \mathrm{d} x = \lim_{\mathbf{a} \to -\infty, \mathbf{b} \to \infty} (\mathrm{L}) \int_{(\mathbf{a}, \mathbf{b}]} g(x) \mathrm{d} x,$$

但需要注意的是, 上式成立的根据是控制收敛定理.

与 L 积分不同的是, $\mathbb{R}^d$ 上的 R 积分不能用分割的方法来定义

下面定义**反常 R-S 积分**.

设 $g$ 是定义在 $\mathbb{R}^d$ 上的实值函数, 若对任意的 $(\mathbf{a}, \mathbf{b}] \subset \mathbb{R}^d$, (R-S) $\int_{(\mathbf{a}, \mathbf{b}]} g(x) \mathrm{d} F(x)$ 都存在, 且

$$\lim_{\mathbf{a} \to -\infty, \mathbf{b} \to \infty} (\text{R-S}) \int_{(\mathbf{a}, \mathbf{b}]} g(x) \mathrm{d} F(x)$$

存在, 则称此极限为 $g$ 在 $\mathbb{R}^d$ 上关于 $F$ 的 R-S 积分, 记作 (R-S) $\int_{-\infty}^{\infty} g(x) \mathrm{d} F(x)$.

若此积分为一实数, 则进一步称 $g$ 在 $\mathbb{R}^d$ 上关于 $F$ R-S 可积.

## 3. 性质

1. 设 r.v. $X \sim F(x)$, 则对任意的 Borel 可测函数 $g$, 若 $g(X)$ 可积, 则 $$\mathrm{E}g(X) = (\text{L-S}) \int_{-\infty}^{\infty} g(x) \mathrm{d}F(x).$$
2. 设 $g, h : (\mathbf{a}, \mathbf{b}] \to \mathbb{R}$ 都是有界函数，且在 $(\mathbf{a}, \mathbf{b}]$ 上关于 $F$ 都 R-S 可积，则

   (i) (齐性) 对任意的 $c \in \mathbb{R}$, $cg$ 在 $(\mathbf{a}, \mathbf{b}]$ 上关于 $F$ 也 R-S 可积，且

   $$(\text{R-S}) \int_a^b cg(x) \mathrm{d} F(x) = c (\text{R-S}) \int_a^b g(x) \mathrm{d} F(x);$$

   (ii) (关于被积函数具有可加性) $g + h$ 在 $(\mathbf{a}, \mathbf{b}]$ 上关于 $F$ 也 R-S 可积，且

   $$(\text{R-S}) \int_a^b [g(x) + h(x)] \mathrm{d} F(x) = (\text{R-S}) \int_a^b g(x) \mathrm{d} F(x) + (\text{R-S}) \int_a^b h(x) \mathrm{d} F(x);$$

   (iii) (单调性) $g \leqslant h \Rightarrow (\text{R-S}) \int_a^b g(x) \mathrm{d} F(x) \leqslant (\text{R-S}) \int_a^b h(x) \mathrm{d} F(x).$

3. (关于积分区间具有可加性) 设$\mathbf{a}, \mathbf{b},\mathbf{c} \in \mathbb{R}^1$，设 $\mathbf{c} \in (\mathbf{a}, \mathbf{b}), g$ 在 $(\mathbf{a}, \mathbf{c}]$ 及 $(\mathbf{c}, \mathbf{b}]$ 上都关于 $F$ R-S 可积, 则 $g$ 在 $(\mathbf{a}, \mathbf{b}]$ 上关于 $F$ 也 R-S 可积, 且
   $$(\text{R-S}) \int_\mathbf{a}^\mathbf{b} g(x) \mathrm{d} F(x) = (\text{R-S}) \int_\mathbf{a}^\mathbf{c} g(x) \mathrm{d} F(x) + (\text{R-S}) \int_\mathbf{c}^\mathbf{b} g(x) \mathrm{d} F(x) .$$
4. 多维 R-S 积分的可加性: 区域剖分设超矩形 $I = (\mathbf{a}, \mathbf{b}] = \prod_{i=1}^d (a_i, b_i]$ 被一个垂直于第 $k$ 个坐标轴的超平面 $x_k = c_k$（其中 $a_k < c_k < b_k$）划分为两个互不相交的超矩形 $I_1$ 和 $I_2$：$I_1 = (a_1, b_1] \times \dots \times (a_k, c_k] \times \dots \times (a_d, b_d]$,$I_2 = (a_1, b_1] \times \dots \times (c_k, b_k] \times \dots \times (a_d, b_d]$，此时显然有 $I = I_1 \cup I_2$ 且 $I_1 \cap I_2 = \emptyset$。$g$ 是定义在 $I$ 上的有界函数。若 $g$ 在 $I_1$ 和 $I_2$ 上关于 $F$ 均 R-S 可积，则 $g$ 在 $I$ 上也关于 $F$ R-S 可积，且：$$\int_{I} g(\mathbf{x}) \mathrm{d} F(\mathbf{x}) = \int_{I_1} g(\mathbf{x}) \mathrm{d} F(\mathbf{x}) + \int_{I_2} g(\mathbf{x}) \mathrm{d} F(\mathbf{x})$$
5. $g$ 在 $(\mathbf{a},\mathbf{b}]$ 上关于 $F$ R-S 可积当且仅当 $\forall\varepsilon > 0$, 存在 $(\mathbf{a},\mathbf{b}]$ 的一个分割 $\mathbb{P}$, 使得
   $$u(g, F, \mathbb{P}) - l(g, F, \mathbb{P}) < \varepsilon.$$
6. 若 $g$ 在 $(a, b]$ 上连续，$F$ 在 $(a, b]$ 上单调不减，则 $g$ 在 $(a, b]$ 关于 $F$ R-S 可积。
7. 若 $g$ 在 $(a, b]$ 上单调，$F$ 在 $(a, b]$ 上单调不减且连续，则 $g$ 在 $(a, b]$ 关于 $F$ R-S 可积。
8. $g$ 在 $(\mathbf{a},\mathbf{b}]$ 上 R 可积当且仅当 $g$ 关于 L 测度 $\lambda$ 几乎处处连续。(不连续点为零测集)
9. 若 $g$ 在 $(a, b]$ 上单调有界，则 $g$ 在 $(a, b]$ 上 R 可积。
10. 若 $g$ 在 $(a, b]$ 上有界，且不连续点的个数至多可数，则 $g$ 在 $(a, b]$ 上 R 可积。
11. 若 $g$ 在 $(\mathbf{a}, \mathbf{b}]$ 上 R 可积，则
    (i) $g$ 在 $(\mathbf{a}, \mathbf{b}]$ 上 L 可积；
    (ii) (L) $\int_{\mathbf{a}}^{\mathbf{b}} g(x) \text{d}x = \text{(R)} \int_{\mathbf{a}}^{\mathbf{b}} g(x) \text{d}x$.
12. L可积不一定R可积分，考虑狄利克雷函数。
13. 设 $F$ 是 $\mathbb{R}$ 上的 L-S 函数，若 $g$ 在 $(\mathbf{a}, \mathbf{b}]$ 上关于 $F$ R-S 可积，则
    (i) $g$ 在 $(\mathbf{a}, \mathbf{b}]$ 上关于 $F$ L-S 可积；
    (ii) (L-S) $\int_{\mathbf{a}}^{\mathbf{b}} g(x) \text{d}F(x) = \text{(R-S)} \int_{\mathbf{a}}^{\mathbf{b}} g(x) \text{d}F(x)$.
14. 设连续函数 $g$ 在 $\mathbb{R}^d$ 上关于 $F$ L-S 可积，则 $g$ 在 $\mathbb{R}^d$ 上关于 $F$ R-S 可积，且
    $$(\text{L-S}) \int_{-\infty}^{\infty} g(x) \mathrm{d}F(x) = (\text{R-S}) \int_{-\infty}^{\infty} g(x) \mathrm{d}F(x).$$
