---
title: netbird reverse proxy
---

## 前置

- [[计算机/netbird]]

---

利用 **NetBird 官方自建管理后台 + 专属反向代理（Reverse Proxy）容器**，配合二级泛域名，打造一套**完全免费、全自动申请 Let's Encrypt 证书**的内网穿透架构。

## 架构拓扑一览

```mermaid
flowchart LR
    A["公网用户"]
    B["HTTPS :443<br/>泛域名 *.rp.example.com"]
    C["云服务器<br/>Traefik 网关 / NetBird Proxy 容器"]
    D["NetBird WireGuard<br/>虚拟内网 100.64.0.0/10"]
    E["局域网服务器<br/>（内网服务）"]

    A --> B --> C --> D --> E
```

---

## DNS 泛解析配置

为了让所有二级子域名（如 `nas.rp...`、`web.rp...`）都能正确找到我们的云服务器网关，我们需要在域名解析后台做两件事：

1. **A 记录：** 将基准子域名 `rp.example.com` 指向你的云服务器公网 IP。
2. **CNAME 记录：** 将泛域名 `*.rp` 指向 `rp.example.com`。

| 主机记录 | 记录类型 | 记录值           |
| -------- | -------- | ---------------- |
| `rp`     | A        | `你的云服务器IP` |
| `*.rp`   | CNAME    | `rp.example.com` |

---

## 云服务器端部署（Docker Compose）

在云服务器的 `docker-compose.yml` 中，将 `proxy` 服务紧贴在 `services` 节点下。**注意缩进**，它需要与 `netbird-server` 平级：

```yaml
services:
  netbird-server:
    image: netbirdio/netbird-server:latest
    # ... 原有配置 ...

  # 保持两个空格缩进，加入代理容器
  proxy:
    image: netbirdio/reverse-proxy:latest
    container_name: netbird-proxy
    restart: unless-stopped
    networks: [netbird]
    depends_on:
      - netbird-server
    env_file:
      - ./proxy.env
    volumes:
      - netbird_proxy_certs:/certs
    labels:
      - traefik.enable=true
      - traefik.tcp.routers.proxy-passthrough.entrypoints=websecure
      - traefik.tcp.routers.proxy-passthrough.rule=HostSNI(`*`)
      - traefik.tcp.routers.proxy-passthrough.tls.passthrough=true
      - traefik.tcp.routers.proxy-passthrough.service=proxy-tls
      - traefik.tcp.routers.proxy-passthrough.priority=1
      - traefik.tcp.services.proxy-tls.loadbalancer.server.port=8443

volumes:
  netbird_proxy_certs:
```

## 生成 Proxy 专用 Token

在部署代理容器之前，我们需要先为它颁发一张“通行证”（Token），让它有权限与你的自建 NetBird Server 进行安全的配置同步。

由于是在自建环境下，最快捷、最安全的方式是**直接在云服务器终端通过容器命令行生成**：

1. 在服务器上，确保你的 `netbird-server` 容器正在运行。
2. 在终端执行以下命令（注意将路径替换为你实际的配置文件挂载路径，通常合一版镜像在容器内的路径为 `/etc/netbird/config.yaml`）：

```bash
docker exec -it netbird-server /go/bin/netbird-server token create --name "my-proxy" --config /etc/netbird/config.yaml
```

## `proxy.env` 环境变量配置

由于国内服务器访问 NetBird 官方 GeoIP 地理位置源经常发生超时（`context deadline exceeded`），如果你追求**完全对公网匿名公开**，强烈建议在配置文件中通过 `NB_PROXY_DISABLE_GEOLOCATION=true` 彻底关闭检测，既能规避报错，又能提升连接响应速度：

```ini
NB_PROXY_DOMAIN=rp.example.com
NB_PROXY_TOKEN=你的Proxy专用Token
NB_PROXY_MANAGEMENT_ADDRESS=http://netbird-server:80
NB_PROXY_ALLOW_INSECURE=true
NB_PROXY_ADDRESS=:8443
NB_PROXY_ACME_CERTIFICATES=true
NB_PROXY_ACME_CHALLENGE_TYPE=tls-alpn-01
NB_PROXY_CERTIFICATE_DIRECTORY=/certs
NB_PROXY_DISABLE_GEOLOCATION=true

```

配置完成后，使用 `docker compose config` 检查一下语法，无误后启动服务：

```bash
docker compose up -d proxy
```

通过 `docker compose logs -f proxy` 查看，当出现 `Initial mapping sync complete` 时，代表已成功。

---

之后在后台图形界面根据提示操作即可。
