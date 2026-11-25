---
title: Normalizing Flows
tags:
  - 机器学习
  - 生成模型
date: 2026-11-25
---
## 前置

- [[generative-model-introduction]]

# Normalizing Flows

_标准化流_（Normalizing Flows, NFs）通过*可逆且可微*的映射 $\mathbf{f}_\phi:\mathbb{R}^D\to\mathbb{R}^D$，将简单先验 $p_{\mathrm{prior}}(\mathbf{z})$（如 $\mathcal{N}(\mathbf{0},\mathbf{I})$）变换为复杂数据分布 $p_{\mathrm{data}}(\mathbf{x})$。

## 换元公式与 MLE

设前向映射 $\mathbf{x}=\mathbf{f}_\phi(\mathbf{z})$ 可逆可微，则 $\mathbf{z}=\mathbf{f}_\phi^{-1}(\mathbf{x})$。双射保持概率质量不变：对任意可测集 $A$，

$$
\int_A p_\phi(\mathbf{x})\,\mathrm{d}\mathbf{x}
=
\int_{\mathbf{f}_\phi^{-1}(A)} p_{\mathrm{prior}}(\mathbf{z})\,\mathrm{d}\mathbf{z}
\tag{1}
$$

作变量代换 $\mathbf{z}=\mathbf{f}_\phi^{-1}(\mathbf{x})$，体积元变换为 $\mathrm{d}\mathbf{z}=\left|\det\frac{\partial\mathbf{f}_\phi^{-1}(\mathbf{x})}{\partial\mathbf{x}}\right|\mathrm{d}\mathbf{x}$，故

$$
\int_A p_\phi(\mathbf{x})\,\mathrm{d}\mathbf{x}
=
\int_A p_{\mathrm{prior}}(\mathbf{z})\,\left|\det\frac{\partial\mathbf{f}_\phi^{-1}(\mathbf{x})}{\partial\mathbf{x}}\right|\mathrm{d}\mathbf{x}
\tag{2}
$$

由 $A$ 的任意性得数据密度

$$
p_\phi(\mathbf{x})
=
p_{\mathrm{prior}}(\mathbf{z})\,\left|\det\frac{\partial\mathbf{f}_\phi^{-1}(\mathbf{x})}{\partial\mathbf{x}}\right|
\tag{3}
$$

其中逆映射的雅可比行列式满足 $\left|\det\frac{\partial\mathbf{f}_\phi^{-1}(\mathbf{x})}{\partial\mathbf{x}}\right|=\left|\det\frac{\partial\mathbf{f}_\phi(\mathbf{z})}{\partial\mathbf{z}}\right|^{-1}$。两边取对数，得数据对数似然：

$$
\ln p_\phi(\mathbf{x})
=
\ln p_{\mathrm{prior}}(\mathbf{z})
+
\ln\left|\det\frac{\partial\mathbf{f}_\phi^{-1}(\mathbf{x})}{\partial\mathbf{x}}\right|
\tag{4}
$$

_训练目标_：最大化训练数据上的平均对数似然：

$$
\mathcal{L}_{\mathrm{NF}}(\phi)
=
\mathbb{E}_{\mathbf{x}\sim p_{\mathrm{data}}(\mathbf{x})}\left[\ln p_\phi(\mathbf{x})\right]
\tag{5}
$$

## 多层流

为平衡*计算效率*与*模型表达能力*，NFs 将多个简单可逆映射组合成链：

$$
\mathbf{f}_\phi
=
\mathbf{f}_{L-1}\circ\mathbf{f}_{L-2}\circ\cdots\circ\mathbf{f}_0
\tag{6}
$$

- _前向采样_：$\mathbf{x}_{k+1}=\mathbf{f}_k(\mathbf{x}_k)$，其中 $\mathbf{z}=\mathbf{x}_0\sim p_{\mathrm{prior}}$，最终数据 $\mathbf{x}=\mathbf{x}_L$。
- _对数似然分解_：对每一层应用单步换元，并由前向雅可比写出

$$
\ln p(\mathbf{x}_{k+1})
=
\ln p(\mathbf{x}_k)
-
\ln\left|\det\frac{\partial\mathbf{f}_k(\mathbf{x}_k)}{\partial\mathbf{x}_k}\right|
\tag{7}
$$

从 $k=0$ 递推到 $k=L-1$，得

$$
\ln p_\phi(\mathbf{x})
=
\ln p_{\mathrm{prior}}(\mathbf{x}_0)
-
\sum_{k=0}^{L-1}\ln\left|\det\frac{\partial\mathbf{f}_k(\mathbf{x}_k)}{\partial\mathbf{x}_k}\right|
\tag{8}
$$

## 经典可逆流

有三类代表性的高效计算对数行列式的单层流：

| 流类型                     | 映射 $\mathbf{f}(\mathbf{z})$                                                                                                                                               | 对数行列式                                                                                                                                        |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| 平面流 (Planar)            | $\mathbf{z}+\mathbf{u}\,h(\mathbf{w}^\top\mathbf{z}+b)$                                                                                                                     | $\ln\lvert 1+\mathbf{u}^\top h'(\mathbf{w}^\top\mathbf{z}+b)\,\mathbf{w}\rvert$                                                                   |
| 残差流 (Residual)          | $\mathbf{z}+\mathbf{v}(\mathbf{z})$                                                                                                                                         | $\sum_{k=1}^{\infty}\frac{(-1)^{k+1}}{k}\operatorname{Tr}\left(\left(\frac{\partial\mathbf{v}(\mathbf{z})}{\partial\mathbf{z}}\right)^{k}\right)$ |
| 仿射耦合 (Affine Coupling) | 分块 $\mathbf{z}=(\mathbf{z}_a,\mathbf{z}_b)$：<br>$\mathbf{y}_a=\mathbf{z}_a$，<br>$\mathbf{y}_b=\mathbf{z}_b\odot\exp(\mathbf{s}(\mathbf{z}_a))+\mathbf{t}(\mathbf{z}_a)$ | $\sum_i s_i(\mathbf{z}_a)$                                                                                                                        |

