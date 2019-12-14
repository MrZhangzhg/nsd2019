import os

print('starting...')

for i in range(3):
    retval = os.fork()
    if not retval:
        print('Hello World!')
        exit()

print('Done')
