---
title: Diffusion Inpainting
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

其中 $\mathbf{x}_0^{\mathrm{known}}$ 由掩码 $\mathbf{m}$ 指定，$\mathbf{x}_0^{\mathrm{unknown}}$ 是待生成的区域。关键约束是：逆向扩散每一步都只能改变未知区域，已知区域必须与前向扩散得到的对应时间步状态一致。

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
- $\operatorname{ReverseStep}_\theta(\mathbf{x}_t,t)$：由扩散模型或采样器给出的一步逆向更新。

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

RePaint 的一个重要特点是：如果已有在完整数据上训练好的无条件扩散模型，通常不需要为了 inpainting 重新训练模型。训练阶段仍然学习完整数据分布上的去噪、生成或分数估计能力，掩码约束主要在采样阶段施加。

具体训练目标取决于扩散模型的参数化方式。可以把模型抽象为一个学习到的逆向动力学或采样器：

$$
\operatorname{ReverseStep}_\theta(\mathbf{x}_t,t)
$$

它的作用是在给定当前状态 $\mathbf{x}_t$ 和时间 $t$ 时，产生更接近数据分布的前一时刻状态。

如果希望模型显式感知 inpainting 条件，也可以将掩码和已知区域作为额外输入，例如：

$$
\operatorname{ReverseStep}_\theta(\mathbf{x}_t,t,\mathbf{M},\mathbf{M}\odot\mathbf{x}_t)
$$

这时训练时通常需要随机采样掩码，并只在待修复区域或全结构上计算相应的训练损失。若目标是复现 RePaint，则采样阶段的掩码混合已经足够表达已知区域约束，不依赖某个特定的训练目标。

## 采样

通用扩散采样从终点先验 $\mathbf{x}_T \sim p_T$ 开始，沿着离散时间网格逐步生成。一次逆向更新可抽象写作：

$$
\tilde{\mathbf{x}}_{t-1}
\leftarrow
\operatorname{ReverseStep}_\theta(\mathbf{x}_t,t)
$$

对于 inpainting，每一步逆向去噪后都要执行掩码混合：

$$
\hat{\mathbf{x}}_{t-1} :=
\tilde{\mathbf{x}}_{t-1} \odot (\mathbf{1}-\mathbf{M})
+ \mathbf{x}_{t-1}^{\mathrm{known}} \odot \mathbf{M}
$$

这一步的含义是：未知区域使用模型生成结果，已知区域替换为从原始数据前向扩散得到的对应时间步状态。这样既保留了已知条件，又让已知区域在噪声尺度上与当前时间步保持一致，避免直接把干净数据硬塞进带噪状态。

## RePaint

本文采用 Lugmayr 等人在 RePaint 中提出的算法进行采样。RePaint 的核心思想是在每个逆向时间步内多次执行「去噪 - 掩码混合 - 重新加噪」，让未知区域有更多机会与已知区域协调。

给定原始数据 $\mathbf{x}_0 \in \mathbb{R}^d$ 和掩码 $\mathbf{M} \in \{0,1\}^d$，其中掩码值为 $1$ 的位置表示已知区域，值为 $0$ 的位置表示未知区域。算法流程如下：

首先，对原始数据执行前向扩散并取出已知区域，得到每个时间步的带噪状态 $\{\mathbf{x}_t^{\mathrm{known}}\}_{t=0}^T$。然后从终点先验 $p_T$ 初始化未知区域，并将已知区域替换为 $\mathbf{x}_T^{\mathrm{known}}$。在每一步去噪后，通过掩码混合恢复已知区域的对应带噪状态：

$$
\hat{\mathbf{x}}_{t-1} :=
\hat{\mathbf{x}}_{t-1} \odot (\mathbf{1}-\mathbf{M})
+ \mathbf{x}_{t-1}^{\mathrm{known}} \odot \mathbf{M}
$$

如果当前 repainting 轮次还没有结束，则再将混合后的样本从 $t-1$ 重新加噪到 $t$，继续进行下一轮局部修正。

### 算法

完整流程如下：

**RePaint inpainting 采样算法**

**输入**：原始数据 $\mathbf{x}_0 \in \mathbb{R}^d$，已知区域掩码 $\mathbf{M} \in \{0,1\}^d$，逆向采样器 $\operatorname{ReverseStep}_\theta$，前向扩散算子，终点先验 $p_T$，总时间步数 $T$，repainting 次数 $u$

**输出**：修复后的数据 $\hat{\mathbf{x}}_0$

1. 预计算已知区域在各时间步的前向扩散状态：
   $$
   \mathbf{x}_t^{\mathrm{known}} \leftarrow
   \operatorname{ForwardDiffusion}(\mathbf{x}_0, t) \odot \mathbf{M},
   \quad t=0,1,\ldots,T
   $$
2. 未知区域从终点先验开始，已知区域使用第 $T$ 步带噪状态：
   $$
   \mathbf{z}_T \sim p_T
   $$
   $$
   \hat{\mathbf{x}}_T \leftarrow
   \mathbf{z}_T \odot (\mathbf{1}-\mathbf{M}) +
   \mathbf{x}_T^{\mathrm{known}} \odot \mathbf{M}
   $$
3. 对 $t=T,T-1,\ldots,1$ 执行逆向去噪。对每个 $t$，再对 $i=1,2,\ldots,u$ 执行 repainting：

   $$
   \hat{\mathbf{x}}_{t-1} \leftarrow
   \operatorname{ReverseStep}_\theta(\hat{\mathbf{x}}_t, t)
   $$

   $$
   \hat{\mathbf{x}}_{t-1} \leftarrow
   \hat{\mathbf{x}}_{t-1}\odot(\mathbf{1}-\mathbf{M}) +
   \mathbf{x}_{t-1}^{\mathrm{known}}\odot\mathbf{M}
   $$

   若 $i<u$ 且 $t>1$，则重新加噪：

   $$
   \hat{\mathbf{x}}_t \leftarrow
   \operatorname{ForwardStep}(\hat{\mathbf{x}}_{t-1}, t)
   $$

4. 返回 $\hat{\mathbf{x}}_0$。

### 注意事项

- 掩码必须与数据形状一致；如果原始掩码只在较粗粒度上定义，需要先广播到每个被扩散的分量。
- 已知区域在中间时间步不应恢复为干净的 $\mathbf{x}_0$，而应恢复为对应时间步的 $\mathbf{x}_t^{\mathrm{known}}$。
- 对连续时间 SDE/ODE 扩散模型，可以把 $t=0,\ldots,T$ 理解为数值求解器选定的离散时间网格。
- repainting 次数 $u$ 控制局部协调强度。较大的 $u$ 通常能改善已知区域和未知区域的衔接，但会线性增加采样开销。
- 如果数据在训练前做了归一化、中心化、裁剪或坐标变换，inpainting 采样时必须使用同一套预处理和反变换。
