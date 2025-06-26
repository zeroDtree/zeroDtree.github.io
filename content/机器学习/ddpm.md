---
title: DDPM
---

- [Denoising Diffusion Probabilistic Models](#denoising-diffusion-probabilistic-models)
  - [1. Forward Diffusion Process](#1-forward-diffusion-process)
    - [1.1. Reparameterization](#11-reparameterization)
  - [2. Training Process](#2-training-process)
  - [3. Sampling Process](#3-sampling-process)
  - [4. Useful Formulas](#4-useful-formulas)

# Denoising Diffusion Probabilistic Models

## 1. Forward Diffusion Process

All vectors are column vectors. For multi-dimensional tensors, they can be flattened into column vectors.

In the forward process, we gradually transform a data distribution $P_0$ into a distribution $\mathcal{N}(\mathbf{0},\mathbf{I})$.

$x_0 \rightarrow x_1 \rightarrow x_2 \rightarrow x_3 \rightarrow ... \rightarrow x_T$

$P_0 \rightarrow P_1 \rightarrow P_2 \rightarrow P_3 \rightarrow ... \rightarrow P_T \approx \mathcal{N}(\mathbf{0},\mathbf{I})$

$$
\mathbf{x}_0\sim{P_0}
$$

Given noise schedule $(\beta_t)_{t=1}^T$,

$$
\begin{align}
q(x_t|x_{t-1}) = \mathcal{N}(x_t; \sqrt{1-\beta_t}x_{t-1}, \beta_t\mathbf{I})
\end{align}
$$

or equivalently, let $\alpha_t = 1 - \beta_t$, we have

$$
\begin{align}
q(\mathbf{x}_t|\mathbf{x}_{t-1}) = \mathcal{N}(\mathbf{x}_t; \sqrt{\alpha_t}\mathbf{x}_{t-1}, (1-\alpha_t)\mathbf{I})
\end{align}
$$

### 1.1. Reparameterization

$
x_t = \sqrt{1-\beta_t}x_{t-1}+\sqrt{\beta_t}\epsilon,\epsilon\sim\mathcal{N}(0,1)
$

By mathematical induction, we can prove that

$$
q(\mathbf{x}_t|\mathbf{x}_0) = \mathcal{N}(\mathbf{x}_t; \sqrt{\prod_{i=1}^{t}(1-\beta_i)}\mathbf{x}_0, (1-(\prod_{i=1}^{t}(1-\beta_i)))\mathbf{I})
$$

That is, multiple noise additions can be expressed as one noise addition and it is easy to know that as the number of noise additions increases, the distribution of the data will be transformed into a standard normal distribution.

```python
import torch
n_steps = 500
betas = torch.linspace(0.0001, 0.02, n_steps)
alphas = 1 - betas
alphas_cumprod = torch.cumprod(alphas, dim=0)
expectation = alphas_cumprod.sqrt()
variance = 1 - alphas_cumprod
expectation_rounded = [round(x, 3) for x in expectation[::10].numpy().tolist()]
variance_rounded = [round(x, 3) for x in variance[::10].numpy().tolist()]
print(f"expectation: {expectation_rounded}")
print(f"variance: {variance_rounded}")
```

```
expectation: [1.0, 0.998, 0.995, 0.989, 0.982, 0.972, 0.961, 0.948, 0.934, 0.917, 0.9, 0.88, 0.86, 0.838, 0.815, 0.791, 0.767, 0.742, 0.716, 0.689, 0.662, 0.635, 0.608, 0.581, 0.554, 0.527, 0.501, 0.474, 0.449, 0.423, 0.399, 0.375, 0.352, 0.329, 0.308, 0.287, 0.267, 0.248, 0.23, 0.213, 0.196, 0.181, 0.166, 0.153, 0.14, 0.128, 0.116, 0.106, 0.096, 0.087]
variance: [0.0, 0.003, 0.01, 0.021, 0.036, 0.054, 0.076, 0.101, 0.128, 0.159, 0.191, 0.225, 0.261, 0.298, 0.335, 0.374, 0.412, 0.45, 0.488, 0.525, 0.561, 0.596, 0.63, 0.662, 0.693, 0.722, 0.749, 0.775, 0.799, 0.821, 0.841, 0.859, 0.876, 0.891, 0.905, 0.918, 0.929, 0.938, 0.947, 0.955, 0.961, 0.967, 0.972, 0.977, 0.98, 0.984, 0.986, 0.989, 0.991, 0.992]
```

## 2. Training Process

Train a neural network $\mathbf{\epsilon}_{\theta}$ to predict the noise $\mathbf{\epsilon}$ in $\mathbf{x}_t = \sqrt{\bar{\alpha}_t}\mathbf{x}_0 + \sqrt{1-\bar{\alpha}_t}\mathbf{\epsilon}$

To minimize:

$$
\begin{align}
\mathop{\mathbb{E}}\limits_{t, \mathbf{x}_0, \mathbf{\epsilon}} \left[ \left\| \mathbf{\epsilon} - \mathbf{\epsilon}_{\theta}(\mathbf{x}_t,t) \right\|^2 \right]
\end{align}
$$

## 3. Sampling Process

First, estimate an clean data $\hat{\mathbf{x}}_0:=\frac{1}{\sqrt{\bar{\alpha}_t}}(\mathbf{x}_t - \sqrt{1-\bar{\alpha}_t}\mathbf{\epsilon}_{\theta}(\mathbf{x}_t,t))$

Then, we can use the following conditional distribution to sample $\mathbf{x}_{t-1}$(the data at the previous time step):

$$
\begin{align}
q(\mathbf{x}_{t-1}|\mathbf{x}_t, \hat{\mathbf{x}}_0) &= \frac{q(\mathbf{x}_t|\mathbf{x}_{t-1}, \hat{\mathbf{x}}_0)q(\mathbf{x}_{t-1}|\hat{\mathbf{x}}_0)}{q(\mathbf{x}_t|\hat{\mathbf{x}}_0)}\\
&=\frac{q(\mathbf{x}_t|\mathbf{x}_{t-1})q(\mathbf{x}_{t-1}|\hat{\mathbf{x}}_0)}{q(\mathbf{x}_t|\hat{\mathbf{x}}_0)}\\
&=\mathcal{N}\left( \boldsymbol{x}_{t-1}; \underbrace{\frac{\sqrt{\alpha_t}(1-\bar{\alpha}_{t-1})\boldsymbol{x}_t + \sqrt{\bar{\alpha}_{t-1}}(1-\alpha_t)\hat{\boldsymbol{x}}_0}{1-\bar{\alpha}_t}}_{\mu_q(\boldsymbol{x}_t, \hat{\boldsymbol{x}}_0)}, \underbrace{\frac{(1-\alpha_t)(1-\bar{\alpha}_{t-1})}{1-\bar{\alpha}_t}\mathbf{I}}_{\Sigma_q(t)} \right)
\end{align}
$$

In practice, $\Sigma_q(t)$ is usually set to $\beta_t\mathbf{I}$.

Substitute $\hat{\mathbf{x}}_0$ into the formula above, we have

$$
\begin{align}
\mu_{q}  = \frac{1}{\sqrt{\alpha_t}} \mathbf{x}_t - \frac{1 - \alpha_t}{\sqrt{1 - \bar{\alpha}_t} \sqrt{\alpha_t}} \mathbf{\epsilon}_t
\end{align}
$$

Therefore,

$$
\mathbf{x}_{t-1} = \frac{1}{\sqrt{\alpha_t}} \left( \mathbf{x}_t - \frac{1-\alpha_t}{\sqrt{1-\bar{\alpha}_t}} \mathbf{\epsilon}_\theta(\mathbf{x}_t, t) \right) + (1-\alpha_t)\mathbf{\epsilon}
$$

## 4. Useful Formulas

$$
\begin{align*}
\mathbf{x}_t = a_t\mathbf{x}_{t-1} + b_t\mathbf{\epsilon}_t
\end{align*}
$$

By mathematical induction, we can prove that

$$
\begin{align*}
\mathbf{x}_t &= (\prod_{i=1}^{t}a_i)\mathbf{x}_0 + \sum_{i=1}^{t}(\prod_{j=i+1}^{t}a_j)b_i\mathbf{\epsilon}_i
\end{align*}
$$

If $a_t^2+b_t^2=1$, then

$$
(\prod_{i=1}^{t}a_i)^2 + \sum_{i=1}^{t}(\prod_{j=i+1}^{t}a_j)^2b_i^2=1
$$

Then

$$
\mathbf{x}_t = (\prod_{i=1}^{t}a_i)\mathbf{x}_0 + \sqrt{1-(\prod_{i=1}^{t}a_i)^2}\mathbf{\epsilon},\mathbf{\epsilon}\sim\mathcal{N}(\mathbf{0},\mathbf{I})
$$

In particular, for DDPM, we have $a_t = \sqrt{\alpha_t} = \sqrt{1-\beta_t}$ and $b_t = \sqrt{1-\alpha_t} = \sqrt{\beta_t}$.
