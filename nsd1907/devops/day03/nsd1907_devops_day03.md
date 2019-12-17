# nsd1907_devops_day03

## ansible

```python
# 本地安装 
(nsd1907) [root@room8pc16 day03]# pip install /var/ftp/pub/zzg_pypkgs/ansible_pkg/*
# 在线安装
(nsd1907) [root@room8pc16 day03]# pip install ansible==2.7.2
(nsd1907) [root@room8pc16 day03]# ansible --version
ansible 2.7.2
```

### ansible应用

- adhoc临时命令
- playbook

```shell
# 创建工作目录
(nsd1907) [root@room8pc16 day03]# mkdir myansible
(nsd1907) [root@room8pc16 day03]# cd myansible/
# 编写配置文件 
(nsd1907) [root@room8pc16 myansible]# vim ansible.cfg
[defaults]
inventory = hosts
remote_user = bob   # ssh到目标主机的用户

[privilege_escalation]   #　提权设置
become = true
become_user = root
become_method = sudo
become_ask_pass = flase


(nsd1907) [root@room8pc16 myansible]# vim ansible.cfg
[defaults]
inventory = hosts
remote_user = root
 
#[privilege_escalation]
#become = true
#become_user = root
#become_method = sudo
#become_ask_pass = flase

(nsd1907) [root@room8pc16 myansible]# vim hosts
[dbservers]
node4
 
[webservers]
node5
node6

# 配置名称解析
[root@room8pc16 day02]# for i in {1..254}
> do
> echo -e "192.168.4.$i\tnode$i.tedu.cn\tnode$i" >> /etc/hosts
> done

# 收集密钥，加入到信任列表
[root@room8pc16 day02]# ssh-keyscan node{4..6} >> ~/.ssh/known_hosts
# 测试连通性
(nsd1907) [root@room8pc16 myansible]# ansible all -m ping -k
# 配置免密登陆
(nsd1907) [root@room8pc16 day02]# ansible-doc authorized_key
(nsd1907) [root@room8pc16 day02]# ansible all -m authorized_key -a "user=root state=present key='{{lookup(\'file\', \'/root/.ssh/id_rsa.pub\') }}'" -k
```

配置vim支持yaml语法

```shell
(nsd1907) [root@room8pc16 myansible]# vim ~/.vimrc 
autocmd FileType yaml setlocal sw=2 ts=2 et ai
```

通过playbook配置yum

```shell
(nsd1907) [root@room8pc16 myansible]# ansible-doc yum_repository
(nsd1907) [root@room8pc16 myansible]# vim yum_repos.yml
---
- name: configure yum repository
  hosts: all
  tasks:
    - name: config yum
      yum_repository:
        file: centos7
        baseurl: ftp://192.168.4.254/centos7.4
        name: centos7
        description: local centos7 repository
        gpgcheck: no
        enabled: yes
(nsd1907) [root@room8pc16 myansible]# ansible-playbook --syntax-check yum_repos.yml
(nsd1907) [root@room8pc16 myansible]# ansible-playbook yum_repos.yml
```

通过playbook完成lamp环境

```shell
(nsd1907) [root@room8pc16 myansible]# vim lamp.yml
---
- name: configure dbservers
  hosts: dbservers
  tasks:
    - name: install db pkgs
      yum:
        name: mariadb-server
        state: present
    - name: config db service
      service:
        name: mariadb
        state: started
        enabled: yes

- name: configure webservers
  hosts: webservers
  tasks:
    - name: install web pkgs
      yum:
        name: httpd, php, php-mysql
        state: present
    - name: config web service
      service:
        name: httpd
        state: started
        enabled: yes
(nsd1907) [root@room8pc16 myansible]# ansible-playbook --syntax-check lamp.yml
(nsd1907) [root@room8pc16 myansible]# ansible-playbook lamp.yml

```










