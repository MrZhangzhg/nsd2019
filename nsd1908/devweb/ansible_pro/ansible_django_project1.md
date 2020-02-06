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









