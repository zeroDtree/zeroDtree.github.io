---
title: 概率论-集中不等式
date: 2024-03-04 19:45:26
tags: 概率论
---

从维基百科和机器学习的书上整理、复制、粘贴了几个常见的集中不等式

- [Markov's inequality](#markovs-inequality)
  - [statement](#statement)
  - [intuition](#intuition)
  - [proof](#proof)
  - [corollaries](#corollaries)
- [Chebyshev's inequality](#chebyshevs-inequality)
  - [statement](#statement-1)
  - [proof](#proof-1)
- [Hoeffding's inequality](#hoeffdings-inequality)
  - [Hoeffding’s lemma](#hoeffdings-lemma)
    - [statement](#statement-2)
    - [Proof](#proof-2)
  - [proof](#proof-3)
- [McDiarmid’s inequality](#mcdiarmids-inequality)
  - [statement](#statement-3)
  - [Definition Martingale Difference](#definition-martingale-difference)
  - [Lemma](#lemma)
  - [Theorem Azuma's inequality](#theorem-azumas-inequality)
    - [proof](#proof-4)
  - [proof](#proof-5)

# Markov's inequality

## statement

If $X$ is a nonnegative random variable and $a>0$, then the probability that $X$ is at least $a$ is at most the expectation of $X$ divided by $a$

$$
\mathrm{P}(X \geq a) \leq \frac{\mathrm{E}(X)}{a}
$$

## intuition

$\mathrm{E}(X)=\mathrm{P}(X<a) \cdot \mathrm{E}(X \mid X < a)+\mathrm{P}(X \geq a) \cdot \mathrm{E}(X \mid X \geq a)$

$\mathrm{E}(X) \geq \mathrm{P}(X \geq a) \cdot \mathrm{E}(X \mid X \geq a) \geq a \cdot \mathrm{P}(X \geq a)$

$\mathrm{P}(X \geq a) \leq \frac{\mathrm{E}(X)}{a}$

## proof

For any event $E$, let $I_E$ be the indicator random variable of $E$, that is, $I_E=1$ if $E$ occurs and $I_E=0$ otherwise.
Using this notation, we have $I_{(X \geq a)}=1$ if the event $X \geq a$ occurs, and $I_{(X \geq a)}=0$ if $X<a$. Then, given $a>0$,

$$
a I_{(X \geq a)} \leq X
$$

which is clear if we consider the two possible values of $X \geq a$. If $X<a$, then $I_{(X \geq a)}=0$, and so $a I_{(X \geq a)}=0 \leq X$.
Otherwise, we have $X \geq a$, for which $I_{X \geq a}=1$ and so $a I_{X \geq a}=a \leq X$.
Since $\mathrm{E}$ is a monotonically increasing function, taking expectation of both sides of an inequality cannot reverse it. Therefore,

$$
\mathrm{E}\left(a I_{(X \geq a)}\right) \leq \mathrm{E}(X) .
$$

Now, using linearity of expectations, the left side of this inequality is the same as

$$
a \mathrm{E}\left(I_{(X \geq a)}\right)=a(1 \cdot \mathrm{P}(X \geq a)+0 \cdot \mathrm{P}(X<a))=a \mathrm{P}(X \geq a) .
$$

Thus we have

$$
a \mathrm{P}(X \geq a) \leq \mathrm{E}(X)
$$

and since $a>0$, we can divide both sides by $a$.

## corollaries

$\phi$ is a nondecreasing nonnegative fundction

$$
\mathrm{P}(|X| \geq a)=\mathrm{P}(\varphi(|X|) \geq \varphi(a)) \stackrel{\mathrm{MI}}{\leq} \frac{\mathrm{E}(\varphi(|X|))}{\varphi(a)}
$$

# Chebyshev's inequality

## statement

$$
\mathrm{P}(|X-\mathrm{E}(X)| \geq a) \leq \frac{\operatorname{Var}(X)}{a^2},
$$

## proof

for any $a>0$

$$
\operatorname{Var}(X)=\mathrm{E}\left[(X-\mathrm{E}(X))^2\right] .
$$

because Markov's inequality

$$
\mathrm{P}\left((X-\mathrm{E}(X))^2 \geq a^2\right) \leq \frac{\operatorname{Var}(X)}{a^2} .
$$

This argument can be summarized (where "MI" indicates use of Markov's inequality):

$$
\mathrm{P}(|X-\mathrm{E}(X)| \geq a)=\mathrm{P}\left((X-\mathrm{E}(X))^2 \geq a^2\right) \stackrel{\mathrm{MI}}{\leq} \frac{\mathrm{E}\left((X-\mathrm{E}(X))^2\right)}{a^2}=\frac{\operatorname{Var}(X)}{a^2} .
$$

# Hoeffding's inequality

Let $X_1, \ldots, X_m$ be independent random variables with $X_i$ taking values in $\left[a_i, b_i\right]$ for all $i \in[1, m]$. Then for any $\epsilon>0$, the following inequalities hold for $S_m=\sum_{i=1}^m X_i$ :

$$
\begin{gathered}
\operatorname{Pr}\left[S_m-\mathrm{E}\left[S_m\right] \geq \epsilon\right] \leq e^{-2 \epsilon^2 / \sum_{i=1}^m\left(b_i-a_i\right)^2} \\
\operatorname{Pr}\left[S_m-\mathrm{E}\left[S_m\right] \leq-\epsilon\right] \leq e^{-2 \epsilon^2 / \sum_{i=1}^m\left(b_i-a_i\right)^2} .
\end{gathered}
$$

## Hoeffding’s lemma

### statement

Let $X$ be a random variable with $E[X]=0$ and $a \leq X \leq b$ with $b>a$. Then, for any $t>0$, the following inequality holds:

$$
\mathrm{E}\left[e^{t X}\right] \leq e^{\frac{t^2(b-a)^2}{8}} .
$$

### Proof

By the convexity of $x \mapsto e^x$, for all $x \in[a, b]$, the following holds:

$$
e^{t x} \leq \frac{b-x}{b-a} e^{t a}+\frac{x-a}{b-a} e^{t b} .
$$

Thus, using $\mathrm{E}[X]=0$,

$$
\mathrm{E}\left[e^{t X}\right] \leq \mathrm{E}\left[\frac{b-X}{b-a} e^{t a}+\frac{X-a}{b-a} e^{t b}\right]=\frac{b}{b-a} e^{t a}+\frac{-a}{b-a} e^{t b}=e^{\phi(t)},
$$

where,

$$
\phi(t)=\log \left(\frac{b}{b-a} e^{t a}+\frac{-a}{b-a} e^{t b}\right)=t a+\log \left(\frac{b}{b-a}+\frac{-a}{b-a} e^{t(b-a)}\right) .
$$

For any $t>0$, the first and second derivative of $\phi$ are given below:

$$
\begin{aligned}
\phi^{\prime}(t) & =a-\frac{a e^{t(b-a)}}{\frac{b}{b-a}-\frac{a}{b-a} e^{t(b-a)}}=a-\frac{a}{\frac{b}{b-a} e^{-t(b-a)}-\frac{a}{b-a}}, \\
\phi^{\prime \prime}(t) & =\frac{-a b e^{-t(b-a)}}{\left[\frac{b}{b-a} e^{-t(b-a)}-\frac{a}{b-a}\right]^2} \\
& =\frac{\alpha(1-\alpha) e^{-t(b-a)}(b-a)^2}{\left[(1-\alpha) e^{-t(b-a)}+\alpha\right]^2} \\
& =\frac{\alpha}{\left[(1-\alpha) e^{-t(b-a)}+\alpha\right]} \frac{(1-\alpha) e^{-t(b-a)}}{\left[(1-\alpha) e^{-t(b-a)}+\alpha\right]}(b-a)^2 .
\end{aligned}
$$

where $\alpha$ denotes $\frac{-a}{b-a}$. Note that $\phi(0)=\phi^{\prime}(0)=0$ and that $\phi^{\prime \prime}(t)=u(1-u)(b-a)^2$ where $u=\frac{\alpha}{\left[(1-\alpha) e^{-t(b-a)}+\alpha\right]}$. Since $u$ is in $[0,1], u(1-u)$ is upper bounded by $1 / 4$ and $\phi^{\prime}(t) \leq \frac{(b-a)^2}{4}$. Thus, by the second order expansion of function $\phi$, there exists $\theta \in[0, t]$ such that:

$$
\phi(t)=\phi(0)+t \phi^{\prime}(0)+\frac{t^2}{2} \phi^{\prime \prime}(\theta) \leq t^2 \frac{(b-a)^2}{8},
$$

## proof

$\begin{aligned} \operatorname{Pr}\left[S_m-\mathrm{E}\left[S_m\right] \geq \epsilon\right] & \leq e^{-t \epsilon} \mathrm{E}\left[e^{t\left(S_m-\mathrm{E}\left[S_m\right]\right)}\right] \\ & =\Pi_{i=1}^m e^{-t \epsilon} \mathrm{E}\left[e^{t\left(X_i-\mathrm{E}\left[X_i\right]\right)}\right] \\ & \leq \Pi_{i=1}^m e^{-t \epsilon} e^{t^2\left(b_i-a_i\right)^2 / 8} \\ & =e^{-t \epsilon} e^{t^2 \sum_{i=1}^m\left(b_i-a_i\right)^2 / 8} \\ & \leq e^{-2 \epsilon^2 / \sum_{i=1}^m\left(b_i-a_i\right)^2},\end{aligned}$

# McDiarmid’s inequality

## statement

Let $X_1, \ldots, X_m \in \mathcal{X}^m$ be a set of $m \geq 1$ independent random variables and assume that there exist $c_1, \ldots, c_m>0$ such that $f: \mathcal{X}^m \rightarrow \mathbb{R}$ satisfies the following conditions:

$$
\left|f\left(x_1, \ldots, x_i, \ldots, x_m\right)-f\left(x_1, \ldots, x_i^{\prime}, \ldots x_m\right)\right| \leq c_i,
$$

for all $i \in[1, m]$ and any points $x_1, \ldots, x_m, x_i^{\prime} \in \mathcal{X}$. Let $f(S)$ denote $f\left(X_1, \ldots, X_m\right)$, then, for all $\epsilon>0$, the following inequalities hold:

$$
\begin{gathered}
\operatorname{Pr}[f(S)-\mathrm{E}[f(S)] \geq \epsilon] \leq \exp \left(\frac{-2 \epsilon^2}{\sum_{i=1}^m c_i^2}\right) \\
\operatorname{Pr}[f(S)-\mathrm{E}[f(S)] \leq-\epsilon] \leq \exp \left(\frac{-2 \epsilon^2}{\sum_{i=1}^m c_i^2}\right) .
\end{gathered}
$$

## Definition Martingale Difference

A sequence of random variables $V_1, V_2, \ldots$ is a martingale difference sequence with respect to $X_1, X_2, \ldots$ if for all $i>0, V_i$ is a function of $X_1, \ldots, X_i$ and

$$
\mathrm{E}\left[V_{i+1} \mid X_1, \ldots, X_i\right]=0 .
$$

## Lemma

Let $V$ and $Z$ be random variables satisfying $\mathrm{E}[V \mid Z]=0$ and, for some function $f$ and constant $c \geq 0$, the inequalities:

$$
f(Z) \leq V \leq f(Z)+c .
$$

Then, for all $t>0$, the following upper bound holds:

$$
\mathrm{E}\left[e^{t V} \mid Z\right] \leq e^{t^2 c^2 / 8} .
$$

## Theorem Azuma's inequality

Let $V_1, V_2, \ldots$ be a martingale difference sequence with respect to the random variables $X_1, X_2, \ldots$, and assume that for all $i>0$ there is a constant $c_i \geq 0$ and
random variable $Z_i$, which is a function of $X_1, \ldots, X_{i-1}$, that satisfy

$$
Z_i \leq V_i \leq Z_i+c_i .
$$

Then, for all $\epsilon>0$ and $m$, the following inequalities hold:

$$
\begin{gathered}
\operatorname{Pr}\left[\sum_{i=1}^m V_i \geq \epsilon\right] \leq \exp \left(\frac{-2 \epsilon^2}{\sum_{i=1}^m c_i^2}\right) \\
\operatorname{Pr}\left[\sum_{i=1}^m V_i \leq-\epsilon\right] \leq \exp \left(\frac{-2 \epsilon^2}{\sum_{i=1}^m c_i^2}\right) .
\end{gathered}
$$

### proof

Proof For any $k \in[1, m]$, let $S_k=\sum_{i=1}^k V_k$. Then, using Chernoff's bounding technique, for any $t>0$, we can write

$$
\begin{aligned}
\operatorname{Pr}\left[S_m \geq \epsilon\right] & \leq e^{-t \epsilon} \mathrm{E}\left[e^{t S_m}\right] \\
& =e^{-t \epsilon} \mathrm{E}\left[e^{t S_{m-1}} \mathrm{E}\left[e^{t \mathbf{V}_m} \mid X_1, \ldots, X_{m-1}\right]\right] \\
& \leq e^{-t \epsilon} \mathrm{E}\left[e^{t S_{m-1}}\right] e^{t^2 c_m^2 / 8} \\
& \leq e^{-t \epsilon} e^{t^2 \sum_{i=1}^m c_i^2 / 8} \\
& =e^{-2 \epsilon^2 / \sum_{i=1}^m c_i^2}
\end{aligned}
$$

where we chose $t=4 \epsilon / \sum_{i=1}^m c_i^2$ to minimize the upper bound. This proves the first statement of the theorem, and the second statement is shown in a similar way.
($if\ F1\subset F2,\ then\ E[E[Y|F1]|F2] = E[E[Y|F2]|F1] = E[Y|F1]$)

## proof

Define a sequence of random variables $V_k, k \in[1, m]$, as follows: $V=f(S)-\mathrm{E}[f(S)], V_1=\mathrm{E}\left[V \mid X_1\right]-\mathrm{E}[V]$, and for $k>1$,

$$
V_k=\mathrm{E}\left[V \mid X_1, \ldots, X_k\right]-\mathrm{E}\left[V \mid X_1, \ldots, X_{k-1}\right] .
$$

Note that $V=\sum_{k=1}^m V_k$. Furthermore, the random variable $\mathrm{E}\left[V \mid X_1, \ldots, X_k\right]$ is a function of $X_1, \ldots, X_k$. Conditioning on $X_1, \ldots, X_{k-1}$ and taking its expectation is therefore:

$$
\mathrm{E}\left[\mathrm{E}\left[V \mid X_1, \ldots, X_k\right] \mid X_1, \ldots, X_{k-1}\right]=\mathrm{E}\left[V \mid X_1, \ldots, X_{k-1}\right],
$$

which implies $\mathrm{E}\left[V_k \mid X_1, \ldots, X_{k-1}\right]=0$. Thus, the sequence $\left(V_k\right)_{k \in[1, m]}$ is a martingale difference sequence. Next, observe that, since $\mathrm{E}[f(S)]$ is a scalar, $V_k$ can be expressed as follows:

$$
V_k=\mathrm{E}\left[f(S) \mid X_1, \ldots, X_k\right]-\mathrm{E}\left[f(S) \mid X_1, \ldots, X_{k-1}\right] .
$$

Now define the random variables for each $i$

$$
\begin{aligned}
U_i & :=\sup _{x \in \mathcal{X}_i} \mathbb{E}\left[f\left(X_{1 \rightharpoondown(i-1)}, x, X_{(i+1) \rightharpoondown n}\right) \mid X_{1 \rightharpoondown(i-1)}, X_i=x\right]-\left[f\left(X_{1 \rightharpoondown(i-1)}, X_{i \rightharpoondown n}\right) \mid X_{1 \rightharpoondown(i-1)}\right], \\
L_i & :=\inf _{x \in \mathcal{X}_i} \mathbb{E}\left[f\left(X_{1 \rightharpoondown(i-1)}, x, X_{(i+1) \rightharpoondown n}\right) \mid X_{1 \rightharpoondown(i-1)}, X_i=x\right]-\left[f\left(X_{1 \rightharpoondown(i-1)}, X_{i \rightharpoondown n}\right) \mid X_{1 \rightharpoondown(i-1)}\right] .
\end{aligned}
$$

Since $X_i, \ldots, X_n$ are independent of each other, conditioning on $X_i=x$ does not affect the probabilities of the other variables, so these are equal to the expressions

$$
\begin{aligned}
U_i & =\sup _{x \in \mathcal{X}_i} \mathbb{E}\left[f\left(X_{1 \rightarrow(i-1)}, x, X_{(i+1) \rightharpoondown n}\right)-f\left(X_{1 \rightharpoondown(i-1)}, X_{i \rightarrow n}\right) \mid X_{1 \rightarrow(i-1)}\right], \\
L_i & =\inf _{x \in \mathcal{X}_i} \mathbb{E}\left[f\left(X_{1 \rightarrow(i-1)}, x, X_{(i+1) \rightharpoondown n}\right)-f\left(X_{1 \rightarrow(i-1)}, X_{i \rightharpoondown n}\right) \mid X_{1 \rightarrow(i-1)}\right] .
\end{aligned}
$$

$$
\begin{aligned}
U_i-L_i & =\sup _{u \in \mathcal{X}_i, \ell \in \mathcal{X}_i} \mathbb{E}\left[f\left(X_{1 \rightharpoondown(i-1)}, u, X_{(i+1) \rightharpoondown n}\right) \mid X_{1 \rightharpoondown(i-1)}\right]-\mathbb{E}\left[f\left(X_{1 \rightharpoondown(i-1)}, \ell, X_{(i+1) \rightharpoondown n}\right) \mid X_{1 \rightharpoondown(i-1)}\right] \\
& =\sup _{u \in \mathcal{X}_i, \ell \in \mathcal{X}_i} \mathbb{E}\left[f\left(X_{1 \rightarrow(i-1)}, u, X_{(i+1) \rightharpoondown n}\right)-f\left(X_{1 \rightarrow(i-1)}, l, X_{(i+1) \rightharpoondown n}\right) \mid X_{1 \rightharpoondown(i-1)}\right] \\
& \leq \sup _{x_u \in \mathcal{X}_i, x_l \in \mathcal{X}_i} \mathbb{E}\left[c_i \mid X_{1 \rightharpoondown(i-1)}\right] \\
& \leq c_i
\end{aligned}
$$

$L_i$ is a random variables about $X_1,X2,...,X_{i-1}$
thus, $L_k \leq V_k \leq L_k+c_k$. In view of these inequalities, we can apply Azuma's inequality to $V=\sum_{k=1}^m V_k$
