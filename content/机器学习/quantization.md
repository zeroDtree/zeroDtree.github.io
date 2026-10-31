---
title: quantization
tags:
  - 量化
  - 大模型
  - PyTorch
---

# quantization

把浮点数上的存储和运算转化成整数的存储和运算。
$[a,b]$上的运算转化到$[c,d]$, 其中$[a,b]$是连续的，$[c,d]$是离散的整数。
$x_R$被量化后的指为$x_I$, $x_I$被反量化后的值为$x_Q$

$x_I = \operatorname{round}((x_R-a)(\frac{d-c}{b-a}) + c)$
$x_Q = (x_I - c)(\frac{b-a}{d-c}) + a$

把$\frac{b-a}{d-c}$记作s

$$
x_I = \operatorname{round}((x_R-a)(\frac{1}{s}) + c) \tag{1}
$$

$$
x_Q = (x_I - c)s + a \tag{2}
$$

把$x_I$带入$x_Q$中。因为$c$是整数，$\operatorname{round}(y+c)-c=\operatorname{round}(y)$，其中$y=(x_R-a)(\frac{1}{s})$，所以

$$
\begin{aligned}
x_Q &= \left(\operatorname{round}\left((x_R-a)(\frac{1}{s})+c\right)-c\right)s+a \\
&= \operatorname{round}\left((x_R-a)(\frac{1}{s})\right)s+a \tag{3}
\end{aligned}
$$

如果$x_R$不在$[a,b]$内,那$x_I$也极有可能不在[c,d]内。
如果$x_I$超出了[c,d],那就取较近的边界值。

$$
  x_I = clip(\operatorname{round}((x_R-a)(\frac{1}{s}) + c), c, d) \tag{4}
$$

$$
  x_Q = (clip(\operatorname{round}((x_R-a)(\frac{1}{s}) + c), c, d) - c)s + a \tag{5}
$$

观察上述(1),(2),(3),(4)可以不依赖与区间$[a,b]$和$[c,d]$的存在。可以看作对整个数轴的线性变换。s为缩放比例。a和c决定的平移。

我们假设值都在正常范围内，没有超出$[c,d]$，不考虑clip(即使用(3)中的$x_Q$)
$x_Q = x_R + \epsilon$

$$
  \begin{aligned}
  \epsilon &= x_Q - x_R\\
           &= \operatorname{round}((x_R-a)(\frac{1}{s}))s + a - x_R\\
           &= ((x_R-a)(\frac{1}{s}) + \delta)s + a - x_R, \text{其中}\delta \sim U(-0.5,0.5) \text{均匀分布}\\
           &= s\delta
  \end{aligned}
$$

所以$\epsilon \sim U(-0.5s, 0.5s)$

## pytorch的quantization

### 1. 根据权重和数据的分布（或最值）确定量化参数scale和zero_point

例如，8比特的对称量化和非对称量化

$$
\begin{aligned}
            \text{if Symmetric:}&\\
            &s = 2 \max(|x_\text{min}|, x_\text{max}) /
                \left( Q_\text{max} - Q_\text{min} \right) \\
            &z = \begin{cases}
                0 & \text{if dtype is qint8} \\
                128 & \text{otherwise}
            \end{cases}\\
            \text{Otherwise:}&\\
                &s = \left( x_\text{max} - x_\text{min}  \right ) /
                    \left( Q_\text{max} - Q_\text{min} \right ) \\
                &z = Q_\text{min} - \operatorname{round}(x_\text{min} / s)
        \end{aligned}
$$

#### 其中的最大值和最小值不一定是“真实”的最大值和最小值

确定最值有多种方式

1. 真实的最值
   $$
           \begin{array}{ll}
           x_\text{min} &= \begin{cases}
               \min(X) & \text{if~}x_\text{min} = \text{None} \\
               \min\left(x_\text{min}, \min(X)\right) & \text{otherwise}
           \end{cases}\\
           x_\text{max} &= \begin{cases}
               \max(X) & \text{if~}x_\text{max} = \text{None} \\
               \max\left(x_\text{max}, \max(X)\right) & \text{otherwise}
           \end{cases}\\
           \end{array}
   $$
