> [!abstract] 定理（唯一非周期闭类下的逐时刻收敛）
> 设 $Q$ 恰好有一个闭沟通类，且该闭类非周期，$\pi$ 为唯一平稳分布。则
>
> $$
> Q^n\longrightarrow\mathbf 1\pi.
> $$
>
> 从而对任意初始分布 $\nu_0\in\Delta_{K-1}$，都有 $\nu_0 Q^n\to\pi$。
>
> > [!note]- 证明
> > 先设 $Q$ 不可约且非周期（即 $T=\emptyset$）。由上引理知 $Q$ 为本原矩阵。由 $Q\mathbf 1=\mathbf 1$ 及 $\|Q\|_\infty=1$ 知谱半径 $\rho(Q)=1$。由本原非负矩阵的 Perron--Frobenius 定理，特征值 $1$ 的代数重数为 $1$，且其余特征值均满足 $|\lambda|<1$。特征值 $1$ 的右特征向量为 $\mathbf 1$，左特征向量为 $\pi$，且 $\pi\mathbf 1=1$，故对应的谱投影为 $\mathbf 1\pi$。对任一满足 $|\lambda|<1$ 的 $r$ 阶 Jordan 块 $J=\lambda I+N$（$N^r=0$），有
> >
> > $$
> > J^n
> > = \sum_{s=0}^{r-1}\binom{n}{s}\lambda^{n-s}N^s
> > \longrightarrow 0
> > \qquad(n\to\infty),
> > $$
> >
> > 故 $Q^n\to\mathbf 1\pi$。左乘 $\nu_0$ 得 $\nu_0 Q^n\to\nu_0\mathbf 1\,\pi=\pi$。
> >
> > 再设唯一闭沟通类 $C_1$ 非周期，而 $T$ 可能非空。记 $C_1=\{i_1,\dots,i_{r_1}\}$（$r_1:=|C_1|$），在分块顺序 $(T,C_1)$ 下，对任意 $a,b\in\{1,\dots,r_1\}$ 有 $(Q^n)_{i_a,i_b}=(Q_1^n)_{ab}$ 且 $\pi_{i_b}=\pi^{(1)}_b$。限制矩阵 $Q_1\in\mathbb R^{r_1\times r_1}$ 不可约且非周期，故对每个 $b\in\{1,\dots,r_1\}$，
> >
> > $$
> > \delta_n
> > := \max_{1\le a\le r_1}\bigl|(Q_1^n)_{ab}-\pi^{(1)}_b\bigr|
> > \longrightarrow 0.
> > $$
> >
> > 由前面暂态逃逸的估计，存在 $N\ge 1$ 与 $\varepsilon\in(0,1]$ 使 $\|Q_{TT}^N\|_\infty\le 1-\varepsilon$，故 $\|Q_{TT}^{kN}\|_\infty\le(1-\varepsilon)^k$，从而 $Q_{TT}^n\to 0$。当 $j\in T$ 时，$\pi_j=0$，且对任意 $i\in E$ 有 $(Q^n)_{ij}\le\mathbb P_i(X_n\in T)\to 0=\pi_j$。
> >
> > 当 $j=i_b\in C_1$（$1\le b\le r_1$）时，若 $i=i_a\in C_1$（$1\le a\le r_1$），则 $(Q^n)_{ij}=(Q^n)_{i_a,i_b}=(Q_1^n)_{ab}\to\pi^{(1)}_b=\pi_j$。若 $i\in T$，记进入 $C_1$ 的首达时为 $\sigma$，则
> >
> > $$
> > \mathbb P_i(X_n=j)
> > = \sum_{t=1}^n\sum_{a=1}^{r_1}\mathbb P_i(\sigma=t,X_t=i_a)\,(Q_1^{n-t})_{ab}.
> > $$
> >
> > 因 $\{\sigma>n\}=\{X_n\in T\}$，有 $\mathbb P_i(\sigma>kN)\le(1-\varepsilon)^k$，故 $\mathbb P_i(\sigma>n)\to 0$。又
> >
> > $$
> > \bigl|
> > \mathbb P_i(X_n=j)-\pi_j\mathbb P_i(\sigma\le n)
> > \bigr|
> > \le
> > \sum_{t=1}^n\mathbb P_i(\sigma=t)\,\delta_{n-t}.
> > $$
> >
> > 对任意 $\eta>0$，取 $M$ 使 $n\ge M$ 时 $\delta_n<\eta$，再取 $n>M$ 使 $\mathbb P_i(\sigma>n-M)<\eta$。由于 $\delta_{n-t}\le 1$，将和式按 $t\le n-M$ 与 $t>n-M$ 拆开可得上式右端小于 $2\eta$，且 $\pi_j\mathbb P_i(\sigma>n)<\eta$。故当 $n$ 充分大时 $\bigl|(Q^n)_{ij}-\pi_j\bigr|<3\eta$，即 $(Q^n)_{ij}\to\pi_j$。因此 $Q^n\to\mathbf 1\pi$。$\square$


