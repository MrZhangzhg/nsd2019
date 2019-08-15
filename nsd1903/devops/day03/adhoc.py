import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

# since API is constructed for CLI it expects certain options to always be set, named tuple 'fakes' the args parsing options object
# options是在执行命令时，指定的选项，这些选项大部分采用默认值即可
# connection选项指的是连接方式
# local表示本机执行，ssh表示通过ssh远程连接执行，smart表示智能判断
Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
options = Options(connection='ssh', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)

# initialize needed objects
# Dataloader用于将yaml / json等文件转换成python的数据类型
loader = DataLoader() # Takes care of finding and reading yaml, json and ini files
# 用于保存各种密码
passwords = dict()

# create inventory, use path to host config file as source or hosts in a comma separated string
# 主机清单文件，有两种表示方式
# 一种是将各个主机用逗号分开的字符串
# 另外一种是将主机清单文件路径保存到列表中
# inventory = InventoryManager(loader=loader, sources='localhost,')
inventory = InventoryManager(loader=loader, sources=['myansible/hosts',])

# variable manager takes care of merging all the different sources to give you a unifed view of variables available in each context
# 定义参数
variable_manager = VariableManager(loader=loader, inventory=inventory)

# create datastructure that represents our play, including tasks, this is basically what our YAML loader does internally.
play_source =  dict(
    name="Ansible Play",
    hosts='webservers',  # 在哪些目标执行指令
    gather_facts='no',   # 执行指令前不收集目标主机信息
    tasks=[  # 调用哪个模块，添加哪些参数
        dict(action=dict(module='shell', args='ls'), register='shell_out'),
        dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
     ]
)

# Create play object, playbook objects use .load instead of init or new methods,
# this will also automatically create the task objects from the info provided in play_source
# 创建Play的实例
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

# Run it - instantiate task queue manager, which takes care of forking and setting up all objects to iterate over host list and tasks
tqm = None
# 创建任务队列管理器实例，用于调用play
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
    if tqm is not None:
        tqm.cleanup()

    # Remove ansible tmpdir
    shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)
