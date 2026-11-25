---
title: Flow Matching
tags:
  - 机器学习
  - 生成模型
  - 流匹配
date: 2026-11-25
---

## 前置

- [[neural-ode]]

# Flow Matching

## 目标

> NODE / CNF 生成时沿速度场积分：
>
> $$
> \frac{\mathrm{d}\mathbf{x}_t}{\mathrm{d}t}=\mathbf{v}_\phi(\mathbf{x}_t,t)
> \tag{1}
> $$
>
> NODE / CNF 通过 MLE 训练：需反向积分解轨迹，并计算散度 $\nabla_{\mathbf{x}}\cdot\mathbf{v}_\phi$，代价高。

自然问题：_能否不算概率密度、不算散度，而是直接训练速度场？_

_理想目标_：用 ODE 速度场将 $p_{\mathrm{src}}$ 输运到 $p_{\mathrm{tgt}}$

$$
\frac{\mathrm{d}\mathbf{x}_t}{\mathrm{d}t}=\mathbf{v}_t(\mathbf{x}_t),
\qquad t\in[0,1]
\tag{2}
$$

边界 $p_0=p_{\mathrm{src}}$，$p_1=p_{\mathrm{tgt}}$。已知 $\mathbf{v}_t$ 即可通过 ODE 求解器前向积分生成样本。

_任务_：用神经网络 $\mathbf{v}_\phi(\mathbf{x},t)$ 拟合理想速度场 $\mathbf{v}_t(\mathbf{x})$——从似然间接学速度，转向可监督的速度回归。

连续性方程（Continuity Equation，CE）：

$$
\frac{\partial p_t(\mathbf{x})}{\partial t}
+
\nabla_{\mathbf{x}}\cdot\left[\mathbf{v}_t(\mathbf{x})p_t(\mathbf{x})\right]
=
0
\tag{3}
$$

（满足 CE 的速度场一般*不唯一*；见附录 D。）

## NODE 与 FM：同动力学，异训练

| 问题       | Neural ODE / CNF         | Flow Matching                |
| ---------- | ------------------------ | ---------------------------- |
| 学什么？   | 速度场 $\mathbf{v}_\phi$ | 速度场 $\mathbf{v}_\phi$     |
| 怎么训练？ | MLE + 散度积分           | 对理想 / 条件速度做 MSE 回归 |
| 怎么生成？ | ODE 积分                 | ODE 积分                     |

## FM 损失与瓶颈

自然想法：直接回归理想速度 $\mathbf{v}_t$，但边缘路径 $p_t$ 与 $\mathbf{v}_t$ 通常未知。

自然回归目标——_流匹配损失_：

$$
\mathcal{L}_{\mathrm{FM}}(\phi)
=
\mathbb{E}_{t\sim\mathcal{U}[0,1]}\mathbb{E}_{\mathbf{x}_t\sim p_t(\cdot)}
\left[\left\|\mathbf{v}_\phi(\mathbf{x}_t,t)-\mathbf{v}_t(\mathbf{x}_t)\right\|_2^2\right]
\tag{4}
$$

> _瓶颈_：对真实数据，$p_t$ 无闭式、无法采样 $\mathbf{x}_t\sim p_t$，理想 $\mathbf{v}_t$ 亦不可显式求得——$\mathcal{L}_{\mathrm{FM}}$ 无法直接用于训练。

## 条件概率密度与条件速度场

引入 $\mathbf{z}\sim\pi(\mathbf{z})$，设计*条件概率路径* $p_t(\mathbf{x}\mid\mathbf{z})$。

可主动将条件路径设为简单高斯，例如

$$
p_t(\mathbf{x}\mid\mathbf{z})=\mathcal{N}(\mathbf{x};\alpha_t\mathbf{z},\sigma_t^2\mathbf{I})
\tag{5}
$$

边缘密度由全概率公式恢复：

$$
p_t(\mathbf{x})=\int p_t(\mathbf{x}\mid\mathbf{z})\pi(\mathbf{z})\,\mathrm{d}\mathbf{z}
\tag{6}
$$

