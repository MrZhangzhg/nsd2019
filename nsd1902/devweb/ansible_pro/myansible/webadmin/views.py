from django.shortcuts import render, redirect
from .models import HostGroup, Module, Host, Args
from . import adhoc2

# Create your views here.

def webadmin_index(request):
    return render(request, 'webadmin_index.html')

def add_hosts(request):
    if request.method == 'POST':
        group = request.POST.get('group').strip()
        host = request.POST.get('host').strip()
        ip = request.POST.get('ip').strip()
        if group:
            # get_or_create返回元组：(组实例，0/1)
            g = HostGroup.objects.get_or_create(groupname=group)[0]
            if host and ip:
                g.host_set.get_or_create(hostname=host, ipaddr=ip)

    groups = HostGroup.objects.all()
    return render(request, 'addhosts.html', {'groups': groups})

def add_modules(request):
    if request.method == 'POST':
        module = request.POST.get('module').strip()
        arg_text = request.POST.get('args').strip()
        if module:
            m = Module.objects.get_or_create(module_name=module)[0]
            if arg_text:
                m.args_set.get_or_create(arg_text=arg_text)

    modules = Module.objects.all()
    return render(request, 'addmodules.html', {'modules': modules})

def tasks(request):
    if request.method == 'POST':
        # 优先在对组执行任务，如果组为空，则设置执行任务的目标是主机
        target = request.POST.get('group')
        if not target:
            target = request.POST.get('host')

        module = request.POST.get('mod')
        args = request.POST.get('param')

        if target and module and args:
            adhoc2.adhoc(hosts_list=['ansicfg/dhosts.py'], hosts=target, module=module, args=args)

    hosts = Host.objects.all()
    groups = HostGroup.objects.all()
    modules = Module.objects.all()
    data = {'hosts': hosts, 'groups': groups, 'modules': modules}
    return render(request, 'tasks.html', data)

def del_arg(request, arg_id):
    arg = Args.objects.get(id=arg_id)
    arg.delete()

    return redirect('add_modules')
