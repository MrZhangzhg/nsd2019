import random

num = random.randint(1, 100)  # 随机取出100以内的整数，包括1和100
running = True

while running:
    answer = int(input('guess(1-100): '))
    if answer > num:
        print('猜大了')
    elif answer < num:
        print('猜小了')
    else:
        print('猜对了')
        running = False
