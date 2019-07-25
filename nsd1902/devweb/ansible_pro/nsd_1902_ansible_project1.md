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

## mainpage应用

1. url

```python
# mainpage/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mainpage, name='mainpage'),
]
```

2. 视图函数

```python
# mainpage/views.py
from django.shortcuts import render

# Create your views here.

def mainpage(request):
    return render(request, 'mainpage.html')

```

3. 模板文件

```html
# templates/mainpage.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Ansible Webadmin</title>
</head>
<body>
<h1>Ansible Webadmin</h1>
</body>
</html>
```

4. 启动开发服务器，测试首页

```shell
(nsd1902) [root@room8pc16 myansible]# python manage.py runserver 0:80
```

5. 引入boostrap：将static目录拷贝到项目目录下，并修改网页头部信息

## webadmin应用

### 管理模型

```python
# webadmin/models.py
from django.db import models

# Create your models here.

class HostGroup(models.Model):
    groupname = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.groupname

class Host(models.Model):
    hostname = models.CharField(max_length=100, unique=True)
    ipaddr = models.CharField(max_length=15)
    group = models.CharField(HostGroup)
    
    def __str__(self):
        return '%s=>%s' % (self.group, self.hostname)

class Module(models.Model):
    module_name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.module_name

class Args(models.Model):
    arg_text = models.CharField(max_length=100)
    module = models.ForeignKey(Module)
    
    def __str__(self):
        return '%s=>%s' % (self.module, self.arg_text)

```

生成数据库中的表

```shell
(nsd1902) [root@room8pc16 myansible]# python manage.py makemigrations
(nsd1902) [root@room8pc16 myansible]# python manage.py migrate
```

项目的根目录下的db.sqlite3是数据库文件。sqlite数据库是文件型数据库，一个文件就是一个库。

```shell
[root@room8pc16 myansible]# sqlite3 db.sqlite3 
sqlite> .help   # 查看帮助
sqlite> .table  # 显示所有的表
sqlite> .schema webadmin_host  # 查看表结构
sqlite> select * from webadmin_host;
```

创建管理员用户

```shell
(nsd1902) [root@room8pc16 myansible]# python manage.py createsuperuser
```

将模型注册到后台管理界面

```python
# webadmin/admin.py
from django.contrib import admin
from .models import HostGroup, Host, Module, Args

# Register your models here.

for item in [HostGroup, Host, Module, Args]:
    admin.site.register(item)
```

登陆到http://x.x.x.x/admin进行管理

## 准备ansible工作环境

```shell
(nsd1902) [root@room8pc16 myansible]# mkdir ansicfg
(nsd1902) [root@room8pc16 myansible]# vim ansicfg/ansible.cfg
[defaults]
inventory = dhosts.py
remote_user = root

(nsd1902) [root@room8pc16 myansible]# touch ansicfg/dhosts.py
(nsd1902) [root@room8pc16 myansible]# chmod +x ansicfg/dhosts.py
```

创建动态主机清单

ansible动态主机清单文件是一个脚本，脚本的输出要求是以下格式：

```python
{
    '组1': {'hosts': ['主机1', '主机2']},
    '组2': {'hosts': ['主机1', '主机2']},
}

result = {}
result['webservers'] = {}   # {'webservers': {}}
result['webservers']['hosts'] = []  # {'webservers': {'hosts': []}}
```

动态主机清单脚本：

```python
#!/root/nsd1902/bin/python
import json
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'sqlite:////var/ftp/nsd2019/nsd1902/devweb/ansible_pro/myansible/db.sqlite3',
    encoding='utf8',
)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class HostGroup(Base):
    __tablename__ = 'webadmin_hostgroup'
    id = Column(Integer, primary_key=True)
    groupname = Column(String(100), unique=True)

class Host(Base):
    __tablename__ = 'webadmin_host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(100), unique=True)
    ipaddr = Column(String(15))
    group_id = Column(Integer, ForeignKey('webadmin_hostgroup.id'))


if __name__ == '__main__':
    result = {}
    session = Session()
    qset = session.query(HostGroup.groupname, Host.ipaddr).join(Host)
    for group, ip in qset:
        if group not in result:
            result[group] = {}
        if not result[group]:
            result[group]['hosts'] = []
        result[group]['hosts'].append(ip)
    print(json.dumps(result))

# 测试
(nsd1902) [root@room8pc16 ansicfg]# ansible all -m ping
```











