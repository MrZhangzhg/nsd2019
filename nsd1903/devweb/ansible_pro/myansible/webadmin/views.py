from django.shortcuts import render
from .models import Group

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

