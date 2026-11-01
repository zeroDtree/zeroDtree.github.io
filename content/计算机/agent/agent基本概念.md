---
tags:
  - Agent
  - 大模型
---

## 核心概念

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