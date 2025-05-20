---
title: openvpn
---

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
