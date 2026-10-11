---
title: Rank
tags:
  - 线性代数
---

## Prerequisites

- [[线性代数/matrix]]

## 初等变换与初等矩阵

Let $A\in F^{m \times n}$ have columns $v_1,\cdots,v_n\in F^m$ and rows $w_1^T,\cdots,w_m^T$, where $w_i^T\in F^{1 \times n}$. The **column space** and the **row space** are

$$
\operatorname{col}(A)=\operatorname{span}(v_1,\cdots,v_n)\subseteq F^m,
\qquad
\operatorname{row}(A)=\operatorname{span}(w_1^T,\cdots,w_m^T)\subseteq F^{1 \times n}.
$$

- Elementary row operations
  - swap row $i$ and row $j$
  - multiply row $i$ by a nonzero scalar $c$
  - add $c$ times row $i$ to row $j$
- Elementary column operations
  - swap column $i$ and column $j$
  - multiply column $i$ by a nonzero scalar $c$
  - add $c$ times column $i$ to column $j$

An **elementary matrix** is a matrix obtained by performing exactly one elementary row operation on the identity matrix.

Left multiplication uses an $m \times m$ elementary matrix; right multiplication uses an $n \times n$ elementary matrix.

- Swap. $E_{ij}$ is $I$ with rows $i$ and $j$ swapped. Then $E_{ij}A$ swaps rows $i$ and $j$ of $A$, and $AE_{ij}$ swaps columns $i$ and $j$ of $A$. $E_{ij}^{-1} = E_{ij}$.
- Scale. $E_i(c)$, $c \neq 0$, is diagonal with $c$ in position $(i,i)$ and $1$ elsewhere. Then $E_i(c)A$ multiplies row $i$ of $A$ by $c$, and $AE_i(c)$ multiplies column $i$ of $A$ by $c$. $E_i(c)^{-1} = E_i(c^{-1})$.
- Add a multiple. $E_{ji}(c)$ is $I$ with $c$ in position $(j,i)$. Then $E_{ji}(c)A$ adds $c$ times row $i$ of $A$ to row $j$, and $AE_{ji}(c)$ adds $c$ times column $j$ of $A$ to column $i$. $E_{ji}(c)^{-1} = E_{ji}(-c)$.

The inverses above are two-sided, so every elementary matrix is invertible. A product of elementary matrices is invertible, with $(E_k\cdots E_1)^{-1}=E_1^{-1}\cdots E_k^{-1}$.

Let $P\in F^{m \times m}$ and $Q\in F^{n \times n}$ be invertible. Then

$$
\operatorname{row}(PA)=\operatorname{row}(A),\qquad \dim\operatorname{col}(PA)=\dim\operatorname{col}(A),
$$

$$
\operatorname{col}(AQ)=\operatorname{col}(A),\qquad \dim\operatorname{row}(AQ)=\dim\operatorname{row}(A).
$$

> proof
>
> The $i$-th row of $PA$ is $\sum_{k=1}^m P_{ik} w_k^T$, so $\operatorname{row}(PA)\subseteq\operatorname{row}(A)$. The same reading of $A=P^{-1}(PA)$ gives $\operatorname{row}(A)\subseteq\operatorname{row}(PA)$.
>
> The columns of $PA$ are $Pv_1,\cdots,Pv_n$, so $\operatorname{col}(PA)=\{Px:x\in\operatorname{col}(A)\}$. By [[抽象代数/向量空间]] 性质 6, $\operatorname{col}(A)$ has a finite basis $u_1,\cdots,u_d$. Every vector of $\operatorname{col}(A)$ is $\sum_i a_i u_i$, and $P$ sends it to $\sum_i a_i Pu_i$, so $Pu_1,\cdots,Pu_d$ spans $\operatorname{col}(PA)$. If $\sum_i a_i Pu_i=0$, then $P(\sum_i a_i u_i)=0$, hence $\sum_i a_i u_i=0$, and every $a_i=0$. 性质 8 gives $\dim\operatorname{col}(PA)=d=\dim\operatorname{col}(A)$.
>
> The $j$-th column of $AQ$ is $A$ times the $j$-th column of $Q$, so it lies in $\operatorname{col}(A)$ and $\operatorname{col}(AQ)\subseteq\operatorname{col}(A)$. The same reading of $A=(AQ)Q^{-1}$ gives $\operatorname{col}(A)\subseteq\operatorname{col}(AQ)$.
>
> 同理，$\dim\operatorname{row}(AQ)=\dim\operatorname{row}(A)$.

