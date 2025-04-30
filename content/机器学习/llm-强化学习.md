---
title: llm_强化学习
date: 2024-11-12 15:38:47
tags: llm
---

```plantuml
(init-model) --> (pretrained-model):init
(pretrained-model) --> (supervised-fine-tuned-model):init
(supervised-fine-tuned-model) -->(reference-model):copy
(supervised-fine-tuned-model) -->(reward-model):init & 替换lm_head为reward_head
(reward-model) --> (value-model):init
(supervised-fine-tuned-model) --> (policy-model):copy
(policy-model) --> (reinforcement-learning-model):init
(reward-model) --> (reinforcement-learning-model):即时奖励
(value-model) --> (reinforcement-learning-model):价值估计
(reference-model) --> (reinforcement-learning-model):防止偏离基本SFT模型
```

{%plantuml%}
(init-model) --> (pretrained-model):init
(pretrained-model) --> (supervised-fine-tuned-model):init
(supervised-fine-tuned-model) -->(reference-model):copy
(supervised-fine-tuned-model) -->(reward-model):init & 替换 lm_head 为 reward_head
(reward-model) --> (value-model):init
(supervised-fine-tuned-model) --> (policy-model):copy
(policy-model) --> (reinforcement-learning-model):init
(reward-model) --> (reinforcement-learning-model):即时奖励
(value-model) --> (reinforcement-learning-model):价值估计
(reference-model) --> (reinforcement-learning-model):防止偏离基本 SFT 模型

{%endplantuml%}

