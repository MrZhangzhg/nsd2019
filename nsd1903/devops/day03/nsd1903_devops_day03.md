# nsd1903_devops_day03

## ansible应用

### 安装

```python
(nsd1903) [root@room8pc16 day03]# pip install zzg_pypkgs/ansible_pkg/*
```

### 配置基础应用环境

```shell
(nsd1903) [root@room8pc16 day03]# mkdir myansible
(nsd1903) [root@room8pc16 day03]# cd myansible
(nsd1903) [root@room8pc16 myansible]# vim ansible.cfg
[defaults]
inventory = hosts
remote_user = root
(nsd1903) [root@room8pc16 myansible]# vim hosts
[dbservers]
node5.tedu.cn

[webservers]
node6.tedu.cn
node7.tedu.cn

# 名称解析
[root@room8pc16 nsd2019]# for i in {1..254}
> do
> echo -e "192.168.4.$i\tnode$i.tedu.cn\tnode$i" >> /etc/hosts
> done

# 收集主集密钥，在首次ssh远程主机时，就不需要回答yes了
[root@room8pc16 nsd2019]# ssh-keyscan 192.168.4.{5..7} node{5..7} node{5..7}.tedu.cn >> ~/.ssh/known_hosts 

# 免密登陆 
[root@room8pc16 nsd2019]# for i in {5..7}
> do
> ssh-copy-id node$i
> done
```



### 应用之adhoc

- adhoc是临时命令，命令比较简单又不是周期性使用时，采用此方式

```shell
(nsd1903) [root@room8pc16 myansible]# ansible all -m ping 
(nsd1903) [root@room8pc16 myansible]# ansible-doc -l | grep copy
(nsd1903) [root@room8pc16 myansible]# ansible-doc copy
(nsd1903) [root@room8pc16 myansible]# ansible all -m copy -a "src=/etc/hosts dest=/etc/hosts"
```

### 应用之playbook

```shell
# 修改vim编辑器，可以支持yaml输入格式
# vim ~/.vimrc
autocmd FileType yaml setlocal sw=2 ts=2 et ai

# 上传yum仓库文件
# 1. 在ansible管理端创建yum文件
(nsd1903) [root@room8pc16 myansible]# mkdir files
(nsd1903) [root@room8pc16 myansible]# vim files/server.repo
[server]
name=server
baseurl=ftp://192.168.4.254/centos7.4
gpgcheck=0
# 2. 编写playbook
(nsd1903) [root@room8pc16 myansible]# vim yumrepo.yml
---
- name: configure yum
  hosts: all
  tasks:
    - name: upload yum repo file
      copy:
        src: files/server.repo
        dest: /etc/yum.repos.d/
# 3. 检查语法
[root@room8pc16 myansible]# ansible-playbook --syntax-check yumrepo.yml 

# 4. 执行playbook
[root@room8pc16 myansible]# ansible-playbook yumrepo.yml 

```





















