import os

for i in range(6):
    retval = os.fork()
    if not retval:
        print('Hello World!')
        exit()  # 进程遇到exit将会完全结束
