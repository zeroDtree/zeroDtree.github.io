---
title: windows + archlinux 双系统安装 大致流程
---

- [archlinux+windows 双系统安装“大致过程”与“注意事项”。](#archlinuxwindows-双系统安装大致过程与注意事项)
	- [1. 获取 arch 的 iso 文件，并将其刻录到 U 盘上(例如可使用 linux 的 dd 或ventoy)](#1-获取-arch-的-iso-文件并将其刻录到-u-盘上例如可使用-linux-的-dd-或ventoy)
	- [2. 关闭电脑的 bios 的安全启动，将 u 盘启动调整到最前面；把 u 盘插到电脑上；重启](#2-关闭电脑的-bios-的安全启动将-u-盘启动调整到最前面把-u-盘插到电脑上重启)
	- [3. 联网](#3-联网)
	- [4. 划分磁盘分区](#4-划分磁盘分区)
	- [5. 格式化磁盘分区（得到文件系统）](#5-格式化磁盘分区得到文件系统)
	- [6. 挂载文件系统](#6-挂载文件系统)
	- [7. 安装基本的内核以及固件，以及需要用到的软件](#7-安装基本的内核以及固件以及需要用到的软件)
	- [8. 生称文件分区挂载表](#8-生称文件分区挂载表)
	- [9. 使用 arch-chroot 进入到/mnt 里](#9-使用-arch-chroot-进入到mnt-里)
	- [10. 开启 os 探测](#10-开启-os-探测)
	- [11. 把 grub 引导项安装到 EFI 分区(/boot)](#11-把-grub-引导项安装到-efi-分区boot)
	- [12. 此时已安装好了 arch,但重启后没有 windows 的引导项。](#12-此时已安装好了-arch但重启后没有-windows-的引导项)
	- [13. 添加 windows 的引导项](#13-添加-windows-的引导项)
	- [14. 此时 archlinux+windows 双系统已经安装完成。](#14-此时-archlinuxwindows-双系统已经安装完成)
	- [15. 可选地，给 arch 安装 KDE 桌面](#15-可选地给-arch-安装-kde-桌面)

# archlinux+windows 双系统安装“大致过程”与“注意事项”。

## 1. 获取 arch 的 iso 文件，并将其刻录到 U 盘上(例如可使用 linux 的 dd 或[ventoy](https://www.ventoy.net/en/index.html))

刻录前要先将 U 盘格式化（FAT32，exFAT）

## 2. 关闭电脑的 bios 的安全启动，将 u 盘启动调整到最前面；把 u 盘插到电脑上；重启

此时会进入 archlinux 安装引导界面，按回车，一段时间按后会进入一个临时的 arch 操作系统。接下来要使用这个临时的操作系统来安装 archlinux

## 3. 联网

如果是笔记本的话，可以使用使用 iwctl 连接 wifi

## 4. 划分磁盘分区

现在一般都是 gpt(GUID Partition Table)分区, 使用 gdisk 进行磁盘分区划分

## 5. 格式化磁盘分区（得到文件系统）

使用 `mkfs.\*`，其中 EFI 分区要格式化为 FAT 格式（mkfs.fat -F 32 /device/path）

## 6. 挂载文件系统

将根文件系统挂载到/mnt
将 EFI 分区挂载到/mnt/boot

## 7. 安装基本的内核以及固件，以及需要用到的软件

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
2025.12.19: dhcpcd和networkmanager安装一个就行。好像。
```
用于编辑文件
pacstrap -K /mnt vim
```

## 8. 生称文件分区挂载表

genfstab -U /mnt >> /mnt/etc/fstab

## 9. 使用 arch-chroot 进入到/mnt 里

```
arch-chroot /mnt
```

## 10. 开启 os 探测

去掉“/ect/defalut/grub”里的“GRUB_DISABLE_OS_PROBER=false”这一行的注释即可

## 11. 把 grub 引导项安装到 EFI 分区(/boot)

```
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=Arch
grub-mkconfig -o /boot/grub/grub.cfg
```

## 12. 此时已安装好了 arch,但重启后没有 windows 的引导项。

重启后可以进入新安装的 arch
重新进入系统后记得打开 iwd,dhcpcd 服务。不开 dhcpcd 的话会分配不到 ip,不能下载东西。

## 13. 添加 windows 的引导项

1. 挂载 windows 的 EFI 分区
2. 再生成一下 grub 引导项目。

```
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=Arch
grub-mkconfig -o /boot/grub/grub.cfg
```

## 14. 此时 archlinux+windows 双系统已经安装完成。

## 15. 可选地，给 arch 安装 KDE 桌面

```
pacman -S --needed xorg sddm plasma kde-applications
systemctl enable sddm
```
