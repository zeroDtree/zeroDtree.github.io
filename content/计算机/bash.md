---
title: bash
---

## 参数拓展

### 赋值

```bash
${var:-word} → 如果 var 未设置或为空，使用 word

${var:=word} → 如果 var 未设置或为空，则赋值为 word

${var:+word} → 如果 var 已设置且非空，替换成 word

${var:?message} → 如果 var 未设置或为空，打印错误并退出脚本
```

### 替换

```bash
${var/pattern/replacement} → 替换第一个匹配

${var//pattern/replacement} → 替换所有匹配

${var/#pattern/replacement} → 前缀匹配替换

${var/%pattern/replacement} → 后缀匹配替换
```
