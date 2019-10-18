import os

print('starting....')
retval = os.fork()
if retval:
    print('Hello from parent')
else:
    print('Hello from child')

print('Hello from both!')
