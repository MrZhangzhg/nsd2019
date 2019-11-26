# nsd1906_devweb_day06

## 制作添加模块页

```python
# webadmin/urls.py
    url(r'^addmodules/$', views.add_modules, name='add_modules')

# webadmin/views.py
from .models import HostGroup, Module

def add_modules(request):
    modules = Module.objects.all()
    return render(request, 'add_modules.html', {'modules': modules})

# templates/add_modules.html
{% extends 'basic.html' %}
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
        <div class="form-group">
            <input class="btn btn-primary" type="submit" value="提 交">
        </div>
    </form>
    <hr>
    <table class="table table-hover table-striped table-bordered h4">
        <thead class="bg-primary">
        <tr>
            <th>模块</th>
            <th>参数</th>
        </tr>
        </thead>
        {% for module in modules %}
            <tr>
                <td>{{ module.modulename }}</td>
                <td>
                    <ul class="list-unstyled">
                        {% for arg in module.args_set.all %}
                            <li>
                                {{ arg.arg_text }}
                            </li>
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

# 完成添加模块的功能
# webadmin/views.py
def add_modules(request):
    if request.method == 'POST':
        module = request.POST.get('module').strip()
        arg = request.POST.get('param').strip()
        if module:  # 如果模块名非空
            m = Module.objects.get_or_create(modulename=module)[0]
            if arg:  # 如果参数也是非空的
                m.args_set.get_or_create(arg_text=arg)

    modules = Module.objects.all()
    return render(request, 'add_modules.html', {'modules': modules})

```

## 实现执行任务页面

```python
# webadmin/urls.py
    url(r'^tasks/$', views.tasks, name='tasks'),

# webadmin/views.py
from .models import HostGroup, Module, Host
def tasks(request):
    hosts = Host.objects.all()
    groups = HostGroup.objects.all()
    modules = Module.objects.all()
    context = {'hosts': hosts, 'groups': groups, 'modules': modules}

    return render(request, 'tasks.html', context)

# templates/tasks.html
{% extends 'basic.html' %}
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
        <div class="tab-content h4" style="margin: 15px 0;">
            <div class="tab-pane active fade in form-group" id="server">
                <select class="form-control" name="ip">
                    <option value="">无</option>
                    {% for host in hosts %}
                        <option value="{{ host.ipaddr }}">
                            {{ host.hostname }}:{{ host.ipaddr }}
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
        <table class="table table-hover table-striped table-bordered h4">
        <thead class="bg-primary">
        <tr>
            <th>模块</th>
            <th>参数</th>
        </tr>
        </thead>
        {% for module in modules %}
            <tr>
                <td>
                    <div class="radio">
                        <label>
                            <input type="radio" name="module">
                            {{ module.modulename }}
                        </label>
                    </div>
                </td>
                <td>
                    <ul class="list-unstyled">
                        {% for arg in module.args_set.all %}
                            <li>
                                <div class="radio">
                                    <label>
                                        <input type="radio" name="args">
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
        <input class="btn btn-primary" type="submit" value="执 行">
    </div>
    </form>
{% endblock %}


# templates/index.html
<a href="{% url 'tasks' %}" target="_blank">
    <img width="150px" src="{% static 'imgs/linux.jpg' %}"><br>
    执行任务
</a>
```













