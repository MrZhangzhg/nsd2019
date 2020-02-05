# NSD1909_DEVWEB_DAY04

## 注意：有问题，在群中直接找项目经理

### 今日内容：

1. 介绍vmware虚拟机的使用
2. 配置环境
3. django

## 配置环境

```shell
# 安装python
[root@localhost ~]# tar xf zzg_pypkgs.tar.gz
[root@localhost ~]# cd zzg_pypkgs/
[root@localhost ~]# cd python3_pkg/
[root@localhost ~]# vim README
yum install -y sqlite-devel tk-devel tcl-devel readline-devel zlib-devel gcc gcc-c++ openssl-devel libffi-devel
tar xzf Python-3.6.7.tgz
cd Python-3.6.7
./configure --prefix=/usr/local/
make && make install
[root@localhost ~]# bash README

# 实现按tab键补全功能：https://www.jianshu.com/p/b83a803cfc86

# 创建虚拟环境
[root@localhost ~]# python3 -m venv ~/nsd1908

# 激活虚拟环境，并安装相应的软件包
[root@localhost ~]# source ~/nsd1908/bin/activate
(nsd1908) [root@localhost ~]# pip install django==
(nsd1908) [root@localhost ~]# pip install django==1.11.6
(nsd1908) [root@localhost ~]# pip install pymysql
```

## pycharm配置

```shell
# 配置pycharm。注意：需要java
(nsd1908) [root@localhost cloud5]# mkdir ~/bin
(nsd1908) [root@localhost cloud5]# tar xf pycharm2017.tar.gz -C ~/bin/

# 打开一个新的终端，运行破解工具
[root@localhost ~]# /root/bin/crack &

# 配置菜单，在菜单中添加pycharm
[root@localhost bin]# yum install -y alacarte
# 应用程序->杂项->主菜单
# 选择“主菜单”窗口中的 应用程序->编程，在右窗格点“新建项目”
# Name: PyCharm2017   Command: /root/bin/pycharm2017/bin/pycharm.sh
# 点击图标，更换为：/root/bin/pycharm2017/bin/pycharm.png

# 启动pycharm2017后，激活时，Lisence Server为http://127.0.0.1:1017
```

## DJANGO

### MTV

M: Model模型，对应数据库

T：Template模板，对应网页

V：View视图，对应函数

```mermaid
graph LR
c(client)--访问-->s(服务器URLCONF)
s--调用-->v(Views视图)
v--CRUD-->m(Model模型)
m--返回-->v
v--加载-->t(Template模板)
t--发送-->c
```

### 在pycharm中创建django项目

新建项目->左空格选择django项目，右窗格指定项目路径为/xxx/xxx/mysite。下面的解释器要改为/root/nsd1908/bin/python

```python
(nsd1908) [root@room8pc16 mysite]# tree .
.
├── manage.py             # 项目管理程序
├── mysite                # 项目配置目录
│   ├── __init__.py       # 初始化文件
│   ├── settings.py       # 项目的配置文件
│   ├── urls.py           # urlconf路由文件
│   └── wsgi.py           # 部署项目到服务器的配置文件
└── templates             # 模板目录，存放网页的目录
```

### 配置django项目

