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
def add_modules(request):
    # print(dir(request))  # 打印request所有的属性
    # print(request.method)  # 打印当前request的方法
    # print(request.POST)
    # print(request.GET)
    if request.method == 'POST':
        mod = request.POST.get('module').strip()
        args = request.POST.get('param').strip()
        if mod:
            module = Module.objects.get_or_create(modulename=mod)[0]
            if args:
                module.args_set.get_or_create(args_text=args)

    modules = Module.objects.all()
    return render(request, 'webadmin/add_modules.html', {'modules': modules})

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

## 完成执行任务功能

1. url

```shell
# webadmin/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    ... ...
    url(r'^tasks/$', views.tasks, name='tasks'),
]
```

2. 编写视图函数

```shell
# webadmin/views.py
from django.shortcuts import render
from .models import Group, Module, Host
from .adhoc2 import adhoc

# Create your views here.

def index(request):
    return render(request, 'webadmin/server_info.html')

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

def add_modules(request):
    # print(dir(request))  # 打印request所有的属性
    # print(request.method)  # 打印当前request的方法
    # print(request.POST)
    # print(request.GET)
    if request.method == 'POST':
        mod = request.POST.get('module').strip()
        args = request.POST.get('param').strip()
        if mod:
            module = Module.objects.get_or_create(modulename=mod)[0]
            if args:
                module.args_set.get_or_create(args_text=args)

    modules = Module.objects.all()
    return render(request, 'webadmin/add_modules.html', {'modules': modules})

def tasks(request):
    if request.method == 'POST':
        ip = request.POST.get('host')
        group = request.POST.get('group')
        module = request.POST.get('module')
        args = request.POST.get('args')
        if group:
            dest = group
        elif ip:
            dest = ip
        else:
            dest = None

        if dest:
            if module and args:  # 如果模块和参数非空
                adhoc(['ansi_cfg/dhosts.py'], dest, module, args)

    hosts = Host.objects.all()
    groups = Group.objects.all()
    modules = Module.objects.all()
    objs = {'hosts': hosts, 'groups': groups, 'modules': modules}
    return render(request, 'webadmin/tasks.html', objs)

```

3. 编写模板文件

```shell
# templates/webadmin/tasks.html
{% extends 'base.html' %}
{% load static %}
{% block title %}执行任务{% endblock %}
{% block content %}
    <ul class="nav nav-tabs h4" style="margin-top: 8px">
        <li class="active"><a href="#server" data-toggle="tab">主机</a></li>
        <li><a href="#servers" data-toggle="tab">主机组</a></li>
    </ul>

    <form action="" method="post">
        {% csrf_token %}
        <div class="tab-content" style="padding: 5px;">
            <div class="tab-pane active fade in" id="server">
                <select class="form-control" name="host">
                    <option value="">无</option>
                    {% for host in hosts %}
                        <option value="{{ host.ipaddr }}">
                            {{ host.hostname }}
                        </option>
                    {% endfor %}
                </select>
            </div>
            <div class="tab-pane fade" id="servers">
                <select class="form-control" name="group">
                    <option value="">无</option>
                    {% for group in groups %}
                        <option value="{{ group.groupname }}">
                            {{ group.groupname }}
                        </option>
                    {% endfor %}
                </select>
            </div>
        </div>
        <hr>
        <table class="h4 table table-bordered table-striped table-hover">
            <thead class="bg-primary text-center">
                <tr>
                    <td>模块</td>
                    <td>参数</td>
                </tr>
            </thead>
            {% for module in modules %}
            <tr>
                <td>
                    <label>
                        <input type="radio" name="module" value="{{ module.modulename }}">
                        {{ module.modulename }}
                    </label>
                </td>
                <td>
                    <ul class="list-unstyled">
                        {% for args in module.args_set.all %}
                            <li>
                                <label>
                                    <input type="radio" name="args" value="{{ args.args_text }}">
                                    {{ args.args_text }}
                                </label>
                            </li>
                        {% endfor %}
                    </ul>
                </td>
            </tr>
        {% endfor %}
        </table>
        <div class="form-group text-center">
            <input class="btn btn-primary" type="submit" value="执 行">
        </div>
    </form>
{% endblock %}
```

4. 修改首页超链接

```shell
# templates/index/index.html
        <a href="{% url 'tasks' %}" target="_blank">
```

## 实现删除参数的功能

- 删除功能是通过函数来实现的
- 执行函数通过访问url来实现
- 结论：删除功能需要访问url，通过url关联函数，调用函数作用是删除参数

```shell
# webadmin/urls.py
urlpatterns = [
    url(r'^$', views.index, name='webadmin_index'),
    url(r'^addhosts/$', views.add_hosts, name='add_hosts'),
    url(r'^addmodules/$', views.add_modules, name='add_modules'),
    url(r'^tasks/$', views.tasks, name='tasks'),
    url(r'^(\d+)/del/$', views.del_args, name='del_args'),
]

# webadmin/views.py
def del_args(request, args_id):
    args = Args.objects.get(id=args_id)
    args.delete()
    
    return redirect('add_modules')

# 修改add_modules.html
{% for args in module.args_set.all %}
<li>
    <div class="col-sm-9">
    	{{ args.args_text }}
    </div>
    <div class="col-sm-3">
    	<a href="{% url 'del_args' args.id %}">del</a>
    </div>
</li>
{% endfor %}
```









