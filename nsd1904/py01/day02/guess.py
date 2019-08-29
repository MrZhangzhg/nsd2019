import random

counter = 0
num = random.randint(1, 100)

while counter < 7:   # 最多5次机会
    counter += 1
    answer = int(input('guess: '))
    if answer < num:
        print('猜小了')
    elif answer > num:
        print('猜大了')
    else:
        print('猜对了')
        break
else:   # 循环被break就不执行else，否则执行
    print('answer is: %s' % num)