有了条件路径 $p_t(\mathbf{x}\mid\mathbf{z})$，驱动该局部轨迹的速度即*条件速度场* $\mathbf{v}_t(\mathbf{x}\mid\mathbf{z})$，满足条件连续性方程。

## 后验期望与全局 CE

若每个条件路径满足条件 CE，并定义边缘密度与后验期望速度场

$$
p_t(\mathbf{x})=\int p_t(\mathbf{x}\mid\mathbf{z})\pi(\mathbf{z})\,\mathrm{d}\mathbf{z},
\qquad
\mathbf{v}_t(\mathbf{x})=\mathbb{E}_{\mathbf{z}\sim p(\mathbf{z}\mid\mathbf{x})}\left[\mathbf{v}_t(\mathbf{x}\mid\mathbf{z})\right]
\tag{7}
$$

则边缘对 $(p_t,\mathbf{v}_t)$ 满足全局 CE（见附录 A）。

## Condition Flow Matching

用*容易计算的条件速度*作监督标签：

$$
\mathbf{v}_t(\mathbf{x})=\mathbb{E}_{\mathbf{z}\sim p(\mathbf{z}\mid\mathbf{x})}\left[\mathbf{v}_t(\mathbf{x}\mid\mathbf{z})\right]
\tag{8}
$$

$$
\mathcal{L}_{\mathrm{FM}}(\phi)
=
\mathbb{E}_{t\sim\mathcal{U}[0,1]}\mathbb{E}_{\mathbf{x}_t\sim p_t(\cdot)}
\left[\left\|\mathbf{v}_\phi(\mathbf{x}_t,t)-\mathbf{v}_t(\mathbf{x}_t)\right\|_2^2\right]
\tag{9}
$$

$$
\mathcal{L}_{\mathrm{CFM}}(\phi)
=
\mathbb{E}_{t\sim\mathcal{U}[0,1]}\mathbb{E}_{\mathbf{z}\sim\pi(\mathbf{z})}\mathbb{E}_{\mathbf{x}_t\sim p_t(\cdot\mid\mathbf{z})}
\left[\left\|\mathbf{v}_\phi(\mathbf{x}_t,t)-\mathbf{v}_t(\mathbf{x}_t\mid\mathbf{z})\right\|_2^2\right]
\tag{10}
$$

### FM 与 CFM 等价性

在可积假设 $\mathbb{E}\left[\left\|\mathbf{v}_t(\mathbf{x}_t)-\mathbf{v}_t(\mathbf{x}_t\mid\mathbf{z})\right\|^2\right]<\infty$ 下，

$$
\mathcal{L}_{\mathrm{CFM}}(\phi)=\mathcal{L}_{\mathrm{FM}}(\phi)+C,
\tag{11}
$$

其中常数 $C$ 与参数 $\phi$ 无关，故

$$
\nabla_\phi\mathcal{L}_{\mathrm{CFM}}=\nabla_\phi\mathcal{L}_{\mathrm{FM}}
\tag{12}
$$

（见附录 B）。

## 条件路径的构造

通用 CFM 还需构造条件路径 $p_t(\mathbf{x}\mid\mathbf{z})$ 与条件速度 $\mathbf{v}_t(\mathbf{x}\mid\mathbf{z})$。
*流优先*与*概率路径优先*是两种*出发方式*，同一 $(p_t,\mathbf{v}_t)$ 常可由两种顺序得到。

- _流优先_：$\psi_t\to\mathbf{v}_t=(\partial_t\psi_t)\circ\psi_t^{-1}\to p_t=(\psi_t)_\ast p_0$（推前）。
- _概率路径优先_：先指定 $p_t$；满足条件 CE 的 $\mathbf{v}_t$ 一般*不唯一*（见附录 D），需再选一种速度构造。

隐变量选取正交于上述范式：_单边_ $\mathbf{z}=\mathbf{x}_1$（聚光灯），_双边_ $\mathbf{z}=(\mathbf{x}_0,\mathbf{x}_1)$（光束）。

