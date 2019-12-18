# nsd1907_devops_day04

上线流程

```mermaid
graph LR
dev(开发)--提交-->qa(测试)
qa--反馈-->dev
qa--交付-->ops(运维上线)
```

编程语言

- 解释执行：bash / python / php
- 编译执行：C / C++ / Go

## CI/CD

- CI：持续集成
- CD：持续交付（部署）

## git

- 是代码的版本管理工具

> 注意：二级命令补全功能的软件包是：bash-completion

```shell
# 将node4作为程序员的电脑，进行代码编写及管理
[root@node4 ~]# yum install -y git
[root@node4 ~]# source /etc/bash_completion.d/git 

# 配置基本信息
[root@node4 ~]# git config --global user.name zzg
[root@node4 ~]# git config --global user.email zzg@tedu.cn
[root@node4 ~]# git config --global core.editor vim

# 创建git仓库方法一：尚未开始编写项目
[root@node4 ~]# git init mytest
[root@node4 ~]# ls -A mytest/
.git

# 创建git仓库方法二：已存在项目目录
[root@node4 ~]# mkdir myapp
[root@node4 ~]# cd myapp/
[root@node4 myapp]# echo '<h1>My Site</h1>' > index.html
[root@node4 myapp]# git init
初始化空的 Git 版本库于 /root/myapp/.git/
[root@node4 myapp]# ls -A
.git  index.html

```











