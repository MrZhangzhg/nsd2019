import os

print('starting')
for i in range(3):
    retval = os.fork()
    if not retval:  # 子进程的retval是0，表示假，取反为真
        print('hello world!')
        exit()  # 子进程遇到exit后，后续代码将不再执行

print('Done')
