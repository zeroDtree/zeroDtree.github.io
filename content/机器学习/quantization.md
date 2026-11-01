---
title: quantization
tags:
  - 量化
  - 大模型
  - PyTorch
---

# quantization

把浮点数上的存储和运算转化成整数的存储和运算。实数区间 $[a,b]$ 映到整数区间 $[c,d]$。$x_R$ 量化后的值为 $x_I$，$x_I$ 反量化后的值为 $x_Q$。

## 1. 仿射量化

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

### 量化误差

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

## 2. scale 与 zero point

令实数 $0$ 对应整数 $z$，并取 $a=(c-z)s$。$c$、$z$ 都是整数时，(1)(2) 写成

$$
x_I = \operatorname{round}\left(\frac{x_R}{s}\right) + z, \tag{6}
$$

$$
x_Q = (x_I - z)s. \tag{7}
$$

$z$ 在 (7) 里消去后，$x_Q = \operatorname{round}(x_R/s)\,s$，舍入误差仍是 $s\delta$。

同一组 $(s,z)$ 覆盖多大一块数据，就是量化粒度。整块张量共用一组，是 per-tensor。权重矩阵每一行（一个输出通道）一组，是 per-channel。一行里每 $g$ 个权重一组，是 per-group，$g$ 是 group size。激活按 token 各用一组，是 per-token。块越小，越跟得上局部范围，scale 和 zero point 也越多。

计算 $s$ 之前，先把统计到的范围扩到包含 $0$：

$$
x_{\min}^{-}=\min(x_{\min},0),\qquad x_{\max}^{+}=\max(x_{\max},0).
$$

整数区间是 $[q_{\min}, q_{\max}]$。TorchAO 的 `choose_qparams_affine` 有三种映射。

对称映射 `SYMMETRIC` 用最大绝对值撑满半个整数跨度，zero point 取整数区间的中点：

$$
\begin{aligned}
s &= \frac{\max(-x_{\min}^{-},\, x_{\max}^{+})}{(q_{\max}-q_{\min})/2}
  = \frac{2\max(|x_{\min}|, x_{\max})}{q_{\max}-q_{\min}}, \\
z &= \left\lfloor\frac{q_{\max}+q_{\min}+1}{2}\right\rfloor.
\end{aligned}
\tag{8}
$$

$x_{\min}\le x_{\max}$ 且范围已经含 $0$ 时，第二个等号成立。`qint8` 的 $[-128,127]$ 给出 $z=0$，`quint8` 的 $[0,255]$ 给出 $z=128$。这就是 PyTorch observer 文档里的对称公式。

`SYMMETRIC_NO_CLIPPING_ERR` 把正负两侧分开算，再取更大的 scale，使两侧的浮点值量化后都不越出整数界。有符号区间（如 $q_{\min}=-8$、$q_{\max}=7$）上

$$
s=\max\left(\frac{x_{\min}^{-}}{q_{\min}},\frac{x_{\max}^{+}}{q_{\max}}\right),
$$

zero point 仍是 (8) 的中点。$[-8,7]$ 的中点是 $0$。负侧若更宽，$s$ 由负侧决定，正侧的整数格就用不满；正侧若更宽则相反。普通 `SYMMETRIC` 用 $(q_{\max}-q_{\min})/2$ 做分母，在 $-8$ 与 $7$ 这种不对称整数界上，某一侧可能在取整后被截断。

非对称映射把 $[x_{\min}^{-}, x_{\max}^{+}]$ 直接铺到 $[q_{\min}, q_{\max}]$：

$$
\begin{aligned}
s &= \frac{x_{\max}^{+}-x_{\min}^{-}}{q_{\max}-q_{\min}}, \\
z &= \operatorname{clip}\left(q_{\min}-\operatorname{round}\left(\frac{x_{\min}^{-}}{s}\right), q_{\min}, q_{\max}\right).
\end{aligned}
\tag{9}
$$

PyTorch 文档把未先含 $0$ 的最小、最大值直接代入，并省略最后的 $\operatorname{clip}$：

$$
s=\frac{x_{\max}-x_{\min}}{Q_{\max}-Q_{\min}},\qquad
z=Q_{\min}-\operatorname{round}(x_{\min}/s).
$$

$s$ 还有下界 $\epsilon$，避免范围退化时除以 $0$。

最小、最大值可以来自已经见过的数据，也可以随 batch 做移动平均。$X$ 是当前张量，$\alpha\in(0,1]$ 是平均常数。尚未初始化时取当前最值，否则

