# 内网穿透

- [内网穿透](#内网穿透)
	- [1. 符号约定与目标](#1-符号约定与目标)
	- [2. frp(fast reverse proxy)](#2-frpfast-reverse-proxy)
		- [2.1. frp工作原理](#21-frp工作原理)
	- [3. zerotier](#3-zerotier)

## 1. 符号约定与目标

- 局域网用大写字母表示，如$A$,$B$,$C$

- 局域网中的主机用小写字母表示，如$a$,$b$,$c$ 分别位于局域网$A$,$B$,$C$

- 公网ip用希腊字母表示，例如$\alpha$,$\gamma$,$\beta$

- 同一个局域网中的主机用小写字母后的数字区分，如$a1$,$a2$,$a5$ 位于局域网A.

目标：利用$\gamma$使得$b$能被$a$访问

## 2. frp(fast reverse proxy)

[github](https://github.com/fatedier/frp)

```
https://github.com/fatedier/frp
```

用法见[example](https://gofrp.org/zh-cn/docs/)

```
https://gofrp.org/zh-cn/docs/
```

### 2.1. frp工作原理

FRP 主要由 frps（服务端） 和 frpc（客户端） 两部分组成：

frps（Server）: 部署在(具有公网 IP 的服务器)$\gamma$上，负责接收客户端连接，并将外部请求转发给 frpc。

frpc（Client）: 部署在(内网机器)$b$上，主动连接 frps，并建立一条 TCP 隧道，让公网流量可以访问本地服务。

$b$上的frpc 启动时，主动连接 $\gamma$上的frps 的 bindPort（默认为7000），$b$上的frpc 通过该端口与 frps 建立持久化的 TCP 控制通道，用于心跳检测和端口映射管理。

$b$上的frpc 根据配置文件 frpc.toml，向 $\gamma$上的frps 注册代理（proxy），声明需要映射的端口（例如 SSH 端口 22）。

$\gamma$上的frps 记录这个代理信息，并在 remotePort(例如6000) 上监听来自外部的连接。

外部机器 $a$ 通过 ssh -oPort=6000 test@$\gamma$.ip 访问 $\gamma$的 的remotePort端口。

$\gamma$上的frps 发现这个端口已被映射至 frpc 代理的 localPort = 22，于是将该连接转发到$b$上的frpc。

$b$上的frpc 收到 frps 转发的 SSH 请求后，将数据包转发到 localIP(127.0.0.1) 和 localPort(22)，从而完成 SSH 连接。

## 3. zerotier

[官网](https://www.zerotier.com/)

```
https://www.zerotier.com/
```

[github]()

```
https://github.com/zerotier/ZeroTierOne
```

用法见[archlinux-wiki-zerotier](https://wiki.archlinux.org/title/ZeroTier)

```
https://wiki.archlinux.org/title/ZeroTier
```
