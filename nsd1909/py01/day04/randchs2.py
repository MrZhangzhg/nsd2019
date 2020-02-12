from random import choice
from string import ascii_letters, digits

# 定义在哪些字符中随机选取
zifuji = ascii_letters + digits

def suijizifu(n=8):
    # 定义保存结果的变量
    result = ''

    # 循环n次，每次选出随机字符，放到结果变量中
    for i in range(n):
        zifu = choice(zifuji)
        result += zifu

    return result

if __name__ == '__main__':
    a = suijizifu()
    print(a)
    print(suijizifu(4))
