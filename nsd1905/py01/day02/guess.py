import random

# 随机生成1－100之间的数字，可以包括1和100
number = random.randint(1, 100)

# while True:
while 1:
    answer = int(input('guess: '))
    if answer > number:
        print('猜大了')
    elif answer < number:
        print('猜小了')
    else:
        print('猜对了')
        break

print(number)
