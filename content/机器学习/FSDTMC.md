---
title: 有限状态离散时间时齐马尔可夫链(FSDTMC)
---

## 1. 转移矩阵与边缘演化

设时间 $n\in\mathbb Z_{\ge 0}$，状态空间为有限集 $E=\{1,\dots,K\}$，自然信息流为 $\mathcal F_n^X:=\sigma(X_0,\dots,X_n)$。随机过程 $(X_n)_{n\ge 0}$ 称为**时齐有限状态离散时间马尔可夫链**（FSDTMC），如果存在矩阵 $Q=(Q_{ij})_{K\times K}$，使得对任意 $n\in\mathbb Z_{\ge 0}$ 与 $j\in E$，

$$
\mathbb P(X_{n+1}=j\mid\mathcal F_n^X)
= \mathbb P(X_{n+1}=j\mid X_n)
= Q_{X_n,j}
\qquad\mathbb P\text{-a.s.}
$$

```mermaid
flowchart LR
    X0["$$X_0$$"] -->|"$$Q$$"| X1["$$X_1$$"]
    X1 -.-> Xnm1["$$X_{n-1}$$"]
    Xnm1 -->|"$$Q$$"| Xn["$$X_n$$"]
```

当 $\mathbb P(X_n=i)>0$ 时，$Q_{ij}=\mathbb P(X_{n+1}=j\mid X_n=i)$。转移矩阵 $Q$ 是**行随机矩阵**：

$$
Q_{ij}\ge 0,
\qquad
\sum_{j=1}^K Q_{ij}=1,
\qquad
Q\mathbf 1=\mathbf 1,
$$

其中 $\mathbf 1=(1,\dots,1)^\top\in\mathbb R^K$。

由 Markov 性，有限维联合分布为

$$
\mathbb P(X_0=i_0,\dots,X_n=i_n)
= \mathbb P(X_0=i_0)\prod_{k=1}^n Q_{i_{k-1},i_k}.
$$

将时刻 $n$ 的边缘分布写成行向量 $\nu_n\in\mathbb R^{1\times K}$，$(\nu_n)_i=\mathbb P(X_n=i)$。由全概率公式

$$
\mathbb P(X_n=j)
= \sum_{i=1}^K \mathbb P(X_{n-1}=i)\,Q_{ij},
$$

得

$$
\nu_n=\nu_{n-1}Q,
\qquad
\nu_n=\nu_0 Q^n.
$$

## 2. 平稳分布

记概率单纯形为

$$
\Delta_{K-1}
:=
\{\nu\in\mathbb R^{1\times K}:\nu_i\ge 0,\ \nu\mathbf 1=1\}.
$$

若行向量 $\pi\in\Delta_{K-1}$ 满足

$$
\pi Q=\pi,
$$

则称 $\pi$ 为 $Q$ 的**平稳分布**。当初始分布 $\nu_0=\pi$ 时，对任意 $n\ge 0$ 有 $\nu_n=\pi Q^n=\pi$。

## 3. 可达、沟通类与周期

若存在 $n\ge 0$ 使 $(Q^n)_{ij}>0$，称 $j$ 由 $i$ **可达**，记作 $i\to j$（当 $i\neq j$ 时，因 $(Q^0)_{ij}=I_{ij}=0$，必有 $n\ge 1$）。若 $i\to j$ 且 $j\to i$，称 $i$ 与 $j$ **沟通**，记作 $i\leftrightarrow j$。

**命题。** 沟通关系 $\leftrightarrow$ 是 $E$ 上的等价关系。

> [!note]- 证明
> - **自反性**：对任意 $i\in E$，取 $n=0$，有 $(Q^0)_{ii}=I_{ii}=1>0$，故 $i\to i$，从而 $i\leftrightarrow i$。
> - **对称性**：若 $i\leftrightarrow j$，则 $i\to j$ 且 $j\to i$，由定义即有 $j\leftrightarrow i$。
> - **传递性**：设 $i\leftrightarrow j$ 且 $j\leftrightarrow k$。由 $i\to j$ 与 $j\to k$，存在 $m,n\ge 0$ 使 $(Q^m)_{ij}>0$ 且 $(Q^n)_{jk}>0$。由矩阵乘法及 $Q$ 的非负性
> 
>   $$
>   (Q^{m+n})_{ik}
>   = \sum_{\ell=1}^K (Q^m)_{i\ell}(Q^n)_{\ell k}
>   \ge (Q^m)_{ij}(Q^n)_{jk}
>   > 0,
>   $$
>   故 $i\to k$。同理，由 $k\to j$ 与 $j\to i$ 可得 $k\to i$。因此 $i\leftrightarrow k$。
>
> 综上，$\leftrightarrow$ 满足自反性、对称性与传递性，是 $E$ 上的等价关系。$\square$

等价关系 $\leftrightarrow$ 将 $E$ 划分为互不相交的等价类，称为**沟通类**。当 $E$ 只有一个沟通类时，称链**不可约**。

沟通类 $C$ 称为**闭沟通类**，如果

$$
i\in C,\ j\notin C
\implies
Q_{ij}=0.
$$

若存在 $j\in C$ 使 $i\to j$（由类内状态互通及传递性，这等价于对任意 $j\in C$ 均有 $i\to j$），称状态 $i$ **可到达沟通类** $C$。

