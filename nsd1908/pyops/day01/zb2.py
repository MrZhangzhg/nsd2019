import os
import time

ret_val = os.fork()

if ret_val:
    print('父进程')
    result = os.waitpid(-1, 0)  # 挂起父进程，直到处理完子进程
    print(result)   # (子进程pid, 0)
    time.sleep(5)
else:
    print('子进程')
    time.sleep(10)
    print('child done')

# watch -n1 ps a   # 观察进程状态
