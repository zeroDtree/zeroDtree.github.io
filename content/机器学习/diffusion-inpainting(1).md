---
title: Diffusion Inpainting(1)
---

## 任务描述

Diffusion inpainting 的目标是在保留已知区域的前提下，利用扩散模型补全未知区域。这里的“区域”可以是图像中的像素、点云中的点、序列中的 token，或任意可被掩码选择的数据分量。

给定原始数据 $\mathbf{x}_0 \in \mathbb{R}^d$ 和二值掩码 $\mathbf{m} \in \{0,1\}^d$：

- $m_i = 1$ 表示第 $i$ 个分量属于已知区域，采样过程中应保持不变；
- $m_i = 0$ 表示第 $i$ 个分量属于未知区域，需要由模型生成或修复。

因此，inpainting 可以看作条件生成问题：

$$
p(\mathbf{x}_0^{\mathrm{unknown}} \mid \mathbf{x}_0^{\mathrm{known}})
$$

其中 $\mathbf{x}_0^{\mathrm{known}}$ 由掩码 $\mathbf{m}$ 指定，$\mathbf{x}_0^{\mathrm{unknown}}$ 是待生成的区域。本文默认模型显式感知 inpainting 条件：掩码和已知区域会作为额外输入参与训练与采样。关键约束是：逆向扩散每一步都只能改变未知区域，已知区域必须与前向扩散得到的对应时间步状态一致。

## 数学符号

- $d$：数据向量维度。对图像、点云等张量数据，可以先把张量展平成向量理解。
- $T$：扩散过程的总时间步。
- $\mathbf{x}_0 \in \mathbb{R}^d$：原始数据。
- $\mathbf{m} \in \{0,1\}^d$：与数据同形状的掩码，$1$ 表示已知区域，$0$ 表示待修复区域。
- $\mathbf{M}$：实际计算中与 $\mathbf{x}$ 同形状的掩码。若原始掩码维度较低，需要先广播到数据形状。
- $\odot$：逐元素相乘（Hadamard 积）。
- $q_t(\mathbf{x}_t \mid \mathbf{x}_0)$：从干净数据到时间 $t$ 的前向扩散分布。
- $p_T$：扩散过程终点的先验分布，常见选择是标准高斯分布。
- $\operatorname{ForwardDiffusion}(\mathbf{x}_0,t)$：从 $\mathbf{x}_0$ 采样得到 $\mathbf{x}_t$ 的前向扩散算子。
- $\operatorname{ForwardStep}(\mathbf{x}_{t-1},t)$：从 $t-1$ 重新加噪到 $t$ 的一步前向算子。
- $\operatorname{ReverseStep}_\theta(\mathbf{x}_t,t,\mathbf{M},\mathbf{x}^{\mathrm{known}})$：由显式条件化的扩散模型或采样器给出的一步逆向更新。

Inpainting 只要求前向过程能给出已知区域在时间 $t$ 的状态，并且逆向采样器能从 $t$ 更新到 $t-1$，就可以施加同样的掩码约束：

$$
\mathbf{x}_t \sim q_t(\mathbf{x}_t \mid \mathbf{x}_0)
$$

在 inpainting 中，已知区域在第 $t$ 步的带噪状态记为：

$$
\mathbf{x}_t^{\mathrm{known}} =
\mathbf{M} \odot \operatorname{ForwardDiffusion}(\mathbf{x}_0, t)
$$

实际实现时也可以只对完整 $\mathbf{x}_0$ 加噪后再取已知区域。

## 训练

具体训练目标取决于扩散模型的参数化方式。这里把模型抽象为一个显式条件化的逆向动力学或采样器。它在当前状态 $\mathbf{x}_t$、时间 $t$ 之外，还接收掩码 $\mathbf{M}$ 和已知区域 $\mathbf{x}^{\mathrm{known}}$：

$$
\operatorname{ReverseStep}_\theta(
\mathbf{x}_t,
t,
\mathbf{M},
\mathbf{x}^{\mathrm{known}}
)
$$

其中 $\mathbf{x}^{\mathrm{known}}$ 通常可以取干净条件 $\mathbf{M}\odot\mathbf{x}_0$；如果采样器希望条件区域也处在同一噪声尺度，也可以输入 $\mathbf{x}_t^{\mathrm{known}}$。