### 算例：环上惰性随机游走

设 $K\ge 3$，$\alpha\in(0,1)$，状态空间取环 $E=\mathbb Z_K=\{0,1,\dots,K-1\}$。每一步以概率 $1-\alpha$ 停留原地，以概率 $\alpha/2$ 移至左邻或右邻：

$$
Q_{ij} =
\begin{cases}
1-\alpha & j=i, \\
\alpha/2 & j\equiv i\pm 1\pmod{K}, \\
0 & \text{其他}.
\end{cases}
$$

$Q$ 由首行 $(1-\alpha,\alpha/2,0,\dots,0,\alpha/2)$ 循环生成，故为双随机矩阵（行和与列和均为 $1$），均匀分布 $\pi=\frac1K\mathbf 1^\top$ 满足 $\pi Q=\pi$。沿环逐步转移可到达任意状态，故链不可约；又 $Q_{ii}=1-\alpha>0$，故周期 $d=1$。由收敛定理知 $Q^n\to\mathbf 1\pi$，对任意初始分布 $\nu_0$ 均有 $\nu_n\to\pi$。

### Cesàro 平均收敛

当唯一闭沟通类有周期时，$\nu_n=\nu_0 Q^n$ 未必逐时刻收敛，但其 Cesàro 平均仍然收敛。

> [!abstract] 定理（唯一平稳分布下的 Cesàro 收敛）
> 若 $\pi$ 是 $Q$ 的唯一平稳分布，则对任意 $\nu_0\in\Delta_{K-1}$，
>
> $$
> \frac1N\sum_{n=0}^{N-1}\nu_0 Q^n
> \longrightarrow
> \pi.
> $$
>
> > [!note]- 证明
> > 记 $\bar\nu_N:=N^{-1}\sum_{n=0}^{N-1}\nu_0 Q^n\in\Delta_{K-1}$。由存在性证明二知 $\|\bar\nu_N Q-\bar\nu_N\|_\infty\le 1/N$。对 $\bar\nu_N$ 的任一收敛子列 $\bar\nu_{N_k}\to\mu$，有 $\mu\in\Delta_{K-1}$ 且 $\mu Q=\mu$；由平稳分布唯一性得 $\mu=\pi$。
> >
> > 若 $\bar\nu_N$ 不收敛于 $\pi$，则存在 $\varepsilon>0$ 及子列使 $\|\bar\nu_{N_k}-\pi\|_\infty\ge\varepsilon$。因 $\Delta_{K-1}$ 紧，该子列存在收敛子列，其极限与 $\pi$ 的距离至少为 $\varepsilon$，矛盾。故 $\bar\nu_N\to\pi$。$\square$

从谱上看，周期链在单位圆上除 $1$ 外的特征值 $\lambda$（$|\lambda|=1,\ \lambda\neq 1$）满足

