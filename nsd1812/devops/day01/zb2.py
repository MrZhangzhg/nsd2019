import os
import time

retval = os.fork()
if retval:
    print('in parent')
    result = os.waitpid(-1, 0)  # 挂起父进程，直到子进程结束才会继续
    print(result)
    time.sleep(10)
    print('parent done')
else:
    print('in child')
    time.sleep(10)
    print('child done')
    exit()


