---
title: KV Cache & Prompt Cache
---

- [1. 重复计算问题](#1-重复计算问题)
- [2. KV Cache](#2-kv-cache)
- [3. Prompt Cache](#3-prompt-cache)
  - [3.1. 错误示例：动态内容放在最前面](#31-错误示例动态内容放在最前面)
  - [3.2. 正确示例：静态长内容放在最前面](#32-正确示例静态长内容放在最前面)
- [4. 提高命中率的工程原则](#4-提高命中率的工程原则)

KV Cache 是 LLM 推理加速的核心技术。**保存已经算过的 Key / Value，避免自回归生成时反复重算同一段前缀**，空间换时间。

## 1. 重复计算问题

假设输入序列有 $t$ 个 token，表示为：

$$
(x_1, x_2, \dots, x_t)
$$

在 Transformer 的自注意力中，每个 token 会通过线性映射生成 Query、Key、Value：

$$
q_i = x_i W_Q,\quad k_i = x_i W_K,\quad v_i = x_i W_V
$$

对于第 $i$ 个位置，注意力输出是对它之前所有 Value 的加权平均：

$$
z_i = \sum_{j=1}^{i} \alpha_{i,j} v_j
$$

其中权重来自 Query 和 Key 的相似度：

$$
\alpha_{i,j}
= \frac{\exp(\text{score}(q_i, k_j))}
{\sum_{l=1}^{i} \exp(\text{score}(q_i, k_l))},
\quad
\text{score}(q_i, k_j) = \frac{q_i k_j^T}{\sqrt{d_k}}
$$

在 Prefill 阶段，模型一次性处理完整 Prompt，所以可以并行计算所有 token 的 $Q, K, V$。真正的问题出现在 Decoding 阶段。

LLM 生成文本是自回归的：生成第 $t+1$ 个 token 时，模型已经拥有前面的 $x_1 \dots x_t$。

如果没有 KV Cache，下一步推理需要重新输入：

$$
(x_1, x_2, \dots, x_t, x_{t+1})
$$

这会带来三个动作：

1. 计算当前 token 的 $q_{t+1}, k_{t+1}, v_{t+1}$。
2. 重新计算已经算过的 $k_1 \dots k_t$ 和 $v_1 \dots v_t$。
3. 用 $q_{t+1}$ 和所有 $k_1 \dots k_{t+1}$ 做点积，再对所有 $v_1 \dots v_{t+1}$ 加权求和。

第二步可能是冗余的。

**因果掩码保护历史状态**：LLM模型使用 Causal Mask。第 $i$ 个位置只能看见自己和之前的 token：

$$
Attention(q_i, K, V)
= \sum_{j=1}^{i}
\text{softmax}\left(\frac{q_i k_j^T}{\sqrt{d}}\right)v_j
$$

因此，追加新的 token 不会反过来改变旧位置的隐藏状态。第 $i$ 个位置在每一层的表示只依赖 $x_1 \dots x_i$，不依赖未来的 $x_{i+1}, x_{i+2}, \dots$。

因此只要模型权重和前缀 token 没变，过去 token 对应的 $K, V$ 就不会变。

## 2. KV Cache

KV Cache 的做法是：**把每一层已经计算过的 $K, V$ 保存在显存里**。

生成第 $t+1$ 个 token 时，只需要做增量计算：

1. 只为当前 token 计算新的 $Q, K, V$：

$$
q_{t+1} = x_{t+1} W_Q,\quad
k_{t+1} = x_{t+1} W_K,\quad
v_{t+1} = x_{t+1} W_V
$$

2. 从缓存中读取历史前缀：

$$
K_{prefix} = (k_1, \dots, k_t),\quad
V_{prefix} = (v_1, \dots, v_t)
$$

3. 把新的 $k_{t+1}, v_{t+1}$ 追加到缓存：

$$
K_{new} = [K_{prefix}, k_{t+1}],\quad
V_{new} = [V_{prefix}, v_{t+1}]
$$

4. 只用当前 Query 和完整 Key 做一次向量-矩阵计算：

$$
\text{scores}_{t+1}
= \frac{q_{t+1} [k_1, \dots, k_{t+1}]^T}{\sqrt{d_k}}
$$

最终得到：

$$
z_{t+1}
= \text{softmax}(\text{scores}_{t+1})
[v_1, \dots, v_{t+1}]
$$

KV Cache 让模型**不再重新计算历史的 Key 和 Value**。

## 3. Prompt Cache

KV Cache 通常指一次请求内部的缓存；Prompt Cache 则更进一步，试图在多次请求之间复用相同前缀的 KV。

Prompt Cache 命中的本质是：

> 两次请求从开头开始的 token 序列必须完全一致，缓存才能从这段共同前缀继续复用。

如果 Prompt 的前缀发生变化，例如 System Prompt 里多了一个空格、工具定义顺序变了、时间戳放在了最前面，那么变化位置之后的所有 KV 都需要重新计算。

Transformer 处理的是 Token ID 序列。一个空格、一个换行、一个字段顺序变化，都可能改变 tokenization 结果，也会改变后续每一层的隐藏状态。

### 3.1. 错误示例：动态内容放在最前面

```text
System: 你是一个助手。当前用户是 {name}，现在时间是 {time}。
Context: [10k 字参考文档...]
User: 请根据文档回答问题。
```

这里 `{name}` 和 `{time}` 每次都变，导致后面的 10k 字文档虽然内容相同，也无法作为稳定前缀复用。

### 3.2. 正确示例：静态长内容放在最前面

```text
System: 你是一个助手。
Context: [10k 字参考文档...]
User: 我是 {name}，现在是 {time}。请根据文档回答问题。
```

这样 `System + Context` 是稳定前缀，动态变量被推到末尾，缓存命中率会高很多。

## 4. 提高命中率的工程原则

| 原则         | 做法                                       | 原因                      |
| :----------- | :----------------------------------------- | :------------------------ |
| 静态前缀优先 | 把 System Prompt、长文档、固定规则放在开头 | 最大化可复用前缀          |
| 动态内容后置 | 用户名、时间戳、随机 ID、实时状态放在末尾  | 避免动态变量截断缓存      |
| 工具定义稳定 | 固定 function schema 的顺序、字段和格式    | 工具列表也是 prompt token |
| 格式标准化   | 统一换行、空格、缩进、JSON 序列化方式      | 空白符也会影响 token      |
| 历史只追加   | 对话历史尽量追加，不修改中间消息           | 保持已有前缀连续          |
| 截断从头部做 | 超出上下文时优先移除最旧历史               | 避免改写中间结构          |