> 下文高斯单边 / 双边实例按*概率路径优先*组织，并用典范仿射流闭式得到 $\mathbf{v}_t$（见附录 C）。

### 高斯路径：典范仿射速度

_概率路径优先_：先指定高斯条件路径

$$
p_t(\mathbf{x}\mid\mathbf{z})=\mathcal{N}\left(\mathbf{x};\mu_t(\mathbf{z}),\sigma_t(\mathbf{z})^2\mathbf{I}\right),
\qquad
\sigma_t(\mathbf{z})>0.
\tag{13}
$$

再取实现该路径的典范仿射流

$$
\psi_t(\mathbf{x}_0\mid\mathbf{z})
:=
\mu_t(\mathbf{z})
+
\sigma_t(\mathbf{z})\frac{\mathbf{x}_0-\mu_0(\mathbf{z})}{\sigma_0(\mathbf{z})},
\tag{14}
$$

其中 $\mathbf{x}_0\sim\mathcal{N}\left(\mu_0(\mathbf{z}),\sigma_0(\mathbf{z})^2\mathbf{I}\right)$ 时有
$\psi_t(\mathbf{x}_0\mid\mathbf{z})\sim p_t(\cdot\mid\mathbf{z})$。对 $\psi_t$ 求导得闭式条件速度（见附录 C）

$$
\mathbf{v}_t(\mathbf{x}_t\mid\mathbf{z})
=
\frac{\mathrm{d}\mu_t}{\mathrm{d}t}
+
\frac{\mathrm{d}\sigma_t}{\mathrm{d}t}\cdot\frac{1}{\sigma_t}\left(\mathbf{x}_t-\mu_t\right).
\tag{15}
$$

### 双边条件路径

_概率路径优先_。取 $\mathbf{z}=(\mathbf{x}_0,\mathbf{x}_1)$，先指定

$$
p_t(\mathbf{x}\mid\mathbf{z})=\mathcal{N}\left(\mathbf{x};a_t\mathbf{x}_0+b_t\mathbf{x}_1,\sigma^2\mathbf{I}\right),
\qquad
a_0=1,\ b_0=0,\quad a_1=0,\ b_1=1
\tag{16}
$$

即 $\mu_t=a_t\mathbf{x}_0+b_t\mathbf{x}_1$、$\sigma_t\equiv\sigma$。因 $\sigma_t'=0$，附录 C 的命题给出

$$
\mathbf{v}_t(\mathbf{x}\mid\mathbf{z})=a_t'\mathbf{x}_0+b_t'\mathbf{x}_1,
\qquad
a_t':=\frac{\mathrm{d}a_t}{\mathrm{d}t},\quad b_t':=\frac{\mathrm{d}b_t}{\mathrm{d}t}.
\tag{17}
$$

确定性极限 $\sigma\to0$ 时 $p_t$ 退化为 Dirac，轨迹 $\mathbf{x}_t=a_t\mathbf{x}_0+b_t\mathbf{x}_1$。

训练时从耦合 $\pi$（或独立地 $\mathbf{x}_0\sim p_{\mathrm{src}}$、$\mathbf{x}_1\sim p_{\mathrm{data}}$）采样配对。目标速度显式依赖 $\mathbf{x}_0$，故 $p_{\mathrm{src}}$ 可取任意可采样分布。

### 单边条件路径

_概率路径优先_。取 $\mathbf{z}=\mathbf{x}_1$、$\pi=p_{\mathrm{data}}$（$\mathbf{x}_0$ 不作为条件变量）。

一般高斯单边下，边缘源由目标与端点 schedule 诱导，记 $p_{\mathrm{src}}=\mathcal{F}(p_{\mathrm{data}})$，通常与 $p_{\mathrm{data}}$ _耦合_。

_经典仿射 schedule_：先指定

$$
p_t(\mathbf{x}\mid\mathbf{x}_1)=\mathcal{N}\left(\mathbf{x};b_t\mathbf{x}_1,a_t^2\mathbf{I}\right),
\qquad
b_0=0,\ a_0=1,\quad b_1=1,\ a_1=\sigma_{\min}>0
\tag{18}
$$

