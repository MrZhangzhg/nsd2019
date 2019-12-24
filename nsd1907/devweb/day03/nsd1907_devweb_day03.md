## nsd1907_devweb_day03

## DJANGO

### MTV

- M：Model模型，对应数据库
- T：Template模板，对应html页面
- V：Views视图，对应函数

```mermaid
graph LR
c(客户端)--访问-->s(服务器URLConf)
s--调用-->v(Views函数)
v--CRUD-->m(Model模型)
m--返回-->v
v--加载-->t(Template模板)
t--返回-->c
```

## django应用

```shell
# 离线
(nsd1907) [root@room8pc16 day03]# pip install /var/ftp/pub/zzg_pypkgs/dj_pkgs/*
# 在线
(nsd1907) [root@room8pc16 day03]# pip install django==1.11.6

# 创建项目，方法一：
(nsd1907) [root@room8pc16 day03]# django-admin startproject mytest
(nsd1907) [root@room8pc16 day03]# ls
mytest  

# 创建项目，方法二：通过pycharm直接创建
# File -> New project -> 左窗格选django，右窗格填写项目目录，确认解释器是一直在用的虚拟环境 -> create
(nsd1907) [root@room8pc16 mysite]# tree .
.
├── manage.py            # 项目管理文件
├── mysite               # 项目配置目录
│   ├── __init__.py      # 项目初始化文件
│   ├── settings.py      # 项目配置文件
│   ├── urls.py          # 路由文件，定义url与函数对应用关系
│   └── wsgi.py          # 部署django应用时的配置文件
└── templates            # 模板目录

2 directories, 5 files

# 启动测试服务器，注意不要在生产环境下使用它
(nsd1907) [root@room8pc16 mysite]# python manage.py runserver
# 访问http://127.0.0.1:8000/查看页面

# 创建数据库
[root@room8pc16 day02]# mysql -uroot -ptedu.cn
MariaDB [(none)]> CREATE DATABASE dj1907 DEFAULT CHARSET utf8;

# mysite/__init__.py
import pymysql

pymysql.install_as_MySQLdb()

# 设置django
# mysite/settings.py
ALLOWED_HOSTS = ['*']   # django可以监听在0.0.0.0
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dj1907',
        'USER': 'root',
        'PASSWORD': 'tedu.cn',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_TZ = False
# 按ctrl+c停止开发服务器后，重新运行它，监听在0.0.0.0的80端口。只有root用户才可以使用1024以内的端口。
(nsd1907) [root@room8pc16 mysite]# python manage.py runserver 0:80

# django默认的应用需要数据库，生成数据库的表
(nsd1907) [root@room8pc16 mysite]# python manage.py makemigrations
(nsd1907) [root@room8pc16 mysite]# python manage.py migrate

# 创建管理员用户

```