模型的作用是在这些条件下产生更接近数据分布的前一时刻状态。训练时通常随机采样掩码，让模型学习“在给定已知区域的情况下恢复未知区域”；损失可以只在待修复区域计算，也可以在全结构上计算，但已知区域不应被当作需要自由生成的目标。

## 采样

通用扩散采样从终点先验 $\mathbf{x}_T \sim p_T$ 开始，沿着离散时间网格逐步生成。一次逆向更新可抽象写作：

$$
\tilde{\mathbf{x}}_{t-1}
\leftarrow
\operatorname{ReverseStep}_\theta(
\mathbf{x}_t,
t,
\mathbf{M},
\mathbf{x}^{\mathrm{known}}
)
$$

即使模型已经显式接收 inpainting 条件，采样时仍然需要在每一步逆向去噪后执行掩码混合：

$$
\hat{\mathbf{x}}_{t-1} :=
\tilde{\mathbf{x}}_{t-1} \odot (\mathbf{1}-\mathbf{M})
+ \mathbf{x}_{t-1}^{\mathrm{known}} \odot \mathbf{M}
$$

这一步的含义是：未知区域使用模型生成结果，已知区域替换为从原始数据前向扩散得到的对应时间步状态。这样既保留了已知条件，又让已知区域在噪声尺度上与当前时间步保持一致，避免直接把干净数据硬塞进带噪状态。

## 另一种 Inpainting 约束：掩码化扩散过程

无论使用哪一种约束方式，模型显式接收的信息量是相同的：掩码、已知条件区域，以及未知区域当前的带噪状态。

上面的做法把 diffusion inpainting 写成“条件化逆向扩散后再用掩码替换”的采样约束。下面描述另一种更结构化的约束方式：**不在每一步事后修正结果，而是在前向加噪、时间输入和训练损失中直接屏蔽已知区域**。

这种方法可以称为 masked diffusion process。它的核心思想是：已知区域不是待生成随机变量，而是始终作为条件上下文存在；只有未知区域参与扩散建模。

给定原始数据 $\mathbf{x}_0 \in \mathbb{R}^d$ 和二值掩码 $\mathbf{M}\in\{0,1\}^d$：

- $M_i=1$ 表示已知区域，应该保持为条件；
- $M_i=0$ 表示未知区域，需要由模型生成。

### 1. 掩码化前向扩散

普通扩散会对所有分量加噪：

$$
\mathbf{x}_t
= \alpha_t \mathbf{x}_0 + \sigma_t \boldsymbol{\epsilon},
\quad
\boldsymbol{\epsilon}\sim \mathcal{N}(\mathbf{0},\mathbf{I})
$$

掩码化扩散只对未知区域加噪：

$$
\mathbf{x}_t
= \mathbf{M}\odot \mathbf{x}_0
+(\mathbf{1}-\mathbf{M})\odot
\left(
\alpha_t \mathbf{x}_0+\sigma_t \boldsymbol{\epsilon}
\right)
$$

等价地，可以把噪声写成：

$$
\boldsymbol{\epsilon}^{\mathrm{mask}}
=
(\mathbf{1}-\mathbf{M})\odot \boldsymbol{\epsilon}
$$

于是已知区域在所有时间步都满足：

$$
\mathbf{M}\odot \mathbf{x}_t
=
\mathbf{M}\odot \mathbf{x}_0
$$

这和“每一步采样后替换已知区域”不同。替换法是在采样轨迹外部施加约束；掩码化扩散则把约束写进了扩散过程本身。

### 2. 掩码化时间输入

如果模型接收统一时间步 $t$，它会默认所有分量都处在同一噪声尺度。对于 inpainting，这并不完全准确：已知区域是干净条件，未知区域才是第 $t$ 步的随机变量。

因此可以把时间步扩展为逐元素时间场：

$$
t_i =
\begin{cases}
0, & M_i=1 \\
t, & M_i=0
\end{cases}
$$

也可以写成向量形式：

$$
\mathbf{t}
=
t\cdot(\mathbf{1}-\mathbf{M})
$$

这里 $t_i=0$ 的含义是：第 $i$ 个分量被视为来自干净条件分布，不需要模型对它做去噪；$t_i=t$ 的分量才需要进行分数估计或逆向更新。
