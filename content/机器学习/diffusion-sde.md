---
title: SDE Diffusion
---

- [Score-based Generative Model through SDE](#score-based-generative-model-through-sde)
	- [1. Notations](#1-notations)
	- [2. Score-based Diffusion through SDE (Unconditional)](#2-score-based-diffusion-through-sde-unconditional)
	- [3. Training (Unconditional)](#3-training-unconditional)
	- [4. Score-based Diffusion through SDE (Conditional)](#4-score-based-diffusion-through-sde-conditional)
	- [5. Special Case](#5-special-case)
	- [6. Denoising Score Matching](#6-denoising-score-matching)
	- [7. VPSDE（Continuous DDPM） (Unconditional)](#7-vpsdecontinuous-ddpm-unconditional)
	- [8. VESDE](#8-vesde)

# Score-based Generative Model through SDE

## 1. Notations

The meaning of $\nabla \cdot [\cdot]$:

For scalar function $\phi(\mathbf{x}): \mathbb{R}^d \to \mathbb{R}$, we know $ \nabla \phi(\mathbf{x}) $ is the gradient.

For vector function $\phi(\mathbf{x}): \mathbb{R}^d \to \mathbb{R}^d $, $\nabla \cdot \phi(\mathbf{x}) \in \mathbb{R}$ is the divergence, defined as the sum of the partial derivatives of each component:

$$
\nabla \cdot \phi(\mathbf{x}) = \sum_{i=1}^{d} \frac{\partial \phi_i}{\partial x_i}
$$

For matrix function $\phi(\mathbf{x}): \mathbb{R}^d \to \mathbb{R}^{d \times d} $, its divergence is a vector, defined as:

$$
\nabla \cdot \phi(\mathbf{x}) = \left( \sum_{j=1}^{d} \frac{\partial \phi_{1j}}{\partial x_j}, \ldots, \sum_{j=1}^{d} \frac{\partial \phi_{dj}}{\partial x_j} \right)^\top
$$

or written in a more general form:

$$
\nabla \cdot \phi(\mathbf{x}) := \left( \nabla \cdot \phi^1(\mathbf{x}), \ldots, \nabla \cdot \phi^d(\mathbf{x}) \right)^\top
$$

where $ \phi^i(\mathbf{x}) $ is the $ i $th row of $ \phi $.

## 2. Score-based Diffusion through SDE (Unconditional)

SDE of forward process(noise):

$$
d \mathbf{x} = f(\mathbf{x}, t) dt + g(\mathbf{x}, t) dw\\
f: \mathbb{R}^d \times [0, T] \to \mathbb{R}^d, g: \mathbb{R}^d \times [0, T] \to \mathbb{R}^{d \times d}
$$

SDE of reverse process(denoise):

$$
d \mathbf{x} = \left(f(\mathbf{x}, t) - \nabla \cdot [g(\mathbf{x}, t)g(\mathbf{x}, t)^T]  -  g(\mathbf{x}, t)g(\mathbf{x}, t)^T \nabla_\mathbf{x} \ln p_t (\mathbf{x})\right) dt + g(\mathbf{x}, t) dw
$$

probability flow ODE:

$$
d \mathbf{x} = \left(f(\mathbf{x}, t) - \frac{1}{2} \nabla \cdot [g(\mathbf{x}, t)g(\mathbf{x}, t)^T]  -  \frac{1}{2} g(\mathbf{x}, t)g(\mathbf{x}, t)^T \nabla_\mathbf{x} \ln p_t (\mathbf{x})\right) dt
$$

## 3. Training (Unconditional)

- Sliced Score Matching:

$$
\theta^* = \arg \min_\theta \mathbb{E}_t \left\{ \lambda(t) \mathbb{E}_{\mathbf{x}(0)} \mathbb{E}_{\mathbf{x}(t)} \mathbb{E}_{\mathbf{v} \sim p_{\mathbf{v}}} \left[ \mathbf{v}^\top \mathbf{s}_\theta(\mathbf{x}(t), t) \mathbf{v} +  \frac{1}{2} (\mathbf{v}^T \mathbf{s}_\theta(\mathbf{x}(t), t) )^2 \right] \right\}\\
$$

- Denoising Score Matching:
  $$
  \theta^* = \arg \min_\theta \mathbb{E}_{t \sim U(0, T)} \lambda(t) \mathbb{E}_{x_0 \sim p_0} \left[ \mathbb{E}_{x \sim p_{0t}} \left[ \left\| s_\theta (x,t) - \nabla_\mathbf{x} \ln p_{0t} (\mathbf{x}|\mathbf{x}_0) \right\|_2^2 \right] \right]
  $$

## 4. Score-based Diffusion through SDE (Conditional)

$$
d \mathbf{x} = \left(f(\mathbf{x}, t) - \nabla \cdot [g(\mathbf{x}, t)g(\mathbf{x}, t)^T]  -  g(\mathbf{x}, t)g(\mathbf{x}, t)^T \nabla_\mathbf{x} \ln p_t (\mathbf{x}|\mathbf{y})\right) dt + g(\mathbf{x}, t) dw
$$

$$
\nabla_\mathbf{x} \ln p_t (\mathbf{x}|\mathbf{y}) = \nabla_\mathbf{x} \ln \left(\frac{p_t (\mathbf{y}|\mathbf{x})p_t (\mathbf{x})}{p_t (\mathbf{y})}\right) = \nabla_\mathbf{x} \ln p_t (\mathbf{y}|\mathbf{x}) + \nabla_\mathbf{x} \ln p_t (\mathbf{x})
$$

$$
d \mathbf{x} = \left(f(\mathbf{x}, t) -  \nabla \cdot [g(\mathbf{x}, t)g(\mathbf{x}, t)^T]  -  g(\mathbf{x}, t)g(\mathbf{x}, t)^T \left(\nabla_\mathbf{x} \ln p_t (\mathbf{y}|\mathbf{x}) + \nabla_\mathbf{x} \ln p_t (\mathbf{x})\right)\right) dt + g(\mathbf{x}, t) dw
$$

We can train a neural network $c(\mathbf{x},t)$ to learn $\ln p_t (\mathbf{y}|\mathbf{x})$

We can also use some prior knowledge to directly determine $\nabla_\mathbf{x} \ln p_t (\mathbf{y}|\mathbf{x})$

## 5. Special Case

If $\exists \tilde{g}(t) \in \mathbb{R}$ s.t. $g(\mathbf{x}, t) = \tilde{g}(t) \cdot I$, then the reverse process can be written as:

$$
d \mathbf{x} = \left(f(\mathbf{x}, t) - \tilde{g}(t)^2 \nabla_\mathbf{x} \ln p_t (\mathbf{x})\right) dt + \tilde{g}(t) dw
$$

## 6. Denoising Score Matching

Assume forward diffusion process can be written as $\mathbf{x}_t = a_t \mathbf{x}_0 + b_t \mathbf{\epsilon}, \mathbf{\epsilon} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$, then

$$
\mathbf{x}_t \sim \mathcal{N}(a_t \mathbf{x}_0, b_t^2 \mathbf{I})
$$

minimize

$$
\mathop{\mathbb{E}}\limits_{t,\mathbf{x}_0, \mathbf{x}_t \sim p_{0t}(\mathbf{x}_t|\mathbf{x}_0)} \|s_{\theta}(\mathbf{x}_t, t) - \nabla_{\mathbf{x}_t} \ln p_{0t}(\mathbf{x}_t|\mathbf{x}_0) \|_2^2
$$

- Equivalence of Epsilon Model and Score Model

$$
\begin{align*}
\text{score} &= \nabla_{\mathbf{x}_t} \ln p_{0t}(\mathbf{x}_t|\mathbf{x}_0)\\
&= -\frac{1}{b_t^2} (\mathbf{x}_t - a_t \mathbf{x}_0)\\
&= -\frac{\mathbf{\epsilon}}{b_t}
\end{align*}
$$

- Unconditional Score Matching

$\argmin \|\frac{-1}{b_t}\epsilon_{\theta}(\mathbf{x}_t, t) - \frac{-1}{b_t} \mathbf{\epsilon}\|_2^2 \iff \argmin \|\epsilon_{\theta}(\mathbf{x}_t, t) - \mathbf{\epsilon}\|_2^2$

- Conditional (Loss Guidance) Score Matching

$\argmin \|\frac{-1}{b_t}\epsilon_{\theta}(\mathbf{x}_t, t) - \frac{-1}{b_t} \mathbf{\epsilon} - \nabla_{x}{-l(\mathbf{x}_t,\mathbf{x}_0)} \|_2^2 \iff \argmin \|\epsilon_{\theta}(\mathbf{x}_t, t) - \mathbf{\epsilon} - \nabla_{x}{b_t l(\mathbf{x}_t,\mathbf{x}_0)} \|_2^2$

## 7. VPSDE（Continuous DDPM） (Unconditional)

$$
P(\mathbf{x}_t|\mathbf{x}_{t-1}) = \mathcal{N} (\mathbf{x}_t; \sqrt{1 - \beta_t} \cdot \mathbf{x}_{t-1}, \beta_t \cdot I)
$$

$$
\mathbf{x}_t = \sqrt{1 - \beta_t} \cdot \mathbf{x}_{t-1} + \sqrt{\beta_t} \cdot \epsilon, \quad \epsilon \sim \mathcal{N} (0, I)
$$

$$
\mathbf{x}_{t + \Delta t} - \mathbf{x}_t = \sqrt{1 - \beta_{t+\Delta t}} \cdot \mathbf{x}_t + \sqrt{\beta_{t + \Delta t}} \cdot \epsilon - \mathbf{x}_t
$$

Because $\sqrt{1-x} = 1 - \frac{x}{2} + o(x)$, we have:

$$
\mathbf{x}_{t + \Delta t} - \mathbf{x}_t = - \frac{\beta_{t + \Delta t}}{2} \cdot \mathbf{x}_t + \sqrt{\beta_{t + \Delta t}} \cdot \epsilon + o(\beta_{t + \Delta t}) \cdot \mathbf{x}_t
$$

SDE of forward process(noise):

$$
d \mathbf{x} = - \frac{\beta_t}{2} \cdot \mathbf{x} dt + \sqrt{\beta_t} dw
$$

SDE of reverse process(denoise):

$$
d \mathbf{x} = \left(- \frac{\beta_t}{2} \cdot \mathbf{x} - \beta_t \cdot \nabla_\mathbf{x} \ln p_t (\mathbf{x})\right) dt + \sqrt{\beta_t} dw
$$

参数对比

| model | beta        | n_step |
| ----- | ----------- | ------ |
| DDPM  | 0.0001-0.02 | 1000   |
| VPSDE | 0.1-20      | 1000   |

## 8. VESDE

$$
\mathbf{x}_t \sim \mathcal{N}(\mathbf{x}_0, \sigma_t^2 I),\quad \sigma_t = \sigma_{min} (\sigma_{max}/\sigma_{min})^{t}
$$

$$
\begin{align*}
d x &= g(t) dw\\
x_t &= x_0 + \int_0^t g(s) ds\\
Var[x_t] &= \int_0^t g(s)^2 ds =: \sigma_t^2\\
g(t) &= \sqrt{\frac{d}{dt} \sigma_t^2} = \sigma_t \sqrt{2\ln(\sigma_{max}/\sigma_{min})}
\end{align*}
$$

离散情况下：

$$
\begin{align*}
x_t &= x_{t-1} + g(t) \epsilon_t, \quad \epsilon_t \sim \mathcal{N}(0, I)\\
\sigma_t^2 &= \sigma_{t-1}^2 + g(t)^2\\
g(t) &= \sqrt{\sigma_t^2 - \sigma_{t-1}^2}
\end{align*}
$$
