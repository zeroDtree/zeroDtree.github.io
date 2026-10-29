---
title: Diffusion Posterior Sampling (DPS)
tags:
  - 机器学习
date: 2026-10-29
---

## 前置

- [[机器学习/posterior_mean|posterior mean]]

## 1. 设定

考虑一般的线性高斯前向扩散过程。记 $a_t,b_t>0$ 为时间 $t$ 的确定性系数，

$$
\mathbf{x}_t=a_t\mathbf{x}_0+b_t\boldsymbol{\epsilon},
\qquad
\boldsymbol{\epsilon}\sim\mathcal{N}(\mathbf{0},\mathbf{I}).
\tag{1}
$$

无条件 score 模型给出 $\nabla_{\mathbf{x}_t}\log p_t(\mathbf{x}_t)$。由 [[机器学习/posterior_mean|posterior mean]] 的 (5)，后验均值是

$$
\hat{\mathbf{x}}_0
:=\mathbb{E}[\mathbf{x}_0\mid\mathbf{x}_t]
=\frac{b_t^2}{a_t}\nabla_{\mathbf{x}_t}\log p_t(\mathbf{x}_t)
+\frac1{a_t}\mathbf{x}_t.
\tag{2}
$$

测量模型与文末定理 1 相同：

$$
\mathbf{y}=\mathcal{A}(\mathbf{x}_0)+\mathbf{n},
\qquad
\mathbf{n}\sim\mathcal{N}(\mathbf{0},\sigma^2\mathbf{I}),
\tag{3}
$$

其中 $\mathcal{A}$ 已知。目标是从后验 $p(\mathbf{x}_0\mid\mathbf{y})$ 采样。

扩散核 $p(\mathbf{x}_t\mid\mathbf{x}_0)$ 与测量似然 $p(\mathbf{y}\mid\mathbf{x}_0)$ 都已知。$p(\mathbf{x}_0\mid\mathbf{x}_t)$ 的完整分布未知，因此 $p(\mathbf{y}\mid\mathbf{x}_t)$ 没有闭式。

## 2. 后验 score

Bayes 公式把条件 score 拆成先验 score 与似然 score：

$$
\nabla_{\mathbf{x}_t}\log p_t(\mathbf{x}_t\mid\mathbf{y})
=\nabla_{\mathbf{x}_t}\log p_t(\mathbf{x}_t)
+\nabla_{\mathbf{x}_t}\log p(\mathbf{y}\mid\mathbf{x}_t).
\tag{4}
$$

先验 score 由无条件扩散模型提供。反向过程在每个时刻需要似然 score $\nabla_{\mathbf{x}_t}\log p(\mathbf{y}\mid\mathbf{x}_t)$。测量模型 (3) 直接给出的是干净数据上的 $p(\mathbf{y}\mid\mathbf{x}_0)$。

## 3. 积分与插件近似

在 $\mathbf{y}\perp\mathbf{x}_t\mid\mathbf{x}_0$ 下，

$$
p(\mathbf{y}\mid\mathbf{x}_t)
=\int p(\mathbf{y}\mid\mathbf{x}_0)\,p(\mathbf{x}_0\mid\mathbf{x}_t)\,d\mathbf{x}_0
=\mathbb{E}\bigl[p(\mathbf{y}\mid\mathbf{x}_0)\mid\mathbf{x}_t\bigr].
\tag{5}
$$

积分需要完整的 $p(\mathbf{x}_0\mid\mathbf{x}_t)$。扩散模型通常只给 score，并由 (2) 给出条件均值 $\hat{\mathbf{x}}_0$。DPS 用这个均值做插件近似 [@chung2022diffusion]：

$$
p(\mathbf{y}\mid\mathbf{x}_t)
\approx
p(\mathbf{y}\mid\hat{\mathbf{x}}_0),
\qquad
\hat{\mathbf{x}}_0=\mathbb{E}[\mathbf{x}_0\mid\mathbf{x}_t].
\tag{6}
$$

记 $f(\mathbf{x}_0)=p(\mathbf{y}\mid\mathbf{x}_0)$，则 (5) 是 $\mathbb{E}[f(\mathbf{x}_0)\mid\mathbf{x}_t]$，(6) 是 $f(\mathbb{E}[\mathbf{x}_0\mid\mathbf{x}_t])$。二者一般不相等。文末定理 1 在 Lipschitz 条件下给出这个间隙的上界。

