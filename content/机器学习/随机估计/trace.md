## Hutchinson 迹估计与随机投影

全文固定维数 $d$：矩阵 $A\in\mathbb R^{d\times d}$，向量 $\mathbf s,\mathbf S\in\mathbb R^d$，随机探针 $\mathbf u\in\mathbb R^d$，$I_d$ 为 $d$ 阶单位阵。

高维情形下，$\operatorname{tr}(A)$ 与 $\lVert\mathbf s\rVert_2^2$ 可以用随机方向上的一维投影作无偏估计，从而避免显式构造完整的 $d\times d$ 矩阵或计算完整向量内积。

设随机向量 $\mathbf u\in\mathbb R^d$ 满足

$$
\mathbb E[\mathbf u\mathbf u^\top]=I_d.
$$

这一各向同性二阶矩条件蕴含

$$
\mathbb E\lVert\mathbf u\rVert_2^2=d<\infty.
$$

常见选择包括：

- 各分量独立同分布的 Rademacher 向量，即 $u_i\in\{-1,+1\}$ 且两个取值概率均为 $1/2$；
- $\mathbf u\sim\mathcal N(\mathbf0,I_d)$。

### 随机矩阵的 Hutchinson 迹估计

> [!abstract] 定理（随机矩阵的 Hutchinson 迹估计）
> 设随机矩阵 $A\in\mathbb R^{d\times d}$ 满足
>
> $$
> \mathbb E\lVert A\rVert_{\mathrm F}<\infty,
> $$
>
> 且 $\mathbf u$ 与 $A$ 独立、$\mathbb E[\mathbf u\mathbf u^\top]=I_d$。则 $\mathbf u^\top A\mathbf u$ 可积，并且
>
> $$
> \mathbb E\left[
> \mathbf u^\top A\mathbf u\mid A
> \right]
> =\operatorname{tr}(A)
> \qquad\text{几乎处处}.
> $$
>
> 因此
>
> $$
> \mathbb E[\mathbf u^\top A\mathbf u]
> =\mathbb E[\operatorname{tr}(A)].
> $$
>
> 当 $A$ 是确定矩阵时，上式退化为
>
> $$
> \operatorname{tr}(A)
> =\mathbb E_{\mathbf u}[\mathbf u^\top A\mathbf u].
> $$
>
> $A$ 不必对称；其反对称部分对二次型和迹都没有贡献。
>
> > [!note]- 证明
> >
> > $$
> > \begin{aligned}
> > \mathbf u^\top A\mathbf u
> > &=\operatorname{tr}(\mathbf u^\top A\mathbf u)
> > =\operatorname{tr}(A\,\mathbf u\mathbf u^\top)
> > =\langle A,\ \mathbf u\mathbf u^\top\rangle_{\mathrm F},
> > &&(\text{迹的循环性})\\
> > \lVert\mathbf u\mathbf u^\top\rVert_{\mathrm F}^2
> > &=\sum_{i,j}u_i^2u_j^2
> > =\Bigl(\sum_i u_i^2\Bigr)\Bigl(\sum_j u_j^2\Bigr)
> > =\lVert\mathbf u\rVert_2^4
> > &&(\text{Frobenius 范数的定义})
> > \end{aligned}
> > $$
> >
> > 于是
> >
> > $$
> > \begin{aligned}
> > \lvert\mathbf u^\top A\mathbf u\rvert
> > &\leq\lVert A\rVert_{\mathrm F}\lVert\mathbf u\mathbf u^\top\rVert_{\mathrm F}
> > =\lVert A\rVert_{\mathrm F}\lVert\mathbf u\rVert_2^2
> > &&(\text{Cauchy–Schwarz})\\
> > \mathbb E\lvert\mathbf u^\top A\mathbf u\rvert
> > &\leq\mathbb E\lVert A\rVert_{\mathrm F}\,
> > \mathbb E\lVert\mathbf u\rVert_2^2
> > &&(\mathbf u\perp\!\!\!\perp A,\ \text{Tonelli})\\
> > &=d\,\mathbb E\lVert A\rVert_{\mathrm F}<\infty
> > &&\bigl(\mathbb E\lVert\mathbf u\rVert_2^2=d,\ \mathbb E\lVert A\rVert_{\mathrm F}<\infty\bigr)
> > \end{aligned}
> > $$
> >
> > 对 $A$ 取条件期望：
> >
> > $$
> > \begin{aligned}
> > \mathbb E[\mathbf u^\top A\mathbf u\mid A]
> > &=\operatorname{tr}\bigl(A\,\mathbb E[\mathbf u\mathbf u^\top\mid A]\bigr)
> > &&(A\ \text{可测},\ \text{迹线性})\\
> > &=\operatorname{tr}(AI_d)
> > =\operatorname{tr}(A)
> > &&\bigl(\mathbb E[\mathbf u\mathbf u^\top\mid A]=I_d\bigr)
> > \end{aligned}
> > $$
> >
> > 再用全期望公式：
> >
> > $$
> > \mathbb E[\mathbf u^\top A\mathbf u]
> > =\mathbb E\bigl[\mathbb E[\mathbf u^\top A\mathbf u\mid A]\bigr]
> > =\mathbb E[\operatorname{tr}(A)].
> > $$
> >
> > 证毕。