An elementary row operation is left multiplication by an elementary matrix, so it leaves $\operatorname{row}(A)$ unchanged and preserves $\dim\operatorname{col}(A)$. An elementary column operation is right multiplication by an elementary matrix, so it leaves $\operatorname{col}(A)$ unchanged and preserves $\dim\operatorname{row}(A)$.

A matrix is in **reduced row echelon form** when

- every zero row lies below every nonzero row;
- the first nonzero entry of each nonzero row is $1$, called a **pivot**;
- each pivot lies strictly to the right of the pivot in the row above;
- every other entry in a pivot column is $0$.

Every $A\in F^{m \times n}$ can be brought to reduced row echelon form by elementary row operations. Start at the first row and scan columns from the left. If the current column is zero at and below the current row, skip that column. Otherwise swap a nonzero entry into the current row, scale the row so the entry equals $1$, and add a multiple of this row to each other row so that the rest of the column becomes $0$. The current row already has $0$ in every earlier pivot column, so these additions leave the earlier pivot columns unchanged. Then move down one row. Each change is an elementary row operation, and the process stops after finitely many columns.

The result $R$ satisfies $R=EA$ for an invertible matrix $E$, so

$$
\operatorname{row}(A)=\operatorname{row}(R),\qquad \dim\operatorname{col}(A)=\dim\operatorname{col}(R).
$$

设 $R$ 有 $r$ 个主元，分别位于第 $j_1<\cdots<j_r$ 列。$R$ 的 $r$ 个非零行张成 $\operatorname{row}(R)$。若

$$
\sum_{i=1}^r c_i(\text{row }i)=0,
$$

则考察第 $j_t$ 个分量：由于第 $j_t$ 列只有第 $t$ 行为 $1$，其余元素均为 $0$，该分量就是 $c_t$，故 $c_t=0$。这对每个 $t$ 都成立，因此这 $r$ 个非零行线性无关，从而构成 $\operatorname{row}(R)$ 的一组基，所以 $\dim\operatorname{row}(R)=r$。

对每个 $i$，记第 $i$ 行主元所在的列为 $p_i\in F^m$。由简化行阶梯形矩阵的定义，$p_i$ 的第 $i$ 个分量为 $1$，其余分量均为 $0$。又因为 $R$ 只有前 $r$ 行可能非零，所以它的任意第 $j$ 列都可以写成

$$
\sum_{i=1}^r R_{ij}p_i.
$$

因此，$p_1,\cdots,p_r$ 张成 $\operatorname{col}(R)$；同时它们是不同的标准基向量，因而线性无关。于是它们构成 $\operatorname{col}(R)$ 的一组基，所以 $\dim\operatorname{col}(R)=r$。

Therefore $\dim\operatorname{col}(A)=\dim\operatorname{row}(A)$.

## Rank

For $A\in F^{m \times n}$,

$$
\operatorname{rank}(A)=\dim\operatorname{col}(A)=\dim\operatorname{row}(A).
$$

The common value equals the number of pivots in the reduced row echelon form of $A$.

## 可逆

Let $A = [v_1\ \cdots\ v_n] \in F^{n \times n}$, where $v_i \in F^n$ is column $i$ of $A$.

$A$ is invertible if and only if $v_1,\ldots,v_n$ is a basis of $F^n$.

> proof
>
> If $v_1,\ldots,v_n$ is a basis, [[抽象代数/向量空间]] 性质 13 writes each column $e_j$ of $I$ as $e_j = Ab_j$. The matrix $B = [b_1\ \cdots\ b_n]$ satisfies $AB = I$, so $\operatorname{det}(A)\operatorname{det}(B) = \operatorname{det}(I) \not= 0$. Hence $\operatorname{det}(A) \not= 0$, and $A$ is invertible.
>
> Conversely, if $A$ is invertible and $Ax = 0$, the same formula gives $A^{-1}0 = 0$, so $x = A^{-1}(Ax) = 0$. The columns are linearly independent. 性质 12 gives $\dim(F^n) = n$. 性质 7 extends the columns to a basis, and 性质 8 says every basis has $n$ vectors, so the columns are already a basis.
