---
title: 神经常微分方程：连续归一化流与瞬时换元
tags:
  - 机器学习
  - 生成模型
date: 2026-11-25
---

## 前置

- [[normalizing-flow]]

# Neural ODEs

_神经常微分方程_（Neural ODEs, NODEs）是离散 NF 在层数 $L\to\infty$、步长 $\Delta t\to0$ 时的连续极限。

残差流单层映射为

$$
\mathbf{x}_{k+1}=\mathbf{x}_k+\mathbf{v}_{\phi_k}(\mathbf{x}_k,k)
\tag{1}
$$

视为欧拉离散化并取 $\Delta t\to0$，得连续动力学

$$
\frac{\mathrm{d}\mathbf{x}}{\mathrm{d}t}=\mathbf{v}_\phi(\mathbf{x}_t,t),
\qquad t\in[0,T]
\tag{2}
$$

- _离散 NF_：有限可逆映射链，样本轨迹为折线
- _连续 CNF_：沿速度场 $\mathbf{v}_\phi$ 的积分曲线平滑演化

## 形式化设定

- _系统方程_：$\frac{\mathrm{d}\mathbf{x}}{\mathrm{d}t}=\mathbf{v}_\phi(\mathbf{x}_t,t)$
- _状态_：$\mathbf{x}_t\in\mathbb{R}^D$
- _目标_：设 $\mathbf{x}_0\sim p_{\mathrm{prior}}$，学习 $\mathbf{v}_\phi$ 使终点边缘分布 $p_\phi(\mathbf{x}_T,T)\approx p_{\mathrm{data}}$

## 瞬时换元公式

设 $\mathbf{x}_t$ 的密度为 $p(\mathbf{x}_t,t)$，且 $\frac{\mathrm{d}\mathbf{x}}{\mathrm{d}t}=\mathbf{v}_\phi(\mathbf{x}_t,t)$。设 $\mathbf{v}_\phi(\cdot,t)\in C^1$，且 ODE 解存在唯一。

将 ODE 的欧拉步视为残差流单层

$$
\mathbf{x}_{t+\Delta t}=\mathbf{x}_t+\Delta t\,\mathbf{v}_\phi(\mathbf{x}_t,t)
\tag{3}
$$

对其应用单层换元公式：

$$
\ln p(\mathbf{x}_{t+\Delta t},t+\Delta t)
=
\ln p(\mathbf{x}_t,t)
-
\ln\left|\det\left(\mathbf{I}+\Delta t\frac{\partial\mathbf{v}_\phi}{\partial\mathbf{x}}\right)\right|
\tag{4}
$$

利用一阶展开 $\ln\left|\det(\mathbf{I}+\Delta t\mathbf{A})\right|=\Delta t\operatorname{tr}(\mathbf{A})+o(\Delta t)$，并取 $\mathbf{A}=\frac{\partial\mathbf{v}_\phi}{\partial\mathbf{x}}$、$\operatorname{tr}(\mathbf{A})=\nabla_{\mathbf{x}}\cdot\mathbf{v}_\phi$，得

$$
\frac{\ln p(\mathbf{x}_{t+\Delta t},t+\Delta t)-\ln p(\mathbf{x}_t,t)}{\Delta t}
=
-\nabla_{\mathbf{x}}\cdot\mathbf{v}_\phi(\mathbf{x}_t,t)+o(1)
\tag{5}
$$

令 $\Delta t\to0$，沿样本轨迹的*瞬时变量代换*为

$$
\frac{\mathrm{d}\ln p(\mathbf{x}_t,t)}{\mathrm{d}t}
=
-\nabla_{\mathbf{x}}\cdot\mathbf{v}_\phi(\mathbf{x}_t,t)
\tag{6}
$$

在 $[0,T]$ 上积分，终点对数密度为

$$
\ln p_\phi(\mathbf{x}_T,T)
=
\ln p_{\mathrm{prior}}(\mathbf{x}_0,0)
-
\int_0^T\nabla_{\mathbf{x}}\cdot\mathbf{v}_\phi(\mathbf{x}_t,t)\,\mathrm{d}t
\tag{7}
$$

## 离散与连续对称性

| 维度     | 离散 NF                                                                                                                                                            | Neural ODE / CNF                                                                                                           |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| 累加机制 | $\sum$                                                                                                                                                             | $\int$                                                                                                                     |
| 空间度量 | $\ln\lvert\det\frac{\partial\mathbf{f}_k(\mathbf{x}_k)}{\partial\mathbf{x}_k}\rvert$                                                                               | $\nabla_{\mathbf{x}}\cdot\mathbf{v}_\phi=\operatorname{tr}\left(\frac{\partial\mathbf{v}_\phi}{\partial\mathbf{x}}\right)$ |
| 对数似然 | $\ln p_\phi(\mathbf{x}_L)=\ln p_{\mathrm{prior}}(\mathbf{x}_0)-\sum_{k=0}^{L-1}\ln\lvert\det\frac{\partial\mathbf{f}_k(\mathbf{x}_k)}{\partial\mathbf{x}_k}\rvert$ | $\ln p_\phi(\mathbf{x}_T,T)=\ln p_{\mathrm{prior}}(\mathbf{x}_0,0)-\int_0^T\nabla\cdot\mathbf{v}_\phi\,\mathrm{d}t$        |

## 训练与对数似然

_训练目标_（MLE）：

$$
\mathcal{L}_{\mathrm{NODE}}(\phi)
:=
\mathbb{E}_{\mathbf{x}\sim p_{\mathrm{data}}(\mathbf{x})}\left[\ln p_\phi(\mathbf{x},T)\right]
\tag{8}
$$

