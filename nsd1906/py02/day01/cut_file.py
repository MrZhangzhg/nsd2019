import time

t9 = time.strptime('2019-5-15 09:00:00', '%Y-%m-%d %H:%M:%S')
t12 = time.strptime('2019-5-15 12:00:00', '%Y-%m-%d %H:%M:%S')

with open('my.log') as fobj:
    for line in fobj:
        t = time.strptime(line[:19], '%Y-%m-%d %H:%M:%S')
        if t > t12:
            break
        if t >= t9:
            print(line, end='')


# with open('my.log') as fobj:
#     for line in fobj:
#         t = time.strptime(line[:19], '%Y-%m-%d %H:%M:%S')
#         if t9 <= t <= t12:
#             print(line, end='')
