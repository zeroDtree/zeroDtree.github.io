---
title: 几乎处处收敛
---

## 前置

[[测度论与概率论/measurable-func]]

## 定义

- 设$f,g$均为定义在测度空间$(\Omega,\mathcal{F},\mu)$上的广义实值函数
  - 若$\mu(f\not=\pm\infty)=0$,则称$f$**几乎处处有限**(finite almost everywhere)(a.e. 有限)
  - 若$\exists M>0$ s.t. $\mu(|f| > M)=0$, 则称$f$**几乎处处有界**(bounded almost everywhere)(a.e. 有界)
  - 若$\mu(f\not=g)=0$,则称$f$与$g$**几乎处处相等**(equal almost everywhere)($f=g$ a.e.)
  - 若$\mu(f < g)=0$, 则称$f$**几乎处处大于**($f \geq g$ a.e.)
  - 若$\exists g \in \overline{\mathcal{L}}(\Omega,\mathcal{F})$ s.t. $f=g$ a.e.,则称$f$**几乎处处可测**(measurable almost everywhere)(a.e. 可测)
- 设$\{f,f_n, n\geq1\}$是a.e.有限的广义实值函数列，若存在零测集$N$使得$\omega \in N^c$时,$f_n(\omega) \to f(\omega)$，则称$f_n$**几乎处处收敛**(almost everywhere convergence)(a.e. 收敛)到$f$。记作$f_n \overset{a.e.}{\to} f$。
- 设$\{f,f_n, n\geq 1\}$是a.e.有限的广义实值函数列，若存在零测集$N$使得$\omega \in N^c$时，$\{f_n,n\geq 1\}$为基本列，则称$\{f_n\}$为**几乎处处收敛的基本列**

测度论中的a.e.(**almost everywhere**) 就是概率论里的a.s.(**almost surely**)

## 性质

1. 若$\mu$是$\mathcal{F}$上的完备测度，则
   - 几乎处处相等的函数要么都可测，要么都不可测。
   - 几乎处处可测函数是可测函数。
2. 设$\{f_n, n\geq 1\} \subseteq \overline{\mathcal{L}}(\Omega,\mathcal{F})$，$f$为广义实值函数，$f_n \overset{a.e.}{\to} f$，则$f$ a.e.可测，进一步地若$\mu$为完备测度，那么$f$可测。
3. 设$\{f,f_n, n\geq 1\}$是a.e.有限的广义实值可测函数列，则
   $f_n \overset{a.e.}{\to} f$ $\iff$ $\mu(\bigcap\limits_{n=1}^{\infty}\bigcup\limits_{k=n}^{\infty}\{|f_k - f| \geq \epsilon\})=0,\forall \epsilon$
4. 设$\{f,f_n, n\geq 1\}$是a.e.有限的广义实值可测函数列,$\mu$为有限测度，则
   $f_n \overset{a.e.}{\to} f \iff \lim\limits_{n\to \infty}\mu(\bigcup\limits_{k=n}^{\infty}\{|f_k - f| \geq \epsilon\})=0,\forall \epsilon>0 \iff \lim\limits_{n\to \infty}\mu\{\sup\limits_{k\geq n}|f_k - f| \geq \epsilon\}=0,\forall \epsilon>0$
5. 设$\{f_n, n\geq 1\}$是a.e.有限的广义实值可测函数列，则$\{f_n\}$为几乎处处收敛的基本列当且仅当
   $\mu(\bigcap\limits_{n=1}^{\infty}\bigcup\limits_{k=n}^{\infty}\{|f_k - f_n| \geq \epsilon\})=0,\forall \epsilon>0$
6. 设 $\{f_n, n \geq 1\}$ 是 a.e. 有限的广义实值可测函数列。
   - 若$\lim\limits_{n \to \infty} \mu \left( \bigcup_{k=n}^\infty \{\, |f_k - f_n| \geq \varepsilon \,\} \right) = 0,\quad \forall \varepsilon > 0 \iff 
  \lim\limits_{n \to \infty} \mu \left( \left\{ \sup_{k \geq n} |f_k - f_n| \geq \varepsilon \right\} \right) = 0, \quad \forall \varepsilon > 0.$
     则 $\{f_n\}$ 为几乎处处收敛的基本列；
   - 当 $\{f_n\}$ 为几乎处处收敛的基本列，且 $\mu$ 为有限测度时，上式成立。
7. 设 $\{f_n,\; n\ge 1\}$ 是 a.e. 有限的广义实值可测函数列，（且$\mu$为有限测度?）,则
   $\{f_n\}$ 为几乎处处收敛的基本列当且仅当存在某个广义实值可测函数 $f$，使得$f_n \xrightarrow{\text{a.e.}} f.$
