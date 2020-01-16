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

# 配置vim，使它支持yaml的特点
(nsd1908) [root@room8pc16 myansible]# vim ~/.vimrc 
autocmd FileType yaml setlocal sw=2 ts=2 et ai

# 配置yum
(nsd1908) [root@room8pc16 myansible]# vim yum.yml
- name: configure yum repo
  hosts: all
  tasks:
    - name: configure yum client
      yum_repository:
        name: centos7
        description: centos 7.4
        baseurl: ftp://192.168.4.254/centos7.4
        file: centos7
        gpgcheck: no
        enabled: yes
# 检查语法
(nsd1908) [root@room8pc16 myansible]# ansible-playbook --syntax-check yum.yml 
# 执行playbook
(nsd1908) [root@room8pc16 myansible]# ansible-playbook yum.yml 


# lamp配置
(nsd1908) [root@room8pc16 myansible]# vim lamp.yml
---
- name: configure dbservers
  hosts: dbservers
  tasks:
    - name: install db pkgs
      yum:
        name: mariadb-server
        state: present
    - name: configure db serivce
      service:
        name: mariadb
        state: started
        enabled: yes

- name: configure webservers
  hosts: webservers
  tasks:
    - name: install web pkgs
      yum:
        name: [httpd, php, php-mysql]
        state: present
    - name: configure web serivce
      service:
        name: httpd
        state: started
        enabled: yes
(nsd1908) [root@room8pc16 myansible]# ansible-playbook --syntax-check lamp.yml
(nsd1908) [root@room8pc16 myansible]# ansible-playbook lamp.yml

```















