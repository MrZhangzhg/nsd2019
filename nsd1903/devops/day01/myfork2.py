import os

for i in range(3): # [0, 1, 2]
    retval = os.fork()
    if not retval:
        print('Hello World!')
        exit()

print('Done')
