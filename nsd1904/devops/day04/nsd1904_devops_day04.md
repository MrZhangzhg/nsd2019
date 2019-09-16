# nsd1904_devops_day04

CI / CD：持续集成 / 持续交付

流行的自动化运维平台：docker / k8s / ansible / git / jenkins

准备三台机器

- node4.tedu.cn: 程序员PC
- node5.tedu.cn: gitlab服务器  -> 4GB以上内存
- node6.tedu.cn: jenkins

## git

- 软件版本管理系统
- 分布式

```shell
# 安装
[root@node4 ~]# yum install -y git
# 配置基础信息
[root@node4 ~]# git config --global user.name "zzg"
[root@node4 ~]# git config --global user.email "zzg@tedu.cn"
[root@node4 ~]# git config --global core.editor vim
# 查看
[root@node4 ~]# git config --list
[root@node4 ~]# cat ~/.gitconfig 
```

### git的工作区域

- 工作区
- 暂存区
- 版本库

```mermaid
graph LR
w(工作区)--git add-->s(暂存区)
s--git commit-->g(版本库)
```

### 初始化版本库

- 项目之初，直接构建

```shell
[root@node4 ~]# git init mypro
初始化空的 Git 版本库于 /root/mypro/.git/
[root@node4 ~]# cd mypro/
[root@node4 mypro]# ls -A
.git
```

- 已有项目

```shell
[root@node4 ~]# mkdir myweb
[root@node4 ~]# cd myweb
[root@node4 myweb]# echo '<h1>Hello World</h1>' > index.html
[root@node4 myweb]# git init
初始化空的 Git 版本库于 /root/myweb/.git/
[root@node4 myweb]# ls -A
.git  index.html
```













