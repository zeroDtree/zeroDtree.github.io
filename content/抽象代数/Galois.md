---
title: Galois Theory
---

## 前置

- [[抽象代数/域论(域拓展)]]

## 定义

- Let $E$ be a field. An **automorphism** of $E$ is a isomorphism of $E$ onto itself.
- If $E$ and $K$ are both field extensions of a field $F$ and $\sigma : E \rightarrow K$ is a field isomorphism, then an element $\alpha \in E$ is **fixed** by $\sigma$ if $\sigma (\alpha) = \alpha$. An element $\alpha \in E$ is **fixed** by a collection of isomorphisms if $\alpha$ is fixed by every isomorphism in the collection. A subset $L$ of $E$ is **fixed** by a collection of isomorphisms if every $\alpha \in L$ is fixed by the collection. Often write **remains fixed** instead of simply **fixed**.
- Let $F \leq K$ be a field extension. The set $G(K/F)$ is the set of all automorphisms of the field $K$ that fix every element of the field $F$.
- Let $E$ be an algebraic extension of the field $F$. Two elements $\alpha$ and $\beta$ in $E$ are conjugates over $F$, if both have the same minimal polynomial over $F$. That is,$\text{irr}(\alpha, F) = \text{irr}(\beta, F)$.
 

## 性质

1. Let $E$ be a field. Then the set of all automorphisms of $E$ is a group under composition.
2. Let $\sigma$ be an automorphism of the field $E$. Then the set $E_\sigma$ of all the elements $a \in E$ that remain fixed by $\sigma$ forms a subfield of $E$.
3. Let $\{ \sigma_i | i \in I \}$ be a collection of automorphisms of a field $E$. Then the set $E_{\{\sigma_i\}}$ , of all $a \in E$ that remain fixed by every $\sigma_i$, for $i \in I$, is a subfield of $E$. 因为域的任意交集还是域。
4. Let $E$ be a field and let $F$ be a subfield of $E$. Then the set $G(E/F)$ of all automorphisms that fix all the elements of $F$ is a subgroup of the automorphism group of $E$. Furthermore, $F$ is a subfield of $E_{G(E/F)}$. 
