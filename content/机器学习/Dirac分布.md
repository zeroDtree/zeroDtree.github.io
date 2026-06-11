---
title: Dirac分布
---

## 前置

- [[抽象代数/对偶空间]]

## 定义

### 测试函数空间

设 $C^\infty(\mathbb{R})$ 为所有无限可微函数 $\phi: \mathbb{R} \to \mathbb{F}$ 的集合（通常 $\mathbb{F} = \mathbb{R}$ 或 $\mathbb{C}$）。定义 $\phi$ 的**支撑集**（Support）为

$$
\operatorname{supp}(\phi) := \overline{\{ x \in \mathbb{R} : \phi(x) \neq 0 \}}.
$$

若 $\operatorname{supp}(\phi)$ 为紧集，则称 $\phi$ 具有**紧支撑**（Compact Support）。定义

$$
\mathcal{D}(\mathbb{R}) := C_c^\infty(\mathbb{R}) := \{\phi \in C^\infty(\mathbb{R}) \mid \operatorname{supp}(\phi) \text{ 为紧集}\}.
$$

称 $\mathcal{D}(\mathbb{R})$ 为实轴上的**测试函数空间**（Test Function Space）。

### 测试函数空间的拓扑

为讨论连续线性泛函，需赋予 $\mathcal{D}(\mathbb{R})$ 一个拓扑。称序列 $\phi_n$ **在 $\mathcal{D}$ 中收敛**于 $\phi$，记作 $\phi_n \xrightarrow{\mathcal{D}} \phi$，当且仅当：

1. 存在固定紧集 $K \subset \mathbb{R}$，使得 $\operatorname{supp}(\phi_n) \subset K$ 且 $\operatorname{supp}(\phi) \subset K$；
2. 对任意整数 $m \geq 0$，

$$
\sup_{x \in K} \left| \phi_n^{(m)}(x) - \phi^{(m)}(x) \right| \to 0,
$$

即所有阶导数在 $K$ 上一致收敛。

由此得到 $\mathcal{D}(\mathbb{R})$ 的标准拓扑；赋予该拓扑后，$\mathcal{D}(\mathbb{R})$ 是局部凸拓扑向量空间。

### 分布空间

设 $\mathcal{D}(\mathbb{R})$ 带有上述拓扑。定义其连续对偶空间

$$
\mathcal{D}'(\mathbb{R}) := (\mathcal{D}(\mathbb{R}))' = \{ T : \mathcal{D}(\mathbb{R}) \to \mathbb{F} \mid T \text{ 为连续线性泛函} \}.
$$

称 $\mathcal{D}'(\mathbb{R})$ 为**分布空间**（Space of Distributions），其元素称为**分布**（Distribution）或**广义函数**（Generalized Function）。

### 对偶配对

对 $T \in \mathcal{D}'(\mathbb{R})$，$\phi \in \mathcal{D}(\mathbb{R})$，定义

$$
\langle T, \phi \rangle := T(\phi),
$$

称为分布与测试函数之间的**对偶配对**。

### 常规分布

设 $f \in L^1_{\mathrm{loc}}(\mathbb{R})$。定义映射 $T_f : \mathcal{D}(\mathbb{R}) \to \mathbb{F}$ 为

$$
\langle T_f, \phi \rangle := \int_{-\infty}^{\infty} f(x)\phi(x)\, dx.
$$

容易验证 $T_f$ 是连续线性泛函，故 $T_f \in \mathcal{D}'(\mathbb{R})$。称 $T_f$ 为由函数 $f$ 诱导的**常规分布**（Regular Distribution）。因此有嵌入

$$
L^1_{\mathrm{loc}}(\mathbb{R}) \hookrightarrow \mathcal{D}'(\mathbb{R}),
$$

即局部可积函数可视为特殊的分布。

### Dirac 分布

定义映射 $\delta : \mathcal{D}(\mathbb{R}) \to \mathbb{F}$ 为

$$
\langle \delta, \phi \rangle := \phi(0).
$$

称 $\delta$ 为 **Dirac 分布**（Dirac Distribution）。

#### 线性性

对任意 $a,b \in \mathbb{F}$，$\phi,\psi \in \mathcal{D}(\mathbb{R})$，有

$$
\langle \delta, a\phi + b\psi \rangle = (a\phi + b\psi)(0) = a\phi(0) + b\psi(0),
$$

故 $\delta$ 是线性的。

#### 连续性

设 $\phi_n \xrightarrow{\mathcal{D}} \phi$。由测试函数空间拓扑的定义，$\phi_n$ 在某固定紧集 $K$ 上与其零阶导数一致收敛；若 $0 \in K$，则 $\phi_n(0) \to \phi(0)$，即

$$
\langle \delta, \phi_n \rangle \to \langle \delta, \phi \rangle.
$$

若 $0 \notin K$，则对充分大的 $n$ 有 $\phi_n(0) = \phi(0) = 0$，结论仍成立。故 $\delta$ 连续，从而 $\delta \in \mathcal{D}'(\mathbb{R})$。

### Dirac 分布不是普通函数

不存在 $f \in L^1_{\mathrm{loc}}(\mathbb{R})$，使得对所有 $\phi \in \mathcal{D}(\mathbb{R})$ 有

$$
\langle \delta, \phi \rangle = \int_{-\infty}^{\infty} f(x)\phi(x)\, dx.
$$

因此 $\delta$ 不是由任何普通函数诱导的分布，称为**奇异分布**（Singular Distribution）。
