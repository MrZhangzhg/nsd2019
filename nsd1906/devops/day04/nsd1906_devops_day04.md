# nsd1906_devops_day04

## ansible

如果你连接远程主机是个普通用户，怎么执行管理任务？

```shell
# vim ansible.cfg
[defaults]
inventory = inventory
remote_user = zhangsan

[priviledge_escalation]    # 提权
become = yes               # 需要切换用户
become_method = sudo       # 切换的方式是sudo（另一种方式是su）
become_user = root         # 切换成管理员
become_ask_pass = no       # 不询问切换密码

# 被管理的服务器，需要配置sudo
# visudo
zhangsan	ALL=(ALL)		NOPASSWD: ALL
```

### ansible-cmdb

- 将ansible收集的主机信息转换成web页面

```python
# 收集远程主机的信息
(nsd1906) [root@room8pc16 myansible]# ansible all -m setup --tree /tmp/nsd1906out

# 安装ansible-cmdb
(nsd1906) [root@room8pc16 myansible]# pip install /var/ftp/pub/zzg_pypkgs/ansible-cmdb_pkgs/*
# 或在线安装
(nsd1906) [root@room8pc16 myansible]# pip install ansible-cmdb

# 生成web页面
(nsd1906) [root@room8pc16 myansible]# ansible-cmdb /tmp/nsd1906out > /tmp/hosts.html
(nsd1906) [root@room8pc16 myansible]# firefox /tmp/hosts.html &
```

## git

- 它是一个分布式的软件版控制系统

```shell
# 安装
[root@node4 ~]# yum install -y git
# 配置基本信息
[root@node4 ~]# git config --global user.name "Mr.Zhang"
[root@node4 ~]# git config --global user.email "zzg@tedu.cn"
[root@node4 ~]# git config --global core.editor vim
# 查看信息
[root@node4 ~]# git config --list 
user.name=Mr.Zhang
user.email=zzg@tedu.cn
core.editor=vim
[root@node4 ~]# cat ~/.gitconfig 
[user]
	name = Mr.Zhang
	email = zzg@tedu.cn
[core]
	editor = vim

```











