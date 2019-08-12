import os
import time

print('starting...')
retval = os.fork()
if retval:
    print('父进程')
    time.sleep(5)
    print('父进程，继续')
    result = os.waitpid(-1, 1)  # 不挂起父进程，处理子进程
    print(result)  # 子进程不是僵尸进程，返回(0, 0)
    time.sleep(10)
    print('父进程，结束')
else:
    print('子进程')
    time.sleep(10)
    print('子进程，结束')


