---
title: SDE Diffusion
---

- [Score-based Generative Model through SDE](#score-based-generative-model-through-sde)
	- [1. Notations](#1-notations)
	- [2. Score-based Diffusion through SDE (Unconditional)](#2-score-based-diffusion-through-sde-unconditional)
	- [3. Training (Unconditional)](#3-training-unconditional)
	- [4. Score-based Diffusion through SDE (Conditional)](#4-score-based-diffusion-through-sde-conditional)
	- [5. Special Case](#5-special-case)
	- [6. Example: Continuous DDPM (Unconditional)](#6-example-continuous-ddpm-unconditional)

# Score-based Generative Model through SDE

## 1. Notations

The meaning of $ \nabla \cdot [\cdot] $:

For scalar function $ \phi(\mathbf{x}): \mathbb{R}^d \to \mathbb{R} $, we know $ \nabla \phi(\mathbf{x}) $ is the gradient.

For vector function $ \phi(\mathbf{x}): \mathbb{R}^d \to \mathbb{R}^d $, $\nabla \cdot \phi(\mathbf{x}) \in \mathbb{R} $ is the divergence, defined as the sum of the partial derivatives of each component:

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
dx = f(x, t) dt + g(x, t) dw\\
f: \mathbb{R}^d \times [0, T] \to \mathbb{R}^d, g: \mathbb{R}^d \times [0, T] \to \mathbb{R}^{d \times d}
$$

SDE of reverse process(denoise):

$$
dx = \left(f(x, t) - \nabla \cdot [g(x, t)g(x, t)^T]  -  g(x, t)g(x, t)^T \nabla_x \ln p_t (x)\right) dt + g(x, t) dw
$$

probability flow ODE:

$$
dx = \left(f(x, t) - \frac{1}{2} \nabla \cdot [g(x, t)g(x, t)^T]  -  \frac{1}{2} g(x, t)g(x, t)^T \nabla_x \ln p_t (x)\right) dt
$$

## 3. Training (Unconditional)

- Sliced Score Matching:

$$
\theta^* = \arg \min_\theta \mathbb{E}_t \left\{ \lambda(t) \mathbb{E}_{\mathbf{x}(0)} \mathbb{E}_{\mathbf{x}(t)} \mathbb{E}_{\mathbf{v} \sim p_{\mathbf{v}}} \left[ \mathbf{v}^\top \mathbf{s}_\theta(\mathbf{x}(t), t) \mathbf{v} +  \frac{1}{2} (\mathbf{v}^T \mathbf{s}_\theta(\mathbf{x}(t), t) )^2 \right] \right\}\\
$$

- Denoising Score Matching:
  $$
  \theta^* = \arg \min_\theta \mathbb{E}_{t \sim U(0, T)} \lambda(t) \mathbb{E}_{x_0 \sim p_0} \left[ \mathbb{E}_{x \sim p_{0t}} \left[ \left\| s_\theta (x,t) - \nabla_x \ln p_{0t} (x|x_0) \right\|_2^2 \right] \right]
  $$

## 4. Score-based Diffusion through SDE (Conditional)

$$
dx = \left(f(x, t) - \nabla \cdot [g(x, t)g(x, t)^T]  -  g(x, t)g(x, t)^T \nabla_x \ln p_t (x|y)\right) dt + g(x, t) dw
$$

$$
\nabla_x \ln p_t (x|y) = \nabla_x \ln \left(\frac{p_t (y|x)p_t (x)}{p_t (y)}\right) = \nabla_x \ln p_t (y|x) + \nabla_x \ln p_t (x)
$$

$$
dx = \left(f(x,t) -  \nabla \cdot [g(x, t)g(x, t)^T]  -  g(x, t)g(x, t)^T \left(\nabla_x \ln p_t (y|x) + \nabla_x \ln p_t (x)\right)\right) dt + g(x, t) dw
$$

We can train a neural network $c(x,t)$ to learn $\ln p_t (y|x)$

We can also use some prior knowledge to directly determine $\nabla_x \ln p_t (y|x)$

## 5. Special Case

If $\exists \tilde{g}(t) \in \mathbb{R}$ s.t. $g(x, t) = \tilde{g}(t) \cdot I$, then the reverse process can be written as:

$$
dx = \left(f(x, t) - \tilde{g}(t)^2 \nabla_x \ln p_t (x)\right) dt + \tilde{g}(t) dw
$$

## 6. Example: Continuous DDPM (Unconditional)

$$
P(x_t|x_{t-1}) = \mathcal{N} (x_t; \sqrt{1 - \beta_t} \cdot x_{t-1}, \beta_t \cdot I)
$$

$$
x_t = \sqrt{1 - \beta_t} \cdot x_{t-1} + \sqrt{\beta_t} \cdot \epsilon, \quad \epsilon \sim \mathcal{N} (0, I)
$$

$$
x_{t + \Delta t} - x_t = \sqrt{1 - \beta_{t+\Delta t}} \cdot x_t + \sqrt{\beta_{t + \Delta t}} \cdot \epsilon - x_t
$$

Because $\sqrt{1-x} = 1 - \frac{x}{2} + o(x)$, we have:

$$
x_{t + \Delta t} - x_t = - \frac{\beta_{t + \Delta t}}{2} \cdot x_t + \sqrt{\beta_{t + \Delta t}} \cdot \epsilon + o(\beta_{t + \Delta t}) \cdot x_t
$$

SDE of forward process(noise):

$$
dx = - \frac{\beta_t}{2} \cdot x dt + \sqrt{\beta_t} dw
$$

SDE of reverse process(denoise):

$$
dx = \left(- \frac{\beta_t}{2} \cdot x - \beta_t \cdot \nabla_x \ln p_t (x)\right) dt + \sqrt{\beta_t} dw
$$
