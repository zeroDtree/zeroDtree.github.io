---
title: PCA
---

## 目标

找到一个线性变换，将数据投影到低维空间，使得投影后的数据方差最大。

## 方法

设$X \in \mathbb{R}^{n \times p}$,每一行表示一个$p$维的样本，$n$是样本数，$p$是特征数。$X_i$表示第$i$个样本，$X_i \in \mathbb{R}^p$被视作列向量。

我们希望找到一个单位向量 $\mathbf{w} \in \mathbb{R}^p$，使得数据在这个方向上的方差最大：$Var(X\mathbf{w})$

$$
\overline{X} := \frac{1}{n} \sum_{i=1}^n X_i
$$

$$
\tilde{X} := X - \mathbf{1} \overline{X}^T
$$

$$
\overline{X\mathbf{w}} = \frac{1}{n} \sum_{i=1}^n (X \mathbf{w})_i = \frac{1}{n} \sum_{i=1}^n X_i^T \mathbf{w} = \overline{X}^T \mathbf{w}
$$

$$
\begin{aligned}
Var(X\mathbf{w}) &= \frac{1}{n-1} (X\mathbf{w} - \mathbf{1} \overline{X\mathbf{w}})^T (X\mathbf{w} - \mathbf{1} \overline{X\mathbf{w}}) \\
& = \frac{1}{n-1} (X\mathbf{w} - \mathbf{1} \overline{X}^T \mathbf{w})^T(X\mathbf{w} - \mathbf{1} \overline{X}^T \mathbf{w})\\
&= \frac{1}{n-1} (\tilde{X} \mathbf{w})^T (\tilde{X} \mathbf{w}) \\
&= \frac{1}{n-1} \mathbf{w}^T \tilde{X}^T \tilde{X} \mathbf{w} \\
\end{aligned}
$$

$
\Sigma := \tilde{X}^T \tilde{X}
$

由于$\Sigma$是对称矩阵，因此$\Sigma$可以分解为$\Sigma = Q \Lambda Q^T$，其中$Q$是正交矩阵，$\Lambda$是对角矩阵。$\Lambda = \text{diag}(\lambda_1, \lambda_2, \cdots, \lambda_p)$，且$\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_p \geq 0$。

$
\mathbf{z} := Q^T \mathbf{w}
$

最大化$Var(X\mathbf{w})$等价于最大化$\mathbf{w}^T \tilde{X}^T \tilde{X} \mathbf{w}$，即最大化$\mathbf{w}^T \Sigma \mathbf{w}$，等价于最大化$\mathbf{w}^T Q \Lambda Q^T \mathbf{w}$，即最大化$\mathbf{z}^T \Lambda \mathbf{z}$，即最大化$\sum_{i=1}^p \lambda_i z_i^2$且$\| \mathbf{z} \|_2 = 1$。

易得当$\mathbf{z} = (1, 0, \cdots, 0)^T$时，$\mathbf{w}^T \Sigma \mathbf{w}$取得最大值。

$$
\begin{aligned}
Q^T \mathbf{w} &= (1, 0, \cdots, 0)^T \\
\mathbf{w} &= Q (1, 0, \cdots, 0)^T \\
\end{aligned}
$$

也就是$\mathbf{w}$为$\Sigma$的最大的特征值对应的特征向量。将此$\mathbf{w}$记作$\mathbf{w}_1$

接下来寻找使得方差第二大的方向$\mathbf{w}_2$。且要与$\mathbf{w}_1$正交。

因为$Q$为正交矩阵，所以若$\mathbf{w}_2$与$\mathbf{w}_1$正交，则$Q^T \mathbf{w}_2$与$Q^T \mathbf{w}_1$正交，即$Q^T \mathbf{w}_2$的第一个分量为0。

易得$\mathbf{w}_2$为$\Sigma$的第二个特征值对应的特征向量。
