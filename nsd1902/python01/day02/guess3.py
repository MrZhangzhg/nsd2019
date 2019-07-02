'用户猜对数字，不再显示答案；用户4次全错，才显示答案'
import random

num = random.randint(1, 10)
counter = 0

while counter < 4:
    answer = int(input('guess(1-10): '))
    if answer > num:
        print('猜大了')
    elif answer < num:
        print('猜小了')
    else:
        print('猜对了')
        break
    counter += 1
else:   # 如果循环被break，else就不执行了，否则执行
    print('answer is: %s' % num)
