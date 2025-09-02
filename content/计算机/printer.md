---
title: 打印机使用
---

打印机使用 （不知其所以然版）

在archlinux上使用局域网内windows共享的打印机

## 安装和使用流程

#### 安装、启用、启动cups服务

```bash
yay -S cups cups-pdf
sudo systemctl enable cups.service
sudo systemctl start cups.service
```

#### 再安装一个KDE的系统printer设置里提示安装的一个软件包。

```bash
yay -S system-config-printer
```

#### 安装avahi ,用来发现局域网内的打印机.

如果不安装这个包的话，就得手动输入windows的ip地址，如果windows没有固定ip的话，每次都需要重新输入ip地址。

```bash
yay -S avahi nss-mdns
sudo systemctl enable avahi-daemon.service
sudo systemctl start avahi-daemon.service
```

Avahi provides local hostname resolution using a `hostname.local` naming scheme.  
To enable it, install the `nss-mdns` package and start/enable `avahi-daemon.service`

Then, edit the file `/etc/nsswitch.conf` and change the hosts line to include `mdns_minimal [NOTFOUND=return]` before `resolve` and `dns`:

```bash
zengls@archlinux ~> cat /etc/nsswitch.conf|grep host
hosts: mymachines mdns_minimal [NOTFOUND=return] resolve [!UNAVAIL=return] files myhostname dns
```

#### 探测局域网内的打印机

```bash
sudo lpinfo --include-schemes dnssd -v
```

输入完上面命令后，会输出局域网内的可用的打印机设备。
形如：

```bash
zengls@archlinux ~> sudo lpinfo --include-schemes dnssd -v
network dnssd://HP%20LaserJet%20Pro%20MFP%203101-3108%20%5B469DA2%5D._ipp._tcp.local/?uuid=xxxxxxxxxxxxxxxx
```

#### 添加打印机

```bash
sudo lpadmin -p printer_name -v "dnssd://HP%20LaserJet%20Pro%20MFP%203101-3108%20%5B469DA2%5D._ipp._tcp.local/?uuid=xxxxxxxxxxxxxxxx" -m everywhere -E
```

## 参考资料

```
https://wiki.archlinux.org/title/CUPS
https://wiki.archlinux.org/title/Avahi
```
