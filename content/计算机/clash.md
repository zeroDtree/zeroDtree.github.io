---
title: clash
---

## 针对问题：修改clash配置文件后，如果更新订阅，修改会被覆盖。

[在General面板]开启Mixin选项，

[在Settings面板]指定Minin类型为javascript，

然后添加js代码。操作`content`对象即可修改配置文件。

```js
module.exports.parse = ({ content, name, url }, { yaml, axios, notify }) => {
  content.rules.unshift("PROCESS-NAME,chrome,DIRECT", "PROCESS-NAME,qqmusic,DIRECT")
  return content
}
```
