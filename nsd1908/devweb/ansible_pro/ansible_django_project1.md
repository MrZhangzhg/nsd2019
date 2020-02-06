## ansible_django_project1

### 准备环境

```python
# 在虚拟环境下安装相应的软件包
(nsd1908) [root@localhost zzg_pypkgs]# pip install ansible_pkg/*
(nsd1908) [root@localhost zzg_pypkgs]# pip install sqlalchemy_pkgs/*
(nsd1908) [root@localhost zzg_pypkgs]# pip install ansible-cmdb_pkgs/*


# 在线安装
(nsd1908) [root@localhost zzg_pypkgs]# pip install ansible==2.7.2
(nsd1908) [root@localhost zzg_pypkgs]# pip install sqlalchemy==1.2.14
(nsd1908) [root@localhost zzg_pypkgs]# pip install ansible-cmdb==1.30

# 运行前一个班的项目
[root@localhost nsd2019]# source ~/nsd1908/bin/activate
(nsd1908) [root@localhost nsd2019]# cd nsd1907/devweb/ansible_project/myansible
(nsd1908) [root@localhost myansible]# python manage.py runserver
# 访问http://127.0.0.1:8000
```

