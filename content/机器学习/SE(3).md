---
title: SE(3)
---

## 1. 前置

- [[抽象代数/群论(群作用)]]

## 2. 等变与不变

设 $G$ 是一个群，$X$ 和 $Y$ 是两个集合。$\rho_X: G \times X \to X$ 是 $G$ 在 $X$ 上的作用，记作 $g \cdot x$。$\rho_Y: G \times Y \to Y$ 是 $G$ 在 $Y$ 上的作用，记作 $g \cdot y$。

一个映射 $\phi: X \to Y$ 被称为 $G$-等变的，如果对于所有的 $g \in G$ 和 $x \in X$，满足：$$\phi(g \cdot x) = g \cdot \phi(x)$$

一个映射 $\psi: X \to Y$ 被称为 $G$-不变的，如果对于所有的 $g \in G$ 和 $x \in X$，满足：$$\psi(g \cdot x) = \psi(x)$$

## 3. Group in $\mathbb{R}^3$

- $GL(3) = \{M \in \mathbb{R}^{3 \times 3} \mid M \text{ is invertible}\}$
- $O(3) = \{M \in \mathbb{R}^{3 \times 3} \mid MM^T = M^T M = I\}$
- $SO(3) = \{M \in \mathbb{R}^{3 \times 3} \mid MM^T = M^T M = I \wedge \det(M) = 1\}$

> $SO(3) < O(3) < GL(3)$

- $SE(3) = \{f \mid f(x) = Rx + t \wedge R \in SO(3) \wedge t \in \mathbb{R}^3\}$

> $SO(3) < SE(3)$

## 4. SE(3)-Equivariance（(Simplified Form)）

当输入空间 $X$ 和输出空间 $Y$ 均为 $3\text{D}$ 坐标空间 $\mathbb{R}^3$，且群作用 $\rho$ 均为标准的坐标变换时：设 $T \in SE(3)$ 是一个变换算子，定义为 $T(\mathbf{x}) = R\mathbf{x} + \mathbf{t}$。

等变性 (Equivariance)：映射 $f: \mathbb{R}^3 \to \mathbb{R}^3$ 是 $SE(3)$-等变的，如果：

$$f(T(\mathbf{x})) = T(f(\mathbf{x})) \quad \forall T \in SE(3)$$

当输入和输出是点云 $\mathbf{X} \in \mathbb{R}^{n \times 3}$ 时，其中每一行 $\mathbf{x}_i^T$ 代表一个点的坐标。群作用定义：对于 $T = (R, \mathbf{t}) \in SE(3)$，它在点云上的作用 $T(\mathbf{X})$ 定义为对每个点执行相同的变换：

$$T(\mathbf{X}) = \mathbf{X}R^T + \mathbf{1}\mathbf{t}^T$$

（注：这里 $\mathbf{1} \in \mathbb{R}^n$ 是全 1 向量，确保平移 $\mathbf{t}$ 加到每一个点上）。等变性定义：若函数 $F: \mathbb{R}^{n \times 3} \to \mathbb{R}^{n \times 3}$ 满足：$$F(T(\mathbf{X})) = T(F(\mathbf{X}))$$则称该函数是点云上的 $SE(3)$-等变函数。
