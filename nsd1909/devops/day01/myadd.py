import os
import time

def add():
    result = 0
    for i in range(1, 20000001):
        result += i
    print(result)

if __name__ == '__main__':
    start = time.time()
    # add()
    # add()
    for i in range(2):
        rc = os.fork()
        if not rc:
            add()
            exit()
    os.waitpid(-1, 0)   # 挂起父进程，直到一个子进程结束，才继续向后执行
    os.waitpid(-1, 0)   # 因为有两个子进程，所以需要两个waitpid
    end = time.time()
    print(end-start)
