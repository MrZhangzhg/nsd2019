import random

counter = 0
number = random.randint(1, 10)

while counter < 5:
    counter += 1

    answer = int(input('guess: '))
    if answer > number:
        print('猜大了')
    elif answer < number:
        print('猜小了')
    else:
        print('猜对了')
        break
else:  # 循环被break，else语句不执行
    print('数字是: %s' % number)
