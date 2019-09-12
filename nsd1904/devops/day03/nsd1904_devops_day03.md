# nsd1904_devops_day03

## ansible

安装

```shell
(nsd1904) [root@room8pc16 day03]# pip install ansible_pkg/*
```

配置ansible的工作环境

```shell
(nsd1904) [root@room8pc16 day03]# mkdir myansible
(nsd1904) [root@room8pc16 day03]# cd myansible
(nsd1904) [root@room8pc16 myansible]# vim ansible.cfg
[defaults]
inventory = hosts
remote_user = root

(nsd1904) [root@room8pc16 myansible]# vim hosts
[dbservers]
node4.tedu.cn

[webservers]
node5.tedu.cn
node6.tedu.cn
(nsd1904) [root@room8pc16 myansible]# ansible --version
(nsd1904) [root@room8pc16 myansible]# ansible all --list-hosts

# 配置名称解析
(nsd1904) [root@room8pc16 myansible]# for i in {1..254}
> do
> echo -e "192.168.4.$i\tnode$i.tedu.cn\tnode$i" >> /etc/hosts
> done

# 收集远程主机密钥
(nsd1904) [root@room8pc16 myansible]# ssh-keyscan 192.168.4.{4..6} node{4..6} node{4..6}.tedu.cn >> ~/.ssh/known_hosts 

```









