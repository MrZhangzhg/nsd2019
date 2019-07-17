# nsd1902_devops_day04

## ansible模块练习

1. 环境变量

   ```python
   # export ANSIBLE_LIBRARY=/opt/myansible_lib/
   ```

2. 编写模块

   ```python
   # vim /opt/myansible_lib/download.py 
   #!/usr/bin/env python
   # -*- coding: utf8 -*-
   '用于下载指定文件'
   
   from ansible.module_utils.basic import AnsibleModule
   import wget
   
   def main():
       module = AnsibleModule(
           argument_spec=dict(
               url=dict(required=True, type='str'),
               path=dict(required=True, type='str')
           )
       )
       wget.download(module.params['url'], module.params['path'])
       module.exit_json(changed=True)
   
   if __name__ == '__main__':
       main()
   ```

   > 注意：远程主机只有python2，不是python3。python2默认字符采用的是ASCII码，而不是unicode，所以python2的文本中不能写汉字。如果需要添加汉字，需要在文件中指定字符集。

3. 在远程主机上安装wget。因为ansible准备好的模块，需要在远程主机上执行。

   ```shell
   # 在本机上下载wget
   # pip3 download wget --trusted-host pypi.douban.com
   
   # 在远程主机上安装wget
   # ansible webservers -m copy -a "src=files/wget-3.2.zip dest=/root"
   # ansible webservers -m shell -a "cd /root; unzip wget-3.2.zip"
   # ansible webservers -m shell -a "cd /root/wget-3.2/; python setup.py install"
   ```

4. 通过自己编写的模块，下载文件

   ```python
   # ansible webservers -m download -a "url=http://192.168.4.254/zabbix.png path=/tmp/zabbix.png"
   ```

## git

### git基本应用

《pro git》https://down.51cto.com/data/273438

安装

```shell
[root@node5 ~]# yum install -y git
```

配置基础信息

```shell
[root@node5 ~]# git config --global user.name "Mr.zzg"
[root@node5 ~]# git config --global user.email "zzg@tedu.cn"
[root@node5 ~]# git config --global core.editor vim
[root@node5 ~]# git config --list
[root@node5 ~]# cat ~/.gitconfig 
```

### git的重要工作区域

- 工作区：编写代码的项目目录
- 暂存区：工作区与版本库之间的缓冲地带
- 版本库：在工作区中有一个名为.git的目录，它是保存文件的目录

```mermaid
graph LR
w(工作区)
z(暂存区)
v(版本库)
w --git add-->z
z --git commit-->v
```

### git应用流程

1. 创建版本库

```shell
# 方法一：还没有项目目录前
[root@node5 ~]# git init pro1
初始化空的 Git 版本库于 /root/pro1/.git/
[root@node5 ~]# ls -A pro1/
.git

# 方法二：已有项目目录
[root@node5 ~]# mkdir pro2
[root@node5 ~]# echo '<h1>my web site</h1>' > pro2/index.html
[root@node5 ~]# cd pro2/
[root@node5 pro2]# git init .
初始化空的 Git 版本库于 /root/pro2/.git/
[root@node5 pro2]# ls -A
.git  index.html
```









