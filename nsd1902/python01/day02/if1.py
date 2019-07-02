if 3 > 0:
    print('yes')

if 3 < 0:
    print('ok')

if 3 < 0:
    print('ok')
else:
    print('not ok')

print('*' * 40)

# 数据类型也可以作为判断条件。任何值为0的数字都是False，非0为True
# 其他非空对象为True，空对象为False。
# None也表示False
if -0.0:
    print('0 is False')

if 101:
    print('101 is True')

if ' ':
    print('white space is True')

if '':
    print('empty string is False')

if []:
    print('empty list is False')

if [1, 2]:
    print('非空列表为True')

if ():
    print('empty tuple is False')

if {'name': 'bob'}:
    print('非空字典为True')

if not None:
    print('None is False')

if not 0:
    print('0 is False')

