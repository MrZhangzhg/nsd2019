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

```











