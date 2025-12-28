---
title: shape
---

## 正常batch

`micro_shape`:每一个样本的shape

`full_shape`: 一个batch的shape

`macro_shape`：`shape[:-len(micro_shape)]`

例：文本的`full_shape=(b, n, d)`, 其中`b`为batch_size,`d`为嵌入维度, 则`macro_shape=(b,)`, `micro_shape=(n, d)`

例：图像的`full_shape=(b, c, w, h)`, 其中`b`为batch_size，`c`为通道数，`w`和`h`分别为宽和高，则`micro_shape=(c, w, h)`, `macro_shape=(b, )`

`macro_shape`在大部分情况下就是`(b,)`

## Batch flattening

假设`b`个样本，`micro_shape`为$(n_i, \dots)$

batch flattening 后 `full_shape`=$(\sum n_i, \dots)$

`macro_shape`被约定为`(b, )`

`micro_shape`被约定为$(\dots)$，即少了一维，那一维被batch flatten占了。

在batch flattening的情况下，原来的shape为$(b,)$的张量，为了与full_shape的数据一起运算，需要被拓展为$(\sum n_i, )$


