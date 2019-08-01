import random

num = random.randint(1, 100)  # 生成1到100之间的随机整数
counter = 0

while counter < 5:
    answer = int(input('guess: '))

    if answer > num:
        print('猜大了')
    elif answer < num:
        print('猜小了')
    else:
        print('猜对了')
        break

    counter += 1
else:   # 当循环被break，else语句不执行，否则执行
    print('answer:', num)
