import random
from string import ascii_letters, digits

all_chs = ascii_letters + digits  # 从大小写字母和数字中选取字符

def mk_pwd(n=8):
    result = ''   # 结果保存到变量result中

    for i in range(n):
        ch = random.choice(all_chs)  # 随机选出一个字符
        result += ch  # 将选出的字符与result拼接

    return result

if __name__ == '__main__':
    a = mk_pwd()
    b = mk_pwd(4)
    print(a)
    print(b)
