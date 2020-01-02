import random

num = random.randint(1, 100)  # 生成一个1到100之间的整数，包括1和100
counter = 0

while counter < 7:
    answer = int(input('guess: '))
    if answer > num:
        print('猜大了')
    elif answer < num:
        print('猜小了')
    else:
        print('猜对了')
        break
    counter += 1
else:  # 循环被break，else就不执行了；否则执行
    print('正确答案是:', num)
