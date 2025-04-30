---
title: archlinux-kde 中文与中文输入 大致流程
date: 2024-10-25 14:05:17
tags: archlinux
---

# archlinux-kde 中文与中文输入

最终结果：终端可以{显示，输入}中文但不把英文翻译成中文

1. 编辑“etc/locale.gen”

```
去掉“en_US.UTF-8”那一行的注释
去掉“zh_CN.UTF-8”那一行的注释
```

2. 执行 locale-gen

```
locale-gen
```

3. 编辑".bashrc"或“.zshrc”文件，添加一行

```
export LANG=en_US.UTF-8
```

4. 安装中文字体

```
yay -S 	adobe-source-han-sans-cn-fonts
```

## 到这里可以就可以正常显示中文了，但还无法输入中文

5. 安装输入框架 fcitx5

```
yay -S fcitx5-im
```

6. 安装 fcitx5 的中文支持

```
yay -S fcitx5-chinese-addons
```

7. 添加 fcitx 的配置，在配置文件“/etc/environment”中添加几行

```
GTK_IM_MODULE=fcitx
QT_IM_MODULE=fcitx
XMODIFIERS=@im=fcitx
SDL_IM_MODULE=fcitx
GLFW_IM_MODULE=ibus
```

8. 在设置中添加拼音输入法

ctrl-space 就可以切换输入法了

## 参考资料：

```
https://wiki.archlinux.org/title/Localization/Simplified_Chinese
https://wiki.archlinux.org/title/Fcitx5#Input_method_module
https://wiki.archlinux.org/title/Input_method#List_of_available_input_method_editors

```
