---
title: "DeepSeek-V4.1 flash 1017"
date: 2026-10-24
tags:
  - 提示词
  - 大模型
---

## 1. 目录

- [DeepSeek-V4.1 ：推理强度、消息组装与工具调用](#deepseek-v41-推理强度消息组装与工具调用)
  - [2. 三层结构：API、编码器、引擎](#2-三层结构api编码器引擎)
  - [3. Token 流](#3-token-流)
  - [4. 消息组装的五步流水线](#4-消息组装的五步流水线)
    - [4.1. 合并工具消息与同角色合并](#41-合并工具消息与同角色合并)
      - [4.1.1. 合并矩阵](#411-合并矩阵)
      - [4.1.2. 几个具体例子](#412-几个具体例子)
      - [4.1.3. 实用规则](#413-实用规则)
    - [4.2. 排序并行工具结果](#42-排序并行工具结果)
    - [4.3. 处理图片](#43-处理图片)
    - [4.4. 丢弃历史 reasoning](#44-丢弃历史-reasoning)
  - [5. 角色渲染细节](#5-角色渲染细节)
    - [5.1. system](#51-system)
    - [5.2. user](#52-user)
    - [5.3. assistant](#53-assistant)
    - [5.4. tool](#54-tool)
    - [5.5. latest\_reminder 与 task](#55-latest_reminder-与-task)
      - [5.5.1. latest\_reminder 是什么](#551-latest_reminder-是什么)
      - [5.5.2. 为什么需要这个专门的 role](#552-为什么需要这个专门的-role)
      - [5.5.3. 哪些调用方式可以设置](#553-哪些调用方式可以设置)
      - [5.5.4. task](#554-task)
  - [6. 工具调用：DSML + tool\_result](#6-工具调用dsml--tool_result)
    - [6.1. 工具定义](#61-工具定义)
    - [6.2. 工具调用](#62-工具调用)
    - [6.3. 工具结果](#63-工具结果)
    - [6.4. 完整例子](#64-完整例子)
  - [7. 推理强度：一行系统提示](#7-推理强度一行系统提示)
    - [7.1. API 表面](#71-api-表面)
    - [7.2. 真正的机制](#72-真正的机制)
    - [7.3. 软控制与硬控制](#73-软控制与硬控制)
    - [7.4. 多轮对话与工具调用](#74-多轮对话与工具调用)
    - [7.5. API 层的采样参数](#75-api-层的采样参数)
  - [8. 参考](#8-参考)

# DeepSeek-V4.1 ：推理强度、消息组装与工具调用

---

## 2. 三层结构：API、编码器、引擎

理解 DeepSeek 的 prompt，先把链路拆成三层：

```text
┌─────────────────────┐
│  API / Recipe 层     │  参数归一化：thinking、reasoning_effort、tools、messages
└──────────┬──────────┘
           │  OpenAI / Anthropic / Responses 格式
           ▼
┌─────────────────────┐
│  encoding/encoding.py │  把 messages 渲染成一条 prompt 字符串 + 图片数据
└──────────┬──────────┘
           │  token IDs / prompt string
           ▼
┌─────────────────────┐
│  Inference Engine    │  只负责生成 token
└─────────────────────┘
```

## 3. Token 流

DeepSeek-V4.1 的 prompt 是一条扁平字符串，由特殊 token 划分角色和结构：

| Token                                                       | 作用                    |
| ----------------------------------------------------------- | --------------------- |
| `<｜begin▁of▁sentence｜>`                                     | BOS                   |
| `<｜end▁of▁sentence｜>`                                       | EOS，每个 assistant 消息末尾 |
| `<｜System｜>`                                                | 系统消息                  |
| `<｜User｜>`                                                  | 用户消息                  |
| `<｜Assistant｜>`                                             | assistant 回复头         |
| `<｜latest_reminder｜>`                                       | 提醒消息（模型侧扩展角色，不触发新轮次）  |
| `<think>` / `</think>`                                      | 思考段起止                 |
| `<｜DSML｜ calls>` / `<｜DSML｜ invoke>` / `<｜DSML｜ parameter>` | 工具调用块                 |
| `<tool_result>...</tool_result>`                            | 工具结果（普通文本标签）          |
| `<｜deepseek_image｜>`                                        | 图片占位符                 |

一个典型的 thinking 模式对话骨架：

```text
<｜begin▁of▁sentence｜>
<｜System｜>Reasoning Effort: 75 (range 1-100, ...)

You are a helpful assistant.
<｜User｜>用户问题
<｜Assistant｜><think>推理内容</think>正式回答<｜end▁of▁sentence｜>
<｜User｜>下一个问题
<｜Assistant｜><think>
```

这里有两个很重要的设计：

1. **assistant 消息本身不带开头的 `<think>`**。`<think>` 是由前一条 user/system 消息的“生成头”追加的；assistant 消息只负责输出 `reasoning_content`、`</think>`、正文和 EOS。
2. **EOS 只出现在 assistant 消息末尾**。user、system、tool_result 都不会追加 EOS。

---

## 4. 消息组装的五步流水线

`encode_messages()` 的签名大致是：

```python
encode_messages(
    messages,
    thinking_mode,              # "chat" or "thinking"
    context=None,               # 前缀缓存/历史上下文
    drop_thinking=True,         # 是否丢弃历史 reasoning
    add_default_bos_token=True,
    reasoning_effort=None,      # None / int 1-100 / "low" / "high" / "max"
    return_multi_modal_data=False,
)
```

内部按以下顺序处理。

### 4.1. 合并工具消息与同角色合并

DeepSeek-V4.1 **没有独立的 `tool` role**。`merge_tool_messages()` 会把：

```python
{"role": "tool", "tool_call_id": "call_1", "content": "Sunny, 22C"}
```

转换成：

```python
{
    "role": "user",
    "content_blocks": [
        {"type": "tool_result", "tool_use_id": "call_1", "content": "Sunny, 22C"}
    ],
}
```

最终渲染成：

```text
<｜User｜><tool_result>Sunny, 22C</tool_result>
```

同时，连续的 user 消息会被合并。比如“工具结果”后面紧跟一条用户输入，它们会进入同一个 `<｜User｜>` 块：

```text
<｜User｜><tool_result>结果A</tool_result>

<tool_result>结果B</tool_result>

用户接下来的问题
```

#### 4.1.1. 合并矩阵

只有 `user` / `tool` 这一条线会合并，`assistant`、`system`、`latest_reminder` 都不会：

| 输入                               | 是否合并 | 渲染结果                                         |
| -------------------------------- | ---- | -------------------------------------------- |
| user, user, user                 | ✅    | 一个 `<｜User｜>U1\n\nU2\n\nU3`                  |
| user, tool                       | ✅    | `<｜User｜>U1\n\n<tool_result>T</tool_result>` |
| tool, tool                       | ✅    | 一个 `<｜User｜>`，多个 `<tool_result>`             |
| user(task=...), user             | ❌    | 两个 `<｜User｜>`，task 阻断合并                      |
| user, assistant, user            | ❌    | 两个 `<｜User｜>`，assistant 隔断                   |
| assistant, assistant             | ❌    | 第二个 assistant 没有 `<｜Assistant｜>` 头           |
| system, system                   | ❌    | 两个 `<｜System｜>`，第二个是 mid-conversation system |
| latest_reminder, latest_reminder | ❌    | 两个 `<｜latest_reminder｜>`                     |

规则只有三条：

1. `tool` 消息先被转换成 `user` 消息 + `<tool_result>` content block；
2. 如果合并后的上一条消息是 `user`、有 `content_blocks`、且没有 `task`，就把新内容并进去，否则新开一条 `user` 消息；
3. 其他 role 原样保留，不参与合并。

#### 4.1.2. 几个具体例子

```text
[user U1, user U2, user U3]
→ <｜User｜>U1\n\nU2\n\nU3<｜Assistant｜><think>

[user U1, assistant A1, user U2]
→ <｜User｜>U1<｜Assistant｜></think>A1<｜end▁of▁sentence｜><｜User｜>U2<｜Assistant｜><think>

[system S1, system S2, user U]
→ <｜System｜>S1<｜System｜>S2<｜User｜>U<｜Assistant｜><think>

[user(task="query") U1, user U2]
→ <｜User｜>U1<｜User｜>U2<｜Assistant｜><think>
```

连续 assistant 是最危险的一种：

```text
[assistant A1, assistant A2]
→ ...<｜Assistant｜><think></think>A1<｜end▁of▁sentence｜></think>A2<｜end▁of▁sentence｜>
```

第二个 assistant 没有自己的 `<｜Assistant｜>` 头，prompt 结构是坏的，**不要连续发送 assistant 消息**。

连续 `system` 是合法的（mid-conversation system），但它们是两个独立的 `<｜System｜>` 块，不会合并；连续 `latest_reminder` 同理，各自独立的 token。

#### 4.1.3. 实用规则

- 想让多段文本落在同一个用户回合：直接发多条 `user`，它们会合并；
- 想保留多个独立用户回合：中间插入 `assistant` 或 `system` 消息；
- 不要连续发 `assistant`；
- 连续 `system`、连续 `latest_reminder` 合法但不合并。

### 4.2. 排序并行工具结果

assistant 一次可能发起多个并行工具调用。工具结果返回的顺序不一定和调用顺序一致，因此 `sort_tool_results_by_call_order()` 会按照 assistant 消息里 `tool_calls` 的顺序重排 `tool_result` 块。

例如 assistant 依次调用了 `a`、`b`，但工具结果先返回 `b` 再返回 `a`，最终 prompt 里仍然是：

```text
<tool_result>A-result</tool_result>

<tool_result>B-result</tool_result>
```

### 4.3. 处理图片

`process_image_messages()` 会把 `image` / `image_url` content block 替换成文本占位符：

```text
<｜deepseek_image｜>
```

图片本身不会进入文本 prompt，而是作为独立的 media 记录返回：

```python
(prompt, {"images": [{"type": "image", "url": "..."}]})
```

工具结果内部的图片也会被递归处理。用户文本或 `reasoning_content` 里如果出现字面量 `<｜deepseek_image｜>`，encoder 会直接拒绝，防止用户伪造图片 token。

### 4.4. 丢弃历史 reasoning

`drop_thinking` 默认是 `True`。在 thinking 模式下，编码器会把“最后一个 user turn 之前”的 assistant 消息的 `reasoning_content` 删掉，只保留正文和工具调用。

判断“最后一个 user turn”的函数是 `find_last_user_index()`，它有两个特殊规则：

- 对话中间的 system 消息算作 user turn；
- **只包含 tool_result、没有 text/image 的 user 消息不算新的 user turn**。

这就是为什么工具结果之后，assistant 仍然处在同一个“当前轮”的 reasoning 上下文中。

另外，**只要对话里出现 tools，`drop_thinking` 会被强制设为 `False`**，历史 reasoning 不再丢弃。这是为了保证工具调用链的上下文完整，代价是 prompt 会变长。

---

## 5. 角色渲染细节

### 5.1. system

```text
<｜System｜>{content}
```

如果 system 消息带有 `tools`，会在内容后追加工具说明和 schema：

```text
<｜System｜>{system 内容}

## Tools

You have access to a set of tools to help answer the user's question.
...
### Available Tool Schemas

{"name": "get_weather", "description": "...", "parameters": {...}}

You MUST strictly follow the above defined tool name and parameter schemas...
```

如果带有 `response_format`，还会追加：

```text
## Response Format:

You MUST strictly adhere to the following schema to reply:
{schema}
```

### 5.2. user

```text
<｜User｜>{content}
```

如果内容是 content blocks，则按顺序拼接，块之间用 `\n\n`：

- `text` → 原文本；
- `tool_result` → `<tool_result>{content}</tool_result>`；
- 其他类型 → `[Unsupported {type}]`。

### 5.3. assistant

assistant 的模板是：

```text
{reasoning}{content}{tool_calls}<｜end▁of▁sentence｜>
```

其中：

- `reasoning` 是 `reasoning_content + </think>`，**没有开头的 `<think>`**；
- 开头的 `<think>` 由前一条 user/system 消息追加；
- `tool_calls` 如果有，渲染成 DSML 块；
- 默认追加 EOS；`wo_eos=True` 时不追加，常用于 prefix caching / teacher forcing。

所以一个带思考的历史 assistant 轮次实际长这样：

```text
<｜User｜>问题<｜Assistant｜><think>推理内容</think>正式回答<｜end▁of▁sentence｜>
```

如果历史 reasoning 被丢弃，则变成：

```text
<｜User｜>问题<｜Assistant｜></think>正式回答<｜end▁of▁sentence｜>
```

### 5.4. tool

V4.1 **没有独立的 tool role**。直接传入 `role="tool"` 会报错：

```text
deepseek_v41 merges tool messages into user; please preprocess with merge_tool_messages()
```

正确做法是让 `merge_tool_messages` 把它变成 user 消息：

```text
<｜User｜><tool_result>工具返回内容</tool_result>
```

### 5.5. latest_reminder 与 task

#### 5.5.1. latest_reminder 是什么

`latest_reminder` 是一个模型侧的扩展角色，作用是把“最新的动态上下文”以提醒的形式注入当前轮，典型内容是日期、时区、locale、位置、环境状态等。它不是一条用户消息，也不是一条系统指令。

```text
<｜latest_reminder｜>{content}
```

`content` 按普通字符串处理，直接拼在 token 后面，编码器不会加 `<｜User｜>` 或 `<｜Assistant｜>` 包装。

| 行为                      | latest_reminder                       |
| ----------------------- | ------------------------------------- |
| 算不算 user turn           | 不算，`find_last_user_index()` 不把它当作用户轮次 |
| 是否触发新的 assistant 回答     | 不触发，自己不会追加 `<｜Assistant｜>`            |
| 是否会被 `drop_thinking` 丢掉 | 不会，`keep_roles` 包含 `latest_reminder`  |
| 渲染位置                    | 取决于 thinking 模式，见下                    |

渲染位置由前一条 user 消息的生成头决定。thinking 模式下，前一条 user 消息先追加 `<｜Assistant｜><think>`，提醒落在当前轮的思考块里：

```text
<｜User｜>What's the date today?<｜Assistant｜><think><｜latest_reminder｜>Today is 2026-10-24; locale=zh-CN
```

模型从这里继续生成推理，提醒相当于它思考上下文的一部分。chat 模式下追加的是 `<｜Assistant｜></think>`，提醒落在 `</think>` 之后：

```text
<｜User｜>What's the date today?<｜Assistant｜></think><｜latest_reminder｜>Today is 2026-10-24; locale=zh-CN
```

#### 5.5.2. 为什么需要这个专门的 role

核心动机是 prefix caching：

- 日期、locale 这类信息每轮都可能变，写进 system prompt 会让整个前缀失效，KV cache 从第一个 block 开始重算；
- 放进对话尾部、当前轮附近，前面稳定的 system、tools schema、历史对话仍然可以命中 prefix cache；
- 它不开启新的对话轮次，模型不会把提醒当成一条需要单独回答的用户消息；
- reasoning pruning 时它被保留，动态上下文不会因为丢弃历史思考而消失。

#### 5.5.3. 哪些调用方式可以设置

| 调用方式                      | 能否设置 | 说明                                                                                                          |
| ------------------------- | ---- | ----------------------------------------------------------------------------------------------------------- |
| 官方 DeepSeek API           | ❌    | `messages[].role` 只公开 `system` / `user` / `assistant` / `tool`，传 `latest_reminder` 大概率被 schema 拒绝（HTTP 400） |
| vLLM（OpenAI-compatible）   | ✅    | PR #61446 让 Rust chat renderer 接受 `role="latest_reminder"`                                                  |
| SGLang（OpenAI-compatible） | ✅    | PR #23692 把 `latest_reminder` 加入 OpenAI chat API 的 role enum                                                |
| DeepInfer 离线推理            | ✅    | 没有 API schema 校验，构造 message dict 直接调用 `encode_messages`                                                     |

自建 OpenAI-compatible 服务上可以直接这样发：

```json
{
    "role": "latest_reminder",
    "content": "Today is 2026-10-24; locale=zh-CN"
}
```

DeepInfer 的离线路径：

```python
messages = [
    {"role": "user", "content": "What's the date today?"},
    {"role": "latest_reminder", "content": "Today is 2026-10-24; locale=zh-CN"},
]
prompt = encode_messages(messages, thinking_mode="thinking")
```

#### 5.5.4. task

`task` 字段用于内部快速指令/分类任务，支持 `action`、`query`、`authority`、`domain`、`title`、`read_url` 等类型。非 `action` 任务会在消息后直接追加对应的特殊 token，例如 `<｜query｜>`；`action` 任务则追加 `<｜Assistant｜>` + thinking 开关对应的 token（thinking 模式是 `<think>`，chat 模式是 `</think>`）+ `<｜action｜>`。

---

## 6. 工具调用：DSML + tool_result

### 6.1. 工具定义

工具定义挂在 system 消息的 `tools` 字段上，编码器会把它们渲染成 `## Tools` 系统提示，并把 schema 逐行写成 JSON：

```text
### Available Tool Schemas

{"name": "get_weather", "description": "Get the weather for a city", "parameters": {...}}
```

注意：只有 system 分支会渲染 `tools`。把 tools 挂在 user 消息上会被忽略。

### 6.2. 工具调用

assistant 的工具调用不是 JSON，而是 DSML 块：

```text
<｜DSML｜ calls>
<｜DSML｜ invoke name="get_weather">
<｜DSML｜ parameter name="city" string="true">Paris</｜DSML｜ parameter>
</｜DSML｜ invoke>
</｜DSML｜ calls>
```

参数编码规则：

- 字符串参数：值原样写入，`string="true"`；
- 数字、布尔、数组、对象：值写 JSON，`string="false"`。

DSML 块前会有一个空行，块后紧跟 assistant 消息的 EOS。

### 6.3. 工具结果

工具结果被合并成 user 消息里的 `<tool_result>` 块：

```text
<｜User｜><tool_result>Sunny, 22C</tool_result>
```

多个结果用 `\n\n` 分隔。如果工具结果后面还有用户输入，它们会合并进同一个 `<｜User｜>` 块。

### 6.4. 完整例子

输入：

```python
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the weather for a city",
        "parameters": {"type": "object", "properties": {"city": {"type": "string"}}},
    },
}]

messages = [
    {"role": "system", "content": "You are a helpful assistant.", "tools": tools},
    {"role": "user", "content": "What's the weather in Paris?"},
    {"role": "assistant", "content": "Let me check.",
     "reasoning_content": "I should call get_weather.",
     "tool_calls": [{"id": "call_1", "type": "function",
                     "function": {"name": "get_weather",
                                  "arguments": "{\\"city\\":\\"Paris\\"}"}}]},
    {"role": "tool", "tool_call_id": "call_1", "content": "Sunny, 22C"},
    {"role": "assistant", "content": "It is sunny and 22C in Paris.",
     "reasoning_content": "The tool returned the weather; answer the user."},
    {"role": "user", "content": "And in London?"},
]
```

渲染出的对话部分：

```text
<｜User｜>What's the weather in Paris?<｜Assistant｜><think>I should call get_weather.</think>Let me check.

<｜DSML｜ calls>
<｜DSML｜ invoke name="get_weather">
<｜DSML｜ parameter name="city" string="true">Paris</｜DSML｜ parameter>
</｜DSML｜ invoke>
</｜DSML｜ calls><｜end▁of▁sentence｜><｜User｜><tool_result>Sunny, 22C</tool_result><｜Assistant｜><think>The tool returned the weather; answer the user.</think>It is sunny and 22C in Paris.<｜end▁of▁sentence｜><｜User｜>And in London?<｜Assistant｜><think>
```

---

## 7. 推理强度：一行系统提示

### 7.1. API 表面

官方 API 把“是否思考”和“思考强度”拆成两个维度：

| API 格式                  | 开关                                    | 强度字段                                 |
| ----------------------- | ------------------------------------- | ------------------------------------ |
| OpenAI Chat Completions | `thinking.type: enabled/disabled`     | `reasoning_effort: low/high/max`     |
| Anthropic Messages      | `thinking.type: enabled/disabled`     | `output_config.effort: low/high/max` |
| Responses               | `reasoning.effort: none/low/high/max` | 同一字段                                 |

默认行为：**思考模式默认开启，effort 默认 `high`**。

传入的 effort 别名会被归一化：

| 请求值                         | 实际档位   |
| --------------------------- | ------ |
| `minimal` / `low`           | `low`  |
| `medium` / `high` / `xhigh` | `high` |
| `max` / `ultra`             | `max`  |

也就是说，官方 API 实际上只有 **low / high / max 三档**；`medium`、`xhigh` 等只是兼容别名。`none` 是关闭思考的哨兵值，不是一个强度档位。

OpenAI SDK 的调用形式大致是：

```python
response = client.chat.completions.create(
    model="deepseek-flash",
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}},
)
```

`none` 只出现在 Responses 的 `reasoning.effort` 中，表示关闭思考；OpenAI / Anthropic 格式用 `thinking.type="disabled"` 关闭。思考关闭后，effort 不会渲染，也不会生效。

### 7.2. 真正的机制

以 `DeepSeek-V4.1-Flash-1017` 为例，`encoding/encoding.py` 里的定义是：

```python
REASONING_EFFORT_TEMPLATE = (
    "Reasoning Effort: {budget} "
    "(range 1-100, the higher the value, the more thorough the reasoning)\n\n"
)

REASONING_EFFORT_MAPPINGS = {
    "low": 50,
    "high": 75,
    "max": 100,
}
DEFAULT_REASONING_EFFORT = "high"
```

当 `thinking_mode == "thinking"` 且消息的**绝对下标为 0** 时，encoder 会在对话最前面注入：

```text
<｜begin▁of▁sentence｜><｜System｜>Reasoning Effort: 75 (range 1-100, the higher the value, the more thorough the reasoning)

<第一条消息内容...>
```

几个关键点：

- **命名档位只是别名**，模型看到的是一个 1–100 的数字：`low=50`、`high=75`、`max=100`。
- 也直接接受 **1–100 的整数**；中间值被设计用来“引出插值式的推理行为”，即介于两档之间的强度。
- 非法值会直接报错：`Invalid reasoning effort ... should be int within [1,100] or ['low', 'high', 'max']`。
- 这行提示**只在 thinking 模式下渲染**；chat 模式下不注入。
- 如果第一条消息本身是 system，effort 前缀会放在 system 内容之前，二者共用同一个 `<｜System｜>` 块。
- 如果第一条消息是 user，thinking 模式下也会先插入 `<｜System｜>Reasoning Effort: ...`，所以模型总能看到 effort。

换句话说，**effort 是一个被训练进模型行为的 prompt 条件信号**，而不是一个运行时旋钮。它改变的是模型生成推理长度的倾向，不保证模型一定想多久。

### 7.3. 软控制与硬控制

| 控制                 | 类型   | 作用                                                          |
| ------------------ | ---- | ----------------------------------------------------------- |
| `reasoning_effort` | 软控制  | 通过 prompt 提示模型“想多深”                                         |
| `thinking` 开关      | 硬控制  | 决定是否进入思考段：chat 模式下生成头直接是 `<｜Assistant｜></think>`            |
| `max_tokens`       | 硬控制  | 限制总生成长度；在 DeepInfer 里 reasoning 和 answer 是同一条 token 流，所以都计入 |
| `</think>` token   | 结构控制 | 服务层用它切分 `reasoning_content` 和 `content`                     |

因此，effort=max 并不等于“无限思考”。如果 `max_tokens` 不够，思考会被截断，`finish_reason` 会体现为长度截断。

### 7.4. 多轮对话与工具调用

- **不带 tools**：历史轮次的 `reasoning_content` 不需要回传；即使传入 API，也会被忽略，不会拼接进上下文。
- **带 tools**：历史轮次的 `reasoning_content` 必须完整回传，否则 API 返回 400。编码器侧对应的行为是：只要出现 tools，就强制 `drop_thinking=False`，保留历史 reasoning。
- **effort 只在 index 0 渲染**：它是一个全局值，不会在后续轮次重复。如果传入非空 `context`，新的 effort 前缀不会出现（详见下一节）。

### 7.5. API 层的采样参数

官方 API 在思考模式下会忽略 `temperature`、`presence_penalty`、`frequency_penalty`；`top_p` 的行为还取决于具体模型：

- `deepseek-flash`：思考模式下 `top_p` 生效，范围 0.95–1.0；
- `deepseek-v4-pro`：思考模式下忽略传入值，携带 tools 时固定 0.95，否则固定 1.0。

需要强调：这是 **API 层策略**。如果你直接使用 DeepInfer，`SamplingParams.temperature` 仍然会被引擎采样使用，引擎不会因为 `thinking_mode` 自动忽略它。

---

## 8. 参考

- [DeepSeek-V4.1-Flash-1017 `encoding/encoding.py`](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017/raw/main/encoding/encoding.py)
- [DeepSeek-V4.1-Flash-1017 `encoding/README.md`](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017/blob/main/encoding/README.md)
- [DeepSeek-V4.1-Flash `chat_template.jinja`](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/raw/main/chat_template.jinja)
- [DeepSeek API Docs — Create Chat Completion](https://api-docs.deepseek.com/api/create-chat-completion)
- [DeepSeek API Docs — 思考模式](https://api-docs.deepseek.com/zh-cn/guides/thinking_mode/)
- [DeepSeek API Docs — Thinking Mode (EN)](https://api-docs.deepseek.com/guides/thinking_mode/)
- [vLLM PR #61446](https://github.com/vllm-project/vllm/pull/61446)：renderer 接受 `role="latest_reminder"`
- [SGLang PR #23692](https://github.com/sgl-project/sglang/pull/23692)：OpenAI chat API 的 role enum 加入 `latest_reminder`
