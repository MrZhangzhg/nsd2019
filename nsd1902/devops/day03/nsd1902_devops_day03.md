# nsd1902_devops_day03

## ansible基础应用

### 在虚拟环境下安装ansible

```python
# cd ansible_pkg/
# pip3 install *

# 或 在线安装
# pip3 install ansible==2.7.2
```

### 准备运行环境

```shell
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

```