$$
\frac1N\sum_{n=0}^{N-1}\lambda^n
= \frac{1-\lambda^N}{N(1-\lambda)}
\longrightarrow 0,
$$

Cesàro 平均消去了单位圆上非 $1$ 特征值对应的振荡分量。

## 样本路径的时间平均

> [!abstract] 定理（有限不可约链的遍历定理）
> 设链有限且不可约，$\pi$ 为唯一平稳分布。则对任意函数 $f:E\to\mathbb R$ 和任意初始分布 $\nu_0$，
>
> $$
> \frac1N\sum_{n=0}^{N-1}f(X_n)
> \xrightarrow[N\to\infty]{\text{a.s.}}
> \sum_{i=1}^K\pi_i f(i).
> $$
>
> 特别地，取 $f=\mathbf 1_{\{j\}}$，得状态 $j$ 的长期访问频率：
>
> $$
> \frac1N\sum_{n=0}^{N-1}\mathbf 1_{\{X_n=j\}}
> \xrightarrow[N\to\infty]{\text{a.s.}}
> \pi_j.
> $$
>
> > [!note]- 证明
> > 记 $\mathbb P_i$、$\mathbb E_i$ 为从 $X_0=i$ 出发的概率与期望。固定状态 $r\in E$，定义首次正返回时
> >
> > $$
> > \tau
> > :=
> > \inf\{n\ge 1:X_n=r\}.
> > $$
> >
> > 先证 $\mathbb E_r[\tau]<\infty$。由不可约性，对每个 $i\neq r$ 存在步数 $n_i\le K-1$ 使 $\mathbb P_i(X_{n_i}=r)>0$；对 $r$ 存在最短正返回路径，步数 $n_r\le K$，满足 $\mathbb P_r(\tau\le n_r)>0$。取 $\ell:=\max_{i\in E}n_i\le K$，并令
> >
> > $$
> > \varepsilon
> > :=
> > \min\Bigl(
> > \{\mathbb P_r(\tau\le\ell)\}
> > \cup
> > \{\mathbb P_i(X_{n_i}=r):i\neq r\}
> > \Bigr)>0,
> > $$
> >
> > 则对任意 $i\neq r$，由 $1\le n_i\le\ell$ 知 $\mathbb P_i(\exists\,m\in\{1,\dots,\ell\},\ X_m=r)\ge\mathbb P_i(X_{n_i}=r)\ge\varepsilon$。因 $\{\tau>n\}=\{X_1\neq r,\dots,X_n\neq r\}\in\mathcal F_n^X$，且在事件 $\{\tau>k\ell\}$（$k\ge 1$）上有 $X_{k\ell}\neq r$，由 Markov 性知在该事件上
> >
> > $$
> > \mathbb P_r\bigl(\tau>(k+1)\ell\bigm|\mathcal F_{k\ell}^X\bigr)
> > \le
> > 1-\varepsilon.
> > $$
> >
> > 两边取期望并结合 $k=0$ 时的 $\mathbb P_r(\tau>\ell)\le 1-\varepsilon$，归纳得 $\mathbb P_r(\tau>k\ell)\le(1-\varepsilon)^k$（$\forall k\ge 0$）。故 $\mathbb P_r(\tau<\infty)=1$，且
> >
> > $$
> > \mathbb E_r[\tau]
> > = \sum_{n=0}^\infty\mathbb P_r(\tau>n)
> > \le \sum_{k=0}^\infty\ell\,\mathbb P_r(\tau>k\ell)
> > \le \frac\ell\varepsilon
> > < \infty.
> > $$
> >
> > 定义单循环内各状态的期望访问次数 $\mathbf m=(m_1,\dots,m_K)$：
> >
> > $$
> > m_j
> > := \mathbb E_r\Biggl[\sum_{n=0}^{\tau-1}\mathbf 1_{\{X_n=j\}}\Biggr]
> > = \sum_{n=0}^\infty\mathbb P_r(X_n=j,\tau>n).
> > $$
> >
> > 显然 $m_r=1$，且 $\sum_{j=1}^K m_j=\mathbb E_r[\tau]$。由 $\{\tau>n\}\in\mathcal F_n^X$ 及 Markov 性，
> >
> > $$
> > \mathbb P_r(X_n=i,\tau>n,X_{n+1}=j)
> > = \mathbb P_r(X_n=i,\tau>n)\,Q_{ij}.
> > $$
> >
> > 对 $i$ 与 $n$ 求和得
> >
> > $$
> > \sum_{i=1}^K m_i Q_{ij}
> > = \sum_{n=0}^\infty\mathbb P_r(\tau>n,X_{n+1}=j)
> > = \sum_{n=1}^\infty\mathbb P_r(\tau\ge n,X_n=j).
> > $$
> >
> > 当 $j\neq r$ 时，$X_n=j$ 蕴含 $\tau\neq n$，且 $X_0=r\neq j$，故右端等于 $\sum_{n=0}^\infty\mathbb P_r(\tau>n,X_n=j)=m_j$；当 $j=r$ 时，$n\ge 1$ 且 $X_n=r$ 蕴含 $\tau\le n$，故 $\{\tau\ge n,X_n=r\}=\{\tau=n\}$，右端等于
> >
> > $$
> > \sum_{n=1}^\infty\mathbb P_r(\tau=n)
> > = \mathbb P_r(\tau<\infty)
> > = 1
> > = m_r.
> > $$
> >
> > 因此 $\mathbf m Q=\mathbf m$。由平稳分布唯一性及 $\mathbf m\mathbf 1=\mathbb E_r[\tau]$，得
> >
> > $$
> > m_j=\pi_j\,\mathbb E_r[\tau].
> > $$
> >
> > 令 $R:=\sum_{n=0}^{\tau-1}f(X_n)$，则 $\mathbb E_r|R|\le\|f\|_\infty\mathbb E_r[\tau]<\infty$，且
> >
> > $$
> > \mathbb E_r[R]
> > = \sum_{j=1}^K f(j)m_j
> > = \mathbb E_r[\tau]\sum_{j=1}^K\pi_j f(j).
> > $$
> >
> > 设 $X_0=r$，定义依次返回 $r$ 的停时列 $\tau_0:=0$，$\tau_{k+1}:=\inf\{n>\tau_k:X_n=r\}$，以及循环长度 $L_k:=\tau_k-\tau_{k-1}$、循环累计和 $R_k:=\sum_{n=\tau_{k-1}}^{\tau_k-1}f(X_n)$。由强 Markov 性，$(L_k,R_k)_{k\ge 1}$ 在 $\mathbb P_r$ 下独立同分布，且与 $(\tau,R)$ 同分布。由强大数定律，在 $\mathbb P_r$ 下几乎必然有
> >
> > $$
> > \frac1M\sum_{k=1}^M R_k
> > \longrightarrow
> > \mathbb E_r[R],
> > \qquad
> > \frac1M\sum_{k=1}^M L_k
> > \longrightarrow
> > \mathbb E_r[\tau],
> > $$
> >
> > 从而
> >
> > $$
> > \frac{\sum_{k=1}^M R_k}{\sum_{k=1}^M L_k}
> > \longrightarrow
> > \sum_{j=1}^K\pi_j f(j).
> > $$
> >
> > 对时刻 $N$，令 $M(N):=\max\{M\ge 0:\tau_M\le N\}$，$S_M:=\sum_{k=1}^M L_k=\tau_M$。则 $S_{M(N)}\le N<S_{M(N)+1}$，$M(N)\to\infty$（$\mathbb P_r$-a.s.），且
> >
> > $$
> > \sum_{n=0}^{N-1}f(X_n)
> > = \sum_{k=1}^{M(N)}R_k + \rho_N,
> > \qquad
> > |\rho_N| \le \|f\|_\infty L_{M(N)+1}.
> > $$
> >
> > 由 $S_M/M\to\mathbb E_r[\tau]$ 及 $S_{M(N)}\le N<S_{M(N)+1}$ 得 $N/M(N)\to\mathbb E_r[\tau]$，$S_{M(N)}/N\to 1$。又 $L_M/M=S_M/M-S_{M-1}/M\to 0$，故
> >
> > $$
> > \frac{|\rho_N|}N
> > \le \|f\|_\infty\frac{L_{M(N)+1}}{M(N)+1}\cdot\frac{M(N)+1}N
> > \longrightarrow 0.
> > $$
> >
> > 于是
> >
> > $$
> > \frac1N\sum_{n=0}^{N-1}f(X_n)
> > = \frac{S_{M(N)}}N\cdot\frac{\sum_{k=1}^{M(N)}R_k}{S_{M(N)}} + \frac{\rho_N}N
> > \xrightarrow[N\to\infty]{\mathbb P_r\text{-a.s.}} \sum_{j=1}^K\pi_j f(j).
> > $$
> >
> > 若 $X_0=i\neq r$，令首达时 $\sigma:=\inf\{n\ge 0:X_n=r\}$，同样有 $\mathbb P_i(\sigma>k\ell)\le(1-\varepsilon)^k$，故 $\sigma<\infty$（$\mathbb P_i$-a.s.）。$\sigma$ 之前的有限和满足 $\bigl|\sum_{n=0}^{\sigma-1}f(X_n)\bigr|/N\le\|f\|_\infty\sigma/N\to 0$；对 $N>\sigma$，
> >
> > $$
> > \frac1N\sum_{n=\sigma}^{N-1}f(X_n)
> > = \frac{N-\sigma}N\cdot\frac1{N-\sigma}\sum_{t=0}^{N-\sigma-1}f(X_{\sigma+t})
> > \xrightarrow[N\to\infty]{\mathbb P_i\text{-a.s.}} \sum_{j=1}^K\pi_j f(j).
> > $$
> >
> > 对一般初始分布 $\nu_0$，由 $\mathbb P_{\nu_0}=\sum_{i=1}^K(\nu_0)_i\mathbb P_i$ 即得结论。$\square$

