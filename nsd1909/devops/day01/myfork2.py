import os

print('starting')

for i in range(3):
    rc = os.fork()
    # if rc == 0:
    if not rc:  # rc的值如果为0，表示假，取反为真；如果值为非0，表示真，取反为假
        print('Hello World!')
        exit()  # 进程遇到exit后，将彻底结束

print('Done')