2. 最值的移动平均：
   $$
           \begin{array}{ll}
                   x_\text{min} = \begin{cases}
                       \min(X) & \text{if~}x_\text{min} = \text{None} \\
                       (1 - c) x_\text{min} + c \min(X) & \text{otherwise}
                   \end{cases}\\
                   x_\text{max} = \begin{cases}
                       \max(X) & \text{if~}x_\text{max} = \text{None} \\
                       (1 - c) x_\text{max} + c \max(X) & \text{otherwise}
                   \end{cases}\\
           \end{array}
   $$
   还有一种是根据数据的分布确定最值。（具体的怎么算得我还没看。）

### 2. 量化

$$
  x_I = \operatorname{round}(\frac{x_R}{s}) + z
$$

$$
x_Q = (x_I - z)s
$$

$$
x_Q = (\operatorname{round}(\frac{x_R}{s}))s
$$

这样量化使得整数z对应实数0

### pytorch的量化误差

量化误差和之前得到的一样。

$$
  \begin{aligned}
  \epsilon &= x_Q - x_R\\
           &= \operatorname{round}((x_R)(\frac{1}{s}))s - x_R\\
           &= ((\frac{x_R}{s}) + \delta)s - x_R, \text{其中}\delta \sim U(-0.5,0.5) \text{均匀分布}\\
           &= s\delta
  \end{aligned}
$$

所以$\epsilon \sim U(-0.5s, 0.5s)$

# PTQ and QAT

PTQ和QAT都是训练完后再执行量化操作。

## PTQ(Post Training Qunatization)

直接对模型进行量化。

根据是否确定actvation的量化参数，可以分为PTDQ和PTSQ。

1. 只对权重量化，因为activation的范围是未知的（scale和zero_point未知）。等到推理的时候，计算出了activation,确定了量化参数，再对activation进行量化，称为PTDQ(D表示Dynamic)，（这个可能理解有点不准确）

2. 对权重和activation都量化，虽然不知道actvation的范围但可以根据已有的数据进行估计。称为PTSQ(S表示static)

在对模型量化前，在模型需要量化的结点插入Observer,用来统计和计算最值，从而确定量化参数。

## QAT(Quantization Aware Training)

1. 获取一个训练好的模型。
2. 插入伪量化（fake quantization）结点，在某个数据集上进行微调。（模型会在微调期间确定量化的参数）
3. 使用第2步中得到参数对模型进行量化。

QAT一般只静态量化.

### 关于QAT中的伪量化

伪量化=量化+反量化。伪量化是模型的参数仍然都是浮点数。

$$
  x_Q = (clip(\operatorname{round}((x_R-a)(\frac{1}{s}) + c), c, d) - c)s + a
$$

模型在微调时模拟了量化。伪量化结点也充当了Observer的角色。

伪量化结点的反向传播使用了（STE）

Quantization is discrete-valued, and thus the derivative is 0 almost everywhere.

$$
\frac{\partial Q(W)}{\partial W}=0
$$

The neural network will learn nothing since gradients become 0 and the weights won't get updated.

$$
g_{\mathbf{W}}=\frac{\partial L}{\partial \mathbf{W}}=\frac{\partial L}{\partial Q(\mathbf{W})} \cdot \frac{\partial Q(\mathbf{W})}{\partial \mathbf{W}}=0
$$

Straight-Through Estimator (STE) simply passes the gradients through the quantization as if it had been the identity function.

$$
g_{\mathbf{W}}=\frac{\partial L}{\partial \mathbf{W}}=\frac{\partial L}{\partial Q(\mathbf{W})}
$$

也就是说，“将被量化”的结点后会插入一个“伪量化”结点。前向传播时，伪量化结点模拟了量化误差，使得模型在微调阶段适应量化误差；反向传播时，伪量化结点的梯度首先会被计算出来，这里STE的意思就是把对【伪量化结点的梯度】作为【将被量化的结点的梯度】



# 参考资料

1. https://leimao.github.io/article/Neural-Networks-Quantization/#Quantization

2. https://zhuanlan.zhihu.com/p/548174416

3. https://www.dropbox.com/scl/fi/1mo0umu0qtq7uxap2l5m3/lec06.pdf?rlkey=bdl2mgusgajddjuvjxb0fot36&dl=0

4. https://zhuanlan.zhihu.com/p/645259854