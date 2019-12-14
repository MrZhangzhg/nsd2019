import os
import time

print('starting...')

retval = os.fork()
if retval:
    print('In Parent')
    result = os.waitpid(-1, 1)  # 不挂起父进程
    print(result)   # (0, 0)
    time.sleep(30)
    print('Parent Done')
else:
    print('In Child')
    time.sleep(15)
    print('Child Done')


