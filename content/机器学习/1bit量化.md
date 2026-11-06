# paper(OneBit: Towards Extremely Low-bit Large Language Models)

## rank-1 approximation

奇异值分解
$A = U\Sigma V^T$
取最大的奇异值($\sigma_1$)，和最大的奇异值对应的左奇异向量和右奇异向量
$\hat{A} = u_1 \sigma_1  v_1^T$

(《Foundations of Data Science》的3.5节证明了这样分解是Frobenius范数下最好的秩1分解，证明我还没看)

$W = W_{sign} \odot W_{value}$，其中 $W_{value}=|W|$，$W_{sign}=\mathrm{Sign}(W)$（符号和绝对值的 Hadamard 积）

$W_{value} \approx ab^T$（把绝对值矩阵做秩 1 分解）

$W \approx W_{sign} \odot (ab^T)$

## proposition 1

$\mathbf{X} \mathbf{W}^{\mathrm{T}} \approx\left[\left(\mathbf{X} \odot \mathbf{b}^{\mathrm{T}}\right) \mathbf{W}_{\text {sign }}^{\mathrm{T}}\right] \odot \mathbf{a}^{\mathrm{T}}$
这个命题的是为了得到想到的网络结构。其中$b^T$赋给模型架构里的$g$，$a^T$赋给$h$。$X\odot b^T$操作表示对$b^T$进行广播（$b^T$是一个行向量，广播的意思就是把$b^T$一行一行重复地排列下去，直到和X的形状一样。），然后和X作hadamard积。

> [!note]- 证明
> $w_{i j} \approx s_{i j} \cdot a_i b_j$, where $s_{i j}$ is the element of $\mathbf{W}_{\text {sign }}$. Hence we have
>
> $$
> \begin{aligned}
> \left(\mathbf{X} \mathbf{W}^{\mathrm{T}}\right)_{i j} & = \sum_k x_{i k} w_{k j}^{\mathrm{T}}=\sum_k x_{i k} w_{j k} \\
> & \approx \sum_k x_{i k} s_{j k} a_j b_k \\
> & =\sum_k x_{i k} b_k s_{j k} a_j \\
> & =\sum_k\left(\mathbf{X} \odot \mathbf{b}^{\mathrm{T}}\right)_{i k} s_{k j}^{\mathrm{T}} a_j \\
> & =\left[\left(\mathbf{X} \odot \mathbf{b}^{\mathrm{T}}\right) \mathbf{W}_{\text {sign }}^{\mathrm{T}}\right]_{i j} a_j \\
> & =\left\{\left[\left(\mathbf{X} \odot \mathbf{b}^{\mathrm{T}}\right) \mathbf{W}_{\text {sign }}^{\mathrm{T}}\right] \odot \mathbf{a}^{\mathrm{T}}\right\}_{i j} .
> \end{aligned}
> $$
## lemma 1

Let $\sigma_i(\mathbf{W})$ denote the $i$-th biggest singular value of matrix $\mathbf{W}$. The following inequality holds:

$$
\sigma_1(|\mathbf{W}|) \geq \sigma_1(\mathbf{W}) .
$$

> [!note]- 证明
> According to the definition of induced norm, there are
>
> $$
> \begin{gathered}
> \sigma_1(\mathbf{W})=\|\mathbf{W}\|_2=\max _{\mathbf{x},\|\mathbf{x}\|_2=1}\|\mathbf{W} \mathbf{x}\|_2, \\
> \sigma_1(|\mathbf{W}|)=\bigl\||\mathbf{W}|\bigr\|_2=\max _{\mathbf{y},\|\mathbf{y}\|_2=1}\||\mathbf{W}| \mathbf{y}\|_2 .
> \end{gathered}
> $$
>
> Note that for $\forall \mathbf{x},\|\mathbf{x}\|_2=1$ and we have
>
> $$
> \begin{aligned}
> \bigl\||\mathbf{W}|\,|\mathbf{x}|\bigr\|_2^2 & =\sum_i\left(\sum_j\left|w_{i j}\right|\left|x_j\right|\right)^2 \\
> & \geq \sum_i\left(\left|\sum_j w_{i j} x_j\right|\right)^2 \\
> & =\sum_i\left(\sum_j w_{i j} x_j\right)^2=\|\mathbf{W} \mathbf{x}\|_2^2 .
> \end{aligned}
> $$
>
> 因为我们总是可以让y取x的绝对值，所以：
>
> $$
> \max _{\mathbf{y},\|\mathbf{y}\|_2=1}\||\mathbf{W}| \mathbf{y}\|_2 \geq \max _{\mathbf{x},\|\mathbf{x}\|_2=1}\|\mathbf{W} \mathbf{x}\|_2 .
> $$
>
> This lemma is proved.
## proposition 2

Given matrices $\mathbf{W}$ and $|\mathbf{W}|$, $\mathbf{W}=\mathbf{W}_{\text {sign }} \odot|\mathbf{W}|$. We decompose these matrices in the way $\mathbf{W}=\mathbf{a} \mathbf{b}^{\mathrm{T}}+\mathbf{E}_1$ and $|\mathbf{W}|=\tilde{\mathbf{a}} \tilde{\mathbf{b}}^{\mathrm{T}}+\mathbf{E}_2$, where $\mathbf{E}_i$ denotes the error matrices. In terms of the Frobenius-norm, the SVID is closer to the original matrix $\mathbf{W}$ :

