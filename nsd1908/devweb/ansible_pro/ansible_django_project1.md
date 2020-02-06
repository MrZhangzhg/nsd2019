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

### 创建项目

1. 通过pycharm创建名为myansible的项目
2. 创建应用

```python
# 创建名为index的应用
(nsd1908) [root@localhost myansible]# python manage.py startapp index

# 创建名为webadmin的应用
(nsd1908) [root@localhost myansible]# python manage.py startapp webadmin
```

3. 修改配置

```python
# myansible/settings.py
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    ... ...
    'index',
    'webadmin',
]
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_TZ = False
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# 将polls项目的static目录拷贝到外层myansible目录
(nsd1908) [root@localhost myansible]# ls
index  manage.py  myansible  static  templates  webadmin
```

4. 授权，将应用的url交给应用处理

```python
# myansible/urls.py
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^webadmin/', include('webadmin.urls')),
    # 注意: r''可以匹配任意url，它必须出现在最后一行
    url(r'', include('index.urls')),
]

# index/urls.py 和 webadmin/urls.py内容相同
from django.conf.urls import url

urlpatterns = []

```

### 编写首页应用

```python
# index/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'', views.index, name='index'),
]

# index/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

# 将polls项目中的base.html拷贝到myanisble/templates/目录中
(nsd1908) [root@localhost myansible]# ls templates/
base.html
# templates/index.html
{% extends 'base.html' %}
{% load static %}
{% block title %}Ansible Webadmin{% endblock %}
{% block content %}
<div class="row h4">
    <div class="col-sm-3 text-center">
        <a href="#" target="_blank">
            <img width="150px" src="{% static 'imgs/linux.jpg' %}"><br>
            主机信息
        </a>
    </div>
    <div class="col-sm-3 text-center">
        <a href="#" target="_blank">
            <img width="150px" src="{% static 'imgs/linux.jpg' %}"><br>
            添加主机
        </a>
    </div>
    <div class="col-sm-3 text-center">
        <a href="#" target="_blank">
            <img width="150px" src="{% static 'imgs/linux.jpg' %}"><br>
            添加模块
        </a>
    </div>
    <div class="col-sm-3 text-center">
        <a href="#" target="_blank">
            <img width="150px" src="{% static 'imgs/linux.jpg' %}"><br>
            执行任务
        </a>
    </div>
</div>
{% endblock %}

# 启动开发服务器，访问http://127.0.0.1/
(nsd1908) [root@localhost myansible]# python manage.py runserver 0:80
```

### 数据库

当前项目使用的数据库是sqlite数据库，这个数据库是文件型的。一个文件就是一个数据库。

```python
# 生成项目默认应用的数据库表
(nsd1908) [root@localhost myansible]# python manage.py makemigrations
(nsd1908) [root@localhost myansible]# python manage.py migrate

# 查看数据库
(nsd1908) [root@localhost myansible]# sqlite3 db.sqlite3 
sqlite> .help  # 查看帮助
sqlite> .tables  # 相当于show tables;
sqlite> .schema auth_user  # 相当于desc auth_user;
sqlite> select * from auth_user;
sqlite> .quit  # 退出

# 创建管理员用户
(nsd1908) [root@localhost myansible]# python manage.py createsuperuser
Username (leave blank to use 'root'): admin
Email address: admin@tedu.cn
Password: 1234.com
Password (again): 1234.com
```















