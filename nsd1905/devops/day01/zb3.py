import os
import time

print('starting')

retval = os.fork()
if retval:
    print('parent')
    result = os.waitpid(-1, 1)  # 1表示不挂起父进程
    print(result)  # 返回值是(0, 0)
    time.sleep(5)
    print('parent done')
else:
    print('child')
    time.sleep(15)
    print('child done')
