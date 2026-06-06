---
title: Coherence
---

Definition, Property and Theorem about Coherence in 《ON THE GENERALIZATION MYSTERY IN DEEP LEARNING》

- [1. Relative work](#1-relative-work)
  - [1.1. Neural networks can memorize random dataset](#11-neural-networks-can-memorize-random-dataset)
  - [1.2. Implicit bias](#12-implicit-bias)
  - [1.3. Uniform convergence may be unable to explain generalization in deep learning.](#13-uniform-convergence-may-be-unable-to-explain-generalization-in-deep-learning)
  - [1.4. What makes a pattern “simple” and why are such patterns reliably learned early](#14-what-makes-a-pattern-simple-and-why-are-such-patterns-reliably-learned-early)
  - [1.5. Comments](#15-comments)
- [2. Future work](#2-future-work)
- [3. Regularization techniques](#3-regularization-techniques)
- [4. Coherence](#4-coherence)
  - [4.1. Boundedness and Scale Invariance](#41-boundedness-and-scale-invariance)
  - [4.2. Stylized mini-batching](#42-stylized-mini-batching)
  - [4.3. Effect of zero vectors](#43-effect-of-zero-vectors)
  - [4.4. Combining orthogonal distributions](#44-combining-orthogonal-distributions)
  - [4.5. Bound on Expected Difference](#45-bound-on-expected-difference)
  - [4.6. Decomposition](#46-decomposition)
- [5. Shortcomings](#5-shortcomings)
- [6. Generalization Theorem of Coherence](#6-generalization-theorem-of-coherence)
  - [6.1. Gap of Generalization](#61-gap-of-generalization)
  - [6.2. Stability](#62-stability)
  - [6.3. Stability equals generalization](#63-stability-equals-generalization)
  - [6.4. Smoothness Assumptions.](#64-smoothness-assumptions)
  - [6.5. Stability of (Stochastic) Gradient Descent](#65-stability-of-stochastic-gradient-descent)
  - [6.6. 1-Step Expansion](#66-1-step-expansion)
  - [6.7. Unrolling recursion).](#67-unrolling-recursion)
  - [6.8. Bound the difference between examples by the coherence as measured by α](#68-bound-the-difference-between-examples-by-the-coherence-as-measured-by-α)
  - [6.9. Stability Theorem](#69-stability-theorem)
  - [6.10. Generalization Theorem](#610-generalization-theorem)
  - [6.11. Corollary: fixed step sizes(learning rate)](#611-corollary-fixed-step-sizeslearning-rate)
  - [6.12. Corollary: step sizes decay linearly](#612-corollary-step-sizes-decay-linearly)

## 1. Relative work

### 1.1. Neural networks can memorize random dataset

[Understanding deep learning requires rethinking generalization.](https://arxiv.org/pdf/1611.03530)
Typical neural networks trained with stochastic gradient descent, which is the usual training method, can easily memorize a random dataset of the same size as the (real) dataset that they were designed for.

### 1.2. Implicit bias

Implicit bias:from among all the models that fit the training set perfectly in an over-parameterized setting, how does gradient descent find one that generalizes well to unseen data when such a model exists

### 1.3. Uniform convergence may be unable to explain generalization in deep learning.

[Uniform convergence may be unable to explain generalization in deep learning.](https://arxiv.org/pdf/1902.04742)

### 1.4. What makes a pattern “simple” and why are such patterns reliably learned early

[A Closer Look at Memorization in Deep Networks](https://arxiv.org/pdf/1706.05394)
In a study on memorization in shallow fully-connected networks and small convolutional networks on mnist and cifar-10, [Arpit et al. 2017](https://arxiv.org/pdf/1706.05394) discovered that for real datasets, starting from different random initializations, many examples are consistently classified correctly or incorrectly after one epoch of training. They call these easy and hard examples respectively. They hypothesize that this variability of difficulty in real data “is because the easier examples are explained by some simple patterns, which are reliably learned within the first epoch of training.”

### 1.5. Comments

First, the difficulty of an example is not simply a property of that example (whether it has simple patterns or not), but depends on the relationship of that example to others in the training set (what it shares with other examples).

Second, the dynamics of training, including initialization, can determine the difficulty of examples. Consequently, it can accommodate the observed phenomenon of adversarial initialization where examples that are easy to learn with random initialization become significantly harder to learn with a different, specially constructed initialization, and the generalization performance of the network suffers. Any notion of simplicity of patterns intrinsic to an example alone cannot explain adversarial initialization since the dataset remains the same, and therefore, so do the patterns in the data.

Examples learned late by gradient descent (that is, the hard examples), by themselves, are insufficient to define the decision boundary to the same extent that early (or easy) examples are.

## 2. Future work

1. Better metrics for coherence and a tighter bounds.
2. Providing a continuous explanation for the phenomenon of deep double descent
3. nonvacuous bound on the generalization gap
4. Generalization and width.
5. Practical use for new algorithms

## 3. Regularization techniques

- Gradients mean estimation techniques
- View L2 regularization
- Early stopping

## 4. Coherence

$$
\alpha \equiv \frac{\ell(w+h)-\ell(w)}{\underset{z \sim \mathcal{D}}{\mathbb{E}}\left[\ell_z\left(w+h_z\right)-\ell_z(w)\right]}=\frac{\underset{z \sim \mathcal{D}, z^{\prime} \sim \mathcal{D}}{\mathbb{E}}\left[g_z \cdot g_{z^{\prime}}\right]}{\underset{z \sim \mathcal{D}}{\mathbb{E}}\left[g_z \cdot g_z\right]}=\frac{\underset{z \sim \mathcal{D}}{\mathbb{E}}\left[\left.g_z\right]\right] \underset{z \sim \mathcal{D}}{\mathbb{E}}\left[g_z\right]}{\underset{z \sim \mathcal{D}}{\mathbb{E}}\left[g_z \cdot g_z\right]}
$$

$$
\alpha(\mathcal{V}) \equiv \frac{\underset{v \sim \mathcal{V}, v^{\prime} \sim \mathcal{V}}{\mathbb{E}}\left[v \cdot v^{\prime}\right]}{\underset{v \sim \mathcal{V}}{\mathbb{E}}[v \cdot v]}
$$

### 4.1. Boundedness and Scale Invariance

$$
0 \leq \alpha(\mathcal{V}) \leq 1
$$

where $\alpha(\mathcal{V})=0$ iff $\mathbb{E}_{v \sim \mathcal{V}}[v]=0$ and $\alpha(\mathcal{V})=1$ iff all the vectors are equal.
Furthermore, for non-zero $k \in \mathbb{R}$, we have,

$$
\alpha(k \mathcal{V})=\alpha(\mathcal{V})
$$

where $k \mathcal{V}$ denotes the distribution of the random variable $k v$ where $v$ is drawn from $\mathcal{V}$.

### 4.2. Stylized mini-batching

Let $v_1, v_2, . ., v_k$ be $k$ i.i.d. variables drawn from $\mathcal{V}$. Let $\mathcal{W}$ denote the distribution of the random variable $w=\frac{1}{k} \sum_{i=1}^k v_i$. We have,

$$
\alpha(\mathcal{W})=\alpha(k \mathcal{W})=\frac{k \cdot \alpha(\mathcal{V})}{1+(k-1) \cdot \alpha(\mathcal{V})}
$$

Furthermore, $\alpha(\mathcal{W}) \geq \alpha(\mathcal{V})$ with equality iff $\alpha(\mathcal{V})=0$ or $\alpha(\mathcal{V})=1$

When $\alpha \ll 1 / k$ but non-zero (i.e., we have high gradient diversity), creating mini-batches of size $k$ increases coherence almost $k$ times. But, when $\alpha \approx 1$ (i.e., low diversity) there is not much point in creating mini-batches since there is little room for improvement.

### 4.3. Effect of zero vectors

If $\mathcal{W}$ denotes the distribution where with probability $p>0$ we pick a vector from $\mathcal{V}$ and with probability $1-p$ we pick the zero vector then $\alpha(\mathcal{W})=p \cdot \alpha(\mathcal{V})$

### 4.4. Combining orthogonal distributions

If $\mathcal{W}$ denotes the distribution where with probability $p>0$ we pick a vector from $\mathcal{U}$ and with probability $1-p$ we pick a vector from $\mathcal{V}$ and all elements in the support of $\mathcal{U}$ are orthogonal to those in the support of $\mathcal{V}$ then we have

$$
\alpha(\mathcal{W}) \leq p \cdot \alpha(\mathcal{U})+(1-p) \cdot \alpha(\mathcal{V})
$$

### 4.5. Bound on Expected Difference

$$
\underset{v \sim \mathcal{V}, v^{\prime} \sim \mathcal{V}}{\mathbb{E}}\left[\left\|v-v^{\prime}\right\|\right] \leq \sqrt{2(1-\alpha(\mathcal{V})) \underset{v \sim \mathcal{V}}{\mathbb{E}}[v \cdot v]}
$$

### 4.6. Decomposition

Let $V$ be the support of the distribution $\mathcal{V}$. Furthermore, let

$$
V=V_1 \oplus V_2 \oplus \cdots \oplus V_k
$$

where the subspaces $V_i(1 \leq i \leq k)$ are orthogonal to each other, that is, $V$ is the orthogonal direct sum of the $V_i . \mathcal{V}$ induces a distribution $\mathcal{V}_i$ on each $V_i$. Suppose each $\alpha\left(\mathcal{V}_i\right)$ exists. Then,

$$
\alpha(\mathcal{V})=f_1 \cdot \alpha\left(\mathcal{V}_1\right)+f_2 \cdot \alpha\left(\mathcal{V}_2\right)+\cdots+f_k \cdot \alpha\left(\mathcal{V}_k\right)
$$

where $f_i \equiv \mathbb{E}_{v_i \sim \mathcal{V}_i}\left[v_i \cdot v_i\right] /\left(\sum_{i=1}^k \underset{v_i \sim \mathcal{V}_i}{\mathbb{E}}\left[v_i \cdot v_i\right]\right)$ and $0 \leq f_i \leq 1$ and $\sum_{i=0}^k f_i=1$.

## 5. Shortcomings

As a measure of coherence, αm/α⊥m over the whole network, being an average, is a blunt instrument, and therefore, a finer-grained analysis, for example, on a per-layer basis, is sometimes necessary.

## 6. Generalization Theorem of Coherence

### 6.1. Gap of Generalization

$$
\text{gap}(\mathcal{D}, m) \equiv \mathbb{E}_{S \sim \mathcal{D}^m} \mathbb{E}_\theta \left[ R(A_\theta(S)) - \hat{R}(A_\theta(S), S) \right]
$$

### 6.2. Stability

$$
\text{stab}(\mathcal{D}, m) \equiv \mathbb{E}_{S \sim \mathcal{D}^m} \mathbb{E}_{S' \sim \mathcal{D}^m} \mathbb{E}_\theta \left[ \frac{1}{m} \sum_{i \in [m]} \left[ \ell(A_\theta(S^{(i)}), z_i) - \ell(A_\theta(S), z_i) \right] \right]
$$

### 6.3. Stability equals generalization

$$
\text{gap}(\mathcal{D}, m) = \text{stab}(\mathcal{D}, m).
$$

### 6.4. Smoothness Assumptions.

1. We assume that $\ell(\cdot, z)$ is $L$-Lipschitz and differentiable for every $z \in Z$, that is,

   $$
   \left|\ell(w, z)-\ell\left(w^{\prime}, z\right)\right| \leq L\left\|w-w^{\prime}\right\|
   $$

   and

   $$
   \|g(w, z)\| \leq L
   $$

2. We also assume that $\ell(\cdot, z)$ is $\beta$-smooth for every $z \in Z$. That is, we assume,
   $$
   \left\|g(w, z)-g\left(w^{\prime}, z\right)\right\| \leq \beta\left\|w-w^{\prime}\right\|
   $$

### 6.5. Stability of (Stochastic) Gradient Descent

Let $I_t(θ)$ be an indicator variable that is 1 if the ith training example is selected in the mini-batch used at time step t ∈ [T ], and 0 otherwise. Therefore,

$$
\underset{\theta}{\mathbb{E}}\left[I_t(\theta)\right]=b / m
$$

Let $\delta_t=\left\|w_t-w_t^{\prime}\right\|$, and let $\Delta_t^{\prime \prime}(b)=\frac{1}{b} \sum_{j \in[b]}\left[g\left(w_{t-1}, z_{t j}\right)-g\left(w_{t-1}^{\prime}, z_{t j}^{\prime}\right)\right]$. then

$$
\delta_t \leq \delta_{t-1}+\eta_t\left\|\Delta_t^{\prime \prime}(b)\right\|
$$

### 6.6. 1-Step Expansion

For $t \in[T]$, we have,

$$
\delta_t \leq\left(1+\eta_t \beta\right) \cdot \delta_{t-1}+\frac{\eta_t I_t(\theta)}{b} \cdot\left\|g\left(w_{t-1}, z_i\right)-g\left(w_{t-1}, z_i^{\prime}\right)\right\|
$$

### 6.7. Unrolling recursion).

$$
\delta_T \leq \sum_{t \in[T]}\left(\frac{\eta_t I_t(\theta)}{b} \cdot\left\|g\left(w_{t-1}, z_i\right)-g\left(w_{t-1}, z_i^{\prime}\right)\right\| \cdot \prod_{k=t+1}^T\left(1+\eta_k \beta\right)\right)
$$

### 6.8. Bound the difference between examples by the coherence as measured by α

$$
\underset{S \sim D^m}{\mathbb{E}} \underset{z_i^{\prime} \sim \mathcal{D}}{\mathbb{E}} \underset{\theta}{\mathbb{E}}\left[\left|\ell\left(\mathbf{A}_\theta\left(S^{(i)}\right), z_i\right)-\ell\left(\mathbf{A}_\theta(S), z_i\right)\right|\right] \leq \frac{L^2}{m} \sum_{t \in[T]}\left[\eta_k \beta\right]_{k=t+1}^T \cdot \eta_t \cdot \sqrt{2\left(1-\alpha\left(w_{t-1}\right)\right)}
$$

### 6.9. Stability Theorem

$$
|\operatorname{stab}(\mathcal{D}, m)| \leq \frac{L^2}{m} \sum_{t \in[T]}\left[\eta_k \beta\right]_{k=t+1}^T \cdot \eta_t \cdot \sqrt{2\left(1-\alpha\left(w_{t-1}\right)\right)}
$$

### 6.10. Generalization Theorem

$$
|\operatorname{gap}(\mathcal{D}, m)| \leq \frac{L^2}{m} \sum_{t \in[T]}\left[\eta_k \beta\right]_{k=t+1}^T \cdot \eta_t \cdot \sqrt{2\left(1-\alpha\left(w_{t-1}\right)\right)}
$$

### 6.11. Corollary: fixed step sizes(learning rate)

If the step sizes are fixed, that is, $\eta_t=\eta$ then

$$
|\operatorname{gap}(\mathcal{D}, m)| \leq \frac{L^2 \eta}{m} \sum_{t \in[T]} \exp ((T-t) \eta \beta) \cdot \sqrt{2\left(1-\alpha\left(w_{t-1}\right)\right)}
$$

### 6.12. Corollary: step sizes decay linearly

If we assume as in Hardt et al. [2016] that step sizes decay linearly, that is, for some $\eta>0$ we have $\eta_t \leq \eta / t$ then

$$
|\operatorname{gap}(\mathcal{D}, m)| \leq \frac{L^2 \eta T^{\eta \beta}}{m} \sum_{t \in[T]} \sqrt{2\left(1-\alpha\left(w_{t-1}\right)\right)}
$$
