# nsd_1908_devops_day04

## CI/CD：持续集成/持续交付

编程语言：

- 解释执行：shell / python / php / javascript
- 编译执行：c / c++ / go / java

```mermaid
graph LR
dev(程序员)--上传-->git(git服务器)
j(jenkins)--拉取-->git
app1(应用服务器)--下载-->j
app2(应用服务器)--下载-->j
app3(应用服务器)--下载-->j
app4(应用服务器)--下载-->j
```

## git：开源的软件版本控制管理工具

### 准备git

将node4作为程序员编写代码的主机

```python
[root@node4 ~]# yum install -y git

# 命令补全功能需要安装的包
[root@node4 ~]# rpm -q bash-completion
bash-completion-2.1-6.el7.noarch

# 启用git的tab补全功能，可以重启系统，也可以采用以下方法
[root@node4 ~]# source /etc/bash_completion.d/git 

# 配置用户信息
[root@node4 ~]# git config --global user.name zzg
[root@node4 ~]# git config --global user.email zzg@tedu.cn
[root@node4 ~]# git config --global core.editor vim
[root@node4 ~]# git config --list 
user.name=zzg
user.email=zzg@tedu.cn
core.editor=vim
[root@node4 ~]# cat ~/.gitconfig 
[user]
	name = zzg
	email = zzg@tedu.cn
[core]
	editor = vim
```

## git的工作区域

- 工作区： 程序项目目录
- 暂存区：工作区与版本库之间的缓冲地带，.git/index
- 版本库：程序项目目录下的.git目录

```mermaid
graph LR
w(工作区)--git add-->s(暂存区)
s--git commit-->g(版本库)
```

### git应用

```shell
# 初始化git方法一
[root@node4 ~]# git init mytest
初始化空的 Git 版本库于 /root/mytest/.git/
[root@node4 ~]# ls -A mytest/
.git

# 初始化git方法二
[root@node4 ~]# mkdir myweb
[root@node4 ~]# cd myweb/
[root@node4 myweb]# echo '<h1>my web site</h1>' > index.html
[root@node4 myweb]# git init
初始化空的 Git 版本库于 /root/myweb/.git/
[root@node4 myweb]# ls -A
.git  index.html

# 查看状态
[root@node4 myweb]# git status 
[root@node4 myweb]# git status -s
?? index.html   # ??表示状态未知

# 将项目目录下所有内容加入到暂存区
[root@node4 myweb]# git add .
[root@node4 myweb]# git status
[root@node4 myweb]# git status -s
A  index.html  # A表示新增加的文件

# 提交到版本库
[root@node4 myweb]# git commit  # 跳出vim写日志，如果什么也不写，则不提交
[root@node4 myweb]# git commit -m "init project"
[root@node4 myweb]# git status
# 位于分支 master
无文件要提交，干净的工作区
[root@node4 myweb]# git status -s

```

















