# tedu_py1812_devops_day03

## zabbix

官方文档页：https://www.zabbix.com/documentation/3.4/zh/manual

这里演示的环境路径是：/var/www/html/zabbix/

那么zabbix api地址是：http://192.168.4.2/zabbix/api_jsonrpc.php

## ansible

### 准备环境

启动三台虚拟机：

| node4.tedu.cn | 192.168.4.4/24 |
| ------------- | -------------- |
| node5.tedu.cn | 192.168.4.5/24 |
| node6.tedu.cn | 192.168.4.6/24 |

名称解析：

```shell
[root@room8pc16 nsd2019]# for i in {1..254}
> do
> echo -e "192.168.4.$i\tnode$i.tedu.cn\tnode$i" >> /etc/hosts
> done
```

收集主机密钥：

```shell
[root@room8pc16 ~]# ssh-keyscan 192.168.4.{4..6} node{4..6} node{4..6}.tedu.cn >> ~/.ssh/known_hosts 
```

安装ansible：

```shell
[root@room8pc16 zzg_pypkgs]# yum install -y sshpass
[root@room8pc16 zzg_pypkgs]# cd ansible_pkg/
[root@room8pc16 ansible_pkg]# pip3 install *
或
[root@room8pc16 ansible_pkg]# pip3 install ansible
```

### 配置ansible的基础应用环境

```shell
[root@room8pc16 day03]# mkdir myansible
[root@room8pc16 day03]# cd myansible/
[root@room8pc16 myansible]# vim ansible.cfg
[defaults]
inventory = hosts
remote_user = root
[dbservers]
node4.tedu.cn

[webservers]
node5.tedu.cn
node6.tedu.cn
[root@room8pc16 myansible]# ansible all -m ping -k
```



### 





