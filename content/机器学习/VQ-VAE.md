---
title: VQ-VAE
tags:
  - 机器学习
  - 生成模型
date: 2026-10-30
---

## 前置

- [[机器学习/VAE|变分自编码器]]
- [[机器学习/Straight-Through-Estimator|Straight-Through Estimator]]

VQ-VAE（Vector Quantized Variational Autoencoder，向量量化变分自编码器）把输入编码成离散符号，再用这些符号重建输入。图像、音频和蛋白质结构都可以写成离散序列，交给 Transformer 一类模型继续建模。

## 离散码本

编码器 $E_\theta$ 把输入 $x$ 映成连续向量

$$
z_e=E_\theta(x).
\tag{1}
$$

向量量化在码本里取与 $z_e$ 最近的向量 $z_q$。解码器 $D_\phi$ 只接收 $z_q$，

$$
\hat{x}=D_\phi(z_q).
\tag{2}
$$

数据流是 $x\to z_e\to z_q\to\hat{x}$。普通自编码器把 $z_e$ 直接送进解码器。VQ-VAE 在中间插入可学习的离散码本，解码器看到的是码本向量。

## 最近邻量化

码本含 $K$ 个可学习向量

$$
\mathcal{E}=\{e_1,e_2,\ldots,e_K\}.
\tag{3}
$$

量化索引取欧氏距离最小的码字，量化结果就是该码字：

$$
k^*=\arg\min_k\|z_e-e_k\|_2^2,
\qquad
z_q=e_{k^*}.
\tag{4}
$$

$K=512$ 时，每个编码位置保存一个取值于 $\{0,1,\ldots,511\}$ 的整数。连续向量由此变成离散 token 序列。索引是离散符号，重建损失经第 4 节的直通估计回到编码器。

## 训练目标

经典 VQ-VAE 的损失是重建、码本与承诺三项之和。$\operatorname{sg}[\cdot]$ 表示停止梯度，$\beta$ 是承诺损失的权重。

$$
\begin{aligned}
\mathcal{L}
&=
\underbrace{\|x-\hat{x}\|^2}_{\text{重建损失}}
+
\underbrace{\|\operatorname{sg}[z_e]-z_q\|^2}_{\text{码本损失}}
+
\underbrace{\beta\|z_e-\operatorname{sg}[z_q]\|^2}_{\text{承诺损失}}.
\end{aligned}
\tag{5}
$$

重建损失拟合 $x$，并经直通估计更新编码器与解码器。码本损失只更新被选中的码本向量，把它拉向 $z_e$。承诺损失只更新编码器，把 $z_e$ 拉向所选码本向量。

## 直通梯度

(4) 的 $\arg\min$ 是离散选择。VQ-VAE 用 [[机器学习/Straight-Through-Estimator|Straight-Through Estimator]]：前向把量化结果交给解码器，反向把量化当成恒等映射。

$$
z_{\mathrm{st}}=z_e+\operatorname{sg}[z_q-z_e],
\qquad
\hat{x}=D_\phi(z_{\mathrm{st}}).
\tag{6}
$$

前向时 $z_{\mathrm{st}}=z_q$。反向时停止梯度截断括号内的项，重建损失对 $z_e$ 的梯度等于对 $z_{\mathrm{st}}$ 的梯度。对应实现是

```python
z_st = z_e + (z_q - z_e).detach()
x_hat = decoder(z_st)
```
