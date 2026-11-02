---
title: quantization
tags:
  - 量化
  - 大模型
  - PyTorch
---

# quantization

整数仿射量化把实数区间 $[a,b]$ 映到整数区间 $[c,d]$。$x_R$ 量化后的值为 $x_I$，$x_I$ 反量化后的值为 $x_Q$。数值改用整数存储。激活一并量化时，点积可以改用整数乘加；只量化权重时，点积仍用浮点，省下的是权重的存储和读取。低精度浮点（FP8）和非均匀码本（NF4）用的是别的有限集合，本文推导均匀整数格点。

## 仿射量化

$$
x_I = \operatorname{round}\left((x_R-a)\frac{d-c}{b-a} + c\right),
$$

$$
x_Q = (x_I - c)\frac{b-a}{d-c} + a.
$$

把 $\frac{b-a}{d-c}$ 记作 $s$，

$$
x_I = \operatorname{round}\left((x_R-a)\frac{1}{s} + c\right) \tag{1}
$$

$$
x_Q = (x_I - c)s + a. \tag{2}
$$


$c$ 是整数格点的下端，所以 $c\in\mathbb{Z}$。此时 $\operatorname{round}(y+c)-c=\operatorname{round}(y)$。把 (1) 代入 (2)，$c$ 消去：

$$
\begin{aligned}
x_Q
&= \left(\operatorname{round}\left((x_R-a)\frac{1}{s}+c\right)-c\right)s+a \\
&= \operatorname{round}\left((x_R-a)\frac{1}{s}\right)s+a. \tag{3}
\end{aligned}
$$

(1)(2) 是数轴上的缩放 $s$ 和平移。$a$ 是整数 $c$ 对应的实数，端点按要覆盖的范围来取。$x_R$ 落在 $[a,b]$ 外时，$x_I$ 会落到 $[c,d]$ 外，取较近的边界：

$$
x_I = \operatorname{clip}\left(\operatorname{round}\left((x_R-a)\frac{1}{s} + c\right), c, d\right) \tag{4}
$$

$$
x_Q = \left(\operatorname{clip}\left(\operatorname{round}\left((x_R-a)\frac{1}{s} + c\right), c, d\right) - c\right)s + a. \tag{5}
$$

## 量化误差

不考虑截断、使用 (3) 时，$x_Q = x_R + \epsilon$。把取整误差写成 $\operatorname{round}(y)=y+\delta$，$\delta\in[-1/2,1/2]$，

$$
\begin{aligned}
\epsilon
&= x_Q - x_R \\
&= \operatorname{round}\left((x_R-a)\frac{1}{s}\right)s + a - x_R \\
&= \left((x_R-a)\frac{1}{s} + \delta\right)s + a - x_R \\
&= s\delta.
\end{aligned}
$$

若把 $\delta$ 看成 $U(-1/2,1/2)$，则 $\epsilon\sim U(-s/2, s/2)$。

## scale 与 zero point

令实数 $0$ 对应整数 $z$，并取 $a=(c-z)s$。$c$、$z$ 都是整数时，(1)(2) 写成

$$
x_I = \operatorname{round}\left(\frac{x_R}{s}\right) + z, \tag{6}
$$

$$
x_Q = (x_I - z)s. \tag{7}
$$

$z$ 在 (7) 里消去后，$x_Q = \operatorname{round}(x_R/s)\,s$，舍入误差仍是 $s\delta$。

### 量化粒度

同一组 $(s,z)$ 覆盖多大一块数据，就是量化粒度。整块张量共用一组，是 per-tensor。权重矩阵每一行（一个输出通道）一组，是 per-channel。一行里每 $g$ 个权重一组，是 per-group，$g$ 是 group size。激活按 token 各用一组，是 per-token。块越小，越跟得上局部范围，scale 和 zero point 也越多。

## 对称量化与非对称量化

### 对称量化

