---
title: 变分自编码器
tags:
  - 机器学习
  - 生成模型
date: 2026-10-29
---

假设数据来自未知分布 $p_{\mathrm{data}}$，目标是用参数模型 $p_\phi$ 逼近它。下文的 $\log$ 表示自然对数。

## 从自编码器到 VAE

自编码器由确定性的编码器和解码器组成。它能把样本重构回来，但只优化重构时，不能保证从预设的简单分布里抽出潜编码后仍得到高质量样本。

变分自编码器（Variational Autoencoder, VAE）给潜空间加上概率结构：先从先验采样潜编码，再由解码器生成数据。重构工具因此成为生成模型。

## 边际似然

极大似然需要边际分布

$$
p_\phi(\mathbf{x})
=
\int p_\phi(\mathbf{x},\mathbf{z})\,d\mathbf{z}
=
\int p_\phi(\mathbf{x}\mid\mathbf{z})\,p(\mathbf{z})\,d\mathbf{z}.
\tag{1}
$$

这个积分通常没有闭式。若潜空间是 $d$ 维，每个维度放 $M$ 个求积节点，全张量网格的函数计算次数是 $\mathcal{O}(M^d)$，随 $d$ 指数增长。直接从先验 $p(\mathbf{z})$ 做蒙特卡洛时，对给定 $\mathbf{x}$ 有效的样本往往很少，估计方差会很大。

于是要先回答：给定观测 $\mathbf{x}$，哪些潜编码 $\mathbf{z}$ 以较高概率产生了它。

## 近似后验

贝叶斯公式给出真实后验

$$
p_\phi(\mathbf{z}\mid\mathbf{x})
=
\frac{p_\phi(\mathbf{x}\mid\mathbf{z})\,p(\mathbf{z})}{p_\phi(\mathbf{x})}.
\tag{2}
$$

分母仍是 (1)，不能直接计算。VAE 用参数为 $\theta$ 的网络给出变分分布，近似这个后验：

$$
q_\theta(\mathbf{z}\mid\mathbf{x})
\approx
p_\phi(\mathbf{z}\mid\mathbf{x}).
\tag{3}
$$

## 证据下界

把 (1) 改写成对 $q_\theta(\mathbf{z}\mid\mathbf{x})$ 的期望。$\log$ 是凹函数，Jensen 不等式给出证据下界（Evidence Lower Bound, ELBO）：

$$
\begin{aligned}
\log p_\phi(\mathbf{x})
&=
\log\int q_\theta(\mathbf{z}\mid\mathbf{x})
\frac{p_\phi(\mathbf{x},\mathbf{z})}{q_\theta(\mathbf{z}\mid\mathbf{x})}\,d\mathbf{z} \\
&=
\log\mathbb{E}_{\mathbf{z}\sim q_\theta(\mathbf{z}\mid\mathbf{x})}
\left[
\frac{p_\phi(\mathbf{x},\mathbf{z})}{q_\theta(\mathbf{z}\mid\mathbf{x})}
\right] \\
&\ge
\mathbb{E}_{\mathbf{z}\sim q_\theta(\mathbf{z}\mid\mathbf{x})}
\left[
\log\frac{p_\phi(\mathbf{x},\mathbf{z})}{q_\theta(\mathbf{z}\mid\mathbf{x})}
\right]
=
\mathcal{L}_{\mathrm{ELBO}}(\theta,\phi;\mathbf{x}).
\end{aligned}
\tag{4}
$$

把联合分布拆成 $p_\phi(\mathbf{x}\mid\mathbf{z})p(\mathbf{z})$，得到重构项与正则项：

