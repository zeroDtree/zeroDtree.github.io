---
title: holant problem
---

## 定义

- signature(local constraint function): A map $f:A\to B$ is a signature if (($\exists n \in \mathbb{N}, q\in \mathbb{Z}^+$ s.t. $A=[q]^n$) and ($\exists$ a commutative semiring $R$ s.t. $B=R$)). The set of signatures is denoted by $\mathcal{F}$
- symmetric signature: A signature $f:[q]^n\to R$ is symmetric if $f$ is invariant under permutation of the variables
- signature grid: A signature grid $\Omega = (G,\pi)$ over $\mathcal{F}$ consists of a graph $G = (V, E )$ and a mapping $\pi$ that assigns to each vertex $v \in V$ an $f_v \in \mathcal{F}$ and a linear order(total order) of the incident edges at $v$.The arity of $f$ is equal to the degree at $v$, and the incident edges at $v$ are associated with the input variables of $f_v$.
- planar signature grid: A planar signature grid is a signature grid such that its underlying graph is planar and for some planar embedding, for every vertex $v$, the linear order of the incident edges at $v$ agrees with the clockwise cyclic order of the incident edges at $v$ in the embedding starting with some particular edge.
- bipartite signature grid: For signature sets $F$ and $G$, a bipartite signature grid over $(F|G)$ is a signature grid $\Omega = (H,\pi)$ over $F\cup G$, where $H=(V,E)$ is a bipartite graph with bipartition $V=(V_1,V_2)$ such that $\pi(V_1)\subseteq F$ and $\pi(V_2)\subseteq G$.
- Holant problem $Holant_q(\mathcal{F})$:
  - input: A signature grid $\Omega = (G=(V,E),\pi)$ over $\mathcal{F}$
  - output: $Holant_q(\Omega;\mathcal{F}) = \sum_{\sigma:E \to [q]} \prod_{v\in V} f_v(\sigma |_{E(v)})$, where $E(v)$ is the set of edges incident to $v$
- tractable: polynomial-time computable
- #P is the set of functions $f : \{0,1\}^* \to \mathbb{N}$ such that there exists a polynomial $p : \mathbb{N} \to \mathbb{N}$ and a polynomial-time deterministic Turing machine $V$, called the verifier, such that for every $x \in \{0,1\}^*$, $f(x) = |\{y \in \{0,1\}^{p(|x|)} : V(x,y) = 1\}|$ (In other words, $f(x)$ equals the size of the set containing all of the polynomial-size certificates).

## 结论

- $CSP_q^d(\mathcal{F}) \equiv_T Holant_q(\mathcal{EQ}_d|\mathcal{F})=Holant_q(\mathcal{EQ}_d \cup \mathcal{F})$
- Let $\mathcal{F}$ be a set of signatures over a domain of size $q$. If there exists an $\mathcal{F}$-gate with signature $f$, then $\text{Holant}_q(\mathcal{F}, f) \leq_T \text{Holant}_q(\mathcal{F})$.

- Let $\mathcal{F}$ and $\mathcal{G}$ be sets of complex-valued signatures over a domain of size $q$. Suppose $\Omega$ is a bipartite signature grid over $(\mathcal{F} \mid \mathcal{G})$. If $T \in \text{GL}_q(\mathbb{C})$, then $\text{Holant}_q(\Omega; \mathcal{F} \mid \mathcal{G}) = \text{Holant}_q(\Omega'; \mathcal{F}T \mid T^{-1}\mathcal{G}),$ where $\Omega'$ is the corresponding signature grid over $(\mathcal{F}T \mid T^{-1}\mathcal{G})$.
