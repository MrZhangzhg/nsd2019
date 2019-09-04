from datetime import datetime

fname = 'myfile.txt'
t9 = datetime.strptime('2019-5-15 9:00:00', '%Y-%m-%d %H:%M:%S')
t12 = datetime.strptime('2019-5-15 12:00:00', '%Y-%m-%d %H:%M:%S')

with open(fname) as fobj:
    for line in fobj:
        t = datetime.strptime(line[:19], '%Y-%m-%d %H:%M:%S')
        if t > t12:
            break
        if t > t9:
            print(line, end='')
