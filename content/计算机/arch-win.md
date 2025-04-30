---
title: windows + archlinux 双系统安装 大致流程
date: 2024-10-25 14:05:17
tags: archlinux
---

# archlinux+windows 双系统安装“大致过程”与“注意事项”。

## 获取 arch 的 iso 文件，并将其刻录到 U 盘上(例如可使用 linux 的 dd 或[ventoy](https://www.ventoy.net/en/index.html))

刻录前要先将 U 盘格式化（FAT32，exFAT）

## 关闭电脑的 bios 的安全启动，将 u 盘启动调整到最前面；把 u 盘插到电脑上；重启

此时会进入 archlinux 安装引导界面，按回车，一段时间按后会进入一个临时的 arch 操作系统。接下来要使用这个临时的操作系统来安装 archlinux

## 联网

如果是笔记本的话，可以使用使用 iwctl 连接 wifi

## 划分磁盘分区

现在一般都是 gpt(GUID Partition Table)分区, 使用 gdisk 进行磁盘分区划分

## 格式化磁盘分区（得到文件系统）

使用 `mkfs.\*`，其中 EFI 分区要格式化为 FAT 格式（mkfs.fat -F 32 /device/path）

## 挂载文件系统

将根文件系统挂载到/mnt
将 EFI 分区挂载到/mnt/boot

## 安装基本的内核以及固件，以及需要用到的软件

```
这三个包（base， linux， linux-firmware）是必须安装的
pacstrap -K /mnt base linux linux-firmware
```

```
grub和efibootmgr用于安装archlinux的启动项到EFI, os-prober用于探测原来的windows操作系统的引导项
pacstrap -K /mnt grub, efibootmgr, os-prober
```

```
iwd networkmanager用于新系统的联网，dhcpcd用于自动分配ip地址
pacstrap -K /mnt iwd networkmanager dhcpcd
```

```
用于编辑文件
pacstrap -K /mnt vim
```

## 生称文件分区挂载表

genfstab -U /mnt >> /mnt/etc/fstab

## 使用 arch-chroot 进入到/mnt 里

```
arch-chroot /mnt
```

## 开启 os 探测

去掉“/ect/defalut/grub”里的“GRUB_DISABLE_OS_PROBER=false”这一行的注释即可

## 把 grub 引导项安装到 EFI 分区(/boot)

```
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=Arch
grub-mkconfig -o /boot/grub/grub.cfg
```

## 此时已安装好了 arch,但重启后没有 windows 的引导项。

重启后可以进入新安装的 arch
重新进入系统后记得打开 iwd,dhcpcd 服务。不开 dhcpcd 的话会分配不到 ip,不能下载东西。

## 添加 windows 的引导项

1. 挂载 windows 的 EFI 分区
2. 再生成一下 grub 引导项目。

```
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=Arch
grub-mkconfig -o /boot/grub/grub.cfg
```

## 此时 archlinux+windows 双系统已经安装完成。

## 可选地，给 arch 安装 KDE 桌面

```
pacman -S --needed xorg sddm plasma kde-applications
systemctl enable sddm
```