## 4. 似然 score 与采样

对高斯测量 (3)，

$$
\log p(\mathbf{y}\mid\mathbf{x}_0)
=-\frac{\|\mathbf{y}-\mathcal{A}(\mathbf{x}_0)\|^2}{2\sigma^2}+C.
$$

把 $\mathbf{x}_0$ 换成 $\hat{\mathbf{x}}_0(\mathbf{x}_t)$ 后对 $\mathbf{x}_t$ 求导。梯度经过 $\hat{\mathbf{x}}_0$，而 $\hat{\mathbf{x}}_0$ 通过 (2) 依赖 $\mathbf{x}_t$ 与 score：

$$
\nabla_{\mathbf{x}_t}\log p(\mathbf{y}\mid\hat{\mathbf{x}}_0)
=-\frac1{2\sigma^2}
\nabla_{\mathbf{x}_t}\|\mathbf{y}-\mathcal{A}(\hat{\mathbf{x}}_0)\|^2.
\tag{7}
$$

条件反向过程把 (4) 中的似然 score 换成 (7)，并把其中的系数收进步长 $\zeta$。先按无条件反向过程从 $\mathbf{x}_t$ 得到候选 $\mathbf{x}_{t-1}'$，再减去残差范数对当前 $\mathbf{x}_t$ 的梯度 [@chung2022diffusion]：

$$
\mathbf{x}_{t-1}
=\mathbf{x}_{t-1}'
-\zeta\,
\nabla_{\mathbf{x}_t}\|\mathbf{y}-\mathcal{A}(\hat{\mathbf{x}}_0)\|_2.
\tag{8}
$$

## 5. 特例

公式 (2) 在两种常见前向过程中收回熟悉的后验均值，代入方式与 [[机器学习/posterior_mean|posterior mean]] 的 2.3 相同。

**DDPM / VP-SDE**：取 $a_t=\sqrt{\bar{\alpha}_t}$、$b_t=\sqrt{1-\bar{\alpha}_t}$，其中 $\bar{\alpha}_t=\prod_{s=1}^{t}\alpha_s$。代入 (2) 得

$$
\hat{\mathbf{x}}_0
=\frac1{\sqrt{\bar{\alpha}_t}}
\Bigl(\mathbf{x}_t+(1-\bar{\alpha}_t)\nabla_{\mathbf{x}_t}\log p_t(\mathbf{x}_t)\Bigr).
\tag{9}
$$

**VE-SDE**：取 $a_t=1$、$b_t=\sigma_t$，则

$$
\hat{\mathbf{x}}_0
=\mathbf{x}_t+\sigma_t^2\nabla_{\mathbf{x}_t}\log p_t(\mathbf{x}_t).
\tag{10}
$$


## 命题 2（Jensen 间隙上界）

设 $\boldsymbol X\in\mathbb R^n$ 是随机向量，其 $\alpha$ 阶绝对中心矩有限（$\alpha>0$）。记

$$
\boldsymbol\mu=\mathbb E[\boldsymbol X],\qquad
m_\alpha=\left(\mathbb E\|\boldsymbol X-\boldsymbol\mu\|_2^\alpha\right)^{1/\alpha}.
$$

若存在常数 $K>0$，使对任意 $\boldsymbol x\in\mathbb R^n$ 都有

$$
|f(\boldsymbol x)-f(\boldsymbol\mu)|\le K\|\boldsymbol x-\boldsymbol\mu\|_2^\alpha,
$$

则

$$
\left|\mathbb E[f(\boldsymbol X)]-f(\mathbb E[\boldsymbol X])\right|\le K m_\alpha^\alpha.
$$

**证明.** 由期望的线性性与三角不等式，

$$
\left|\mathbb E[f(\boldsymbol X)]-f(\boldsymbol\mu)\right|
=\left|\mathbb E\big[f(\boldsymbol X)-f(\boldsymbol\mu)\big]\right|
\le\mathbb E\big|f(\boldsymbol X)-f(\boldsymbol\mu)\big|
\le K\,\mathbb E\|\boldsymbol X-\boldsymbol\mu\|_2^\alpha
=K m_\alpha^\alpha. \qquad\square
$$

