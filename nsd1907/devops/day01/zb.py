import os
import time

print('starting...')

retval = os.fork()
if retval:
    print('In Parent')
    time.sleep(45)
    print('Parent Done')
else:
    print('In Child')
    time.sleep(15)
    print('Child Done')

# watch -n1 ps a
