# nsd1904_devops_day03

## ansible

安装

```shell
(nsd1904) [root@room8pc16 day03]# pip install ansible_pkg/*
```

### 配置ansible的工作环境

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

# 免密登陆
(nsd1904) [root@room8pc16 myansible]# for i in {4..6}
> do
> ssh-copy-id node$i
> done
```

### 执行命令的方式

- adhoc临时命令

```shell
# 输密码
(nsd1904) [root@room8pc16 myansible]# ansible all -m ping -k
# 免密情况下使用
(nsd1904) [root@room8pc16 myansible]# ansible all -m ping
```

- playbook
  - 一个playbook由多个play构成
  - 每个play指定哪些主机执行哪些任务
  - 任务由模块加参数来完成

配置vim，使它可以自适应yaml语法：

```shell
# vim ~/.vimrc
autocmd FileType yaml setlocal sw=2 ts=2 et ai
```

### 编写playbook

- 在web服务器上安装并启动httpd
- 在数据服务器上安装并启动mariadb

```shell
(nsd1904) [root@room8pc16 myansible]# vim lamp.yml
---
- name: configure dbservers
  hosts: dbservers
  tasks:
    - name: install mariadb-server
      yum:
        name: mariadb-server
        state: present
    - name: configure mariadb service
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
        state: latest
    - name: configure httpd service
      service:
        name: httpd
        state: started
        enabled: yes

# 语法检查
(nsd1904) [root@room8pc16 myansible]# ansible-playbook --syntax-check lamp.yml 
# 执行playbook
(nsd1904) [root@room8pc16 myansible]# ansible-playbook lamp.yml 
```

### 命名元组

- 继承于元组，元组拥有的属性，它都拥有
- 命名元组的下标有名字

```python
>>> from collections import namedtuple
>>> Point = namedtuple('Point', ['x', 'y', 'z'])
>>> p1 = Point(10, 15, 25)
>>> p1[0]
10
>>> p1[1:]
(15, 25)
>>> p1.x
10
>>> p1.y
15
>>> p1.z
25

```

### adhoc临时命令

官网：https://docs.ansible.com/ansible/2.7/index.html ->搜索python api

把python api example中的代码复制、粘贴到文件中，并执行

### 将yml文件手工转成python的数据类型

```shell
(nsd1904) [root@room8pc16 myansible]# vim lamp.yml
---
- name: configure dbservers
  hosts: dbservers
  tasks:
    - name: install mariadb-server
      yum:
        name: mariadb-server
        state: present
    - name: configure mariadb service
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
        state: latest
    - name: configure httpd service
      service:
        name: httpd
        state: started
        enabled: yes
```

转换为：

```python
[
    {
        'name': 'configure dbservers',
        'hosts': 'dbservers',
        'tasks': [
            {
                'name': 'install mariadb-server',
                'yum': {
                    'name': 'mariadb-server',
                    'state': 'present'
                }
            },
            {
                'name': 'configure mariadb service',
                'service': {
                    'name': 'mariadb',
                    'state': 'started',
                    'enabled': 'yes'
                }
            },
        ]
    },
    {
        'name': 'configure webservers',
        'hosts': 'webservers',
        'tasks': {
            {
                'name': 'install web pkgs',
                'yum': {
                    'name': ['httpd', 'php', 'php-mysql'],
                	'state': 'latest'
                }
            },
            {
                'name': 'configure httpd service',
      			'service': {
                    'name': 'httpd',
                    'state': 'started',
                    'enabled': 'yes'
                }
            }
        }
    }
]
```

## ansible-cmdb

- ansible-cmdb是ansible的一个插件
- 它可以把收集到的远程主机信息以Web方式呈现

```shell
(nsd1904) [root@room8pc16 day03]# pip install ansible-cmdb_pkgs/*
```