**命题。** 有限状态链至少存在一个闭沟通类，且每个状态都能到达某个闭沟通类。

> [!note]- 证明
> 任取初始状态 $y_0\in E$，记其所在的沟通类为 $C^{(0)}$。按如下方式归纳构造状态序列 $y_0,y_1,\dots$ 及其所在的沟通类 $C^{(0)},C^{(1)},\dots$：
>
> 设已得到 $y_0,y_1,\dots,y_k$ 及沟通类 $C^{(0)},C^{(1)},\dots,C^{(k)}$（$y_p\in C^{(p)}$），满足
>
> $$
> y_0\to y_1\to\cdots\to y_k.
> $$
>
> - 若 $C^{(k)}$ 是闭沟通类，则构造终止。此时由可达关系的传递性有 $y_0\to y_k\in C^{(k)}$，即 $y_0$ 可到达闭沟通类 $C^{(k)}$。
> - 若 $C^{(k)}$ 不是闭沟通类，由定义知存在 $x_k\in C^{(k)}$ 与 $y_{k+1}\notin C^{(k)}$ 使 $Q_{x_k y_{k+1}}>0$（从而 $x_k\to y_{k+1}$）。记 $y_{k+1}$ 所在的沟通类为 $C^{(k+1)}$。因 $y_k,x_k\in C^{(k)}$，有 $y_k\to x_k$，故 $y_k\to y_{k+1}$。
>
> 下证新沟通类 $C^{(k+1)}$ 与已有的 $C^{(0)},\dots,C^{(k)}$ 均不相同。若存在 $0\le p\le k$ 使 $C^{(k+1)}=C^{(p)}$，则 $y_{k+1}$ 与 $y_p$ 属于同一沟通类，故 $y_{k+1}\to y_p$；结合 $y_p\to\cdots\to y_k$ 得 $y_{k+1}\to y_k$。又已知 $y_k\to y_{k+1}$，故 $y_k\leftrightarrow y_{k+1}$，即 $y_{k+1}\in C^{(k)}$，与 $y_{k+1}\notin C^{(k)}$ 的选取矛盾。
>
> 因此，构造每延续一步都会产生一个新的沟通类。由于有限集 $E=\{1,\dots,K\}$ 至多划分为 $K$ 个互不相交的沟通类，该构造至多进行 $K-1$ 步必终止于某个闭沟通类 $C^{(r)}$（$0\le r\le K-1$），且 $y_0\to y_r\in C^{(r)}$。
>
> 由 $y_0\in E$ 的任意性，每个状态都能到达某个闭沟通类；特别地，因 $E\neq\emptyset$，至少存在一个闭沟通类。$\square$

记全部闭沟通类为 $C_1,\dots,C_m$（$m\ge 1$），其余状态构成的集合

$$
T:=E\setminus\bigcup_{k=1}^m C_k
$$

称为**暂态集**，$T$ 中的状态称为**暂态**。

对状态 $i$，若返回步数集合 $\{n\ge 1:(Q^n)_{ii}>0\}$ 非空，定义其**周期**为

$$
d(i):=\gcd\{n\ge 1:(Q^n)_{ii}>0\}.
$$

$d(i)=1$ 时称 $i$ 非周期，$d(i)>1$ 时称 $i$ 为周期状态。在有限不可约链中，每个状态的返回步数集合都非空（$|E|=1$ 时 $Q_{11}=1$；$|E|\ge 2$ 时取 $j\neq i$，由 $i\to j\to i$ 即得正长度返回路径）。

**命题。** 同一沟通类中的状态具有相同的周期。

> [!note]- 证明
> 设 $i\leftrightarrow j$，且 $i$ 的返回步数集合非空。取 $r,s\ge 1$ 使 $(Q^r)_{ij}>0$、$(Q^s)_{ji}>0$。因 $Q$ 的各次幂均为非负矩阵，由矩阵乘法 $Q^{s+r}=Q^s Q^r$ 并只保留求和中的 $k=i$ 项，得
>
> $$
> (Q^{s+r})_{jj}
> = \sum_{k=1}^K (Q^s)_{jk}(Q^r)_{kj}
> \ge (Q^s)_{ji}(Q^r)_{ij}
> > 0,
> $$
>
> 故 $j$ 的返回步数集合非空，且 $d(j)\mid(s+r)$。对任意满足 $(Q^n)_{ii}>0$ 的 $n\ge 1$，由 $Q^{s+n+r}=Q^s Q^n Q^r$ 并只保留双重求和中的 $(k,\ell)=(i,i)$ 项，有
>
> $$
> \begin{aligned}
> (Q^{s+n+r})_{jj}
> &= \sum_{\ell=1}^K (Q^{s+n})_{j\ell}(Q^r)_{\ell j} \\
> &= \sum_{k=1}^K\sum_{\ell=1}^K (Q^s)_{jk}(Q^n)_{k\ell}(Q^r)_{\ell j} \\
> &\ge (Q^s)_{ji}(Q^n)_{ii}(Q^r)_{ij}
> > 0,
> \end{aligned}
> $$
>
> 故 $d(j)\mid(s+n+r)$。结合 $d(j)\mid(s+r)$ 得 $d(j)\mid n$。由 $n$ 的任意性知 $d(j)\mid d(i)$。交换 $i,j$ 得 $d(i)\mid d(j)$，故 $d(i)=d(j)$。$\square$

