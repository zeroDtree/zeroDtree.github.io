---
title: posterior mean
---



### Tweedie's formula

---

Let $p(\mathbf{y}|\mathbf{\eta})$ belong to the exponential family distribution

$$p(\mathbf{y}|\mathbf{\eta}) = p_0(\mathbf{y}) \exp(\mathbf{\eta}^\top T(\mathbf{y}) - \varphi(\mathbf{\eta}))$$

where $\mathbf{\eta}$ is the canonical vector of the family, $T(\mathbf{y})$ is some function of $\mathbf{y}$, and $\varphi(\mathbf{\eta})$ is the cumulant generation function which normalizes the density, and $p_0(\mathbf{y})$ is the density up to the scale factor when $\mathbf{\eta} = 0$. Then, the posterior mean $\hat{\mathbf{\eta}} := \mathbb{E}[\mathbf{\eta}|\mathbf{y}]$ should satisfy

$$(\nabla_{\mathbf{y}} T(\mathbf{y}))^\top \hat{\mathbf{\eta}} = \nabla_{\mathbf{y}} \log p(\mathbf{y}) - \nabla_{\mathbf{y}} \log p_0(\mathbf{y})$$

### Posterior mean of VP-SDE (continuous DDPM)

---

For the case of VP-SDE or DDPM sampling, $p(\mathbf{x}_0|\mathbf{x}_t)$ has the unique posterior mean at

$$
\hat{\mathbf{x}}_0 := \mathbb{E}[\mathbf{x}_0|\mathbf{x}_t] = \frac{1}{\sqrt{\bar{\alpha}(t)}}(\mathbf{x}_t + (1 - \bar{\alpha}(t))\nabla_{\mathbf{x}_t}\log p_t(\mathbf{x}_t))
$$

**Proof.** For the case of VP-SDE or DDPM forward sampling, we have

$$
p(\mathbf{x}_t|\mathbf{x}_0) = \mathcal{N}(\mathbf{x}_t; \sqrt{\bar{\alpha}(t)}\mathbf{x}_0, (1 - \bar{\alpha}(t))I)
$$

$$
p(\mathbf{x}_t|\mathbf{x}_0) = \frac{1}{(2\pi(1 - \bar{\alpha}(t)))^{d/2}}\exp\left(-\frac{\|\mathbf{x}_t - \sqrt{\bar{\alpha}(t)}\mathbf{x}_0\|^2}{2(1 - \bar{\alpha}(t))}\right),
$$

which is a Gaussian distribution. The corresponding canonical decomposition is then given by

$$
p(\mathbf{x}_t|\mathbf{x}_0) = p_0(\mathbf{x}_t)\exp\left(\mathbf{x}_0^\top T(\mathbf{x}_t) - \varphi(\mathbf{x}_0)\right),
$$

where

$$
\begin{align*}
p_0(\mathbf{x}_t) &:= \frac{1}{(2\pi(1 - \bar{\alpha}(t)))^{d/2}}\exp\left(-\frac{\|\mathbf{x}_t\|^2}{2(1 - \bar{\alpha}(t))}\right) \\
T(\mathbf{x}_t) &:= \frac{\sqrt{\bar{\alpha}(t)}}{1 - \bar{\alpha}(t)}\mathbf{x}_t \\
\varphi(\mathbf{x}_0) &:= \frac{\bar{\alpha}(t)\|\mathbf{x}_0\|^2}{2(1 - \bar{\alpha}(t))}
\end{align*}
$$

Therefore, we have

$$
\frac{\sqrt{\bar{\alpha}(t)}}{1 - \bar{\alpha}(t)}\hat{\mathbf{x}}_0 = \nabla_{\mathbf{x}_t}\log p_t(\mathbf{x}_t) + \frac{1}{1 - \bar{\alpha}(t)}\mathbf{x}_t
$$

which leads to

$$
\hat{\mathbf{x}}_0 = \frac{1}{\sqrt{\bar{\alpha}(t)}}(\mathbf{x}_t + (1 - \bar{\alpha}(t))\nabla_{\mathbf{x}_t}\log p_t(\mathbf{x}_t))
$$

This concludes the proof.

### Posterior mean of General SDE

A general SDE of diffusion is given by

$$
d \mathbf{x} = \mathbf{f}(\mathbf{x}, t)dt + G(t) d\mathbf{w}_t
$$

where $\mathbf{f}: \mathbb{R}^d \times [0, T] \to \mathbb{R}^d$ and $G: [0, T] \to \mathbb{R}^{d \times d}$ are given functions.

$\red{TODO}$