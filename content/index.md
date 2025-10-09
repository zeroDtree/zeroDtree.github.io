---
title: Forever young
---

- [Notation](#notation)
	- [1. Math Symbols](#1-math-symbols)
	- [2. Logic Symbols](#2-logic-symbols)
	- [3. Computer Symbols](#3-computer-symbols)
- [Folders with clear dependencies](#folders-with-clear-dependencies)
- [友链](#友链)

# Notation

## 1. Math Symbols

- Vector is denoted as bold letter, e.g. $\mathbf{a}$, Matrix is denoted as capital letter, e.g. $A$, $a_i$ means the $i$th element of $\mathbf{a}$, $a_{ij}$ means the $(i,j)$th element of $A$
- All vectors are column vectors
- $\mathbb{Z}$ is the set of integers.
- $\mathbb{Q}$ is the set of rational numbers.
- $\mathbb{R}$ is the set of real numbers.
- $\mathbb{C}$ is the set of complex numbers.
- $\mathbb{F}$ is a filtration.
- $\mathbb{P}$ is a probability measure.
- $\mathbb{E}$ is the expectation operator.
- $[n]$ := $\{1,2,\cdots,n\}$
- $\mathbb{Z}_n$ := $\{0,1,\cdots,n-1\}$
- $\mathbb{Z}_{\geq n}$ := $\{i \mid i \in \mathbb{Z} \wedge i \geq n\}$
- $\overline{\mathbb{R}}$ := $\mathbb{R} \cup \{-\infty,+\infty\}$
- For $X \subseteq \overline{\mathbb{R}}$, $X^+$ := $\{x\in X|x>0\}$
- For $X \subseteq \overline{\mathbb{R}}$, $X^*$ := $\{x\in X|x\geq 0\}$
- For $\mathbf{a}, \mathbf{b} \in \overline{\mathbb{R}}^n, \mathbf{a} \lt \mathbf{b}$ := $\forall i, a_i \leq b_i$
- Class of sets is denoted as calligraphic letter, e.g. $\mathcal{A}$, $\mathcal{B}$, $\mathcal{F}$
- $\mathcal{P}(X)$ is the power set of $X$
- $\biguplus$ represents the union of disjoint sets.
- $A^{\text{\#}}$ is the adjoint matrix of $A$
- $(X, \tau)$ is a topological space, briefly written as $X$
- $\mathcal{B}(X):= \sigma(\mathcal{\tau})$, where $(X, \tau)$ is a topological space
- $\wedge$ represents the **and** for logic, **min** for function
- $\vee$ represents the **or** for logic, **max** for function

## 2. Logic Symbols

- Little letters (e.g. $p,q,r$) are used to represent propostional variables
- $\neg$ is used to represent negation
- $\wedge$ is used to represent conjunction
- $\vee$ is used to represent disjunction
- $\to$ is used to represent implication
- $\leftrightarrow$ is used to represent equivalence
- $\mathscr{A} \implies \mathscr{B}$ means $(\mathscr{A} \rightarrow \mathscr{B})$ is True
- $\mathscr{A} \iff \mathscr{B}$ means $((\mathscr{A} \rightarrow \mathscr{B}) \wedge (\mathscr{B} \rightarrow \mathscr{A}))$ is True
- $\mathscr{L}_0$ is used to represent a zero-order language
- $\mathscr{L}$ is used to represent a first-order language
- `mathscr` upper letters (e.g. $\mathscr{A},\mathscr{B},\mathscr{C}$) are used to represent the formulas (well-formed formulas,wfs) of a language $\mathscr{L}$ and $\mathscr{L}_0$

## 3. Computer Symbols

- Local network is denoted as capital letter, e.g. $A$,$B$,$C$
- Host in local network is denoted as small letter, e.g. $a$,$b$,$c$ located in local network $A$,$B$,$C$
- Public ip is denoted as Greek letter, e.g. $\alpha$,$\gamma$,$\beta$
- Hosts in the same local network are distinguished by subscripts, e.g. $a_1$,$a_2$,$a_5$ located in local network $A$.

# Folders with clear dependencies

![[dependency_graph]]

- linear-algebra
- 数学分析
- 抽象代
- 数理逻辑
- 朴素集合论
- 测度论与概率论

# 友链

![[友链]]
