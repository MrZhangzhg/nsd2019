import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

# since API is constructed for CLI it expects certain options to always be set, named tuple 'fakes' the args parsing options object
# 提供adhoc命令行选项
# connection设置连接方式，有3种：
# local表示在本机执行；ssh表示通过ssh连接到目标主机后执行
# smart表示智能选择，默认也是采用ssh执行
# forks是并发处理主机的数量
Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
options = Options(connection='smart', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)

# initialize needed objects
# DataLoader用于分析yaml / json / ini等格式的文件，将其转换成python的数据类型
loader = DataLoader() # Takes care of finding and reading yaml, json and ini files
# 保存加密密码
passwords = dict(vault_pass='secret')

# create inventory, use path to host config file as source or hosts in a comma separated string
# 主机清单文件，有两种写法：
# 一种是将管理的所有主机用逗号分隔，写成字符串
# 另一种是使用主机清单文件列表
# inventory = InventoryManager(loader=loader, sources='localhost,')
inventory = InventoryManager(loader=loader, sources=['myansible/hosts'])

# variable manager takes care of merging all the different sources to give you a unifed view of variables available in each context
# 变量
variable_manager = VariableManager(loader=loader, inventory=inventory)

# create datastructure that represents our play, including tasks, this is basically what our YAML loader does internally.
play_source = dict(  # 将配置创建成一个play源
        name="Ansible Play",
        hosts='webservers',  # 在哪些主机上执行命令
        gather_facts='no',
        tasks = [
            dict(action=dict(module='shell', args='id root'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
         ]
    )

# Create play object, playbook objects use .load instead of init or new methods,
# this will also automatically create the task objects from the info provided in play_source
# 创建play对象
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

# Run it - instantiate task queue manager, which takes care of forking and setting up all objects to iterate over host list and tasks
# 创建任务队列管理器，运行play
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
    # 清理环境
    if tqm is not None:
        tqm.cleanup()

    # Remove ansible tmpdir
    shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)


