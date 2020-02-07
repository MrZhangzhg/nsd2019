import shutil
import ansible.constants as C
from collections import namedtuple
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.playbook.play import Play
from ansible.vars.manager import VariableManager

def adhoc(sources, hosts, module, args):
    # Options是在执行ansible临时命令时，提供的选项，需要了解的选项有
    # connection是连接方式，local表示在本机执行，ssh表示ssh执行，smart表示自动选择
    # forks指的是一次同时向多少台主机发送指令
    Options = namedtuple('Options',
                         ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
    options = Options(connection='smart', module_path=['/to/mymodules'], forks=10, become=None, become_method=None,
                      become_user=None, check=False, diff=False)

    # DataLoader用于解析json/ini/yaml等文件，将其转换成python的数据类型
    loader = DataLoader()
    # 设置密码
    passwords = dict(vault_pass='secret')

    # 主机清单文件，表示方式有两种
    # 一种是将各个主机用冒号分隔，成为一个字符串
    # 另外一种方式是使用主机路径列表
    # inventory = InventoryManager(loader=loader, sources='localhost,')
    inventory = InventoryManager(loader=loader, sources=sources)

    # 变量管理
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # 创建play源
    play_source = dict(
        name="Ansible Play",
        hosts=hosts,  # 在哪台主机上执行任务
        gather_facts='no',
        tasks=[
            dict(action=dict(module=module, args=args), register='shell_out'),
            # dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
        ]
    )

    # 创建play对象
    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

    # 通过任务队列管理器执行play
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

if __name__ == '__main__':
    adhoc(['myansible/hosts'], 'dbservers', 'yum', 'name=vsftpd state=latest')
