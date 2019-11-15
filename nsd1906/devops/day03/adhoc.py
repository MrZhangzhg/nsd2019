import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

# since API is constructed for CLI it expects certain options to always be set, named tuple 'fakes' the args parsing options object
# option用于定义选项，绝大部分使用默认值即可
# connection是连接方式，有三种：
# local: 本地执行指令；ssh: 通过ssh连接执行；smart：自动判断
# fork指定可以创建的进程数，每个进程连接一台服务器
Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
# options = Options(connection='local', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)
options = Options(connection='smart', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)

# initialize needed objects
# DataLoader负责将yaml、json、ini等文件转换成python的数据类型
loader = DataLoader() # Takes care of finding and reading yaml, json and ini files
# 存储加密密码
passwords = dict(vault_pass='secret')

# create inventory, use path to host config file as source or hosts in a comma separated string
# 主机清单，有两种形式，一种是用逗号将所有的主机分隔的字符串
# 另一种形式，是使用列表将主机清单文件位置包含
# inventory = InventoryManager(loader=loader, sources='localhost,')
inventory = InventoryManager(loader=loader, sources=['myansible/hosts'])

# variable manager takes care of merging all the different sources to give you a unifed view of variables available in each context
# 用于保存变量的管理器
variable_manager = VariableManager(loader=loader, inventory=inventory)

# create datastructure that represents our play, including tasks, this is basically what our YAML loader does internally.
# 创建代表play的数据结构
play_source=dict(
        name="Ansible Play",
        hosts='webservers',  # 在哪些主机上执行任务
        gather_facts='no',
        tasks=[
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
         ]
    )

# Create play object, playbook objects use .load instead of init or new methods,
# this will also automatically create the task objects from the info provided in play_source
# 创建一个play对象
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

# Run it - instantiate task queue manager, which takes care of forking and setting up all objects to iterate over host list and tasks
# 创建任务队列管理器，用于调度执行play
tqm = None
try:
    tqm = TaskQueueManager(
              inventory=inventory,
              variable_manager=variable_manager,
              loader=loader,
              options=options,
              passwords=passwords,
          )
    result = tqm.run(play) # most interesting data for a play is actually sent to the callback's methods
finally:
    # we always need to cleanup child procs and the structres we use to communicate with them
    # 清理执行后的环境，如删除临时文件
    if tqm is not None:
        tqm.cleanup()

    # Remove ansible tmpdir
    shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)