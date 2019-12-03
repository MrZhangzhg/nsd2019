# if 3 > 0:
#     print('3比0大')
#
# if 'to' in 'python':
#     print('to在python中')
# else:
#     print('to不在python中')
#
# if -0.0:
#     print('任何值为0的数字都是False')
#
# if 0.01:
#     print('非0为True')
#
# if ' ':
#     print('空格也是一个字符，非空为True')
#
# if [10, 20]:
#     print('非空列表为True')
#
# if ():
#     print('空元组为False')
#
# if {'name': 'tom'}:
#     print('非空字典为True')
#
# if not None:
#     print('None为False，取反为True')
#
# if not 0:
#     print('0为False，取反为True')

# a = 10
# b = 20
# if a < b:
#     smaller = a
# else:
#     smaller = b
# print(smaller)
# 以上写法可以简化为
a = 10
b = 20
smaller = a if a < b else b
print(smaller)






