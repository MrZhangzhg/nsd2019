import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C


# since API is constructed for CLI it expects certain options to always be set, named tuple 'fakes' the args parsing options object
# 通过命名的元组配置ansible命令的选项
# connection设置连接方式，local表示本地执行，ssh表示通过ssh远程执行，smart表示智能选择
Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
options = Options(connection='smart', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)

# initialize needed objects
# ansible应用到了大量的yaml/ini/json等格式的文件，这些文件需要转换成python的数据类型
# Dataloader用于格式转换
loader = DataLoader() # Takes care of finding and reading yaml, json and ini files
# passwords用于存储各类密码
passwords = dict()

# create inventory, use path to host config file as source or hosts in a comma separated string
# 用于创建主机清单，可以有两种方式，一种是把所有的主机用逗号隔开，写在一个大字符串中
# 另一种方式，是提供主机清单文件名的列表
# inventory = InventoryManager(loader=loader, sources='localhost,')
inventory = InventoryManager(loader=loader, sources=['myansible/hosts'])

# variable manager takes care of merging all the different sources to give you a unifed view of variables available in each context
# 配置变量管理器
variable_manager = VariableManager(loader=loader, inventory=inventory)

# create datastructure that represents our play, including tasks, this is basically what our YAML loader does internally.
# 创建代表play的数据结构
play_source = dict(
        name="Ansible Play",
        hosts='webservers',  # 在哪些主机上执行任务
        gather_facts='no',   # 不收集主机信息
        tasks=[
            dict(action=dict(module='shell', args='id root'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
         ]
    )

# Create play object, playbook objects use .load instead of init or new methods,
# this will also automatically create the task objects from the info provided in play_source
# 创建一个play
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

# Run it - instantiate task queue manager, which takes care of forking and setting up all objects to iterate over host list and tasks
# 创建任务队列管理器实例
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
    if tqm is not None:
        tqm.cleanup()

    # Remove ansible tmpdir
    shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)
