from django.shortcuts import render
from .models import HostGroup, Module

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

