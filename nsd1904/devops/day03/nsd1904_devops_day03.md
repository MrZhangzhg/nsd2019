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
# 安装
(nsd1904) [root@room8pc16 day03]# pip install ansible-cmdb_pkgs/*

# 收集远程主机的信息
(nsd1904) [root@room8pc16 myansible]# ansible all -m setup --tree /tmp/nsd1904

# 利用ansible-cmdb生成web页面
(nsd1904) [root@room8pc16 myansible]# ansible-cmdb /tmp/nsd1904 > /tmp/servers.html
(nsd1904) [root@room8pc16 myansible]# firefox /tmp/servers.html &
```

## 编写自定义模块

通过ANSIBLE_LIBRARY定义ansible搜索模块时，额外的搜索目录：

```shell
(nsd1904) [root@room8pc16 myansible]# export ANSIBLE_LIBRARY=/tmp/mymodules
(nsd1904) [root@room8pc16 myansible]# mkdir /tmp/mymodules
```

编写模块，实现远程主机在本机进行拷贝文件

```python
# vim /tmp/mymodules/rcopy.py
from ansible.module_utils.basic import AnsibleModule
import shutil

def main():
    module = AnsibleModule(
        argument_spec=dict(
            yuan=dict(required=True, type='str'),
            mubiao=dict(required=True, type='str')
        )
    )
    shutil.copy(module.params['yuan'], module.params['mubiao'])
    module.exit_json(changed=True)
    
if __name__ == '__main__':
    main()

```

运行测试：

```shell
(nsd1904) [root@room8pc16 myansible]# ansible webservers -m rcopy -a "yuan=/etc/hosts mubiao=/tmp/zj.txt"
(nsd1904) [root@room8pc16 myansible]# ansible webservers -a "ls /tmp/zj.txt"
```



编写download模块

```shell
# vim /tmp/mymodules/download.py
from ansible.module_utils.basic import AnsibleModule
import wget

def main():
    module = AnsibleModule(
        argument_spec=dict(
            url=dict(required=True, type='str'),
            dest=dict(required=True, type='str')
        )
    )
    wget.download(module.params['url'], module.params['dest'])
    module.exit_json(changed=True)

if __name__ == '__main__':
    main()


(nsd1904) [root@room8pc16 myansible]# ansible dbservers -m download -a "url=http://192.168.4.254/server.repo dest=/tmp/"
# 报错，因为远程主机上没有wget模块
```

在远程主机上安装python模块

```shell
# 在物理机上下载wget
(nsd1904) [root@room8pc16 myansible]# pip download wget --trusted-host pypi.douban.com
# 拷贝软件到远程主机
(nsd1904) [root@room8pc16 myansible]# scp wget-3.2.zip node4:/root
# 在远程主机上安装
[root@node4 ~]# unzip wget-3.2.zip 
[root@node4 ~]# cd wget-3.2/
[root@node4 wget-3.2]# python setup.py install
# 注意，离线安装所有的python包，都是使用此方法

(nsd1904) [root@room8pc16 myansible]# ansible dbservers -m download -a "url=http://192.168.4.254/server.repo dest=/tmp/"
(nsd1904) [root@room8pc16 myansible]# ansible dbservers -a "ls /tmp/server.repo"

```