## 引理 2（一维高斯密度是 Lipschitz 的）

设 $\phi:\mathbb R\to\mathbb R$ 是均值为 $\mu$、方差为 $\sigma^2>0$ 的一维高斯密度，则存在有限常数 $L>0$，使对任意 $x,y\in\mathbb R$ 有

$$
|\phi(x)-\phi(y)|\le L|x-y|.
$$

**证明.** 由 $\phi'(x)=-\dfrac{x-\mu}{\sigma^2}\phi(x)$ 知 $\phi'$ 连续，且 $\lim_{x\to\pm\infty}\phi'(x)=0$（指数衰减快于线性增长），故 $\phi'$ 在 $\mathbb R$ 上有界。取 $L=\sup_{x\in\mathbb R}|\phi'(x)|<\infty$，由中值定理，

$$
|\phi(x)-\phi(y)|=|\phi'(\xi)|\,|x-y|\le L|x-y|. \qquad\square
$$

## 引理 3（各向同性多元高斯密度是 Lipschitz 的）

设 $\phi:\mathbb R^d\to\mathbb R$ 是均值为 $\boldsymbol\mu$、协方差为 $\sigma^2\boldsymbol I$ 的高斯密度（$\sigma^2>0$），则存在有限常数 $L>0$，使对任意 $\boldsymbol x,\boldsymbol y\in\mathbb R^d$ 有

$$
|\phi(\boldsymbol x)-\phi(\boldsymbol y)|\le L\|\boldsymbol x-\boldsymbol y\|_2.
$$

**证明.** 梯度为

$$
\nabla\phi(\boldsymbol x)=-\frac{\boldsymbol x-\boldsymbol\mu}{\sigma^2}\phi(\boldsymbol x),
$$

故

$$
\|\nabla\phi(\boldsymbol x)\|_2
=\frac{\|\boldsymbol x-\boldsymbol\mu\|_2}{\sigma^2(2\pi\sigma^2)^{d/2}}
\exp\left(-\frac{\|\boldsymbol x-\boldsymbol\mu\|_2^2}{2\sigma^2}\right)
$$

连续，且在 $\|\boldsymbol x-\boldsymbol\mu\|_2\to\infty$ 时趋于 $0$，从而在 $\mathbb R^d$ 上有界。取 $L=\sup_{\boldsymbol z\in\mathbb R^d}\|\nabla\phi(\boldsymbol z)\|_2<\infty$，沿线段 $\boldsymbol\gamma(s)=\boldsymbol y+s(\boldsymbol x-\boldsymbol y)$（$s\in[0,1]$）积分并用 Cauchy–Schwarz 不等式，

$$
|\phi(\boldsymbol x)-\phi(\boldsymbol y)|
\le\int_0^1\|\nabla\phi(\boldsymbol\gamma(s))\|_2\,\|\boldsymbol x-\boldsymbol y\|_2\,ds
\le L\|\boldsymbol x-\boldsymbol y\|_2. \qquad\square
$$

## 定理 1（DPS 的近似误差上界）

考虑测量模型

$$
\boldsymbol y=\mathcal A(\boldsymbol x_0)+\boldsymbol n,\qquad
\boldsymbol n\sim\mathcal N(\boldsymbol 0,\sigma^2\boldsymbol I_d),
$$

其中 $\mathcal A:\mathbb R^n\to\mathbb R^d$ 连续可微且 Jacobian 有界：

$$
C_{\mathcal A}:=\sup_{\boldsymbol x\in\mathbb R^n}\|J_{\mathcal A}(\boldsymbol x)\|_{\mathrm{op}}<\infty .
$$

令 $\hat{\boldsymbol x}_0=\mathbb E[\boldsymbol x_0\mid\boldsymbol x_t]$，

$$
m_1:=\mathbb E\big[\|\boldsymbol x_0-\hat{\boldsymbol x}_0\|_2\mid\boldsymbol x_t\big],
$$

则存在有限常数 $L>0$，使

$$
\left|p(\boldsymbol y\mid\boldsymbol x_t)-p(\boldsymbol y\mid\hat{\boldsymbol x}_0)\right|\le L C_{\mathcal A}m_1 .
$$

**证明.**

