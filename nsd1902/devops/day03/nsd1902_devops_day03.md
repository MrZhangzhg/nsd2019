# nsd1902_devops_day03

## ansible基础应用

### 在虚拟环境下安装ansible

```python
# cd ansible_pkg/
# pip3 install *

# 或 在线安装
# pip3 install ansible==2.7.2

# yum install -y sshpass
```

### 准备运行环境

```shell
# 创建工作目录并创建配置文件
# mkdir myansible
# cd myansible
# vim ansible.cfg
[defaults]
inventory = hosts
remote_user = root

# vim hosts
[dbservers]
node5.tedu.cn

[webservers]
node6.tedu.cn
node7.tedu.cn

# 配置名称解析
[root@room8pc16 nsd2019]# for i in {1..254}
> do
> echo -e "192.168.4.$i\tnode$i.tedu.cn\tnode$i" >> /etc/hosts
> done


# 收集远程主机的密钥并保存。用户登陆时，不再提示是否接受密钥
[root@room8pc16 nsd2019]# ssh-keyscan node{5..7} node{5..7}.tedu.cn 192.168.4.{5..7} >> ~/.ssh/known_hosts 


# 测试环境
# ansible all -m ping -k
```

### ansible之adhoc（临时命令）

```shell
# ansible 主机　-m 模块　-a "参数"
```

### ansible之playbook

- 配置远程主机的密钥

```shell
# 查模块帮助
# ansible-doc authorized_key

# vim auth_key.yml
---
- name: configure ssh key
  hosts: all
  tasks:
    - name: upload key
      authorized_key:
        user: root
        state: present
        key: "{{ lookup('file', '/root/.ssh/id_rsa.pub') }}"
# 检查语法
# ansible-playbook --syntax-check auth_key.yml

# 执行playbook
# ansible-playbook auth_key.yml -k

```











