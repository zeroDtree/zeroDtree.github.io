---
title: holomorphic function
---

## 1. Complex Differentiable Function

Let $E$ be an subset in $\mathbb{C}$ and $f$ a complex-valued function on $X \subset \mathbb{C}$. The function $f$ is **complex differentiable** at the point $z_0$, where $z_0$ is a limit point of $E$, iff

$$
\lim_{z \to z_0, z \in E \setminus \{z_0\}} \frac{f(z) - f(z_0)}{z - z_0}  = L \in \mathbb{C}
$$

The limit is called the **derivative** of $f$ at $z_0$ and is denoted by $f'(z_0)$.

Other equivalent definitions:
(1)

$$
\lim_{h \to 0,h\not=0} \frac{f(z_0 + h) - f(z_0)}{h}  = L \in \mathbb{C}
$$

(2)

$$
\lim_{z \to z_0, z \in E \setminus \{z_0\}}  \frac{\|f(z) - (f(z_0) + L(z - z_0))\|}{\|z - z_0\|} = 0
$$

### 1.1. Rules of Arithmetic of complex differentiable functions

If $f$ and $g$ are complex differentiable in $\Omega$, then:

- $f + g$ is complex differentiable in $\Omega$ and $(f + g)' = f' + g'$.
- $fg$ is complex differentiable in $\Omega$ and $(fg)' = f'g + fg'$.
- If $g(z_0) \neq 0$, then $f/g$ is complex differentiable at $z_0$ and $(f/g)' = \frac{f'g - fg'}{g^2}.$

Moreover, if $f : \Omega \to U$ and $g : U \to \mathbb{C}$ are complex differentiable, the chain rule holds
$$(g \circ f)'(z) = g'(f(z))f'(z) \quad \text{for all } z \in \Omega.$$

> proof：for $f/g$ > $A(z) = f(z) - f(z_0) - f'(z_0)(z - z_0)$ > $B(z) = g(z) - g(z_0) - g'(z_0)(z - z_0)$
> Given that: $\frac{A(z)}{z-z_0} \to 0, \frac{B(z)}{z-z_0} \to 0$ as $z \to z_0$ (by definition)
> We can write the following ratio:
>
> $$
> \frac{f(z)}{g(z)} - (\frac{f(z_0)}{g(z_0)} + L (z - z_0)) = \frac{f(z)g(z_0) - f(z_0)g(z) - L(z - z_0)g(z)g(z_0)}{g(z)g(z_0)}
> $$
>
> $f(z) = f(z_0) + f'(z_0)(z - z_0) + A(z)$ and $g(z)$ = $g(z_0) + g'(z_0)(z - z_0) + B(z)$
> Substituting into the ratio, we get:
>
> $$
> \frac{(f'(z_0)g(z_0) - f(z_0)g'(z_0) - Lg(z)g(z_0))(z - z_0) + A(z)g(z_0) - f(z_0)B(z)}{g(z)g(z_0)}
> $$
>
> $L = \frac{f'(z_0)g(z_0) - f(z_0)g'(z_0)}{g(z_0)^2}$
> We have $(f'(z_0)g(z_0) - f(z_0)g'(z_0) = L g(z_0)^2)$
> Therefore
> the ratio is:
>
> $$
> \begin{aligned}
> \frac{(L g(z_0)^2 - L g(z)g(z_0))(z - z_0) + A(z)g(z_0) - f(z_0)B(z)}{g(z)g(z_0)}\\
> = \frac{(L g(z_0)(g(z_0) - g(z)))(z - z_0) + A(z)g(z_0) - f(z_0)B(z)}{g(z)g(z_0)}
> \end{aligned}
> $$
>
> It is easy to see that the numerator tends to 0 as $z \to z_0$ and the denominator tends to $g(z_0)^2$.

## 2. Holomorphic Function

A function is **holomorphic** on an **open set** $U$ if it is complex differentiable at every point of $U$. A function $f$ is holomorphic at a point $z_0$ if it is holomorphic on some neighbourhood of $z_0$. A function is holomorphic on some non-open set $A$ if it is holomorphic at every point of $A$.

if $f$ is holomorphic in all of $\mathbb{C}$ we say that $f$ is **entire**.

## 3. Properties

### 3.1. Cauchy-Riemann equations

Let $z,z_0 \in \Omega$, $z = x + iy$,$z_0 = x_0 + iy_0$,
if $f(x+iy) = u(x,y) + iv(x,y)$ be holomorphic in $\Omega$. Then

$$
\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}
$$

> proof:
>
> $$
> \begin{aligned}
> f(z)' &= \lim_{x=x_0,y \to y_0} \frac{f(x+iy) - f(x_0+iy_0)}{(x-x_0) + i(y-y_0)}\\
> &=\lim_{x=x_0,y \to y_0} \frac{u(x_0,y) + iv(x_0,y) - u(x_0,y_0) - iv(x_0,y_0)}{(x_0-x_0) + i(y-y_0)}\\
> &= \lim_{x=x_0,y \to y_0} \frac{u(x_0,y) - u(x_0,y_0)}{(x_0-x_0) + i(y-y_0)} + i \lim_{x=x_0,y \to y_0} \frac{v(x_0,y) - v(x_0,y_0)}{(x_0-x_0) + i(y-y_0)}\\
> &= \frac{1}{i}\frac{\partial u}{\partial y} + \frac{\partial v}{\partial y}\\
> &= -i \frac{\partial u}{\partial y} + \frac{\partial v}{\partial y}
> \end{aligned}
> $$
>
> similarly,
>
> $$
> \begin{aligned}
> f(z)' &= \lim_{y=y_0,x \to x_0} \frac{f(x+iy) - f(x_0+iy_0)}{(x-x_0) + i(y-y_0)}\\
> &= \frac{\partial u}{\partial x} + i \frac{\partial v}{\partial x}
> \end{aligned}
> $$
>
> Becuase The two limits above are both equal to $f'(z_0)$, we have
>
> $$
> \frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}
> $$

### 3.2. Derivative and Jacobian Properties of Holomorphic Functions

$$
\frac{\partial}{\partial z} = \frac{1}{2}\left(\frac{\partial}{\partial x} + \frac{1}{i}\frac{\partial}{\partial y}\right)
\quad \text{and} \quad
\frac{\partial}{\partial \bar{z}} = \frac{1}{2}\left(\frac{\partial}{\partial x} - \frac{1}{i}\frac{\partial}{\partial y}\right).
$$

If $f$ is holomorphic at $z_0$, then

$$
\frac{\partial f}{\partial \bar{z}}(z_0) = 0 \quad \text{and} \quad
f'(z_0) = \frac{\partial f}{\partial z}(z_0) = 2\frac{\partial u}{\partial z}(z_0).
$$

Also, if we write $F(x,y) = f(z)$, then $F$ is differentiable in the sense of real variables, and

$$
\det J_F(x_0, y_0) = |f'(z_0)|^2.
$$
