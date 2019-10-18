import os
import time

print('starting')

retval = os.fork()
if retval:
    print('parent')
    result = os.waitpid(-1, 0)  # 0表示挂起父进程，直到子进程结束后才继续
    print(result)  # 返回值是(子进程ID, 0)
    time.sleep(5)
    print('parent done')
else:
    print('child')
    time.sleep(15)
    print('child done')
