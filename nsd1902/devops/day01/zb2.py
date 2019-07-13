import os
import time

print('starting...')
retval = os.fork()
if retval:
    print('父进程')
    time.sleep(10)
    print('go on')
    print(os.waitpid(-1, 0))  # 挂起父进程
    time.sleep(5)
else:
    print('子进程')
    time.sleep(15)
    exit()

print('done')