## 附录 A：仿射耦合的对数行列式

> [!abstract] 命题（仿射耦合的对数雅可比）
> 将输入分块为 $\mathbf{z}=(\mathbf{z}_a,\mathbf{z}_b)$，定义仿射耦合
>
> $$
> \mathbf{y}_a=\mathbf{z}_a,
> \qquad
> \mathbf{y}_b=\mathbf{z}_b\odot\exp(\mathbf{s}(\mathbf{z}_a))+\mathbf{t}(\mathbf{z}_a),
> $$
>
> 其中 $\mathbf{s},\mathbf{t}$ 对 $\mathbf{z}_a$ 可微（例如由神经网络给出）。记 $\mathbf{y}=\mathbf{f}(\mathbf{z})$，则
>
> $$
> \ln\left|\det\frac{\partial\mathbf{f}(\mathbf{z})}{\partial\mathbf{z}}\right|=\sum_i s_i(\mathbf{z}_a).
> $$
>
> 逆映射闭式为
>
> $$
> \mathbf{z}_a=\mathbf{y}_a,
> \qquad
> \mathbf{z}_b=(\mathbf{y}_b-\mathbf{t}(\mathbf{y}_a))\odot\exp(-\mathbf{s}(\mathbf{y}_a)).
> $$
>
> > [!note]- 证明
> > 雅可比按分块写为
> >
> > $$
> > \mathbf{J}_f
> > =
> > \begin{pmatrix}
> > \dfrac{\partial\mathbf{y}_a}{\partial\mathbf{z}_a} & \dfrac{\partial\mathbf{y}_a}{\partial\mathbf{z}_b}\\[6pt]
> > \dfrac{\partial\mathbf{y}_b}{\partial\mathbf{z}_a} & \dfrac{\partial\mathbf{y}_b}{\partial\mathbf{z}_b}
> > \end{pmatrix}.
> > $$
> >
> > 由 $\mathbf{y}_a=\mathbf{z}_a$ 得 $\dfrac{\partial\mathbf{y}_a}{\partial\mathbf{z}_a}=\mathbf{I}$、$\dfrac{\partial\mathbf{y}_a}{\partial\mathbf{z}_b}=\mathbf{0}$。
> >
> > 对 $\mathbf{z}_b$ 求偏导时视 $\mathbf{z}_a$ 为常数，故 $\mathbf{s}(\mathbf{z}_a)$、$\mathbf{t}(\mathbf{z}_a)$ 不参与该偏导：
> >
> > $$
> > \frac{\partial\mathbf{y}_b}{\partial\mathbf{z}_b}
> > =
> > \operatorname{diag}\left(\exp(\mathbf{s}(\mathbf{z}_a))\right).
> > $$
> >
> > 对 $\mathbf{z}_a$ 求导则须用链式法则计入 $\mathbf{s},\mathbf{t}$ 对 $\mathbf{z}_a$ 的依赖：
> >
> > $$
> > \mathbf{C}
> > :=
> > \frac{\partial\mathbf{y}_b}{\partial\mathbf{z}_a}
> > =
> > \operatorname{diag}\left(\mathbf{z}_b\odot\exp(\mathbf{s}(\mathbf{z}_a))\right)\frac{\partial\mathbf{s}}{\partial\mathbf{z}_a}
> > +
> > \frac{\partial\mathbf{t}}{\partial\mathbf{z}_a}.
> > $$
> >
> > 因此
> >
> > $$
> > \mathbf{J}_f
> > =
> > \begin{pmatrix}
> > \mathbf{I} & \mathbf{0}\\
> > \mathbf{C} & \operatorname{diag}\left(\exp(\mathbf{s}(\mathbf{z}_a))\right)
> > \end{pmatrix}.
> > $$
> >
> > 此为分块下三角矩阵，行列式等于对角块行列式之积，$\mathbf{C}$ 不出现：
> >
> > $$
> > \begin{aligned}
> > \det\mathbf{J}_f
> > &=
> > \det(\mathbf{I})\,\det\left(\operatorname{diag}\left(\exp(\mathbf{s}(\mathbf{z}_a))\right)\right)\\
> > &=
> > \prod_i\exp(s_i(\mathbf{z}_a))
> > =
> > \exp\left(\sum_i s_i(\mathbf{z}_a)\right).
> > \end{aligned}
> > $$
> >
> > 两边取对数即得
> > $\ln\left|\det\mathbf{J}_f\right|=\sum_i s_i(\mathbf{z}_a)$。
> >
> > 逆映射：由 $\mathbf{y}_a=\mathbf{z}_a$ 得 $\mathbf{z}_a=\mathbf{y}_a$，再解
> > $\mathbf{y}_b=\mathbf{z}_b\odot\exp(\mathbf{s}(\mathbf{z}_a))+\mathbf{t}(\mathbf{z}_a)$ 即得所述闭式。
