# nsd1906_devweb_day05

## 运维web化项目

- ansible
- django
- bootstrap

## 项目规划

- http://127.0.0.1/：项目首页，列出有哪些功能
- http://127.0.0.1/webadmin/：管理首页，列出所有主机信息
- http://127.0.0.1/webadmin/addhosts/：添加/显示主机和主机组
- http://127.0.0.1/webadmin/addmodules/：添加/显示模块和参数
- http://127.0.0.1/webadmin/tasks/：在指定的主机或组上执行管理任务
- 根据规划的url特点创建两个应用：index和webadmin

## 初始化项目

- 首先，通过pycharm创建名为myansible的项目
- 数据库用默认的sqlite3，它是一个文件型数据库，默认创建在项目的根目录下，名为db.sqlite3。mysql是数据库服务器软件，它可以包含很多个库，mysql还可以通过网络提供服务；sqlite是文件型的，一个文件就是一个库。

```python
# 创建应用
(nsd1906) [root@room8pc16 myansible]# python manage.py startapp index
(nsd1906) [root@room8pc16 myansible]# python manage.py startapp webadmin

# 修改主配置文件
# myansible/settings.py
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    ... ...
    'index',
    'webadmin'
]
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_TZ = False
STATICFILES_DIRS = [  # 指定静态文件目录还有根目录的static
    os.path.join(BASE_DIR, "static"),
]

# 将前面课程中的static目录拷贝到项目目录下
(nsd1906) [root@room8pc16 myansible]# cp -r /var/ftp/nsd2019/nsd1906/devweb/day02/static/ .


# 授权，将应用的url交给应用处理
# myansible/urls.py
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^webadmin/', include('webadmin.urls')),
    # r''可以匹配任意字符串
    url(r'', include('index.urls')),
]

# webadmin/urls.py
from django.conf.urls import url

urlpatterns = []

# index/urls.py
from django.conf.urls import url

urlpatterns = []

# 生成数据库表
(nsd1906) [root@room8pc16 myansible]# python manage.py makemigrations
(nsd1906) [root@room8pc16 myansible]# python manage.py migrate

# 创建管理员用户
(nsd1906) [root@room8pc16 myansible]# python manage.py createsuperuser

```

## 编写index应用

```python
# 编写url
# index/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

# 编写函数
# index/views.py
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


# 实现模板继承
# 复制投票项目的basic.html到templates目录
(nsd1906) [root@room8pc16 myansible]# cp ../../day03/mysite/templates/basic.html templates/

# 编写模板
# templates/index.html


```