不可约链的所有状态具有共同周期 $d$；$d=1$ 时称链**非周期**。

例如二状态交替链

$$
Q=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}
$$

不可约，周期 $d=2$，由 $\pi Q=\pi$ 与 $\pi\mathbf 1=1$ 得唯一平稳分布 $\pi=(1/2,1/2)$。对任意初始分布 $\nu_0=(a,b)$（$a,b\ge 0$，$a+b=1$），有

$$
\nu_1
= \nu_0 Q
= (a,b)
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}
= (b,a),
\qquad
\nu_2
= \nu_1 Q
= (b,a)
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}
= (a,b).
$$

一般地，$\nu_{2k}=(a,b)$，$\nu_{2k+1}=(b,a)$。当 $a\neq b$ 时，$\nu_n$ 在 $(a,b)$ 与 $(b,a)$ 之间交替，极限不存在。

## 4. 平稳分布的存在性

**命题。** 每个有限状态行随机矩阵 $Q$ 都至少有一个平稳分布。

> [!note]- 证明一：左特征向量
> 由 $Q\mathbf 1=\mathbf 1$ 知 $\det(Q-I)=0$，从而 $\det(Q^\top-I)=0$。故存在非零实向量 $\mathbf v\in\mathbb R^{1\times K}$ 满足
>
> $$
> \mathbf v Q=\mathbf v.
> $$
>
> 对第 $j$ 个分量应用三角不等式及 $Q_{ij}\ge 0$：
>
> $$
> |v_j|
> = \left|\sum_{i=1}^K v_i Q_{ij}\right|
> \le \sum_{i=1}^K |v_i| Q_{ij}.
> $$
>
> 记 $|\mathbf v|=(|v_1|,\dots,|v_K|)$，则逐分量有 $|\mathbf v|\le|\mathbf v|Q$。两边右乘 $\mathbf 1$，由 $Q\mathbf 1=\mathbf 1$ 得
>
> $$
> |\mathbf v|\mathbf 1
> \le |\mathbf v|Q\mathbf 1
> = |\mathbf v|\mathbf 1.
> $$
>
> 因 $|\mathbf v|Q-|\mathbf v|$ 各分量非负且分量之和为 $0$，故
>
> $$
> |\mathbf v|Q=|\mathbf v|.
> $$
>
> 由 $\mathbf v\neq\mathbf 0$ 知 $S:=|\mathbf v|\mathbf 1>0$。令 $\pi:=S^{-1}|\mathbf v|$，则 $\pi\in\Delta_{K-1}$ 且 $\pi Q=\pi$。$\square$

> [!note]- 证明二：Cesàro 平均
> 任取 $\nu_0\in\Delta_{K-1}$，定义
>
> $$
> \bar\nu_N
> :=
> \frac1N\sum_{n=0}^{N-1}\nu_0 Q^n\in\Delta_{K-1}.
> $$
>
> 右乘 $Q$ 作差：
>
> $$
> \begin{aligned}
> \bar\nu_N Q-\bar\nu_N
> &=
> \frac1N\sum_{n=0}^{N-1}
> \bigl(\nu_0 Q^{n+1}-\nu_0 Q^n\bigr)
> \\
> &=
> \frac1N(\nu_0 Q^N-\nu_0).
> \end{aligned}
> $$
>
> 因 $\nu_0 Q^N,\nu_0\in\Delta_{K-1}$，对每个分量 $j$ 有
>
> $$
> \bigl|(\bar\nu_N Q-\bar\nu_N)_j\bigr|
> = \frac1N\bigl|(\nu_0 Q^N)_j-(\nu_0)_j\bigr|
> \le \frac1N,
> $$
>
> 故 $\bar\nu_N Q-\bar\nu_N\to\mathbf 0$。由于 $\Delta_{K-1}$ 是 $\mathbb R^{1\times K}$ 中的有界闭集（紧集），序列 $(\bar\nu_N)$ 存在收敛子列 $\bar\nu_{N_k}\to\pi\in\Delta_{K-1}$（$k\to\infty$）。沿该子列取极限，由矩阵乘法的连续性得
>
> $$
> \mathbf 0
> = \lim_{k\to\infty}(\bar\nu_{N_k}Q-\bar\nu_{N_k})
> = \Bigl(\lim_{k\to\infty}\bar\nu_{N_k}\Bigr)Q - \lim_{k\to\infty}\bar\nu_{N_k}
> = \pi Q-\pi,
> $$
>
> 即 $\pi Q=\pi$。$\square$

## 5. 平稳分布的唯一性

**定理。** 若 $Q$ 不可约，则平稳分布 $\pi$ 唯一，并且对所有 $i\in E$ 有 $\pi_i>0$。

