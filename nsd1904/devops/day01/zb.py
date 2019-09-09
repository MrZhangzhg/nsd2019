import time
import os

retval = os.fork()
if retval:
    print('parent')
    time.sleep(40)
    print('parent done')
else:
    print('child')
    time.sleep(10)
    print('child done')
    exit()
