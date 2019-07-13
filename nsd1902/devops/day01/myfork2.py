import os

print('starting...')
retval = os.fork()
if retval:  # 父进程的retval是非0值
    print('in partent')
else:
    print('in child')

print('hello from both')

