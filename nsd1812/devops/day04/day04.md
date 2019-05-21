# tedu_nsd1812_devops_day04

## Git

### 准备一台虚拟机，需要可以访问互联网

node3.tedu.cn: 连接到default NAT这个网络。default这个网络是KVM默认提供的，采用NAT方式允许连接到它上面的虚拟机访问互联网。

### 配置node3的网络

```shell
[root@localhost ~]# ifconfig virbr0 down
[root@localhost ~]# brctl delbr virbr0
[root@localhost ~]# ifdown eth0; ifup eth0
[root@localhost ~]# ping www.qq.com
```

配置node3的yum并安装git

```shell
[root@node3 ~]# vim /etc/yum.repos.d/server.repo
[server]
name=server
baseurl=ftp://192.168.122.1/centos7.4
gpgcheck=0
[root@node3 ~]# yum install -y git

```



### 

