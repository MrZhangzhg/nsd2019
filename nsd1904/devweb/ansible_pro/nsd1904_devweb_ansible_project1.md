# nsd1904_devweb_ansible_project1

## 项目展示

### 运行nsd1903班ansible_pro项目

```shell
$ source ~/nsd1904/bin/activate
$ cd nsd2019/nsd1903/devweb/ansible_pro/myansible
$ python manage.py runserver
访问127.0.0.1:8000
```

### 功能说明

- http://127.0.0.1:8000/：首页，列出所有功能项
- http://127.0.0.1:8000/webadmin/：展示托管主机详细信息
- http://127.0.0.1:8000/webadmin/addhosts/：实现添加主机/组功能
- http://127.0.0.1:8000/webadmin/addmodules/：实现添加模块/参数功能
- http://127.0.0.1:8000/webadmin/tasks/：在指定的主机或组上执行管理任务

## 编写项目

### 项目初始化

1. 通过pycharm创建名为myansible的项目
2. 创建名为index和webadmin的应用

```shell
(nsd1904) [root@room8pc16 myansible]# python manage.py startapp index
(nsd1904) [root@room8pc16 myansible]# python manage.py startapp webadmin
```

3. 修改配置文件

```shell
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
```

4. 授权

```shell
# myansible/urls.py
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^webadmin/', include('webadmin.urls')),
    # r''，可以匹配任何url，务必放到最后
    url(r'', include('index.urls')),
]
# index/urls.py,  # webadmin/urls.py
from django.conf.urls import url

urlpatterns = [
]
```

## 配置index应用

1. 配置URL

```shell
# index/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'', views.index, name='index'),
]
```

2. 编写index函数

```shell
# index/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
```

3. 创建模板文件

```shell
# templates/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Ansible Webadmin</title>
</head>
<body>
Ansible Webadmin
</body>
</html>
```

4. 引入bootstrap：拷贝前一个项目的static目录到项目的根目录下

```shell
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Ansible Webadmin</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
</head>
<body>
Ansible Webadmin
</body>
</html>
```

5. 实现模板继承

```shell
# 拷贝前一个项目的base.html到templates目录
# 修改templates/index.html
{% extends 'base.html' %}
{% load static %}
{% block title %}Ansible Webadmin{% endblock %}
{% block content %}
<div class="row text-center h4" style="margin-bottom: 50px">
    <div class="col-sm-3">
        <a href="#">
            <img src="{% static 'imgs/linux.jpg' %}" width="150px"><br>
            主机信息
        </a>
    </div>
    <div class="col-sm-3">
        <a href="#">
            <img src="{% static 'imgs/linux.jpg' %}" width="150px"><br>
            添加主机
        </a>
    </div>
    <div class="col-sm-3">
        <a href="#">
            <img src="{% static 'imgs/linux.jpg' %}" width="150px"><br>
            添加模块
        </a>
    </div>
    <div class="col-sm-3">
        <a href="#">
            <img src="{% static 'imgs/linux.jpg' %}" width="150px"><br>
            执行任务
        </a>
    </div>
</div>
{% endblock %}
```

## 编写webadmin应用

1. 编写模型Model

```shell
# webadmin/models.py
from django.db import models

class HostGroup(models.Model):
    groupname = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.groupname

class Host(models.Model):
    hostname = models.CharField(max_length=50)
    ipaddr = models.CharField(max_length=15)
    group = models.ForeignKey(HostGroup)
    
    def __str__(self):
        return "%s=>%s: %s" % (self.group, self.hostname, self.ipaddr)

class Module(models.Model):
    modulename = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.modulename

class Argument(models.Model):
    arg_text = models.CharField(max_length=200)
    module = models.ForeignKey(Module)
    
    def __str__(self):
        return "%s=>%s" % (self.module, self.arg_text)
```

2. 生成表

```shell
(nsd1904) [root@room8pc16 myansible]# python manage.py makemigrations
(nsd1904) [root@room8pc16 myansible]# python manage.py migrate
```

3. 查看表结构

```shell
# sqlite数据库是文件型数据库，一个文件就是一个库
(nsd1904) [root@room8pc16 myansible]# sqlite3 db.sqlite3 
sqlite> .help    # 查看帮助
sqlite> .tables   # 相当于show tables
sqlite> .schema webadmin_host   # 相当于desc webadmin_host
sqlite> SELECT * from auth_user;   # sql语句
```

4. 创建管理员

```shell
(nsd1904) [root@room8pc16 myansible]# python manage.py createsuperuser
```

5. 将模型注册到后台

```shell
# webadmin/admin.py
from django.contrib import admin
from .models import HostGroup, Host, Module, Argument

# Register your models here.
for item in [HostGroup, Host, Module, Argument]:
    admin.site.register(item)
```

6. 登陆后台，添加主机、组。http://127.0.0.1/admin/



