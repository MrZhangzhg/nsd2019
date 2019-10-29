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

## webadmin应用

1. 编写模型：需要放到数据库中的数据有：主机信息、模块信息
   - 主机信息：组、主机名、IP地址
   - 模块信息：模块名、参数

```python
from django.db import models

# Create your models here.
class HostGroup(models.Model):
    groupname = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return "主机组: %s" % self.groupname

class Host(models.Model):
    hostname = models.CharField(max_length=50)
    ip_addr = models.CharField(max_length=15)
    group = models.ForeignKey(HostGroup)
    
    def __str__(self):
        return "%s=>%s:%s" % (self.group, self.hostname, self.ip_addr)

class Module(models.Model):
    modulename = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return "模块:%s" % self.modulename

class Argument(models.Model):
    arg_text = models.CharField(max_length=200)
    module = models.ForeignKey(Module)
    
    def __str__(self):
        return "%s=>%s" % (self.module, self.arg_text)

# 生成表
(nsd1905) [root@room8pc16 myansible]# python manage.py makemigrations
(nsd1905) [root@room8pc16 myansible]# python manage.py migrate

# 创建管理员用户
(nsd1905) [root@room8pc16 myansible]# python manage.py createsuperuser
Username (leave blank to use 'root'): admin
Email address: admin@tedu.cn
Password: 
Password (again): 
Superuser created successfully.

# 将模型注册到后台管理界面
# webadmin/admin.py
from django.contrib import admin
from .models import HostGroup, Host, Module, Argument

for item in [HostGroup, Host, Module, Argument]:
    admin.site.register(item)

# 查看后台管理页面，添加几台主机进行测试。http://x.x.x.x/admin
```

## 准备ansible环境

查看数据库。当前项目所用的数据库是sqlite数据库，它是一个文件型数据库，一个文件就是一个数据库。

```shell
(nsd1905) [root@room8pc16 myansible]# ls db.sqlite3 
db.sqlite3
(nsd1905) [root@room8pc16 myansible]# sqlite3 db.sqlite3 
sqlite> .help   # 查看帮助
sqlite> .tables   # show tables
sqlite> .schema webadmin_host  # desc webadmin_host
sqlite> SELECT * from webadmin_host;  # 执行SQL语句
```

```python
# 创建配置文件
(nsd1905) [root@room8pc16 myansible]# mkdir ansi_cfg
(nsd1905) [root@room8pc16 myansible]# vim ansi_cfg/ansible.cfg
[defaults]
inventory = dhosts.py
remote_user = root

# 创建动态主机清单
# 主机和组存在数据库中，需要通过脚本程序，将它们从数据库中取出。
# 要求脚本文件有x权限，并且输出格式如下：
# {
#     组1: {
#         'hosts': [主机1, 主机2],
#     },
#　   组2: {
#　       'hosts': [主机3, 主机4],
#　   },
#　}
(nsd1905) [root@room8pc16 myansible]# touch ansi_cfg/dhosts.py
(nsd1905) [root@room8pc16 myansible]# chmod +x ansi_cfg/dhosts.py 
(nsd1905) [root@room8pc16 myansible]# vim ansi_cfg/dhosts.py 
#!/root/nsd1905/bin/python

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'sqlite:////var/ftp/nsd2019/nsd1905/devweb/myansible/db.sqlite3',
    encoding='utf8',
)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class HostGroup(Base):
    __tablename__ = 'webadmin_hostgroup'
    id = Column(Integer, primary_key=True)
    groupname = Column(String(50), unique=True)

class Host(Base):
    __tablename__ = 'webadmin_host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(50))
    ip_addr = Column(String(15))
    group_id = Column(Integer, ForeignKey('webadmin_hostgroup.id'))

if __name__ == '__main__':
    session = Session()
    result = {}
    qset = session.query(HostGroup.groupname, Host.ip_addr).join(Host)
    # print(qset.all())
    for group, host in qset:
        if group not in result:
            result[group] = {}
            result[group]['hosts'] = []
        result[group]['hosts'].append(host)

    print(result)

# 测试运行
(nsd1905) [root@room8pc16 ansi_cfg]# ansible all -m ping

```

## 编写webadmin的首页

1. 通过ansible-cmdb生成web页面

```python
(nsd1905) [root@room8pc16 ansi_cfg]# ansible all -m setup --tree /tmp/nsd1905out/
(nsd1905) [root@room8pc16 ansi_cfg]# ansible-cmdb /tmp/nsd1905out/ > ../templates/webadmin.html
```

2. 编写url

```python
# webadmin/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='webadmin'),
]
```

3. 编写视图函数

```python
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'webadmin.html')

```

4. 修改index应用首页的超链接

```shell
<div class="col-sm-3 text-center h4">
    <a href="{% url 'webadmin' %}" target="_blank">
        <img width="150px" src="{% static 'imgs/linux.jpg' %}"><br>
        主机信息
    </a>
</div>
```

## 制作添加主机页

```python
# webadmin/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='webadmin'),
    url(r'^addhosts/$', views.add_hosts, name='add_hosts'),
]

# webadmin/views.py  取出所有的组，发往前台页面
from django.shortcuts import render
from .models import HostGroup
...略...
def add_hosts(request):
    groups = HostGroup.objects.all()
    
    return render(request, 'add_hosts.html', {'groups': groups})

# templates/add_hosts.html
{% extends 'basic.html' %}
{% load static %}
{% block title %}添加主机{% endblock %}
{% block content %}
<div class="h4">
    <form action="">

    </form>
    <table class="table table-bordered table-hover table-striped">
        <thead>
            <tr class="text-center bg-primary">
                <td>主机组</td>
                <td>主机</td>
            </tr>
        </thead>
        {% for group in groups %}
            <tr>
                <td>{{ group.groupname }}</td>
                <td>
                    <ul class="list-unstyled">
                        {% for host in group.host_set.all %}
                            <li>
                                {{ host.hostname }}:{{ host.ip_addr }}
                            </li>
                        {% endfor %}
                    </ul>
                </td>
            </tr>
        {% endfor %}

    </table>
</div>
{% endblock %}

# 修改templates/index.html，添加超链接
<a href="{% url 'add_hosts' %}" target="_blank">
    <img width="150px" src="{% static 'imgs/linux.jpg' %}"><br>
    添加主机
</a>
```









