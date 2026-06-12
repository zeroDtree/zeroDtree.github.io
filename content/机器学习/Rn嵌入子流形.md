---
title: 欧几里得空间中的嵌入子流形
---

- [定义](#定义)
- [引理及其证明](#引理及其证明)
- [证明](#证明)
- [几何直观](#几何直观)

#### 定义

**Definition.** Let $\mathcal{E}=\mathbb{R}^d$. A non-empty subset $\mathcal{M}$ of $\mathcal{E}$ is a (smooth) embedded submanifold of $\mathcal{E}$ of dimension $n$ if either

1. $n = d$ and $\mathcal{M}$ is open in $\mathcal{E}$—we also call this an open submanifold; or
2. $n = d - k$ for some $k \geq 1$ and, for each $x \in \mathcal{M}$, there exists a neighborhood
   $U$ of $x$ in $\mathcal{E}$ and a smooth function $h: U \to \mathbb{R}^k$ such that
   (a) If $y$ is in $U$, then $h(y) = 0$ if and only if $y \in \mathcal{M}$; and
   (b) rank $Dh(x) = k$.
   Such a function $h$ is called a local defining function for $\mathcal{M}$ at $x$.

If $\mathcal{M}$ is a linear (sub)space, we also call it a linear manifold.

**Proposition.** 上述定义的嵌入子流形是光滑流形。

要证明上述命题，需要几个引理。

#### 引理及其证明

**Lemma.** (Inverse function theorem). Suppose $U \subseteq \mathcal{E}$ and $V \subseteq \mathcal{F}$ are open subsets of linear spaces of the same dimension, and $F: U \to V$ is smooth. If $DF(x)$ is invertible at some point $x \in U$, then there exist neighborhoods $U' \subseteq U$ of $x$ and $V' \subseteq V$ of $F(x)$ such that $F|_{U'}: U' \to V'$ (the restriction of $F$ to $U'$ and $V'$) is a diffeomorphism. 即光滑函数如果的雅可比矩阵如果可逆，则存在局部微分同胚。

**Lemma.**(嵌入子流形的等价定义) 设 $\mathcal{E}$ 是一个 $d$ 维线性空间。$\mathcal{E}$ 的子集 $\mathcal{M}$ 是 $\mathcal{E}$ 的维数为 $n = d - k$ 的嵌入子流形，当且仅当对于每个 $x \in \mathcal{M}$，存在 $x$ 在 $\mathcal{E}$ 中的邻域 $U$，$\mathbb{R}^d$ 中的开集 $V$ 以及微分同胚映射 $F: U \to V$，使得 $F(\mathcal{M} \cap U) = E \cap V$，其中 $E = \{y \in \mathbb{R}^d: y_{n+1} = \cdots = y_d = 0\}$ 是 $\mathbb{R}^d$ 的线性子空间。

$\Rightarrow$（必要性）

对于任意$x\in \mathcal{M}$, 设嵌入子流形定义中的邻域和局部定义函数分别为$U''$和$h$

因为$rank(Dh(x))=k$，所以$Dh(x)$是一个$k\times d$的行满纸矩阵

$$
Dh(x) = \begin{pmatrix}
A_{k \times d-k} & B_{k \times k} \\
\end{pmatrix}
$$

通过调整$(y_1,y_2,\cdots,y_d)$的顺序，使得$B$为可逆矩阵。 这样调整的可行性可以考虑在进入$h$前乘以一个置换矩阵，而置换矩阵都是微分同胚映射。

构造一个$F(y)=(y_1,y_2,\cdots,y_{d-k},h_1(y),h_2(y),\cdots,h_k(y))$

$$
DF(y) = \begin{pmatrix}
I_{d-k} & 0 \\
A & B
\end{pmatrix}
$$

显然$DF(y)$是可逆的，根据逆映射定理，存在$U'\subseteq \mathbb{R}^d$和$V'\subseteq \mathbb{R}^d$，使得$F|_{U'}: U' \to V'$是微分同胚。

令$U=U' \cap U''$，$V=F(U)=V' \cap F(U'')$，则$F|_{U}: U \to V$是微分同胚。

$F(\mathcal{M} \cap U) \subseteq E \cap V$ 显然

$F(\mathcal{M} \cap U) \supseteq E \cap V$ ，$\forall z\in E \cap V$，$\exists y\in U$ s.t. $z=F(y)$,$y\in U''$, 因为 $z=F(y)\in E, h(y)=0$, 所以 $y \in \mathcal{M}$，所以$y \in \mathcal{M} \cap U$, 因此$z=F(y)\in F(\mathcal{M} \cap U)$

$\Leftarrow$ 待证明（后面的证明不需要这个充分性）

**Lemma.** $T_xM$ is a linear space, and $Ker(Dh(x))=T_xM$

proof:

$\forall v \in T_xM$,存在一个$M$上的光滑曲线$c:(-1,1) \to M,c(0)=x$ s.t. $c'(0)=v$。

因为$\forall y \in M \cap U,h(y)=0$，所以$h(c(t))=0$，对$t$求导，得到
$\frac{d}{dt}|_{t=0} h(c(t))=Dh(c(0))(c'(0))=0$, 所以$c'(0)=v \in Ker(Dh(x))$

因此$T_xM \subseteq Ker(Dh(x))$。

所以tangent space $T_xM$是$Ker(Dh(x))$的一个子集。注意这个子集现在还不一定是一个线性空间，只有在证明了$T_xM=Ker(Dh(x))$之后，$T_xM$才能说是一个线性空间。下面就去证明$T_xM=Ker(Dh(x))$

根据嵌入子流形的等价定义，存在$U'\subseteq \mathbb{R}^d$和$V'\subseteq \mathbb{R}^d$，使得$F|_{U'}: U' \to V'$是微分同胚，$F(\mathcal{M} \cap U') = E \cap V'$，其中 $E = \{y \in \mathbb{R}^d: y_{n+1} = \cdots = y_d = 0\}$ 是 $\mathbb{R}^d$ 的线性子空间。

构造曲线

$$
\gamma(t) = F(x) + t
\left[
\begin{matrix}
v\\
0
\end{matrix}
\right]
, v \in \mathbb{R}^{d-k}, 0 \in \mathbb{R}^k
$$

$$
c(t) = F^{-1}(\gamma(t))
$$

因为$F$是微分同胚，且$\gamma(t)$光滑，所以$c(t)$光滑。

$$
c'(0) = DF^{-1}(F(x))
\left[
\begin{matrix}
v\\
0
\end{matrix}
\right]
= (DF)^{-1}(F(x))
\left[
\begin{matrix}
v\\
0
\end{matrix}
\right]
$$

有$DF^{-1}$的线性性、可逆性，以及$v$的任意性，所以$T_xM$包含一个维度与$Ker(Dh(x))$相同的线性子空间。因此$T_xM=Ker(Dh(x))$。

#### 证明

证明分以下几步骤

- 证明$\mathcal{M}$是Hausdorff 和second countable的拓扑空间
- 证明$\mathcal{M}$是locally euclidean的拓扑空间,分类讨论
  - (a) $\mathcal{M}$是d维open submanifold
  - (b) $\mathcal{M}$是d-k维 submanifold

$\mathbb{R}^d$是内积空间，内积可以诱导范数，范数可以诱导度量，度量可以诱导拓扑。

$\mathbb{R}^d$是度量空间,而度量空间都是Hausdorff和second countable的，所以$\mathbb{R}^d$是Hausdorff和second countable的。

$\mathcal{M}$是拓扑空间$\mathbb{R}^d$的子集，$\mathcal{M}$是$\mathbb{R}^d$的子空间(相对拓扑)，子空间会继承原空间的Hausdorff和second countable性质，因此$\mathcal{M}$是Hausdorff和second countable的。

下面证明local euclidean性质

若$\mathcal{M}$是d维open submanifold，则$\mathcal{M}$是locally euclidean的，取恒等映射作为local defining function。容易验证满足local euclidean的定义。

若$\mathcal{M}$是d-k维 submanifold,

根据前面的定义等价性引理，存在$U'\subseteq \mathbb{R}^d$和$V'\subseteq \mathbb{R}^d$，使得$F|_{U'}: U' \to V'$是微分同胚，$F(\mathcal{M} \cap U') = E \cap V'$，其中 $E = \{y \in \mathbb{R}^d: y_{d-k+1} = \cdots = y_d = 0\}$ 是 $\mathbb{R}^d$ 的线性子空间。

构造一个同构映射(向量空间之间的同构)

$$
L: E \to \mathbb{R}^k, L(y_1,y_2,\cdots,y_{d-k},0,0,\cdots,0) = (y_1,y_2,\cdots,y_{d-k})
$$

$L$是同构映射，并且易得$L$也是同胚映射(微分同胚)

构造chart

$$
\phi = L \circ F|_{U'}
$$

$L$和$F|_{U'}$都是同胚映射，所以$\phi$也是同胚映射(微分同胚)。

$\mathcal{M} \cap U'$是$\mathcal{M}$的开集(相对开集)，$\phi[\mathcal{M} \cap U']=L[E\cap V']$是$\mathbb{R}^k$的开集。

因此chart 为$(\mathcal{M} \cap U', \phi)$，满足local euclidean的定义。

综上，$\mathcal{M}$是(光滑)流形。

#### 几何直观

考虑三维空间中的一个球$M=\{x \in \mathbb{R}^3 \mid x_1^2 + x_2^2 + x_3^2 = 1\}$

球上一点$p$有一个切平面，切平面是二维的

然后将切平面旋转称一个与xy轴平面平行的平面

从点$p$的邻域向切平面做投影，然后经过旋转变换就得就得到了xy平面上的一个开集

可以想象得到，局部投影是同胚的，旋转变化是可逆的线性变换，因此也是同胚的，同胚复合也是同胚的。所以我们找到了这个chart。