> [!note]- 证明
> 平稳分布的存在性已由上一节命题保证。先证一个基本性质：若非负行向量 $\mathbf u\in\mathbb R^{1\times K}$（$\mathbf u\ge\mathbf 0$）满足 $\mathbf u Q=\mathbf u$，且存在 $i\in E$ 使 $u_i>0$，则对所有 $j\in E$ 均有 $u_j>0$。事实上，由 $\mathbf u Q=\mathbf u$ 归纳可得对任意 $n\ge 0$ 有 $\mathbf u Q^n=\mathbf u$。对任意 $j\in E$，由不可约性（$i\to j$）存在 $n\ge 0$ 使 $(Q^n)_{ij}>0$。因 $\mathbf u$ 与 $Q^n$ 的各分量均非负，只保留求和中的 $k=i$ 项即得
>
> $$
> u_j
> = (\mathbf u Q^n)_j
> = \sum_{k=1}^K u_k(Q^n)_{kj}
> \ge u_i(Q^n)_{ij}
> > 0.
> $$
>
> 换言之，满足 $\mathbf u\ge\mathbf 0$ 与 $\mathbf u Q=\mathbf u$ 的向量要么恒为 $\mathbf 0$，要么每个分量严格为正。
>
> - **严格正性**：设 $\pi\in\Delta_{K-1}$ 是平稳分布，则 $\pi\ge\mathbf 0$ 且 $\pi Q=\pi$。由 $\sum_{i=1}^K\pi_i=1$ 知 $\pi\neq\mathbf 0$，故由上述性质得对所有 $i\in E$ 有 $\pi_i>0$。
> - **唯一性**：设 $\pi,\tilde\pi\in\Delta_{K-1}$ 均为平稳分布。由严格正性知对所有 $i\in E$ 有 $\tilde\pi_i>0$，又 $E$ 为有限集，故可定义
>
>   $$
>   c := \max_{i\in E}\frac{\pi_i}{\tilde\pi_i}>0,
>   \qquad
>   \mathbf u := c\tilde\pi-\pi.
>   $$
>
>   对任意 $i\in E$，由 $c\ge\pi_i/\tilde\pi_i$ 及 $\tilde\pi_i>0$ 知 $u_i=c\tilde\pi_i-\pi_i\ge 0$，即 $\mathbf u\ge\mathbf 0$；且存在达到最大值的指标 $j\in E$ 使 $u_j=0$。同时由线性性有
>
>   $$
>   \mathbf u Q
>   = (c\tilde\pi-\pi)Q
>   = c\tilde\pi Q-\pi Q
>   = c\tilde\pi-\pi
>   = \mathbf u.
>   $$
>
>   若 $\mathbf u\neq\mathbf 0$，由开头所证性质必有对所有 $i\in E$ 成立 $u_i>0$，这与 $u_j=0$ 矛盾。因此 $\mathbf u=\mathbf 0$，即 $\pi=c\tilde\pi$。两边右乘 $\mathbf 1$，由 $\pi\mathbf 1=\tilde\pi\mathbf 1=1$ 得 $c=1$，故 $\pi=\tilde\pi$。$\square$

**定理。** 设闭沟通类为 $C_1,\dots,C_m$，$T$ 为暂态集。

1. 每个 $C_k$ 上的限制子矩阵 $Q_k$ 是有限不可约行随机矩阵，有唯一且处处为正的平稳分布 $\pi^{(k)}$。将其在 $C_k$ 外补 $0$，得到全空间上的平稳分布 $\tilde\pi^{(k)}$。
2. $Q$ 的全体平稳分布为
   $$
   \pi = \sum_{k=1}^m\alpha_k\tilde\pi^{(k)},
   \qquad
   \alpha_k\ge 0,
   \qquad
   \sum_{k=1}^m\alpha_k=1,
   $$
   其中系数 $\alpha_k=\sum_{i\in C_k}\pi_i$ 由 $\pi$ 唯一确定。
3. 平稳分布唯一当且仅当 $m=1$。

