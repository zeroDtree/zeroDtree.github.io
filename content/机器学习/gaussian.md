---
title: Gaussian Distribution
---

## One-dimensional Gaussian Distribution

$$
p(x) = \mathcal{N}(\mu, \sigma^2) = \frac{1}{\sigma\sqrt{2\pi}}\,
\exp\!\left(-\frac{(x-\mu)^{2}}{2\sigma^{2}}\right),x\in \mathbb{R}, \mu\in \mathbb{R}, \sigma>0
$$

## Multi-dimensional Gaussian Distribution

A random vector is said to be k-variate normally distributed if every linear combination of its k components has a univariate normal distribution.

## KL Divergence between two Gaussian Distributions

$$
p_1(\mathbf{x}) = \mathcal{N}(\mathbf{x};\mu_1, \mathbf{\Sigma}_1), p_2(\mathbf{x}) = \mathcal{N}(\mathbf{x};\mu_2, \mathbf{\Sigma}_2), \mathbf{x}\in \mathbb{R}^d
$$

$$
D_{KL}(p_1||p_2) = \frac{1}{2} \left( \log \frac{|\Sigma_2|}{|\Sigma_1|} + \text{Tr}(\Sigma_2^{-1}\Sigma_1) + (\mu_2 - \mu_1)^T\Sigma_2^{-1}(\mu_2 - \mu_1) - d \right)
$$
