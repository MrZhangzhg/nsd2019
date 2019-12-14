import os

print('starting...')

retval = os.fork()

if retval:
    print('Hello from Parent')
else:
    print('Hello from Child')

print('Hello from Both!')
