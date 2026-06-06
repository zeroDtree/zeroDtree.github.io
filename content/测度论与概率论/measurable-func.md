---
title: 可测函数
---

## Prerequisites

- [[测度论与概率论/measurable-mapping]]
- [[数学分析/converge]]

## 定义

- 若$f$是从$(\Omega, \mathcal{F})$到$(\mathbb{R}, \mathcal{B}(\mathbb{R}))$的可测映射，则称$f$为$(\Omega, \mathcal{F})$上的可测函数,简称$\mathcal{F}$-可测函数。
- 若$f$是从$(\Omega, \mathcal{F})$到$(\overline{\mathbb{R}}, \mathcal{B}(\overline{\mathbb{R}}))$的可测映射，则称$f$为$(\Omega, \mathcal{F})$上的广义实值可测函数,简称$\mathcal{F}$-可测广义实值函数。
- $\mathcal{L}(\Omega, \mathcal{F})$表示$(\Omega, \mathcal{F})$上的所有可测函数构成的集合。
- $\mathcal{L}^+(\Omega, \mathcal{F})$表示$(\Omega, \mathcal{F})$上的所有非负可测函数构成的集合。
- $\overline{\mathcal{L}}(\Omega, \mathcal{F})$表示$(\Omega, \mathcal{F})$上的所有广义实值可测函数构成的集合。
- $\overline{\mathcal{L}}^+(\Omega, \mathcal{F})$表示$(\Omega, \mathcal{F})$上的所有非负广义实值可测函数构成的集合。
- $C(\Omega)$为$(\Omega, \mathcal{F})$上的所有连续函数构成的集合。定义$\mathcal{B}a:=\sigma(\bigcup_{f\in C(\Omega)} f^{-1}(\mathcal{B}(\mathbb{R})))$，称为Baire $\sigma$-代数。
- $f$为(广义实值)函数，$f^{+}:=f \vee 0, f^{-}:=(-f) \vee 0$
- 设$\{f_{n},n\in \mathbb{N}^{+}\}$为函数列，则可定义$\{f_{n},n\in \mathbb{N}^{+}\}$的下确界、上确节、下极限、上极限
  - $(\inf_{n\geq 1} f_{n})(\omega):= \inf_{n\geq 1} f_{n}(\omega)$
  - $(\sup_{n\geq 1} f_{n})(\omega):= \sup_{n\geq 1} f_{n}(\omega)$
  - $(\liminf\limits_{n\geq 1} f_{n})(\omega):= \liminf\limits_{n\geq 1} f_{n}(\omega)$
  - $(\limsup\limits_{n\geq 1} f_{n})(\omega):= \limsup\limits_{n\geq 1} f_{n}(\omega)$
- **简单可测函数**： 设$(\Omega, \mathcal{F})$为可测空间，$A_1,A_2,\cdots,A_n \in \mathcal{F}$ 是$\Omega$的一个划分，$a_1,a_2,\cdots,a_n \in \mathbb{R}$，则称函数$f:\Omega \to \mathbb{R},f=\sum_{i=1}^{n} a_i I_{A_i}$为简单可测函数。所有的简单可测函数记作$S(\Omega, \mathcal{F})$，所有的非负简单可测函数记作$S^+(\Omega, \mathcal{F})$。

## 性质

1.  设$(\Omega, \rho)$为度量空间，则$\mathcal{B}a(\Omega)=\mathcal{B}(\Omega)$
2.  可测函数的判别方法：$f\in \mathcal{L}(\Omega, \mathcal{F})$等价于下列条件之一：
    - $\forall b \in \mathbb{R}, \{f<b\} \in \mathcal{F}$
    - $\forall b \in \mathbb{R}, \{f\leq b\} \in \mathcal{F}$
    - $\forall a \in \mathbb{R}, \{f>a\} \in \mathcal{F}$
    - $\forall a \in \mathbb{R}, \{f\geq a\} \in \mathcal{F}$
3.  广义实值可测函数的判别方法：$f\in \overline{\mathcal{L}}(\Omega, \mathcal{F})$等价于下列条件之一：
    - $\forall b \in \mathbb{R}, \{f<b\} \in \mathcal{F}$
    - $\forall b \in \mathbb{R}, \{f\leq b\} \in \mathcal{F}$
    - $\forall a \in \mathbb{R}, \{f>a\} \in \mathcal{F}$
    - $\forall a \in \mathbb{R}, \{f\geq a\} \in \mathcal{F}$
