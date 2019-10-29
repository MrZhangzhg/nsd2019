# nsd1905_ansible_project01

ansible项目展示：查看1904班项目

```shell
[root@room8pc16 ~]# source ~/nsd1905/bin/activate
(nsd1905) [root@room8pc16 ~]# cd /var/ftp/nsd2019/nsd1904/devweb/ansible_pro/myansible/
(nsd1905) [root@room8pc16 myansible]# python manage.py runserver
```

访问：http://127.0.0.1:8000/

功能说明：

http://127.0.0.1:8000/：项目首页，有4个超链接，可以访问主要的4个功能：主机信息、添加主机(组)、添加模块、执行任务

http://127.0.0.1:8000/webadmin/：显示所有主机的信息

http://127.0.0.1:8000/webadmin/addhosts/：添加主机、组

http://127.0.0.1:8000/webadmin/addmodules/：添加模块、参数

http://127.0.0.1:8000/webadmin/tasks/：在选定的主机/组上执行任务



## 初始化项目

1. 在pycharm中创建名为myansible的项目
2. 创建两个应用：index和webadmin

```python
(nsd1905) [root@room8pc16 myansible]# python manage.py startapp index
(nsd1905) [root@room8pc16 myansible]# python manage.py startapp webadmin
```

3. 修改配置文件

```python
# myansible/settings.py
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    ...略...
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

4. 把投票应用的static目录拷贝到myansible项目根目录下

## 完成index应用

1. 授权，将应用的URL交给应用处理

```python
# myansible/urls.py
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^webadmin/', include('webadmin.urls')),
    url(r'', include('index.urls')),
]

# index/urls.py  / webadmin/urls.py
from django.conf.urls import url

urlpatterns = []
```

2. 编写首页应用页面

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

# 创建模板，可以直接使用投票应用的basic.html作为基础模板
(nsd1905) [root@room8pc16 myansible]# cp ../day03/mysite/templates/basic.html templates/
# templates/index.html
{% extends 'basic.html' %}
{% load static %}
{% block title %}Ansible Webadmin{% endblock %}
{% block content %}
    <div class="row">
        <div class="col-sm-3 text-center h4">
            <a href="#" target="_blank">
                <img width="150px" src="{% static 'imgs/linux.jpg' %}"><br>
                主机信息
            </a>
        </div>
        <div class="col-sm-3 text-center h4">
            <a href="#" target="_blank">
                <img width="150px" src="{% static 'imgs/linux.jpg' %}"><br>
                添加主机
            </a>
        </div>
        <div class="col-sm-3 text-center h4">
            <a href="#" target="_blank">
                <img width="150px" src="{% static 'imgs/linux.jpg' %}"><br>
                添加模块
            </a>
        </div>
        <div class="col-sm-3 text-center h4">
            <a href="#" target="_blank">
                <img width="150px" src="{% static 'imgs/linux.jpg' %}"><br>
                执行任务
            </a>
        </div>
    </div>
{% endblock %}
```







