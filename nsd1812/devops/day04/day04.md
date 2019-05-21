# tedu_nsd1812_devops_day04

## Git

### 准备一台虚拟机，需要可以访问互联网

假设node3是程序员的个人电脑，在这台机器上编写代码。

node3.tedu.cn: 连接到default NAT这个网络。default这个网络是KVM默认提供的，采用NAT方式允许连接到它上面的虚拟机访问互联网。

### 配置node3的网络

```shell
[root@localhost ~]# ifconfig virbr0 down
[root@localhost ~]# brctl delbr virbr0
[root@localhost ~]# ifdown eth0; ifup eth0
[root@localhost ~]# ping www.qq.com
```

### 配置node3的yum并安装git

```shell
[root@node3 ~]# vim /etc/yum.repos.d/server.repo
[server]
name=server
baseurl=ftp://192.168.122.1/centos7.4
gpgcheck=0
[root@node3 ~]# yum install -y git
```

配置git基本参数

```shell
[root@node3 ~]# git config --global user.name 'zzg'
[root@node3 ~]# git config --global user.email 'zzg@tedu.cn'
[root@node3 ~]# git config --global core.editor vim
[root@node3 ~]# git config --list
user.name=zzg
user.email=zzg@tedu.cn
core.editor=vim
[root@node3 ~]# cat ~/.gitconfig 
[user]
	name = zzg
	email = zzg@tedu.cn
[core]
	editor = vim
```

### git重要的概念

- 工作区：编写程序时，创建一个目录，把程序文件全都放在该目录下，这个目录就是工作区
- 暂存区：工作区和版本库之间的缓冲地带
- 版本库：git在工作区中创建一个隐藏目录.git，这个目录是版本库，它在工作区下，但是不是工作区的一部分。

```mermaid
graph LR
work(工作区)
cache(暂存区)
ver(版本库)
work--提交-->cache
cache--确认-->ver
```

## 初始化

- 新建项目时已经计划使用git

```shell
[root@node3 ~]# git init myproject
初始化空的 Git 版本库于 /root/myproject/.git/
[root@node3 ~]# ls -A myproject/
.git
```

- 在已经存在的项目中使用git

```shell
[root@node3 ~]# mkdir devops
[root@node3 ~]# cd devops/
[root@node3 devops]# echo '<h1>Hello World!</h1>' > index.html
[root@node3 devops]# git init .
初始化空的 Git 版本库于 /root/devops/.git/
[root@node3 devops]# ls -A
.git  index.html
```

### git应用

```shell
[root@node3 devops]# git status  # 状态
# 位于分支 master
#
# 初始提交
#
# 未跟踪的文件:
#   （使用 "git add <file>..." 以包含要提交的内容）
#
#	index.html
提交为空，但是存在尚未跟踪的文件（使用 "git add" 建立跟踪）
[root@node3 devops]# git status -s  # 简要信息
?? index.html
[root@node3 devops]# git add .   # 将目录下所有内容加入暂存区，开始跟踪
# 位于分支 master
#
# 初始提交
#
# 要提交的变更：
#   （使用 "git rm --cached <file>..." 撤出暂存区）
#
#	新文件：    index.html
#
[root@node3 devops]# git status -s
A  index.html
[root@node3 devops]# git rm --cached index.html   # 撤出暂存区
rm 'index.html'
[root@node3 devops]# git status
# 位于分支 master
#
# 初始提交
#
# 未跟踪的文件:
#   （使用 "git add <file>..." 以包含要提交的内容）
#
#	index.html
提交为空，但是存在尚未跟踪的文件（使用 "git add" 建立跟踪）
[root@node3 devops]# git status -s
?? index.html
[root@node3 devops]# git add .  # 重新加入暂存区
[root@node3 devops]# git status -s
A  index.html
[root@node3 devops]# git commit  # 确认至版本库，需要写日志
[root@node3 devops]# git status
# 位于分支 master
无文件要提交，干净的工作区
[root@node3 devops]# git status -s

# 接下来的常规则应用，就是修改代码、加入跟踪、确认至版本库
[root@node3 devops]# echo '<h2>nsd 1812</n2>' >> index.html 
[root@node3 devops]# cp /etc/hosts .
[root@node3 devops]# git status -s
 M index.html
?? hosts
[root@node3 devops]# git add .
[root@node3 devops]# git status -s
A  hosts
M  index.html
[root@node3 devops]# git status 
# 位于分支 master
# 要提交的变更：
#   （使用 "git reset HEAD <file>..." 撤出暂存区）
#
#	新文件：    hosts
#	修改：      index.html
#
[root@node3 devops]# git commit -m "modify index.html, add hosts"
[master 0fff998] modify index.html, add hosts
 2 files changed, 3 insertions(+)
 create mode 100644 hosts
[root@node3 devops]# git status
# 位于分支 master
无文件要提交，干净的工作区
```

恢复误删除的文件

```shell
[root@node3 devops]# rm -rf *
[root@node3 devops]# ls
[root@node3 devops]# git status
# 位于分支 master
# 尚未暂存以备提交的变更：
#   （使用 "git add/rm <file>..." 更新要提交的内容）
#   （使用 "git checkout -- <file>..." 丢弃工作区的改动）
#
#	删除：      hosts
#	删除：      index.html
#
修改尚未加入提交（使用 "git add" 和/或 "git commit -a"）
[root@node3 devops]# git checkout -- *
[root@node3 devops]# ls
hosts  index.html

```