$$
\begin{aligned}
\mathcal{L}_{\mathrm{ELBO}}(\theta,\phi;\mathbf{x})
&=
\int q_\theta(\mathbf{z}\mid\mathbf{x})
\log\frac{p_\phi(\mathbf{x}\mid\mathbf{z})\,p(\mathbf{z})}{q_\theta(\mathbf{z}\mid\mathbf{x})}\,d\mathbf{z} \\
&=
\mathbb{E}_{\mathbf{z}\sim q_\theta(\mathbf{z}\mid\mathbf{x})}
[\log p_\phi(\mathbf{x}\mid\mathbf{z})]
-
D_{\mathrm{KL}}\!\left(q_\theta(\mathbf{z}\mid\mathbf{x})\,\middle\|\,p(\mathbf{z})\right).
\end{aligned}
\tag{5}
$$

第一项是重构项，第二项把近似后验拉向先验。训练时最大化数据上的平均 ELBO：

$$
\max_{\theta,\phi}
\mathbb{E}_{\mathbf{x}\sim p_{\mathrm{data}}}
[\mathcal{L}_{\mathrm{ELBO}}(\theta,\phi;\mathbf{x})].
\tag{6}
$$

## 高斯假设与重参数化

标准 VAE 把近似后验取成对角高斯，解码分布取成各向同性高斯：

$$
q_\theta(\mathbf{z}\mid\mathbf{x})
=
\mathcal{N}\!\left(
\mathbf{z};
\boldsymbol{\mu}_\theta(\mathbf{x}),
\mathrm{diag}(\boldsymbol{\sigma}_\theta^2(\mathbf{x}))
\right),
\tag{7}
$$

$$
p_\phi(\mathbf{x}\mid\mathbf{z})
=
\mathcal{N}\!\left(
\mathbf{x};
\boldsymbol{\mu}_\phi(\mathbf{z}),
\sigma^2\mathbf{I}
\right).
\tag{8}
$$

$\sigma>0$ 是预设超参数。先验取标准正态 $p(\mathbf{z})=\mathcal{N}(\mathbf{0},\mathbf{I})$。

重构项要对 $\mathbf{z}\sim q_\theta(\mathbf{z}\mid\mathbf{x})$ 取期望。直接从 $q_\theta$ 抽样时，随机性穿过 $\theta$，梯度传不回编码器。重参数化把随机性放进与参数无关的噪声里：

$$
\mathbf{z}
=
\boldsymbol{\mu}_\theta(\mathbf{x})
+
\boldsymbol{\sigma}_\theta(\mathbf{x})\odot\boldsymbol{\epsilon},
\qquad
\boldsymbol{\epsilon}\sim\mathcal{N}(\mathbf{0},\mathbf{I}).
\tag{9}
$$

$\mathbf{z}$ 对 $\theta$ 可微，重构项可以反向传播。

## 重构项

在 (8) 下，重构项等于负均方误差加常数：

$$
\mathbb{E}_{\mathbf{z}\sim q_\theta(\mathbf{z}\mid\mathbf{x})}
[\log p_\phi(\mathbf{x}\mid\mathbf{z})]
=
-\frac{1}{2\sigma^2}
\mathbb{E}_{\mathbf{z}\sim q_\theta(\mathbf{z}\mid\mathbf{x})}
\left[
\|\mathbf{x}-\boldsymbol{\mu}_\phi(\mathbf{z})\|^2
\right]
+C.
\tag{10}
$$

> **证明.** 设 $\mathbf{x}\in\mathbb{R}^D$。协方差 $\sigma^2\mathbf{I}$ 的行列式是 $|\sigma^2\mathbf{I}|=\sigma^{2D}$，故
>
> $$
> \begin{aligned}
> p_\phi(\mathbf{x}\mid\mathbf{z})
> &=
> (2\pi)^{-D/2}\sigma^{-D}
> \exp\!\left(
> -\frac{1}{2\sigma^2}
> \|\mathbf{x}-\boldsymbol{\mu}_\phi(\mathbf{z})\|^2
> \right), \\
> \log p_\phi(\mathbf{x}\mid\mathbf{z})
> &=
> -\frac{1}{2\sigma^2}
> \|\mathbf{x}-\boldsymbol{\mu}_\phi(\mathbf{z})\|^2
> +C,
> \end{aligned}
> $$
>
> 其中 $C=\log\bigl((2\pi)^{-D/2}\sigma^{-D}\bigr)$ 只依赖 $D$ 与 $\sigma$，与 $\mathbf{z}$ 和网络参数无关。对 $q_\theta(\mathbf{z}\mid\mathbf{x})$ 取期望即得 (10)。$\square$

