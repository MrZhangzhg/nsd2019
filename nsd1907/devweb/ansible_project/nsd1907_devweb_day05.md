# nsd1907_devweb_day05

- 创建项目

```python
# 创建应用
(nsd1907) [root@room8pc16 myansible]# python manage.py startapp index
(nsd1907) [root@room8pc16 myansible]# python manage.py startapp webadmin
(nsd1907) [root@room8pc16 myansible]# ls
index  manage.py  myansible  templates  webadmin

# 修改配置
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
STATICFILES_DIRS = [   # 定义各个应用搜索静态文件路径，项目根目录的static目录
    os.path.join(BASE_DIR, "static"),
]

# 将前一个投票应用的static目录拷贝到当前项目根目录下
(nsd1907) [root@room8pc16 myansible]# cp -r ../../day0304/mysite/polls/static/ .

# 生成项目默认应用需要的数据库表
(nsd1907) [root@room8pc16 myansible]# python manage.py \
makemigrations
(nsd1907) [root@room8pc16 myansible]# python manage.py migrate

# 创建管理员用户
(nsd1907) [root@room8pc16 myansible]# python manage.py \
createsuperuser
Username (leave blank to use 'root'): admin

# 访问数据库
(nsd1907) [root@room8pc16 myansible]# sqlite3 db.sqlite3 
sqlite> .help   # 查看帮助
sqlite> .tables   # show tables
sqlite> .schema auth_user   # desc auth_user
sqlite> SELECT * FROM auth_user;
```

## 应用规划

- http://127.0.0.1:8000/：首页应用，用于展示所有的功能
- http://127.0.0.1:8000/webadmin/：显示所有被管理的主机信息
- http://127.0.0.1:8000/webadmin/addhosts/：添加、显示主机和主机组
- http://127.0.0.1:8000/webadmin/addmodules/：添加、显示模块和参数
- http://127.0.0.1:8000/webadmin/tasks/：在指定的组或主机上执行任务

## 应用授权

```python
# myansible/urls.py
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^webadmin/', include('webadmin.urls')),
    # r''可以匹配任意url，务必写在最下方
    url(r'', include('index.urls')),
]

# index/urls.py  /  webadmin/urls.py
from django.conf.urls import url

urlpatterns = []

```











