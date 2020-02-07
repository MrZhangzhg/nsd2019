## ansible_django_project2

### 制作webadmin应用

#### url规划

```python
http://127.0.0.1/webadmin：显示主机信息
http://127.0.0.1/webadmin/add_hosts：添加主机
http://127.0.0.1/webadmin/add_modules：添加模块
http://127.0.0.1/webadmin/tasks：执行ansible任务
```

#### 编写模型

```python
# webadmin/models.py
from django.db import models

class HostGroup(models.Model):
    groupname = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.groupname

class Host(models.Model):
    hostname = models.CharField(max_length=100)
    ipaddr = models.CharField(max_length=15)
    group = models.ForeignKey(HostGroup)
    
    def __str__(self):
        return "%s=>%s:%s" % (self.group, self.hostname, self.ipaddr)

class Module(models.Model):
    modluename = models.CharField(max_length=50)
    
    def __str__(self):
        return self.modluename

class Argument(models.Model):
    arg_text = models.CharField(max_length=200)
    module = models.ForeignKey(Module)
    
    def __str__(self):
        return "%s=>%s" % (self.module, self.arg_text)

(nsd1908) [root@localhost myansible]# python manage.py makemigrations
(nsd1908) [root@localhost myansible]# python manage.py migrate

# 将模型注册到后台管理界面
# webadmin/admin.py
from django.contrib import admin
from .models import HostGroup, Host, Module, Argument

for item in [HostGroup, Host, Module, Argument]:
    admin.site.register(item)

# 登陆到http://127.0.0.1/admin/，添加两个组和一些主机
```

#### 配置ansible

```python
(nsd1908) [root@localhost myansible]# mkdir ansi_cfg
(nsd1908) [root@localhost myansible]# cd ansi_cfg
(nsd1908) [root@localhost ansi_cfg]# vim ansible.cfg
[defaults]
inventory = ./dhosts.py
remote_user = root
# 实现到远程主机的免密登陆
(nsd1908) [root@localhost ansi_cfg]# ssh-keygen 
(nsd1908) [root@localhost ansi_cfg]# ssh-copy-id 127.0.0.1

(nsd1908) [root@localhost ansi_cfg]# touch dhosts.py
(nsd1908) [root@localhost ansi_cfg]# chmod 755 dhosts.py
```

#### 创建动态主机清单文件

```python
动态主机清单文件就是一个脚本，它必须输出以下格式：
{
    'dbservers': {'hosts': ['主机1', '主机2']},
    'webservers' {'hosts': ['主机3', '主机4']},
}

# vim dhosts.py
#!/root/nsd1908/bin/python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'sqlite:////var/ftp/nsd2019/nsd1908/devweb/ansible_pro/myansible/db.sqlite3',
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
    hostname = Column(String(100))
    ipaddr = Column(String(15))
    group_id = Column(ForeignKey('webadmin_hostgroup.id'))

if __name__ == '__main__':
    session = Session()
    qset = session.query(Host.ipaddr, HostGroup.groupname).join(HostGroup)
    # print(qset.all())
    result = {}
    for ip, group in qset:
        if group not in result:
            result[group] = {}
            result[group]['hosts'] = []
        result[group]['hosts'].append(ip)
    print(result)
(nsd1908) [root@localhost ansi_cfg]# ./dhosts.py 
{'dbservers': {'hosts': ['127.0.0.1']}, 'webservers': {'hosts': ['127.0.0.1', '127.0.0.1']}}
(nsd1908) [root@localhost ansi_cfg]# ansible all -m ping
```

#### 制作webadmin首页

```python
# 通过ansible-cmdb生成信息
(nsd1908) [root@localhost ansi_cfg]# ansible all -m setup --tree /tmp/nsd1908out/
(nsd1908) [root@localhost ansi_cfg]# ansible-cmdb /tmp/nsd1908out/ > ../templates/hosts.html

# webadmin/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='mainpage'),
]

# webadmin/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'hosts.html')

# templates/index.html
<a href="{% url 'mainpage' %}" target="_blank">
    <img width="150px" src="{% static 'imgs/linux.jpg' %}"><br>
    主机信息
</a>
```

#### 制作添加主机页