（即 $\mu_t=b_t\mathbf{x}_1$、$\sigma_t=a_t$），$p_{\mathrm{src}}=\mathcal{N}(\mathbf{0},\mathbf{I})$ 与 $p_{\mathrm{data}}$ 无关。附录 C 的命题给出

$$
\mathbf{v}_t(\mathbf{x}\mid\mathbf{x}_1)
=
b_t'\mathbf{x}_1+\frac{a_t'}{a_t}\left(\mathbf{x}-b_t\mathbf{x}_1\right).
\tag{19}
$$

## Rectified Flow

Rectified Flow 是双边*概率路径优先*的确定性极限：先取
$p_t(\mathbf{x}\mid\mathbf{z})=\delta\left(\mathbf{x}-\left[(1-t)\mathbf{x}_0+t\mathbf{x}_1\right]\right)$
（即 $a_t=1-t$、$b_t=t$、$\sigma\to0$），再沿退化流求导得 $\mathbf{v}_t=\mathbf{x}_1-\mathbf{x}_0$。
高斯仿射公式要求 $\sigma_t>0$，RF 需经 $\sigma\to0$ / 弱意义理解，不能直接代入。训练退化为简单速度回归。

$$
\begin{aligned}
p_0 &:= p_{\mathrm{src}} := \mathcal{N}(\mathbf{0},\mathbf{I}),\\
p_1 &:= p_{\mathrm{tgt}} := p_{\mathrm{data}}
\end{aligned}
\tag{20}
$$

采用独立耦合

$$
\pi(\mathbf{x}_0,\mathbf{x}_1)=p_0(\mathbf{x}_0)p_1(\mathbf{x}_1)
\tag{21}
$$

定义条件变量

$$
\mathbf{z}:=(\mathbf{x}_0,\mathbf{x}_1),
\qquad
\mathbf{x}_0\sim p_0,\ \mathbf{x}_1\sim p_1
\tag{22}
$$

对给定配对 $(\mathbf{x}_0,\mathbf{x}_1)$，采用线性插值路径

$$
\mathbf{x}_t=(1-t)\mathbf{x}_0+t\mathbf{x}_1,
\qquad t\in[0,1]
\tag{23}
$$

对应条件分布退化为 Dirac 测度

$$
p_t(\mathbf{x}\mid\mathbf{x}_0,\mathbf{x}_1)=\delta\left(\mathbf{x}-\left[(1-t)\mathbf{x}_0+t\mathbf{x}_1\right]\right)
\tag{24}
$$

因路径确定性，无需对 $p_t(\cdot\mid\mathbf{z})$ 额外采样。

条件速度场由路径定义直接求导：

$$
\begin{aligned}
\mathbf{v}_t(\mathbf{x}\mid\mathbf{x}_0,\mathbf{x}_1)
&=\frac{\mathrm{d}}{\mathrm{d}t}\left[(1-t)\mathbf{x}_0+t\mathbf{x}_1\right]\\
&=\mathbf{x}_1-\mathbf{x}_0
\end{aligned}
\tag{25}
$$

## RF 训练

根据 CFM 框架，代入独立耦合与 Dirac 路径，内层期望 $\mathbb{E}_{\mathbf{x}_t\sim p_t(\cdot\mid\mathbf{z})}$ 消失，得 _Rectified Flow_ 损失

$$
\begin{aligned}
\mathcal{L}_{\mathrm{RF}}(\phi)
&:=\mathcal{L}_{\mathrm{CFM}}(\phi)\\
&=\mathbb{E}_{t\sim\mathcal{U}[0,1]}\mathbb{E}_{\mathbf{x}_0\sim p_0}\mathbb{E}_{\mathbf{x}_1\sim p_1}
\left[\left\|\mathbf{v}_\phi\left((1-t)\mathbf{x}_0+t\mathbf{x}_1,t\right)-(\mathbf{x}_1-\mathbf{x}_0)\right\|_2^2\right]
\end{aligned}
\tag{26}
$$

