import os
import time

retval = os.fork()
if retval:
    print('parent')
    # 不挂起父进程，子进程是僵尸进程就处理掉，不是则跳过
    result = os.waitpid(-1, 1)
    print(result)  # result是(0, 0)
    time.sleep(20)
    print('parent done')
else:
    print('child')
    time.sleep(10)
    print('child done')

# watch -n1 ps a





