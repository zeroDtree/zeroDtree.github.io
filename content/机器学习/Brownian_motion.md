---
title: Brownian Motion
---



The Wiener process $W_t$ is characterized by four facts:

- $W_0 = 0$
- $W_t$ is almost surely continuous
- $W_t$ has independent increments
- $W_t - W_s \sim \mathcal{N}(0, t-s)$ (for $0 \leq s \leq t$)

$\mathcal{N}(\mu, \sigma^2)$ denotes the normal distribution with expected value $\mu$ and variance $\sigma^2$. The condition that it has independent increments means that if $0 \leq s_1 < t_1 \leq s_2 < t_2$ then $W_{t_1} - W_{s_1}$ and $W_{t_2} - W_{s_2}$ are independent random variables. In addition, for some filtration $\mathcal{F}_t$, $W_t$ is $\mathcal{F}_t$-measurable for all $t \geq 0$.
