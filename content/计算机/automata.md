---
title: 有限自动机(FA)
date: 2024-10-21 14:05:17
tags: 可计算性与计算复杂性
---

《Introduction to the Theory of Computation》里的自动机部分的定义和定理。

- [Finite automaton](#finite-automaton)
- [Nondeterministic finite automaton](#nondeterministic-finite-automaton)
- [Regular language](#regular-language)
- [Regular operations](#regular-operations)
- [Regular expression](#regular-expression)
- [Regular language is equivalent to language described by regular expression](#regular-language-is-equivalent-to-language-described-by-regular-expression)
- [Pumping lemma](#pumping-lemma)

#### Finite automaton

A finite automaton is a 5-tuple $\left(Q, \Sigma, \delta, q_0, F\right)$, where

1. $Q$ is a finite set called the states,
2. $\Sigma$ is a finite set called the alphabet,
3. $\delta: Q \times \Sigma \longrightarrow Q$ is the transition function
4. $q_0 \in Q$ is the start state, and
5. $F \subseteq Q$ is the set of accept states.

A string w is accepted by M if M read w, enter accept states.

If A is the set of all strings that machine M accepts, we say that A is the
language of machine M and write L(M ) = A. We say that M recognizes A or
that M accepts A.

```
A string w is rejected iff w is not accepted.
```

#### Nondeterministic finite automaton

A nondeterministic finite automaton is a 5-tuple $\left(Q, \Sigma, \delta, q_0, F\right)$, where

1. $Q$ is a finite set of states,
2. $\Sigma$ is a finite alphabet,
3. $\delta: Q \times \Sigma_{\varepsilon} \longrightarrow \mathcal{P}(Q)$ is the transition function,
4. $q_0 \in Q$ is the start state, and
5. $F \subseteq Q$ is the set of accept states.

Note: $\Sigma_{\varepsilon}$ 中包含一个空字符 $\varepsilon$

$\textbf{DFA equivalent to NFA}$

只需证明: Every nondeterministic finite automaton has an equivalent deterministic finite
automaton.

```
two automaton is equivalent iff they recogize same language
```

证明：将$Q$的幂集$\mathcal{P}(Q)$作为$DFA$的状态,状态$q$的闭包$E[q]$表示从状态$q$只经过$\epsilon$所能到达的所有状态的集合
构造的$DFA$如下：

1. 状态集：$\mathcal{P}(Q)=\{X|X \subseteq Q\}$
2. 符号表: $\Sigma_{\varepsilon}\backslash \{\varepsilon\}$ = $\Sigma$
3. 状态转移函数：$\delta(X,a)=\bigcup_{q\in X}E[\delta(q,a)]$
4. 初始状态：$E[q_0]$
5. 接受状态：$\{X\in \mathcal{P}(Q)|X\cap F \neq \emptyset\}$

#### Regular language

A language is called a regular language if some finite automatonrecognizes it.

A language is regular if and only if some nondeterministic finite automaton recognizes it.

#### Regular operations

Let $A$ and $B$ be regular languages. We define the regular operations union, concatenation, and star as follows:

- Union: $A \cup B=\{x \mid x \in A$ or $x \in B\}$.
- Concatenation: $A \circ B=\{x y \mid x \in A$ and $y \in B\}$.
- Star: $A^*=\left\{x_1 x_2 \ldots x_k \mid k \geq 0\right.$ and each $\left.x_i \in A\right\}$.

the collection of regular languages is closed under all three of the regular operations.

#### Regular expression

Say that $R$ is a regular expression if $R$ is

1. $a$ for some $a$ in the alphabet $\Sigma$,
2. $\varepsilon$,
3. $\emptyset$,
4. $\left(R_1 \cup R_2\right)$, where $R_1$ and $R_2$ are regular expressions,
5. $\left(R_1 \circ R_2\right)$, where $R_1$ and $R_2$ are regular expressions, or
6. $\left(R_1^*\right)$, where $R_1$ is a regular expression.

In items 1 and 2 , the regular expressions $a$ and $\varepsilon$ represent the
languages $\{a\}$ and $\{\varepsilon\}$, respectively. In item 3 , the regular expres-
sion $\emptyset$ represents the empty language. In items 4,5 , and 6 , the
expressions represent the languages obtained by taking the union
or concatenation of the languages $R_1$ and $R_2$, or the star of the
language $R_1$, respectively.

$L(R)$ to be the language of $R$.

#### Regular language is equivalent to language described by regular expression

A language is regular if and only if some regular expression describes it.

#### Pumping lemma

Pumping lemma If $A$ is a regular language, then there is a number $p$ (the pumping length) where if $s$ is any string in $A$ of length at least $p$, then $s$ may be divided into three pieces, $s=x y z$, satisfying the following conditions:

1. for each $i \geq 0, x y^i z \in A$,
2. $|y|>0$, and
3. $|x y| \leq p$.