- [奖励模型](#奖励模型)
  - [实现细节](#实现细节)
  - [Loss of reward model](#loss-of-reward-model)
  - [Example code](#example-code)
  - [Margin(optional)](#marginoptional)
- [PPO 优化](#ppo-优化)
  - [PPO 名字的来源](#ppo-名字的来源)
  - [PPO 涉及的四个模型](#ppo-涉及的四个模型)
  - [核心思想：“更”好](#核心思想更好)
  - [最小化目标](#最小化目标)
    - [GAE 优势](#gae-优势)
  - [PPO 伪代码](#ppo-伪代码)
  - [Example code](#example-code-1)

## 奖励模型

- 准备数据，格式为(prompt, chosen, rejected) 或 (chosen, rejected)
- 获取一个 SFT 模型作为 base 模型，去掉 SFT 的 llm_head,添加一个新的 reward_head，这个 每个 token 的 reward_head（这个 reward_head 每所有 token 共享） 应该输出一个标量值，表示给定输入的奖励
- 定义损失函数：$loss = -log(sigmoid(r_{chosen}-r_{rejected}))$
- 训练奖励模型

### 实现细节

策略模型会根据 query(即 prompt) 生成一段输出 response

seq_len = query.len+response.len

奖励模型和 value 模型的输入是 query 和 response 的拼接

输入的 shape 为(batch_size, seq_len)

输出的 shape 为(batch_size, seq_len, 1)

也就是说每个 token 都有一个与其 context 对应的奖励值

然后我们可以取最后一个 token 的奖励值作为整个序列的奖励值，即 `rewards = rewards[:, -1, :]`，
也可以取每个 token 的 reward 的 mean

### Loss of reward model

```python
def compute_loss(
    self,
    model: Union[PreTrainedModel, nn.Module],
    inputs: Dict[str, Union[torch.Tensor, Any]],
    return_outputs=False,
) -> Union[torch.Tensor, Tuple[torch.Tensor, Dict[str, torch.Tensor]]]:
    rewards_chosen = model(
        input_ids=inputs["input_ids_chosen"],
        attention_mask=inputs["attention_mask_chosen"],
        return_dict=True,
    )["logits"]
    rewards_rejected = model(
        input_ids=inputs["input_ids_rejected"],
        attention_mask=inputs["attention_mask_rejected"],
        return_dict=True,
    )["logits"]
    loss = -nn.functional.logsigmoid(rewards_chosen - rewards_rejected).mean()
    if return_outputs:
        return loss, {
            "rewards_chosen": rewards_chosen,
            "rewards_rejected": rewards_rejected,
        }
    return loss
```

### Example code

```python
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    AutoModelForCausalLM,
)
model = AutoModelForCausalLM.from_pretrained("gpt2")
print(model)
print("=" * 100)
model = AutoModelForSequenceClassification.from_pretrained("gpt2", num_labels=1)
def prepare_tokenizer(tokenizer):
    if tokenizer.eos_token is None:
        tokenizer.add_special_tokens({"eos_token": "<|endoftext|>"})
        model.resize_token_embeddings(len(tokenizer))
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    return tokenizer
tokenizer = AutoTokenizer.from_pretrained("gpt2")
tokenizer = prepare_tokenizer(tokenizer)
print(model)

import datasets
dataset_name = "trl-lib/ultrafeedback_binarized"
dataset = datasets.load_dataset(dataset_name)
print(dataset)
print(dataset["train"][0])

def from_chat_to_preference(example):
    result = {
        "chosen": example["chosen"][0]["content"] + example["chosen"][1]["content"],
        "rejected": example["rejected"][0]["content"]
        + example["rejected"][1]["content"],
    }
    return result



dataset = dataset.map(from_chat_to_preference)

from trl import RewardTrainer, RewardConfig
training_args = RewardConfig(
    report_to=["wandb"],
    output_dir=f"./results/ultrafeedback_binarized/1",
    run_name="ultrafeedback_binarized",
    per_device_train_batch_size=1,
    gradient_accumulation_steps=1,
    per_device_eval_batch_size=1,
    num_train_epochs=1,
    save_total_limit=2,  # limit the number of saved checkpoints
    save_strategy="steps",
    save_steps=1,
    load_best_model_at_end=True,
    eval_strategy="steps",
    eval_steps=1,
    eval_accumulation_steps=1,
    logging_steps=100,
    learning_rate=1e-4,
    lr_scheduler_type="constant",
    warmup_ratio=0.0,
    weight_decay=0.0,
    remove_unused_columns=False,  # tokenize the dataset on the fly
    # label_names=["labels"],
    metric_for_best_model="eval_loss",
    greater_is_better=False,
    seed=42,
    max_grad_norm=1.0,
    ddp_find_unused_parameters=False,
    fp16=True,
    no_cuda=True,
)
trainer = RewardTrainer(
    model=model,
    args=training_args,
    processing_class=tokenizer,
    train_dataset=dataset["train"],
    eval_dataset=dataset["test"],
)

trainer.train()

```

### Margin(optional)

![[机器学习/llm-强化学习/reward_margin.png]]

## PPO 优化

### [PPO 名字的来源](https://medium.com/@oleglatypov/a-comprehensive-guide-to-proximal-policy-optimization-ppo-in-ai-82edab5db200)

Imagine you’re training a computer program, like a virtual student, to write better and better essays. PPO helps this virtual student improve their essay-writing skills step by step.

Instead of making big changes all at once, PPO encourages small and gradual improvements. This way, the virtual student’s writing doesn’t change dramatically from one essay to the next. It’s like refining their skills bit by bit without completely altering their style.

This cautious approach has a special name: Proximal Policy Optimization. “Proximal” means staying close to the original style, and “Policy Optimization” is about finding better strategies. By staying close to the original style, the virtual student’s improvements are more stable and consistent.

### PPO 涉及的四个模型

- **Policy Model**: The model that generates the actions (e.g., text generation) based on the current policy.
  - P-model 就是最终会被用户使用的 user-friendly 的模型。例如 chatgpt。
  - 初始为 STF 模型。
  - 会被训练。
- **Value Model**: The model that estimates the value of a given state or sequence of actions.
  - V-model 用于评估给从给定状态，到无限的未来，能获得的奖励的期望值。
  - 初始为奖励模型。
  - 会被训练。
- **Reward Model**: The model that evaluates the quality of the generated actions or sequences, providing a scalar reward.
  - Reward-model 是体现人类偏好的模型，给定一个序列，输出一个值，表示该序列符合人类偏好的程度。
  - 是已经经过”人类偏好数据“训练好的模型，在 PPO 阶段直接使用。
  - 不会被训练，模型参数在 PPO 阶段不会改变。
- **Reference Model**: The model that provides a baseline for comparison, often used to compute the KL divergence to ensure the updated policy does not deviate too much from the original policy.
  - Reference-model 可用于计算 KL 散度或剪切，确保更新后的策略不会偏离原始策略太远。
  - 一般使用 STF 模型 作为 Reference-model。
  - 不会被训练，模型参数在 PPO 阶段不会改变。

### 核心思想：“更”好

好的含义：

- 从现在到无限的未来，获得更多的奖励。
- 不要和原始模型不要差太多

### 最小化目标

$$
r_t(\theta) = \frac{p_{\theta_{new}}(a_t|s_t)}{p_{\theta_{old}}(a_t|s_t)}
$$

$$
L^{CLIP}(\theta) = -\mathbb{E}_t\left[\min\left(r_t(\theta)\hat{A}_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon)\hat{A}_t\right)\right]
$$

$$
L^{VF}(\theta) = \mathbb{E}_t\left[\left(V_\theta(s_t)-\hat{R}_t\right)^2\right]
$$

$$
L^{PPO}(\theta) = L^{CLIP}(\theta) + cL^{VF}(\theta)
$$

#### GAE 优势

$\delta_t = R_t + \gamma V(s_{t+1}) - V(s_t)$
$\hat{A}_t = \delta_t + \gamma \lambda \hat{A}_{t+1}$
回报 returns $\hat{R}_t = \hat{A}_t + V(s_t)=R_t + \gamma V(s_{t+1})$

dp 求 return

```python
# 6. compute advantages and returns
lastgaelam = 0
advantages_reversed = []
gen_length = responses.shape[1]
for t in reversed(range(gen_length)):
    nextvalues = values[:, t + 1] if t < gen_length - 1 else 0.0
    delta = rewards[:, t] + args.gamma * nextvalues - values[:, t]
    lastgaelam = delta + args.gamma * args.lam * lastgaelam
    advantages_reversed.append(lastgaelam)
advantages = torch.stack(advantages_reversed[::-1], axis=1)
returns = advantages + values
```

### PPO 伪代码

```python
for batch in dataloader:
  torch.no_grad():
    使用query对policy model 进行采样(生成)，得到query_response,logits,log_prob
    使用query_response对reference model 进行forward,得到ref_logits,ref_log_prob
    使用query_response对value model 进行forward,得到value
    使用query_response对reward model 进行forward,得到reward
    使用log_prob,ref_log_prob计算kl散度，并将-kl散度加到reward上
    使用dp倒着计算advantages
    returns = advantages + values
  for ppo_epoch_idx in range(args.num_ppo_epochs):(使用这一个batch更新num_ppo_epochs次policy model)
    计算r_t
    compute_loss
    update policy model
    update value model
```

### Example code

```python
import shutil

import torch
from accelerate import PartialState
from datasets import load_dataset
from transformers import (
    AutoModelForCausalLM,
    AutoModelForSequenceClassification,
    AutoTokenizer,
    HfArgumentParser,
)

from trl import (
    ModelConfig,
    PPOConfig,
    PPOTrainer,
    ScriptArguments,
    get_kbit_device_map,
    get_peft_config,
    get_quantization_config,
)
from trl.trainer.utils import SIMPLE_CHAT_TEMPLATE


"""
python -i examples/scripts/ppo/ppo.py \
    --dataset_name trl-internal-testing/descriptiveness-sentiment-trl-style \
    --dataset_train_split descriptiveness \
    --learning_rate 3e-6 \
    --output_dir models/minimal/ppo \
    --per_device_train_batch_size 64 \
    --gradient_accumulation_steps 1 \
    --total_episodes 10000 \
    --model_name_or_path EleutherAI/pythia-1b-deduped \
    --missing_eos_penalty 1.0

accelerate launch --config_file examples/accelerate_configs/deepspeed_zero3.yaml \
    examples/scripts/ppo/ppo.py \
    --dataset_name trl-internal-testing/descriptiveness-sentiment-trl-style \
    --dataset_train_split descriptiveness \
    --output_dir models/minimal/ppo \
    --num_ppo_epochs 1 \
    --num_mini_batches 1 \
    --learning_rate 3e-6 \
    --per_device_train_batch_size 1 \
    --gradient_accumulation_steps 16 \
    --total_episodes 10000 \
    --model_name_or_path EleutherAI/pythia-1b-deduped \
    --sft_model_path EleutherAI/pythia-1b-deduped \
    --reward_model_path EleutherAI/pythia-1b-deduped \
    --local_rollout_forward_batch_size 1 \
    --missing_eos_penalty 1.0
"""


if __name__ == "__main__":
    parser = HfArgumentParser((ScriptArguments, PPOConfig, ModelConfig))
    script_args, training_args, model_config = parser.parse_args_into_dataclasses()
    # remove output_dir if exists
    shutil.rmtree(training_args.output_dir, ignore_errors=True)

    ################
    # Model & Tokenizer
    ################
    torch_dtype = (
        model_config.torch_dtype
        if model_config.torch_dtype in ["auto", None]
        else getattr(torch, model_config.torch_dtype)
    )
    quantization_config = get_quantization_config(model_config)
    model_kwargs = dict(
        revision=model_config.model_revision,
        attn_implementation=model_config.attn_implementation,
        torch_dtype=torch_dtype,
        device_map=get_kbit_device_map() if quantization_config is not None else None,
        quantization_config=quantization_config,
    )

    tokenizer = AutoTokenizer.from_pretrained(
        model_config.model_name_or_path,
        padding_side="left",
        trust_remote_code=model_config.trust_remote_code,
    )
    tokenizer.add_special_tokens({"pad_token": "[PAD]"})
    if tokenizer.chat_template is None:
        tokenizer.chat_template = SIMPLE_CHAT_TEMPLATE
    value_model = AutoModelForSequenceClassification.from_pretrained(
        training_args.reward_model_path,
        trust_remote_code=model_config.trust_remote_code,
        num_labels=1,
    )
    reward_model = AutoModelForSequenceClassification.from_pretrained(
        training_args.reward_model_path,
        trust_remote_code=model_config.trust_remote_code,
        num_labels=1,
    )
    policy = AutoModelForCausalLM.from_pretrained(
        training_args.sft_model_path, trust_remote_code=model_config.trust_remote_code
    )

    peft_config = get_peft_config(model_config)
    if peft_config is None:
        ref_policy = AutoModelForCausalLM.from_pretrained(
            training_args.sft_model_path,
            trust_remote_code=model_config.trust_remote_code,
        )
    else:
        ref_policy = None

    ################
    # Dataset
    ################
    dataset = load_dataset(
        script_args.dataset_name, split=script_args.dataset_train_split
    )
    eval_samples = 100
    train_dataset = dataset.select(range(len(dataset) - eval_samples))
    eval_dataset = dataset.select(range(len(dataset) - eval_samples, len(dataset)))
    dataset_text_field = "prompt"

    def prepare_dataset(dataset, tokenizer):
        """pre-tokenize the dataset before training; only collate during training"""

        def tokenize(element):
            outputs = tokenizer(
                element[dataset_text_field],
                padding=False,
            )
            return {"input_ids": outputs["input_ids"]}

        return dataset.map(
            tokenize,
            batched=True,
            remove_columns=dataset.column_names,
            num_proc=training_args.dataset_num_proc,
        )

    # Compute that only on the main process for faster data processing.
    # see: https://github.com/huggingface/trl/pull/1255
    with PartialState().local_main_process_first():
        train_dataset = prepare_dataset(train_dataset, tokenizer)
        eval_dataset = prepare_dataset(eval_dataset, tokenizer)

    ################
    # Training
    ################

    training_args.no_cuda = True
    trainer = PPOTrainer(
        config=training_args,
        processing_class=tokenizer,
        policy=policy,
        ref_policy=ref_policy,
        reward_model=reward_model,
        value_model=value_model,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
    )
    trainer.train()

    # Save and push to hub
    trainer.save_model(training_args.output_dir)
    if training_args.push_to_hub:
        trainer.push_to_hub(dataset_name=script_args.dataset_name)

    trainer.generate_completions()

```
