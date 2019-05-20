import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

# since API is constructed for CLI it expects certain options to always be set, named tuple 'fakes' the args parsing options object
# 此处定义了执行ansible命令时的选项
# connection定义连接方式，local表示本机，ssh表示ssh，smart表示自动选择
# module_path指定自定义的模块位置
# forks指定启动的进程数目
# become：如果使用普通用户远程登陆服务器，那么切换成其他用户该怎么切换
# check: 不真正执行操作，而是预言操作的结果
# diff 显示修改小文件前后的变化
Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
options = Options(connection='ssh', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)

# initialize needed objects
# DataLoader用于查找并解析yaml、json、ini文件，把它们转换成python的数据类型
loader = DataLoader() # Takes care of finding and reading yaml, json and ini files
# 设置密码
passwords = dict()

# create inventory, use path to host config file as source or hosts in a comma separated string
# 定义主机清单，可以将各主机用逗号隔开的字符串，也可以指定文件路径列表
# inventory = InventoryManager(loader=loader, sources='localhost,')
inventory = InventoryManager(loader=loader, sources=['myansible/hosts'])

# variable manager takes care of merging all the different sources to give you a unifed view of variables available in each context
# 变量管理器
variable_manager = VariableManager(loader=loader, inventory=inventory)

# create datastructure that represents our play, including tasks, this is basically what our YAML loader does internally.
play_source =  dict(
        name = "Ansible Play",  # play的名字
        hosts = 'webservers',    # 指定在哪些主机上执行命令
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
         ]
    )

# Create play object, playbook objects use .load instead of init or new methods,
# this will also automatically create the task objects from the info provided in play_source
# 通过上面的配置，创建一个play
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

# Run it - instantiate task queue manager, which takes care of forking and setting up all objects to iterate over host list and tasks
# 创建任管理器，执行play
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
