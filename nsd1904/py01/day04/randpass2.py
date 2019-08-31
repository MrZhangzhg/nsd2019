from random import choice
from string import ascii_letters, digits

# 全局变量，从定义开始到程序结束，一直可见可用
all_chs = ascii_letters + digits

def randpass(n=8):
    result = ''
    for i in range(n):
        ch = choice(all_chs)
        result += ch

    return result

if __name__ == '__main__':
    print(randpass())
    print(randpass(4))