```python
# webadmin/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='mainpage'),
    url(r'^add_hosts/$', views.add_hosts, name='add_hosts'),
]

# webadmin/views.py
from django.shortcuts import render
from .models import HostGroup

def index(request):
    return render(request, 'hosts.html')

def add_hosts(request):
    if request.method == 'POST':
        group = request.POST.get('group').strip()
        host = request.POST.get('host').strip()
        ip = request.POST.get('ip').strip()
        if group:  # 如果group非空
            g = HostGroup.objects.get_or_create(groupname=group)[0]
            if host and ip:  # 如果host和ip非空
                g.host_set.get_or_create(hostname=host, ipaddr=ip)

    groups = HostGroup.objects.all()
    return render(request, 'add_hosts.html', {'groups': groups})


# templates/add_hosts.html
{% extends 'base.html' %}
{% load static %}
{% block title %}添加主机{% endblock %}
{% block content %}
# action=""表示提交表单时，提交到当前url，即http://127.0.0.1/webadmin/add_hosts/
    <form action="" method="post" class="form-inline h4">
        {% csrf_token %}
        <div class="form-group">
            <label>主机组：</label>
            <input class="form-control" type="text" name="group">
        </div>
        <div class="form-group">
            <label>主机：</label>
            <input class="form-control" type="text" name="host">
        </div>
        <div class="form-group">
            <label>IP：</label>
            <input class="form-control" type="text" name="ip">
        </div>
        <input class="btn btn-primary" type="submit" value="提 交">
    </form>
    <hr>
    <table class="table table-bordered table-striped table-hover h4">
        <thead>
            <tr class="bg-primary">
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
                            <li>{{ host.hostname }}:{{ host.ipaddr }}</li>
                        {% endfor %}
                    </ul>
                </td>
            </tr>
        {% endfor %}
    </table>
{% endblock %}

# templates/index.html
<a href="{% url 'add_hosts' %}" target="_blank">
    <img width="150px" src="{% static 'imgs/linux.jpg' %}"><br>
    添加主机
</a>
```

#### 制作添加模块页

```python
# webadmin/urls.py
... ...
    url(r'^add_modules/$', views.add_modules, name='add_modules'),
... ...

# webadmin/views.py
from .models import HostGroup, Module

def add_modules(request):
    if request.method == 'POST':
        module = request.POST.get('module').strip()
        arg = request.POST.get('param').strip()
        if module:
            m = Module.objects.get_or_create(modluename=module)[0]
            m.argument_set.get_or_create(arg_text=arg)

    modules = Module.objects.all()
    return render(request, 'add_modules.html', {'modules': modules})


# templates/add_modules.html
{% extends 'base.html' %}
{% load static %}
{% block title %}添加模块{% endblock %}
{% block content %}
    <form action="" method="post" class="form-inline h4">
        {% csrf_token %}
        <div class="form-group">
            <label>模块：</label>
            <input class="form-control" type="text" name="module">
        </div>
        <div class="form-group">
            <label>参数：</label>
            <input class="form-control" type="text" name="param">
        </div>
        <input class="btn btn-primary" type="submit" value="提 交">
    </form>
    <hr>
    <table class="table table-bordered table-striped table-hover h4">
        <thead>
            <tr class="bg-primary">
                <td>模块</td>
                <td>参数</td>
            </tr>
        </thead>
        {% for module in modules %}
            <tr>
                <td>{{ module.modluename }}</td>
                <td>
                    <ul class="list-unstyled">
                        {% for arg in module.argument_set.all %}
                            <li>{{ arg.arg_text }}</li>
                        {% endfor %}
                    </ul>
                </td>
            </tr>
        {% endfor %}
    </table>
{% endblock %}

# templates/index.html
<a href="{% url 'add_modules' %}" target="_blank">
    <img width="150px" src="{% static 'imgs/linux.jpg' %}"><br>
    添加模块
</a>
```

#### 制作执行任务页

```python
# webadmin/urls.py
... ...
    url(r'^tasks/$', views.tasks, name='tasks'),
... ...

# webadmin/views.py
from .models import HostGroup, Module, Host

def tasks(request):
    hosts = Host.objects.all()
    groups = HostGroup.objects.all()
    modules = Module.objects.all()
    context = {'hosts': hosts, 'groups': groups, 'modules': modules}
    return render(request, 'tasks.html', context)

# templates/tasks.html
{% extends 'base.html' %}
{% load static %}
{% block title %}执行任务{% endblock %}
{% block content %}
{% endblock %}

# templates/index.html
<a href="{% url 'tasks' %}" target="_blank">
    <img width="150px" src="{% static 'imgs/linux.jpg' %}"><br>
    执行任务
</a>
```