> [!note]- 证明
> 记 $r_k:=|C_k|$，将闭沟通类 $C_k$ 的元素编号为 $C_k=\{i_{k,1},\dots,i_{k,r_k}\}$（固定 $k$ 时简记为 $C_k=\{i_1,\dots,i_{r_k}\}$），暂态集编号为 $T=\{t_1,\dots,t_{|T|}\}$。按 $T,C_1,\dots,C_m$ 排列状态。因闭沟通类 $C_k$ 无流出边（$i\in C_k,\ j\notin C_k\implies Q_{ij}=0$），在 $C_k$ 所在行块中，除对角块 $Q_k\in\mathbb R^{r_k\times r_k}$ 外其余块均为 $0$，转移矩阵呈分块上三角形式：
>
> $$
> Q =
> \begin{pmatrix}
> Q_{TT}&A_1&A_2&\cdots&A_m\\
> 0&Q_1&0&\cdots&0\\
> 0&0&Q_2&\cdots&0\\
> \vdots&\vdots&\vdots&\ddots&\vdots\\
> 0&0&0&\cdots&Q_m
> \end{pmatrix},
> $$
>
> 其中各子块按局部行列下标定义为
>
> $$
> (Q_k)_{ab} := Q_{i_{k,a},i_{k,b}} \quad (1\le a,b\le r_k),
> \qquad
> (Q_{TT})_{ab} := Q_{t_a,t_b} \quad (1\le a,b\le |T|),
> \qquad
> (A_k)_{ab} := Q_{t_a,i_{k,b}}.
> $$
>
> 以下依次证明定理的三项结论：
>
> **证明结论 1：** 固定 $k\in\{1,\dots,m\}$，简记 $C_k=\{i_1,\dots,i_{r_k}\}$。
>
> - **$Q_k$ 是行随机矩阵**：对任意 $a,b\in\{1,\dots,r_k\}$，有 $(Q_k)_{ab}=Q_{i_a,i_b}\ge 0$；又当 $j\notin C_k$ 时 $Q_{i_a,j}=0$，故对任意 $a\in\{1,\dots,r_k\}$，
>
>   $$
>   \sum_{b=1}^{r_k}(Q_k)_{ab}
>   = \sum_{b=1}^{r_k}Q_{i_a,i_b} + \sum_{j\notin C_k}Q_{i_a,j}
>   = \sum_{j\in E}Q_{i_a,j}
>   = 1.
>   $$
>
> - **$Q_k$ 不可约**：由分块结构归纳可知，对任意 $n\ge 0$，$Q^n$ 在 $C_k\times C_k$ 上的子块恰为 $Q_k^n$，即对任意 $a,b\in\{1,\dots,r_k\}$ 有 $(Q_k^n)_{ab}=(Q^n)_{i_a,i_b}$。因 $C_k$ 是沟通类，对任意 $a,b\in\{1,\dots,r_k\}$，状态 $i_a,i_b\in C_k$ 互通，故存在 $n\ge 0$ 使 $(Q^n)_{i_a,i_b}>0$，从而 $(Q_k^n)_{ab}>0$，故 $Q_k$ 不可约。
> - **$\pi^{(k)}$ 的存在唯一性与 $\tilde\pi^{(k)}$ 的平稳性**：由不可约链的唯一性定理，有限不可约行随机矩阵 $Q_k$ 存在唯一平稳分布 $\pi^{(k)}\in\mathbb R^{1\times r_k}$，满足 $\pi^{(k)}Q_k=\pi^{(k)}$、$\pi^{(k)}\mathbf 1_{r_k}=1$ 且对所有 $a\in\{1,\dots,r_k\}$ 有 $\pi^{(k)}_a>0$。定义补零行向量 $\tilde\pi^{(k)}\in\mathbb R^{1\times K}$：在分块顺序 $(T,C_1,\dots,C_m)$ 下，其第 $k$ 个闭类分块为 $\pi^{(k)}$，其余分块均为 $\mathbf 0$，即
>
>   $$
>   \tilde\pi^{(k)} := (\mathbf 0,\mathbf 0,\dots,\pi^{(k)},\dots,\mathbf 0),
>   \qquad
>   \tilde\pi^{(k)}_{i_{k,a}} = \pi^{(k)}_a \quad (1\le a\le r_k),\quad \tilde\pi^{(k)}_j = 0 \quad (j\notin C_k).
>   $$
>
>   显然 $\tilde\pi^{(k)}_j\ge 0$（$\forall j\in E$），且 $\tilde\pi^{(k)}\mathbf 1=\pi^{(k)}\mathbf 1_{r_k}=1$，故 $\tilde\pi^{(k)}\in\Delta_{K-1}$。按分块矩阵乘法计算 $\tilde\pi^{(k)}Q$：
>   - 在 $T$ 分块上为 $\mathbf 0\,Q_{TT}=\mathbf 0$；
>   - 在 $C_\ell$（$\ell\neq k$）分块上为 $\mathbf 0\,A_\ell+\mathbf 0\,Q_\ell=\mathbf 0$；
>   - 在 $C_k$ 分块上为 $\mathbf 0\,A_k+\pi^{(k)}Q_k=\pi^{(k)}$。
>
>   因此 $\tilde\pi^{(k)}Q=\tilde\pi^{(k)}$，即 $\tilde\pi^{(k)}$ 是 $Q$ 的平稳分布。结论 1 得证。
>
> **证明结论 2：** 分“必要性（任意平稳分布均可表为凸组合）”、“充分性（任意凸组合均为平稳分布）”与“系数唯一性”三步。
>
> - **必要性**：设 $\pi=(\mathbf x,\mathbf y_1,\dots,\mathbf y_m)\in\Delta_{K-1}$ 是 $Q$ 的任一平稳分布，其中 $\mathbf x=(\pi_{t_1},\dots,\pi_{t_{|T|}})\in\mathbb R^{1\times|T|}$，$\mathbf y_k=(\pi_{i_{k,1}},\dots,\pi_{i_{k,r_k}})\in\mathbb R^{1\times r_k}$。展开 $\pi Q=\pi$ 得块方程组
>
>   $$
>   \mathbf x = \mathbf x Q_{TT},
>   \qquad
>   \mathbf y_k = \mathbf x A_k + \mathbf y_k Q_k
>   \quad(k=1,\dots,m).
>   $$
>
>   先证 $\mathbf x=\mathbf 0$（若 $T=\emptyset$ 则无需此步）。设 $T\neq\emptyset$，由 $\mathbf x=\mathbf x Q_{TT}$ 归纳可得对任意 $n\ge 1$ 有 $\mathbf x=\mathbf x Q_{TT}^n$。对每个 $i\in T$，由前文命题知 $i$ 可到达某个闭类，设到达 $T^{\mathrm c}:=\bigcup_{k=1}^m C_k$ 的最短正概率路径为 $i=i_0\to i_1\to\cdots\to i_{n_i}\in T^{\mathrm c}$。由最短性，$i_0,\dots,i_{n_i-1}$ 均在 $T$ 内且两两不同，故步数满足 $1\le n_i\le|T|$，且
>
>   $$
>   \delta_i := \sum_{j\notin T}(Q^{n_i})_{ij} \ge (Q^{n_i})_{i,i_{n_i}} > 0.
>   $$
>
>   取 $N:=|T|$。因闭类无返回 $T$ 的边，当 $j\notin T$ 时，第 $j$ 行的非零元全在 $T^{\mathrm c}$ 中，故对任意 $r\ge 0$ 有 $\sum_{\ell\notin T}(Q^r)_{j\ell}=1$。由 $Q^N=Q^{n_i}Q^{N-n_i}$ 得
>
>   $$
>   \begin{aligned}
>   \sum_{\ell\notin T}(Q^N)_{i\ell}
>   &= \sum_{j\in E}(Q^{n_i})_{ij}\sum_{\ell\notin T}(Q^{N-n_i})_{j\ell} \\
>   &\ge \sum_{j\notin T}(Q^{n_i})_{ij}\underbrace{\sum_{\ell\notin T}(Q^{N-n_i})_{j\ell}}_{=1} \\
>   &= \delta_i.
>   \end{aligned}
>   $$
>
>   由分块上三角乘法知 $Q^N$ 的左上块恰为 $Q_{TT}^N$，即 $(Q_{TT}^N)_{ab}=(Q^N)_{t_a,t_b}$（$1\le a,b\le|T|$）。故对任意 $a\in\{1,\dots,|T|\}$，$Q_{TT}^N$ 的第 $a$ 行和满足
>
>   $$
>   (Q_{TT}^N\mathbf 1_{|T|})_a
>   = \sum_{b=1}^{|T|}(Q_{TT}^N)_{ab}
>   = \sum_{\ell\in T}(Q^N)_{t_a,\ell}
>   = 1 - \sum_{\ell\notin T}(Q^N)_{t_a,\ell}
>   \le 1 - \delta_{t_a}.
>   $$
>
>   令 $\varepsilon:=\min_{i\in T}\delta_i>0$，则 $\|Q_{TT}^N\|_\infty=\max_{1\le a\le|T|}(Q_{TT}^N\mathbf 1_{|T|})_a\le 1-\varepsilon<1$。结合 $\mathbf x=\mathbf x Q_{TT}^N$ 与 $\mathbf x\ge\mathbf 0$，两边右乘 $\mathbf 1_{|T|}$ 得
>
>   $$
>   \mathbf x\mathbf 1_{|T|}
>   = \mathbf x Q_{TT}^N\mathbf 1_{|T|}
>   = \sum_{a=1}^{|T|} x_a(Q_{TT}^N\mathbf 1_{|T|})_a
>   \le (1-\varepsilon)\,\mathbf x\mathbf 1_{|T|}.
>   $$
>
>   因 $\varepsilon>0$ 且 $\mathbf x\mathbf 1_{|T|}\ge 0$，必有 $\mathbf x\mathbf 1_{|T|}=0$，故 $\mathbf x=\mathbf 0$。
>
>   将 $\mathbf x=\mathbf 0$ 代入块方程组，得 $\mathbf y_k=\mathbf y_k Q_k$（$k=1,\dots,m$）。对每个 $k$，定义
>
>   $$
>   \alpha_k := \mathbf y_k\mathbf 1_{r_k} = \sum_{i\in C_k}\pi_i \ge 0.
>   $$
>
>   - 若 $\alpha_k=0$，由 $\mathbf y_k\ge\mathbf 0$ 知 $\mathbf y_k=\mathbf 0=\alpha_k\pi^{(k)}$；
>   - 若 $\alpha_k>0$，令 $\hat{\mathbf y}_k:=\alpha_k^{-1}\mathbf y_k$，则 $\hat{\mathbf y}_k\ge\mathbf 0$、$\hat{\mathbf y}_k\mathbf 1_{r_k}=1$ 且 $\hat{\mathbf y}_k Q_k=\hat{\mathbf y}_k$，即 $\hat{\mathbf y}_k$ 是 $Q_k$ 的平稳分布。由结论 1 中 $\pi^{(k)}$ 的唯一性得 $\hat{\mathbf y}_k=\pi^{(k)}$，故亦有 $\mathbf y_k=\alpha_k\pi^{(k)}$。
>
>   因此
>
>   $$
>   \pi
>   = (\mathbf 0,\alpha_1\pi^{(1)},\dots,\alpha_m\pi^{(m)})
>   = \sum_{k=1}^m\alpha_k\tilde\pi^{(k)},
>   $$
>
>   且由 $\pi\mathbf 1=1$ 与 $\mathbf x=\mathbf 0$ 得
>
>   $$
>   \sum_{k=1}^m\alpha_k
>   = \sum_{k=1}^m\sum_{i\in C_k}\pi_i + \sum_{i\in T}\pi_i
>   = \sum_{i\in E}\pi_i
>   = 1.
>   $$
>
> - **充分性**：任取满足 $\alpha_k\ge 0$ 与 $\sum_{k=1}^m\alpha_k=1$ 的系数，令 $\pi:=\sum_{k=1}^m\alpha_k\tilde\pi^{(k)}$。由 $\tilde\pi^{(k)}\ge\mathbf 0$ 及 $\alpha_k\ge 0$ 知 $\pi\ge\mathbf 0$；同时
>
>   $$
>   \pi\mathbf 1
>   = \sum_{k=1}^m\alpha_k(\tilde\pi^{(k)}\mathbf 1)
>   = \sum_{k=1}^m\alpha_k
>   = 1,
>   \qquad
>   \pi Q
>   = \sum_{k=1}^m\alpha_k(\tilde\pi^{(k)}Q)
>   = \sum_{k=1}^m\alpha_k\tilde\pi^{(k)}
>   = \pi,
>   $$
>
>   故 $\pi$ 是 $Q$ 的平稳分布。
> - **系数唯一性**：设 $\pi=\sum_{\ell=1}^m\alpha_\ell\tilde\pi^{(\ell)}$。因当 $i=i_{k,a}\in C_k$（$1\le a\le r_k$）时，对所有 $\ell\neq k$ 有 $\tilde\pi^{(\ell)}_i=0$，而 $\tilde\pi^{(k)}_{i_{k,a}}=\pi^{(k)}_a$，故在 $C_k$ 上对分量求和得
>
>   $$
>   \sum_{i\in C_k}\pi_i
>   = \sum_{\ell=1}^m\alpha_\ell\sum_{i\in C_k}\tilde\pi^{(\ell)}_i
>   = \alpha_k\sum_{a=1}^{r_k}\pi^{(k)}_a
>   = \alpha_k.
>   $$
>
>   因此系数 $\alpha_k=\sum_{i\in C_k}\pi_i$ 由 $\pi$ 唯一确定。结论 2 得证。
>
> **证明结论 3：**
>
> - **充分性（$m=1\implies$ 平稳分布唯一）**：若 $m=1$，由结论 2 知任意平稳分布 $\pi$ 必满足 $\pi=\alpha_1\tilde\pi^{(1)}$ 且 $\alpha_1=1$，故 $Q$ 有唯一平稳分布 $\tilde\pi^{(1)}$。
> - **必要性（平稳分布唯一 $\implies m=1$）**：若 $m\ge 2$，由结论 1 知 $\tilde\pi^{(1)}$ 与 $\tilde\pi^{(2)}$ 均为 $Q$ 的平稳分布。取 $i=i_{1,1}\in C_1$，因 $C_1\cap C_2=\emptyset$，有 $\tilde\pi^{(1)}_i=\pi^{(1)}_1>0$ 而 $\tilde\pi^{(2)}_i=0$，故 $\tilde\pi^{(1)}\neq\tilde\pi^{(2)}$，平稳分布不唯一（事实上，对任意 $\alpha\in[0,1]$，$\alpha\tilde\pi^{(1)}+(1-\alpha)\tilde\pi^{(2)}$ 均为互不相同的平稳分布）。
>
> 因此平稳分布唯一当且仅当 $m=1$。结论 3 得证。$\square$

