---
title: Homogeneous linear differential equation of order n with constant coefficients
---

## Homogeneous linear differential equation of order n with constant coefficients

$$
\frac{d^n y}{dt^n} + a_{n-1} \frac{d^{n-1} y}{dt^{n-1}} + \cdots + a_1 \frac{dy}{dt} + a_0 y = 0
$$

Because the operator is linear mapping, the solution space is a vector space

suppose $e^{\lambda t}$ is a solution, then

$$
\begin{aligned}
\frac{d^n}{dt^n} e^{\lambda t} + a_{n-1} \frac{d^{n-1}}{dt^{n-1}} e^{\lambda t} + \cdots + a_1 \frac{d}{dt} e^{\lambda t} + a_0 e^{\lambda t} &= 0 \\
\left( \frac{d^n}{dt^n} + a_{n-1} \frac{d^{n-1}}{dt^{n-1}} + \cdots + a_1 \frac{d}{dt} + a_0 \right) e^{\lambda t} &= 0 \\
\lambda^n e^{\lambda t} + a_{n-1} \lambda^{n-1} e^{\lambda t} + \cdots + a_1 \lambda e^{\lambda t} + a_0 e^{\lambda t} &= 0 \\
\left( \lambda^n + a_{n-1} \lambda^{n-1} + \cdots + a_1 \lambda + a_0 \right) e^{\lambda t} &= 0 \\
\left( \lambda^n + a_{n-1} \lambda^{n-1} + \cdots + a_1 \lambda + a_0 \right) &= 0 \\
\end{aligned}
$$

the characteristic equation is

$$
p(\lambda) = \lambda^n + a_{n-1} \lambda^{n-1} + \cdots + a_1 \lambda + a_0 = 0
$$

there must be $m$ distinct roots, $\lambda_1, \lambda_2, \cdots, \lambda_m$, the multiplicity of the root is $k_1, k_2, \cdots, k_m$

the root $\lambda_i$ has multiplicity $k_i$, then the solution is

$$
y = \sum_{i=1}^m \sum_{j=0}^{k_i-1} c_{ij} t^j e^{\lambda_i t}
$$
