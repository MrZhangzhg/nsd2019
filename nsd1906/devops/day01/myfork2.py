import os

print('starting...')

for i in range(3):
    retval = os.fork()
    if not retval:
        print('Hello World!')
        exit()  # 进程遇到exit，彻底结束

print('Done')
