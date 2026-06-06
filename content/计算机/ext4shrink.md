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

# gpt+ext4 缩容实践

```bash
yang@yang-Z690-AORUS-ELITE ~> lsblk
NAME             MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda                8:0    0   7.3T  0 disk
└─sda1             8:1    0   7.3T  0 part /media/yang/78855587-a2a3-4497-b95b-9e72c8845d2b
nvme0n1          259:0    0 931.5G  0 disk
├─nvme0n1p1      259:1    0   285M  0 part /boot/efi
├─nvme0n1p2      259:2    0  95.4G  0 part /
└─nvme0n1p3      259:3    0 835.9G  0 part /home
nvme1n1          259:4    0 931.5G  0 disk
└─vg_lvm-lv_data 253:0    0 931.5G  0 lvm  /data
yang@yang-Z690-AORUS-ELITE ~> sudo umount /media/yang/78855587-a2a3-4497-b95b-9e72c8845d2b
yang@yang-Z690-AORUS-ELITE ~> lsblk
NAME             MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda                8:0    0   7.3T  0 disk
└─sda1             8:1    0   7.3T  0 part
nvme0n1          259:0    0 931.5G  0 disk
├─nvme0n1p1      259:1    0   285M  0 part /boot/efi
├─nvme0n1p2      259:2    0  95.4G  0 part /
└─nvme0n1p3      259:3    0 835.9G  0 part /home
nvme1n1          259:4    0 931.5G  0 disk
└─vg_lvm-lv_data 253:0    0 931.5G  0 lvm  /data
yang@yang-Z690-AORUS-ELITE ~ [8]> sudo e2fsck -fy /dev/sda1
e2fsck 1.45.5 (07-Jan-2020)
第 1 遍：检查 inode、块，和大小
第 2 遍：检查目录结构
第 3 遍：检查目录连接性
第 4 遍：检查引用计数
第 5 遍：检查组概要信息
/dev/sda1：236557/244191232 文件（0.2% 为非连续的），168797375/1953506304 块
yang@yang-Z690-AORUS-ELITE ~> resize2fs /dev/sda1 4T
resize2fs 1.45.5 (07-Jan-2020)
open: 权限不够 打开 /dev/sda1 时
yang@yang-Z690-AORUS-ELITE ~ [1]> sudo resize2fs /dev/sda1 4T
resize2fs 1.45.5 (07-Jan-2020)
将 /dev/sda1 上的文件系统调整为 1073741824 个块（每块 4k）。
/dev/sda1 上的文件系统大小已经调整为 1073741824 个块（每块 4k）。
yang@yang-Z690-AORUS-ELITE ~> gdisk /dev/sda
GPT fdisk (gdisk) version 1.0.5
Problem opening /dev/sda for reading! Error is 13.
You must run this program as root or use sudo!
yang@yang-Z690-AORUS-ELITE ~> sudo gdisk /dev/sda
[sudo] yang 的密码：
GPT fdisk (gdisk) version 1.0.5

Partition table scan:
  MBR: protective
  BSD: not present
  APM: not present
  GPT: present

Found valid GPT with protective MBR; using GPT.

Command (? for help): p
Disk /dev/sda: 15628053168 sectors, 7.3 TiB
Model: ST8000NM017B-2TJ
Sector size (logical/physical): 512/4096 bytes
Disk identifier (GUID): 37F6F6DC-7210-486A-BBEC-7431EC451010
Partition table holds up to 128 entries
Main partition table begins at sector 2 and ends at sector 33
First usable sector is 34, last usable sector is 15628053134
Partitions will be aligned on 2048-sector boundaries
Total free space is 2669 sectors (1.3 MiB)

Number  Start (sector)    End (sector)  Size       Code  Name
   1            2048     15628052479   7.3 TiB     8300

Command (? for help): d
Using 1

Command (? for help): p
Disk /dev/sda: 15628053168 sectors, 7.3 TiB
Model: ST8000NM017B-2TJ
Sector size (logical/physical): 512/4096 bytes
Disk identifier (GUID): 37F6F6DC-7210-486A-BBEC-7431EC451010
Partition table holds up to 128 entries
Main partition table begins at sector 2 and ends at sector 33
First usable sector is 34, last usable sector is 15628053134
Partitions will be aligned on 2048-sector boundaries
Total free space is 15628053101 sectors (7.3 TiB)

Number  Start (sector)    End (sector)  Size       Code  Name

Command (? for help): n
Partition number (1-128, default 1):
First sector (34-15628053134, default = 2048) or {+-}size{KMGTP}:
Last sector (2048-15628053134, default = 15628053134) or {+-}size{KMGTP}: +5T
Current type is 8300 (Linux filesystem)
Hex code or GUID (L to show codes, Enter = 8300):
Changed type of partition to 'Linux filesystem'

Command (? for help): p
Disk /dev/sda: 15628053168 sectors, 7.3 TiB
Model: ST8000NM017B-2TJ
Sector size (logical/physical): 512/4096 bytes
Disk identifier (GUID): 37F6F6DC-7210-486A-BBEC-7431EC451010
Partition table holds up to 128 entries
Main partition table begins at sector 2 and ends at sector 33
First usable sector is 34, last usable sector is 15628053134
Partitions will be aligned on 2048-sector boundaries
Total free space is 4890634861 sectors (2.3 TiB)

Number  Start (sector)    End (sector)  Size       Code  Name
   1            2048     10737420287   5.0 TiB     8300  Linux filesystem

Command (? for help): w

Final checks complete. About to write GPT data. THIS WILL OVERWRITE EXISTING
PARTITIONS!!

Do you want to proceed? (Y/N): y
OK; writing new GUID partition table (GPT) to /dev/sda.
The operation has completed successfully.
yang@yang-Z690-AORUS-ELITE ~> lsblk
NAME             MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda                8:0    0   7.3T  0 disk
└─sda1             8:1    0     5T  0 part
nvme0n1          259:0    0 931.5G  0 disk
├─nvme0n1p1      259:1    0   285M  0 part /boot/efi
├─nvme0n1p2      259:2    0  95.4G  0 part /
└─nvme0n1p3      259:3    0 835.9G  0 part /home
nvme1n1          259:4    0 931.5G  0 disk
└─vg_lvm-lv_data 253:0    0 931.5G  0 lvm  /data
yang@yang-Z690-AORUS-ELITE ~ [1]> mkdir test
yang@yang-Z690-AORUS-ELITE ~> sudo mount /dev/sda1 test
yang@yang-Z690-AORUS-ELITE ~> cd test/
yang@yang-Z690-AORUS-ELITE ~/test> ls
lost+found/  work_dir/
yang@yang-Z690-AORUS-ELITE ~/test> df -h
df: /tmp/fuse: 传输端点尚未连接
文件系统                    容量  已用  可用 已用% 挂载点
udev                         63G     0   63G    0% /dev
tmpfs                        13G  2.2M   13G    1% /run
/dev/nvme0n1p2               94G   80G  8.9G   90% /
tmpfs                        63G     0   63G    0% /dev/shm
tmpfs                       5.0M  4.0K  5.0M    1% /run/lock
tmpfs                        63G     0   63G    0% /sys/fs/cgroup
/dev/nvme0n1p1              285M  6.1M  279M    3% /boot/efi
/dev/nvme0n1p3              822G  405G  376G   52% /home
tmpfs                        13G   72K   13G    1% /run/user/1000
/dev/mapper/vg_lvm-lv_data  916G  686G  184G   79% /data
tmpfs                        13G   28K   13G    1% /run/user/1001
tmpfs                        13G  4.0K   13G    1% /run/user/1002
tmpfs                        13G  4.0K   13G    1% /run/user/1003
tmpfs                        13G  4.0K   13G    1% /run/user/1004
tmpfs                        13G  4.0K   13G    1% /run/user/1005
/dev/sda1                   4.0T  585G  3.2T   16% /home/yang/test
yang@yang-Z690-AORUS-ELITE ~/test [1]>
```
