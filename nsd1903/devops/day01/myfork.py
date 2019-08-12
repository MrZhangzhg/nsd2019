import os

print('Starting...')
retval = os.fork()
if retval:
    print('Hello From Parent')
else:
    print('Hello From Child')

print('Hello From Both')