当 $m=1$ 且 $T\neq\emptyset$ 时，平稳分布唯一但在暂态上取 $0$。例如

$$
Q=
\begin{pmatrix}
1&0\\
1&0
\end{pmatrix}
$$

中，对任意 $n\ge 1$ 均有 $Q^n=Q$，故 $(Q^n)_{21}=1>0$（$2\to 1$），而对一切 $n\ge 1$ 均有 $(Q^n)_{12}=0$（$1\nrightarrow 2$）。因此 $1$ 与 $2$ 不互通，沟通类为 $\{1\}$ 与 $\{2\}$：

- 对 $\{1\}$：唯一状态 $1$ 对类外状态 $2$ 有 $Q_{12}=0$，无流出边，故 $\{1\}$ 是闭沟通类，即 $C_1=\{1\}$；
- 对 $\{2\}$：存在类外状态 $1\notin\{2\}$ 使 $Q_{21}=1>0$，故 $\{2\}$ 不是闭沟通类，从而暂态集为 $T=E\setminus C_1=\{2\}$。

由 $\pi Q=(\pi_1+\pi_2,0)=(\pi_1,\pi_2)$ 及 $\pi_1+\pi_2=1$，得唯一平稳分布为 $\pi=(1,0)$。而

$$
Q=
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix}
$$

