---
title: agent
---

- [1. 核心概念](#1-核心概念)
- [2. 提示词 (Prompt) 组织架构](#2-提示词-prompt-组织架构)
- [3. 编程语言嵌入 (Template Engine)](#3-编程语言嵌入-template-engine)
- [4. tool/skill 的安全策略](#4-toolskill-的安全策略)
- [5. 多agent协作](#5-多agent协作)
  - [5.1. 协作的拓扑结构：](#51-协作的拓扑结构)
    - [5.1.1. 主从模式 (Orchestrator - Workers)](#511-主从模式-orchestrator---workers)
    - [5.1.2. 接力模式 (Sequential Pipeline)](#512-接力模式-sequential-pipeline)
    - [5.1.3. 群聊模式 (Joint Collaboration / Peer-to-Peer)](#513-群聊模式-joint-collaboration--peer-to-peer)
      - [5.1.3.1. 中心化：主持人模式 (Moderator)](#5131-中心化主持人模式-moderator)
      - [5.1.3.2. 去中心化：共识路由模式 (Consensus)](#5132-去中心化共识路由模式-consensus)
      - [5.1.3.3. 环境化：系统调度模式 (Orchestrator)](#5133-环境化系统调度模式-orchestrator)

## 1. 核心概念

- **LLM (Large Language Model)**：Agent 的“控制中心（Controller）”，负责逻辑推理、意图识别与文本生成。
- **Function Call / Tool Use**：一种连接机制。LLM 输出结构化指令（如 JSON），由宿主环境转化为具体的函数执行，使 LLM 具备操作外部世界的能力。
- **MCP (Model Context Protocol)**：由 Anthropic 发起的标准化工具调用与数据交互协议，旨在消除不同工具间的集成壁垒。

---

- **State (状态机)**：持久化存储 Agent 的长短期记忆、执行上下文及变量状态。
- **Graph (拓扑图)**：
  - **Node (节点)**：执行单元。可以是 **LLM 节点**（决策/生成）或 **Tool 节点**（执行/计算）。
  - **Edge / Route (路由)**：
    - **Hard Route (静态路由)**：基于预设条件（如 `if/else` 或状态码）的确定性跳转。
    - **Soft Route (动态路由)**：由 LLM 充当“路由器”，根据当前 State 语义化决定下一个目标节点。
- **Subgraph (子图)**：逻辑封装单元。将复杂的局部流程抽象为一个独立节点，实现架构的模块化与复用。

---

- **Skill (技能)**：针对特定业务目标封装的逻辑闭环。
  - **Soft Skill (Declarative / 声明式技能)**
    - **表现形式**：详尽的 SOP 文档、System Prompt 或带有元数据的 README。
    - **核心逻辑**：基于“提示词工程”。通过自然语言告知 LLM 执行步骤、约束条件与目标策略。
    - **运行方式**：LLM 依靠上下文理解能力（In-context Learning）在运行时动态构建执行路径。
  - **Hard Skill (Procedural / 过程式技能)**
    - **表现形式**：封装好的 **Subgraph**。拥有明确的代码逻辑、节点定义与拓扑连线。
    - **核心逻辑**：基于“工作流工程”。将复杂任务拆解为高可靠性的确定性步骤。
    - **运行方式**：Agent 以调用子程序的方式进入子图，严格遵循定义的拓扑结构执行。

---

## 2. 提示词 (Prompt) 组织架构

- **Message (消息)**：最小交互单元，包含 `System` (系统级指令)、`User` (用户输入)、`Assistant` (AI 响应) 及 `Tool` (工具返回)。
- **Prompt (提示词)**：有序的 Message 序列，构成模型理解任务的基准。
- **Preset (预置指令)**：Agent 的“元配置”。定义核心人格、全局 MCP 规范、输出约束（如 JSON 强制格式）及底层逻辑。
- **Chat (会话)**：由时间序排列的 Message 组成的上下文窗口（Context Window）。
- **LoreBook (知识书/规则书)**：**动态上下文注入机制**。
  - 触发式加载：当用户输入命中关键词或特定场景时，自动将相关 Prompt 片段注入 Preset 或当前 Context。
  - 用途：实现 Soft Skill 的按需加载，节省上下文 Token。
- **Character Card (角色卡)**：Agent 的逻辑实体。一个角色可挂载多个 LoreBook 和 Skill（包括子图形式的 Hard Skill），形成完备的能力画像。

---

## 3. 编程语言嵌入 (Template Engine)

为了实现 Prompt 的高度动态化与逻辑控制，引入插值脚本机制：

- **转义机制**：采用 `#{ }` 作为脚本引导符，实现从“静态文本模式”向“逻辑执行模式”的切换。
- **嵌入逻辑**：
  - **初始状态**：文本模式（Raw String）。
  - **执行状态**：遇到 `#{ script }` 时，解释器执行其中的代码（如条件判断、循环、变量取值）。
  - **渲染产物**：脚本执行的最终返回值将被序列化并替换回原文本位置。
- **实现方案**：需配备轻量级解释器/编译器，支持在 Prompt 渲染阶段实时处理业务逻辑。

## 4. tool/skill 的安全策略

| Mode                    | Config             | Behavior                              | Use Case                  |
| ----------------------- | ------------------ | ------------------------------------- | ------------------------- |
| 🤚 **Manual**           | `manual`           | All commands need confirmation        | Production, learning      |
| 🚫 **Blacklist Reject** | `blacklist_reject` | Auto-reject dangerous, confirm others | Development               |
| ⛔ **Universal Reject** | `universal_reject` | Auto-reject all commands              | Read-only scenarios       |
| ✅ **Whitelist Accept** | `whitelist_accept` | Auto-approve safe, reject dangerous   | Balanced automation       |
| 🟢 **Universal Accept** | `universal_accept` | Auto-approve everything ⚠️            | Trusted environments only |

为了安全可以再套一层容器/沙盒

## 5. 多agent协作

将“Graph”的概念从单体 Agent 内部的节点编排，上升到**多个 Character Card 之间的通信与调度**。

当引入多 Agent 协作时，Preset 的作用会发生分化，可以将其分为两个层次：

- 层次定义归属建议Global Preset全局协议（如 MCP 规范、协作消息格式、安全策略）。System/Environment (全局共享)
- Local Preset角色特有的逻辑（如：Orchestrator 的拆解逻辑，或 Worker 的执行细节）。

### 5.1. 协作的拓扑结构：

#### 5.1.1. 主从模式 (Orchestrator - Workers)

- **逻辑**：由一个 **Manager Agent** 担任中心节点，负责拆解任务（Decomposition），并调用其他 **Worker Agents** 执行具体 Skill。
- **实现**：Worker Agent 被封装为 Manager 的一个 **Hard Skill (Subgraph)**。
- **适用**：目标明确、流程复杂的任务。

#### 5.1.2. 接力模式 (Sequential Pipeline)

- **逻辑**：Agent A 完成阶段性产物后，通过 **Hard Route** 将 State 传递给 Agent B。
- **实现**：利用 **Graph** 的连线，将不同的 Character Card 挂载到不同的 Node 上。
- **适用**：翻译、代码审查、文案润色等线性流。

#### 5.1.3. 群聊模式 (Joint Collaboration / Peer-to-Peer)

- **逻辑**：多个 Agent 共享同一个 **Chat Context**。通过 **Soft Route** 决定谁是下一个发言者（Speaker Selection）。
- **实现**：在 Preset 中定义“发言规则”，并利用 LLM 路由决定控制权流转。
- **适用**：创意讨论、多角色模拟、复杂问题博弈。

群聊模式的权力分配决定了协作的有序性与涌现性，可细分为以下三种演进方案：

##### 5.1.3.1. 中心化：主持人模式 (Moderator)

决策主体：指定的 Host Agent。

运行逻辑：作为“中转站”过滤所有发言，行使指派权（谁发言）、审核权（纠错）与终止权（达成共识）。

实现层：在角色的 Local Preset 中注入会话管理逻辑。

特性：强确定性。有效防止幻觉导致的死循环或偏离目标。

##### 5.1.3.2. 去中心化：共识路由模式 (Consensus)

决策主体：当前发言节点。

运行逻辑：基于 Soft Route。Agent A 结束发言时，根据上下文意图自发产生 [Handover: Agent_B] 指令。

实现层：在 Global Preset 中标准化“交棒协议”字段。

特性：高动态性。适合多专家会诊、开放式创意脑暴。

##### 5.1.3.3. 环境化：系统调度模式 (Orchestrator)

决策主体：宿主环境/图引擎。

运行逻辑：脱离 Agent 主观意识。系统通过 #{ } 脚本引擎 监听 Chat Context 关键词或状态位，由 Edge 强制重定向。

实现层：逻辑硬编码于 Graph 的连线定义中，独立于角色之外。

特性：极致能效。节省 Token 消耗，适合标准 SOP 的强制流转。