对称量化把实数区间放成关于 $0$ 对称，并且 $0$ 对应整数区间的中心。取

$$
Q=2^{n-1}-1,\qquad c=-Q,\qquad d=Q,\qquad z=0.
$$

记 $M=\max_i|x_i|$，令 $a=-M$，$b=M$。则 $s=(b-a)/(d-c)=M/Q$，

$$
x_I
=
\operatorname{clip}\left(\operatorname{round}\left(\frac{x_R}{s}\right),-Q,Q\right),
\qquad
x_Q=sx_I.
\tag{8}
$$

可表示的实数是 $s\{-Q,\ldots,Q\}$。

$n$ 位有符号整数的满区间是 $[-2^{n-1},2^{n-1}-1]$，中点为 $-1/2$，落在两个整数之间。取 $z=0$ 时，负侧有 $2^{n-1}$ 个负码，正侧有 $2^{n-1}-1$ 个正码。PyTorch 的 `qint8` 对称 observer 使用 $c=-128$、$d=127$、$z=0$，

$$
s
=
\frac{2\max_i|x_i|}{d-c}
=
\frac{\max_i|x_i|}{127.5}.
$$

可表示的实数是 $s\{-128,\ldots,127\}$。

### 非对称量化

非对称量化允许 $a\neq -b$。先把 $0$ 放进区间：

$$
a=\min(x_{\min},0),
\qquad
b=\max(x_{\max},0),
\qquad
s=\frac{b-a}{d-c}.
$$

在 (6) 下让 $x_R=a$ 映到 $c$，就要 $\operatorname{round}(a/s)+z=c$。再把 $z$ 限制在整数区间内，

$$
z
=
\operatorname{clip}\left(
c-\operatorname{round}\left(\frac{a}{s}\right),
c,d
\right).
\tag{9}
$$

### 整数点积

激活和权重都写成 (7)。$W\in\mathbb{R}^{M\times N}$ 的一行是一个输出通道，$X\in\mathbb{R}^{N\times T}$ 的一列是一个样本，$Y=WX$。$W_I$、$X_I$ 是对应的整数矩阵，$\mathbf{1}$ 是全 $1$ 列向量。

权重的 scale 与 zero point 按输出通道排成 $s_w,z_w\in\mathbb{R}^{M}$，激活的按样本排成 $s_x,z_x\in\mathbb{R}^{T}$。整张量共用一组时，各分量相等，对角矩阵就是标量乘单位阵。

$$
W=\operatorname{diag}(s_w)\,(W_I-z_w\mathbf{1}_N^{\mathrm{T}}),
\qquad
X=(X_I-\mathbf{1}_N z_x^{\mathrm{T}})\,\operatorname{diag}(s_x).
$$

乘开得

$$
\begin{aligned}
Y
&=
\operatorname{diag}(s_w)
\Big(
W_IX_I
-(W_I\mathbf{1}_N)z_x^{\mathrm{T}}
-z_w(\mathbf{1}_N^{\mathrm{T}}X_I)
+Nz_wz_x^{\mathrm{T}}
\Big)
\operatorname{diag}(s_x).
\end{aligned}
\tag{10}
$$

$W_IX_I$ 是整数矩阵乘。$\operatorname{diag}(s_w)$ 按行缩放，$\operatorname{diag}(s_x)$ 按列缩放，两者都在它外面。$(W_I\mathbf{1}_N)z_x^{\mathrm{T}}$ 由权重行和与各样本的 zero point 组成，权重行和不依赖 $X$。$z_w(\mathbf{1}_N^{\mathrm{T}}X_I)$ 是各样本的激活和。$Nz_wz_x^{\mathrm{T}}$ 是两个 zero point 向量的外积。

$z_w=0$ 时，(10) 的后两项为 $0$，

$$
Y
=
\operatorname{diag}(s_w)
\Big(
W_IX_I-(W_I\mathbf{1}_N)z_x^{\mathrm{T}}
\Big)
\operatorname{diag}(s_x).
\tag{11}
$$

