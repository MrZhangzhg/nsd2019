import os

print('starting...')
retval = os.fork()  # 创建子进程，后续代码将同时在父子进程中执行
if retval:
    print('Hello from 父进程')
else:
    print('Hello from 子进程')

print('Hello from both')
