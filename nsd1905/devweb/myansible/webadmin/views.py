from django.shortcuts import render
from .models import HostGroup

# Create your views here.
def index(request):
    return render(request, 'webadmin.html')

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