有两个闭类 $C_1=\{1\}$、$C_2=\{2\}$，平稳分布全体为 $(\alpha,1-\alpha)$（$0\le\alpha\le 1$）。

## 6. 分布的收敛

非负方阵 $Q$ 称为**本原矩阵**，如果存在整数 $m\ge 1$ 使 $Q^m$ 的所有元素严格为正（记作 $Q^m>0$）。

**引理。** 有限不可约非周期行随机矩阵是本原矩阵。

> [!note]- 证明
> 固定一个状态 $i\in E$，令返回步数集合为 $G:=\{n\ge 1:(Q^n)_{ii}>0\}$。分三步证明：
>
> **第一步：$G$ 对加法封闭。** 由有限不可约性知 $G$ 非空。对任意 $a,b\in G$，由矩阵乘法及 $Q$ 的非负性，只保留求和中的 $k=i$ 项得
>
> $$
> (Q^{a+b})_{ii}
> = \sum_{k=1}^K (Q^a)_{ik}(Q^b)_{ki}
> \ge (Q^a)_{ii}(Q^b)_{ii}
> > 0,
> $$
>
> 故 $a+b\in G$。由此归纳可知，对任意 $g_1,\dots,g_\ell\in G$ 及不全为 $0$ 的非负整数 $c_1,\dots,c_\ell\in\mathbb Z_{\ge 0}$，均有 $\sum_{s=1}^\ell c_s g_s\in G$。
>
> **第二步：充分大的正整数均属于 $G$。** 任取 $g_1\in G$，其大于 $1$ 的正因子只有有限个；由非周期性知 $\gcd(G)=1$，故对 $g_1$ 的每个大于 $1$ 的因子 $d$，均存在 $h_d\in G$ 使 $d\nmid h_d$。将 $g_1$ 与这些有限个 $h_d$ 合并，即得有限个元素 $g_1,\dots,g_\ell\in G$ 满足 $\gcd(g_1,\dots,g_\ell)=1$。由裴蜀（Bézout）定理，存在整数 $z_1,\dots,z_\ell\in\mathbb Z$ 使 $\sum_{s=1}^\ell z_s g_s=1$。将正负项分离，令
>
> $$
> G_+
> :=
> \sum_{z_s>0}z_s g_s,
> \qquad
> G_-
> :=
> \sum_{z_s<0}(-z_s)g_s,
> $$
>
> 则 $G_+-G_-=1$。
>
> - 若 $G_-=0$，则 $G_+=1\in G$，由加法封闭性知一切正整数 $n\ge 1$ 均属于 $G$，取 $N:=1$。
> - 若 $G_-\ge 1$，则 $G_-$ 与 $G_+=G_-+1$ 均为 $G$ 中元素的正整数线性组合，由第一步知 $G_-,G_+\in G$。令 $N:=\max\{1,(G_--1)G_-\}$。对任意整数 $n\ge N$，对 $G_-$ 作带余除法得
>
>   $$
>   n = qG_- + r,
>   \qquad
>   q\in\mathbb Z,\quad 0\le r\le G_--1.
>   $$
>
>   由 $n\ge(G_--1)G_-$ 知 $q\ge G_--1\ge r$，故 $q-r\ge 0$。将 $1=G_+-G_-$ 代入得
>
>   $$
>   n = qG_- + r(G_+-G_-) = (q-r)G_- + rG_+.
>   $$
>
>   因 $q-r\ge 0$、$r\ge 0$，且由 $n\ge 1$ 知两者不全为 $0$，由第一步即得 $n\in G$。
>
> 综上，存在整数 $N\ge 1$，使得对一切 $n\ge N$ 均有 $(Q^n)_{ii}>0$。
>
> **第三步：由不可约性推广至全矩阵严格为正。** 由不可约性，对每个 $u\in E$ 存在 $s_u\ge 0$ 使 $(Q^{s_u})_{ui}>0$，对每个 $v\in E$ 存在 $r_v\ge 0$ 使 $(Q^{r_v})_{iv}>0$。令
>
> $$
> S := \max_{u\in E}s_u,
> \qquad
> R := \max_{v\in E}r_v,
> \qquad
> M := N+S+R\ge 1.
> $$
>
> 对任意整数 $m\ge M$ 及任意 $u,v\in E$，有 $m-s_u-r_v\ge N$，从而 $(Q^{m-s_u-r_v})_{ii}>0$。由矩阵乘法 $Q^m=Q^{s_u}Q^{m-s_u-r_v}Q^{r_v}$ 并只保留双重求和中的 $(k,\ell)=(i,i)$ 项，得
>
> $$
> \begin{aligned}
> (Q^m)_{uv}
> &= \sum_{k=1}^K\sum_{\ell=1}^K (Q^{s_u})_{uk}(Q^{m-s_u-r_v})_{k\ell}(Q^{r_v})_{\ell v} \\
> &\ge (Q^{s_u})_{ui}(Q^{m-s_u-r_v})_{ii}(Q^{r_v})_{iv}
> > 0.
> \end{aligned}
> $$
>
> 因此对一切 $m\ge M$ 均有 $Q^m>0$，特别地 $Q$ 是本原矩阵。$\square$


