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
Installing collected packages: MarkupSafe, Jinja2, setuptools, PyYAML, (nsd1904) [root@room8pc16 myansible]# ansible all --list-hosts

```









