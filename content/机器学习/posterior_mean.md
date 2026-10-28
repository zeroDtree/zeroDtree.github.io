---
title: posterior mean
tags:
  - 概率
  - 扩散模型
---

## 1. Tweedie 公式

设 $p(\mathbf{y}\mid\boldsymbol{\eta})$ 属于指数族分布

$$
p(\mathbf{y}\mid\boldsymbol{\eta})
=p_0(\mathbf{y})\exp\!\bigl(\boldsymbol{\eta}^\top T(\mathbf{y})-\varphi(\boldsymbol{\eta})\bigr),
\tag{1}
$$

其中 $\boldsymbol{\eta}$ 是指数族的经典参数向量，$T(\mathbf{y})$ 是 $\mathbf{y}$ 的某个（充分统计量）函数，$\varphi(\boldsymbol{\eta})$ 是使密度归一化的累积量生成函数，$p_0(\mathbf{y})$ 是 $\boldsymbol{\eta}=\mathbf{0}$ 时的密度（相差一个常数比例因子）。Tweedie 公式 [@chung2022diffusion] 指出，后验均值 $\hat{\boldsymbol{\eta}}:=\mathbb{E}[\boldsymbol{\eta}\mid\mathbf{y}]$ 满足

$$
(\nabla_{\mathbf{y}}T(\mathbf{y}))^\top\hat{\boldsymbol{\eta}}
=\nabla_{\mathbf{y}}\log p(\mathbf{y})-\nabla_{\mathbf{y}}\log p_0(\mathbf{y}).
\tag{2}
$$

## 2. 线性高斯扩散中的后验均值

### 2.1. 1 前向过程与结论

考虑一般的线性高斯前向扩散过程

$$
\mathbf{x}_t=a_t\mathbf{x}_0+b_t\boldsymbol{\epsilon},
\qquad
\boldsymbol{\epsilon}\sim\mathcal{N}(\mathbf{0},\mathbf{I}),
\tag{3}
$$

其中 $a_t,b_t\in\mathbb{R}$ 是时间 $t$ 的确定性函数，且通常满足 $a_t>0$、$b_t>0$。相应的前向转移密度为

$$
p(\mathbf{x}_t\mid\mathbf{x}_0)
=\mathcal{N}(\mathbf{x}_t;a_t\mathbf{x}_0,b_t^2\mathbf{I}).
\tag{4}
$$

把该密度写成指数族形式后应用 Tweedie 公式 (2)，即可得到后验均值的显式表达

$$
\mathbb{E}[\mathbf{x}_0\mid\mathbf{x}_t]
=\frac{b_t^2}{a_t}\nabla_{\mathbf{x}_t}\log p_t(\mathbf{x}_t)
+\frac1{a_t}\mathbf{x}_t.
\tag{5}
$$

### 2.2. 2 推导

由 (4)，转移密度为

$$
p(\mathbf{x}_t\mid\mathbf{x}_0)
=\frac1{(2\pi b_t^2)^{d/2}}
\exp\!\left(-\frac{\|\mathbf{x}_t-a_t\mathbf{x}_0\|^2}{2b_t^2}\right).
$$

展开指数项：

$$
\begin{aligned}
-\frac{\|\mathbf{x}_t-a_t\mathbf{x}_0\|^2}{2b_t^2}
&=-\frac{\mathbf{x}_t^\top\mathbf{x}_t-2a_t\mathbf{x}_t^\top\mathbf{x}_0+a_t^2\mathbf{x}_0^\top\mathbf{x}_0}{2b_t^2}\\
&=-\frac{\|\mathbf{x}_t\|^2}{2b_t^2}
+\frac{a_t}{b_t^2}\mathbf{x}_t^\top\mathbf{x}_0
-\frac{a_t^2\|\mathbf{x}_0\|^2}{2b_t^2}.
\end{aligned}
$$

因此转移密度可写成指数族的标准形式

$$
p(\mathbf{x}_t\mid\mathbf{x}_0)
=p_0(\mathbf{x}_t)\exp\!\bigl(\mathbf{x}_0^\top T(\mathbf{x}_t)-\varphi(\mathbf{x}_0)\bigr),
$$

其中各项定义为

$$
p_0(\mathbf{x}_t):=\frac1{(2\pi b_t^2)^{d/2}}\exp\!\left(-\frac{\|\mathbf{x}_t\|^2}{2b_t^2}\right),
\quad
T(\mathbf{x}_t):=\frac{a_t}{b_t^2}\mathbf{x}_t,
\quad
\varphi(\mathbf{x}_0):=\frac{a_t^2\|\mathbf{x}_0\|^2}{2b_t^2}.
$$