## 附录 A：后验期望诱导全局 CE

> [!abstract] 命题（后验期望速度场满足全局 CE）
> 设对几乎所有 $\mathbf{z}$，条件路径与条件速度满足条件连续性方程
>
> $$
> \frac{\partial p_t(\mathbf{x}\mid\mathbf{z})}{\partial t}
> +
> \nabla_{\mathbf{x}}\cdot\left[p_t(\mathbf{x}\mid\mathbf{z})\mathbf{v}_t(\mathbf{x}\mid\mathbf{z})\right]
> =
> 0
> $$
>
> 定义边缘密度与后验期望速度场
>
> $$
> p_t(\mathbf{x})=\int p_t(\mathbf{x}\mid\mathbf{z})\pi(\mathbf{z})\,\mathrm{d}\mathbf{z},
> \qquad
> \mathbf{v}_t(\mathbf{x})=\mathbb{E}_{\mathbf{z}\sim p(\mathbf{z}\mid\mathbf{x})}\left[\mathbf{v}_t(\mathbf{x}\mid\mathbf{z})\right]
> $$
>
> 并设 $p_t(\cdot\mid\mathbf{z})$、$\mathbf{v}_t(\cdot\mid\mathbf{z})$ 足够光滑，使 $\nabla_{\mathbf{x}}$ 与 $\int_{\mathbf{z}}$ 可交换。则
>
> $$
> \frac{\partial p_t(\mathbf{x})}{\partial t}
> +
> \nabla_{\mathbf{x}}\cdot\left[p_t(\mathbf{x})\mathbf{v}_t(\mathbf{x})\right]
> =
> 0.
> $$
>
> > [!note]- 证明
> > 由贝叶斯公式 $p(\mathbf{z}\mid\mathbf{x})=\frac{p_t(\mathbf{x}\mid\mathbf{z})\pi(\mathbf{z})}{p_t(\mathbf{x})}$，将后验期望展开并乘以 $p_t$：
> >
> > $$
> > p_t(\mathbf{x})\mathbf{v}_t(\mathbf{x})
> > =
> > \int p_t(\mathbf{x}\mid\mathbf{z})\mathbf{v}_t(\mathbf{x}\mid\mathbf{z})\pi(\mathbf{z})\,\mathrm{d}\mathbf{z}
> > $$
> >
> > 于是
> >
> > $$
> > \begin{aligned}
> > \nabla_{\mathbf{x}}\cdot\left[p_t(\mathbf{x})\mathbf{v}_t(\mathbf{x})\right]
> > &=
> > \int\nabla_{\mathbf{x}}\cdot\left[p_t(\mathbf{x}\mid\mathbf{z})\mathbf{v}_t(\mathbf{x}\mid\mathbf{z})\right]\pi(\mathbf{z})\,\mathrm{d}\mathbf{z}\\
> > &=
> > \int\left(-\frac{\partial p_t(\mathbf{x}\mid\mathbf{z})}{\partial t}\right)\pi(\mathbf{z})\,\mathrm{d}\mathbf{z}\\
> > &=
> > -\frac{\partial}{\partial t}\int p_t(\mathbf{x}\mid\mathbf{z})\pi(\mathbf{z})\,\mathrm{d}\mathbf{z}
> > =
> > -\frac{\partial p_t(\mathbf{x})}{\partial t}.
> > \end{aligned}
> > $$

## 附录 B：FM 与 CFM 损失等价

