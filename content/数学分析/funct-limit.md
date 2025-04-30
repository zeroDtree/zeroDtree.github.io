## Definition of convergence of functions at a point

**Convergence of functions at a point**: Let $X$ be a subset of $\mathbb{R}^n$, let $f: X \rightarrow \mathbb{R}^m$ be a function, let $E$ be a subset of $X$, $x_0$ be an adherent point of $E$, and let $L \in \mathbb{R}^m$. We say that $f$ $\textit{converges to}$ $L$ $\textit{at}$ $x_0$ $\textit{in}$ $E$ and write

$$
\lim_{x \to x_0, x \in E} f(x) = L,
$$

**iff** $\forall \epsilon > 0, \exists \delta > 0$, s.t. (($\forall x \in E \wedge d(x_0, x) < \delta$) $\longrightarrow$ $d(f(x), L) < \epsilon$) is true.

### Equivalent definition

The following statements are equivalent:

1. $f$ converges to $L$ at $x_0$ in $E$.
2. For every sequence $(a_n)_{n=0}^{\infty}$ which consists entirely of elements of $E$ and converges to $x_0$, the sequence $(f(a_n))_{n=0}^{\infty}$ converges to $L$.

> proof:
> (1) $\longrightarrow$ (2):
> (1) $\Longleftrightarrow$ $\forall \epsilon > 0, \exists \delta > 0$, s.t. (($\forall x \in E \wedge d(x_0, x) < \delta$) $\longrightarrow$ $d(f(x), L) < \epsilon$) is true.
> $(a_n \to x_0) \Longleftrightarrow \forall \delta > 0, \exists N \in \mathbb{Z}_{\geq 0}$, s.t. $\forall n \geq N, d(a_n, x_0) < \delta$
> Then, $\forall \epsilon > 0, \exists N \in \mathbb{Z}_{\geq 0}$, s.t. $\forall n \geq N, d(f(a_n), L) < \epsilon$
> so, $(f(a_n))_{n=0}^{\infty}$ converges to $L$.
> (2) $\longrightarrow$ (1):
> Suppose $f$ does not converge to $L$ at $x_0$ in $E$.
> It means that $\exists \epsilon > 0,\forall \delta > 0,\exists x \in E\wedge d(x_0, x) < \delta \text{ s.t. } d(f(x), L) \geq \epsilon$
> Choose $\delta = \frac{1}{n+1}, n \in \mathbb{Z}_{\geq 0}$
> Then, $\exists x_n \in E, d(x_0, x_n) < \frac{1}{n+1}, d(f(x_n), L) \geq \epsilon$
> so, $(x_n)_{n=0}^{\infty}$ is a sequence which consists entirely of elements of $E$ and converges to $x_0$, but $(f(x_n))_{n=0}^{\infty}$ does not converge to $L$.
> This is a contradiction.
> Therefore, $f$ converges to $L$ at $x_0$ in $E$.

## For n=1

We can get the law of limit of functions in one variable from the law of limit of sequences.

$$
\begin{align*}
\lim_{x \to x_0} (f \pm g)(x) &= \lim_{x \to x_0} f(x) \pm \lim_{x \to x_0} g(x)\\
\lim_{x \to x_0} \max(f, g)(x) &= \max\left(\lim_{x \to x_0} f(x), \lim_{x \to x_0} g(x)\right)\\
\lim_{x \to x_0} \min(f, g)(x) &= \min\left(\lim_{x \to x_0} f(x), \lim_{x \to x_0} g(x)\right)\\
\lim_{x \to x_0} (fg)(x) &= \lim_{x \to x_0} f(x) \lim_{x \to x_0} g(x)\\
\lim_{x \to x_0} (f/g)(x) &= \frac{\lim_{x \to x_0} f(x)}{\lim_{x \to x_0} g(x)}
\end{align*}
$$

where we have dropped the restriction $x \in E$ for brevity

## For n>1

$\bold{x} = (x_1, x_2, \cdots, x_n)^T \in \mathbb{R}^n$

$\bold{x}^n \to \bold{y}$ means that $\forall \epsilon > 0, \exists N \in \mathbb{Z}_{\geq 0}$, s.t. $\forall n \geq N, d(\bold{x}^n, \bold{y}) < \epsilon$

The following statements are equivalent:

1. $\bold{x^n} \to \bold{y}$
2. $\forall i \in \{1, 2, \cdots, n\}, (x_i^n)_{n=0}^{\infty} \to y_i$

> proof:
> (1) $\longrightarrow$ (2):
> $\bold{x}^n \to \bold{y}$ means that $\forall \epsilon > 0, \exists N \in \mathbb{Z}_{\geq 0}$, s.t. $\forall n \geq N, \sqrt{\sum_{i=1}^{n} (x_i^n - y_i)^2} < \epsilon$
> so, $\forall i \in \{1, 2, \cdots, n\}, \exists N_i \in \mathbb{Z}_{\geq 0}$, s.t. $\forall n \geq N_i, |x_i^n - y_i| \leq \sqrt{\sum_{i=1}^{n} (x_i^n - y_i)^2} < \epsilon$
> (2) $\longrightarrow$ (1):
> $(x_i^n)_{n=0}^{\infty} \to y_i$ means that $\forall \epsilon > 0, \exists N_i \in \mathbb{Z}_{\geq 0}$, s.t. $\forall n \geq N_i, |x_i^n - y_i| < \epsilon/n$
> Let $N = \max\{N_1, N_2, \cdots, N_n\}$
> Then, $\forall n \geq N, \sqrt{\sum_{i=1}^{n} (x_i^n - y_i)^2} \leq \sum_{i=1}^{n} |x_i^n - y_i| < n (\epsilon/n) = \epsilon$
> so, $\bold{x}^n \to \bold{y}$

Let $f: X \to \mathbb{R}^m, X \subseteq \mathbb{R}^n, f(\bold{x}) = (f_1(\bold{x}), f_2(\bold{x}), \cdots, f_m(\bold{x}))^T$

From above, we can easily get that

$\lim_{\bold{x} \to \bold{x}_0} f(\bold{x}) = (\lim_{\bold{x} \to \bold{x}_0} f_1(\bold{x}), \lim_{\bold{x} \to \bold{x}_0} f_2(\bold{x}), \cdots, \lim_{\bold{x} \to \bold{x}_0} f_m(\bold{x}))^T$

Let $X \subseteq \mathbb{R}^n$, $f,g: X \to \mathbb{R}^m$

We can get the law of limit of functions in multi-variables from the law of limit of one variable.

$$
\begin{align*}
\lim_{\bold{x} \to \bold{x}_0} (f \pm g)(\bold{x}) &= \lim_{\bold{x} \to \bold{x}_0} f(\bold{x}) \pm \lim_{\bold{x} \to \bold{x}_0} g(\bold{x})\\
\lim_{\bold{x} \to \bold{x}_0} (fg)(\bold{x}) &= \lim_{\bold{x} \to \bold{x}_0} f(\bold{x}) \lim_{\bold{x} \to \bold{x}_0} g(\bold{x})\\
\lim_{\bold{x} \to \bold{x}_0} (f/g)(\bold{x}) &= \frac{\lim_{\bold{x} \to \bold{x}_0} f(\bold{x})}{\lim_{\bold{x} \to \bold{x}_0} g(\bold{x})}
\end{align*}
$$

where multiplication and division are component-wise.
