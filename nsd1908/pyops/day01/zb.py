import os
import time

ret_val = os.fork()
if ret_val:
    print('in parent')
    time.sleep(30)
    print('parent done')
else:
    print('in child')
    time.sleep(15)
    print('child done')

# watch -n1 ps a   # 观察进程状态

