# nsd_1902_ansible_project2

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

## 制作添加模块页

1. url

```python
# webadmin/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.webadmin_index, name='webadmin_index'),
    url(r'^addhosts/$', views.add_hosts, name='add_hosts'),
    url(r'^addmodules/$', views.add_modules, name='add_modules'),
]
```

2. 视图函数

```python
# webadmin/views.py
from .models import HostGroup, Module
def add_modules(request):
    modules = Module.objects.all()
    return render(request, 'addmodules.html', {'modules': modules})

```

3. 模板文件

```html
# templates/addmodules.html

```

4. 修改mainpage.html中“添加主机”的超链接

```html
        <a href="{% url 'add_modules' %}" target="_blank">
```





