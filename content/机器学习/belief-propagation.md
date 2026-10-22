---
title: 信念传播
date: 2026-10-21
tags:
  - 概率
---

信念传播（Belief Propagation）是因子图上的消息传递。本文给出有限离散变量上的和积算法，用来计算式 (1) 的单变量边缘。

## 因子分解

设 $V$ 为有限集。每个 $i\in V$ 对应随机变量 $X_i$，取值于有限集 $\mathcal{X}_i$。赋值 $\mathbf{x}=(x_i)_{i\in V}$ 属于 $\mathcal{X}=\prod_{i\in V}\mathcal{X}_i$。

设 $F$ 为有限的因子指标集。每个 $a\in F$ 有作用域 $V_a\subseteq V$，以及

$$
\psi_a:\prod_{i\in V_a}\mathcal{X}_i\to[0,\infty).
$$

$\mathbf{x}_a$ 表示 $\mathbf{x}$ 在 $V_a$ 上的限制。令

$$
Z=\sum_{\mathbf{x}\in\mathcal{X}}\prod_{a\in F}\psi_a(\mathbf{x}_a),
$$

并设 $Z>0$。联合分布定义为

$$
P(\mathbf{x})=\frac{1}{Z}\prod_{a\in F}\psi_a(\mathbf{x}_a).
\tag{1}
$$

目标是对每个 $i\in V$ 与 $x_i\in\mathcal{X}_i$ 计算

$$
P(X_i=x_i)=\sum_{\mathbf{x}\setminus x_i}P(\mathbf{x}).
$$

$\mathbf{x}\setminus x_i$ 表示除坐标 $i$ 以外的赋值，求和范围是 $\prod_{k\in V\setminus\{i\}}\mathcal{X}_k$。

## 因子图

因子图是二分图 $G=(V\cup F,E)$，

$$
E=\bigl\{\{i,a\}:a\in F,\ i\in V_a\bigr\}.
$$

变量节点的邻域是 $N(i)=\{a\in F:i\in V_a\}$，因子节点的邻域是 $N(a)=V_a$。

## 消息

每条边 $\{i,a\}$ 上有两个函数

$$
m_{i\to a},\; m_{a\to i}:\mathcal{X}_i\to[0,\infty).
$$

变量到因子的更新为

$$
m_{i\to a}(x_i)=\prod_{b\in N(i)\setminus\{a\}}m_{b\to i}(x_i).
\tag{2}
$$

乘积的指标集是 $N(i)\setminus\{a\}$，其中不含接收方 $a$。若 $N(i)=\{a\}$，则乘积为空，值定义为 $1$。

因子到变量的更新为

$$
m_{a\to i}(x_i)
=\sum_{\mathbf{x}_a\setminus x_i}
\psi_a(\mathbf{x}_a)
\prod_{j\in N(a)\setminus\{i\}}
m_{j\to a}(x_j).
\tag{3}
$$

$x_i\in\mathcal{X}_i$ 是自变量，求和时保持不变。$\mathbf{x}_a\setminus x_i$ 是 $\mathbf{x}_a$ 在 $N(a)\setminus\{i\}$ 上的坐标，求和范围是

$$
\prod_{j\in N(a)\setminus\{i\}}\mathcal{X}_j.
$$

设 $N(a)\setminus\{i\}=\{j_1,\ldots,j_r\}$，则

$$
\sum_{\mathbf{x}_a\setminus x_i}
=\sum_{x_{j_1}\in\mathcal{X}_{j_1}}\cdots\sum_{x_{j_r}\in\mathcal{X}_{j_r}},
$$

并且每个被加项里的 $\mathbf{x}_a$ 在坐标 $i$ 上等于该固定的 $x_i$。$r=0$ 时，求和仅含空赋值这一项，乘积为 $1$，因此 $m_{a\to i}=\psi_a$。被加项个数为 $\prod_{j\in N(a)\setminus\{i\}}|\mathcal{X}_j|$。

式 (2) 把到达变量 $i$ 的其他因子消息相乘，对应式 (1) 中因子的乘积。式 (3) 先乘上 $\psi_a$，再对其余坐标求和，使结果只是 $\mathcal{X}_i$ 上的函数。

## 信念

$$
b_i(x_i)\propto\prod_{a\in N(i)}m_{a\to i}(x_i).
\tag{4}
$$

式 (4) 的乘积取遍 $N(i)$。发往某个 $a$ 的式 (2) 不含 $m_{a\to i}$，信念则把这条消息乘回来。当

$$
\sum_{y\in\mathcal{X}_i}\prod_{a\in N(i)}m_{a\to i}(y)>0
$$

时，定义

$$
b_i(x_i)
=\frac{\prod_{a\in N(i)}m_{a\to i}(x_i)}
{\sum_{y\in\mathcal{X}_i}\prod_{a\in N(i)}m_{a\to i}(y)}.
\tag{5}
$$

把任意一条入消息乘以正常数，分子与分母同乘该常数，$b_i$ 不变。

## 无环与含环

设 $G$ 是树，并任取一个根。更新可以排成这样的顺序：先由远及近计算所有指向根的消息，再由近及远计算所有离开根的消息。计算一条消息时，式 (2) 或式 (3) 右端用到的消息都已经得到。叶变量发往唯一因子的消息是空乘积，叶因子发往唯一变量的消息等于该因子。每条有向消息计算一次后，

$$
b_i(x_i)=P(X_i=x_i),\qquad i\in V,\ x_i\in\mathcal{X}_i.
$$

$G$ 含环时，先令所有消息为恒等于 $1$ 的函数，再反复执行式 (2) 与式 (3)。这个迭代称为 loopy belief propagation。迭代可能发散或振荡。收敛时的极限是更新映射的不动点，依赖于初始消息和更新顺序；这个不动点可以不等于 $(P(X_i))_{i\in V}$。上一节的等式用到了 $G$ 无环。
