import os
import time

retval = os.fork()
if retval:
    print('in parent')
    result = os.waitpid(-1, 1)  # 不挂起父进程
    print(result)
    time.sleep(30)
    print('parent done')
else:
    print('in child')
    time.sleep(10)
    print('child done')
    exit()
