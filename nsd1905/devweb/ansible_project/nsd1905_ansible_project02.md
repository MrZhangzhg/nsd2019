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



















