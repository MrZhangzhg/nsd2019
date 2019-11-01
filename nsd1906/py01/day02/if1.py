# py_str = 'Python'
#
# if 'th' in py_str:
#     print('th在Python中')
#
# if -0.0:
#     print('值为0的数字为假')
#
# if ' ':
#     print('空格也是一个字符，为真')
#
# if []:
#     print('空列表为假')
#
# if (1, 2):
#     print('非空元组，为真')
#
# if {'name': 'bob'}:
#     print('非空字典，为真')
#
# if not {}:
#     print('空字典为假，取反为真')
#
# if not None:
#     print('None表示空对象，类似于mysql中的null，为假，取反为真')

a = 10
b = 20
if a < b:
    s1 = a
else:
    s1 = b
print('s1=%s' % s1)

s2 = a if a < b else b
print('s2=%s' % s2)





