---
title: Docker
---

## docker pull 代理

```bash
sudo vim /etc/docker/daemon.json
在/etc/docker/daemon.json这个文件里添加形如下面的内容
{
  "proxies": {
    "http-proxy": "http://127.0.0.1:7890",
    "https-proxy": "http://127.0.0.1:7890",
    "no-proxy": "*.test.example.com,.example.org,127.0.0.0/8"
  }
}
```

```
参考资料：https://docs.docker.com/config/daemon/proxy/#daemon-configuration
```

## docker build 代理

```bash
--build-arg HTTP_PROXY=172.17.0.1:17890 --build-arg HTTPS_PROXY=172.17.0.1:17890
```

示例

```bash
docker build -f docker/Dockerfile -t alphafold . --build-arg HTTP_PROXY=172.17.0.1:17890 --build-arg HTTPS_PROXY=172.17.0.1:17890
```
