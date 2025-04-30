---
title: quantization
date: 2024-03-09 08:22:03
tags: 量化
---

- [model compression](#model-compression)
- [quantization](#quantization)
  - [pytorch的quantization](#pytorch的quantization)
    - [1. 根据权重和数据的分布（或最值）确定量化参数scale和zero\_point](#1-根据权重和数据的分布或最值确定量化参数scale和zero_point)
      - [其中的最大值和最小值不一定是“真实”的最大值和最小值](#其中的最大值和最小值不一定是真实的最大值和最小值)
    - [2. 量化](#2-量化)
    - [pytorch的量化误差](#pytorch的量化误差)
- [PTQ and QAT](#ptq-and-qat)
  - [PTQ(Post Training Qunatization)](#ptqpost-training-qunatization)
  - [QAT(Quantization Aware Training)](#qatquantization-aware-training)
    - [关于QAT中的伪量化](#关于qat中的伪量化)
- [paper(OneBit: Towards Extremely Low-bit Large Language Models)](#paperonebit-towards-extremely-low-bit-large-language-models)
  - [rank-1 approximation](#rank-1-approximation)
  - [proposition 1](#proposition-1)
    - [proof](#proof)
  - [lemma 1](#lemma-1)
    - [Proof](#proof-1)
  - [proposition 2](#proposition-2)
    - [proof](#proof-2)
  - [知识蒸馏](#知识蒸馏)
- [参考资料](#参考资料)


# model compression
模型压缩（轻量化）的四种常见方法

1. pruning
把权重矩阵W中的某些元素置0,希望对输出结果影响较小。
如果置0的时候按行或按列或按块，就称为结构化剪枝，否则为非结构化剪枝。
剪枝的时候可以调整权重来补偿剪枝带来的误差

2. knowledge distillation
训练一个较小的模型，用大模型（教师模型）来指导小模型（学生模型），学生模型不仅要去拟合数据，也要去逼近教师模型的分布。例如可以通过损失函数的定义来实现。例如$l = l_{1} + \alpha l_2$

3. matrix decomposition
将原来(矩阵的形状)大的权重矩阵分解成多个小的(低秩的)矩阵，用低秩矩阵近似原有权重矩阵。这样可以大大降低模型分解之后的计算量

4. 把实数上的运算转化到整数域上，加速运算和减少存储需求。
  

# quantization
把浮点数上的存储和运算转化成整数的存储和运算。
$[a,b]$上的运算转化到$[c,d]$, 其中$[a,b]$是连续的，$[c,d]$是离散的整数。
$x_R$被量化后的指为$x_I$, $x_I$被反量化后的值为$x_Q$

$x_I = round((x_R-a)(\frac{d-c}{b-a}) + c)$
$x_Q = (x_I - c)(\frac{b-a}{d-c}) + a$

把$\frac{b-a}{d-c}$记作s
$$
x_I = round((x_R-a)(\frac{1}{s}) + c) \tag{1}
$$
$$
x_Q = (x_I - c)s + a \tag{2}
$$
把$x_I$带入$x_Q$中
$$
x_Q = round((x_R-a)(\frac{1}{s}))s + a \tag{3}
$$

如果$x_R$不在$[a,b]$内,那$x_I$也极有可能不在[c,d]内。
如果$x_I$超出了[c,d],那就取较近的边界值。
$$
  x_I = clip(round((x_R-a)(\frac{1}{s}) + c), c, d) \tag{4}
$$
$$
  x_Q = (clip(round((x_R-a)(\frac{1}{s}) + c), c, d) - c)s + a \tag{5}
$$

观察上述(1),(2),(3),(4)可以不依赖与区间$[a,b]$和$[c,d]$的存在。可以看作对整个数轴的线性变换。s为缩放比例。a和c决定的平移。

我们假设值都在正常范围内，没有超出$[c,d]$，不考虑clip(即使用(3)中的$x_Q$)
$x_Q = x_R + \epsilon$
$$
  \begin{aligned}
  \epsilon &= x_Q - x_R\\
           &= round((x_R-a)(\frac{1}{s}))s + a - x_R\\
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
                &z = Q_\text{min} - \text{round}(x_\text{min} / s)
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
  x_I = round(\frac{x_R}{s}) + z
$$
$$
x_Q = (x_I - z)s
$$
$$
x_Q = (round(\frac{x_R}{s}))s
$$
这样量化使得整数z对应实数0

### pytorch的量化误差
量化误差和之前得到的一样。
$$
  \begin{aligned}
  \epsilon &= x_Q - x_R\\
           &= round((x_R)(\frac{1}{s}))s - x_R\\
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
  x_Q = (clip(round((x_R-a)(\frac{1}{s}) + c), c, d) - c)s + a
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


# paper(OneBit: Towards Extremely Low-bit Large Language Models)
## rank-1 approximation
奇异值分解
$A = U\Sigma V^T$
取最大的奇异值($\sigma_1$)，和最大的奇异值对应的左奇异向量和右奇异向量
$\hat{A} = u_1 \sigma_1  v_1^T$

(《Foundations of Data Science》的3.5节证明了这样分解是Frobenius范数下最好的秩1分解，证明我还没看)

$W = W_{sign} \odot W_{value}$ (符号和绝对值的Hadamard积)

$W_{value} = ab^T$ (也就是说把矩阵的绝对值秩1分解)

$W_{value} \approx W_{sign} \odot (a b^T)$

## proposition 1
$\mathbf{X} \mathbf{W}^{\mathrm{T}} \approx\left[\left(\mathbf{X} \odot \mathbf{b}^{\mathrm{T}}\right) \mathbf{W}_{\text {sign }}^{\mathrm{T}}\right] \odot \mathbf{a}^{\mathrm{T}}$
这个命题的是为了得到想到的网络结构。这个里面的b和a就是模型架构里的g和h，其中$X\odot b^T$操作表示对$b^T$进行广播（$b^T$是一个行向量，广播的意思就是把$b^T$一行一行重复地排列下去，直到和X的形状一样。），然后和X作hadamard积。
### proof 
$w_{i j} \approx s_{i j} \cdot a_i b_j$, where $s_{i j}$ is the element of $\mathbf{W}_{\text {sign }}$. Hence we have
$$
\begin{aligned}
\left(\mathbf{X} \mathbf{W}^{\mathrm{T}}\right)_{i j} & = \sum_k x_{i k} w_{k j}^{\mathrm{T}}=\sum_k x_{i k} w_{j k} \\
& \approx \sum_k x_{i k} s_{j k} a_j b_k \\
& =\sum_k x_{i k} b_k s_{j k} a_j \\
& =\sum_k\left(\mathbf{X} \odot \mathbf{b}^{\mathrm{T}}\right)_{i k} s_{k j}^{\mathrm{T}} a_j \\
& =\left[\left(\mathbf{X} \odot \mathbf{b}^{\mathrm{T}}\right) \mathbf{W}_{\text {sign }}^{\mathrm{T}}\right]_{i j} a_j \\
& =\left\{\left[\left(\mathbf{X} \odot \mathbf{b}^{\mathrm{T}}\right) \mathbf{W}_{\text {sign }}^{\mathrm{T}}\right] \odot \mathbf{a}^{\mathrm{T}}\right\}_{i j} .
\end{aligned}
$$

## lemma 1
Let $\sigma_i(\mathbf{W})$ denote the $i$-th biggest singular value of matrix $\mathbf{W}$. The following inequality holds:
$$
\sigma_1(|\mathbf{W}|) \geq \sigma_1(\mathbf{W}) .
$$

### Proof
According to the definition of induced norm, there are
$$
\begin{gathered}
\sigma_1(\mathbf{W})=\|\mathbf{W}\|_2=\max _{\mathbf{x},\|\mathbf{x}\|_2=1}\|\mathbf{W} \mathbf{x}\|_2, \\
\sigma_1(|\mathbf{W}|)=\|\mathbf{W}\|_2=\max _{\mathbf{y},\|\mathbf{y}\|_2=1}\||\mathbf{W}| \mathbf{y}\|_2 .
\end{gathered}
$$

Note that for $\forall \mathbf{x},\|\mathbf{x}\|_2=1$ and we have
$$
\begin{aligned}
\left\|\left|\mathbf{W}\|\mathbf{x} \mid\|_2^2\right.\right. & =\sum_i\left(\sum_j\left|w_{i j}\right|\left|x_j\right|\right)^2 \\
& \geq \sum_i\left(\left|\sum_j w_{i j} x_j\right|\right)^2 \\
& =\sum_i\left(\sum_j w_{i j} x_j\right)^2=\|\mathbf{W} \mathbf{x}\|_2^2 .
\end{aligned}
$$
因为我们总是可以让y取x的绝对值，所以：
$$
\max _{\mathbf{y},\|\mathbf{y}\|_2=1}\||\mathbf{W}| \mathbf{y}\|_2 \geq \max _{\mathbf{x},\|\mathbf{x}\|_2=1}\|\mathbf{W} \mathbf{x}\|_2 .
$$
This lemma is proved.

## proposition 2
Given matrices $\mathbf{W}$ and $|\mathbf{W}|$, $\mathbf{W}=\mathbf{W}_{\text {sign }} \odot|\mathbf{W}|$. We decompose these matrices in the way $\mathbf{W}=\mathbf{a} \mathbf{b}^{\mathrm{T}}+\mathbf{E}_1$ and $|\mathbf{W}|=\tilde{\mathbf{a}} \tilde{\mathbf{b}}^{\mathrm{T}}+\mathbf{E}_2$, where $\mathbf{E}_i$ denotes the error matrices. In terms of the Frobenius-norm, the SVID is closer to the original matrix $\mathbf{W}$ :
$$
\left\|\mathbf{W}-\mathbf{W}_{\text {sign }} \odot \tilde{\mathbf{a}} \tilde{\mathbf{b}}^T\right\|_F^2 \leq\left\|\mathbf{W}-\mathbf{a} \mathbf{b}^T\right\|_F^2 .
$$
这个命题主要想说，在Frobenius范数意义下，先取绝对值再分解比直接分解的误差小。

### proof
Here we consider SVD to prove it. For SVD, the norm of the error matrix $\mathbf{E}$ in the rank1 approximation is the sum of the squares of all singular values except for the largest one. We have
$E = A - \hat{A}= A - u_1 \sigma_1 v_1^T$

$\|E\|_F^2=\sum_{i, j}\left(A_{i j}-\sigma_1 u_{1 i} v_{1 j}\right)^2$

$\|E\|_F^2=\sum_{i, j} A_{i j}^2-2 \sigma_1 \sum_{i, j} A_{i j} u_{1 i} v_{1 j}+\sigma_1^2 \sum_{i, j} u_{1 i}^2 v_{1 j}^2$

u和v是U和V里的奇异向量，$u_1*\sigma_1 = Av_1$, 且u和v都是单位向量。$\sum_{i, j} u_{1 i}^2 v_{1 j}^2 = (|u_1|^2\  |u_1|^2) = 1$,所以

$\|E\|_F^2=\sum_{i, j} A_{i j}^2-2 \sigma_1 \sum_{i, j} A_{i j} u_{1 i} v_{1 j}+\sigma_1^2$

然后使用迹技巧

$\begin{aligned} & \sum_{i, j} A_{i j} u_{1 i} v_{1 j}=\operatorname{tr}\left(A^T u_1 v_1^T\right) \\ & =\operatorname{tr}\left(v_1^T A^T u_1\right) \\ & =\operatorname{tr}\left(u_1^T \sigma_1 u_1\right) \\ & =\sigma_1 \operatorname{tr}\left(u_1^T u_1\right) \\ & =\sigma_1\left(v_1^T u_1\right)
\\ &= \sigma_1
\end{aligned}$

所以

$\begin{aligned} & \|E\|_F^2=\sum_{i, j} A_{i j}^2-2 \sigma_1^2+\sigma_1^2 \\ & \|E\|_F^2=\sum_{i, j} A_{i j}^2-\sigma_1^2\end{aligned}$

因为矩阵的Frobenius范数的平方等于矩阵的所有奇异值的平方和，即

$\|\boldsymbol{A}\|_F=\sqrt{\sigma_1^2+\sigma_2^2+\ldots+\sigma_n^2}$

所以误差矩阵的Frobenius范数的平方等于除了最大奇异值的其他所有奇异值的平方和。
$$
\begin{gathered}
\left\|\mathbf{E}_1\right\|_F^2=\sum_{i=2}^n \sigma_i^2(\mathbf{W}), \\
\left\|\mathbf{E}_2\right\|_F^2=\sum_{i=2}^n \sigma_i^2(|\mathbf{W}|) .
\end{gathered}
$$

Based on $\|\mathbf{W}\|_F^2=\||\mathbf{W}|\|_F^2$, we have
$$
\sum_{i=1}^n \sigma_i^2(\mathbf{W})=\sum_{i=1}^n \sigma_i^2(|\mathbf{W}|) .
$$

According to Lemma 1, we can conclude
$$
\left\|\mathbf{E}_2\right\|_F^2 \leq\left\|\mathbf{E}_1\right\|_F^2 .
$$

From the equation in this proposition, we can formulate
$$
\mathbf{W}_{\text {sign }} \odot|\mathbf{W}|=\mathbf{W}_{\text {sign }} \odot \overline{\mathbf{a}} \tilde{\mathbf{b}}^{\mathrm{T}}+\mathbf{W}_{\text {sign }} \odot \mathbf{E}_{2 .}
$$

Hence we have
$$
\mathbf{W}-\mathbf{W}_{\text {sign }} \odot \overline{\mathbf{a}} \tilde{\mathbf{b}}^{\mathrm{T}}=\mathbf{W}_{\text {sign }} \odot \mathbf{E}_2 .
$$

Therefore
$$
\begin{aligned}
\left\|\mathbf{W}_{\text {sign }} \odot \mathbf{E}_2\right\|_F^2 & =\sum_{i, j} s_{i j}^2 e_{i j}^2=\sum_{i, j} e_{i j}^2 \\
& =\left\|\mathbf{E}_2\right\|_F^2 \leq\left\|\mathbf{E}_1\right\|_F^2,
\end{aligned}
$$
where $s_{i j}= \pm 1$ is the element of $\mathbf{W}_{\text {sign }}$. Hence the inequation in this proposition is proved.

## 知识蒸馏
这里就是用命题1得到的Y的表达式。
$$\begin{array}{r}\mathbf{W}_{ \pm 1}=\operatorname{Sign}(\mathbf{W}), \\ \mathbf{Y}=\left[(\mathbf{X} \odot \mathbf{g}) \mathbf{W}_{ \pm 1}^{\mathrm{T}}\right] \odot \mathbf{h}, \\ \mathbf{Z}=\text { LayerNorm }(\mathbf{Y}),\end{array}$$

$$
\mathcal{L}_{\mathrm{CE}}=-\frac{1}{n_s} \sum_{i=1}^{n_s} \sum_c P_c^{\mathcal{T}}\left(\mathbf{o}_i\right) \log P_c^{\mathcal{S}}\left(\mathbf{o}_i\right),
$$
where $c$ denotes the number of classes and $n_s$ denotes the number of training samples in the current batch. $\mathcal{T}$ and $\mathcal{S}$ are the teacher model and student model, respectively. The error of hidden states is defined as
$$
\mathcal{L}_{\text {MSE }}=\sum_{i=1}^{n_s} \sum_{j=1}^{n_l}\left\|\frac{\mathbf{q}_{i, j}^{\mathcal{T}}}{\left\|\mathbf{q}_{i, j}^{\mathcal{T}}\right\|_2}-\frac{\mathbf{q}_{i, j}^{\mathcal{S}}}{\left\|\mathbf{q}_{i, j}^{\mathcal{S}}\right\|_2}\right\|_2^2,
$$
where $n_l$ denotes the number of layers and $\mathbf{q}$ denotes the hidden state. Hence the final objective function can be formulated as
$$
\mathcal{L}_{\mathrm{KD}}=\mathcal{L}_{\mathrm{CE}}+\alpha \mathcal{L}_{\mathrm{MSE}},
$$

$L_{CE}$使得学生模型在输出上接近教师模型。
$L_{MSE}$使得学生模型在内部参数上接近教师模型。


# 参考资料
1. https://leimao.github.io/article/Neural-Networks-Quantization/#Quantization

2. https://zhuanlan.zhihu.com/p/548174416

3. https://www.dropbox.com/scl/fi/1mo0umu0qtq7uxap2l5m3/lec06.pdf?rlkey=bdl2mgusgajddjuvjxb0fot36&dl=0

4. https://zhuanlan.zhihu.com/p/645259854

5. 论文：OneBit: Towards Extremely Low-bit Large Language Models

6. 论文：Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference

7. 论文：A Survey on Model Compression for Large Language Models