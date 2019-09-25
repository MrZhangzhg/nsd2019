# nsd1904_devweb_ansible_project2

## 添加模块功能

1. url

```shell
# webadmin/urls.py
    url(r'^addmodules/$', views.add_modules, name='add_modules'),
```

2. 视图函数

```shell
# webadmin/views.py
def add_modules(request):
    if request.method == 'POST':
        mod_name = request.POST.get('mod').strip()
        arg = request.POST.get('param').strip()
        if mod_name:
            module = Module.objects.get_or_create(modulename=mod_name)[0]
            if arg:
                module.argument_set.get_or_create(arg_text=arg)

    modules = Module.objects.all()
    return render(request, 'add_modules.html', {'modules': modules})
```

3. 模板

```shell
{% extends 'base.html' %}
{% load static %}
{% block title %}添加模块{% endblock %}
{% block content %}
    <div class="row h4">
        <div class="col-sm-12">
            <form action="" class="form-inline" method="post">
                {% csrf_token %}
                <div class="form-group">
                    <label>模块：</label>
                    <input class="form-control" type="text" name="mod">
                </div>
                <div class="form-group">
                    <label>参数：</label>
                    <input class="form-control" type="text" name="param">
                </div>
                <div class="form-group">
                    <input class="btn btn-primary" type="submit" value="提 交">
                </div>
            </form>
        </div>
    </div>
    <hr>
    <table class="table table-bordered table-hover table-striped h4">
        <thead>
            <tr class="bg-primary text-center">
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
{% endblock %}
```

4. 修改templates/index.html中“添加模块”的超链接

```shell
        <a href="{% url 'add_modules' %}" target="_blank">
```

5. 测试

## 编写“执行任务”页面

1. url

```shell
# webadmin/urls.py
    url(r'^tasks/$', views.tasks, name='tasks'),
```

2. 视图函数

```shell
# webadmin/views.py
def tasks(request):
    groups = HostGroup.objects.all()
    hosts = Host.objects.all()
    modules = Module.objects.all()
    context = {'hosts': hosts, 'groups': groups, 'modules': modules}
    return render(request, 'tasks.html', context)
```

3. 模板

```shell
# templates/tasks.html
{% extends 'base.html' %}
{% load static %}
{% block title %}执行任务{% endblock %}
{% block content %}
    {{ groups }}
    {{ hosts }}
    {{ modules }}
{% endblock %}
```

4. 修改templates/index.html中“执行任务”的超链接

```shell
        <a href="{% url 'tasks' %}" target="_blank">
```





