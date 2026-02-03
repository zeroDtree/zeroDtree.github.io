---
title: 安卓root 大致流程与注意事项
---

- [1. 解锁bootloader](#1-解锁bootloader)
- [2. 下载手机所对应的版本的 Fastboot ROM](#2-下载手机所对应的版本的-fastboot-rom)
- [3. 手机上下载Magisk](#3-手机上下载magisk)
- [4. 使用fastboot刷机](#4-使用fastboot刷机)

`红米k30 pro`手机，电脑为archlinux。

手机通过usb连接电脑，开启`文件传输`和`usb调试模式`

## 1. 解锁bootloader

## 2. 下载手机所对应的版本的 Fastboot ROM

搜索关键词：miui rom

下载的文件名可能为：`lmi_images_V14.0.4.0.SJKCNXM_20230417.0000.00_12.0_cn_c8619b5a5b.tgz`

解压，找到里面的`boot.img`文件，复制到手机的`Download`目录下

## 3. 手机上下载Magisk

使用Magisk修补`boot.img`, 将修补后的文件拷贝到电脑上

## 4. 使用fastboot刷机

关机，然后按电源键+减音键开机，进入fastboot模式

在电脑端输入：

```bash
zengls@archlinux ~> fastboot devices
99f55e6a         fastboot
zengls@archlinux ~> fastboot flash boot ~/Downloads/magisk_patched-30400_IvJh9.img
Sending 'boot' (131072 KB)                         OKAY [  2.760s]
Writing 'boot'                                     OKAY [  0.353s]
Finished. Total time: 3.127s
zengls@archlinux ~> fastboot reboot
Rebooting                                          OKAY [  0.001s]
Finished. Total time: 0.202s
```

重启完成后就root了。
