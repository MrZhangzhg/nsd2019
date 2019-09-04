# 取出2019-05-15 9点到12点之间的数据
import time

fname = 'myfile.txt'
t9 = time.strptime('2019-5-15 9:00:00', '%Y-%m-%d %H:%M:%S')
t12 = time.strptime('2019-5-15 12:00:00', '%Y-%m-%d %H:%M:%S')

# with open(fname) as fobj:
#     for line in fobj:
#         # 文件每行的前19个字符是时间字符串
#         t = time.strptime(line[:19], '%Y-%m-%d %H:%M:%S')
#         if t9 < t < t12:
#             print(line, end='')
###########################
with open(fname) as fobj:
    for line in fobj:
        t = time.strptime(line[:19], '%Y-%m-%d %H:%M:%S')
        if t > t12:
            break
        if t > t9:
            print(line, end='')
