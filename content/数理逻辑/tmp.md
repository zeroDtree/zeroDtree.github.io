\begin{proposition}[3.23]
Let $\varphi(x)$ be a wff.\ of $\mathcal L$ in which $x_i$ appears free, and let $t$ be a term which is free for $x_i$ in $\varphi(x_i)$. Suppose that $v$ is a valuation and $v'$ is the valuation which is $i$-equivalent to $v$ and has $v'(x_i)=v(t)$. Then $v$ satisfies $\varphi(t)$ if and only if $v'$ satisfies $\varphi(x_i)$.
\end{proposition}

\begin{proof}
First observe that for any term $u$ in which $x_i$ occurs we can obtain a term $u'$ by substituting $t$ for $x_i$ throughout, and that then $v(u')=v'(u)$. We prove this by induction on the length of $u$ (i.e.\ the number of symbols in $u$).

\paragraph{Base step} $u$ is $x_i$, so $u'$ is $t$. Then
\[
v(u')=v(t)=v'(x_i)=v'(u).
\]

\paragraph{Induction step} $u$ is $f(u_1,\dots,u_n)$, where $u_1,\dots,u_n$ are terms with smaller length. Let $u_1',\dots,u_n'$ be obtained by substituting $t$ for $x_i$ throughout. Then $u'=f(u_1',\dots,u_n')$. So
\begin{align*}
v(u') &= f^{\mathcal M}\bigl(v(u_1'),\dots,v(u_n')\bigr)\\
      &= f^{\mathcal M}\bigl(v'(u_1),\dots,v'(u_n)\bigr),
      \quad\text{by the induction hypothesis,}\\
      &= v'(u).
\end{align*}
Thus $v(u')=v'(u)$ has been established, for every term $u$ of $\mathcal L$.

We prove the proposition now by induction on the length of the wff.\ $\varphi(x_i)$, i.e.\ the number of connectives and quantifiers in $\varphi(x_i)$.

\paragraph{Base step} $\varphi(x_i)$ is an atomic formula, say $A_j(u_1,\dots,u_n)$ where $u_1,\dots,u_n$ are terms in $\mathcal L$. Suppose that $v'$ satisfies $\varphi(x_i)$. Then
\[
A_j^{\mathcal M}\bigl(v'(u_1),\dots,v'(u_n)\bigr)
\]
holds in the interpretation, so
\[
A_j^{\mathcal M}\bigl(v(u_1'),\dots,v(u_n')\bigr)
\]
holds in the interpretation, where $u_1',\dots,u_n'$ are obtained as above by substituting $t$ for $x_i$ throughout. (Here we use the preliminary result above.) We now have that $v$ satisfies the wff.\ $A_j(u_1',\dots,u_n')$, i.e.\ $v$ satisfies $\varphi(t)$. The converse can be demonstrated by retracing this argument.

\paragraph{Induction step}
\begin{itemize}
  \item[\textbf{Case 1.}] $\varphi(x_i)$ is $\neg B(x_i)$.

  \item[\textbf{Case 2.}] $\varphi(x_i)$ is $B(x_i)\to C(x_i)$.

  These are straightforward and left as exercises.

  \item[\textbf{Case 3.}] $\varphi(x_i)$ is $(\forall x_j)B(x_i)\;(j\neq i)$.
\end{itemize}
\end{proof}

Suppose that $v$ does not satisfy $\varphi(t)$. We show that $v'$ does not satisfy $\varphi(x_i)$. There is a valuation $w$ which is $j$-equivalent to $v$ and which does not satisfy $B(t)$. Let $w'$ be the valuation which is $i$-equivalent to $w$ and has $w'(x_i)=w(t)$. Then by the induction hypothesis applied to $B(x_i)$, we have that $w'$ does not satisfy $B(x_i)$ (since $w$ does not satisfy $B(t)$).

Now $t$ is free for $x_i$ in $(\forall x_j)B(x_i)$, so $x_j$ does not occur in $t$. Hence $v(t)$ depends only on $v(x_k)$ for $k\neq j$. But for $k\neq j$, $v(x_k)=w(x_k)$, so $v(t)=w(t)$. It follows that $w'$ is $j$-equivalent to $v'$, since $w$ is $j$-equivalent to $v$. Since $w'$ does not satisfy $B(x_i)$, then $v'$ does not satisfy $(\forall x_j)B(x_i)$, i.e., $v'$ does not satisfy $\varphi(x_i)$. The converse requires a similar argument, and is left as an exercise.