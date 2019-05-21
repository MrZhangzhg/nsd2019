# tedu_py1812_devops_day03-2

## ansible

### yaml转python数据格式

```yaml
[root@room8pc16 myansible]# vim lamp.yml
---
- name: configure dbservers
  hosts: dbservers
  tasks:
    - name: install mariadb
      yum:
        name: mariadb-server
        state: present
    - name: start mariadb
      service:
        name: mariadb
        state: started
        enabled: yes

- name: configure webservers
  hosts: webservers
  tasks:
    - name: install apache
      yum:
        name: [httpd, php, php-mysql]
        state: latest
    - name: start httpd
      service:
        name: httpd
        state: started
        enabled: yes
```

转换成python数据类型

```python
[
    {
        'name': 'configure dbservers',
        'hosts': 'dbservers',
        'tasks': [
            {
                'name': 'install mariadb',
                'yum': {
                    'name': 'mariadb-server',
                    'state': 'present'
                }
            },
            {
                'name': 'start mariadb',
                'service': {
                    'name': 'mariadb',
                    'state': 'started',
                    'enabled': 'yes'
                }
            },
        ]
    }
]
```

### 编写下载模块

```shell
# 建立自定义模块目录
[root@room8pc16 day03]# mkdir library
[root@room8pc16 day03]# cd library
[root@room8pc16 library]# export ANSIBLE_LIBRARY=/var/ftp/nsd2019/nsd1812/devops/day03/library
[root@room8pc16 library]# vim download.py
import wget
from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            url=dict(required=True, type='str'),
            local=dict(required=True, type='str')
        )
    )
    wget.download(module.params['url'], module.params['local'])
    module.exit_json(changed=True)

if __name__ == '__main__':
    main()

# 测试，把一张图片放到web服务器的根目录下，如url是：
# http://192.168.4.5/building.jpeg
# 通过ansible使用download模块，要求dbservers下载图片到/home下
[root@room8pc16 myansible]# ansible dbservers -m download -a "url=http://192.168.4.5/building.jpeg local=/home/"
# 执行时报错，提示没有wget模块。原因是ansible会将download模块拷贝到远程dbservers服务器，在dbservers上执行download，但是dbservers上没有安装wget模块。
```

安装wget

```shell
# 在物理主机上下载wget，并拷贝到dbservers上
[root@room8pc16 tmp]# pip3 download wget --trusted-host mirrors.163.com
[root@room8pc16 tmp]# scp wget-3.2.zip 192.168.4.4:/tmp
# 在远程主机上安装wget，由于远程主机没有pip，所以采用以下安装方式
[root@room8pc16 tmp]# ssh 192.168.4.4
[root@node4 ~]# cd /tmp/
[root@node4 tmp]# unzip wget-3.2.zip 
[root@node4 tmp]# cd wget-3.2/
[root@node4 wget-3.2]# python setup.py install
```

远程服务器已经有wget模块了，就可以在物理机上运行ansible指令下载了：

```shell
[root@room8pc16 myansible]# ansible dbservers -m download -a "url=http://192.168.4.5/building.jpeg local=/home/"

```

