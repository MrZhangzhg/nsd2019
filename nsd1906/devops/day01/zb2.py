import os
import time

retval = os.fork()
if retval:
    print('parent')
    # 挂起父进程，处理完变成僵尸进程的子进程后才继续
    result = os.waitpid(-1, 0)
    print(result)  # result是(子进程PID, 0)
    time.sleep(10)
    print('parent done')
else:
    print('child')
    time.sleep(15)
    print('child done')

# watch -n1 ps a
