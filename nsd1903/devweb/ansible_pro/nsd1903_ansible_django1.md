# nsd1903_ansible_django1

查看效果：运行1902班的项目

django案例：http://www.conyli.cc/django-2-by-example

django by example: https://www.jianshu.com/p/05810d38f93a

## 项目：服务器管理的web化

### 项目规划

- http://x.x.x.x：列出所有的功能，包括服务器信息、添加主机/组、添加模块、执行任务
- http://127.0.0.1/webadmin/：显示所有服务器的软硬件配置信息
- http://127.0.0.1/webadmin/addhosts/：添加和显示主机/组
- http://127.0.0.1/webadmin/addmodules/：添加和显示模块/参数
- http://127.0.0.1/webadmin/tasks/：选择主机或组执行相应的任务

## 项目初始化

1. 通过pycharm创建django项目，名为myansible。
2. 创建两个应用

```shell
(nsd1903) [root@room8pc16 myansible]# python manage.py startapp index
(nsd1903) [root@room8pc16 myansible]# python manage.py startapp webadmin
```

3. 修改配置

```shell
# settings.py
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    ... ...
    'index',
    'webadmin',
]
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_TZ = False
STATICFILES_DIRS = [   # 指定静态文件目录还可以使用根目录下的static
    os.path.join(BASE_DIR, "static"),
]
```

4. 授权，将应用的URL授权给应用

```shell
# myansible/urls.py
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^webadmin/', include('webadmin.urls')),
    url(r'', include('index.urls')),  # 匹配任意路径，务必写到最后
]

# webadmin/urls.py , index/urls.py
from django.conf.urls import url

urlpatterns = [
]
```

5. 将static目录拷贝到项目的根目录下

## 编写index应用

1. 配置url

```shell
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'', views.index, name='index'),
]
```

2. 编写index函数

```shell
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index/index.html')
```

3. 编写模板

```shell
# 在项目目录下的templates中创建index和webadmin两个子目录
# 创建templates/index/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Ansible Webadmin</title>
</head>
<body>
这是一个测试
</body>
</html>
```

4. 访问 http://127.0.0.1/ 测试

```shell
(nsd1903) [root@room8pc16 myansible]# python manage.py runserver 0:80
```

5. 引入bootstrap

```shell

```







