import os
import time

print('starting...')
retval = os.fork()
if retval:
    print('父进程')
    time.sleep(60)
else:
    print('子进程')
    time.sleep(15)
    exit()

print('done')

# watch -n1 ps a