$$
\begin{aligned}
x_{\min} &\leftarrow (1-\alpha)x_{\min} + \alpha\min(X), \\
x_{\max} &\leftarrow (1-\alpha)x_{\max} + \alpha\max(X).
\end{aligned}
$$

只保留历史最值时，用 $\min(x_{\min},\min(X))$ 和 $\max(x_{\max},\max(X))$ 代替这两式。

## 3. 伪量化

伪量化是量化再反量化，输出仍是浮点。(5) 就是它的 $(a,c)$ 写法。(6)(7) 合起来是

$$
\hat{x}
=
\left(
\operatorname{clip}\left(
\operatorname{round}\left(\frac{x}{s}\right)+z,\,
q_{\min}, q_{\max}
\right)
-z
\right)s. \tag{10}
$$

训练图里的权重仍是浮点参数。前向用 $\hat{x}$ 代替 $x$，让后面的层看见量化误差。

$\operatorname{round}$ 几乎处处导数为 $0$，直接反传时更前面的参数收不到更新。[[机器学习/Straight-Through-Estimator|Straight-Through Estimator]] 保持前向取整，反向把局部导数换成恒等映射。量化还要截断：舍入结果落在 $[q_{\min}, q_{\max}]$ 内（含两端）时局部导数为 $1$，外面为 $0$。

$s$、$z$ 当作常数。记 $u=x/s$，$r=\operatorname{round}(u)$，$q=\operatorname{clip}(r+z, q_{\min}, q_{\max})$，则 $\hat{x}=(q-z)s$。恒等 STE 给出 $\partial r/\partial u\approx 1$。截断的代理导数是

$$
m=
\begin{cases}
1, & q_{\min}\le r+z\le q_{\max}, \\
0, & \text{否则}.
\end{cases}
$$

链式法则里 $s$ 与 $1/s$ 相消：

$$
\frac{\partial\hat{x}}{\partial x}
=
s\cdot m\cdot 1\cdot\frac{1}{s}
=
m. \tag{11}
$$

范围内的元素，伪量化对输入的梯度是 $1$；越界的元素梯度是 $0$。前向数值仍带有舍入和截断误差。

TorchAO 用两个 autograd 函数实现这一点。`_Round` 的反向原样返回上游梯度。`_ClampSTE` 在边界上仍返回梯度，范围外用 `torch.where` 换成 $0$，避免 $0\cdot\mathrm{NaN}=\mathrm{NaN}$。

```python
class RoundSTE(torch.autograd.Function):
    @staticmethod
    def forward(ctx, x):
        return torch.round(x)

    @staticmethod
    def backward(ctx, gy):
        return gy

class ClampSTE(torch.autograd.Function):
    @staticmethod
    def forward(ctx, x, lo, hi):
        ctx.save_for_backward(x)
        ctx.lo, ctx.hi = lo, hi
        return torch.clamp(x, lo, hi)

    @staticmethod
    def backward(ctx, gy):
        (x,) = ctx.saved_tensors
        in_range = (x >= ctx.lo) & (x <= ctx.hi)
        zero = torch.zeros((), dtype=gy.dtype, device=gy.device)
        return torch.where(in_range, gy, zero), None, None
```

整数 zero point 的量化是

$$
q=\operatorname{ClampSTE}\left(\operatorname{RoundSTE}(x/s)+z\right),\qquad
\hat{x}=(q-z)s.
$$

例如 $s=1/2$，$z=0$，$[q_{\min}, q_{\max}]=[-2,2]$，输入 $[-1.6,-1,0.4,1.6]$。$x/s$ 舍入后是 $[-3,-2,1,3]$，截断后是 $[-2,-2,1,2]$，反量化得到 $[-1,-1,1/2,1]$。按 (11)，梯度是 $[0,1,1,0]$：$-3$ 和 $3$ 越界，$-2$ 落在下界上，梯度仍为 $1$。

## 4. PTQ 与 QAT

PTQ（post-training quantization）在训练结束之后确定 $s$、$z$，再把权重量化。系数一旦定下，前向按这个映射计算，取整处不再为训练建立反传。

激活的范围往往要等输入到来才知道。只量化权重、激活留到前向时用当前张量计算 $s$、$z$，是动态量化。权重和激活的范围都事先用校准数据估好，是静态量化。校准在要量化的位置插入 observer，记下最小、最大值或它们的移动平均，再代入 (8) 或 (9)。

QAT（quantization-aware training）在训练时就插入 (10)。三步是：

