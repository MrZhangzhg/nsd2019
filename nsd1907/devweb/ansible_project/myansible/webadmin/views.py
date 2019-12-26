from django.shortcuts import render
from .models import HostGroup

# Create your views here.
def index(request):
    return render(request, 'hosts.html')

def add_hosts(request):
    # 如果是post方法，则添加主机
    if request.method == 'POST':
        # 将用户提交字段的额外空白字符串移除
        group = request.POST.get('group').strip()
        host = request.POST.get('host').strip()
        ip = request.POST.get('ip').strip()
        if group:  # 如果group是非空的则取出或创建组实例
            g = HostGroup.objects.get_or_create(groupname=group)[0]
            if host and ip:  # 如果host和ip都是非空的，才能创建主机
                g.host_set.get_or_create(hostname=host, ip_addr=ip)

    groups = HostGroup.objects.all()
    return render(request, 'add_hosts.html', {'groups': groups})
