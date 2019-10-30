# nsd1905_ansible_project02

完成添加主机页

```python
# 修改模板，为模板添加表单，表单的action为空，表示发送数据到当前URL。
# templates/add_hosts.html
{% extends 'basic.html' %}
{% load static %}
{% block title %}添加主机{% endblock %}
{% block content %}
<div class="h4">
    <form class="form-inline" action="" method="post">
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
            <label>IP地址：</label>
            <input class="form-control" type="text" name="ip">
        </div>
        <div class="form-group">
            <input class="btn btn-primary" type="submit" value="提 交">
        </div>
    </form>
    <hr>
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

# 测试HTTP的方法。当添加主机页是get方法，那么就不检查表单数据；如果是POST方法，则取出表单中的数据，并将其写入到数据库。
# webadmin/views.py
def add_hosts(request):
    print(request.method)   # 在终端打印出请求的方法
    groups = HostGroup.objects.all()

    return render(request, 'add_hosts.html', {'groups': groups})
# 通过项目首页点击“添加主机”进入页面，此时是get方法；在“添加主机”页面，提交表单，此时是post方法。在启动开发服务器的终端查看打印出来的内容。

# 测试用户发送的请求都有哪些属性。对象的属性，可以通过dir()来获取。
def add_hosts(request):
    print(request.method)   # 在终端打印请求方法
    print(dir(request))  # 在终端中打印request的属性
    groups = HostGroup.objects.all()

    return render(request, 'add_hosts.html', {'groups': groups})

# 查看到request有GET和POST属性，打印GET和POST的值
def add_hosts(request):
    # print(request.method)   # 在终端打印请求方法
    # print(dir(request))  # 在终端中打印request的属性
    print(request.GET)
    print(request.POST)
    groups = HostGroup.objects.all()

    return render(request, 'add_hosts.html', {'groups': groups})

# 实现添加主机的具体功能
def add_hosts(request):
    # print(request.method)   # 在终端打印请求方法
    # print(dir(request))  # 在终端中打印request的属性
    # print(request.GET)
    # print(request.POST)
    if request.method == 'POST':
        groupname = request.POST.get('group')
        hostname = request.POST.get('host')
        ip_addr = request.POST.get('ip')
        if groupname:  # 如果主机组名非空
            # get_or_create用于取出或创建组，返回的是: (组实例，状态)
            group = HostGroup.objects.get_or_create(groupname=groupname)[0]
            if hostname and ip_addr:  # 如果主机名和IP也非空
                group.host_set.get_or_create(hostname=hostname, ip_addr=ip_addr)

    groups = HostGroup.objects.all()
    return render(request, 'add_hosts.html', {'groups': groups})
```

## 编写添加模块页

```python
# webadmin/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='webadmin'),
    url(r'^addhosts/$', views.add_hosts, name='add_hosts'),
    url(r'^addmodules/$', views.add_modules, name='add_modules'),
]

# webadmin/veiws.py
from .models import HostGroup, Module

def add_modules(request):
    if request.method == 'POST':
        modulename = request.POST.get('module')
        args = request.POST.get('params')
        if modulename:  # 如果模块名非空
            module = Module.objects.get_or_create(modulename=modulename)[0]
            if args:  # 如果主机名和IP也非空
                module.argument_set.get_or_create(arg_text=args)

    modules = Module.objects.all()
    return render(request, 'add_modules.html', {'modules': modules})

# templates/add_modules.html
{% extends 'basic.html' %}
{% load static %}
{% block title %}添加模块{% endblock %}
{% block content %}
<div class="h4">
    <form class="form-inline" action="" method="post">
        {% csrf_token %}
        <div class="form-group">
            <label>模块：</label>
            <input class="form-control" type="text" name="module">
        </div>
        <div class="form-group">
            <label>参数：</label>
            <input class="form-control" type="text" name="params">
        </div>
        <div class="form-group">
            <input class="btn btn-primary" type="submit" value="提 交">
        </div>
    </form>
    <hr>
    <table class="table table-bordered table-hover table-striped">
        <thead>
            <tr class="text-center bg-primary">
                <td>模块</td>
                <td>参数</td>
            </tr>
        </thead>
        {% for module in modules %}
            <tr>
                <td>{{ module.modulename }}</td>
                <td>
                    <ul class="list-unstyled">
                        {% for arg in module.argument_set.all %}
                            <li>
                                {{ arg.arg_text }}
                            </li>
                        {% endfor %}
                    </ul>
                </td>
            </tr>
        {% endfor %}
    </table>
</div>
{% endblock %}

# 修改项目首页中的超链接，templates/index.html
<a href="{% url 'add_modules' %}" target="_blank">
    <img width="150px" src="{% static 'imgs/linux.jpg' %}"><br>
    添加模块
</a>
```

## 完成执行任务页面

