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

```





