> [!abstract] 命题（CFM 与 FM 同梯度）
> 设 $\mathcal{L}_{\mathrm{FM}}$、$\mathcal{L}_{\mathrm{CFM}}$ 如主文所定义，且
>
> $$
> \mathbb{E}\left[\left\|\mathbf{v}_t(\mathbf{x}_t)-\mathbf{v}_t(\mathbf{x}_t\mid\mathbf{z})\right\|^2\right]<\infty.
> $$
>
> 则存在与 $\phi$ 无关的常数 $C$，使得
>
> $$
> \mathcal{L}_{\mathrm{CFM}}(\phi)=\mathcal{L}_{\mathrm{FM}}(\phi)+C,
> $$
>
> 从而
>
> $$
> \nabla_\phi\mathcal{L}_{\mathrm{CFM}}=\nabla_\phi\mathcal{L}_{\mathrm{FM}}.
> $$
>
> > [!note]- 证明
> > _取样约定_：$t\sim\mathcal{U}[0,1]$，且 $(\mathbf{z},\mathbf{x}_t)$ 按
> > $\mathbf{z}\sim\pi(\mathbf{z})$、$\mathbf{x}_t\sim p_t(\cdot\mid\mathbf{z})$ 联合采样
> > （等价于先取边缘 $\mathbf{x}_t\sim p_t$，再取后验 $\mathbf{z}\sim p(\mathbf{z}\mid\mathbf{x}_t)$）。
> >
> > 记缩写
> >
> > $$
> > \mathbf{v}_\phi:=\mathbf{v}_\phi(\mathbf{x}_t,t),
> > \qquad
> > \mathbf{v}_t:=\mathbf{v}_t(\mathbf{x}_t),
> > \qquad
> > \mathbf{v}_t^z:=\mathbf{v}_t(\mathbf{x}_t\mid\mathbf{z}).
> > $$
> >
> > _平方展开_：点态恒等式
> >
> > $$
> > \left\|\mathbf{v}_\phi-\mathbf{v}_t^z\right\|^2
> > =
> > \left\|\mathbf{v}_\phi-\mathbf{v}_t\right\|^2
> > +
> > \left\|\mathbf{v}_t-\mathbf{v}_t^z\right\|^2
> > +
> > 2(\mathbf{v}_\phi-\mathbf{v}_t)^\top(\mathbf{v}_t-\mathbf{v}_t^z)
> > $$
> >
> > 两边取期望，得
> >
> > $$
> > \mathcal{L}_{\mathrm{CFM}}(\phi)
> > =
> > \underbrace{\mathbb{E}\left[\left\|\mathbf{v}_\phi-\mathbf{v}_t\right\|^2\right]}_{\text{Item 1}}
> > +
> > \underbrace{\mathbb{E}\left[\left\|\mathbf{v}_t-\mathbf{v}_t^z\right\|^2\right]}_{\text{Item 2}}
> > +
> > \underbrace{2\mathbb{E}\left[(\mathbf{v}_\phi-\mathbf{v}_t)^\top(\mathbf{v}_t-\mathbf{v}_t^z)\right]}_{\text{Item 3}}.
> > $$
> >
> > _Item 1_：被积函数 $\left\|\mathbf{v}_\phi-\mathbf{v}_t\right\|^2$ 不依赖 $\mathbf{z}$。对后验 $\mathbf{z}\mid\mathbf{x}_t$ 积分后，联合期望化为边缘期望
> >
> > $$
> > \mathbb{E}_{t,\mathbf{z},\mathbf{x}_t}\left[\left\|\mathbf{v}_\phi-\mathbf{v}_t\right\|^2\right]
> > =
> > \mathbb{E}_t\mathbb{E}_{\mathbf{x}_t\sim p_t}\left[\left\|\mathbf{v}_\phi(\mathbf{x}_t,t)-\mathbf{v}_t(\mathbf{x}_t)\right\|^2\right]
> > =
> > \mathcal{L}_{\mathrm{FM}}(\phi).
> > $$
> >
> > _Item 2_：令
> >
> > $$
> > C:=\mathbb{E}\left[\left\|\mathbf{v}_t-\mathbf{v}_t^z\right\|^2\right].
> > $$
> >
> > 右端仅含理想场 $\mathbf{v}_t$ 与条件场 $\mathbf{v}_t^z$，与网络参数 $\phi$ 无关。
> >
> > _Item 3_：固定 $(t,\mathbf{x}_t)$，由边缘速度的后验期望定义
> >
> > $$
> > \mathbf{v}_t(\mathbf{x}_t)=\mathbb{E}_{\mathbf{z}\mid\mathbf{x}_t}\left[\mathbf{v}_t(\mathbf{x}_t\mid\mathbf{z})\right]
> > $$
> >
> > 得
> >
> > $$
> > \mathbb{E}_{\mathbf{z}\mid\mathbf{x}_t}\left[\mathbf{v}_t-\mathbf{v}_t^z\right]=\mathbf{0}.
> > $$
> >
> > 又 $(\mathbf{v}_\phi-\mathbf{v}_t)$ 对后验 $\mathbf{z}\mid\mathbf{x}_t$ 可视为常数，故
> >
> > $$
> > \mathbb{E}_{\mathbf{z}\mid\mathbf{x}_t}\left[(\mathbf{v}_\phi-\mathbf{v}_t)^\top(\mathbf{v}_t-\mathbf{v}_t^z)\right]
> > =
> > (\mathbf{v}_\phi-\mathbf{v}_t)^\top\mathbb{E}_{\mathbf{z}\mid\mathbf{x}_t}\left[\mathbf{v}_t-\mathbf{v}_t^z\right]
> > =
> > \mathbf{0}.
> > $$
> >
> > 再对 $(t,\mathbf{x}_t)$ 取期望，交叉项整体为 $0$。
> >
> > _结论_：三式合并得 $\mathcal{L}_{\mathrm{CFM}}(\phi)=\mathcal{L}_{\mathrm{FM}}(\phi)+C$。两边对 $\phi$ 求导（$C$ 与 $\phi$ 无关）即
> >
> > $$
> > \nabla_\phi\mathcal{L}_{\mathrm{CFM}}=\nabla_\phi\mathcal{L}_{\mathrm{FM}}.
> > $$