## 正则项

两个 $d$ 维高斯

$$
p_1(\mathbf{x})=\mathcal{N}(\mathbf{x};\boldsymbol{\mu}_1,\boldsymbol{\Sigma}_1),
\qquad
p_2(\mathbf{x})=\mathcal{N}(\mathbf{x};\boldsymbol{\mu}_2,\boldsymbol{\Sigma}_2)
$$

的 KL 散度有闭式

$$
\begin{aligned}
&D_{\mathrm{KL}}(p_1\|p_2) \\
&\quad=
\frac12\Big(
\log\frac{|\boldsymbol{\Sigma}_2|}{|\boldsymbol{\Sigma}_1|}
+
\operatorname{tr}(\boldsymbol{\Sigma}_2^{-1}\boldsymbol{\Sigma}_1)
+
(\boldsymbol{\mu}_2-\boldsymbol{\mu}_1)^\top
\boldsymbol{\Sigma}_2^{-1}
(\boldsymbol{\mu}_2-\boldsymbol{\mu}_1)
-d
\Big).
\end{aligned}
\tag{11}
$$

训练里的正则项是把 (11) 代入 (7) 与标准正态先验。记 $\boldsymbol{\mu}=\boldsymbol{\mu}_\theta(\mathbf{x})$，$\boldsymbol{\sigma}=\boldsymbol{\sigma}_\theta(\mathbf{x})$，则 $\boldsymbol{\Sigma}_1=\mathrm{diag}(\boldsymbol{\sigma}^2)$，$\boldsymbol{\Sigma}_2=\mathbf{I}$，$\boldsymbol{\mu}_2=\mathbf{0}$。于是 $|\boldsymbol{\Sigma}_2|=1$，$|\boldsymbol{\Sigma}_1|=\prod_i\sigma_i^2$，$\operatorname{tr}(\boldsymbol{\Sigma}_1)=\sum_i\sigma_i^2$，$(\boldsymbol{\mu}_2-\boldsymbol{\mu}_1)^\top(\boldsymbol{\mu}_2-\boldsymbol{\mu}_1)=\|\boldsymbol{\mu}\|^2$，得到

$$
D_{\mathrm{KL}}\!\left(q_\theta(\mathbf{z}\mid\mathbf{x})\,\middle\|\,p(\mathbf{z})\right)
=
\frac12\sum_{i=1}^{d}
\bigl(
\mu_i^2+\sigma_i^2-\log\sigma_i^2-1
\bigr).
\tag{12}
$$

## 最大化 ELBO 等价于最小化联合 KL

记推断联合分布与生成联合分布为

$$
q_\theta(\mathbf{x},\mathbf{z})
=
p_{\mathrm{data}}(\mathbf{x})\,q_\theta(\mathbf{z}\mid\mathbf{x}),
\qquad
p_\phi(\mathbf{x},\mathbf{z})
=
p(\mathbf{z})\,p_\phi(\mathbf{x}\mid\mathbf{z}).
$$

这里 $p_\phi(\mathbf{z})=p(\mathbf{z})$，因为先验抽样不依赖 $\phi$；$q_\theta(\mathbf{x})=p_{\mathrm{data}}(\mathbf{x})$，因为数据抽样不依赖 $\theta$。联合 KL 拆成边际 KL 与期望后验 KL：

$$
\begin{aligned}
&D_{\mathrm{KL}}\!\left(q_\theta(\mathbf{x},\mathbf{z})\,\middle\|\,p_\phi(\mathbf{x},\mathbf{z})\right) \\
&\quad=
D_{\mathrm{KL}}\!\left(p_{\mathrm{data}}(\mathbf{x})\,\middle\|\,p_\phi(\mathbf{x})\right)
+
\mathbb{E}_{\mathbf{x}\sim p_{\mathrm{data}}}
\left[
D_{\mathrm{KL}}\!\left(
q_\theta(\mathbf{z}\mid\mathbf{x})
\,\middle\|\,
p_\phi(\mathbf{z}\mid\mathbf{x})
\right)
\right].
\end{aligned}
\tag{13}
$$

