# nsd1903_ansible_django2

## 编写“添加主机”功能页

1. url

```shell
# webadmin/urls.py
urlpatterns = [
    url(r'^$', views.index, name='webadmin_index'),
    url(r'^addhosts/$', views.add_hosts, name='add_hosts'),
]
```

2. view视图函数

```shell
# webadmin/views.py
from django.shortcuts import render
from .models import Group

def add_hosts(request):
    groups = Group.objects.all()
    return render(request, 'webadmin/add_hosts.html', {'groups': groups})
```

3. 编写模板文件

```shell
# templates/webadmin/add_hosts.html
{% extends 'base.html' %}
{% load static %}
{% block title %}添加主机{% endblock %}
{% block content %}
    <form action="" class="form-inline h4" method="post">
        {% csrf_token %}
        <div class="form-group">
            <label>主机组：</label>
            <input type="text" class="form-control" name="group">
        </div>
        <div class="form-group">
            <label>主机：</label>
            <input type="text" class="form-control" name="hostname">
        </div>
        <div class="form-group">
            <label>IP地址：</label>
            <input type="text" class="form-control" name="ip">
        </div>
        <div class="form-group">
            <input type="submit" class="btn btn-primary" value="提 交">
        </div>
    </form>
    <table class="h4 table table-bordered table-striped table-hover">
        <thead class="bg-primary text-center">
            <tr>
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
                            <li>{{ host.hostname }}: {{ host.ipaddr }}</li>
                        {% endfor %}
                    </ul>
                </td>
            </tr>
        {% endfor %}
    </table>
{% endblock %}
```

4. 修改index/index.html的超链接

```shell
# index/index.html
        <a href="{% url 'add_hosts' %}" target="_blank">
```

5. 实现添加主机功能

```shell
# 表单的action=""表示提交数据给当前页面。当前页面的url是/webadmin/add_hosts，这个url，对应的是add_hosts函数。
# 判断request请求的方法是不是post，如果是则取出post来的数据
# webadmin/views.py
def add_hosts(request):
    if request.method == 'POST':
        g = request.POST.get('group').strip()
        h = request.POST.get('hostname').strip()
        ip = request.POST.get('ip').strip()
        if g:  # 如果组名非空
            # get_or_create是取出或创建，返回值是元组(组实例，状态)
            group = Group.objects.get_or_create(groupname=g)[0]
            # 如果h和ip都是非空字符串
            if h and ip:
                group.host_set.get_or_create(hostname=h, ipaddr=ip)

    groups = Group.objects.all()
    return render(request, 'webadmin/add_hosts.html', {'groups': groups})

```

## 编写“添加模块”功能页

1. url

```shell
# webadmin/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    ... ...
    url(r'^addmodules/$', views.add_modules, name='add_modules'),
]
```

2. 视图函数

```shell

```

3. 编写模板文件

```shell
# templates/webadmin/add_modules.html
{% extends 'base.html' %}
{% load static %}
{% block title %}添加模块{% endblock %}
{% block content %}
    <form action="" class="form-inline h4" method="post">
        {% csrf_token %}
        <div class="form-group">
            <label>模块：</label>
            <input type="text" class="form-control" name="module">
        </div>
        <div class="form-group">
            <label>参数：</label>
            <input type="text" class="form-control" name="param">
        </div>
        <div class="form-group">
            <input type="submit" class="btn btn-primary" value="提 交">
        </div>
    </form>
    <table class="h4 table table-bordered table-striped table-hover">
        <thead class="bg-primary text-center">
            <tr>
                <td>模块</td>
                <td>参数</td>
            </tr>
        </thead>
        {% for module in modules %}
            <tr>
                <td>{{ module.modulename }}</td>
                <td>
                    <ul class="list-unstyled">
                        {% for args in module.args_set.all %}
                            <li>{{ args.args_text }}</li>
                        {% endfor %}
                    </ul>
                </td>
            </tr>
        {% endfor %}
    </table>
{% endblock %}
```

4. 修改首页模板文件超链接

```shell
# templates/index/index.html
        <a href="{% url 'add_modules' %}" target="_blank">
```









