# nsd_1908_devops_day03

## ansible

```python
# 安装
(nsd1908) [root@room8pc16 day03]# pip install /var/ftp/pub/zzg_pypkgs/ansible_pkg/*

# 配置
(nsd1908) [root@room8pc16 day03]# mkdir myansible
(nsd1908) [root@room8pc16 day03]# cd myansible
##############################
# 如果远程用户是普通用户，使用此方式
(nsd1908) [root@room8pc16 myansible]# vim ansible.cfg
[defaults]
inventory = hosts
remote_user = tom

[privilege_escalation]
become = True
become_method = sudo
become_user = root
become_ask_pass = False
# 被管理的所有主机需要授权tom可以执行任何管理员命令
[root@room8pc16 pub]# visudo 
tom    ALL=(ALL)   NOPASSWD: ALL
######################################
# 直接使用root用户对远程主机进行管理
(nsd1908) [root@room8pc16 myansible]# vim ansible.cfg
[defaults]
inventory = hosts
remote_user = root

(nsd1908) [root@room8pc16 myansible]# vim hosts
[dbservers]
node4

[webservers]
node5
node6

```





