from django.shortcuts import render, redirect
from .models import HostGroup, Module, Host, Argument
from .adhoc2 import adhoc

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

def add_modules(request):
    if request.method == 'POST':
        modulename = request.POST.get('module')
        args = request.POST.get('params')
        if modulename:  # 如果模块名非空
            module = Module.objects.get_or_create(modulename=modulename)[0]
            if args:  # 如果主机名和IP也非空
                module.argument_set.get_or_create(arg_text=args)

    modules = Module.objects.all()
    return render(request, 'add_modules.html', {'modules': modules})

def tasks(request):
    if request.method == 'POST':
        ip = request.POST.get('host')
        group = request.POST.get('group')
        module = request.POST.get('module')
        args = request.POST.get('params')
        # 判断，如果主机和组全选了，只在主机上执行任务
        dest = None  # 用于存储执行任务的目标，是主机？是组？
        if ip:
            dest = ip
        elif group:
            dest = group

        if dest:  # 如果dest不是None，则执行任务
            # 调用ansible的函数
            #(nsd1905)[root@room8pc16 myansible]# cp ../../devops/day03/adhoc2.py webadmin/
            if module and args:
                adhoc(['ansi_cfg/dhosts.py'], dest, module, args)

    hosts = Host.objects.all()
    groups = HostGroup.objects.all()
    modules = Module.objects.all()
    context = {'hosts': hosts, 'groups': groups, 'modules': modules}
    return render(request, 'tasks.html', context)

def del_arg(request, arg_id):
    args = Argument.objects.get(id=arg_id)
    args.delete()

    return redirect('add_modules')