> **证明.** 生成模型同时有分解 $p_\phi(\mathbf{x},\mathbf{z})=p_\phi(\mathbf{x})\,p_\phi(\mathbf{z}\mid\mathbf{x})$。于是
>
> $$
> \begin{aligned}
> &D_{\mathrm{KL}}\!\left(q_\theta(\mathbf{x},\mathbf{z})\,\middle\|\,p_\phi(\mathbf{x},\mathbf{z})\right) \\
> &\quad=
> \iint q_\theta(\mathbf{x},\mathbf{z})
> \log\frac{q_\theta(\mathbf{x},\mathbf{z})}{p_\phi(\mathbf{x},\mathbf{z})}
> \,d\mathbf{z}\,d\mathbf{x} \\
> &\quad=
> \iint q_\theta(\mathbf{x},\mathbf{z})
> \log\frac{p_{\mathrm{data}}(\mathbf{x})\,q_\theta(\mathbf{z}\mid\mathbf{x})}
> {p_\phi(\mathbf{x})\,p_\phi(\mathbf{z}\mid\mathbf{x})}
> \,d\mathbf{z}\,d\mathbf{x} \\
> &\quad=
> \iint q_\theta(\mathbf{x},\mathbf{z})
> \left[
> \log\frac{p_{\mathrm{data}}(\mathbf{x})}{p_\phi(\mathbf{x})}
> +
> \log\frac{q_\theta(\mathbf{z}\mid\mathbf{x})}{p_\phi(\mathbf{z}\mid\mathbf{x})}
> \right]
> \,d\mathbf{z}\,d\mathbf{x}.
> \end{aligned}
> $$
>
> 第一项先对 $\mathbf{z}$ 积分。$\int q_\theta(\mathbf{x},\mathbf{z})\,d\mathbf{z}=p_{\mathrm{data}}(\mathbf{x})$，故
>
> $$
> \iint q_\theta(\mathbf{x},\mathbf{z})
> \log\frac{p_{\mathrm{data}}(\mathbf{x})}{p_\phi(\mathbf{x})}
> \,d\mathbf{z}\,d\mathbf{x}
> =
> D_{\mathrm{KL}}\!\left(p_{\mathrm{data}}(\mathbf{x})\,\middle\|\,p_\phi(\mathbf{x})\right).
> $$
>
> 第二项先把 $q_\theta(\mathbf{x},\mathbf{z})=p_{\mathrm{data}}(\mathbf{x})\,q_\theta(\mathbf{z}\mid\mathbf{x})$ 代入，内层就是条件 KL：
>
> $$
> \begin{aligned}
> &\iint q_\theta(\mathbf{x},\mathbf{z})
> \log\frac{q_\theta(\mathbf{z}\mid\mathbf{x})}{p_\phi(\mathbf{z}\mid\mathbf{x})}
> \,d\mathbf{z}\,d\mathbf{x} \\
> &\quad=
> \mathbb{E}_{\mathbf{x}\sim p_{\mathrm{data}}}
> \left[
> D_{\mathrm{KL}}\!\left(
> q_\theta(\mathbf{z}\mid\mathbf{x})
> \,\middle\|\,
> p_\phi(\mathbf{z}\mid\mathbf{x})
> \right)
> \right].
> \end{aligned}
> $$
>
> 两项相加即得 (13)。$\square$

对数似然与 ELBO 的差就是这个后验 KL：

$$
\log p_\phi(\mathbf{x})
-
\mathcal{L}_{\mathrm{ELBO}}(\theta,\phi;\mathbf{x})
=
D_{\mathrm{KL}}\!\left(
q_\theta(\mathbf{z}\mid\mathbf{x})
\,\middle\|\,
p_\phi(\mathbf{z}\mid\mathbf{x})
\right).
\tag{14}
$$

