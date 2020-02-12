from random import choice

# 定义在哪些字符中随机选取
zifuji = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
# 定义保存结果的变量
result = ''

# 循环n次，每次选出随机字符，放到结果变量中
for i in range(8):
    zifu = choice(zifuji)
    result += zifu

print(result)
