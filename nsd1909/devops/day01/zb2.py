import os
import time

print('starting')

rc = os.fork()
if rc:
    print('父进程')
    # 挂起父进程，处理僵尸进程后才会继续执行
    result = os.waitpid(-1, 0)  # 处理僵尸进程后的返回值是: (子进程pid, 0)
    print(result)
    time.sleep(15)
    print('父进程结束')
else:
    print('子进程')
    time.sleep(15)
    print('子进程结束')

