---
title: samba 网络磁盘
---

在 Arch Linux 上搭建 SMB 共享，供 macOS 通过 NetBird 虚拟网络挂载为网络磁盘。

## 1. 前提

- 服务端：Arch Linux，已安装 [NetBird](netbird.md) 并加入同一虚拟局域网
- 客户端：macOS
- 共享目录与 Samba 用户名需与下文配置中的 `path`、`valid users` 一致

## 2. 服务器端

### 2.1. 安装

```bash
yay -S samba
```

### 2.2. 准备共享目录与用户

创建共享目录并设置权限（将 `username` 替换为实际 Linux 用户名）：

```bash
sudo mkdir -p /path/to/netdisk
sudo chown username:username /path/to/netdisk
```

Samba 使用独立的密码库，需为 Linux 用户单独设置 SMB 密码：

```bash
sudo smbpasswd -a username
```

### 2.3. 修改配置

编辑 `/etc/samba/smb.conf`，内容如下：

```conf
[global]
    workgroup = WORKGROUP
    server string = ArchLinux NetBird NAS
    server role = standalone server

    disable netbios = yes
    dns proxy = no
    server min protocol = SMB2_10
    server smb encrypt = desired
    deadtime = 30

    logging = systemd
    max log size = 50

    ea support = yes
    vfs objects = fruit streams_xattr
    fruit:metadata = stream
    fruit:model = Macmini
    fruit:posix_metadata = yes
    fruit:veto_appledouble = no
    fruit:copyfile = yes
    aio read size = 1
    aio write size = 1

    use sendfile = yes
    min receivefile size = 16384

    load printers = no
    printing = bsd
    printcap name = /dev/null
    disable spoolss = yes
    show add printer wizard = no

[NetBirdDisk]
    comment = My Remote NetDisk
    path = /path/to/netdisk
    browseable = yes
    writable = yes
    read only = no
    guest ok = no
    valid users = username
    create mask = 0644
    directory mask = 0755
```

检查语法是否正确：

```bash
testparm
```

### 2.4. 启动服务

```bash
sudo systemctl enable smb
sudo systemctl start smb
```

## 3. 客户端

### 3.1. macOS 连接

1. 确认 Mac 已连接 NetBird，并记下 Arch 主机在虚拟局域网中的 IP（如 `100.x.x.x`）
2. 打开 Finder → **前往** → **连接服务器**（或 `⌘K`）
3. 输入 `smb://100.x.x.x/NetBirdDisk`，点击连接
4. 使用上一步 `smbpasswd` 设置的 **username** 与密码登录