4.  常值函数是(广义实值)可测函数
5.  可测函数的基本性质：
    - $f,g\in \overline{\mathcal{L}}(\Omega, \mathcal{F})$，则$\{f<g\},\{f=g\},\{f\leq g\} \in \mathcal{F}$
    - $f,g \in \mathcal{L}(\Omega, \mathcal{F}), \lambda \in \mathbb{R}$,则$\lambda f, f+g, fg, f/g \in \mathcal{L}(\Omega, \mathcal{F})$
    - $f,g\in \overline{\mathcal{L}}(\Omega, \mathcal{F})$,则$f\vee g, f\wedge g \in \overline{\mathcal{L}}(\Omega, \mathcal{F})$
    - $f,g\in \mathcal{L}(\Omega, \mathcal{F})$,则$f\vee g, f\wedge g \in \mathcal{L}(\Omega, \mathcal{F})$
6.  可测函数极限的性质
    - $f\in \mathcal{L}(\Omega, \mathcal{F}) \iff f^{+},f^{-} \in \mathcal{L}(\Omega, \mathcal{F}) \implies |f| \in \mathcal{L}(\Omega, \mathcal{F})$
    - $f\in \overline{\mathcal{L}}(\Omega, \mathcal{F}) \iff f^{+},f^{-} \in \overline{\mathcal{L}}(\Omega, \mathcal{F}) \implies |f| \in \overline{\mathcal{L}}(\Omega, \mathcal{F})$
    - 设$\{f_n, n \geq 1\} \subseteq \overline{\mathcal{L}}(\Omega, \mathcal{F})$，则$\inf_{n\geq 1} f_n, \sup_{n\geq 1} f_n, \liminf\limits_{n\geq 1} f_n, \limsup\limits_{n\geq 1} f_n \in \overline{\mathcal{L}}(\Omega, \mathcal{F})$
7.  向量值可测函数
    - $\mathbf{f}\in \mathcal{F}/\mathcal{B}(\mathbb{R}^d) \iff f_i \in \mathcal{F}/\mathcal{B}(\mathbb{R}),\forall i \in [d]$
8.  复值可测函数
    - $\mathbf{f}:\Omega \to \mathbb{C}$,$\mathbf{f}=Re\mathbf{f}+iIm\mathbf{f}$, 则$\mathcal{f}\in \mathcal{F}/\mathcal{B}(\mathbb{C}) \iff Re\mathbf{f},Im\mathbf{f}\in \mathcal{F}/\mathcal{B}(\mathbb{R})$
9.  简单可测函数加减仍为简单可测函数
    - $f,g\in S(\Omega, \mathcal{F}) \implies f+g\in S(\Omega, \mathcal{F})$
10. 设$(\Omega, \mathcal{F})$为可测空间，$f:\Omega \to \overline{\mathbb{R}}$,则：
    - 若$f$非负可测，则存在$\{f_n,n\geq 1\} \subseteq S^+(\Omega, \mathcal{F})$，使得$f_n \uparrow f$
    - $f$可测$\iff$存在$\{f_n,n\geq 1\} \subseteq S(\Omega, \mathcal{F})$，使得$f_n \to f$
11. 设$\phi\in\sigma(f)/\mathcal{B}(\mathbb{R})\iff \exists g\in \overline{\mathcal{L}}(\Omega, \mathcal{F}),s.t.\ \phi=g\circ f$
12. 函数形式的单调类定理：$f$为实值函数或有界
    - 设$\mathcal{E}$为$\Omega$上的一个$\pi$类，$\mathcal{H}$为$\mathcal{E}$上的一个由实值函数构成的线性空间，且满足<br>
      1. $1\in \mathcal{H}$
      2. $(f_n\in H,n\geq1, 0 \leq f_n \uparrow f) \implies f\in H$<br>
      3. $\forall A \in \mathcal{E}, I_A \in H$
         则$\mathcal{H}$包含所有$\sigma(\mathcal{E})$-可测的实值或有界函数.
