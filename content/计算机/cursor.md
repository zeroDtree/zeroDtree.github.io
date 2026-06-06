---
title: cursor
---

## cursor无法使用 Claude 模型

### 方案一：开启 TUN 模式

在 Clash 中开启 TUN 模式，使流量经由虚拟网卡全局代理。

### 方案二：配置代理设置

在 `settings.json` 中添加以下配置：

```json
{
  "http.proxy": "http://127.0.0.1:7890",
  "http.proxySupport": "override",
  "http.proxyStrictSSL": false,
  "http.noProxy": ["localhost", "127.0.0.1"],
  "cursor.general.disableHttp2": true
}
```
