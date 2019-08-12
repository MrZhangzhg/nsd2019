import os
import time

print('starting...')
retval = os.fork()
if retval:
    print('父进程')
    time.sleep(30)
    print('父进程，醒了')
else:
    print('子进程')
    time.sleep(10)
    print('子进程，醒了')
    exit()

# watch -n1 ps a

