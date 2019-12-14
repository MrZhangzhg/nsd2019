import os
import time

print('starting...')

retval = os.fork()
if retval:
    print('In Parent')
    result = os.waitpid(-1, 0)  # 挂起父进程，直到子进程结束
    print(result)   # (子进程pid, 0)
    time.sleep(15)
    print('Parent Done')
else:
    print('In Child')
    time.sleep(15)
    print('Child Done')


