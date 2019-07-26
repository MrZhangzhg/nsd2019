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
{% extends 'base.html' %}
{% load static %}
{% block title %}添加模块{% endblock %}
{% block content %}
    <div class="col-sm-12">
        <form action="" method="post" class="form-inline">
            {% csrf_token %}
            <div class="form-group">
                <label>模块：</label>
                <input type="text" class="form-control" name="module">
            </div>
            <div class="form-group">
                <label>参数：</label>
                <input type="text" class="form-control" name="args">
            </div>
            <div class="form-group">
                <input class="btn btn-primary" type="submit" value="提交">
            </div>
        </form>
    </div>
    <hr>
    <div class="col-sm-12">
        <table class="table table-hover table-striped table-bordered">
            <thead class="bg-primary text-center">
                <tr>
                    <td>模块</td>
                    <td>参数</td>
                </tr>
            </thead>
            <tbody>
                {% for module in modules %}
                    <tr>
                        <td>{{ module.module_name }}</td>
                        <td>
                            <ul class="list-unstyled">
                                {% for arg in module.args_set.all %}
                                    <li>{{ arg.arg_text }}</li>
                                {% endfor %}
                            </ul>
                        </td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
{% endblock %}
```

4. 修改mainpage.html中“添加主机”的超链接

```html
        <a href="{% url 'add_modules' %}" target="_blank">
```





