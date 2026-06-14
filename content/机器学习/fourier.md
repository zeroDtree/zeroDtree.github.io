---
title: 傅里叶变换
---

## 前置

- [[机器学习/Dirac分布]]

## 傅里叶级数

### 定义

设 $f$ 为周期 $T$ 的复值函数，且在单个周期内平方可积：$f \in L^2([-T/2, T/2])$。令基频 $\omega_0 = 2\pi/T$。函数组 $\{e^{\mathrm{j} n \omega_0 t}\}_{n=-\infty}^{\infty}$ 构成 $L^2([-T/2,T/2])$ 的一组正交基（非规范化），满足

$$
\int_{-T/2}^{T/2} e^{\mathrm{j} n \omega_0 t}\, e^{-\mathrm{j} m \omega_0 t}\, dt = T\,\delta_{mn},
$$

故

$$
f(t) = \sum_{n=-\infty}^{\infty} c_n e^{\mathrm{j} n \omega_0 t},
$$

其中傅里叶系数（分析公式）为

$$
c_n = \frac{1}{T} \int_{-T/2}^{T/2} f(t) e^{-\mathrm{j} n \omega_0 t}\, dt
= \frac{1}{T} \langle f, e^{\mathrm{j} n \omega_0 t} \rangle,
$$

其中 $\langle f, g \rangle = \displaystyle\int_{-T/2}^{T/2} f(t)\overline{g(t)}\,dt$。

## 从 FS 到 FT

**核心思想**：对非周期信号 $f$，在区间 $[-T/2, T/2]$ 上截断并作周期延拓；当 $T \to \infty$ 时，其傅里叶级数趋于傅里叶变换。

当 $T \to \infty$ 时，$\omega_0 = 2\pi/T \to 0$，离散频点 $n\omega_0$ 的间隔趋于连续变量 $\omega$。将 $c_n$ 代入合成公式：

$$
f(t) = \sum_{n=-\infty}^{\infty} \left[ \frac{1}{T} \int_{-T/2}^{T/2} f(\tau) e^{-\mathrm{j} n \omega_0 \tau}\, d\tau \right] e^{\mathrm{j} n \omega_0 t}.
$$

由 $1/T = \omega_0/(2\pi)$，上式化为

$$
f(t) = \frac{1}{2\pi} \sum_{n=-\infty}^{\infty} \left[ \int_{-T/2}^{T/2} f(\tau) e^{-\mathrm{j} (n \omega_0) \tau}\, d\tau \right] e^{\mathrm{j} (n \omega_0) t}\, \omega_0.
$$

记括号内积分为 $F(n\omega_0)$，令 $\omega = n\omega_0$、$d\omega = \omega_0$，则求和 $\sum_n F(n\omega_0)\,\omega_0$ 在 Riemann 和意义下趋于 $\displaystyle\int F(\omega)\,d\omega$。令 $T \to \infty$，定义**连续傅里叶变换**（FT）与**逆变换**（IFT）：

$$
F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-\mathrm{j} \omega t}\, dt, \qquad
f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) e^{\mathrm{j} \omega t}\, d\omega.
$$

## 从 FT 到 DFT

将 FT 离散化需两步：**时域采样**（得到 DTFT）与**频域采样**（得到 DFT）。

### 时域采样与 DTFT

理想采样等价于用 Dirac 梳 $p(t) = \sum_{n=-\infty}^{\infty} \delta(t - nT_s)$ 调制连续信号：

$$
f_s(t) = f(t)\, p(t) = \sum_{n=-\infty}^{\infty} f(nT_s)\, \delta(t - nT_s).
$$

对 $f_s$ 作 FT，利用 $\delta$ 的抽样性质：

$$
F_s(\omega) = \int \sum_{n=-\infty}^{\infty} f(nT_s)\, \delta(t - nT_s)\, e^{-\mathrm{j} \omega t}\, dt
= \sum_{n=-\infty}^{\infty} f(nT_s)\, e^{-\mathrm{j} \omega n T_s}.
$$

令 $\Omega = \omega T_s$，$x[n] = f(nT_s)$，得**离散时间傅里叶变换**（DTFT）：

$$
X(e^{\mathrm{j}\Omega}) = \sum_{n=-\infty}^{\infty} x[n]\, e^{-\mathrm{j} \Omega n}.
$$

DTFT 的频域连续且 $2\pi$ 周期：

$$
X(e^{\mathrm{j}(\Omega + 2\pi)}) = X(e^{\mathrm{j}\Omega}),
$$

这是 DTFT 与 FT 的关键区别之一：时域离散化导致频域周期延拓。

### 频域采样与 DFT

DTFT 的频域仍连续，无法直接存储。对长度为 $N$ 的序列 $x[n]$，在 DTFT 的一个周期 $[0, 2\pi)$ 上取 $N$ 个均匀频点 $\Omega_k = 2\pi k/N$（$k = 0,\dots,N-1$），代入 DTFT 得 **DFT**：

$$
X[k] = \sum_{n=0}^{N-1} x[n]\, e^{-\mathrm{j} \frac{2\pi}{N} k n}, \qquad k = 0, 1, \dots, N-1.
$$
