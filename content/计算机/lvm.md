---
title: lvm记录
---

# Ubuntu 20.04 物理硬盘制作 LVM 逻辑卷记录

在 Linux 系统中，使用 LVM（Logical Volume Manager）可以让我们更灵活地管理磁盘空间。本文将记录如何将一块全新的（或需重置的）NVMe 固态硬盘制作成 LVM 卷并挂载使用。

## 1. 环境准备

- **操作系统**：Ubuntu 20.04.6 LTS
- **目标硬盘**：`/dev/nvme1n1` (容量：931.5G)
- **安装工具**：
  由于 Ubuntu 部分精简版未内置 LVM 管理工具，需先行安装：
  ```bash
  sudo apt update
  sudo apt install lvm2 -y
  ```

---

## 2. LVM 制作全过程

LVM 的构建遵循：**PV (物理卷) -> VG (卷组) -> LV (逻辑卷)** 的层级结构。

### 2.1.清理并创建物理卷 (PV)

如果硬盘之前有分区表（如 GPT 签名），`pvcreate` 会提示是否擦除，输入 `y` 确认。

```bash
# 1. 卸载可能已挂载的分区
sudo umount /dev/nvme1n1p1

# 2. 将整块盘初始化为物理卷
sudo pvcreate /dev/nvme1n1
```

### 2.2. 创建卷组 (VG)

卷组是一个资源池，将物理卷归纳进一个组内。

```bash
# 创建名为 vg_lvm 的卷组
sudo vgcreate vg_lvm /dev/nvme1n1
```

### 2.3. 创建逻辑卷 (LV)

从卷组资源池中划分空间。这里我们将 100% 的剩余空间都分配给名为 `lv_data` 的逻辑卷。

```bash
sudo lvcreate -l 100%FREE -n lv_data vg_lvm
```

### 2.4. 格式化逻辑卷

将创建好的逻辑卷格式化为 `ext4` 文件系统（也可以选择 `xfs`）。

```bash
sudo mkfs.ext4 /dev/vg_lvm/lv_data
```

---

## 3. 挂载与验证

### 3.1. 临时挂载

```bash
# 创建挂载点
sudo mkdir /data

# 执行挂载
sudo mount /dev/vg_lvm/lv_data /data/
```

### 3.2. 查看结果

使用 `lsblk` 命令可以看到清晰的树状结构，表示 `nvme1n1` 已经由 LVM 管理并成功挂载：

```text
NAME             MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
nvme1n1          259:4    0 931.5G  0 disk
└─vg_lvm-lv_data 253:0    0 931.5G  0 lvm  /data
```

---

## 4. 持久化挂载 (开机自动挂载)

为了防止系统重启后挂载失效，建议修改 `/etc/fstab`：

1.  查询逻辑卷的 **UUID**：
    ```bash
    sudo blkid /dev/vg_lvm/lv_data
    ```
2.  编辑 `/etc/fstab`：
    ```bash
    sudo nano /etc/fstab
    ```
3.  在文件末尾添加一行（替换为你自己的 UUID）：
    ```text
    UUID=xxxxxxxxxxxx  /data  ext4  defaults  0  2
    ```

## 5. 扩展存储：合并第二块硬盘

当需要增加现有挂载点容量时，可以动态加入新物理卷：

1. **清理并创建 PV**：
   `sudo wipefs -a /dev/sda`
   `sudo pvcreate /dev/sda`
2. **扩容卷组 (VG)**：
   `sudo vgextend vg_lvm /dev/sda`
3. **扩容逻辑卷 (LV)**：
   `sudo lvextend -l +100%FREE /dev/vg_lvm/lv_data`
4. **刷新文件系统**：
   `sudo resize2fs /dev/vg_lvm/lv_data`
