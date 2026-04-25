---
title: RePaint
---

## 前置

- [[机器学习/diffusion-inpainting(1)]]

## RePaint

RePaint 的核心思想是在每个逆向时间步内多次执行「去噪 - 掩码混合 - 重新加噪」，让未知区域有更多机会与已知区域协调。

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
