---
title: rsync
tags:
  - Linux
---

增量同步目录，只传有变化的部分。远程默认走 SSH。
```bash
rsync -avP /path/to/src/ /path/to/dest/
```
或
```bash
rsync -avPXH /path/to/src/ /path/to/dest/
```

<code style="color:#15803d">avPXH</code> 是命令里实际写的选项。`-a` 展开为 `-rlptgoD`。

| 选项 | 含义 |
| --- | --- |
| <code style="color:#15803d">-a</code> | 归档模式，即下面的 `-rlptgoD` |
| `-r` | 递归 |
| `-l` | 把符号链接复制为符号链接 |
| `-p` | 保留权限 |
| `-t` | 保留修改时间 |
| `-g` | 保留属组 |
| `-o` | 保留属主 |
| `-D` | 保留设备文件和特殊文件 |
| <code style="color:#15803d">-v</code> | 列出传输的文件 |
| <code style="color:#15803d">-P</code> | `--partial --progress`：中断后留下半成品，并显示单文件进度 |
| <code style="color:#15803d">-X</code> | 保留扩展属性 |
| <code style="color:#15803d">-H</code> | 保留硬链接 |

源路径末尾有没有 `/`，决定拷贝的是目录本身还是目录里的内容：

```bash
rsync -avPXH /path/to/src  /path/to/dest   # dest/src/...
rsync -avPXH /path/to/src/ /path/to/dest   # dest/...
```

远程把路径写成 `user@host:path`：

```bash
rsync -avPXH /path/to/src/ user@host:/path/to/dest/
```