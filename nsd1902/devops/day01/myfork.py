import os

print('Starting...')
os.fork()  # 生成子进程
# 后续代码在父子进程中都要执行
print('Hello World!')