> **证明.** $\log p_\phi(\mathbf{x})$ 不依赖 $\mathbf{z}$，可以放进对 $q_\theta(\mathbf{z}\mid\mathbf{x})$ 的期望。由 (4) 中 ELBO 的定义，
>
> $$
> \begin{aligned}
> &\log p_\phi(\mathbf{x})
> -
> \mathcal{L}_{\mathrm{ELBO}}(\theta,\phi;\mathbf{x}) \\
> &\quad=
> \mathbb{E}_{\mathbf{z}\sim q_\theta(\mathbf{z}\mid\mathbf{x})}
> \left[
> \log p_\phi(\mathbf{x})
> -
> \log\frac{p_\phi(\mathbf{x},\mathbf{z})}{q_\theta(\mathbf{z}\mid\mathbf{x})}
> \right] \\
> &\quad=
> \mathbb{E}_{\mathbf{z}\sim q_\theta(\mathbf{z}\mid\mathbf{x})}
> \left[
> \log\frac{p_\phi(\mathbf{x})\,q_\theta(\mathbf{z}\mid\mathbf{x})}{p_\phi(\mathbf{x},\mathbf{z})}
> \right] \\
> &\quad=
> \mathbb{E}_{\mathbf{z}\sim q_\theta(\mathbf{z}\mid\mathbf{x})}
> \left[
> \log\frac{q_\theta(\mathbf{z}\mid\mathbf{x})}{p_\phi(\mathbf{z}\mid\mathbf{x})}
> \right] \\
> &\quad=
> D_{\mathrm{KL}}\!\left(
> q_\theta(\mathbf{z}\mid\mathbf{x})
> \,\middle\|\,
> p_\phi(\mathbf{z}\mid\mathbf{x})
> \right).
> \end{aligned}
> $$
>
> 第三步用了 $p_\phi(\mathbf{x},\mathbf{z})=p_\phi(\mathbf{x})\,p_\phi(\mathbf{z}\mid\mathbf{x})$。$\square$

(14) 说明 ELBO 的间隙就是近似后验与真实后验的 KL。$q_\theta(\mathbf{z}\mid\mathbf{x})=p_\phi(\mathbf{z}\mid\mathbf{x})$ 时，下界成为等式。把 (14) 代回 (13)，再展开边际 KL：

$$
\begin{aligned}
&D_{\mathrm{KL}}\!\left(q_\theta(\mathbf{x},\mathbf{z})\,\middle\|\,p_\phi(\mathbf{x},\mathbf{z})\right) \\
&\quad=
D_{\mathrm{KL}}\!\left(p_{\mathrm{data}}(\mathbf{x})\,\middle\|\,p_\phi(\mathbf{x})\right)
+
\mathbb{E}_{\mathbf{x}\sim p_{\mathrm{data}}}
\left[
\log p_\phi(\mathbf{x})
-
\mathcal{L}_{\mathrm{ELBO}}(\theta,\phi;\mathbf{x})
\right] \\
&\quad=
\mathbb{E}_{\mathbf{x}\sim p_{\mathrm{data}}}[\log p_{\mathrm{data}}(\mathbf{x})]
-
\mathbb{E}_{\mathbf{x}\sim p_{\mathrm{data}}}
[\mathcal{L}_{\mathrm{ELBO}}(\theta,\phi;\mathbf{x})].
\end{aligned}
\tag{15}
$$

> **证明.** 由 (13)，左端等于边际 KL 加上期望后验 KL。再用 (14) 把后验 KL 换成 $\log p_\phi(\mathbf{x})-\mathcal{L}_{\mathrm{ELBO}}(\theta,\phi;\mathbf{x})$，得到 (15) 的第一个等号。边际 KL 等于 $\mathbb{E}_{\mathbf{x}\sim p_{\mathrm{data}}}[\log p_{\mathrm{data}}(\mathbf{x})-\log p_\phi(\mathbf{x})]$，其中的 $\mathbb{E}[\log p_\phi(\mathbf{x})]$ 与前一项里的 $\mathbb{E}[\log p_\phi(\mathbf{x})]$ 相消，得到第二个等号。$\square$

