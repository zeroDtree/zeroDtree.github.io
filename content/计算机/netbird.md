---
title: netbird 服务器搭建
---

本文记录在国内环境自建 netbird 服务端时遇到的几个问题与处理方式，便于日后对照排查。

## 官网教程

- https://github.com/netbirdio/netbird
- https://docs.netbird.io/selfhosted/selfhosted-quickstart

## 安装记录

环境与域名：

- 腾讯云虚拟机，系统为 debian 12
- 域名在 godaddy 注册

### 依赖与安装步骤

以下先按官方文档准备环境；官方 quick start 原文如下。

---

**Infrastructure requirements:**

- A Linux VM with at least **1CPU** and **2GB** of memory.
- The VM should be publicly accessible on TCP ports **80** and **443** and UDP port: **3478**.
- **Public domain** name pointing to the VM.

**Software requirements:**

- Docker installed on the VM with the docker-compose plugin ([Docker installation guide](https://docs.docker.com/engine/install/)) or docker with docker-compose in version 2 or higher.
- [jq](https://jqlang.github.io/jq/) installed. In most distributions
  Usually available in the official repositories and can be installed with `sudo apt install jq` or `sudo yum install jq`
- [curl](https://curl.se/) installed.
  Usually available in the official repositories and can be installed with `sudo apt install curl` or `sudo yum install curl`

**Steps**

- Download and run the installation script:

```bash
export NETBIRD_DOMAIN=netbird.example.com; curl -fsSL https://github.com/netbirdio/netbird/releases/latest/download/getting-started.sh | bash
```

- Once finished, you can manage the resources via `docker-compose`

---

### 执行完上述步骤后，当前目录会多出若干文件

```bash
root@VM-0-8-debian ~/p/netbird# ls
config.yaml  dashboard.env  docker-compose.yml
```

如果勾选了NetBird Proxy，会有两个额外的文件

```bash
root@VM-0-8-debian ~/p/netbird# ls
config.yaml  dashboard.env  docker-compose.yml proxy.env  traefik-dynamic.yaml
```

### 因无法拉取地理位置数据库而长时间卡住

安装脚本跑完最后一步时，终端可能出现类似下面的输出。

```bash
root@VM-0-8-debian ~/p/netbird# export NETBIRD_DOMAIN=netbird.example.com; curl -fsSL https://github.com/netbirdio/netbird/releases/latest/download/getting-started.sh | bash

Which reverse proxy will you use?
  [0] Traefik (recommended - automatic TLS, included in Docker Compose)
  [1] Existing Traefik (labels for external Traefik instance)
  [2] Nginx (generates config template)
  [3] Nginx Proxy Manager (generates config + instructions)
  [4] External Caddy (generates Caddyfile snippet)
  [5] Other/Manual (displays setup documentation)

Enter choice [0-5] (default: 0): 0

Enter your email for Let's Encrypt certificate notifications.
Email address: your_email@example.com

Do you want to enable the NetBird Proxy service?
The proxy allows you to selectively expose internal NetBird network resources
to the internet. You control which resources are exposed through the dashboard.
Enable proxy? [y/N]:
Rendering initial files...

Starting NetBird services

[+] up 6/6
 ✔ Network netbird_netbird                    Created                                                                                                                                                             0.0s
 ✔ Volume netbird_netbird_data                Created                                                                                                                                                             0.0s
 ✔ Volume netbird_netbird_traefik_letsencrypt Created                                                                                                                                                             0.0s
 ✔ Container netbird-server                   Started                                                                                                                                                             0.4s
 ✔ Container netbird-dashboard                Started                                                                                                                                                             0.3s
 ✔ Container netbird-traefik                  Started                                                                                                                                                             0.4s
Waiting for NetBird server to become ready . . . . .
```

此后脚本会长时间停在「等待服务就绪」一类提示上，若不加干预会一直等下去。

可按 `Ctrl+C` 结束脚本，再查看容器日志；常见原因是管理端在尝试下载 GeoLite2 城市库时网络不可达，从而阻塞启动。

```bash
root@VM-0-8-debian ~/p/netbird# docker compose up -d
[+] up 3/3
 ✔ Container netbird-traefik   Running                                                                                                                                                                            0.0s
 ✔ Container netbird-dashboard Running                                                                                                                                                                            0.0s
 ✔ Container netbird-server    Running                                                                                                                                                                            0.0s
root@VM-0-8-debian ~/p/netbird# docker logs -f netbird-server

# 日志的最后一行内容如下
2026-04-15T16:19:08.724Z INFO management/server/geolocation/database.go:34: Geolocation database file GeoLite2-City_20251217.mmdb not found, file will be downloaded
```

若环境无法下载 `GeoLite2-City_xxxxxxx.mmdb`，进程便会一直卡在这一步。

可行做法之一：通过环境变量关闭地理信息功能，避免启动时下载该文件。

在 `docker-compose.yml` 中为 `netbird-server` 服务引用独立环境文件，例如：

```yaml
netbird-server:
  image: netbirdio/netbird-server:latest
  container_name: netbird-server
  restart: unless-stopped
  env_file:
    - ./netbird-server.env
```

新建 `netbird-server.env`，内容如下。

```bash
NB_DISABLE_GEOLOCATION=true
```

### 为 Docker 网络固定名称

若未为软件栈中的网络显式指定名称，反向代理一侧的日志里可能出现与网络名相关的警告。

```bash
root@VM-0-8-debian ~/p/netbird# docker logs -f netbird-traefik
# ... 中间省略 ...
2026-04-15T16:25:02Z WRN Could not find network named "netbird" for container "/netbird-server". Maybe you're missing the project's prefix in the label? container=netbird-server-netbird-e7f2483fe882dbd144eb859bfbffdf9424a4da5f2f28b2d77a240d7c449324d6 providerName=docker serviceName=netbird-server
2026-04-15T16:25:02Z WRN Defaulting to first available network (&{"netbird_netbird" "172.30.0.3" '\x00' "" "37d0b08fa0ed5246b6bd4a36b17c15a4388132b8e940c47d09ae3a26c3456b12"}) for container "/netbird-server". container=netbird-server-netbird-e7f2483fe882dbd144eb859bfbffdf9424a4da5f2f28b2d77a240d7c449324d6 providerName=docker serviceName=netbird-server
```

在清空容器与数据卷并对照默认命名规则后可知：网络全名会带上项目前缀，前缀通常来自当前工作目录名（例如目录名为 `netbird` 时会出现 `netbird_netbird`）。

```bash
root@VM-0-8-debian ~/p/netbird# docker compose down --volumes # to remove all containers and volumes
[+] down 6/6
 ✔ Container netbird-dashboard                Removed                                                                                                                                                             3.4s
 ✔ Container netbird-server                   Removed                                                                                                                                                             0.3s
 ✔ Container netbird-traefik                  Removed                                                                                                                                                             0.3s
 ✔ Volume netbird_netbird_data                Removed                                                                                                                                                             0.0s
 ✔ Volume netbird_netbird_traefik_letsencrypt Removed                                                                                                                                                             0.0s
 ✔ Network netbird_netbird                    Removed                                                                                                                                                             0.2s
root@VM-0-8-debian ~/p/netbird#
```

在 `networks` 中为该网络设置固定 `name`，与 Traefik 标签里声明的网络名一致后，上述警告即可消除。

在 `docker-compose.yml` 的 `networks` 段中增加 `name: netbird`，例如：

```yaml
networks:
  netbird:
    name: netbird
    driver: bridge
    ipam:
      config:
        - subnet: 172.30.0.0/24
          gateway: 172.30.0.1
```

### 国外注册域名与证书申请失败

若域名在海外注册、解析，或受备案与注册商策略影响，从服务器侧访问证书校验所需端口时，链路可能被中间设备重置，安装日志中会出现证书申请失败一类报错。

```bash
root@VM-0-8-debian ~/p/netbird# docker logs -f netbird-traefik
# ... 中间省略 ...
*traefik.Provider 2026-04-15T11:16:26Z INF Starting provider *acme.ChallengeTLSALPN 2026-04-15T11:16:26Z INF Starting provider *docker.Provider 2026-04-15T11:16:26Z INF Starting provider *acme.Provider 2026-04-15T11:16:26Z INF Testing certificate renew... acmeCA=https://acme-v02.api.letsencrypt.org/directory providerName=letsencrypt.acme 2026-04-15T11:16:38Z ERR Unable to obtain ACME certificate for domains error="unable to generate a certificate for the domains [netbird.xxxxxx.com]: error: one or more domains had a problem:\n[netbird.xxxxxx.com] invalid authorization: acme: error: 400 :: urn:ietf:params:acme:error:connection :: x.x.x.x: Connection reset by peer\n" ACME CA=https://acme-v02.api.letsencrypt.org/directory acmeCA=https://acme-v02.api.letsencrypt.org/directory domains=["netbird.xxxxxx.com"] providerName=letsencrypt.acme routerName=netbird-dashboard@docker rule=Host(netbird.xxxxxx.com)
```

可行做法之一：改用基于 DNS 的校验方式，由境内云厂商在解析上自动写入临时校验记录。下文以腾讯云 DNS 为例。

在 `docker-compose.yml` 中调整其中反向代理服务的证书解析相关命令行参数，例如：

```yaml
services:
  # Traefik reverse proxy (automatic TLS via Let's Encrypt)
  traefik:
    image: traefik:v3.6
    container_name: netbird-traefik
    restart: unless-stopped
    env_file:
      - ./traefik.env
    networks:
      netbird:
        ipv4_address: 172.30.0.10
    command:
      # Logging
      - "--log.level=INFO"
      - "--accesslog=true"
      # Docker provider
      - "--providers.docker=true"
      - "--providers.docker.exposedbydefault=false"
      - "--providers.docker.network=netbird"
      # Entrypoints
      - "--entrypoints.web.address=:80"
      - "--entrypoints.websecure.address=:443"
      - "--entrypoints.websecure.allowACMEByPass=true"
      # Disable timeouts for long-lived gRPC streams
      - "--entrypoints.websecure.transport.respondingTimeouts.readTimeout=0"
      - "--entrypoints.websecure.transport.respondingTimeouts.writeTimeout=0"
      - "--entrypoints.websecure.transport.respondingTimeouts.idleTimeout=0"
      # HTTP to HTTPS redirect
      - "--entrypoints.web.http.redirections.entrypoint.to=websecure"
      - "--entrypoints.web.http.redirections.entrypoint.scheme=https"
      # Let's Encrypt ACME
      - "--certificatesresolvers.letsencrypt.acme.email=3186428803@qq.com"
      - "--certificatesresolvers.letsencrypt.acme.storage=/letsencrypt/acme.json"
        #- "--certificatesresolvers.letsencrypt.acme.httpchallenge=true"
        #- "--certificatesresolvers.letsencrypt.acme.httpchallenge.entrypoint=web"
        #- "--certificatesresolvers.letsencrypt.acme.tlschallenge=true"
      - "--certificatesresolvers.letsencrypt.acme.dnschallenge=true"
      - "--certificatesresolvers.letsencrypt.acme.dnschallenge.provider=tencentcloud"
      - "--certificatesresolvers.letsencrypt.acme.dnschallenge.resolvers=119.29.29.29:53"
      # - "--certificatesresolvers.letsencrypt.acme.dnschallenge.propagation.delayBeforeChecks=300"
      # gRPC transport settings
      - "--serverstransport.forwardingtimeouts.responseheadertimeout=0s"
      - "--serverstransport.forwardingtimeouts.idleconntimeout=0s"
```

其中 `119.29.29.29` 为腾讯云公共 DNS，用于校验前等待解析传播时查询权威记录。

新建 `traefik.env`，内容如下。

```bash
TENCENTCLOUD_SECRET_ID=xxxxxxxxxxxxx
TENCENTCLOUD_SECRET_KEY=xxxxxxxxxxxxxxxxx
```

其中 `TENCENTCLOUD_SECRET_ID` 与 `TENCENTCLOUD_SECRET_KEY` 为腾讯云 API 密钥（需具备操作 DNS 解析的权限）。

密钥在控制台申请：

```
https://console.cloud.tencent.com/cam/capi
```

DNSPod（解析）控制台：

```
https://console.cloud.tencent.com/cns
```

在 DNSPod 侧接管解析后，会得到两条由服务商分配的 NS，例如：

```
sarah.dnspod.net
bear.dnspod.net
```

最后在原域名注册商处，将域名的 NS 改为上述两条（本文域名购于 godaddy，在注册商后台修改 NS 即可）。

![[计算机/images/godday-nameserver.png]]

解析生效后，在 DNSPod 中为 netbird 所用主机名及需要的顶级记录添加 A 记录（按你实际规划填写即可）。

## 基本工作原理

- https://docs.netbird.io/about-netbird/how-netbird-works
