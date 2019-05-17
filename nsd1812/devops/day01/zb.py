import os
import time

print('starting...')
retval = os.fork()
if retval:
    print('in parent, sleeping...')
    time.sleep(30)
    print('parent done')
else:
    print('in child, sleeping...')
    time.sleep(15)
    print('child done.')
    exit()
# watch -n1 ps a
