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

# webadmin/views.py
def tasks(request):
    hosts = Host.objects.all()
    groups = HostGroup.objects.all()
    modules = Module.objects.all()
    context = {'hosts': hosts, 'groups': groups, 'modules': modules}
    return render(request, 'tasks.html', context)


# templates/tasks.html
{% extends 'base.html' %}
{% load static %}
{% block title %}Ansible Webadmin{% endblock %}
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















