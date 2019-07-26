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

5. 完善函数，实现添加模块和参数的功能

```python
def add_modules(request):
    if request.method == 'POST':
        module = request.POST.get('module').strip()
        arg_text = request.POST.get('args').strip()
        if module:
            m = Module.objects.get_or_create(module_name=module)[0]
            if arg_text:
                m.args_set.get_or_create(arg_text=arg_text)

    modules = Module.objects.all()
    return render(request, 'addmodules.html', {'modules': modules})
```

## 制作执行任务页

1. URL

```python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.webadmin_index, name='webadmin_index'),
    url(r'^addhosts/$', views.add_hosts, name='add_hosts'),
    url(r'^addmodules/$', views.add_modules, name='add_modules'),
    url(r'^tasks/$', views.tasks, name='tasks'),
]

```

2. 视图函数

```python
def tasks(request):
    return render(request, 'tasks.html')
```

3. 模板文件

```html
＃ templates/tasks.html
{% extends 'base.html' %}
{% load static %}
{% block title %}执行任务{% endblock %}
{% block content %}
    <div class="col-sm-12">
        <form action="" method="post">
            {% csrf_token %}
            <ul class="nav nav-tabs">
                <li class="active"><a href="#server" data-toggle="tab">主机</a></li>
                <li><a href="#servergroup" data-toggle="tab">主机组</a></li>
            </ul>
            <div class="tab-content" style="margin-top: 5px;">
                <div id="server" class="tab-pane active fade in">
                    <div class="form-group">
                        <select name="host" class="form-control">
                            <option value="">无</option>
                            {% for host in hosts %}
                                <option value="{{ host.ipaddr }}">{{ host.hostname }}</option>
                            {% endfor %}
                        </select>
                    </div>
                </div>
                <div id="servergroup" class="tab-pane fade">
                    <div class="form-group">
                        <select name="group" class="form-control">
                            <option value="">无</option>
                            {% for group in groups %}
                                <option value="{{ group.groupname }}">{{ group.groupname }}</option>
                            {% endfor %}
                        </select>
                    </div>
                </div>
            </div>
            <hr>
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
                        <td>
                            <div class="radio">
                                <label>
                                    <input type="radio" name="mod" value="{{ module.module_name }}">
                                    {{ module.module_name }}
                                </label>
                            </div>
                        </td>
                        <td>
                            <ul class="list-unstyled">
                                {% for arg in module.args_set.all %}
                                    <li>
                                        <div class="radio">
                                            <label>
                                                <input type="radio" name="param" value="{{ arg.arg_text }}">
                                                {{ arg.arg_text }}
                                            </label>
                                        </div>
                                    </li>
                                {% endfor %}
                            </ul>
                        </td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
        <div class="form-group text-center">
            <input class="btn btn-primary" type="submit" value="执 行">
        </div>
        </form>
    </div>
{% endblock %}
```

4. 修改mainpage.html中的超链接

```html
    <a href="{% url 'tasks' %}" target="_blank">
```

5. 修改视图函数，使之真正可以执行任务



## 删除功能

为参数增加删除功能。在“添加模块”页的参数后面，增加一个“删除”链接。

- 删除选项，是对数据库的操作
- 操作数据库模型，通过视图函数来完成
- 访问某个URL，实现调用函数

1. url

```python
    url(r'^del_arg/(\d+)/$', views.del_arg, name='del_arg'),
```

2. 视图函数

```python
def del_arg(request, arg_id):
    arg = Args.objects.get(id=arg_id)
    arg.delete()
    
    return redirect('addmodules')
```

3. 修改模板，在参数后面加上删除链接

```html
<td>
    <ul class="list-unstyled">
        {% for arg in module.args_set.all %}
        <li>
            <div class="col-sm-9">
                {{ arg.arg_text }}
            </div>
            <div class="col-sm-3">
                <a href="{% url 'del_arg' arg.id %}">del</a>
            </div>
        </li>
        {% endfor %}
    </ul>
</td>
```



