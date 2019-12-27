from django.shortcuts import render, redirect
from .models import HostGroup, Module, Host, Argument
from . import adhoc2

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

def tasks(request):
    if request.method == 'POST':
        ip = request.POST.get('ip')
        group = request.POST.get('group')
        module = request.POST.get('module')
        args = request.POST.get('param')

        dest = None   # 设定执行目标
        if ip:  # 如果主机非空
            dest = ip
        elif group:
            dest = group

        if dest and module and args:  # 如果dest非空，模块和参数非空
            adhoc2.adhoc(['ansi_cfg/dhosts.py'], dest, module, args)

    hosts = Host.objects.all()
    groups = HostGroup.objects.all()
    modules = Module.objects.all()
    context = {'hosts': hosts, 'groups': groups, 'modules': modules}
    return render(request, 'tasks.html', context)

def del_arg(request, arg_id):
    args = Argument.objects.get(id=arg_id)
    args.delete()
    return redirect('add_modules')