(15) 末行的第一项是真实数据分布的负熵，与 $(\theta,\phi)$ 无关。因此

$$
\max_{\theta,\phi}
\mathbb{E}_{\mathbf{x}\sim p_{\mathrm{data}}}
[\mathcal{L}_{\mathrm{ELBO}}(\theta,\phi;\mathbf{x})]
\quad\Longleftrightarrow\quad
\min_{\theta,\phi}
D_{\mathrm{KL}}\!\left(
q_\theta(\mathbf{x},\mathbf{z})
\,\middle\|\,
p_\phi(\mathbf{x},\mathbf{z})
\right).
\tag{16}
$$

## 表达力与模糊化

### 对角高斯是单峰的

(7) 把近似后验限制在对角高斯里。网络无论多深，输出的都是一个单峰高斯。真实后验 $p_\phi(\mathbf{z}\mid\mathbf{x})$ 多峰时，这个变分族拟合不上，ELBO 变松，推断变弱。加深网络改变不了变分族，需要更丰富的近似分布。

### 最优解码器是条件均值

高斯解码器以均方误差为重构目标时，对固定的编码器，最优解码均值是近似后验下 $\mathbf{x}$ 的条件期望。同一 $\mathbf{z}$ 对应多个 $\mathbf{x}$ 时，这个平均值会把生成结果模糊化：

$$
\boldsymbol{\mu}^*(\mathbf{z})
=
\frac{
\mathbb{E}_{\mathbf{x}\sim p_{\mathrm{data}}}
[q_\theta(\mathbf{z}\mid\mathbf{x})\,\mathbf{x}]
}{
\mathbb{E}_{\mathbf{x}\sim p_{\mathrm{data}}}
[q_\theta(\mathbf{z}\mid\mathbf{x})]
}.
\tag{17}
$$

> **证明.** 设编码器已经给定。MSE 目标是
>
> $$
> \begin{aligned}
> &\min_{\boldsymbol{\mu}}
> \mathbb{E}_{\mathbf{x}\sim p_{\mathrm{data}}}
> \left[
> \mathbb{E}_{\mathbf{z}\sim q_\theta(\mathbf{z}\mid\mathbf{x})}
> \left[
> \|\mathbf{x}-\boldsymbol{\mu}(\mathbf{z})\|^2
> \right]
> \right] \\
> &\quad=
> \min_{\boldsymbol{\mu}}
> \int q_\theta(\mathbf{z})
> \left[
> \int q_\theta(\mathbf{x}\mid\mathbf{z})
> \|\mathbf{x}-\boldsymbol{\mu}(\mathbf{z})\|^2
> \,d\mathbf{x}
> \right]
> d\mathbf{z}.
> \end{aligned}
> $$
>
> 外层对 $\mathbf{z}$ 积分，内层可以逐点最小化。固定 $\mathbf{z}$，记
>
> $$
> J(\boldsymbol{\mu})
> =
> \int q_\theta(\mathbf{x}\mid\mathbf{z})
> \|\mathbf{x}-\boldsymbol{\mu}\|^2
> \,d\mathbf{x}.
> $$
>
> 对 $\boldsymbol{\mu}$ 求导：
>
> $$
> \nabla_{\boldsymbol{\mu}} J
> =
> -2\int q_\theta(\mathbf{x}\mid\mathbf{z})(\mathbf{x}-\boldsymbol{\mu})\,d\mathbf{x}.
> $$
>
> 令梯度为零，得到
>
> $$
> \boldsymbol{\mu}^*(\mathbf{z})
> =
> \int q_\theta(\mathbf{x}\mid\mathbf{z})\,\mathbf{x}\,d\mathbf{x}
> =
> \mathbb{E}_{\mathbf{x}\sim q_\theta(\mathbf{x}\mid\mathbf{z})}[\mathbf{x}].
> $$
>
> 由 $q_\theta(\mathbf{x},\mathbf{z})=p_{\mathrm{data}}(\mathbf{x})\,q_\theta(\mathbf{z}\mid\mathbf{x})$，
>
> $$
> q_\theta(\mathbf{x}\mid\mathbf{z})
> =
> \frac{q_\theta(\mathbf{z}\mid\mathbf{x})\,p_{\mathrm{data}}(\mathbf{x})}{q_\theta(\mathbf{z})},
> \qquad
> q_\theta(\mathbf{z})
> =
> \mathbb{E}_{\mathbf{x}\sim p_{\mathrm{data}}}[q_\theta(\mathbf{z}\mid\mathbf{x})].
> $$
>
> 代回条件期望：
>
> $$
> \boldsymbol{\mu}^*(\mathbf{z})
> =
> \frac{1}{q_\theta(\mathbf{z})}
> \int q_\theta(\mathbf{z}\mid\mathbf{x})\,\mathbf{x}\,p_{\mathrm{data}}(\mathbf{x})\,d\mathbf{x}
> =
> \frac{
> \mathbb{E}_{\mathbf{x}\sim p_{\mathrm{data}}}
> [q_\theta(\mathbf{z}\mid\mathbf{x})\,\mathbf{x}]
> }{
> \mathbb{E}_{\mathbf{x}\sim p_{\mathrm{data}}}
> [q_\theta(\mathbf{z}\mid\mathbf{x})]
> }.
> $$
>
> 这就是 (17)。$\square$

