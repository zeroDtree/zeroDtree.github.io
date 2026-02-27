---
title: Gaussian Distribution
---

- [1. One-dimensional Gaussian Distribution](#1-one-dimensional-gaussian-distribution)
- [2. Multi-dimensional Gaussian Distribution](#2-multi-dimensional-gaussian-distribution) - [2.1. 多维高斯分布的概率密度函数(在能写出概率密度的情况下)](#21-多维高斯分布的概率密度函数在能写出概率密度的情况下)
- [3. KL Divergence between two Gaussian Distributions](#3-kl-divergence-between-two-gaussian-distributions)
- [4. Derivative of Gaussian Distribution](#4-derivative-of-gaussian-distribution)

## 1. One-dimensional Gaussian Distribution

$$
p(x) = \mathcal{N}(\mu, \sigma^2) = \frac{1}{\sigma\sqrt{2\pi}}\,
\exp\!\left(-\frac{(x-\mu)^{2}}{2\sigma^{2}}\right),x\in \mathbb{R}, \mu\in \mathbb{R}, \sigma>0
$$

## 2. Multi-dimensional Gaussian Distribution

A random vector is said to be k-variate normally distributed if every linear combination of its k components has a univariate normal distribution.

#### 2.1. 多维高斯分布的概率密度函数(在能写出概率密度的情况下)

$$
p(\mathbf{x}) = \mathcal{N}(\mathbf{x};\mu, \mathbf{\Sigma}) = \frac{1}{(2\pi)^{d/2}|\mathbf{\Sigma}|^{1/2}}\exp\left(-\frac{1}{2}(\mathbf{x}-\mu)^T\mathbf{\Sigma}^{-1}(\mathbf{x}-\mu)\right)\\
\mathbf{x}\in \mathbb{R}^d, \mu\in \mathbb{R}^d, \mathbf{\Sigma}\in \mathbb{R}^{d \times d}
$$

特殊情况 $\Sigma=\sigma^2 I$时，

$$
p(\mathbf{x}) = \mathcal{N}(\mathbf{x};\mu, \sigma^2 I) = \frac{1}{(2\pi)^{d/2}\sigma^d}\exp\left(-\frac{1}{2\sigma^2}\|\mathbf{x}-\mu\|^2\right)
$$

## 3. KL Divergence between two Gaussian Distributions

$$
p_1(\mathbf{x}) = \mathcal{N}(\mathbf{x};\mu_1, \mathbf{\Sigma}_1), p_2(\mathbf{x}) = \mathcal{N}(\mathbf{x};\mu_2, \mathbf{\Sigma}_2), \mathbf{x}\in \mathbb{R}^d
$$

$$
D_{KL}(p_1||p_2) = \frac{1}{2} \left( \log \frac{|\Sigma_2|}{|\Sigma_1|} + \text{Tr}(\Sigma_2^{-1}\Sigma_1) + (\mu_2 - \mu_1)^T\Sigma_2^{-1}(\mu_2 - \mu_1) - d \right)
$$

## 4. Derivative of Gaussian Distribution

Assume $\mathbf{\Sigma}\in \mathbb{R}^{d\times d}$ is an symmetric positive definite matrix, then

$$
\mathcal{N}(\mathbf{x}; \mathbf{\mu}, \mathbf{\Sigma}) = \frac{1}{\sqrt{(2\pi)^d|\mathbf{\Sigma}|}} \exp\left(-\frac{1}{2} (\mathbf{x} - \mathbf{\mu})^T \mathbf{\Sigma}^{-1} (\mathbf{x} - \mathbf{\mu})\right)
$$

If $\mathbf{\Sigma} = \sigma^2 \mathbf{I}$, then

$$
\begin{align*}
\nabla_{x} \ln \mathcal{N}(x; \mu, \sigma^2) &= \nabla_{x} -\frac{1}{2\sigma^2} (\mathbf{x} - \mathbf{\mu})^T (\mathbf{x} - \mathbf{\mu})\\
&= -\frac{1}{\sigma^2} (\mathbf{x} - \mathbf{\mu})
\end{align*}
$$