### 随机投影估计平方范数

> [!abstract] 定理（随机投影估计平方范数）
> 设 $\mathbf S\in\mathbb R^d$ 满足
>
> $$
> \mathbb E\lVert\mathbf S\rVert_2^2<\infty,
> $$
>
> 且 $\mathbf u$ 与 $\mathbf S$ 独立、$\mathbb E[\mathbf u\mathbf u^\top]=I_d$。则 $(\mathbf u^\top\mathbf S)^2$ 可积，并且
>
> $$
> \mathbb E\left[
> (\mathbf u^\top\mathbf S)^2\mid\mathbf S
> \right]
> =\lVert\mathbf S\rVert_2^2
> \qquad\text{几乎处处}.
> $$
>
> 因此
>
> $$
> \mathbb E[(\mathbf u^\top\mathbf S)^2]
> =\mathbb E\lVert\mathbf S\rVert_2^2.
> $$
>
> 特别地，对任意固定 $\mathbf s\in\mathbb R^d$，
>
> $$
> \mathbb E_{\mathbf u}
> \left[
> (\mathbf u^\top\mathbf s)^2
> \right]
> =\lVert\mathbf s\rVert_2^2.
> $$
>
> > [!note]- 证明
> >
> > $$
> > \begin{aligned}
> > (\mathbf u^\top\mathbf S)^2
> > &\leq\lVert\mathbf u\rVert_2^2\lVert\mathbf S\rVert_2^2
> > &&(\text{Cauchy–Schwarz})\\
> > \mathbb E[(\mathbf u^\top\mathbf S)^2]
> > &\leq\mathbb E\bigl[\lVert\mathbf u\rVert_2^2\lVert\mathbf S\rVert_2^2\bigr]
> > =\mathbb E\lVert\mathbf u\rVert_2^2\,\mathbb E\lVert\mathbf S\rVert_2^2
> > &&(\mathbf u\perp\!\!\!\perp\mathbf S,\ \text{Tonelli})\\
> > &=d\,\mathbb E\lVert\mathbf S\rVert_2^2<\infty
> > &&\bigl(\mathbb E\lVert\mathbf u\rVert_2^2=d,\ \mathbb E\lVert\mathbf S\rVert_2^2<\infty\bigr)
> > \end{aligned}
> > $$
> >
> > 对 $\mathbf S$ 取条件期望：
> >
> > $$
> > \begin{aligned}
> > \mathbb E[(\mathbf u^\top\mathbf S)^2\mid\mathbf S]
> > &=\mathbb E\bigl[\mathbf S^\top\mathbf u\mathbf u^\top\mathbf S\mid\mathbf S\bigr]\\
> > &=\mathbf S^\top\mathbb E[\mathbf u\mathbf u^\top\mid\mathbf S]\mathbf S
> > &&(\mathbf S\ \text{可测},\ \text{线性})\\
> > &=\mathbf S^\top I_d\mathbf S
> > =\lVert\mathbf S\rVert_2^2
> > &&\bigl(\mathbb E[\mathbf u\mathbf u^\top\mid\mathbf S]=I_d\bigr)
> > \end{aligned}
> > $$
> >
> > 对固定 $\mathbf s$：
> >
> > $$
> > \begin{aligned}
> > \mathbb E\bigl[(\mathbf u^\top\mathbf s)^2\bigr]
> > &=\sum_{i,j=1}^d s_i s_j\,\mathbb E[u_i u_j]\\
> > &=\sum_{i,j=1}^d s_i s_j\,\delta_{ij}
> > =\sum_{i=1}^d s_i^2
> > =\lVert\mathbf s\rVert_2^2
> > &&\bigl(\mathbb E[u_i u_j]=\delta_{ij}\bigr)
> > \end{aligned}
> > $$
> >
> > 证毕。

使用 $M$ 个独立探针并取平均，便得到常用的无偏 Monte Carlo 估计：

$$
\widehat{\operatorname{tr}}(A)
=\frac1M\sum_{m=1}^M
\mathbf u_m^\top A\mathbf u_m,
\qquad
\widehat{\lVert\mathbf s\rVert_2^2}
=\frac1M\sum_{m=1}^M
(\mathbf u_m^\top\mathbf s)^2,
$$

前提是以上矩条件和独立性条件成立。
