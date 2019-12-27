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











