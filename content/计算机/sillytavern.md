---
title: SillyTavern
---

- [工作原理](#工作原理)
- [SillyTavern 的`Conversation`的组织方式](#sillytavern-的conversation的组织方式)

以下以`Chat Completion` API 为例。

## 工作原理

`LLM` 接受`Prompt`(字符串)，生成`Response`(字符串)。

用户向 `LLM` 发送请求，`LLM` 返回响应。请求和响应的组成的交替序列，称为`Conversation`，请求和响应被统称为`Message`。

`Message`的格式为：

```json
{
	"role": "角色",
	"content": "内容"
}
```

`role`一共有三种：

- `system`：系统角色，用于设置`LLM`的工作方式。对应的`Message`称为`System Message`（系统消息）。
- `user`：用户角色，用于向`LLM`发送请求。对应的`Message`称为`User Message`（用户消息）。
- `assistant`：助手角色，用于向`LLM`发送响应。对应的`Message`称为`Assistant Message`（助手消息）。

`Conversation`的所有`Message`都会被转化成字符串，然后被拼接到一起，作为`LLM`的`Prompt`。

这个`Prompt`是最终输入到`LLM`的里的东西。

`Chat Completion` API (或更一般的 `LLM` 的 API) 没有持久化记忆功能，记忆完全由`Prompt`决定。

因此用户可以虚构`Prompt`(即虚构`Conversation`)，来实现记忆功能。

SillyTavern 的主要作用之一就是帮助用户虚构`Prompt`。

## SillyTavern 的`Conversation`的组织方式

```json
{
  messages: [
    {
      role: 'system',
      content: "Write 虚拟角色's next reply in a fictional chat between 虚拟角色 and 小明."
    },
    {
      role: 'user',
      content: '[世界书条目Position: Before Char Def]\n' +
        '\n' +
        '角色定义：小明的好朋友\n' +
        '\n' +
        '[世界书条目Position: After Char Def]\n' +
        '\n' +
        '[Start a new Chat]\n' +
        '\n' +
        '[世界书条目Position: at System depth:200]'
    },
    {
      role: 'assistant',
      content: '[世界书条目Position: at Assistant, depth:100]'
    },
    {
      role: 'user',
      content: '[世界书条目Position: at User, depth:100]\n' +
        '\n' +
        '[世界书条目Position: at System depth:100]'
    },
    {
      role: 'assistant',
      content: '[世界书条目Position: at Assistant， depth: 50]\n\n角色的第一条消息：你好'
    },
    {
      role: 'user',
      content: '[世界书条目Position: at System depth:1]\n' +
        '\n' +
        '最近如何\n' +
        '\n' +
        '[世界书条目Position: at System depth:0]'
    }
  ]
}
```

观察上述例子可得到以下结论

- 第一条消息总是系统消息。然后是虚拟角色定义及其定义前后的世界书条目（Before Char Def，虚拟角色定义，After Char Def）。
- 世界书里的系统条目会被转化为用户消息。
- `depth`逻辑上相邻的属于同一角色的`Message`会被拼接到一起。
- `depth`越小，`Message`越靠近最新的消息。
- `depth`相同的`Message`会根据`role`的排列(优先级：系统消息>用户消息>助手消息)，优先级越大，`Message`越靠近最新的消息。
- 用户的最新一条消息处于 depth=0 和 1 之间。
