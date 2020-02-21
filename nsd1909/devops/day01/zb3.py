import os
import time

print('starting')

rc = os.fork()
if rc:
    print('父进程')
    # 不挂起父进程，如果子进程刚好是僵尸进程，则处理；如果不是，父进程也要继续向下执行
    result = os.waitpid(-1, 1)  # 子进程不是僵尸进程，返回值是: (0, 0)
    print(result)
    time.sleep(30)
    print('父进程结束')
else:
    print('子进程')
    time.sleep(15)
    print('子进程结束')
