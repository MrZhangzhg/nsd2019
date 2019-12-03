import random

num = random.randint(1, 100)  # 生成1-100之间的随机数
counter = 0   # 计数器

while counter < 7:
    counter += 1
    answer = int(input('guess: '))

    if answer == num:
        print('猜对了')
        break

    if answer > num:
        print('猜大了')
    else:
        print('猜小了')
else:
    print('正确答案是: %s' % num)



