# 猜数程序，7次机会，猜对不用输出正确答案；7次全错，输出正确答案
import random

num = random.randint(1, 100)
i = 0

while i < 7:
    answer = int(input('guess: '))
    if answer == num:
        print('猜对了')
        break
    elif answer > num:
        print('猜大了')
    else:
        print('猜小了')

    i += 1
else:   # 当循环被break，else不执行，否则执行
    print('答案是: %s' % num)
