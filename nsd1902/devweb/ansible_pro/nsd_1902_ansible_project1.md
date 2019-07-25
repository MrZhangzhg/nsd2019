# nsd_1902_ansible_project

## 项目目标

1. 通过web页显示所有主机的信息
2. 在网页中可以注册主机和组
3. 在网页中可以注册ansible模块和参数
4. 通过网页可以实现对远程主机/组的管理
5. 实现ansible动态主机清单

## URL规划

http://x.x.x.x/  用于显示所有的功能

http://127.0.0.1/webadmin/ 显示所有服务器的主机信息

http://127.0.0.1/webadmin/addhosts/  显示、添加主机/组

http://127.0.0.1/webadmin/addmodules/  显示、添加模块和参数

http://127.0.0.1/webadmin/tasks/  在主机/组执行任务

## 创建ansible项目

- 通过pycharm创建名为myansible的项目
- 创建mainpage和webadmin的应用

```shell
(nsd1902) [root@room8pc16 myansible]# python manage.py startapp mainpage
(nsd1902) [root@room8pc16 myansible]# python manage.py startapp webadmin
```

- 修改配置文件

```python
# myansible/settings.py
ALLOWED_HOSTS = '*'
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webadmin',
    'mainpage',
]
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_TZ = False
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
```

- 授权

```python
# myansible/urls.py
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^webadmin/', include('webadmin.urls')),
    url(r'', include('mainpage.urls')),
]

# mainpage/urls.py
from django.conf.urls import url

urlpatterns = [
    
]

# webadmin.urls.py
from django.conf.urls import url

urlpatterns = [
    
]
```