输入通道分成若干组。$W_{I,g}$、$X_{I,g}$ 是第 $g$ 组在 $W_I$ 中的列和在 $X_I$ 中的行。$z_w=0$ 时，这一组有自己的 $\operatorname{diag}(s_{w,g})$，

$$
Y
=
\sum_g
\operatorname{diag}(s_{w,g})
\Big(
W_{I,g}X_{I,g}
-(W_{I,g}\mathbf{1})z_x^{\mathrm{T}}
\Big)
\operatorname{diag}(s_x).
\tag{12}
$$

$\operatorname{diag}(s_{w,g})$ 留在对组的求和里。$\operatorname{diag}(s_x)$ 对每一组相同，仍在求和之外。

## 量化参数的确定

### Min-Max

取 $a=\min(x_{\min},0)$，$b=\max(x_{\max},0)$，再按对称或非对称的公式计算 $s$ 和 $z$。校准样本都落在 $[a,b]$ 内，截断误差为 $0$。若权重几乎都在 $[-0.1,0.1]$，只有一个为 $10$，则 $s$ 由 $10$ 决定，其余权重只占少数格点。

### 分位数

用分位数代替两端的极值。对称时设 $|x|$ 的分布函数为 $F_{|x|}$，

$$
T=F_{|x|}^{-1}(1-\alpha),
\qquad
a=-T,
\qquad
b=T.
$$

非对称时设 $x$ 的分布函数为 $F$，

$$
a=F^{-1}(\alpha),
\qquad
b=F^{-1}(1-\beta).
$$

再取 $a\leftarrow\min(a,0)$，$b\leftarrow\max(b,0)$，使 $0\in[a,b]$，这样 (7) 能表示 $0$。比例 $\alpha$、$\beta$ 之外的样本被截断，范围内的 $s$ 更小。

### 均方误差

在候选的 $(s,z)$ 上最小化重建误差。$x_{Q,i}$ 由 (5) 算出，

$$
(s^\ast,z^\ast)
=
\operatorname{argmin}_{s,z}
\frac{1}{N}
\sum_{i=1}^{N}
\left(x_i-x_{Q,i}\right)^2.
\tag{13}
$$

一部分样本可以被截断，只要平方误差下降。对称量化把搜索收成一个阈值 $T$，$s=T/Q$，$z=0$。

(13) 只含张量自身的坐标。权重误差乘上激活之后，才得到层输出的误差。

### KL 散度

先做直方图。每个候选截断阈值对应一个量化后的分布：阈值以外的质量并入端点，区间内按整数格点合并，再映回原来的分桶。$P$ 是截断后的直方图，$Q$ 是量化后映回的直方图。选择使

$$
D_{\mathrm{KL}}(P\|Q)
=
\sum_i P(i)\log\frac{P(i)}{Q(i)}
\tag{14}
$$

最小的阈值。(14) 比较的是两个分布，(13) 比较的是逐点平方误差。

## 推理时量化（PTQ）

PTQ 在模型训练完成后进行，不需要重新训练。先选取少量有代表性的数据作为校准集，运行浮点模型，通过 observer 统计权重和激活的数值范围，据此确定 scale 和 zero point。然后按量化参数将权重转换为整数；对于激活，可以使用校准得到的静态量化参数，也可以在推理时动态统计范围。最后将浮点算子替换为对应的量化算子。常见做法包括只量化权重，以及同时量化权重和激活。

## 训练时量化（QAT）

QAT 在训练或微调过程中模拟量化效果。先为权重和激活确定初始的 scale 和 zero point，再插入伪量化算子，使前向计算能够感受到量化误差。反向传播时使用直通估计器近似取整操作的梯度，让模型参数在任务损失的驱动下适应量化误差。训练结束后冻结量化参数，将伪量化算子转换为实际的整数算子。