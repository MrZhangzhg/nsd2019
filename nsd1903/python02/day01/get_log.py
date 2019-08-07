"""取出文件中指定时间段9:00-12:00的数据

myfile.txt
2019-05-15 08:10:01 aaaa
2019-05-15 08:32:00 bbbb
2019-05-15 09:01:02 cccc
2019-05-15 09:28:23 dddd
2019-05-15 10:42:58 eeee
2019-05-15 11:08:00 ffff
2019-05-15 12:35:03 gggg
2019-05-15 13:13:24 hhhh
"""

import time

# 创建9点和12点的9元组时间对象
t9 = time.strptime('2019-05-15 09:00:00', '%Y-%m-%d %H:%M:%S')
t12 = time.strptime('2019-05-15 12:00:00', '%Y-%m-%d %H:%M:%S')

##################################
# 初步实现
# 读取文件的每一行，取出前19个字符，转找成9元组时间对象
# 如果时间在t9到t12之间，则打印
# with open('myfile.txt') as fobj:
#     for line in fobj:
#         t = time.strptime(line[:19], '%Y-%m-%d %H:%M:%S')
#         if t9 < t < t12:
#             print(line, end='')
##################################
# 改善代码
# 初步实现中，文件所有的行都需要读取，但是12点之后的行没有必要
with open('myfile.txt') as fobj:
    for line in fobj:
        t = time.strptime(line[:19], '%Y-%m-%d %H:%M:%S')
        if t > t12:
            break
        if t > t9:
            print(line, end='')

