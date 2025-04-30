---
title: padding_side
date: 2024-06-25 22:11:56
tags: transformer
---

# 语言模型的padding问题。
## 生成式语言模型（例如decoder-only的模型）
### 训练的时候，一般右侧填充

```
如果采用右侧填充：
    无论采用绝对还是相对位置编码，看起来都没有什么问题
如果向左填充：
    如果采用绝对位置编码（如sin）：
        不同的句子长度，会影响同一个句子的token的位置编码。
        比如[pad,pad,pad,i,wang,to,sing, eos]
        和  [pad, i, wang, to, sing, eos]的相同句子里的
        token的位置编码不一样。这样合不合理？
            不合理的方面：
                同一个句子在不同batch中的位置编码可能不一致
            可能合理的方面：
                不合理的方面也许有利于鲁棒性？
    如果采用相对位置编码（如RoPE）：
        看起来不会产生问题。
```


### 生成的时候向左填充
这个在huggingface的文档里有一个理由:
LLMs are decoder-only architectures, meaning they continue to iterate on your input prompt. If your inputs do not have the same length, they need to be padded. Since LLMs are not trained to continue from pad tokens, your input needs to be left-padded. Make sure you also don’t forget to pass the attention mask to generate!
（原文地址https://huggingface.co/docs/transformers/llm_tutorial#wrong-padding-side ）

经与一位朋友讨论，生成的时候batch_size设置成1可以规避pad side问题，这样可能会使得处理大量数据时生成速度稍慢。

## encoder-（decoder）类型的语言模型（例如机器翻译，文本情感分类）右侧填充
1. 填充右侧的方式为人类一般的隐式习惯
2. 对于文本分类，需要获得每个句子的首个token(cls),如果采取左侧填充，不便于快速获取cls（special classification embedding）的位置
3. 这些任务不需要把输入和输出拼起来。
（参考的https://blog.csdn.net/qq_40965091/article/details/132007023 ）