from django.shortcuts import render, redirect
from .models import Group, Module, Host, Args
from .adhoc2 import adhoc

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

def add_modules(request):
    # print(dir(request))  # 打印request所有的属性
    # print(request.method)  # 打印当前request的方法
    # print(request.POST)
    # print(request.GET)
    if request.method == 'POST':
        mod = request.POST.get('module').strip()
        args = request.POST.get('param').strip()
        if mod:
            module = Module.objects.get_or_create(modulename=mod)[0]
            if args:
                module.args_set.get_or_create(args_text=args)

    modules = Module.objects.all()
    return render(request, 'webadmin/add_modules.html', {'modules': modules})

def tasks(request):
    if request.method == 'POST':
        ip = request.POST.get('host')
        group = request.POST.get('group')
        module = request.POST.get('module')
        args = request.POST.get('args')
        if group:
            dest = group
        elif ip:
            dest = ip
        else:
            dest = None

        if dest:
            if module and args:  # 如果模块和参数非空
                adhoc(['ansi_cfg/dhosts.py'], dest, module, args)

    hosts = Host.objects.all()
    groups = Group.objects.all()
    modules = Module.objects.all()
    objs = {'hosts': hosts, 'groups': groups, 'modules': modules}
    return render(request, 'webadmin/tasks.html', objs)

def del_args(request, args_id):
    args = Args.objects.get(id=args_id)
    args.delete()

    return redirect('add_modules')
