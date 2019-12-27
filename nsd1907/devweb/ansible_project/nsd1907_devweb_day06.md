# nsd1907_devweb_day06

## 实现添加模块页

```python
# webadmin/urls.py
... ...
    url(r'^addmodules/$', views.add_modules, name='add_modules'),
... ...

# webadmin/views.py
... ...
def add_modules(request):
    if request.method == 'POST':
        module = request.POST.get('module').strip()
        args = request.POST.get('param').strip()
        if module:
            m = Module.objects.get_or_create(modulename=module)[0]
            if args:
                m.argument_set.get_or_create(arg_text=args)

    modules = Module.objects.all()
    return render(request, 'add_modules.html', {'modules': modules})

# templates/add_modules.html
{% extends 'base.html' %}
{% load static %}
{% block title %}添加模块{% endblock %}
{% block content %}
    <form action="" class="form-inline" method="post">
        {% csrf_token %}
        <div class="form-group">
            <label>模块：</label>
            <input class="form-control" type="text" name="module">
        </div>
        <div class="form-group">
            <label>参数：</label>
            <input class="form-control" type="text" name="param">
        </div>
        <div class="form-group">
            <input class="btn btn-primary" type="submit" value="提 交">
        </div>
    </form>
    <hr>
    <table class="table table-striped table-hover table-bordered">
        <thead class="bg-primary">
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
                        {% for args in module.argument_set.all %}
                            <li>
                                {{ args.arg_text }}
                            </li>
                        {% endfor %}
                    </ul>
                </td>
            </tr>
        {% endfor %}
    </table>
{% endblock %}

# templates/index.html
... ...
    <div class="col-sm-3 text-center">
        <a href="{% url 'add_modules' %}" target="_blank">
            <img width="150px" src="{% static 'imgs/linux.jpg' %}"><br>
            添加模块
        </a>
    </div>
... ...
```

## 制作执行任务页

```python
# webadmin/urls.py
... ...
    url(r'^tasks/$', views.tasks, name='tasks'),
... ...

# 将ansilbe课程中的adhoc2.py拷贝过来
(nsd1907) [root@room8pc16 ansi_cfg]# cp ../../../../devops/day03/adhoc2.py ../webadmin/


# webadmin/views.py
... ...
from . import adhoc2
... ...
def tasks(request):
    if request.method == 'POST':
        ip = request.POST.get('ip')
        group = request.POST.get('group')
        module = request.POST.get('module')
        args = request.POST.get('param')

        dest = None   # 设定执行目标
        if ip:  # 如果主机非空
            dest = ip
        elif group:
            dest = group

        if dest and module and args:  # 如果dest非空，模块和参数非空
            adhoc2.adhoc(['ansi_cfg/dhosts.py'], dest, module, args)

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
    <ul class="nav nav-tabs h4">
        <li class="active">
            <a href="#server" data-toggle="tab">主机</a>
        </li>
        <li>
            <a href="#servergroup" data-toggle="tab">主机组</a>
        </li>
    </ul>
        <form action="" method="post">
            {% csrf_token %}
            <div class="tab-content h4">
                <div class="tab-pane active fade in form-group" id="server">
                    <select class="form-control" name="ip">
                        <option value="">无</option>
                        {% for host in hosts %}
                            <option value="{{ host.ip_addr }}">
                                {{ host.hostname }}:{{ host.ip_addr }}
                            </option>
                        {% endfor %}
                    </select>
                </div>
                <div class="tab-pane fade form-group" id="servergroup">
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
            <table class="table table-striped table-hover table-bordered">
                <thead class="bg-primary">
                <tr>
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
                                {% for args in module.argument_set.all %}
                                    <li class="radio">
                                        <label>
                                            <input type="radio" name="param" value="{{ args.arg_text }}">
                                            {{ args.arg_text }}
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



# templates/index.html
    <div class="col-sm-3 text-center">
        <a href="{% url 'tasks' %}" target="_blank">
            <img width="150px" src="{% static 'imgs/linux.jpg' %}"><br>
            执行任务
        </a>
    </div>


```

## 在“添加模块”页面增加删除参数的功能

- 删除参数需要执行函数实现
- 调用函数又是通过访问一个URL来实现的

```python
# webadmin/urls.py
... ...
    url(r'^del_arg/(\d+)/$', views.del_arg, name='del_arg'),
... ...

# webadmin/views.py
from django.shortcuts import render, redirect
from .models import HostGroup, Module, Host, Argument
... ...
def del_arg(request, arg_id):
    args = Argument.objects.get(id=arg_id)
    args.delete()
    return redirect('add_modules')

# templates/add_modules.html
<li>
    <div class="col-sm-9">
    	{{ args.arg_text }}
    </div>
    <div class="col-sm-3">
        <a href="{% url 'del_arg' args.id %}">
        	del
        </a>
    </div>
</li>
```