## KL 系数

实践中常把 ELBO 改成重构项与 KL 的加权和，也就是 $\beta$-VAE：

$$
\mathcal{L}_\beta(\theta,\phi;\mathbf{x})
=
-\mathbb{E}_{\mathbf{z}\sim q_\theta(\mathbf{z}\mid\mathbf{x})}
[\log p_\phi(\mathbf{x}\mid\mathbf{z})]
+
\beta\,
D_{\mathrm{KL}}\!\left(q_\theta(\mathbf{z}\mid\mathbf{x})\,\middle\|\,p(\mathbf{z})\right).
\tag{18}
$$

最小化 (18) 时，$\beta=1$ 对应标准 ELBO 的负值。$\beta$ 调节训练稳定性、潜空间连续性，以及生成与重构的取舍。

### $\beta\to 0$

$\beta\to 0$ 时 KL 惩罚消失，目标退化为纯重构，模型回到普通自编码器。

重参数化 (9) 里的噪声只会增大重构误差。没有 KL 约束时，最优编码器把质量全部放在重构似然最大的一点：

$$
q_\theta(\mathbf{z}\mid\mathbf{x})
\to
\delta\!\left(\mathbf{z}-\mathbf{z}^*(\mathbf{x})\right),
\qquad
\mathbf{z}^*(\mathbf{x})
=
\operatorname*{arg\,max}_{\mathbf{z}}
\log p_\phi(\mathbf{x}\mid\mathbf{z}).
\tag{19}
$$

也就是 $\boldsymbol{\sigma}_\theta^2(\mathbf{x})\to\mathbf{0}$。各样本的后验变成互不重叠的点质量，编码落在孤立流形上，流形之间出现空洞。重构可以很清晰，但从先验 $p(\mathbf{z})$ 采样容易掉进这些空洞。

### KL 主导

$\beta$ 较大时，KL 项主导训练。它在数据上的期望可以拆成互信息与聚合后验 KL：

$$
\begin{aligned}
&\mathbb{E}_{\mathbf{x}\sim p_{\mathrm{data}}}
\left[
D_{\mathrm{KL}}\!\left(q_\theta(\mathbf{z}\mid\mathbf{x})\,\middle\|\,p(\mathbf{z})\right)
\right] \\
&\quad=
\mathcal{I}_q(\mathbf{x};\mathbf{z})
+
D_{\mathrm{KL}}\!\left(q_\theta(\mathbf{z})\,\middle\|\,p(\mathbf{z})\right).
\end{aligned}
\tag{20}
$$