对给定数据点 $\mathbf{x}$，沿 ODE *反向*积分（$t:T\to0$）计算精确对数似然：

$$
\ln p_\phi(\mathbf{x},T)
=
\ln p_{\mathrm{prior}}(\mathbf{x}_0)
-
\int_0^T\nabla_{\mathbf{x}}\cdot\mathbf{v}_\phi(\mathbf{x}_t,t)\,\mathrm{d}t
\tag{9}
$$

其中 $\frac{\mathrm{d}\mathbf{x}}{\mathrm{d}t}=\mathbf{v}_\phi(\mathbf{x}_t,t)$，初值 $\mathbf{x}_T=\mathbf{x}$；先验项 $\ln p_{\mathrm{prior}}(\mathbf{x}_0)$ 通常有闭式。

## 高效散度估计

散度等价于 Jacobian 的迹：

$$
\nabla_{\mathbf{x}}\cdot\mathbf{v}_\phi
=
\operatorname{tr}\left(\frac{\partial\mathbf{v}_\phi}{\partial\mathbf{x}}\right)
\tag{10}
$$

显式求迹在 $D$ 维空间为 $O(D^2)$。可用*随机迹估计*以无偏随机向量积近似 $\operatorname{tr}(\mathbf{J})$，降低高维似然计算成本。

## 附录 B：行列式一阶展开与迹–散度

> [!abstract] 命题（行列式一阶展开与迹–散度恒等式）
> 设 $\mathbf{A}\in\mathbb{R}^{D\times D}$ 固定，且 $\Delta t$ 充分小使 $\mathbf{I}+\Delta t\mathbf{A}$ 可逆。则
>
> $$
> \ln\left|\det(\mathbf{I}+\Delta t\mathbf{A})\right|=\Delta t\,\operatorname{tr}(\mathbf{A})+o(\Delta t).
> $$
>
> 特别地，若 $\mathbf{A}=\frac{\partial\mathbf{v}_\phi}{\partial\mathbf{x}}$，则 $\operatorname{tr}(\mathbf{A})=\nabla_{\mathbf{x}}\cdot\mathbf{v}_\phi$，从而
>
> $$
> \ln\left|\det\left(\mathbf{I}+\Delta t\frac{\partial\mathbf{v}_\phi}{\partial\mathbf{x}}\right)\right|
> =
> \Delta t\,\nabla_{\mathbf{x}}\cdot\mathbf{v}_\phi+o(\Delta t).
> $$
>
> > [!note]- 证明
> > _第一步（行列式一阶展开）。_
> > 对可逆矩阵 $\mathbf{X}$，行列式微分公式给出
> >
> > $$
> > \mathrm{d}\left|\mathbf{X}\right|=\left|\mathbf{X}\right|\operatorname{tr}(\mathbf{X}^{-1}\mathrm{d}\mathbf{X}).
> > $$
> >
> > 于是
> >
> > $$
> > \mathrm{d}\ln\left|\det\mathbf{X}\right|
> > =
> > \frac{1}{\left|\mathbf{X}\right|}\mathrm{d}\left|\mathbf{X}\right|
> > =
> > \operatorname{tr}(\mathbf{X}^{-1}\mathrm{d}\mathbf{X}).
> > $$
> >
> > 取 $\mathbf{X}=\mathbf{I}+\Delta t\mathbf{A}$。因 $\mathbf{A}$ 不随 $\Delta t$ 变化，有 $\mathrm{d}\mathbf{X}=\mathbf{A}\,\mathrm{d}(\Delta t)$，故
> >
> > $$
> > \frac{\mathrm{d}}{\mathrm{d}(\Delta t)}\ln\left|\det(\mathbf{I}+\Delta t\mathbf{A})\right|
> > =
> > \operatorname{tr}\left((\mathbf{I}+\Delta t\mathbf{A})^{-1}\mathbf{A}\right).
> > $$
> >
> > 在 $\Delta t=0$ 处取值：
> >
> > $$
> > \left.\frac{\mathrm{d}}{\mathrm{d}(\Delta t)}\ln\left|\det(\mathbf{I}+\Delta t\mathbf{A})\right|\right|_{\Delta t=0}
> > =
> > \operatorname{tr}(\mathbf{A}).
> > $$
> >
> > 又 $\ln\left|\det\mathbf{I}\right|=0$，由一元 Taylor 一阶展开得
> >
> > $$
> > \ln\left|\det(\mathbf{I}+\Delta t\mathbf{A})\right|
> > =
> > \Delta t\,\operatorname{tr}(\mathbf{A})+o(\Delta t).
> > $$
> >
> > _第二步（迹等于散度）。_
> > 令 $\mathbf{A}=\frac{\partial\mathbf{v}_\phi}{\partial\mathbf{x}}$。按分量，
> >
> > $$
> > \operatorname{tr}(\mathbf{A})
> > =
> > \sum_{i=1}^D A_{ii}
> > =
> > \sum_{i=1}^D\frac{\partial(\mathbf{v}_\phi)_i(\mathbf{x})}{\partial x_i}
> > =
> > \nabla_{\mathbf{x}}\cdot\mathbf{v}_\phi.
> > $$
> >
> > 两步合并即得命题结论。此处将 $\mathbf{A}$ 视为固定状态 $\mathbf{x}$ 处的局部雅可比；对 CNF，这正是固定时刻、固定状态下欧拉步的局部一阶展开。
