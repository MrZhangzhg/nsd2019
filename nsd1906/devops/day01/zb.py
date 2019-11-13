import os
import time

retval = os.fork()
if retval:
    print('parent')
    time.sleep(45)
    print('parent done')
else:
    print('child')
    time.sleep(15)
    print('child done')

# watch -n1 ps a
