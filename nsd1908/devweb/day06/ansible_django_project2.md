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













