from django.shortcuts import render, redirect
from .models import HostGroup, Module, Argument, Host

import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

def adhoc(sources, hosts, module, args):
    Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
    options = Options(connection='ssh', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)
    loader = DataLoader()
    passwords = dict()
    inventory = InventoryManager(loader=loader, sources=sources)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_source =  dict(
            name = "Ansible Play",
            hosts = hosts,
            gather_facts = 'no',
            tasks = [
                dict(action=dict(module=module, args=args), register='shell_out'),
             ]
        )

    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)
    tqm = None
    try:
        tqm = TaskQueueManager(
                  inventory=inventory,
                  variable_manager=variable_manager,
                  loader=loader,
                  options=options,
                  passwords=passwords,
              )
        result = tqm.run(play)
    finally:
        if tqm is not None:
            tqm.cleanup()

        shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)



def index(request):
    return render(request, 'index.html')

def mainpage(request):
    return render(request, 'mainpage.html')

def addhosts(request):
    if request.method == 'POST':
        groupname = request.POST.get('group').strip()
        hostname = request.POST.get('host').strip()
        ip = request.POST.get('ip').strip()
        if groupname:
            # get_or_create返回的是元组(组实例, True|False)
            group = HostGroup.objects.get_or_create(groupname=groupname)[0]
            if hostname and ip:
                group.host_set.get_or_create(hostname=hostname, ipaddr=ip)

    groups = HostGroup.objects.all()
    return render(request, 'addhosts.html', {'groups': groups})

def addmodules(request):
    if request.method == 'POST':
        modulename = request.POST.get('module').strip()
        argument = request.POST.get('args').strip()
        if modulename:
            module = Module.objects.get_or_create(modulename=modulename)[0]
            if argument:
                module.argument_set.get_or_create(arg_text=argument)

    modules = Module.objects.all()
    return render(request, 'addmodules.html', {'modules': modules})

def delarg(request, arg_id):
    argument = Argument.objects.get(id=arg_id)
    argument.delete()
    return redirect('addmodules')

def tasks(request):
    if request.method == 'POST':
        hostname = request.POST.get('host')
        groupname = request.POST.get('group')
        module = request.POST.get('module')
        arg = request.POST.get('argument')
        if hostname:
            dest = hostname
        else:
            dest = groupname

        adhoc(['ansicfg/dhosts.py'], dest, module, arg)

    groups = HostGroup.objects.all()
    modules = Module.objects.all()
    hosts = Host.objects.all()
    context = {'groups': groups, 'modules': modules, 'hosts': hosts}
    return render(request, 'tasks.html', context)
