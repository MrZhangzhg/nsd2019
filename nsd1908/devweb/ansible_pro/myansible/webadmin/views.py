from django.shortcuts import render, redirect
from .models import HostGroup, Module, Host, Argument
from .adhoc2 import adhoc  # 把devops课程中的adhoc2当作模块导入

def index(request):
    return render(request, 'hosts.html')

def add_hosts(request):
    if request.method == 'POST':
        group = request.POST.get('group').strip()
        host = request.POST.get('host').strip()
        ip = request.POST.get('ip').strip()
        if group:  # 如果group非空
            g = HostGroup.objects.get_or_create(groupname=group)[0]
            if host and ip:  # 如果host和ip非空
                g.host_set.get_or_create(hostname=host, ipaddr=ip)

    groups = HostGroup.objects.all()
    return render(request, 'add_hosts.html', {'groups': groups})

def add_modules(request):
    if request.method == 'POST':
        module = request.POST.get('module').strip()
        arg = request.POST.get('param').strip()
        if module:
            m = Module.objects.get_or_create(modluename=module)[0]
            m.argument_set.get_or_create(arg_text=arg)

    modules = Module.objects.all()
    return render(request, 'add_modules.html', {'modules': modules})

def tasks(request):
    if request.method == 'POST':
        ip = request.POST.get('ip')
        group = request.POST.get('hostgroup')
        module = request.POST.get('mod')
        arg = request.POST.get('param')
        # 决定在主机还是组上执行任务，优先选组
        if group:
            dest = group
        elif ip:
            dest = ip
        else:
            dest = None

        if dest:  # 如果dest不是None
            adhoc(['ansi_cfg/dhosts.py'], dest, module, arg)

    hosts = Host.objects.all()
    groups = HostGroup.objects.all()
    modules = Module.objects.all()
    context = {'hosts': hosts, 'groups': groups, 'modules': modules}
    return render(request, 'tasks.html', context)

def del_arg(request, arg_id):
    arg = Argument.objects.get(id=arg_id)
    arg.delete()
    return redirect('add_modules')
