---
title: Rank
---

## Prerequisites

- [[linear-algebra/matrix]]

## Linear combination

A linear combination of a sequence of vectors $v_1, v_2, \cdots, v_k$ is a vector of the form $c_1 v_1 + c_2 v_2 + \cdots + c_k v_k$, where $c_i \in F, v_i \in F^n$.

## Linear Independence

A sequence of vectors $v_1, v_2, \cdots, v_k$ is said to be linearly independent if the only solution to the equation $c_1 v_1 + c_2 v_2 + \cdots + c_k v_k = 0$ is the trivial solution $c_1 = c_2 = \cdots = c_k = 0$. Where $c_i \in F, v_i \in F^n$.

## Span

The span of a sequence of vectors $v_1, v_2, \cdots, v_k$ is the set of all linear combinations of $v_1, v_2, \cdots, v_k$, denoted by $span(v_1, v_2, \cdots, v_k)$.

$span(v_1, v_2, \cdots, v_k) = \{c_1 v_1 + c_2 v_2 + \cdots + c_k v_k | c_i \in F, v_i \in F^n\}$

$span(v_1, v_2, \cdots, v_k)$ is a subspace of $F^n$.

If $A=(v_1, v_2, \cdots, v_k) \in F^{n \times k}$, then $col(A):=span(A): = span(v_1, v_2, \cdots, v_k)$.

## Elementary transformations

- Elementary row operations
  - swap row $i$ and row $j$
  - multiply row $i$ by a nonzero scalar $c$
  - add $c$ times row $i$ to row $j$
- Elementary column operations
  - swap column $i$ and column $j$
  - multiply column $i$ by a nonzero scalar $c$
  - add $c$ times column $i$ to column $j$

Elementary row operations can be implemented by multiplying $A$ by an elementary matrix from the left.

Elementary column operations can be implemented by multiplying $A$ by an elementary matrix from the right.

Elementary row operations not change the dimension of the **row space** and the **column space**.

Elementary column operations not change the dimension of the **column space** and the **row space**.

Elementary row operations can be used to reduce a matrix to its reduced row echelon form. Dimension of the row space equals Dimension of the column space in reduced row echelon form.

Therefore, $$\dim(col(A)) = \dim(row(A))$$.

## Rank

$A \in F^{m \times n}$ is a matrix.

$rank(A) = \dim(col(A)) = \dim(row(A))$
