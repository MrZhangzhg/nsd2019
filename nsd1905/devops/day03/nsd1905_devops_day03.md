# nsd1905_devops_day03

## ansible应用

```shell
(nsd1905) [root@room8pc16 ~]# pip install zzg_pypkgs/ansible_pkg/*
# 或在线安装
(nsd1905) [root@room8pc16 day03]# pip install ansible==2.7.2

# 创建工作目录
(nsd1905) [root@room8pc16 day03]# mkdir myansible
(nsd1905) [root@room8pc16 day03]# cd myansible
# 创建配置文件
(nsd1905) [root@room8pc16 myansible]# vim ansible.cfg
[defaults]
inventory = hosts
remote_user = root
# 创建主机清单文件
(nsd1905) [root@room8pc16 myansible]# vim hosts
[dbservers]
node4

[webservers]
node5
node6
# 准备三台虚拟机
node4: 192.168.4.4
node5: 192.168.4.5
node6: 192.168.4.6
配置可以对其免密登陆
(nsd1905) [root@room8pc16 myansible]# for i in {4..6}
> do
> ssh-copy-id root@192.168.4.$i
> done
配置名称解析
(nsd1905) [root@room8pc16 day01]# for i in {1..254}
> do
> echo -e "192.168.4.$i\tnode$i.tedu.cn\tnode$i" >> /etc/hosts
> done
收集主机密钥
(nsd1905) [root@room8pc16 day01]# ssh-keyscan node{4..6} node{4..6}.tedu.cn 192.168.4.{4..6} >> ~/.ssh/known_hosts 

# 测试到远程主机的通信
(nsd1905) [root@room8pc16 myansible]# ansible all -m ping

# 配置vim，使编写yaml文件时，更方便
(nsd1905) [root@room8pc16 day01]# vim ~/.vimrc 
autocmd FileType yaml setlocal sw=2 ts=2 et ai

# 编写playbook，完成对web服务器和db服务器的配置

```