```python
# 配置数据库
[root@localhost cloud5]# yum install -y mariadb-server
[root@localhost cloud5]# systemctl start mariadb
[root@localhost cloud5]# systemctl enable mariadb

# 修改密码
[root@localhost cloud5]# mysqladmin password tedu.cn

# 创建数据库
[root@localhost cloud5]# mysql -uroot -ptedu.cn
MariaDB [(none)]> CREATE DATABASE nsd1908 DEFAULT CHARSET utf8;

# 配置django可以使用pymysql模块： mysite/__init__.py
import pymysql

pymysql.install_as_MySQLdb()

# 修改django项目配置： mysite/settings.py
ALLOWED_HOSTS = ['*']   # 允许用户可以通过所有地址访问
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nsd1908',
        'USER': 'root',
        'PASSWORD': 'tedu.cn',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_TZ = False

# 启动开发服务器测试，服务器运行在0.0.0.0的80端口
(nsd1908) [root@localhost mysite]# python manage.py runserver 0:80
# 访问http://127.0.0.1/

# 为django项目中默认的应用生成数据库表
(nsd1908) [root@localhost mysite]# python manage.py makemigrations
(nsd1908) [root@localhost mysite]# python manage.py migrate

# 创建管理员用户
(nsd1908) [root@localhost mysite]# python manage.py createsuperuser
Username (leave blank to use 'root'): admin
Email address: admin@tedu.cn
Password: 1234.com
Password (again): 1234.com

# 重新启动开发服务器
(nsd1908) [root@localhost mysite]# python manage.py runserver 0:80
# 访问管理后台：http://127.0.0.1/admin
```

## 配置应用

### 创建一个投票应用

```python
# 创建应用
(nsd1908) [root@localhost mysite]# python manage.py startapp polls
(nsd1908) [root@localhost mysite]# ls
manage.py  mysite  polls  templates

# 集成polls应用到项目
# mysite/settings.py
INSTALLED_APPS = [
    ... ...
    'polls',
]
```

### 投票应用的规划

- http://127.0.0.1/polls/：投票首页，显示所有的投票项
- http://127.0.0.1/polls/1/：1号问题的投票详情，可以进行投票
- http://127.0.0.1/polls/1/result/：1号问题的投票结果

### 完成应用

1. 授权，将应用的url交给应用处理

```python
# mysite/urls.py
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^polls/', include('polls.urls')),
]

# polls/urls.py
from django.conf.urls import url

urlpatterns = []
```

2. 制作投票首页
```python
# 1. 创建路由映射
# polls/urls.py
from django.conf.urls import url
from . import views  # 从当前目录导入views模块

urlpatterns = [
    # 用户访问http://x.x.x.x/polls/时，使用index函数响应，为该url起名为index
    url(r'^$', views.index, name='index'),
]

# 2. 创建视图函数
# polls/views.py
from django.shortcuts import render

# 每个函数至少需要一个参数，用于接收用户发来的请求
def index(request):
    return render(request, 'index.html')

# 3. 创建模板文件
# templates/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>投票首页</title>
</head>
<body>
<h1>投票首页</h1>
</body>
</html>

# 4. 访问http://127.0.0.1/polls/进行测试
```

2. 制作投票详情页

```python
# 1. polls/urls.py
from django.conf.urls import url
from . import views  # 从当前目录导入views模块

urlpatterns = [
    # 用户访问http://x.x.x.x/polls/时，使用index函数响应，为该url起名为index
    url(r'^$', views.index, name='index'),
    # 将url中的数字用\d+匹配，再通过()将其作为参数传递给detail函数
    url(r'^(\d+)/$', views.detail, name='detail'),
]

# 2. polls/views.py
... ...
def detail(request, question_id):
    # 字典的内容将转换成question_id=nn传给detail.html，作为它可以使用的变量
    return render(request, 'detail.html', {'question_id': question_id})

# 3. templates/detail.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>投票详情</title>
</head>
<body>
<h1>{{ question_id }}号问题的投票详情</h1>
</body>
</html>

# 4. 访问http://x.x.x.x/polls/数字
```

3. 制作投票结果页

```python
# 1. polls/urls.py
... ...
    url(r'^(\d+)/result/$', views.result, name='result'),
... ...

# 2. polls/views.py
... ...
def result(request, question_id):
    return render(request, 'result.html', {'question_id': question_id})

# 3. templates/result.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>投票结果</title>
</head>
<body>
<h1>{{ question_id }}号问题投票结果</h1>
</body>
</html>

# 4. 访问访问http://x.x.x.x/polls/数字/result
```









