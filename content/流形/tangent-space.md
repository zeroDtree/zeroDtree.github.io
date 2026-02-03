---
title: Tangent space of smooth manifold(光滑流形的切空间)
---

文中chart都是指从某一个极大图册(maximal atlas)中取。

直观描述：$M$是$n$维光滑流形，$p \in M$，$M$在$p$处的切空间$T_pM$是$M$在$p$处的所有切向量的集合。

如何形式化地描述流形上的切向量呢？

考虑$\mathbb{R}^3$中一个曲面，$p$是曲面上的一个点。一条经过$p$的曲线$c(t)$满足，$c(0)=p$，则$c(t)$在$p$处的导数$c'(0)$是点$p$的一个切向量。

## Tangent space

$M$是$n$维光滑流形，$p \in M$，$c:(-1,1) \to M$是$p$点处的光滑曲线，$c(0)=p$，$(U,\phi)$是$p$点处的一个chart, $f_{\phi,c}=\phi\circ c:(-1,1) \to \mathbb{R}^n,f_{\phi,c}'(0) = \frac{d}{dt} \phi \circ c(t) \mid_{t=0}$，

$\mathcal{A} = \{c:(-1,1) \to M \mid c \in \mathcal{C}^{\infty}, c(0)=p\}$

定义一种关系$\sim$，$c_1,c_2 \in \mathcal{A}$，$c_1 \sim c_2$当且仅当存在chart $(U,\phi)$，使得$f_{\phi,c_1}'(0)=f_{\phi,c_2}'(0)$, 显然$\sim$是等价关系。

上述等价关系与chart的选取无关。假设$(V,\psi)$是$p$点处的另一个chart,我们验证$f_{\psi,c_1}'(0)=f_{\psi,c_2}'(0)$

$f_{\psi,c_1}(t) = \psi \circ c_1(t) = \psi \circ \phi^{-1} \circ \phi \circ c_1(t)$

$f_{\psi,c_2}(t) = \psi \circ c_2(t) = \psi \circ \phi^{-1} \circ \phi \circ c_2(t)$

因此$f_{\psi,c_1}'(0)=f_{\psi,c_2}'(0)$，即$c_1 \sim c_2$与chart的选取无关。

$\mathcal{A}$在等价关系$\sim$下的所有等价类组成集合记作$T_pM$，$T_pM$是$M$在$p$处的切空间(Tangent space)。一个曲线$c$所在的等价类记作$[c]$

对于点$p$的一个chart $(U,\phi)$，定义映射 $\mu: T_pM \to \mathbb{R}^n$，$\mu([c]) = f_{\phi,c}'(0) = \frac{d}{dt} \phi \circ c(t) \mid_{t=0}$

验证$\mu$是双射，单射显然，满射考虑：曲线$\phi^{-1} (\phi(x) + tv)$，其导数为$v$,由$v$的任意性可得满射。

在切空间$T_pM$上定义加法和标量乘法

$[c_1] + [c_2] = [\mu^{-1} (\mu([c_1]) + \mu([c_2]))]$

$a[c] = [\mu^{-1} (a\mu([c]))]$

易得$\mu$是同构映射(向量空间角度的同构映射，即为线性映射)，因此$T_pM$是向量空间。

因为同构，所以可以将$T_pM$中的$[c]$等价地记作(rename) $\frac{d}{dt} \phi \circ c(t) \mid_{t=0}$, 切空间中的元素称为切向量。

**tangent bundle**(切丛) of $M$ is the union of all the tangent spaces of $M$: $TM = \bigcup_{p \in M} T_pM = \{(p,v) \mid p \in M, v \in T_pM\}$.

**retraction**(收缩映射): A retraction on a manifold $M$ is a smooth map $R : TM \to M : (x, v) \to R_x (v)$ such that each curve $c(t) = R_x (tv)$ satisfies $c(0) = x$ and $c' (0) = v$.
