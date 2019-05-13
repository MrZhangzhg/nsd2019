import time

t9 = time.strptime('2019-05-13 09:00:00', '%Y-%m-%d %H:%M:%S')
t12 = time.strptime('2019-05-13 12:00:00', '%Y-%m-%d %H:%M:%S')

with open('mylog.log') as fobj:
    for line in fobj:
        tstr = line[:19]  # 每一行的前19个字符是时间
        # print(tstr)
        t = time.strptime(tstr, '%Y-%m-%d %H:%M:%S')  # 把字符串转找成时间
        if t9 < t < t12:
            print(line, end='')
