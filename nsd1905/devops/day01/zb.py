import os
import time


print('starting...')
retval = os.fork()
if retval:
    print('parent')
    time.sleep(30)
    print('parent done')
else:
    print('child')
    time.sleep(10)
    print('child done')
