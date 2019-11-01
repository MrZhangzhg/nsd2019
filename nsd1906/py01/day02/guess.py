import random

number = random.randint(1, 10)  # 随机生成1－10内的整数
counter = 0

while counter < 5:
    counter += 1
    answer = int(input('guess(1-10): '))
    if answer > number:
        print('猜大了')
    elif answer < number:
        print('猜小了')
    else:
        print('猜对了')
        break
else:
    # 循环也有else语句，如果循环被break，else不执行，否则执行
    print('这个数是: %s' % number)
