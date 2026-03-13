---
title: agent
---

- [1. 概念](#1-概念)
- [2. 提示词的组织方式](#2-提示词的组织方式)
- [3. 解释器](#3-解释器)

## 1. 概念

- LLM：Agent 的“大脑”，负责文本生成
- Function Call / Tool（函数调用/工具调用）：LLM输出某种格式的函数调用文本，agent将文本转化为函数调用，使得LLM能够与外部环境交互。
- MCP：工具调用规范

---

- State：存储LLM的记忆与状态
- Graph：
  - Node：
    - LLM：Node
    - Tool：Node
  - Route：
    - Hard Route: 基于条件的硬编码跳转。
    - Soft Route: 由 LLM 根据当前状态（State）决定下一个跳转的 Node。
- Subgraph

---

- Skill：针对特定业务目标封装的一套逻辑闭环。
  - Soft Skill(Declarative Skill)
    - 表现形式：一份详尽的 SOP（标准作业程序） 文档、一段 System Prompt，或者是一个带有丰富元数据的 README。
  - 核心逻辑：通过文档告诉 LLM：“如果你要完成某件事，你应该第一步做什么，第二步做什么，注意哪些禁忌。”
    - 运行方式：LLM 阅读这些文档，凭借自身的推理能力（Zero-shot 或 Few-shot）在脑中实时构建执行路径。
  - Hard Skill(Procedural Skill)
    - 表现形式：一个封装好的 Subgraph（子图）。它有明确的代码、节点（Node）定义和连线（Route）逻辑。
  - 核心逻辑：将复杂的“事”拆解为一个个确定的步骤，并用程序逻辑固定下来。
  - 运行方式：Agent 像调用函数一样进入这个子图，严格按照定义的拓扑结构运行。

---

## 2. 提示词的组织方式

- Message
  - System Message
  - User Message
  - AI Message
- Prompt：Message序列
- Preset：给LLM的一个常驻prompt。其他类型的提示词最终都会被组织（or注入）到这个prompt里。
  preset一般Agent 的“核心人格”与“底层逻辑”。包含全局 MCP 规范、回复格式要求（如：必须输出 JSON）以及当前 Agent 的基本背景。
- Chat: 一个聊天会话，由若干有顺序的Message组成。
- LoreBook：给LLM的一个临时prompt。触发一定的条件后会被自动注入到preset中
  常用Soft Skill 的动态加载。
- Character Card: 解决特定需求的agent的逻辑实体，一个Character可以绑定若干Lorebook。按理来说一个Character也要能绑定Skill。

---

## 3. 解释器

为了更灵活地操作prompt

规定一种转义字符，用于切换工作模式，例如由`#`引导进入脚本模式，（类似于typst）

初始状态是文本模式，在遇到`#{}`执行其中的代码，代码的结果被嵌入到文本中。

因此需要一个解释器。
