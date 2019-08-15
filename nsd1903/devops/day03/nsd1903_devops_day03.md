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

```



### 应用之adhoc

- adhoc是临时命令





















