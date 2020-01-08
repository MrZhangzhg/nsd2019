import time

# 分别定义9点和12点的时间
t9 = time.strptime('2019-05-15 09:00:00', '%Y-%m-%d %H:%M:%S')
t12 = time.strptime('2019-05-15 12:00:00', '%Y-%m-%d %H:%M:%S')

# 打开文件，取出每一行的时间，如果时间在t9到t12之间，那么打印它
with open('weblog.txt') as fobj:
    for line in fobj:
        t = time.strptime(line[:19], '%Y-%m-%d %H:%M:%S')
        # if t9 <= t <= t12:
        #     print(line, end='')
        if t > t12:
            break
        if t >= t9:
            print(line, end='')

