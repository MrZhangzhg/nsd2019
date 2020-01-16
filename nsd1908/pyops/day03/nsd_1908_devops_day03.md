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

# 配置名称解析
(nsd1908) [root@room8pc16 myansible]# for i in {1..254}
> do
> echo -e "192.168.4.$i\tnode$i.tedu.cn\tnode$i" >> /etc/hosts
> done

# 收集密钥
(nsd1908) [root@room8pc16 myansible]# ssh-keyscan node{4..6} >> ~/.ssh/known_hosts

# 配置免密登陆
(nsd1908) [root@room8pc16 myansible]# for host in node{4..6}; do ssh-copy-id $host; done

# 配置免密登陆的playbook
# 该playbook的执行需要sshpass软件包
# (nsd1908) [root@room8pc16 myansible]# yum install sshpass
(nsd1908) [root@room8pc16 myansible]# vim myssh_key.yml
---
- name: configure ssh pubkey
  hosts: all
  tasks:
    - name: upload pub key
      authorized_key:
        user: root
        state: present
        key: "{{ lookup('file', '/root/.ssh/id_rsa.pub') }}"
(nsd1908) [root@room8pc16 myansible]# ansible-playbook myssh_key.yml -k


```





