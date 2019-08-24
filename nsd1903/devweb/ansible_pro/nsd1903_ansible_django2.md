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
```









