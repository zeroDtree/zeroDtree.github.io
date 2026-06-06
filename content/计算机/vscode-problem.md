---
title: vscode/cursor的一些问题
---

集成终端里按 Tab 补全时，VS Code/Cursor 内置终端补全与 fish 冲突，焦点会跑掉。关闭 accessibility 与终端 shell 集成、终端建议后可避免：

```json
{
  "editor.accessibilitySupport": "off",
  "terminal.integrated.shellIntegration.enabled": false,
  "terminal.integrated.shellIntegration.decorationsEnabled": "never",
  "terminal.integrated.suggest.enabled": false
}
```
