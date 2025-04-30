---
title: DDPM
date: 2024-11-15 20:45:45
---

- [Denoising Diffusion Probabilistic Models](#denoising-diffusion-probabilistic-models)
  - [1. 加噪过程](#1-加噪过程)
    - [1.1. 重参数化](#11-重参数化)
  - [2. 去噪过程](#2-去噪过程)
      - [2.1. 利用重新参数话，消去 1 个随机变量，以减小方差。](#21-利用重新参数话消去-1-个随机变量以减小方差)
  - [3. 训练过程](#3-训练过程)
  - [4. 采样过程](#4-采样过程)
  - [5. 用到的性质](#5-用到的性质)
      - [5.1. 数学期望的性质](#51-数学期望的性质)
      - [5.2. 加噪的递归展开](#52-加噪的递归展开)
  - [6. 参考资料](#6-参考资料)

# Denoising Diffusion Probabilistic Models

## 1. 加噪过程

默认向量都是列向量，对于多维 Tensor,可以把它 flatten 成列向量。

在前向过程中把一个数据分布 P 一步一步变成分布 $\mathcal{N}(0,I)$

$P \rightarrow P_1 \rightarrow P_2 \rightarrow P_3 \rightarrow ... \rightarrow \mathcal{N}(0,I)$

$$
x_0\sim{P}
$$

$$
q(x_t|x_{t-1}) = \mathcal{N}(x_t; \sqrt{1-\beta_t}x_{t-1}, \beta_t\mathbf{I})
$$

### 1.1. 重参数化

$
x_t = \sqrt{1-\beta_t}x_{t-1}+\sqrt{\beta_t}\epsilon,\epsilon\sim\mathcal{N}(0,1)
$

通过数学归纳法可证明

$$
q(x_t|x_0) = \mathcal{N}(x_t; \sqrt{\prod_{i=1}^{t}(1-\beta_i)}x_0, (1-(\prod_{i=1}^{t}(1-\beta_i)))\mathbf{I})
$$

即多次加噪可以表示为一次加噪

且易知随着加噪次数的增多，会把数据的分布转化成标准正态分布

```python
import torch
n_steps = 500
beta = torch.linspace(0.0001, 0.02, n_steps)
beta = 1 - beta
x = torch.prod(beta)
expectation = x.sqrt()
variance = (1 - x) * 1
print(f"expectation: {expectation}, variance: {variance}")
```

```
expectation: 0.07970395684242249, variance: 0.9936472773551941
```

## 2. 去噪过程

更一般地设，$x_t=a_tx_{t-1} + b_t\epsilon_t,\epsilon_t\sim \mathcal{N}(0,I),a_t^2+b_t^2=1$

$x_{t-1} = \frac{1}{a_t}(x_t - b_t\epsilon_t)$

递归展开后 $x_t = (\prod_{i=1}^{t}a_i)x_0 + \sqrt{1-(\prod_{i=1}^{t}a_i)^2}\epsilon,\epsilon\sim\mathcal{N}(0,I)$

$(\prod_{i=1}^{t}a_i):=\bar{a}_t$

$\sqrt{1-(\prod_{i=1}^{t}a_i)^2}:=\bar{b}_t$

现在希望从$\mathcal{N}(0,I)$ 回到原始数据分布 P

令$\widehat{x}_{t-1}=u(x_t,t)=\frac{1}{\bar{a}_t}(x_t - \bar{b}_t\epsilon_{\theta}(x_t,t))$

$x_0 \xrightarrow{\bar{\epsilon}_t} x_{t-1} \xrightarrow{\epsilon_t} x_t$

$x_0 \xrightarrow{\bar{\epsilon}_t} x_{t-1} \xleftarrow{\epsilon_{\theta}(t)} x_t$

目标:最小化

$$
\begin{align*}
||x_{t-1}-\hat{x}_{t-1}||^2&=||\frac{1}{\bar{a}_t}(x_t - b_t\epsilon_t)- \frac{1}{\bar{a}_t}(x_t - b_t\epsilon_{\theta}(x_t,t))||^2\\
&\propto||\epsilon_t - \epsilon_{\theta}(x_t,t)||\\
&=||\epsilon_t - \epsilon_{\theta}(\bar{a}_tx_0 + a_t\bar{b}_{t-1}\bar{\epsilon}_{t-1} + b_t\epsilon_t,t)||^2 \tag{c}\\
\end{align*}
$$

#### 2.1. 利用重新参数话，消去 1 个随机变量，以减小方差。

$$
\begin{align*}
a_t\bar{b}_{t-1}\bar{\epsilon}_{t-1}+b_t\epsilon_t \Leftrightarrow \sqrt{a_t^2\bar{b}_{t-1}^2 + b_t^2}\epsilon=\bar{b}_t\epsilon,\epsilon\sim\mathcal{N}(0,1) \tag{a}
\end{align*}
$$

同理

$$
\begin{align*}
-a_t\bar{b}_{t-1}\epsilon_t+b_t\bar{\epsilon}_{t-1} \Leftrightarrow \bar{b}_t\omega,\omega\sim\mathcal{N}(0,1) \tag{b}
\end{align*}
$$

这里$\epsilon$和$\omega$ 是独立的

结合(a)和(b),解一个二元一次方程组把$\epsilon_t$表示出来

$$
\begin{align*}
a_1x+b_1y&=c_1\\
a_2x+b_2y&=c_2\\
x=\bar{\epsilon}_{t-1},&y=\epsilon_t
\end{align*}
$$

解得

$$
\begin{align*}
\epsilon_t &= \frac{\bar{b}_tb_t\epsilon - \bar{b}_ta_t\bar{b}_{t-1}\omega}{b_t^2+a_t^2\bar{b}_{t-1}^2}\\
&= \frac{b_t\epsilon - a_t\bar{b}_{t-1}\omega}{\bar{b}_t}
\end{align*}
$$

把$\epsilon_t$代入(c),然后给(c)套一个期望，因为我们希望最小化的是期望

$$
\begin{align*}
(c)&=E_{\bar{\epsilon}_{t-1},\epsilon_t}[||\epsilon_t - \epsilon_{\theta}(\bar{a}_tx_0 + a_t\bar{b}_{t-1}\bar{\epsilon}_{t-1} + b_t\epsilon_t,t)||^2]\\
&=E_{\epsilon,\omega}[||\frac{b_t}{\bar{b}_{t}}\epsilon - \frac{a_t\bar{b}_{t-1}}{\bar{b}_{t}}\omega - \epsilon_{\theta}(\bar{a}_tx_0 + \bar{b}_t\epsilon,t)||^2]\\
&=E_{\epsilon,\omega}[||(\frac{b_t}{\bar{b}_{t}}\epsilon - \epsilon_{\theta}(\bar{a}_tx_0 + \bar{b}_t\epsilon,t))- \frac{a_t\bar{b}_{t-1}}{\bar{b}_{t}}\omega||^2]\\
&:=E_{\epsilon,\omega}[||\phi(\epsilon)-k\omega||^2]\\
&=E_{\epsilon}[||\phi(\epsilon)||^2] + k^2E_{\omega}[||\omega||^2] - 2kE_{\epsilon,\omega}[\phi(\epsilon)^T\omega]
\end{align*}
$$

其中$\phi(\epsilon)=\frac{b_t}{\bar{b}_{t}}\epsilon - \epsilon_{\theta}(\bar{a}_tx_0 + \bar{b}_t\epsilon,t)$,$k=\frac{a_t\bar{b}_{t-1}}{\bar{b}_{t}}$

因为$\omega$和$\epsilon$是独立的，所以$\phi(\epsilon)$和$\omega$也是独立的(未证明)

$$
E[\phi(\epsilon)^T\omega] = E[\phi(\epsilon)]^TE[\omega] = 0
$$

因此我们的最小化目标为

$$
E_{\epsilon}[||\phi(\epsilon)||^2]=E_{\epsilon}[(||\frac{b_t}{\bar{b}_{t}}\epsilon - \epsilon_{\theta}(\bar{a}_tx_0 + \bar{b}_t\epsilon,t))||^2]
$$

所以损失函数设计为

$$
loss = ||\epsilon - \epsilon_{\theta}(\bar{a}_tx_0 + \bar{b}_t\epsilon,t)||^2
$$

对应到DDPM的论文中

$a_t=\sqrt{1-\beta_t}:=\sqrt{\alpha_t}$， 

$\bar{a}_t=\prod_{i=1}^{t}a_i=\prod_{i=1}^{t}\sqrt{\alpha_i}=\sqrt{\prod_{i=1}^{t}\alpha_i}=\sqrt{\bar{\alpha}_t}$

## 3. 训练过程

1. 采样一个样本$x_0 \sim P$
2. 采样一个时间步$t$
3. 采样一个高斯噪声$\epsilon \sim \mathcal{N}(0,I)$
4. 前向传播计算$\epsilon_{\theta}(\bar{a}_tx_0 + \bar{b}_t\epsilon,t)$
5. 反向传播最小化损失函数$|| \epsilon - \epsilon_{\theta}(\bar{a}_tx_0 + \bar{b}_t\epsilon,t)||^2$

$\epsilon_{\theta}$ 是神经网络,输入和输出有相同的维度。

## 4. 采样过程

1. 采用一个高斯噪声$\epsilon \sim \mathcal{N}(0,I)$
2. 倒着一步步去噪，$x_{t-1}=\frac{1}{a_t}(x_t - b_t\epsilon_{\theta}(x_t,t))$
3. 直到$t=0$时，$x_0$就是我们想要的采样结果

## 5. 用到的性质

#### 5.1. 数学期望的性质

$$
    E[Y] = E[AX + b] = AE[X] + b = A\mu + b
$$

$$
    \begin{align*}
    Cov(Y) &= Cov(AX + b) \\
    &= Cov(AX) \text{ (常数b不影响协方差)} \\
    &= E[(AX - A\mu)(AX - A\mu)^T] \\
    &= E[A(X - \mu)(X - \mu)^TA^T] \\
    &= AE[(X - \mu)(X - \mu)^T]A^T \\
    &= A\Sigma A^T
    \end{align*}
$$

- 高斯分布经过线性变换仍然是高斯分布(未证明)
- 独立的高斯分布相加之后还是高斯分布(未证明)

#### 5.2. 加噪的递归展开

$$
\begin{align*}
x_t &= a_tx_{t-1} + b_t\epsilon_t\\
x_t &= (\prod_{i=1}^{t}a_i)x_0 + \sum_{i=i}^{t}(\prod_{j=i+1}^{t}a_j)b_i\epsilon_i
\end{align*}
$$

如果$a_t^2+b_t^2=1$,则

$$
(\prod_{i=1}^{t}a_i)^2 + \sum_{i=1}^{t}(\prod_{j=i+1}^{t}a_j)^2b_i^2=1
$$

$$
x_t = (\prod_{i=1}^{t}a_i) x_0 + \sqrt{1-(\prod_{i=1}^{t}a_i)^2}\epsilon,\epsilon\sim\mathcal{N}(0,I)
$$

## 6. 参考资料

```
https://kexue.fm/archives/9119
https://zhuanlan.zhihu.com/p/525106459
https://arxiv.org/abs/2006.11239
```
