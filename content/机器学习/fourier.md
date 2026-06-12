---
title: 傅里叶变换
---

## 前置

-
- [[机器学习/Dirac分布]]

## 傅里叶级数

### 定义

设 $f$ 为周期 $T$ 的复值函数，且在单个周期内平方可积：$f \in L^2([-T/2, T/2])$。令基频 $\omega_0 = 2\pi/T$。函数组 $\{e^{\mathrm{j} n \omega_0 t}\}_{n=-\infty}^{\infty}$ 构成 $L^2([-T/2,T/2])$ 的一组规范正交基，故

$$
f(t) = \sum_{n=-\infty}^{\infty} c_n e^{\mathrm{j} n \omega_0 t},
$$

其中傅里叶系数（分析公式）为

$$
c_n = \frac{1}{T} \int_{-T/2}^{T/2} f(t) e^{-\mathrm{j} n \omega_0 t}\, dt
= \langle f, e^{\mathrm{j} n \omega_0 t} \rangle.
$$

## 从 FS 到 FT

**核心思想**：非周期函数可视为周期 $T \to \infty$ 的极限情形。

当 $T \to \infty$ 时，$\omega_0 = 2\pi/T \to 0$，离散频点 $n\omega_0$ 的间隔趋于连续变量 $\omega$。将 $c_n$ 代入合成公式：

$$
f(t) = \sum_{n=-\infty}^{\infty} \left[ \frac{1}{T} \int_{-T/2}^{T/2} f(\tau) e^{-\mathrm{j} n \omega_0 \tau}\, d\tau \right] e^{\mathrm{j} n \omega_0 t}.
$$

由 $1/T = \omega_0/(2\pi)$，上式化为

$$
f(t) = \frac{1}{2\pi} \sum_{n=-\infty}^{\infty} \left[ \int_{-T/2}^{T/2} f(\tau) e^{-\mathrm{j} (n \omega_0) \tau}\, d\tau \right] e^{\mathrm{j} (n \omega_0) t}\, \omega_0.
$$

令 $T \to \infty$，求和 $\sum (\cdots)\,\omega_0$ 在 Riemann 和意义下趋于积分。定义**连续傅里叶变换**（FT）与**逆变换**（IFT）：

$$
F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-\mathrm{j} \omega t}\, dt, \qquad
f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) e^{\mathrm{j} \omega t}\, d\omega.
$$

| 变换 | 时域         | 频域                               |
| ---- | ------------ | ---------------------------------- |
| FS   | 连续、周期   | 离散、非周期（系数 $c_n$）         |
| FT   | 连续、非周期 | 连续、非周期（谱密度 $F(\omega)$） |

FT 是 FS 在周期趋于无穷时的极限形式。

## 从 FT 到 DFT

将 FT 离散化需两步：**时域采样**（得到 DTFT）与**频域采样**（得到 DFT）。

### 时域采样与 DTFT

理想采样等价于用 Dirac 梳 $p(t) = \sum_{n=-\infty}^{\infty} \delta(t - nT_s)$ 调制连续信号：

$$
f_s(t) = f(t)\, p(t) = \sum_{n=-\infty}^{\infty} f(nT_s)\, \delta(t - nT_s).
$$

对 $f_s$ 作 FT：

$$
F_s(\omega) = \sum_{n=-\infty}^{\infty} f(nT_s)\, e^{-\mathrm{j} \omega n T_s}.
$$

令 $\Omega = \omega T_s$，$x[n] = f(nT_s)$，得**离散时间傅里叶变换**（DTFT）：

$$
X(e^{\mathrm{j}\Omega}) = \sum_{n=-\infty}^{\infty} x[n]\, e^{-\mathrm{j} \Omega n}.
$$

### 频域采样与 DFT

DTFT 的频域仍连续，无法直接存储。在 $[0, 2\pi)$ 上取 $N$ 个等间隔频点 $\Omega_k = 2\pi k/N$（$k = 0,\dots,N-1$），并设时域仅在 $0 \leq n \leq N-1$ 非零，代入 DTFT 得 **DFT**：

$$
X[k] = \sum_{n=0}^{N-1} x[n]\, e^{-\mathrm{j} \frac{2\pi}{N} k n}, \qquad k = 0, 1, \dots, N-1.
$$
