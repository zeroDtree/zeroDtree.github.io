---
title: EDM
aliases:
  - /随机过程/diffusion/EDM
  - /机器学习/diffusion/EDM
---

## 前置

- [[随机过程/扩散模型/分数匹配]]

## 1. EDM 的扩散参数化

EDM（Elucidating the Design Space of Diffusion-Based Generative Models）
[@karras2022elucidating] 把扩散过程、网络预条件、损失权重、训练噪声分布和采样日程解耦。

考虑 $s(t)>0$、$\sigma(t)\ge0$ 的参数化

$$
\mathbf X_t
=s(t)\mathbf X_0
+s(t)\sigma(t)\boldsymbol\epsilon,
\qquad
\boldsymbol\epsilon\sim\mathcal N(\mathbf0,\mathbf I).
$$

令

$$
\mathbf u_t:=\frac{\mathbf X_t}{s(t)}
=\mathbf X_0+\sigma(t)\boldsymbol\epsilon.
$$

若 $p(\mathbf u;\sigma)$ 是 $\mathbf X_0+\sigma\boldsymbol\epsilon$ 的密度，则

$$
p_t(\mathbf x)
=s(t)^{-d}
p\!\left(\frac{\mathbf x}{s(t)};\sigma(t)\right)
$$

以及

$$
\nabla_{\mathbf x}\log p_t(\mathbf x)
=\frac1{s(t)}
\nabla_{\mathbf u}\log p(\mathbf u;\sigma(t))
\bigg|_{\mathbf u=\mathbf x/s(t)}.
$$

条件高斯分数为

$$
\nabla_{\mathbf x}
\log p_{0t}(\mathbf x\mid\mathbf x_0)
=
\frac1{s(t)\sigma(t)^2}
\left(
\mathbf x_0-\frac{\mathbf x}{s(t)}
\right).
$$

若去噪器

$$
D_\theta(\mathbf u,\sigma)
\approx
\mathbb E[\mathbf X_0\mid
\mathbf X_0+\sigma\boldsymbol\epsilon=\mathbf u],
$$

则 Tweedie 公式给出

$$
\nabla_{\mathbf u}\log p(\mathbf u;\sigma)
\approx
\frac{D_\theta(\mathbf u,\sigma)-\mathbf u}{\sigma^2}.
$$

## 2. EDM 的 probability-flow ODE

由线性高斯扩散的一般结论，

