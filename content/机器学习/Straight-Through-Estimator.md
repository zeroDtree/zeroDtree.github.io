---
title: Straight-Through Estimator
tags:
  - 机器学习
date: 2026-10-29
---

反向传播沿计算图把损失 $L$ 往前传。每经过一个结点，就把上游梯度乘上该结点的局部导数。取整、符号和硬阈值要么不可导，要么导数几乎处处为 $0$。局部导数为 $0$ 时，更前面的参数收不到更新。

Straight-Through Estimator（STE，直通估计器）保持前向计算不变，只在反向替换局部导数。最常用的替换是恒等映射的导数，使上游梯度原样通过。

## 1. 恒等梯度

设这个操作为 $Q$，

$$
y=Q(x).
$$

链式法则把损失对 $x$ 的梯度写成上游梯度与局部导数的乘积：

$$
\frac{\partial L}{\partial x}
=
\frac{\partial L}{\partial y}
\frac{\partial y}{\partial x}.
\tag{1}
$$

$\partial L/\partial y$ 是从 $L$ 传回 $y$ 的上游梯度。$Q$ 为取整时，$\partial y/\partial x=0$ 几乎处处成立，(1) 给出 $\partial L/\partial x=0$。

恒等 STE 把局部导数换成恒等映射的导数。$Q$ 按坐标作用时，对角元近似为 $1$，其余近似为 $0$：

$$
\frac{\partial y_i}{\partial x_i}\approx 1,\qquad
\frac{\partial y_i}{\partial x_j}\approx 0\quad(i\neq j).
$$

对应的雅可比就是单位阵 $I$。代回 (1)，

$$
\frac{\partial L}{\partial x}
\approx
\frac{\partial L}{\partial y}\,I
=
\frac{\partial L}{\partial y}.
\tag{2}
$$

$I$ 是局部导数的替代。按 (2)，$x$ 收到的梯度等于上游梯度 $\partial L/\partial y$。前向输出仍是 $Q(x)$。

## 2. 用 detach 实现

下面把前向数值和反向通路拆开。`detach` 切断括号中的梯度，留下的 $x$ 提供恒等导数。

```python
y = Q(x)
y_st = x + (y - x).detach()
```

前向时 `detach` 不改变数值，因此 $y_{\mathrm{st}}=x+(y-x)=y$。后面的层使用的仍是 $Q(x)$。

反向时，$(y-x)$ 已从计算图断开，对 $x$ 的贡献为 $0$。$y_{\mathrm{st}}$ 对 $x$ 的局部导数只来自第一项 $x$：

$$
\frac{\partial y_{\mathrm{st}}}{\partial x}=I.
$$

上游梯度 $\partial L/\partial y_{\mathrm{st}}$ 再乘这个局部导数：

$$
\frac{\partial L}{\partial x}
=
\frac{\partial L}{\partial y_{\mathrm{st}}}
\frac{\partial y_{\mathrm{st}}}{\partial x}
=
\frac{\partial L}{\partial y_{\mathrm{st}}}.
$$

这就是 (2)。取整这类 $Q$ 不含可学习参数，梯度停在 `detach` 处即可，只需经第一项 $x$ 继续向前。