聚合后验是 $q_\theta(\mathbf{z})=\int p_{\mathrm{data}}(\mathbf{x})\,q_\theta(\mathbf{z}\mid\mathbf{x})\,d\mathbf{x}$。

> **证明.** 在被积函数里插入 $q_\theta(\mathbf{z})/q_\theta(\mathbf{z})$：
>
> $$
> \begin{aligned}
> &\mathbb{E}_{\mathbf{x}\sim p_{\mathrm{data}}}
> \left[
> D_{\mathrm{KL}}\!\left(q_\theta(\mathbf{z}\mid\mathbf{x})\,\middle\|\,p(\mathbf{z})\right)
> \right] \\
> &\quad=
> \int p_{\mathrm{data}}(\mathbf{x})
> \int q_\theta(\mathbf{z}\mid\mathbf{x})
> \log\frac{q_\theta(\mathbf{z}\mid\mathbf{x})}{p(\mathbf{z})}
> \,d\mathbf{z}\,d\mathbf{x} \\
> &\quad=
> \int p_{\mathrm{data}}(\mathbf{x})
> \int q_\theta(\mathbf{z}\mid\mathbf{x})
> \log\frac{q_\theta(\mathbf{z}\mid\mathbf{x})}{q_\theta(\mathbf{z})}
> \,d\mathbf{z}\,d\mathbf{x} \\
> &\qquad+
> \int p_{\mathrm{data}}(\mathbf{x})
> \int q_\theta(\mathbf{z}\mid\mathbf{x})
> \log\frac{q_\theta(\mathbf{z})}{p(\mathbf{z})}
> \,d\mathbf{z}\,d\mathbf{x}.
> \end{aligned}
> $$
>
> 第一项就是 $\mathbb{E}_{\mathbf{x}\sim p_{\mathrm{data}}}[D_{\mathrm{KL}}(q_\theta(\mathbf{z}\mid\mathbf{x})\|q_\theta(\mathbf{z}))]$，即 $\mathcal{I}_q(\mathbf{x};\mathbf{z})$。第二项交换积分顺序，内层 $\int p_{\mathrm{data}}(\mathbf{x})\,q_\theta(\mathbf{z}\mid\mathbf{x})\,d\mathbf{x}=q_\theta(\mathbf{z})$，得到 $D_{\mathrm{KL}}(q_\theta(\mathbf{z})\|p(\mathbf{z}))$。$\square$

$\mathcal{I}_q(\mathbf{x};\mathbf{z})$ 是 $\mathbf{z}$ 携带的关于 $\mathbf{x}$ 的信息，生成时希望它大；$D_{\mathrm{KL}}(q_\theta(\mathbf{z})\|p(\mathbf{z}))$ 是潜空间整体形状相对先验的偏差，希望它小。互信息过小时，$\mathbf{z}$ 几乎不含 $\mathbf{x}$ 的信息，潜编码难以控制生成。

### 后验崩溃

若进一步 $q_\theta(\mathbf{z}\mid\mathbf{x})\approx p(\mathbf{z})$，近似后验与 $\mathbf{x}$ 无关，则 (17) 的分子分母都多出一个与 $\mathbf{x}$ 无关的 $p(\mathbf{z})$：

$$
\boldsymbol{\mu}^*(\mathbf{z})
=
\frac{
p(\mathbf{z})\,
\mathbb{E}_{\mathbf{x}\sim p_{\mathrm{data}}}[\mathbf{x}]
}{
p(\mathbf{z})\,
\mathbb{E}_{\mathbf{x}\sim p_{\mathrm{data}}}[1]
}
=
\mathbb{E}_{\mathbf{x}\sim p_{\mathrm{data}}}[\mathbf{x}].
\tag{21}
$$

对任意 $\mathbf{z}$，最优输出都是全体训练样本的平均值，也就是一张与 $\mathbf{z}$ 无关的全局均值图。