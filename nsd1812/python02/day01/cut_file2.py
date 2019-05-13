from datetime import datetime

t9 = datetime.strptime('2019-05-13 09:00:00', '%Y-%m-%d %H:%M:%S')
t12 = datetime.strptime('2019-05-13 12:00:00', '%Y-%m-%d %H:%M:%S')

with open('mylog.log') as fobj:
    for line in fobj:
        tstr = line[:19]
        t = datetime.strptime(tstr, '%Y-%m-%d %H:%M:%S')
        if t9 < t < t12:
            print(line, end='')
