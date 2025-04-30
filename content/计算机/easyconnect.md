---
title: docker，proxychains，easyconnect， FreeFileSync
date: 2024-06-27 14:05:17
tags: vpn
---

# docker deamon 代理 + docker封印easyconnect + proxychains使用easyconnect+ FreeFileSync使用easyconnect 的代理

使用github上的一个项目：
```
https://github.com/docker-easyconnect/docker-easyconnect
```
1. 2024年docker好像被禁了，首先需要给docker deamon配置一下梯子
```bash
sudo vim /etc/docker/daemon.json
在/etc/docker/daemon.json这个文件里添加形如下面的内容
{
  "proxies": {
    "http-proxy": "http://127.0.0.1:7890",
    "https-proxy": "http://127.0.0.1:7890",
    "no-proxy": "*.test.example.com,.example.org,127.0.0.0/8"
  }
}
```
```
参考资料：https://docs.docker.com/config/daemon/proxy/#daemon-configuration
```
2. docker pull 适合你的easyconnect版本的image</br>
3. 执行下面这个脚本(不妨命名为vpn.sh)，然后给vpn.sh 添加可执行权限，运行vpn.sh, 就可以创建easyconnect的container，这个container是临时的，程序结束（例如CRTL-C）后会自动删除容器。
```bash
container_name="docker-easyconnect"
vpn_server="xx.xx.xx.xx"
username="your user name"
passwd="your password"
EC_VER="7.6.3"
sudo docker run --name ${container_name} --rm --device /dev/net/tun --cap-add NET_ADMIN -ti -p 127.0.0.1:1080:1080 -p 127.0.0.1:8888:8888 -e EC_VER=${EC_VER} -e CLI_OPTS="-d${vpn_server} -u ${username} -p ${passwd}" hagb/docker-easyconnect:cli
```
```
参考资料：https://github.com/docker-easyconnect/docker-easyconnect 这个项目的README.md
```

# 现在已经可以通过 127.0.0.1:1080、127.0.0.1:8888 分别访问 socks5 和 http 代理了。

例如ssh登陆虚拟局域网主机，可以使用proxychains强制给ssh设置代理，到端口1080
```
proxxychains -f  your_proxychains_config_file ssh user@desthost
```
your_proxychains_config_file的内容（形）如下：
```
tcp_read_time_out 15000
tcp_connect_time_out 8000
[ProxyList]
socks5  127.0.0.1 1080
```
1. 这里我整理成了一个脚本，内容如下
```
username=your_user_name
host=your_host_addr
conf_path=/path/to/your/proxychains.conf
proxychains -f ${conf_path} ssh ${username}@${host}
```
1. FreeFileSync如何使用easyconnect的代理呢?

可以使用proxychains强制FreeFileSync 使用easyconnect的代理，编辑FreeFileSync的.desktop文件.
```
➜  ~ cat .local/share/applications/FreeFileSync.desktop 
[Desktop Entry]
Categories=Utility;FileTools;Archiving;
Exec=proxychains -q -f /home/zengls/conf/proxychains.conf /opt/FreeFileSync/FreeFileSync %F
Icon=/opt/FreeFileSync/Resources/FreeFileSync.png
MimeType=application/x-freefilesync-gui;application/x-freefilesync-batch;
Name[en_US]=FreeFileSync
Name=FreeFileSync
StartupNotify=true
Terminal=false
Type=Application
X-KDE-SubstituteUID=false
```
注意“-q”参数是必要的，否则proxychains的输出会影响“FreeFileSync判断本机操作系统”，导致无法打开FreeFileSync