## 附录 C：高斯路径的闭式速度场

> [!abstract] 命题（高斯路径的闭式速度场）
> 在*概率路径优先*下，设已指定 $p_t(\cdot\mid\mathbf{z})=\mathcal{N}\left(\mu_t(\mathbf{z}),\sigma_t(\mathbf{z})^2\mathbf{I}\right)$ 且 $\sigma_t(\mathbf{z})>0$。
> 典范仿射流
>
> $$
> \psi_t(\mathbf{x}_0\mid\mathbf{z})
> :=
> \mu_t(\mathbf{z})
> +
> \sigma_t(\mathbf{z})\frac{\mathbf{x}_0-\mu_0(\mathbf{z})}{\sigma_0(\mathbf{z})}
> $$
>
> 实现该高斯路径，并满足 $\mathbf{v}_t(\cdot\mid\mathbf{z})=\left(\partial_t\psi_t(\cdot\mid\mathbf{z})\right)\circ\psi_t(\cdot\mid\mathbf{z})^{-1}$。则
>
> $$
> \mathbf{v}_t(\mathbf{x}_t\mid\mathbf{z})
> =
> \frac{\mathrm{d}\mu_t(\mathbf{z})}{\mathrm{d}t}
> +
> \frac{\mathrm{d}\sigma_t(\mathbf{z})}{\mathrm{d}t}\cdot\frac{1}{\sigma_t(\mathbf{z})}
> \left(\mathbf{x}_t-\mu_t(\mathbf{z})\right).
> $$
>
> > [!note]- 证明
> > 下述证明沿典范流 $\psi_t$ 求导（流优先计算）；该 $\psi_t$ 正是实现已指定高斯路径的仿射实现。
> >
> > 对 $\psi_t(\mathbf{x}_0\mid\mathbf{z})$ 关于 $t$ 求全导数，视 $\mathbf{x}_0$、$\mu_0$、$\sigma_0$ 为常数：
> >
> > $$
> > \frac{\mathrm{d}\psi_t(\mathbf{x}_0\mid\mathbf{z})}{\mathrm{d}t}
> > =
> > \frac{\mathrm{d}\mu_t(\mathbf{z})}{\mathrm{d}t}
> > +
> > \frac{\mathrm{d}\sigma_t(\mathbf{z})}{\mathrm{d}t}\cdot\frac{\mathbf{x}_0-\mu_0(\mathbf{z})}{\sigma_0(\mathbf{z})}.
> > $$
> >
> > 令 $\mathbf{x}_t=\psi_t(\mathbf{x}_0\mid\mathbf{z})$。由 $\sigma_t>0$ 映射可逆，反解得
> >
> > $$
> > \frac{\mathbf{x}_0-\mu_0(\mathbf{z})}{\sigma_0(\mathbf{z})}
> > =
> > \frac{\mathbf{x}_t-\mu_t(\mathbf{z})}{\sigma_t(\mathbf{z})}.
> > $$
> >
> > 代入上式，并由速度场定义
> > $\mathbf{v}_t(\mathbf{x}_t\mid\mathbf{z})=\left.\frac{\mathrm{d}\psi_t}{\mathrm{d}t}\right|_{\mathbf{x}_0=\psi_t^{-1}(\mathbf{x}_t)}$
> > 即得命题公式。

