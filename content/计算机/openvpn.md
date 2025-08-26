---
title: openvpn
---

- [openvpn 工作原理图](#openvpn-工作原理图)
- [openvpn 安装流程(for archlinux)](#openvpn-安装流程for-archlinux)
	- [easy-rsa 安装](#easy-rsa-安装)
	- [服务器端 openvpn 安装](#服务器端-openvpn-安装)
	- [证书拷贝](#证书拷贝)
	- [openvpn 服务器端配置文件](#openvpn-服务器端配置文件)
	- [openvpn 安装配置客户端配置文件](#openvpn-安装配置客户端配置文件)
- [openvpn 内网客户端互通](#openvpn-内网客户端互通)
- [固定客户端的内网ip](#固定客户端的内网ip)

## openvpn 工作原理图

![[计算机/images/openvpn.png]]

## openvpn 安装流程(for archlinux)

假设在机器$a$上生成和签发密钥，在服务器$\gamma$上安装openvpn，在机器$b$上安装openvpn客户端。

以下使用easy-rsa生成openvpn所需的证书和密钥

### easy-rsa 安装

(在机器$a$上)下载安装easy-rsa

```bash
yay -S easy-rsa
```

生成和签发证书

```bash
easyrsa init-pki
easyrsa build-ca
easyrsa gen-req server nopass
easyrsa sign-req server server
easyrsa gen-req client nopass
easyrsa sign-req client client
easyrsa gen-dh
cd pki
openvpn --genkey secret ta.key
```

需要关注的、被生成的证书和密钥的目录结构为

```
pki:
ca.crt  dh.pem  issued  reqs  ta.key  private

pki/issued:
client.crt  server.crt

pki/private:
ca.key  client.key  server.key

pki/reqs:
client.req  server.req
```

### 服务器端 openvpn 安装

(在服务器$\gamma$上)下载安装openvpn

```bash
yay -S openvpn
```

### 证书拷贝

在机器$a$上将生成的证书和密钥拷贝到服务器$\gamma$上

```bash
cd pki
scp ca.crt dh.pem issued/server.crt private/server.key ta.key {username}@{server_ip}:/etc/openvpn/server/
```

### openvpn 服务器端配置文件

(在服务器$\gamma$上)

默认安装openvpn后会有一个配置文件样例，不同电脑样例位置可能不一样，但相信你能找到的。

```bash
cp /usr/share/doc/openvpn/examples/sample-config-files/server.conf /etc/openvpn/
```

根据需要改写里面的配置文件即可。

启动openvpn

```bash
systemctl enable openvpn@server
systemctl start openvpn@server
```

### openvpn 安装配置客户端配置文件

(在机器$b$上)与服务器端类似，下载安装openvpn，并拷贝证书和密钥，根据需要改写配置文件。

## openvpn 内网客户端互通

在服务器$\gamma$上，将openvpn服务器端配置文件里的`client-to-client`取消注释

server.conf

```
# Uncomment this directive to allow different
# clients to be able to "see" each other.
# By default, clients will only see the server.
# To force clients to only see the server, you
# will also need to appropriately firewall the
# server's TUN/TAP interface.
client-to-client
```

## 固定客户端的内网ip

把openvpn的网络拓扑改成子网模式。
然后创建一个目录ccd,对每个客户端进行单独配置。

server.conf

```
# Network topology
# Should be subnet (addressing via IP)
# unless Windows clients v2.0.9 and lower have to
# be supported (then net30, i.e. a /30 per client)
# Defaults to net30 (not recommended)
topology subnet

client-config-dir ccd

# EXAMPLE: Suppose you want to give
# Thelonious a fixed VPN IP address of 10.11.0.100.
# First uncomment out these lines:
client-config-dir ccd
# route 10.11.0.0 255.255.255.0
# Then add this line to ccd/Thelonious:
#   ifconfig-push 10.11.0.100 255.255.255.0
```

ccd/Thelonious

```
ifconfig-push 10.11.0.100 255.255.255.0
```
注意：这个客户端名需要和easy-rsa里的客户端证书名一样。