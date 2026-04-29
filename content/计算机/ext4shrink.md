---
title: ext4 缩容记录(测试)
---

# gpt+ext4 缩容测试

## 1. 启动容器并进入

```bash
docker build -t ext4test . -f ubuntu:22.04.dockerfile
docker run --name ext --privileged -it ext4test /bin/bash
```

---

dockerfile 的内容如下

```dockerfile
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN set -eux; \
    . /etc/os-release; \
    ARCH="$(dpkg --print-architecture)"; \
    if echo "$ARCH" | grep -Eq '^(arm64|armhf|ppc64el|riscv64|s390x)$'; then \
        TUNA_BASE='http://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports'; \
    else \
        TUNA_BASE='http://mirrors.tuna.tsinghua.edu.cn/ubuntu'; \
    fi; \
    printf '%s\n' \
      "deb $TUNA_BASE $VERSION_CODENAME main restricted universe multiverse" \
      "deb $TUNA_BASE $VERSION_CODENAME-updates main restricted universe multiverse" \
      "deb $TUNA_BASE $VERSION_CODENAME-backports main restricted universe multiverse" \
      "deb $TUNA_BASE $VERSION_CODENAME-security main restricted universe multiverse" \
      > /etc/apt/sources.list; \
    apt-get update -y; \
    apt-get install -y --no-install-recommends \
      e2fsprogs parted kpartx util-linux gdisk fish; \
    rm -rf /var/lib/apt/lists/*

RUN chsh -s /usr/bin/fish && mkdir /mnt/test
RUN dd if=/dev/zero of=/root/test.img bs=1M count=1024

```

---

## 2. 创建镜像并绑定 loop

```bash
set -euo pipefail

IMG=~/img
dd if=/dev/zero of="$IMG" bs=1M count=1024 status=progress
LOOP=$(losetup -f --show -P "$IMG")
echo "$LOOP"   # 例如 /dev/loop27
```

---

## 3. 建 GPT 分区（gdisk）

```bash
gdisk "$LOOP"
```

在 `gdisk` 里输入：

1. `n`（新建分区）
2. 分区号、起始、结束都回车（默认）
3. 类型回车（`8300`）
4. `w` 写盘并退出

刷新并创建分区映射：

```bash
partprobe "$LOOP" || true
partx -u "$LOOP" || true
kpartx -av "$LOOP"
PART=/dev/mapper/$(basename "$LOOP")p1
```

---

## 4. 格式化、挂载、写入数据

```bash
mkfs.ext4 -F "$PART"
mkdir -p /mnt/test
mount "$PART" /mnt/test

dd if=/dev/zero of=/mnt/test/haha bs=1M count=400 status=progress
ls -alh /mnt/test
df -h /mnt/test
```

---

## 5. 缩容（先文件系统，再分区）

```bash
umount /mnt/test
e2fsck -fy "$PART"
resize2fs "$PART" 800M
```

重建分区为约 `850M`（起始扇区保持不变）：

```bash
gdisk "$LOOP"
```

在 `gdisk` 里输入：

1. `d`（删 1 号分区）
2. `n`（新建 1 号分区）
3. 起始扇区回车（默认，通常是 `2048`）
4. 结束扇区输入 `+850M`
5. 类型回车（`8300`）
6. `w` 写盘退出

更新映射并验证：

```bash
kpartx -u "$LOOP"
mount "$PART" /mnt/test
df -h /mnt/test
ls -alh /mnt/test
```

---

## 6. 清理（可选）

```bash
umount /mnt/test || true
kpartx -d "$LOOP" || true
losetup -d "$LOOP" || true
```
