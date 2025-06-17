## Definition of convergence of functions at a point

**Convergence of functions at a point**: Let $X$ be a subset of $\mathbb{C}^n$, let $f: X \rightarrow \mathbb{C}^m$ be a function, let $E$ be a subset of $X$, $x_0$ be an adherent point of $E$, and let $L \in \mathbb{C}^m$. We say that $f$ $\textit{converges to}$ $L$ $\textit{at}$ $x_0$ $\textit{in}$ $E$ and write

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
> $(a_n \to x_0) \Longleftrightarrow \forall \delta > 0, \exists N \in \mathbb{Z}_{\geq 0}$, s.t. $\forall n \geq N, d(a_n, x_0) < \delta$.
> Then, $\forall \epsilon > 0, \exists N \in \mathbb{Z}_{\geq 0}$, s.t. $\forall n \geq N, d(f(a_n), L) < \epsilon$.
> so, $(f(a_n))_{n=0}^{\infty}$ converges to $L$.
> (2) $\longrightarrow$ (1):
> Suppose $f$ does not converge to $L$ at $x_0$ in $E$.
> It means that $\exists \epsilon > 0,\forall \delta > 0,\exists x \in E\wedge d(x_0, x) < \delta \text{ s.t. } d(f(x), L) \geq \epsilon$.
> Choose $\delta = \frac{1}{n+1}, n \in \mathbb{Z}_{\geq 0}$.
> Then, $\exists x_n \in E, d(x_0, x_n) < \frac{1}{n+1}, d(f(x_n), L) \geq \epsilon$.
> so, $(x_n)_{n=0}^{\infty}$ is a sequence which consists entirely of elements of $E$ and converges to $x_0$, but $(f(x_n))_{n=0}^{\infty}$ does not converge to $L$.
> This is a contradiction.
> Therefore, $f$ converges to $L$ at $x_0$ in $E$.

## For n=1

We can get the law of limit of functions in one variable from the law of limit of sequences.

$$
\begin{align*}
\lim_{x \to x_0} (f \pm g)(x) &= \lim_{x \to x_0} f(x) \pm \lim_{x \to x_0} g(x)\\
\lim_{x \to x_0} (fg)(x) &= \lim_{x \to x_0} f(x) \lim_{x \to x_0} g(x)\\
\lim_{x \to x_0} (f/g)(x) &= \frac{\lim_{x \to x_0} f(x)}{\lim_{x \to x_0} g(x)}
\end{align*}
$$

where we have dropped the restriction $x \in E$ for brevity

## For n>1

$\mathbf{x} = (x_1, x_2, \cdots, x_n)^T \in \mathbb{C}^n$

$\mathbf{x}^n \to \mathbf{y}$ means that $\forall \epsilon > 0, \exists N \in \mathbb{Z}_{\geq 0}$, s.t. $\forall n \geq N, d(\mathbf{x}^n, \mathbf{y}) < \epsilon$

The following statements are equivalent:

1. $\mathbf{x^n} \to \mathbf{y}$
2. $\forall i \in \{1, 2, \cdots, n\}, (x_i^n)_{n=0}^{\infty} \to y_i$

> proof:
> (1) $\longrightarrow$ (2):
> $\mathbf{x}^n \to \mathbf{y}$ means that $\forall \epsilon > 0, \exists N \in \mathbb{Z}_{\geq 0}$, s.t. $\forall n \geq N, \sqrt{\sum_{i=1}^{n} d(x_i^n,y_i)^2} < \epsilon$
> so, $\forall i \in \{1, 2, \cdots, n\}, \exists N_i \in \mathbb{Z}_{\geq 0}$, s.t. $\forall n \geq N_i, d(x_i^n,y_i) \leq \sqrt{\sum_{i=1}^{n} d(x_i^n, y_i)^2} < \epsilon$
> (2) $\longrightarrow$ (1):
> $(x_i^n)_{n=0}^{\infty} \to y_i$ means that $\forall \epsilon > 0, \exists N_i \in \mathbb{Z}_{\geq 0}$, s.t. $\forall n \geq N_i, d(x_i^n, y_i) < \epsilon/n$
> Let $N = \max\{N_1, N_2, \cdots, N_n\}$
> Then, $\forall n \geq N, \sqrt{\sum_{i=1}^{n} d(x_i^n, y_i)^2} \leq \sum_{i=1}^{n} d(x_i^n, y_i) < n (\epsilon/n) = \epsilon$
> so, $\mathbf{x}^n \to \mathbf{y}$

Let $f: X \to \mathbb{C}^m, X \subseteq \mathbb{C}^n, f(\mathbf{x}) = (f_1(\mathbf{x}), f_2(\mathbf{x}), \cdots, f_m(\mathbf{x}))^T$

From above, we can easily get that

$\lim_{\mathbf{x} \to \mathbf{x}_0} f(\mathbf{x}) = (\lim_{\mathbf{x} \to \mathbf{x}_0} f_1(\mathbf{x}), \lim_{\mathbf{x} \to \mathbf{x}_0} f_2(\mathbf{x}), \cdots, \lim_{\mathbf{x} \to \mathbf{x}_0} f_m(\mathbf{x}))^T$

Let $X \subseteq \mathbb{C}^n$, $f,g: X \to \mathbb{C}^m$

We can get the law of limit of functions in multi-variables from the law of limit of one variable.

$$
\begin{align*}
\lim_{\mathbf{x} \to \mathbf{x}_0} (f \pm g)(\mathbf{x}) &= \lim_{\mathbf{x} \to \mathbf{x}_0} f(\mathbf{x}) \pm \lim_{\mathbf{x} \to \mathbf{x}_0} g(\mathbf{x})\\
\lim_{\mathbf{x} \to \mathbf{x}_0} (fg)(\mathbf{x}) &= \lim_{\mathbf{x} \to \mathbf{x}_0} f(\mathbf{x}) \lim_{\mathbf{x} \to \mathbf{x}_0} g(\mathbf{x})\\
\lim_{\mathbf{x} \to \mathbf{x}_0} (f/g)(\mathbf{x}) &= \frac{\lim_{\mathbf{x} \to \mathbf{x}_0} f(\mathbf{x})}{\lim_{\mathbf{x} \to \mathbf{x}_0} g(\mathbf{x})}
\end{align*}
$$

where multiplication and division are component-wise.