```python
# webadmin/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='webadmin'),
    url(r'^addhosts/$', views.add_hosts, name='add_hosts'),
    url(r'^addmodules/$', views.add_modules, name='add_modules'),
    url(r'^tasks/$', views.tasks, name='tasks'),
]

# webadmin/views.py
def tasks(request):
    hosts = Host.objects.all()
    groups = HostGroup.objects.all()
    modules = Module.objects.all()
    context = {'hosts': hosts, 'groups': groups, 'modules': modules}
    return render(request, 'tasks.html', context)

# 修改项目首页中的超链接
# templates/index.html
<a href="{% url 'tasks' %}" target="_blank">
    <img width="150px" src="{% static 'imgs/linux.jpg' %}"><br>
    执行任务
</a>

# templates/tasks.html
{% extends 'basic.html' %}
{% load static %}
{% block title %}添加模块{% endblock %}
{% block content %}
    <div class="h4">
        <ul class="nav nav-tabs">
            <li class="active"><a href="#server" data-toggle="tab">主机</a></li>
            <li><a href="#server-group" data-toggle="tab">主机组</a></li>
        </ul>
        <form action="" method="post">
            {% csrf_token %}
            <div class="tab-content" style="margin: 15px 0">
            <div class="tab-pane fade in active form-group" id="server">
                <select name="host" class="form-control">
                    <option value="">无</option>
                    {% for host in hosts %}
                        <option value="{{ host.ip_addr }}">
                            {{ host.hostname }}:{{ host.ip_addr }}
                        </option>
                    {% endfor %}
                </select>
            </div>
            <div class="tab-pane fade form-group" id="server-group">
                <select name="group" class="form-control">
                    <option value="">无</option>
                    {% for group in groups %}
                        <option value="{{ group.groupname }}">
                            {{ group.groupname }}
                        </option>
                    {% endfor %}
                </select>
            </div>
        </div>
            <table class="table table-bordered table-hover table-striped">
                <thead>
                    <tr class="text-center bg-primary">
                        <td>模块</td>
                        <td>参数</td>
                    </tr>
                </thead>
                {% for module in modules %}
                    <tr>
                        <td>
                            <div class="radio">
                                <label>
                                    <input type="radio" name="module" value="{{ module.modulename }}">
                                    {{ module.modulename }}
                                </label>
                            </div>
                        </td>
                        <td>
                            <ul class="list-unstyled">
                                {% for arg in module.argument_set.all %}
                                    <li>
                                        <div class="radio">
                                            <label>
                                                <input type="radio" name="params" value="{{ arg.arg_text }}">
                                                {{ arg.arg_text }}
                                            </label>
                                        </div>
                                    </li>
                                {% endfor %}
                            </ul>
                        </td>
                    </tr>
                {% endfor %}
            </table>
            <div class="form-group text-center">
                <input class="btn btn-primary" type="submit" value="执  行">
            </div>
        </form>
    </div>
{% endblock %}


# 完成视图函数
from .adhoc2 import adhoc

def tasks(request):
    if request.method == 'POST':
        ip = request.POST.get('host')
        group = request.POST.get('group')
        module = request.POST.get('module')
        args = request.POST.get('params')
        # 判断，如果主机和组全选了，只在主机上执行任务
        dest = None  # 用于存储执行任务的目标，是主机？是组？
        if ip:
            dest = ip
        elif group:
            dest = group

        if dest:  # 如果dest不是None，则执行任务
            # 调用ansible的函数
            #(nsd1905)[root@room8pc16 myansible]# cp ../../devops/day03/adhoc2.py webadmin/
            if module and args:
                adhoc(['ansi_cfg/dhosts.py'], dest, module, args)

    hosts = Host.objects.all()
    groups = HostGroup.objects.all()
    modules = Module.objects.all()
    context = {'hosts': hosts, 'groups': groups, 'modules': modules}
    return render(request, 'tasks.html', context)

```

## 在“添加模块”页增加删除参数的按钮

1. 点击“删除”将会执行一个函数，该函数用于删除参数
2. 如何触发执行函数？用户访问URL！
3. 让删除功能是访问一个URL，该URL对应一个函数，函数是在数据库中取出相应的记录，然后删除

```python
# webadmin/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='webadmin'),
    url(r'^addhosts/$', views.add_hosts, name='add_hosts'),
    url(r'^addmodules/$', views.add_modules, name='add_modules'),
    url(r'^tasks/$', views.tasks, name='tasks'),
    url(r'^del_arg/(\d+)/$', views.del_arg, name='del_arg'),
]

# webadmin/views.py
from django.shortcuts import render, redirect
from .models import HostGroup, Module, Host, Argument

def del_arg(request, arg_id):
    args = Argument.objects.get(id=arg_id)
    args.delete()
    
    return redirect('add_modules')

# templates/add_modules.html
... ...
<ul class="list-unstyled">
    {% for arg in module.argument_set.all %}
        <li>
            <div class="col-sm-9">
            	{{ arg.arg_text }}
            </div>
            <div class="col-sm-3">
            	<a href="{% url 'del_arg' arg.id %}">
            	del
            </a>
            </div>
        </li>
    {% endfor %}
</ul>
... ... 
```

