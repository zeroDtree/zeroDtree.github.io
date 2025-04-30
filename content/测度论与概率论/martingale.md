---
title: martingale
---

## Definition

- Probability space: a triple $(\Omega, \Sigma, \mathbb{P})$, where $\Omega$ is a set, $\Sigma$ is a sigma-algebra on $\Omega$, and $\mathbb{P}$ is a probability measure on $\Sigma$.

- Stochastic process: a collection of random variables indexed by a set, usually denoted as $\{X_t: t \in T\}$ or $\{X(t): t \in T\}$
  In stochastic process, $T$ often is a total ordered index set (e.g. $\mathbb{N}, \mathbb{Z}, \mathbb{R}$)

- Banach space: a complete normed vector space.

- Filtration: Let $(\Omega, \Sigma, \mathbb{P})$ be a probability space, $I$ be a total ordered index set, $\mathbb{F}=\{\Sigma_i : i \in I \wedge \Sigma_i \text{ is a sub-sigma-algebra of } \Sigma\}$, We say $\mathbb{F}$ is a filtration if $\Sigma_i \subseteq \Sigma_j$ for all $i < j$. $(\Omega, \Sigma, \mathbb{P}, \mathbb{F})$ is called a filtered probability space.

- Adapted to the filtration: Let $(\Omega, \Sigma, \mathbb{P})$ be a probability space, $T$ be a total ordered index set, $\mathbb{F}=\{\Sigma_i: i\in T\}$ be a filtration of $\Sigma$, a stochastic process $X: T \times \Omega \rightarrow S$ is called adapted to the filtration $\mathbb{F}$ if for each $t \in T$, $X_t$ is a $\Sigma_t$-measurable function.

### Martingale

In full generality, a stochastic process $Y: T \times \Omega \rightarrow S$ taking values in a Banach space $S$ with norm $\|\cdot\|_S$ is a **martingale** with respect to a filtration $\Sigma_*$ and probability measure $\mathbb{P}$ if

- $\Sigma_*$ is a filtration of the underlying probability space $(\Omega, \Sigma, \mathbb{P})$;
- $Y$ is adapted to the filtration $\Sigma_*$, i.e., for each $t$ in the index set $T$, the random variable $Y_t$ is a $\Sigma_t$-measurable function;
- for each $t$, $Y_t$ lies in the $L^p$ space $L^1(\Omega, \Sigma_t, \mathbb{P}; S)$, i.e.
  $$
      \mathbb{E}_{\mathbb{P}}(\|Y_t\|_S) < +\infty;
  $$
- for all $s$ and $t$ with $s < t$ and all $F \in \Sigma_s$,

  $$
      \mathbb{E}_{\mathbb{P}}\left([Y_t - Y_s] \chi_F\right) = 0,
  $$

  where $\chi_F$ denotes the indicator function of the event $F$.
  In Grimmett and Stirzaker's _Probability and Random Processes_, this last condition is denoted as

  $$
  Y_s = \mathbb{E}_{\mathbb{P}}(Y_t \mid \Sigma_s),
  $$

  which is a general form of conditional expectation.