$$
\boxed{
\mathrm d\mathbf X_t
=
\left[
\frac{s'(t)}{s(t)}\mathbf X_t
-s(t)\sigma(t)\sigma'(t)
\nabla_{\mathbf u}\log p(\mathbf u;\sigma(t))
\bigg|_{\mathbf u=\mathbf X_t/s(t)}
\right]\mathrm dt
}.
$$

代入去噪器后，

$$
\boxed{
\frac{\mathrm d\mathbf X_t}{\mathrm dt}
=
\left(
\frac{s'(t)}{s(t)}
+\frac{\sigma'(t)}{\sigma(t)}
\right)\mathbf X_t
-
s(t)\frac{\sigma'(t)}{\sigma(t)}
D_\theta\!\left(
\frac{\mathbf X_t}{s(t)},\sigma(t)
\right)
}.
$$

这对应 EDM 论文的式 (4)。EDM 常取

$$
s(t)\equiv1,
$$

于是

$$
\frac{\mathrm d\mathbf X_t}{\mathrm dt}
=
\frac{\sigma'(t)}{\sigma(t)}
\left[
\mathbf X_t-D_\theta(\mathbf X_t,\sigma(t))
\right].
$$

再取 $\sigma(t)=t>0$，并定义网络分数

$$
\mathbf s_\theta(\mathbf x,t)
:=\frac{D_\theta(\mathbf x,t)-\mathbf x}{t^2},
$$

则

$$
\boxed{
\frac{\mathrm d\mathbf X_t}{\mathrm dt}
=
\frac{
\mathbf X_t-D_\theta(\mathbf X_t,t)}
t
=-t\,\mathbf s_\theta(\mathbf X_t,t)
}.
$$

采样时沿噪声尺度从大到小积分，通常使用 Euler 或二阶 Heun 修正。

## 3. 去噪器预条件

EDM 不让主网络直接承担所有尺度变化，而定义

$$
\boxed{
D_\theta(\mathbf x,\sigma)
=
c_{\mathrm{skip}}(\sigma)\mathbf x
+
c_{\mathrm{out}}(\sigma)
F_\theta\!\left(
c_{\mathrm{in}}(\sigma)\mathbf x,
c_{\mathrm{noise}}(\sigma)
\right)
}.
$$

四个系数分别负责：

- $c_{\mathrm{in}}$：把网络输入缩放到近似单位方差；
- $c_{\mathrm{skip}}$：提供随噪声变化的线性去噪基线；
- $c_{\mathrm{out}}$：把网络输出恢复到合适的残差尺度；
- $c_{\mathrm{noise}}$：把噪声标准差编码为网络条件。

设干净数据 $\mathbf y$ 零均值、每个分量方差
$\sigma_{\mathrm{data}}^2$，噪声
$\mathbf n\sim\mathcal N(\mathbf0,\sigma^2\mathbf I)$ 与数据不相关，并令

$$
\mathbf x=\mathbf y+\mathbf n.
$$

EDM 的系数为

$$
\boxed{
c_{\mathrm{skip}}(\sigma)
=
\frac{\sigma_{\mathrm{data}}^2}
{\sigma^2+\sigma_{\mathrm{data}}^2}
},
$$

$$
\boxed{
c_{\mathrm{out}}(\sigma)
=
\frac{\sigma\sigma_{\mathrm{data}}}
{\sqrt{\sigma^2+\sigma_{\mathrm{data}}^2}}
},
$$

$$
\boxed{
c_{\mathrm{in}}(\sigma)
=
\frac1{\sqrt{\sigma^2+\sigma_{\mathrm{data}}^2}},
\qquad
c_{\mathrm{noise}}(\sigma)
=\frac14\log\sigma
}.
$$

### 3.1 输入和输出尺度

因为

$$
\operatorname{Var}(x_j)
=\sigma_{\mathrm{data}}^2+\sigma^2,
$$

$c_{\mathrm{in}}$ 使输入每个分量具有近似单位方差。

去掉 skip 后，网络要预测的目标是

$$
\mathbf r
=
\frac{
\mathbf y-c_{\mathrm{skip}}\mathbf x}
{c_{\mathrm{out}}}.
$$

用下节得到的 $c_{\mathrm{skip}}$ 计算，

$$
\operatorname{Var}
(\mathbf y-c_{\mathrm{skip}}\mathbf x)
=
\frac{
\sigma^2\sigma_{\mathrm{data}}^2}
{\sigma^2+\sigma_{\mathrm{data}}^2},
$$

其标准差正是 $c_{\mathrm{out}}$，所以网络目标在各噪声级保持近似单位尺度。

### 3.2 $c_{\mathrm{skip}}$ 的 LMMSE 推导

在标量线性估计族

$$
\widehat{\mathbf y}=a\mathbf x
$$

中最小化

$$
J(a)
=\mathbb E\|\mathbf y-a\mathbf x\|_2^2.
$$

求导并令零：

$$
\begin{aligned}
J'(a)
&=-2\mathbb E[\mathbf y^\top\mathbf x]
+2a\mathbb E[\mathbf x^\top\mathbf x]=0,\\
a^\star
&=
\frac{\mathbb E[\mathbf y^\top\mathbf x]}
{\mathbb E[\mathbf x^\top\mathbf x]}.
\end{aligned}
$$

由 $\mathbf x=\mathbf y+\mathbf n$ 及不相关性，

$$
\mathbb E[\mathbf y^\top\mathbf x]
=d\sigma_{\mathrm{data}}^2,
$$

$$
\mathbb E[\mathbf x^\top\mathbf x]
=d(\sigma_{\mathrm{data}}^2+\sigma^2).
$$

因此

$$
a^\star
=
\frac{\sigma_{\mathrm{data}}^2}
{\sigma_{\mathrm{data}}^2+\sigma^2}
=c_{\mathrm{skip}}(\sigma).
$$

所以当主网络输出为零时，skip 分支已经是该各向同性标量线性类中的 LMMSE 估计。它不声称对任意非高斯数据都是完整 MMSE 后验均值；非线性残差由网络学习。

## 4. 训练目标与权重

EDM 的去噪损失为

$$
\mathcal L
=
\mathbb E_{\sigma,\mathbf y,\mathbf n}
\left[
\lambda(\sigma)
\left\|
D_\theta(\mathbf y+\mathbf n,\sigma)
-\mathbf y
\right\|_2^2
\right],
\qquad
\mathbf n\sim\mathcal N(\mathbf0,\sigma^2\mathbf I).
$$

选择

$$
\boxed{
\lambda(\sigma)
=\frac1{c_{\mathrm{out}}(\sigma)^2}
=
\frac{\sigma^2+\sigma_{\mathrm{data}}^2}
{\sigma^2\sigma_{\mathrm{data}}^2}
}
$$

后，改写成网络输出空间：

$$
\begin{aligned}
\mathcal L
=
\mathbb E\Bigg[
&\lambda(\sigma)c_{\mathrm{out}}(\sigma)^2\\
&\cdot
\left\|
F_\theta(
c_{\mathrm{in}}\mathbf x,c_{\mathrm{noise}})
-
\frac{
\mathbf y-c_{\mathrm{skip}}\mathbf x}
{c_{\mathrm{out}}}
\right\|_2^2
\Bigg].
\end{aligned}
$$

有效前因子
$\lambda c_{\mathrm{out}}^2=1$，同时目标方差也被归一化，从而减弱噪声尺度造成的训练失衡。

## 5. 采样噪声日程

取 $N$ 个正噪声级，按采样方向从
$\sigma_{\max}$ 降到 $\sigma_{\min}$：

$$
\boxed{
\sigma_i
=
\left[
\sigma_{\max}^{1/\rho}
+\frac{i}{N-1}
\left(
\sigma_{\min}^{1/\rho}
-\sigma_{\max}^{1/\rho}
\right)
\right]^\rho,
\quad i=0,\ldots,N-1
}.
$$

再附加

$$
\sigma_N=0.
$$

于是

$$
\sigma_0=\sigma_{\max}
>\cdots>
\sigma_{N-1}=\sigma_{\min}
>\sigma_N=0.
$$

$\rho$ 控制步数在噪声尺度上的分配；EDM 图像实验常取
$\rho=7$，RFD3 [@butcher2025novo] 实现也取 $7$。

> **原图 caption：EDM 的时间步设计。**  
> 图意是沿
> $\sigma_{\max}\to\sigma_{\min}\to0$
> 反向积分；上式明确了数组方向，避免把 $\sigma_0=0$ 与采样起点混在一起。

## 6. $\sigma_{\mathrm{data}}$ 的含义

$\sigma_{\mathrm{data}}$ 是用于预条件的**典型数据标准差尺度**。在各维近似同尺度时，可取训练集按分量计算的经验 RMS/标准差并汇总为标量；它不是由数据取值区间唯一决定的常数。

若像素被归一化到 $[-1,1]$：

- 若真是均匀分布，标准差为
  $$
  \sqrt{\frac{(1-(-1))^2}{12}}
  =\frac1{\sqrt3}\approx0.577;
  $$
- “约 $95\%$ 数据落在 $\pm2\sigma$”的正态经验会给出
  $\sigma_{\mathrm{data}}\approx0.5$，但这只是尺度启发，不是由区间推出的定理。

EDM 图像设置常用

$$
\sigma_{\mathrm{data}}=0.5.
$$

对蛋白质坐标等不在 $[-1,1]$ 的数据，应根据实际数据尺度估计，而不是照搬 $0.5$。

## 7. 训练时的 lognormal 噪声采样

EDM 令

$$
\log\sigma
\sim
\mathcal N(P_{\mathrm{mean}},P_{\mathrm{std}}^2),
$$

等价于

$$
\sigma
=
\exp(
P_{\mathrm{mean}}+P_{\mathrm{std}}\epsilon),
\qquad
\epsilon\sim\mathcal N(0,1).
$$

这里

$$
\operatorname{median}(\sigma)
=e^{P_{\mathrm{mean}}},
$$

而均值为

$$
\mathbb E[\sigma]
=
\exp\!\left(
P_{\mathrm{mean}}
+\frac12P_{\mathrm{std}}^2
\right).
$$

因此 $e^{P_{\mathrm{mean}}}$ 应称为**中位噪声尺度**，不是均值或“精修尺度”。

EDM 图像参数

$$
P_{\mathrm{mean}}=-1.2,
\qquad
P_{\mathrm{std}}=1.2
$$

对应：

- $\log\sigma$ 落在均值 $\pm1$ 个标准差时，
  $\sigma\in[e^{-2.4},e^0]\approx[0.0907,1]$；
- 落在 $\pm2$ 个标准差时，
  $\sigma\in[e^{-3.6},e^{1.2}]\approx[0.0273,3.32]$。

来源中的 RFD3 参数

$$
P_{\mathrm{mean}}=-1.2,
\qquad
P_{\mathrm{std}}=1.5
$$

对应：

- $\pm1$ 个标准差：
  $\sigma\in[e^{-2.7},e^{0.3}]
  \approx[0.0672,1.35]$；
- $\pm2$ 个标准差：
  $\sigma\in[e^{-4.2},e^{1.8}]
  \approx[0.0150,6.05]$。

这些区间不是 lognormal 分布的支持集或硬截断“范围”：分布支持是
$(0,\infty)$。它们分别对应正态变量约 $68.27\%$ 与 $95.45\%$ 的中心概率区间。

若实现采用

$$
\sigma
=\sigma_{\mathrm{data}}
\exp(
P_{\mathrm{mean}}+P_{\mathrm{std}}\epsilon),
$$

则所有分位数整体乘以 $\sigma_{\mathrm{data}}$，适合把无量纲日程映射到非图像数据的物理尺度；这与原始 EDM 不带该乘子时的参数命名应分开记录。
