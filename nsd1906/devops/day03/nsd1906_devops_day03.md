# nsd1906_devops_day03

## 嵌套的数据类型

- 只要记住，容器类型可以包含其他类型的数据
- 字典通过key取出值，列表和元组能过下标取值。取出的值如果还是字典或列表元组，可以继续通过key和下标取值。

```python
>>> users = {'bob': {'email': 'bob@qq.com', 'qq': '123423454'}, 'alice': {'email': 'alice@tedu.cn', 'qq': '98792342'}}
# 取出bob的信息
>>> users['bob']
{'email': 'bob@qq.com', 'qq': '123423454'}
# 取出bob的email
{'email': 'bob@qq.com', 'qq': '123423454'}
>>> users['bob']['email']
'bob@qq.com'

>>> users2 = {'bob': ['bob@qq.com', '2344525'], 'alice': ['alice@tedu.cn', '4523426364']}
>>> users2['alice']
['alice@tedu.cn', '4523426364']
>>> users2['alice'][-1]
'4523426364'
```

## ansible

```python
# 本地安装方式
(nsd1906) [root@room8pc16 day03]# pip install /var/ftp/pub/zzg_pypkgs/ansible_pkg/*
# 在线安装方式
(nsd1906) [root@room8pc16 day03]# pip install ansible==2.7.2

# 初始化ansible环境
[root@room8pc16 day03]# mkdir myansible
[root@room8pc16 day03]# cd myansible
[root@room8pc16 myansible]# vim ansible.cfg
[defaults]
inventory = hosts
remote_user = root

[root@room8pc16 myansible]# vim hosts
[dbservers]
node4

[webservers]
node5
node6

# 创建三台虚拟机，配置好IP地址，可用于管理。实现免密登陆

```