$$
\left\|\mathbf{W}-\mathbf{W}_{\text {sign }} \odot \tilde{\mathbf{a}} \tilde{\mathbf{b}}^T\right\|_F^2 \leq\left\|\mathbf{W}-\mathbf{a} \mathbf{b}^T\right\|_F^2 .
$$

这个命题主要想说，在Frobenius范数意义下，先取绝对值再分解比直接分解的误差小。

> [!note]- 证明
> Here we consider SVD to prove it. For SVD, the norm of the error matrix $\mathbf{E}$ in the rank1 approximation is the sum of the squares of all singular values except for the largest one. We have
> $E = A - \hat{A}= A - u_1 \sigma_1 v_1^T$
>
> $\|E\|_F^2=\sum_{i, j}\left(A_{i j}-\sigma_1 u_{1 i} v_{1 j}\right)^2$
>
> $\|E\|_F^2=\sum_{i, j} A_{i j}^2-2 \sigma_1 \sum_{i, j} A_{i j} u_{1 i} v_{1 j}+\sigma_1^2 \sum_{i, j} u_{1 i}^2 v_{1 j}^2$
>
> u和v是U和V里的奇异向量，$u_1*\sigma_1 = Av_1$, 且u和v都是单位向量。$\sum_{i, j} u_{1 i}^2 v_{1 j}^2 = \|u_1\|_2^2 \|v_1\|_2^2 = 1$,所以
>
> $\|E\|_F^2=\sum_{i, j} A_{i j}^2-2 \sigma_1 \sum_{i, j} A_{i j} u_{1 i} v_{1 j}+\sigma_1^2$
>
> 然后使用迹技巧
>
> $\begin{aligned} & \sum_{i, j} A_{i j} u_{1 i} v_{1 j}=\operatorname{tr}\left(A^T u_1 v_1^T\right) \\ & =\operatorname{tr}\left(v_1^T A^T u_1\right) \\ & =\operatorname{tr}\left(u_1^T \sigma_1 u_1\right) \\ & =\sigma_1 \operatorname{tr}\left(u_1^T u_1\right) \\ & =\sigma_1\left(u_1^T u_1\right)
> \\ &= \sigma_1
> \end{aligned}$
>
> 所以
>
> $\begin{aligned} & \|E\|_F^2=\sum_{i, j} A_{i j}^2-2 \sigma_1^2+\sigma_1^2 \\ & \|E\|_F^2=\sum_{i, j} A_{i j}^2-\sigma_1^2\end{aligned}$
>
> 因为矩阵的Frobenius范数的平方等于矩阵的所有奇异值的平方和，即
>
> $\|\boldsymbol{A}\|_F=\sqrt{\sigma_1^2+\sigma_2^2+\ldots+\sigma_n^2}$
>
> 所以误差矩阵的Frobenius范数的平方等于除了最大奇异值的其他所有奇异值的平方和。
>
> $$
> \begin{gathered}
> \left\|\mathbf{E}_1\right\|_F^2=\sum_{i=2}^n \sigma_i^2(\mathbf{W}), \\
> \left\|\mathbf{E}_2\right\|_F^2=\sum_{i=2}^n \sigma_i^2(|\mathbf{W}|) .
> \end{gathered}
> $$
>
> Based on $\|\mathbf{W}\|_F^2=\||\mathbf{W}|\|_F^2$, we have
>
> $$
> \sum_{i=1}^n \sigma_i^2(\mathbf{W})=\sum_{i=1}^n \sigma_i^2(|\mathbf{W}|) .
> $$
>
> According to Lemma 1, we can conclude
>
> $$
> \left\|\mathbf{E}_2\right\|_F^2 \leq\left\|\mathbf{E}_1\right\|_F^2 .
> $$
>
> From the equation in this proposition, we can formulate
>
> $$
> \mathbf{W}_{\text {sign }} \odot|\mathbf{W}|=\mathbf{W}_{\text {sign }} \odot \tilde{\mathbf{a}} \tilde{\mathbf{b}}^{\mathrm{T}}+\mathbf{W}_{\text {sign }} \odot \mathbf{E}_{2}
> $$
>
> Hence we have
>
> $$
> \mathbf{W}-\mathbf{W}_{\text {sign }} \odot \tilde{\mathbf{a}} \tilde{\mathbf{b}}^{\mathrm{T}}=\mathbf{W}_{\text {sign }} \odot \mathbf{E}_2 .
> $$
>
> Therefore
>
> $$
> \begin{aligned}
> \left\|\mathbf{W}_{\text {sign }} \odot \mathbf{E}_2\right\|_F^2 & =\sum_{i, j} s_{i j}^2 e_{i j}^2=\sum_{i, j} e_{i j}^2 \\
> & =\left\|\mathbf{E}_2\right\|_F^2 \leq\left\|\mathbf{E}_1\right\|_F^2,
> \end{aligned}
> $$
>
> where $s_{i j}= \pm 1$ is the element of $\mathbf{W}_{\text {sign }}$. Hence the inequation in this proposition is proved.
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

$\mathcal{L}_{\mathrm{CE}}$使得学生模型在输出上接近教师模型。
$\mathcal{L}_{\mathrm{MSE}}$使得学生模型在隐藏状态上接近教师模型。