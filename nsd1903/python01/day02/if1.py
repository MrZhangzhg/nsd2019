# if 3 > 0:
#     print('yes')
#     print('OK')
#
# if 3 > 10:
#     print('right')
#
# print('*' * 30)
#
# if 3 > 10:
#     print('right')
# else:
#     print('no')

##########################################
# 数据类型也可以作为判断条件
# 任何值为0的数字都表示False
if -0.0:
    print('0 => False')

if 0.01:
    print('none zero => True')

# 任何非空对象都表示True，空对象是False
if ' ':
    print('space is True')

if [1, 2, 3]:
    print('非空列表为真')

if ():
    print('空元组为False')

if {}:
    print('空字典为False')





