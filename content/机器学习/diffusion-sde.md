---
title: SDE Diffusion
---

# Score-based Generative Model through SDE

- [Score-based Generative Model through SDE](#score-based-generative-model-through-sde)
	- [1. DDPM (Unconditional)](#1-ddpm-unconditional)
	- [2. Score-based Diffusion through SDE (Unconditional)](#2-score-based-diffusion-through-sde-unconditional)
	- [3. Training (Unconditional)](#3-training-unconditional)
	- [4. Score-based Diffusion through SDE (Conditional)](#4-score-based-diffusion-through-sde-conditional)

---

## 1. DDPM (Unconditional)

$$
P(x_t|x_{t-1}) = \mathcal{N} (x_t; \sqrt{1 - \beta_t} * x_{t-1}, \beta_t * I)
$$

$$
x_t = \sqrt{1 - \beta_t} * x_{t-1} + \sqrt{\beta_t} * \epsilon, \quad \epsilon \sim \mathcal{N} (0, I)
$$

$$
x_{t + \Delta t} - x_t = \sqrt{1 - \beta_{t+\Delta t}} * x_t + \sqrt{\beta_{t + \Delta t}} * \epsilon - x_t
$$

$$
\sqrt{1-x} = 1 - \frac{x}{2} + o(x)
$$

$$
x_{t + \Delta t} - x_t = - \frac{\beta_{t + \Delta t}}{2} * x_t + \sqrt{\beta_{t + \Delta t}} * \epsilon + o(\beta_{t + \Delta t})x_t
$$

---

## 2. Score-based Diffusion through SDE (Unconditional)

**正向过程(加噪)**

$$
dx = f(x, t) dt + g(x, t) dw
$$

$$
dx = - \frac{\beta_t}{2} * x dt + \sqrt{\beta_t} dw
$$

**逆向过程(去噪)**

$$
dx = \left(f(x, t) - g(x, t)^2 \nabla_x \ln p_t (x)\right) dt + g(x, t) dw
$$

$$
dx = \left(- \frac{\beta_t}{2} * x - \beta_t \nabla_x \ln p_t (x)\right) dt + \sqrt{\beta_t} dw
$$

---

## 3. Training (Unconditional)

训练一个神经网络 $s_\theta (x,t)$ 来预测 $\nabla_x \ln p_t (x)$，因此我们的最小化目标为：

$$
\mathbb{E}_{t \sim U(0, T)} \left[ \mathbb{E}_{x \sim p_t} \left[ \left\| s_\theta (x,t) - \nabla_x \ln p_t (x) \right\|_2^2 \right] \right]
$$

但是 $p_t$ 是未知的，这里使用条件期望的重期望公式：

$$
\mathbb{E}_{X \sim P}[X] = \mathbb{E}_{Y \sim Q}[\mathbb{E}_{X \sim P}[X|Y]]
$$

$$
\mathbb{E}_{X \sim P}[f(P(X))] = \mathbb{E}_{Y \sim Q}[\mathbb{E}_{X \sim P} [f(P(X))|Y]]
$$

因此最小化目标可以转化为：

$$
\mathbb{E}_{t \sim U(0, T)} \mathbb{E}_{x_0 \sim p_0} \left[ \mathbb{E}_{x \sim p_t} \left[ \left\| s_\theta (x,t) - \nabla_x \ln p_t (x) \right\|_2^2 | x_0 \right] \right]
$$

$$
\mathbb{E}_{t \sim U(0, T)} \mathbb{E}_{x_0 \sim p_0} \left[ \mathbb{E}_{x \sim p_{0t}} \left[ \left\| s_\theta (x,t) - \nabla_x \ln p_{0t} (x|x_0) \right\|_2^2 \right] \right]
$$

---

## 4. Score-based Diffusion through SDE (Conditional)

$$
dx = \left(f(x, t) - g(x, t)^2 \nabla_x \ln p_t (x|y)\right) dt + g(x, t) dw
$$

$$
\nabla_x \ln p_t (x|y) = \nabla_x \ln \left(\frac{p_t (y|x)p_t (x)}{p_t (y)}\right)
$$

$$
= \nabla_x \ln p_t (y|x) + \nabla_x \ln p_t (x)
$$

$$
dx = \left(f(x,t) - g(x, t)^2 \left(\nabla_x \ln p_t (y|x) + \nabla_x \ln p_t (x)\right)\right) dt + g(x, t) dw
$$

可以训练一个神经网络 $c(x,t)$ 来学习 $\ln p_t (y|x)$

也可以使用某些先验知识直接确定 $\nabla_x \ln p_t (y|x)$
