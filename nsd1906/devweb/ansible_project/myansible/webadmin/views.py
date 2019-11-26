from django.shortcuts import render
from .models import HostGroup, Module, Host

# Create your views here.
def index(request):
    return render(request, 'webadmin.html')

def add_hosts(request):
    # 如果是表单的post方法，则取出相关的参数，创建主机和组
    if request.method == 'POST':
        group = request.POST.get('group').strip()
        host = request.POST.get('host').strip()
        ip = request.POST.get('ip').strip()
        if group:  # 如果group字符串非空
            # get_or_create返回的是元组: (组实例, True/False)
            g = HostGroup.objects.get_or_create(groupname=group)[0]
            if host and ip:  # 如果host和ip都非空
                g.host_set.get_or_create(hostname=host, ipaddr=ip)

    groups = HostGroup.objects.all()
    return render(request, 'add_hosts.html', {'groups': groups})

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

def tasks(request):
    hosts = Host.objects.all()
    groups = HostGroup.objects.all()
    modules = Module.objects.all()
    context = {'hosts': hosts, 'groups': groups, 'modules': modules}

    return render(request, 'tasks.html', context)
