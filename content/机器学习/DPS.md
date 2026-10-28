---
title: DPS 近似误差上界
tags:
  - 机器学习
---

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