## 附录 D：速度场通解

> [!abstract] 命题（诱导同一边缘密度的速度场通解）
> 设基础场 $\mathbf{v}_t(\mathbf{x})$ 满足连续性方程
>
> $$
> \frac{\partial p_t(\mathbf{x})}{\partial t}
> +
> \nabla_{\mathbf{x}}\cdot\left[p_t(\mathbf{x})\mathbf{v}_t(\mathbf{x})\right]
> =
> 0
> $$
>
> 候选场 $\mathbf{u}_t(\mathbf{x})$ 诱导相同边缘密度 $p_t$。定义概率流差
>
> $$
> \mathbf{w}_t(\mathbf{x}):=p_t(\mathbf{x})\left(\mathbf{u}_t(\mathbf{x})-\mathbf{v}_t(\mathbf{x})\right).
> $$
>
> 则在 $p_t(\mathbf{x})>0$ 处，$\mathbf{u}_t$ 与 $\mathbf{v}_t$ 诱导相同 $p_t$ 当且仅当
>
> $$
> \mathbf{u}_t(\mathbf{x})=\mathbf{v}_t(\mathbf{x})+\frac{\mathbf{w}_t(\mathbf{x})}{p_t(\mathbf{x})},
> \qquad
> \nabla\cdot\mathbf{w}_t=0.
> $$
>
> > [!note]- 证明
> > _充分性_：设 $\nabla\cdot\mathbf{w}_t=0$，令 $\mathbf{u}_t=\mathbf{v}_t+\mathbf{w}_t/p_t$，代入 CE：
> >
> > $$
> > \begin{aligned}
> > &\frac{\partial p_t(\mathbf{x})}{\partial t}+\nabla\cdot\left[p_t\mathbf{u}_t\right]\\
> > &=\frac{\partial p_t(\mathbf{x})}{\partial t}+\nabla\cdot\left[p_t\mathbf{v}_t+\mathbf{w}_t\right]\\
> > &=\underbrace{\frac{\partial p_t}{\partial t}+\nabla\cdot(p_t\mathbf{v}_t)}_{=0}
> > +\underbrace{\nabla\cdot\mathbf{w}_t}_{=0}=0.
> > \end{aligned}
> > $$
> >
> > 故 $\mathbf{u}_t$ 同样满足以 $p_t$ 为边缘密度的连续性方程。
> >
> > _必要性_：设 $\mathbf{u}_t$ 亦满足 CE，两式相减得
> >
> > $$
> > \nabla\cdot\left[p_t\left(\mathbf{u}_t-\mathbf{v}_t\right)\right]=0.
> > $$
> >
> > 定义 $\mathbf{w}_t:=p_t(\mathbf{u}_t-\mathbf{v}_t)$，则 $\nabla\cdot\mathbf{w}_t=0$；在 $p_t(\mathbf{x})>0$ 处移项即得通解。
> >
> > _结论_：满足同一 $p_t$ 的速度场不唯一，通解为 $\mathbf{v}_t+\mathbf{w}_t/p_t$（$\nabla\cdot\mathbf{w}_t=0$）。