1. prepare：把 `nn.Linear` 换成带伪量化的线性层，权重仍是浮点参数。
2. 照常前向、反传、更新。范围内的梯度按 (11) 穿过伪量化，模型因此适应舍入误差。
3. convert：去掉伪量化模块，用同一套量化配置把浮点权重换成真正的低精度表示。

prepare 和 convert 使用同一套目标配置，训练时模拟的格式和部署时的格式就对应。`model.eval()` 切换 Dropout、BatchNorm 这类模块的行为。去掉伪量化要走 convert。

$s$、$z$ 在 QAT 里有三种来源。

- 动态：每次前向用当前张量重算。`choose_qparams_affine` 标了 `@torch.no_grad()`，min/max 到 $s$ 的计算不在梯度图里。权重得到的梯度来自 (11)，其中 $s$ 被视为常数。
- 静态：用一批数据或 observer 定下 $s$、$z$ 后重复使用。伪量化在这里同时扮演 observer。
- range learning：初始化之后把 $s$ 收成 `nn.Parameter`。对称量化把 zero point 置 $0$；非对称量化把 zero point 也收成参数。优化器要在这次初始化之后创建，才能看到这些新参数。

第三种才让 $s$ 自己收到梯度。忽略截断且 $z=0$ 时，$\hat{x}=s\operatorname{round}(x/s)$。记 $u=x/s$，并用 $\partial\operatorname{round}(u)/\partial u\approx 1$，

$$
\begin{aligned}
\frac{\partial\hat{x}}{\partial s}
&= \operatorname{round}(u) + s\cdot 1\cdot\left(-\frac{x}{s^2}\right) \\
&= \operatorname{round}(x/s) - x/s. \tag{12}
\end{aligned}
$$

(12) 是局部简化。完整实现还要乘上截断因子 $m$，并处理 zero point。Learned Step Size Quantization 也把步长当作可学习参数，再用 STE 穿过取整。TorchAO 的 range learning 同样把 scale 放进优化器，具体参数化和梯度以它的实现为准。

## 5. TorchAO 里的接法

`FakeQuantizedLinear` 继承 `nn.Linear`。前向对浮点权重做伪量化；激活也要量化时，先对激活做同样的伪量化。最后仍调用 `F.linear`，所以 QAT 阶段的矩阵乘是浮点的。低精度打包和对应的 GEMM 发生在 convert 之后。

通用整数路径的伪量化都进入 `_fake_quantize_affine`。per-tensor 和 per-token 的系数来自 `choose_qparams_affine`，per-group 用分组的 qparams，再以同样的仿射公式量化。整数 zero point 域里，这一步是

```python
quant = _ClampSTE.apply(
    _Round.apply(input * (1.0 / scale)) + zero_point,
    quant_min,
    quant_max,
)
```

反量化回到输入的浮点 dtype。梯度就是第 3 节的 (11)。

`Int4WeightOnlyConfig` 在 prepare 时走另一条 `Int4WeightFakeQuantizer`，用来对齐 bf16 激活、INT4 权重的 kernel。二维权重按最后一维分成 `group_size` 一组。记一组的最小、最大值为 $w_{\min}$、$w_{\max}$，

$$
s=\frac{\max(w_{\max}-w_{\min},\,\epsilon)}{15},\qquad
z_f=w_{\min}+8s.
$$

先映到无符号的 $16$ 个等级，再平移到有符号 INT4：

$$
q_u=\operatorname{clip}\left(\operatorname{round}\left(\frac{w-w_{\min}}{s}\right), 0, 15\right),\qquad
\hat{w}=w_{\min}+q_u s.
$$

这里的 $z_f$ 是浮点偏移。代入 $\hat{w}=(q_u-8)s+z_f$ 就得到上一式。取整用 `_Round`，截断用 `Tensor.clamp`。每次前向都按当前权重重算 $s$ 和 $z_f$，二者是这次前向的局部结果。

# 参考资料

1. https://leimao.github.io/article/Neural-Networks-Quantization/#Quantization

2. https://zhuanlan.zhihu.com/p/548174416

3. https://www.dropbox.com/scl/fi/1mo0umu0qtq7uxap2l5m3/lec06.pdf?rlkey=bdl2mgusgajddjuvjxb0fot36&dl=0

4. https://zhuanlan.zhihu.com/p/645259854

5. https://github.com/pytorch/ao/blob/main/torchao/quantization/quant_primitives.py

6. https://docs.pytorch.org/ao/stable/workflows/qat.html

7. Learned Step Size Quantization, https://arxiv.org/abs/1902.08153