于是后验均值 $\hat{\mathbf{x}}_0:=\mathbb{E}[\mathbf{x}_0\mid\mathbf{x}_t]$ 满足 Tweedie 公式 (2)：

$$
(\nabla_{\mathbf{x}_t}T(\mathbf{x}_t))^\top\hat{\mathbf{x}}_0
=\nabla_{\mathbf{x}_t}\log p_t(\mathbf{x}_t)-\nabla_{\mathbf{x}_t}\log p_0(\mathbf{x}_t).
$$

计算充分统计量的梯度：

$$
\nabla_{\mathbf{x}_t}T(\mathbf{x}_t)
=\nabla_{\mathbf{x}_t}\left(\frac{a_t}{b_t^2}\mathbf{x}_t\right)
=\frac{a_t}{b_t^2}\mathbf{I}.
$$

计算基准密度的对数梯度：

$$
\nabla_{\mathbf{x}_t}\log p_0(\mathbf{x}_t)
=\nabla_{\mathbf{x}_t}\left(-\frac{\|\mathbf{x}_t\|^2}{2b_t^2}\right)
=-\frac{\mathbf{x}_t}{b_t^2}.
$$

代入 Tweedie 公式：

$$
\frac{a_t}{b_t^2}\hat{\mathbf{x}}_0
=\nabla_{\mathbf{x}_t}\log p_t(\mathbf{x}_t)+\frac{\mathbf{x}_t}{b_t^2}.
$$

两边同乘 $b_t^2/a_t$，即得后验均值的显式表达 (5)：

$$
\hat{\mathbf{x}}_0
=\frac{b_t^2}{a_t}\nabla_{\mathbf{x}_t}\log p_t(\mathbf{x}_t)
+\frac1{a_t}\mathbf{x}_t.
$$

### 2.3. 3 特殊情况

公式 (5) 涵盖了扩散模型中的多种重要特殊情况。

**DDPM / VP-SDE**：取 $a_t=\sqrt{\bar{\alpha}_t}$、$b_t=\sqrt{1-\bar{\alpha}_t}$，其中 $\bar{\alpha}_t=\prod_{s=1}^{t}\alpha_s$。代入 (5) 得

$$
\begin{aligned}
\mathbb{E}[\mathbf{x}_0\mid\mathbf{x}_t]
&=\frac{1-\bar{\alpha}_t}{\sqrt{\bar{\alpha}_t}}
\nabla_{\mathbf{x}_t}\log p_t(\mathbf{x}_t)
+\frac1{\sqrt{\bar{\alpha}_t}}\mathbf{x}_t\\
&=\frac1{\sqrt{\bar{\alpha}_t}}
\Bigl(\mathbf{x}_t+(1-\bar{\alpha}_t)\nabla_{\mathbf{x}_t}\log p_t(\mathbf{x}_t)\Bigr),
\end{aligned}
$$

这正是 DDPM 中经典的后验均值公式。

**VE-SDE**：取 $a_t=1$、$b_t=\sigma_t$，其中 $\sigma_t$ 是噪声标准差，此时

$$
\mathbb{E}[\mathbf{x}_0\mid\mathbf{x}_t]
=\sigma_t^2\nabla_{\mathbf{x}_t}\log p_t(\mathbf{x}_t)+\mathbf{x}_t.
$$

## 3. 理论意义与实际应用

Tweedie 公式在线性高斯扩散中的应用具有重要的理论和实践价值：

1. **统一理论框架**：为不同类型的扩散模型提供统一的数学基础。
2. **条件生成**：在 loss guidance 等方法中，用 $\mathbb{E}[\mathbf{x}_0\mid\mathbf{x}_t]$ 估计无噪声数据。
3. **采样算法**：许多确定性采样器（如 DDIM [@song2020denoising]）都依赖后验均值的准确估计。
4. **模型分析**：有助于理解不同扩散过程的内在联系与差异。

该公式建立了分数函数 $\nabla_{\mathbf{x}_t}\log p_t(\mathbf{x}_t)$ 与后验均值 $\mathbb{E}[\mathbf{x}_0\mid\mathbf{x}_t]$ 之间的直接联系，为扩散模型的理论分析和实际应用提供了坚实的数学基础。
