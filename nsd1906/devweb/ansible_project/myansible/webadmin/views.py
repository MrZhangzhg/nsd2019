from django.shortcuts import render, redirect
from .models import HostGroup, Module, Host, Args
from .adhoc2 import adhoc

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
    if request.method == 'POST':
        group = request.POST.get('group')
        ip = request.POST.get('ip')
        module = request.POST.get('module')
        args = request.POST.get('args')
        dest = None   # dest是ansible执行任务的目标
        # 如果group和ip都是非空的，那么在组上执行任务
        if group:
            dest = group
        elif ip:
            dest = ip

        if dest:  # 如果dest非空则扫行任务
            if module and args:   # 如果module和args也是非空的
                adhoc('ansible_cfg/dhosts.py', dest, module, args)

    hosts = Host.objects.all()
    groups = HostGroup.objects.all()
    modules = Module.objects.all()
    context = {'hosts': hosts, 'groups': groups, 'modules': modules}

    return render(request, 'tasks.html', context)

def del_arg(request, arg_id):
    arg = Args.objects.get(id=arg_id)
    arg.delete()

    return redirect('add_modules')
