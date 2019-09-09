import os

print('starting...')
os.fork()  # 生成子进程，后续代码将在父子进程中同时运行
print('Hello World!')
