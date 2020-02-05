# NSD1909_DEVWEB_DAY04

## 注意：有问题，在群中直接找项目经理

### 今日内容：

1. 介绍vmware虚拟机的使用
2. 配置环境
3. django

## 配置环境

```shell
# 安装python
[root@localhost ~]# tar xf zzg_pypkgs.tar.gz
[root@localhost ~]# cd zzg_pypkgs/
[root@localhost ~]# cd python3_pkg/
[root@localhost ~]# vim README
yum install -y sqlite-devel tk-devel tcl-devel readline-devel zlib-devel gcc gcc-c++ openssl-devel libffi-devel
tar xzf Python-3.6.7.tgz
cd Python-3.6.7
./configure --prefix=/usr/local/
make && make install
[root@localhost ~]# bash README

# 实现按tab键补全功能：https://www.jianshu.com/p/b83a803cfc86

# 创建虚拟环境
[root@localhost ~]# python3 -m venv ~/nsd1908

# 激活虚拟环境，并安装相应的软件包
[root@localhost ~]# source ~/nsd1908/bin/activate
(nsd1908) [root@localhost ~]# pip install django==
(nsd1908) [root@localhost ~]# pip install django==1.11.6
(nsd1908) [root@localhost ~]# pip install pymysql
```

## pycharm配置

```shell
# 配置pycharm。注意：需要java
(nsd1908) [root@localhost cloud5]# mkdir ~/bin
(nsd1908) [root@localhost cloud5]# tar xf pycharm2017.tar.gz -C ~/bin/

# 打开一个新的终端，运行破解工具
[root@localhost ~]# /root/bin/crack &

# 配置菜单，在菜单中添加pycharm
[root@localhost bin]# yum install -y alacarte
# 应用程序->杂项->主菜单
# 选择“主菜单”窗口中的 应用程序->编程，在右窗格点“新建项目”
# Name: PyCharm2017   Command: /root/bin/pycharm2017/bin/pycharm.sh
# 点击图标，更换为：/root/bin/pycharm2017/bin/pycharm.png

# 启动pycharm2017后，激活时，Lisence Server为http://127.0.0.1:1017
```



