**第一步：把边缘似然写成期望.** 记

$$
h(\boldsymbol z)=\frac{1}{(2\pi\sigma^2)^{d/2}}\exp\left(-\frac{\|\boldsymbol y-\boldsymbol z\|_2^2}{2\sigma^2}\right),
\qquad
f(\boldsymbol x)=h(\mathcal A(\boldsymbol x)),
$$

则 $p(\boldsymbol y\mid\boldsymbol x_0)=f(\boldsymbol x_0)$。由全概率公式，

$$
p(\boldsymbol y\mid\boldsymbol x_t)=\int f(\boldsymbol x_0)\,p(\boldsymbol x_0\mid\boldsymbol x_t)\,d\boldsymbol x_0
=\mathbb E\big[f(\boldsymbol x_0)\mid\boldsymbol x_t\big],
$$

而 $p(\boldsymbol y\mid\hat{\boldsymbol x}_0)=f(\hat{\boldsymbol x}_0)$，故误差为

$$
\mathcal J:=\left|\mathbb E\big[f(\boldsymbol x_0)\mid\boldsymbol x_t\big]-f(\hat{\boldsymbol x}_0)\right|.
$$

**第二步：$h$ 与 $\mathcal A$ 都是 Lipschitz 的.** 对固定的 $\boldsymbol y$，$h$ 是协方差为 $\sigma^2\boldsymbol I_d$ 的高斯密度，由引理 3 存在 $L<\infty$ 使

$$
|h(\boldsymbol z_1)-h(\boldsymbol z_2)|\le L\|\boldsymbol z_1-\boldsymbol z_2\|_2.
$$

另一方面，由 Jacobian 有界以及

$$
\mathcal A(\boldsymbol x)-\mathcal A(\boldsymbol x')
=\int_0^1 J_{\mathcal A}\big(\boldsymbol x'+s(\boldsymbol x-\boldsymbol x')\big)(\boldsymbol x-\boldsymbol x')\,ds
$$

可得 $\|\mathcal A(\boldsymbol x)-\mathcal A(\boldsymbol x')\|_2\le C_{\mathcal A}\|\boldsymbol x-\boldsymbol x'\|_2$，即 $\mathcal A$ 是 $C_{\mathcal A}$-Lipschitz 的。二者复合给出

$$
|f(\boldsymbol x_0)-f(\hat{\boldsymbol x}_0)|\le L C_{\mathcal A}\|\boldsymbol x_0-\hat{\boldsymbol x}_0\|_2 .
$$

**第三步：估计误差.** 对左端取条件期望，用三角不等式即得

$$
\mathcal J
\le\mathbb E\big[|f(\boldsymbol x_0)-f(\hat{\boldsymbol x}_0)|\mid\boldsymbol x_t\big]
\le L C_{\mathcal A}\,\mathbb E\big[\|\boldsymbol x_0-\hat{\boldsymbol x}_0\|_2\mid\boldsymbol x_t\big]
=L C_{\mathcal A}m_1 .
$$

这正是命题 2 在 $\alpha=1$、$K=L C_{\mathcal A}$、$f=h\circ\mathcal A$ 下的特例。$\square$

## 备注

- 全程只要求 Lipschitz 常数存在且有限，不必算出其显式表达式；引理 2、3 只需导数或梯度连续且有界。
- 仅有 $h$ 的 Lipschitz 性推不出 $h\circ\mathcal A$ 的 Lipschitz 性，因此需要对 $\mathcal A$ 加全局 Lipschitz 条件，证明中取的是充分条件 $\sup_{\boldsymbol x}\|J_{\mathcal A}(\boldsymbol x)\|_{\mathrm{op}}<\infty$。若 $\mathcal A$ 线性，则自动成立且 $C_{\mathcal A}=\|\mathcal A\|_{\mathrm{op}}$。
- 为使 $\mathcal J$ 严格成为命题 2 意义下的 Jensen 间隙，需要 $\hat{\boldsymbol x}_0=\mathbb E[\boldsymbol x_0\mid\boldsymbol x_t]$；若它只是普通估计，上界依然成立，但应理解为对该估计的误差控制。

综上，在所列条件下

$$
\mathcal J\le L C_{\mathcal A}m_1,\qquad L<\infty .
$$