若链恰有一个闭沟通类 $C_1$（允许暂态集 $T\neq\emptyset$），由于从任意状态进入 $C_1$ 的首达时几乎必然有限，且唯一平稳分布 $\pi$ 在 $T$ 上为 $0$，上述遍历定理对任意初始分布仍然成立。

## 条件汇总

对有限状态离散时间时齐马尔可夫链（转移矩阵 $Q$ 行随机）：

1. **平稳分布存在**：无额外条件。每个闭沟通类 $C_k$ 对应唯一一个支撑在 $C_k$ 上的平稳分布 $\tilde\pi^{(k)}$，全体平稳分布为其凸组合，暂态上的平稳概率恒为 $0$。
2. **平稳分布唯一**：当且仅当闭沟通类恰好有一个（$m=1$）。若链不可约（$m=1$ 且 $T=\emptyset$），则唯一平稳分布满足 $\pi_i>0$（$\forall i\in E$）。
3. **Cesàro 平均与样本时间平均收敛**：当 $m=1$ 时，对任意初始分布 $\nu_0$ 有 $\frac1N\sum_{n=0}^{N-1}\nu_0 Q^n\to\pi$，且对任意 $f:E\to\mathbb R$ 有 $\frac1N\sum_{n=0}^{N-1}f(X_n)\xrightarrow{\text{a.s.}}\sum_{i=1}^K\pi_i f(i)$（无需非周期）。
4. **逐时刻分布收敛**：当 $m=1$ 且该唯一闭沟通类非周期时，$Q^n\to\mathbf 1\pi$，从而对任意初始分布 $\nu_0$ 有 $\nu_0 Q^n\to\pi$。