### 6.1. 算例：均匀重置链

设 $E=\{1,\dots,K\}$，$\alpha\in(0,1)$。每一步以概率 $1-\alpha$ 留在当前状态，以概率 $\alpha$ 从 $E$ 中均匀抽取下一状态：

$$
Q_{ij} =
\begin{cases}
1-\alpha+\alpha/K & j=i, \\
\alpha/K & j\neq i.
\end{cases}
$$

令 $J:=\frac1K\mathbf 1\mathbf 1^\top$，则 $Q=(1-\alpha)I+\alpha J$。由 $\mathbf 1^\top\mathbf 1=K$ 知 $J^2=J$，$(I-J)^2=I-J$，且 $J(I-J)=(I-J)J=0$。将 $Q$ 写为互补投影之和

$$
Q = J+(1-\alpha)(I-J),
$$

则对任意 $n\ge 1$，

$$
Q^n
= \bigl(J+(1-\alpha)(I-J)\bigr)^n
= J^n+(1-\alpha)^n(I-J)^n
= J+(1-\alpha)^n(I-J).
$$

均匀分布 $\pi=\frac1K\mathbf 1^\top$ 满足 $\pi J=\pi$，故 $\pi Q=(1-\alpha)\pi+\alpha\pi=\pi$。对任意初始分布 $\nu_0\in\Delta_{K-1}$，由 $\nu_0\mathbf 1=1$ 得

$$
\nu_0 J
= \frac1K(\nu_0\mathbf 1)\mathbf 1^\top
= \pi,
\qquad
\nu_0(I-J) = \nu_0-\pi,
$$

从而

$$
\nu_n
= \nu_0 Q^n
= \pi+(1-\alpha)^n(\nu_0-\pi)
\xrightarrow[n\to\infty]{} \pi.
$$

