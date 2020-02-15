import time

# 定义9点和12点的时间
t9 = time.strptime('2019-05-15 09:00:00', '%Y-%m-%d %H:%M:%S')
t12 = time.strptime('2019-05-15 12:00:00', '%Y-%m-%d %H:%M:%S')

# 遍历文件，时间在t9和t12之间的行，打印
with open('mylog.log') as fobj:
    for line in fobj:
        t = time.strptime(line[:19], '%Y-%m-%d %H:%M:%S')
        # if t9 <= t <= t12:
        #     print(line, end='')
        if t > t12:
            break
        if t >= t9:
            print(line, end='')
