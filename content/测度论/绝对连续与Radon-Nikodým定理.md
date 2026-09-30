---
title: 绝对连续与Radon-Nikodým定理
tags:
  - 测度论
---

## 前置

- [[测度论/符号测度]]

## 定义

- 设 $\nu, \varphi$ 都是 $\mathcal{F}$ 上的符号测度.
  - 如果对满足关系式 $\vert{}\varphi\vert{}(A) = 0$ 的每个 $A \in \mathcal{F}$, 都有 $\nu(A) = 0$, 那么称 $\nu$ 关于 $\varphi$ **绝对连续** (absolutely continuous), 记作 $\nu \ll \varphi$;
  - 如果 $\nu \ll \varphi$, 且 $\varphi \ll \nu$, 那么称 $\nu$ 与 $\varphi$ **等价** (equivalent), 记作 $\nu \sim \varphi$.
- 称$\nu(A) = \int_A f \mathrm{d}\mu$ 中的 $f$ 为 $\nu$ 关于 $\mu$ 的 **Radon-Nikodým 导数** (Radon-Nikodým derivative), 记作 $\frac{\mathrm{d}\nu}{\mathrm{d}\mu}$, 即 $f = \frac{\mathrm{d}\nu}{\mathrm{d}\mu}$, 因而 $\nu(A) = \int_A f \mathrm{d}\mu$ 可以改写为
  $$\nu(A) = \int_A \frac{\mathrm{d}\nu}{\mathrm{d}\mu} \mathrm{d}\mu, \quad \forall A \in \mathcal{F}.$$
  此外, 若 $\nu$ 有限, 知 $f$ a.e. 有限。

## 性质

1. 设 $\nu, \varphi$ 为 $\mathcal{F}$ 上二符号测度, 则下列各条等价:
   (i) $\nu \ll \varphi$;
   (ii) $\nu^+ \ll \varphi$, 且 $\nu^- \ll \varphi$;
   (iii) $\vert{}\nu\vert{} \ll \vert{}\varphi\vert{}$.
2. 设 $\nu, \varphi$ 为 $\mathcal{F}$ 上二符号测度, 其中 $\nu$ 有限, 则 $\nu \ll \varphi$ 当且仅当 $\forall \varepsilon > 0, \exists \delta > 0$, 只要 $A \in \mathcal{F}$ 满足 $\vert{}\varphi\vert{}(A) < \delta$, 就有 $\vert{}\nu\vert{}(A) < \varepsilon$.
3. 设 $\nu$ 和 $\mu$ 都是 $\mathcal{F}$ 上的有限测度, $\nu \ll \mu$, 且 $\nu \neq 0$, 则存在某个 $\varepsilon > 0$ 和 $A \in \mathcal{F}$, 使得 $\mu(A) > 0$ 且 $A$ 是符号测度 $\nu - \varepsilon\mu$ 的正集.
4. 设 $\nu$ 和 $\mu$ 都是 $\mathcal{F}$ 上的测度, 令

   $$
   \mathcal{H} = \left\{ f \in \mathcal{\overline{L}}^+ (\Omega, \mathcal{F}) : \text{对任意的 } A \in \mathcal{F} \text{ 都有 } \int_A f \mathrm{d}\mu \leqslant \nu(A) \right\}
   $$

   则
   (i) $\mathcal{H}$ 非空;
   (ii) 对任意的 $\{f_n, n \geqslant 1\} \subset \mathcal{H}$, 都有 $\sup_{n \geqslant 1} f_n \in \mathcal{H}$;
   (iii) 存在 $f \in \mathcal{H}$, 使得 $\int_\Omega f \mathrm{d}\mu = \alpha$, 其中
   $$\alpha = \sup \left\{ \int_\Omega g \mathrm{d}\mu : g \in \mathcal{H} \right\}. $$

5. **定理 8.21 (Radon-Nikodým 定理)** 设 $\mu$ 为 $\mathcal{F}$ 上的 $\sigma$-有限测度.
   1. 若 $\nu$ 是 $\mathcal{F}$ 上 $\sigma$-有限的符号测度, $\nu \ll \mu$, 则存在一个 $\mu\text{-a.e.}$ 有限的且关于 $\mu$ **积分存在**的 $f \in \overline{\mathcal{L}}(\Omega, \mathcal{F})$, 使得
      $$\nu(A) = \int_A f \mathrm{d}\mu, \quad A \in \mathcal{F}$$
      另外, 上述 $f$ 在等价意义下是唯一的, 即若 $f, g$ 都满足上述等式, 则 $f = g \text{ }\mu\text{-a.e.}$
   2. 若存在一个关于 $\mu$ **可积**的函数 $f$ 使上述等式成立, 则 $\nu$ 是 $\mathcal{F}$ 上 $\sigma$-有限的符号测度, 且 $\nu \ll \mu$.

6. **定理 8.22 (Radon-Nikodým 定理的推广)** 设 $\mu$ 为 $\mathcal{F}$ 上的 $\sigma$-有限测度, $\nu$ 是 $\mathcal{F}$ 上的符号测度 (不必 $\sigma$-有限). 若 $\nu \ll \mu$, 则存在一个在 $\mu\text{-a.e.}$ 意义下唯一的, 且关于 $\mu$ 的积分存在 (不必 $\mu\text{-a.e.}$ 有限) 的广义实值可测函数 $f$ 使
   $$
   \nu(A) = \int_A f \mathrm{d}\mu, \quad A \in \mathcal{F}
   $$
   成立.
7. **习题8.20** 设 $(\Omega, \mathcal{F}, \mu)$ 为测度空间, $f \in \overline{\mathcal{L}}(\Omega, \mathcal{F})$ 关于 $\mu$ 的积分存在, $\nu = f \cdot \mu$.
   则 $\frac{\mathrm{d}\nu^+}{\mathrm{d}\mu} = f^+ \text{ }\mu\text{-a.e.}$, $\frac{\mathrm{d}\nu^-}{\mathrm{d}\mu} = f^- \text{ }\mu\text{-a.e.}$
8. **推论 8.24** 设 $\mu$ 为 $\mathcal{F}$ 上的 $\sigma$-有限测度, $\nu$ 为 $\mathcal{F}$ 上的符号测度, $g \in \overline{\mathcal{L}}(\Omega, \mathcal{F})$. 若 $\nu \ll \mu$, 则 $g$ 关于 $\nu$ 的积分存在当且仅当 $g \frac{\mathrm{d}\nu}{\mathrm{d}\mu}$ 关于 $\mu$ 的积分存在, 此时有
   $$
   \int_A g \mathrm{d}\nu = \int_A \left(g \frac{\mathrm{d}\nu}{\mathrm{d}\mu}\right) \mathrm{d}\mu, \quad \forall A \in \mathcal{F}.
   $$
9. **推论 8.25 (链式法则)** 设 $\mu$ 和 $\nu$ 都是 $\mathcal{F}$ 上的 $\sigma$-有限测度, $\varphi$ 为 $\mathcal{F}$ 上的符号测度. 若 $\varphi \ll \nu, \nu \ll \mu$, 则
   $$\frac{\mathrm{d}\varphi}{\mathrm{d}\mu} = \frac{\mathrm{d}\varphi}{\mathrm{d}\nu} \cdot \frac{\mathrm{d}\nu}{\mathrm{d}\mu} \quad \mu\text{-a.e..}$$
