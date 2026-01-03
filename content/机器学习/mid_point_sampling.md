---
title: 中心点法采样误差分析
---

- [1. 假设](#1-假设)
- [2. 真实解的泰勒展开（基准）](#2-真实解的泰勒展开基准)
- [3. 欧拉法的误差阶（对照）](#3-欧拉法的误差阶对照)
- [4. RK2（中点法）的定义](#4-rk2中点法的定义)
- [5. 中点速度的泰勒展开](#5-中点速度的泰勒展开)
- [6. RK2 更新公式的展开](#6-rk2-更新公式的展开)
- [7. 与真实解逐项对比](#7-与真实解逐项对比)

## 1. 假设

考虑一阶常微分方程（ODE）：

$$
\dot{x}(t) = v(x(t), t), \quad x(t_0) = x_0
$$

假设：

- $v(x,t)$ 在 $x,t$ 上足够光滑（至少三阶连续可导）
- 时间步长为 $\Delta t$

---

## 2. 真实解的泰勒展开（基准）

对真实解 $x(t+\Delta t)$ 在 $t$ 点展开：

$$
x(t+\Delta t) = x(t)+ \Delta t \dot{x}(t)+ \frac{\Delta t^2}{2} \ddot{x}(t)+ \frac{\Delta t^3}{6} \dddot{x}(t) + O(\Delta t^4)
$$

一阶导数

$$
\dot{x}(t) = v(x(t), t)
$$

二阶导数

由于 $v$ 同时依赖于 $x$ 和 $t$，而 $x=x(t)$，使用多变量链式法则：

$$
\ddot{x}(t)
= \frac{d}{dt} v(x(t), t)
= v_x(x(t), t)\dot{x}(t) + v_t(x(t), t)
$$

代入 $\dot{x}(t)=v(x(t),t)$：

$$
\ddot{x}(t)
= v_x(x(t), t)\,v(x(t), t) + v_t(x(t), t)
$$

---

## 3. 欧拉法的误差阶（对照）

欧拉法更新公式：

$$
x_{\text{Euler}}(t+\Delta t)
= x(t) + \Delta t\, v(x(t), t)
$$

局部截断误差

$$
\text{LTE}_{\text{Euler}} = O(\Delta t^2)
$$

全局误差，步数 $N = O(1/\Delta t)$，误差累积：

$$
\text{Global Error}_{\text{Euler}} = O(\Delta t)
$$

---

## 4. RK2（中点法）的定义

第一步：中点预测

$$
x_{\text{mid}}
= x(t) + \frac{\Delta t}{2} v(x(t), t)
$$

$$
t_{\text{mid}} = t + \frac{\Delta t}{2}
$$

第二步：中点斜率

$$
v_{\text{mid}} = v(x_{\text{mid}}, t_{\text{mid}})
$$

最终更新

$$
x_{\text{RK2}}(t+\Delta t)
= x(t) + \Delta t \, v_{\text{mid}}
$$

---

## 5. 中点速度的泰勒展开

对 $v(x,t)$ 在点 $(x(t), t)$ 做二阶泰勒展开：

$$
\begin{aligned}
v(x_{\text{mid}}, t_{\text{mid}})
&= v(x(t), t) \\
&+ v_x(x(t), t)\left(\frac{\Delta t}{2} v(x(t), t)\right)
&+ v_t(x(t), t)\left(\frac{\Delta t}{2}\right) \\
&\quad + O(\Delta t^2)
\end{aligned}
$$

整理得：

$$
v_{\text{mid}}
= v + \frac{\Delta t}{2}(v_x v + v_t) + O(\Delta t^2)
$$

---

## 6. RK2 更新公式的展开

代入更新公式：

$$
\begin{aligned}
x_{\text{RK2}}(t+\Delta t)
&= x(t) + \Delta t v_{\text{mid}} \\
&= x(t) + \Delta t v + \frac{\Delta t^2}{2}(v_x v + v_t) \\
&+ O(\Delta t^3)
\end{aligned}
$$

---

## 7. 与真实解逐项对比

真实解：

$$
x(t+\Delta t)
= x(t) + \Delta t v + \frac{\Delta t^2}{2}(v_x v + v_t) + \frac{\Delta t^3}{6}\dddot{x}(t) + O(\Delta t^4)
$$

RK2 数值解：

$$
x_{\text{RK2}}(t+\Delta t)
= x(t) + \Delta t v + \frac{\Delta t^2}{2}(v_x v + v_t) + O(\Delta t^3)
$$

步数 $N = O(1/\Delta t)$：

$$
\text{Global Error}_{\text{RK2}}
= N \cdot \text{LTE}
= O(\Delta t^2)
$$
